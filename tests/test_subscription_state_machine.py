from __future__ import annotations

import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest


@pytest.mark.parametrize("role,model,reasoning", [
    ("orchestrator", "gpt-6-terra", "medium"),
    ("node_controller", "gpt-6-sol", "low"),
    ("research_analysis", "gpt-6-sol", "medium"),
    ("chapter_blueprint", "gpt-6-sol", "medium"),
    ("chapter_writing", "gpt-6-sol", "medium"),
    ("visual_research", "gpt-6-sol", "low"),
    ("visual_placement", "gpt-6-sol", "low"),
    ("chapter_clean_evaluate", "gpt-6-sol", "low"),
])
def test_approved_dispatch(role, model, reasoning):
    state_machine.validate_dispatch_config(role, model, reasoning, "none")


@pytest.mark.parametrize("role,model,reasoning,fork", [
    ("chapter_writing", "gpt-6-astra", "low", "none"),
    ("visual_research", "gpt-6-luna", "low", "none"),
    ("evaluate", "gpt-6-sol", "medium", "none"),
    ("chapter_blueprint", "gpt-6-sol", "low", "none"),
    ("diagnose", "gpt-6-sol", "low", "all"),
    ("visual_placement", "gpt-6-sol", "low", "1"),
    ("unknown", "gpt-6-sol", "low", "none"),
])
def test_unapproved_dispatch_rejected(role, model, reasoning, fork):
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate_dispatch_config(role, model, reasoning, fork)

MODULE_PATH = (
    Path(__file__).parents[1]
    / "plugins"
    / "writing-agent-plus"
    / "skills"
    / "writing-agent-plus"
    / "scripts"
    / "state_machine.py"
)
SPEC = importlib.util.spec_from_file_location("subscription_state_machine", MODULE_PATH)
assert SPEC and SPEC.loader
state_machine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(state_machine)


def snapshot(**updates):
    value = {
        "run_id": "run-1",
        "topic": "Adaptive products",
        "state": "READY",
        "current_stage": "broad_research",
        "diagnose_attempts": 0,
    }
    value.update(updates)
    return value


def test_first_stage_is_valid():
    value = snapshot()
    state_machine.validate(value)
    assert state_machine.next_action(value) == "start:broad_research"


def test_downstream_stage_requires_approved_dependencies():
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(snapshot(current_stage="deep_research"))


def test_deep_research_accepts_required_approvals():
    value = snapshot(
        current_stage="deep_research",
        approved_broad_research_doc_id="doc-br",
        approved_research_mapping_doc_id="doc-map",
    )
    state_machine.validate(value)


def test_approval_gate_requires_pending_document():
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(snapshot(state="AWAITING_APPROVAL"))


def test_blueprint_selection_only_on_blueprint():
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(
            snapshot(
                state="AWAITING_BLUEPRINT_SELECTION",
                pending_doc_id="doc-options",
            )
        )


def test_completed_requires_all_six_approvals():
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(snapshot(state="COMPLETED"))


def test_diagnose_cap_is_enforced():
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(snapshot(diagnose_attempts=4))


def deep_research_snapshot(**updates):
    value = snapshot(
        current_stage="deep_research",
        approved_broad_research_doc_id="doc-br",
        approved_research_mapping_doc_id="doc-map",
    )
    value.update(updates)
    return value


def chapter_writing_snapshot(**updates):
    value = snapshot(
        current_stage="chapter_writing",
        approved_research_mapping_doc_id="doc-map",
        approved_deep_research_doc_id="doc-deep",
        visual_review_doc_id="doc-visual",
        visual_assets_folder_id="folder-assets",
        visual_review_status="resolved",
        visual_review_evaluation_status="passed",
        visual_review_evaluated_doc_id="doc-visual",
        visual_review_deep_research_doc_id="doc-deep",
        visual_decisions={"candidate-1": "KEEP", "candidate-2": "EXCLUDE"},
        visual_candidate_ids=["candidate-1", "candidate-2"],
        visual_decisions_review_doc_id="doc-visual",
    )
    value.update(updates)
    return value


def completed_snapshot(**updates):
    value = chapter_writing_snapshot(
        state="COMPLETED",
        approved_broad_research_doc_id="doc-br",
        approved_research_analysis_doc_id="doc-analysis",
        approved_chapter_blueprint_doc_id="doc-blueprint",
        canonical_chapter_writing_doc_id="doc-canonical",
        final_chapter_writing_doc_id="doc-final",
        approved_chapter_writing_doc_id="doc-final",
        canonical_evaluation_status="passed",
        final_evaluation_status="passed",
        canonical_evaluated_doc_id="doc-canonical",
        final_evaluated_doc_id="doc-final",
        final_canonical_doc_id="doc-canonical",
        final_visual_review_doc_id="doc-visual",
        placement_report_doc_id="doc-placement",
    )
    value.update(updates)
    return value


