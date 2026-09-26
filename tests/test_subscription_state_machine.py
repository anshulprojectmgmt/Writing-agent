from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

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
