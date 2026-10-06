"""Validate subscription-edition run snapshots exported from the control sheet."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

STAGES = [
    "broad_research",
    "research_analysis",
    "chapter_blueprint",
    "research_mapping",
    "deep_research",
    "chapter_writing",
]

UPSTREAM = {
    "broad_research": [],
    "research_analysis": ["broad_research"],
    "chapter_blueprint": ["broad_research", "research_analysis"],
    "research_mapping": ["broad_research", "chapter_blueprint"],
    "deep_research": ["broad_research", "research_mapping"],
    "chapter_writing": ["research_mapping", "deep_research"],
}

STATES = {
    "READY",
    "RUNNING",
    "AWAITING_APPROVAL",
    "AWAITING_BLUEPRINT_SELECTION",
    "AWAITING_VISUAL_REVIEW",
    "PAUSED_LIMIT",
    "BLOCKED",
    "COMPLETED",
    "CANCELLED",
}

APPROVAL_FIELDS = {stage: f"approved_{stage}_doc_id" for stage in STAGES}
MEDIUM_ROLES = {"research_analysis", "chapter_blueprint", "chapter_writing", "canonical_chapter_worker"}
LOW_ROLES = {"broad_research", "research_mapping", "deep_research", "evaluate", "diagnose", "visual_research", "visual_research_evaluate", "apply_visual_decisions", "visual_placement", "chapter_clean_evaluate", "canonical_clean_evaluate", "final_clean_evaluate"}
CONTROLLER_ROLES = {"orchestrator", "node_controller"}
ROLE_ALIASES = {"deep_research_worker": "deep_research", "deep_research_evaluate": "evaluate", "visual_placement_linkedin": "visual_placement"}


class InvalidSnapshot(ValueError):
    pass


def _present(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _timestamp(value: object) -> datetime:
    if not _present(value):
        raise InvalidSnapshot("not_before must be an ISO timestamp with timezone")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidSnapshot("invalid not_before timestamp") from exc
    if result.tzinfo is None:
        raise InvalidSnapshot("not_before requires timezone")
    return result


def _require(snapshot: dict, field: str) -> str:
    value = snapshot.get(field)
    if not _present(value):
        raise InvalidSnapshot(f"{field} is required")
    return value


def validate_dispatch_config(role: str, model: str, reasoning: str, fork_turns: str) -> None:
    """Fail closed before role dispatch; actual host settings must also be logged."""
    if fork_turns != "none":
        raise InvalidSnapshot("every workflow role requires fork_turns='none'")
    role = ROLE_ALIASES.get(role, role)
    if role in CONTROLLER_ROLES:
        allowed = {("gpt-6-terra", "medium"), ("gpt-6-sol", "low")}
    elif role in MEDIUM_ROLES:
        allowed = {("gpt-6-sol", "medium")}
    elif role in LOW_ROLES:
        allowed = {("gpt-6-sol", "low")}
    else:
        raise InvalidSnapshot(f"unknown workflow role: {role}")
    if (model, reasoning) not in allowed:
        raise InvalidSnapshot(f"unsupported model/reasoning for {role}")


def _validate_visuals(snapshot: dict) -> None:
    _require(snapshot, "visual_review_doc_id")
    _require(snapshot, "visual_assets_folder_id")
    if snapshot.get("visual_review_status") != "resolved":
        raise InvalidSnapshot("Chapter Writing requires resolved Visual Review")
    if snapshot.get("visual_review_evaluation_status") != "passed":
        raise InvalidSnapshot("Chapter Writing requires passing Visual Review evaluation")
    if snapshot.get("visual_review_evaluated_doc_id") != snapshot["visual_review_doc_id"]:
        raise InvalidSnapshot("Visual evaluation targets a different review")
    if _require(snapshot, "visual_review_deep_research_doc_id") != _require(snapshot, "approved_deep_research_doc_id"):
        raise InvalidSnapshot("Visual Review is stale for approved Deep Research")
    decisions = snapshot.get("visual_decisions")
    if not isinstance(decisions, dict):
        raise InvalidSnapshot("visual_decisions must contain every current FOUND candidate")
    if any(not _present(key) or not isinstance(value, str) or value not in {"KEEP", "EXCLUDE"} for key, value in decisions.items()):
        raise InvalidSnapshot("Every visual decision must be KEEP or EXCLUDE")
    # Empty candidate sets are valid, but they must be explicitly supplied.
    candidates = snapshot.get("visual_candidate_ids")
    if not isinstance(candidates, list) or any(not _present(item) for item in candidates):
        raise InvalidSnapshot("visual_candidate_ids must list current FOUND candidates")
    if len(candidates) != len(set(candidates)) or set(candidates) != set(decisions):
        raise InvalidSnapshot("visual decisions do not cover exactly the current candidates")
    if snapshot.get("visual_decisions_review_doc_id") != snapshot["visual_review_doc_id"]:
        raise InvalidSnapshot("Visual decisions belong to a different review")


def _validate_final(snapshot: dict) -> None:
    canonical = _require(snapshot, "canonical_chapter_writing_doc_id")
    final = _require(snapshot, "final_chapter_writing_doc_id")
    _require(snapshot, "placement_report_doc_id")
    if canonical == final:
        raise InvalidSnapshot("Artifacts A and B must be separate documents")
    if snapshot.get("canonical_evaluation_status") != "passed" or snapshot.get("canonical_evaluated_doc_id") != canonical:
        raise InvalidSnapshot("Artifact A must have a matching passing clean evaluation")
    if snapshot.get("final_evaluation_status") != "passed" or snapshot.get("final_evaluated_doc_id") != final:
        raise InvalidSnapshot("Artifact B must have a matching passing clean evaluation")
    if snapshot.get("final_canonical_doc_id") != canonical:
        raise InvalidSnapshot("Artifact B must derive from the current Artifact A")
    if snapshot.get("final_visual_review_doc_id") != snapshot["visual_review_doc_id"]:
        raise InvalidSnapshot("Artifact B uses a stale Visual Review")


def validate_approval(snapshot: dict, doc_id: str) -> None:
    validate(snapshot)
    if snapshot["state"] != "AWAITING_APPROVAL":
        raise InvalidSnapshot("approval requires the current human approval gate")
    if doc_id != snapshot.get("pending_doc_id"):
        raise InvalidSnapshot("approval does not match the exact pending document")


def validate(snapshot: dict) -> None:
    state = snapshot.get("state")
    stage = snapshot.get("current_stage")
    if state not in STATES:
        raise InvalidSnapshot(f"unknown state: {state!r}")
    if stage not in STAGES:
        raise InvalidSnapshot(f"unknown current_stage: {stage!r}")
    if not _present(snapshot.get("run_id")):
        raise InvalidSnapshot("run_id is required")
    if not _present(snapshot.get("topic")):
        raise InvalidSnapshot("topic is required")

    for upstream in UPSTREAM[stage]:
        if not _present(snapshot.get(APPROVAL_FIELDS[upstream])):
            raise InvalidSnapshot(
                f"{stage} cannot run without approved {upstream} document"
            )

    if state in {"AWAITING_APPROVAL", "AWAITING_BLUEPRINT_SELECTION"}:
        if not _present(snapshot.get("pending_doc_id")):
            raise InvalidSnapshot(f"{state} requires pending_doc_id")

    if state == "AWAITING_BLUEPRINT_SELECTION" and stage != "chapter_blueprint":
        raise InvalidSnapshot("blueprint selection is valid only for chapter_blueprint")

    if state == "AWAITING_VISUAL_REVIEW":
        if stage != "deep_research":
            raise InvalidSnapshot("visual review is valid only for deep_research")
        review = _require(snapshot, "visual_review_doc_id")
        if _require(snapshot, "pending_visual_review_doc_id") != review:
            raise InvalidSnapshot("pending visual review must match the current review")

    if snapshot.get("not_before") not in (None, ""):
        _timestamp(snapshot["not_before"])

    if stage == "chapter_writing" and state not in {"BLOCKED", "CANCELLED"}:
        _validate_visuals(snapshot)
        if state in {"AWAITING_APPROVAL", "COMPLETED"}:
            _validate_final(snapshot)
            if state == "AWAITING_APPROVAL" and snapshot["pending_doc_id"] != snapshot["final_chapter_writing_doc_id"]:
                raise InvalidSnapshot("Chapter Writing approval must target Artifact B")
        if snapshot.get("next_action") in {"visual_placement", "visual_placement_linkedin", "final_clean_evaluate"}:
            canonical = _require(snapshot, "canonical_chapter_writing_doc_id")
            if snapshot.get("canonical_evaluation_status") != "passed" or snapshot.get("canonical_evaluated_doc_id") != canonical:
                raise InvalidSnapshot("Visual Placement requires passing current Artifact A")

    if state == "COMPLETED":
        if stage != "chapter_writing":
            raise InvalidSnapshot("COMPLETED must be at chapter_writing")
        missing = [
            stage_name
            for stage_name, field in APPROVAL_FIELDS.items()
            if not _present(snapshot.get(field))
        ]
        if missing:
            raise InvalidSnapshot(
                "COMPLETED requires approvals for: " + ", ".join(missing)
            )
        if snapshot["approved_chapter_writing_doc_id"] != snapshot["final_chapter_writing_doc_id"]:
            raise InvalidSnapshot("approved Chapter Writing must be current Artifact B")
        if snapshot.get("pending_doc_id") or snapshot.get("pending_visual_review_doc_id"):
            raise InvalidSnapshot("COMPLETED cannot retain pending review artifacts")

    attempts = snapshot.get("diagnose_attempts", 0)
    if type(attempts) is not int or attempts < 0 or attempts > 3:
        raise InvalidSnapshot("diagnose_attempts must be an integer from 0 to 3")


def next_action(snapshot: dict, now: datetime | None = None) -> str:
    validate(snapshot)
    state = snapshot["state"]
    if state == "AWAITING_APPROVAL":
        return "wait_for_exact_document_decision"
    if state == "AWAITING_BLUEPRINT_SELECTION":
        return "wait_for_blueprint_choice"
    if state == "AWAITING_VISUAL_REVIEW":
        return "wait_for_visual_decisions"
    if state in {"BLOCKED", "COMPLETED", "CANCELLED"}:
        return "none"
    clock = now or datetime.now(timezone.utc)
    if clock.tzinfo is None:
        raise InvalidSnapshot("now requires timezone")
    if snapshot.get("not_before") and clock < _timestamp(snapshot["not_before"]):
        return "wait_until_not_before"
    if state == "READY":
        return f"start:{snapshot['current_stage']}"
    if state == "RUNNING":
        return snapshot.get("next_action") or "reconcile_active_operation"
    if state == "PAUSED_LIMIT":
        if not snapshot.get("not_before"):
            return "reconcile_after_limit_reset"
        return snapshot.get("next_action") or "reconcile_after_limit_reset"
    return "none"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--print-next", action="store_true")
    args = parser.parse_args()
    try:
        payload = json.loads(args.snapshot.read_text(encoding="utf-8"))
        validate(payload)
    except (OSError, json.JSONDecodeError, InvalidSnapshot) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 2
    print("VALID")
    if args.print_next:
        print(next_action(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