def test_visual_review_gate_requires_matching_pending_document_and_deep_research():
    value = deep_research_snapshot(
        state="AWAITING_VISUAL_REVIEW",
        visual_review_doc_id="doc-visual",
        pending_visual_review_doc_id="doc-visual",
    )
    state_machine.validate(value)
    action = state_machine.next_action(value)
    assert action.startswith("wait_")
    assert not action.startswith(("start:", "dispatch:"))

    for invalid in (
        {"current_stage": "chapter_writing", "approved_deep_research_doc_id": "doc-deep"},
        {"visual_review_doc_id": None},
        {"pending_visual_review_doc_id": None},
        {"pending_visual_review_doc_id": "different-doc"},
    ):
        candidate = {**value, **invalid}
        with pytest.raises(state_machine.InvalidSnapshot):
            state_machine.validate(candidate)


@pytest.mark.parametrize(
    "invalid",
    [
        {"visual_review_doc_id": None},
        {"visual_assets_folder_id": None},
        {"visual_review_status": "pending"},
        {"visual_review_evaluation_status": "failed"},
        {"visual_review_evaluated_doc_id": "doc-old-review"},
        {"visual_review_deep_research_doc_id": "another-deep-doc"},
        {"visual_decisions": None},
        {"visual_decisions": {"candidate-1": "MAYBE"}},
        {"visual_decisions": {"candidate-1": "keep"}},
        {"visual_decisions": {"candidate-1": "KEEP"}},
        {"visual_decisions": {"candidate-1": "KEEP", "candidate-2": "EXCLUDE", "candidate-3": "KEEP"}},
        {"visual_candidate_ids": ["candidate-1", "candidate-1"]},
        {"visual_decisions_review_doc_id": "doc-old-review"},
    ],
)
def test_chapter_writing_rejects_missing_or_invalid_visual_resolution(invalid):
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(chapter_writing_snapshot(**invalid))


def test_chapter_writing_accepts_zero_visual_candidates():
    state_machine.validate(chapter_writing_snapshot(visual_decisions={}, visual_candidate_ids=[]))


@pytest.mark.parametrize(
    "invalid",
    [
        {"canonical_chapter_writing_doc_id": None},
        {"final_chapter_writing_doc_id": "doc-canonical"},
        {"canonical_evaluation_status": "failed"},
        {"final_evaluation_status": "pending"},
        {"canonical_evaluated_doc_id": "stale-canonical"},
        {"final_evaluated_doc_id": "stale-final"},
        {"final_canonical_doc_id": "stale-canonical"},
        {"final_visual_review_doc_id": "doc-old-review"},
        {"approved_chapter_writing_doc_id": "stale-final"},
        {"pending_doc_id": "still-pending"},
        {"placement_report_doc_id": None},
    ],
)
def test_completed_rejects_missing_or_mismatched_chapter_provenance(invalid):
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate(completed_snapshot(**invalid))


def test_completed_accepts_distinct_evaluated_canonical_and_final_documents():
    state_machine.validate(completed_snapshot())


def test_not_before_blocks_dispatch_until_due():
    now = datetime(2026, 10, 6, 12, 0, tzinfo=timezone.utc)
    value = snapshot(not_before=(now + timedelta(minutes=5)).isoformat())
    assert state_machine.next_action(value, now=now) == "wait_until_not_before"
    assert state_machine.next_action(value, now=now + timedelta(minutes=5)) == "start:broad_research"


def test_paused_limit_without_known_retry_reconciles_instead_of_dispatching():
    value = snapshot(state="PAUSED_LIMIT", next_action="start:broad_research")
    assert state_machine.next_action(value, now=datetime.now(timezone.utc)) == "reconcile_after_limit_reset"


def test_approval_requires_exact_pending_document_and_approval_gate():
    value = snapshot(state="AWAITING_APPROVAL", pending_doc_id="doc-current")
    state_machine.validate_approval(value, "doc-current")
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate_approval(value, "doc-stale")
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate_approval(snapshot(), "doc-current")
    visual_gate = deep_research_snapshot(
        state="AWAITING_VISUAL_REVIEW",
        visual_review_doc_id="doc-visual",
        pending_visual_review_doc_id="doc-visual",
    )
    with pytest.raises(state_machine.InvalidSnapshot):
        state_machine.validate_approval(visual_gate, "doc-visual")
