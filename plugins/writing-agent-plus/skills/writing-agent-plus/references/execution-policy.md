# Models, isolated contexts and transition validation

Read this policy before setup and every dispatch. Preserve unrelated content skills unchanged. The existing Chapter Writing worker uses its integrated contract version 1; Visual Placement preserves its prose.

| Role | Model | Reasoning |
|---|---|---|
| Main orchestrator and node controllers | gpt-6-terra | medium |
| Broad Research worker | gpt-6-sol | low |
| Research Analysis worker | gpt-6-sol | medium |
| Chapter Blueprint worker and options continuation | gpt-6-sol | medium |
| Research Mapping worker | gpt-6-sol | low |
| Main Deep Research worker | gpt-6-sol | low |
| Canonical Chapter Writing worker (Artifact A) | gpt-6-sol | medium |
| Every legacy evaluator and Diagnose | gpt-6-sol | low |
| Visual Extraction (Visual Research V2) | gpt-6-sol | low |
| Visual Generation durable agent | gpt-6-sol | low |
| Visual Generation Selector / Adapt controller / Render controller / generated evaluator / Unified Review verifier | gpt-6-sol | low |
| Visual Placement preserving written style (Artifact B) | gpt-6-sol | low |
| Clean Evaluate Canonical and Clean Evaluate Final | gpt-6-sol | low |

Image rendering inside the Visual Generation Render execution uses ChatGPT native image generation according to the pinned Render skill. It is not an alternate workflow model/role and must not be replaced by Runway or another external image-generation provider.

If Terra is unavailable, disclose and use Sol low for controllers only. Never use Astra, Luna or GPT-5.x. Configure actual host model/reasoning controls; a name in a prompt does not configure a model. If the parent chat's model cannot be changed, use a fresh supported controller subagent and let the parent relay IDs/status/approval only. If required settings are unavailable, stop before dispatch and report the limitation.

## Mandatory context separation

Start every controller, artifact worker, evaluator, diagnoser, Visual Extraction agent, Visual Generation durable agent, visual decision applier, visual placement agent and clean evaluator in a fresh role context with `fork_turns="none"`. Do not reuse finished agents for another durable role. Blueprint continuation also uses a fresh worker and reads the saved options plus exact decision by ID.

Deep Research has exactly three durable sub-agents: Main Deep Research, Visual Extraction and Visual Generation.

Inside Visual Generation, context isolation continues at skill-execution level:
- Selector runs in a fresh context.
- Every target subsection's Adapt runs in its own fresh context.
- Every GEN candidate's Render runs in its own fresh context and sees only that candidate's approved brief/evidence lock.
- Every GEN candidate's generated evaluator runs in its own fresh context and inspects the actual rendered asset.
- Unified Visual Review build/verification uses a fresh context.

Do not reuse a candidate's Adapt/Render/evaluation context for another candidate. Do not pass previous rendered images/conversation history into the next candidate unless the pinned installed Render skill explicitly loads its own approved bundled reference assets. The user must not manually supply style references for normal production runs.

Load only the active adapter, required original package/instruction/references and matching rubric. Pass IDs, labelled chapter runtime values, operation/version metadata and instruction paths. Never pass parent conversation history, draft prose, research summaries, findings, or comment text; roles read these from authorized Docs themselves. Human visual decisions are exact role inputs when applying decisions, not inferred context.

These are separate conversational contexts, not separate machines or filesystem permissions. Agents share tools/files; they must not inspect unrelated scratch or artifacts. Do not claim OS-level isolation or expose private reasoning. Show actual task IDs, selected model/reasoning and fork mode in Activity & Usage Notes and Events so dispatch is auditable.

If fresh context creation is unavailable, block the production workflow. Clearing scratch or switching prompts inside one conversation is not an equivalent fallback.

## Mandatory guard calls

Use `scripts/state_machine.py` to validate the current exported snapshot before every production transition and recovery dispatch. Use `next_action(snapshot, now)` to respect all human gates and known Not Before timestamps. With an unknown reset time, PAUSED_LIMIT permits reconciliation only, never inferred dispatch.

