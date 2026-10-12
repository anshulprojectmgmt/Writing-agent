Deep Research Node — Detailed Instructions

1. Inputs

Normal run receives previous_node_1, previous_doc_id_1, previous_node_2, previous_doc_id_2, chapter_topic, chapter_details, main_drive_folder_id, tracking_sheet_id.

Verify previous_node_1 = "broad_research" and previous_node_2 = "research_mapping" and both Docs open. Otherwise stop before research.

Re-entry after comments on the Deep Research Package also receives doc_id and starts from Diagnose.

Visual-decision mode additionally receives:
mode = apply_visual_decisions
visual_review_doc_id
visual_assets_folder_id
visual_decisions
and the existing Deep Research doc_id.

When mode=apply_visual_decisions, do not rerun research, extraction, selection, adaptation, rendering, review, or evaluation. Use section 8.

2. Drive setup

Reuse/create one `Deep Research` folder under main_drive_folder_id as folder_id.
Inside it reuse/create one `Visual Assets` folder as visual_assets_folder_id.
Visual Extraction may persist exact-source assets in Visual Assets. Visual Generation creates/reuses `Visual Assets/Generated` for generated assets.

Keep these audit artifacts in Deep Research:
- Deep Research Package
- Source Visual Review
- Visual Generation Plan
- Generated Visual Manifest
- Unified Visual Review
- evaluation/review reports

Upstream Docs are read-only.

3. Three durable sub-agents

The Deep Research node has exactly three durable sub-agents:

1. `Main Deep Research`
   - canonical Deep Research evidence work
   - internal Evaluate/Diagnose loop

2. `Visual Extraction`
   - implemented by existing Visual Research V2 worker
   - source inspection/extraction only
   - internal Source Visual evaluation

3. `Visual Generation`
   - fallback selector
   - pinned installed Adapt skill
   - pinned installed Render skill
   - pinned installed Render Review skill required by Render
   - Writing Agent generated-image evaluation
   - Unified Visual Review build/evaluation
   - application of human VIS/GEN decisions

Do not promote Selector, Adapt, Render, Render Review, generated evaluation, or Unified Review to additional durable workflow agents/stages. They are internal skill executions of Visual Generation.

Context separation remains mandatory. Every internal worker/evaluator/diagnose/selector/adapt/render/render-review/evaluation execution runs in its own fresh context as required by active runtime policy. Persist only artifact IDs/status between executions.

4. Logs

Columns remain Node | Version | Subagent | Doc ID | Comment.
Node is always Deep Research.

For new V3 runs use only these durable Subagent values:
- Main Deep Research
- Visual Extraction
- Visual Generation
- Diagnose

Historical V2 rows using Deep Research / Evaluate / Visual Research / Evaluate Visual / Apply Visual Decisions remain valid history and are not rewritten.

Append one row after every internal execution, even when several rows share the same durable Subagent. Put internal step in Comment and operation metadata, for example:
- Main Deep Research — `Step=Research`
- Main Deep Research — `Step=Evaluate`
- Visual Extraction — `Step=Extract`
- Visual Extraction — `Step=Evaluate Source Visuals`
- Visual Generation — `Step=Selector`
- Visual Generation — `Step=Adapt GEN-003`
- Visual Generation — `Step=Render GEN-003 Attempt=1`
- Visual Generation — `Step=Review Render GEN-003 Attempt=1`
- Visual Generation — `Step=Evaluate GEN-003 Attempt=1`
- Visual Generation — `Step=Unified Review`
- Visual Generation — `Step=Evaluate Unified Review`
- Visual Generation — `Step=Apply Visual Decisions`

Every logged internal step records exact input/output IDs, outcome, candidate ID when applicable, and retry count when applicable.

5. Sub-agent 1 — Main Deep Research

Deep Research Agent receives Research Mapping doc, Broad Research doc, chapter context, folder_id, version. It deepens assigned evidence and resolves mapped GAPs only; it does not make visual decisions.

Evaluate current Deep Research Package against `deep_research` using active safe-evaluation protocol.

Failed canonical evaluation routes to Diagnose; every revised Deep Research Package is evaluated again. Cap Diagnose according to existing workflow policy.

Do not start visual work until current Deep Research Package passes.

6. Sub-agent 2 — Visual Extraction

After current Deep Research Package passes, call existing Visual Research Agent as Visual Extraction sub-agent with:
- research_mapping_doc_id = previous_doc_id_2
- deep_research_doc_id = current passing Deep Research doc
- deep_research_folder_id = folder_id
- visual_assets_folder_id
- version

Visual Extraction follows Visual Research V2 exactly:
- inspect only mapped primary sources plus primary sources added by Deep Research specifically to resolve that subsection's mapped GAP;
- select using only the three source-visual criteria;
- selection happens before extraction;
- persist faithful exact-source assets where possible;
- keep SOURCE-LINKED when faithful persistence is unavailable;
- never generate/redraw/substitute.

