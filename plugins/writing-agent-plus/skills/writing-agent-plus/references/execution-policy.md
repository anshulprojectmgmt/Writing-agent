# Models, isolated contexts and transition validation

Read this policy before setup and every dispatch. Preserve canonical content skills unchanged.

| Role | Model | Reasoning |
|---|---|---|
| Main orchestrator and node controllers | gpt-6-terra | medium |
| Broad Research worker | gpt-6-sol | low |
| Research Analysis worker | gpt-6-sol | medium |
| Chapter Blueprint worker and options continuation | gpt-6-sol | medium |
| Research Mapping worker | gpt-6-sol | low |
| Deep Research worker | gpt-6-sol | low |
| Canonical Chapter Writing worker (Artifact A) | gpt-6-sol | medium |
| Every legacy evaluator and Diagnose | gpt-6-sol | low |
| Visual Research and decision-application worker | gpt-6-sol | low |
| Visual Research evaluator | gpt-6-sol | low |
| Visual Placement plus LinkedIn style (Artifact B) | gpt-6-sol | low |
| Clean Evaluate Canonical and Clean Evaluate Final | gpt-6-sol | low |

If Terra is unavailable, disclose and use Sol low for controllers only. Never use Astra, Luna or GPT-5.x. Configure actual host model/reasoning controls; a name in a prompt does not configure a model. If the parent chat's model cannot be changed, use a fresh supported controller subagent and let the parent relay IDs/status/approval only. If required settings are unavailable, stop before dispatch and report the limitation.

## Mandatory context separation

Start every controller, artifact worker, evaluator, diagnoser, visual researcher, visual decision applier, visual placement agent and clean evaluator in a fresh role context with `fork_turns="none"`. Do not reuse finished agents for another role. Blueprint continuation also uses a fresh worker and reads the saved options plus exact decision by ID.

Load only the active adapter, required original package/instruction/references and matching rubric. Pass IDs, labelled chapter runtime values, operation/version metadata and instruction paths. Never pass parent conversation history, draft prose, research summaries, findings, or comment text; roles read these from the authorized Docs themselves. Human visual decisions are exact role inputs when applying decisions, not inferred context.

These are separate conversational contexts, not separate machines or filesystem permissions. Agents share tools/files; they must not inspect unrelated scratch or artifacts. Do not claim OS-level isolation or expose private reasoning. Show actual task IDs, selected model/reasoning and fork mode in Activity & Usage Notes and Events so the dispatch is auditable.

If fresh context creation is unavailable, block the workflow. Clearing scratch or switching prompts inside the same chat is not an equivalent fallback.

## Mandatory guard calls

Use `scripts/state_machine.py` to validate the current exported snapshot before every production transition and recovery dispatch. Use `next_action(snapshot, now)` to respect all human gates and known Not Before timestamps. With an unknown reset time, PAUSED_LIMIT permits reconciliation only, never inferred dispatch.

Before every agent call validate the actual intended role/model/reasoning/fork configuration using `validate_dispatch_config`. After creation, record the actual task ID and selected host settings. Before accepting stage approval call `validate_approval` with the exact requested pending document. Reject stale approvals.

Chapter Writing requires a current passing Visual Review, exact current candidate IDs, exact human decisions covering that set, the source Deep Research ID and Visual Assets folder. Empty candidate sets are valid only when explicitly verified. Final approval/completion requires distinct Artifact A/B IDs, matching passing evaluations, current A/review provenance, Placement Report ID and approval of B. Never construct a successful snapshot from intended rather than verified artifact metadata.

## Snapshot fields

Persist guard metadata in the Runs row and mirrored chapter Run State using the append-only fields in sheet-schema.md. Resume Record also stores an exportable JSON snapshot containing these fields:

`visual_review_status`, `visual_review_evaluation_status`, `visual_review_evaluated_doc_id`, `visual_review_deep_research_doc_id`, `visual_candidate_ids`, `visual_decisions`, `visual_decisions_review_doc_id`, `canonical_evaluation_status`, `canonical_evaluated_doc_id`, `final_chapter_writing_doc_id`, `final_evaluation_status`, `final_evaluated_doc_id`, `final_canonical_doc_id`, `final_visual_review_doc_id`, `placement_report_doc_id`.

Populate them only after direct verification of the current review, reports and artifacts. If a source changes, mark dependent review/final metadata stale and return to the appropriate stage. Preserve earlier versions rather than inventing a new approval. Report disagreements between Sheet and Resume Record rather than silently selecting one.

## Recovery cadence

Use one real recovery task at hourly cadence when supported; never claim 30-minute checks in this environment. Update/verify an existing task only during authorized live setup. A scheduled task processes at most one eligible transition, remains quiet at approval/blueprint/visual gates, and respects known Not Before. Installed instructions do not themselves create or enable a scheduler.