Before every durable agent call validate the intended role/model/reasoning/fork configuration using `validate_dispatch_config`. For internal Visual Generation executions, log the fresh task/context ID and parent candidate/step under the Visual Generation durable role. After creation, record actual task ID and selected host settings. Before accepting stage approval call `validate_approval` with exact requested pending document. Reject stale approvals.

Chapter Writing requires a current passing Unified Visual Review, exact current candidate IDs, exact human decisions covering that set, the source Deep Research ID and Visual Assets folder. Empty candidate sets are valid only when explicitly verified. Final approval/completion requires distinct Artifact A/B IDs, matching passing evaluations, current A/review provenance, Placement Report ID and approval of B. Never construct a successful snapshot from intended rather than verified artifact metadata.

## Snapshot fields

Persist guard metadata in the Runs row and mirrored chapter Run State using the append-only fields in sheet-schema.md. Resume Record also stores an exportable JSON snapshot containing these fields:

`visual_review_status`, `visual_review_evaluation_status`, `visual_review_evaluated_doc_id`, `visual_review_deep_research_doc_id`, `visual_candidate_ids`, `visual_decisions`, `visual_decisions_review_doc_id`, `canonical_evaluation_status`, `canonical_evaluated_doc_id`, `final_chapter_writing_doc_id`, `final_evaluation_status`, `final_evaluated_doc_id`, `final_canonical_doc_id`, `final_visual_review_doc_id`, `placement_report_doc_id`.

These fields remain sufficient for V3 because `visual_review_doc_id` now points to the current passing Unified Visual Review and `visual_candidate_ids` may contain both VIS and GEN IDs. Internal Source Visual Review, Visual Generation Plan and Generated Visual Manifest IDs are logged in Artifact Log/Events rather than added to the main downstream snapshot contract.

Populate metadata only after direct verification of current review, reports and artifacts. If a source changes, mark dependent review/final metadata stale and return to the appropriate stage. Preserve earlier versions rather than inventing a new approval. Report disagreements between Sheet and Resume Record rather than silently selecting one.

## Recovery cadence

Use one real recovery task at hourly cadence when supported; never claim 30-minute checks in this environment. Update/verify an existing task only during authorized live setup. A scheduled task processes at most one eligible transition, remains quiet at approval/blueprint/visual gates, and respects known Not Before. Installed instructions do not themselves create or enable a scheduler.

If a limit interrupts Visual Generation, checkpoint the exact internal step/candidate/attempt and resume only that recorded step after reconciliation. Do not rerun already passing GEN candidates or rebuild source extraction unnecessarily.

## Mandatory Chapter Writing integration preflight

Before Chapter Writing start/resume/revision, export the verified production snapshot and run `scripts/validate_chapter_contract.py <production-root>`. Load all seven worker dependencies listed in its SKILL.md into the fresh Chapter Writing context. The two writing skills and internal humanizer are bundled exact registry snapshots, not extra registered nodes. Preserve the model mapping above.

Before Visual Placement/final evaluation/approval, verify the separate canonical evaluation report against Artifact A Notes and actual formatting. Store the four integrated execution guard fields from sheet-schema.md, then run state_machine.py. Missing/stale receipt or any skipped check blocks the transition. Keep reference paths/hashes in worker Notes and matching report, only metadata in controller state. Do not silently mark historical unknowns as passed.

## Mandatory approved presentation gate
Read Chapter Writing references/presentation-contract.md and presentation-profile.json. Use personal-agents-approved-v1 and run scripts/validate_chapter_presentation.py on actual native Doc JSON plus the revision-bound presentation plan. Counts/self-declarations cannot substitute. Worker-only tests also require this before returning success. Independently inspect semantic placement in clean evaluation. The execution receipt must include matching presentation profile/baseline provenance, current Artifact A revision, passing native_validator_passed and locatable evidence. Missing/stale/failed presentation blocks handoff regardless of score. Use numbered main HEADING_1, unnumbered HEADING_2, functional icons, meaningful existing opening emphasis, explanatory lists, plain reader citations and exact linked source URLs in Handoff. No new formatting node or Visual Placement rewrite.