Its output for V3 is a `Source Visual Review`, not final human review.

Evaluate Source Visual Review against existing `visual_research` rubric using safe evaluation. If source visual evaluation fails, stop. Never send failed extraction output to Visual Generation.

7. Sub-agent 3 — Visual Generation

After Source Visual Review passes, call `Visual Generation Agent` with:
- deep_research_doc_id = current passing Deep Research doc
- source_visual_review_doc_id = current passing Source Visual Review
- deep_research_folder_id = folder_id
- visual_assets_folder_id
- version

Visual Generation follows attached V3 skill exactly.

Internally it must:
1. select generation targets only where no usable EXTRACTED primary-source visual exists;
2. choose DATA_EXPLAINER / TOPIC_EXPLAINER / HUMOUR_METAPHOR using approved short selector rubric;
3. run full pinned installed `adapt-linkedin-visual-content` package in a fresh context for each target subsection;
4. run full pinned installed `render-linkedin-visual-post` package in another fresh context for each candidate using ChatGPT native image generation and Article-section mode;
5. run Render's pinned installed `review-linkedin-visual-post` dependency in another fresh context using its article validator/review behavior; failed review discards the complete attempt rather than patching it;
6. only after installed review passes, evaluate actual rendered asset against Writing Agent `generated_visual` rubric in another fresh context;
7. allow at most two complete render attempts across both acceptance gates;
8. build Generated Visual Manifest;
9. build Unified Visual Review containing unchanged VIS candidates + only GEN candidates that passed both gates;
10. evaluate Unified Visual Review.

The human must never be required to manually provide style references. Visual Generation loads pinned installed skill references/assets automatically.

Returned `visual_review_doc_id` from this V3 flow is always passing Unified Visual Review.

If Visual Generation or Unified Review evaluation fails, stop. Never send failed review to human or Chapter Writing.

8. Apply visual decisions mode

Verify existing Deep Research doc_id, current Unified visual_review_doc_id, and visual_assets_folder_id.

Call Visual Generation Agent in decision-application mode with those IDs and human's exact visual_decisions.

It may change only HUMAN DECISION values for exact current VIS/GEN candidate IDs to KEEP or EXCLUDE.

Do not call Visual Extraction to apply V3 decisions. Do not rerun research, extraction, selector, Adapt, Render, Render Review, or evaluation.

Return status resolved only when no current candidate remains PENDING and decision set exactly covers current candidate set. Never guess ambiguous candidate ID or decision.

9. Normal routing

First run:
Main Deep Research -> internal Evaluate -> Visual Extraction -> internal Source Visual Evaluate -> Visual Generation -> internal Adapt/Render/Render Review/generated/unified evaluations -> final return.

If Main Deep Research evaluation fails:
Diagnose -> next version -> Evaluate Main Deep Research.

If source extraction evaluation fails:
stop/block according to active runtime policy.

If Visual Generation/Unified Review evaluation fails:
stop/block according to active runtime policy.

Re-entry after human comments on Deep Research:
Diagnose -> Evaluate Main Deep Research -> fresh Visual Extraction -> fresh source evaluation -> fresh Visual Generation -> fresh Unified Visual Review.

A revised Deep Research Package invalidates all prior source/generated visual artifacts and prior human visual decisions for downstream routing. Preserve them as history but require a fresh current review.

10. Human gate

The orchestrator collects:
1. explicit approval of Deep Research Package; and
2. KEEP/EXCLUDE decisions for every current VIS/GEN candidate in passing Unified Visual Review.

Chapter Writing must not start while any current candidate remains PENDING.

11. Errors

Missing inputs/Docs/folders, failed publish, invalid evaluator result, unavailable required installed visual skill/review package, inability to create required isolated contexts, missing IDs, or failed Unified Visual Review -> halt. Never fabricate IDs, silently skip generation, or bypass evaluation.

A subsection may still end with no candidate when source extraction finds none and generated rendering fails twice. Record that failure explicitly in Unified Visual Review; do not fabricate a fallback.

12. Boundaries

Node owns folders, Logs, version lookup, routing, final output.
Main Deep Research owns evidence deepening/GAP resolution.
Visual Extraction owns primary-source visual discovery/extraction and Source Visual Review.
Visual Generation owns fallback selection, Adapt, Render, installed Render Review, Writing Agent generated evaluation, Unified Visual Review, and applying human VIS/GEN decisions.
Human owns final visual selection.
Chapter Writing/Visual Placement own later manuscript creation/placement.

13. Final Output

Keep existing downstream contract unchanged. Return exactly:
{"node":"deep_research","doc_id":"<deep_research_doc_id>","visual_review_doc_id":"<unified_visual_review_doc_id>","visual_assets_folder_id":"<visual_assets_folder_id>","visual_review_status":"pending|resolved"}

Do not add generation-plan/manifest keys to this envelope. Their IDs remain auditable in Deep Research Logs/artifacts without breaking downstream contracts.
