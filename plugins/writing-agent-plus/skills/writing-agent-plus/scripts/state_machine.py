"""Validate subscription-edition run snapshots exported from the control sheet."""

from __future__ import annotations

import argparse
import json
import sys
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
    "PAUSED_LIMIT",
    "BLOCKED",
    "COMPLETED",
    "CANCELLED",
}

APPROVAL_FIELDS = {stage: f"approved_{stage}_doc_id" for stage in STAGES}


class InvalidSnapshot(ValueError):
    pass


def _present(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


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

    if state == "COMPLETED":
        missing = [
            stage_name
            for stage_name, field in APPROVAL_FIELDS.items()
            if not _present(snapshot.get(field))
        ]
        if missing:
            raise InvalidSnapshot(
                "COMPLETED requires approvals for: " + ", ".join(missing)
            )

    attempts = snapshot.get("diagnose_attempts", 0)
    if not isinstance(attempts, int) or attempts < 0 or attempts > 3:
        raise InvalidSnapshot("diagnose_attempts must be an integer from 0 to 3")


def next_action(snapshot: dict) -> str:
    validate(snapshot)
    state = snapshot["state"]
    if state == "READY":
        return f"start:{snapshot['current_stage']}"
    if state == "RUNNING":
        return snapshot.get("next_action") or "reconcile_active_operation"
    if state == "PAUSED_LIMIT":
        return snapshot.get("next_action") or "reconcile_after_limit_reset"
    if state == "AWAITING_APPROVAL":
        return "wait_for_exact_document_decision"
    if state == "AWAITING_BLUEPRINT_SELECTION":
        return "wait_for_blueprint_choice"
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
