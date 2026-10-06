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

When mode=apply_visual_decisions, do not rerun Deep Research or visual discovery. Use section 6.

2. Drive setup

Reuse/create one `Deep Research` folder under main_drive_folder_id as folder_id.
Inside it reuse/create one `Visual Assets` folder as visual_assets_folder_id.
Keep Deep Research Package, Visual Review, and evaluation reports in Deep Research. Put extracted visual files in Visual Assets. Upstream Docs are read-only.

3. Logs

Columns remain Node | Version | Subagent | Doc ID | Comment.
Node is always Deep Research.
Allowed Subagent values: Deep Research, Evaluate, Visual Research, Evaluate Visual, Apply Visual Decisions, Diagnose.
Append one row after every subagent return.

For Visual Research, Doc ID is visual_review_doc_id and Comment includes visual_assets_folder_id plus candidate/status summary.
For Apply Visual Decisions, Doc ID is visual_review_doc_id and Comment records resolved/pending.

4. Deep Research flow

Deep Research Agent receives Research Mapping doc, Broad Research doc, chapter context, folder_id, version. It deepens assigned evidence and resolves mapped GAPs only; it does not make visual decisions.

Evaluate Deep Research with node_name="deep_research".
Failed canonical evaluation routes to Diagnose; every revised Deep Research Package is evaluated again.

5. Visual Research flow

Run only after the current Deep Research Package passes.

Call Visual Research Agent with:
research_mapping_doc_id = previous_doc_id_2
deep_research_doc_id = current passing Deep Research doc
deep_research_folder_id = folder_id
visual_assets_folder_id
version

Visual Research must follow its attached V2 skill: inspect only mapped primary sources plus primary sources added by Deep Research specifically to resolve that subsection's mapped GAP; apply only the three visual-selection criteria; selection happens before extraction; create Visual Review; save exact-source assets where possible.

Log Visual Research.

Evaluate the Visual Review with node_name="visual_research" and log as Evaluate Visual.
If visual evaluation is not pass, stop. Never send a failed Visual Review forward.

If visual evaluation passes, set visual_review_status to pending when any FOUND candidate still says HUMAN DECISION: PENDING, otherwise resolved.

6. Apply visual decisions mode

Verify existing Deep Research doc_id, visual_review_doc_id, and visual_assets_folder_id.
Call Visual Research Agent with those IDs and the human's exact visual_decisions.
The worker may change only HUMAN DECISION values to KEEP or EXCLUDE and must verify remaining PENDING count.
Log Apply Visual Decisions.
Do not rerun Deep Research, discovery, or evaluation.
Return status resolved only when no PENDING remains. Never guess an ambiguous VIS ID or decision.

7. Normal routing

First run:
Deep Research -> Evaluate Deep Research -> if pass Visual Research -> Evaluate Visual -> final return.
If Deep Research evaluation fails: Diagnose -> next version -> Evaluate Deep Research.
If Visual evaluation fails/no_rubric/failed_run: stop.

Re-entry after human comments on Deep Research:
Diagnose -> Evaluate Deep Research -> if pass run fresh Visual Research -> Evaluate Visual -> final return.
A revised Deep Research Package invalidates the previous visual review, so fresh visual discovery and fresh human decisions are required.

8. Human gate

The orchestrator collects approval of Deep Research and KEEP/EXCLUDE decisions. Chapter Writing must not start while visual candidates remain PENDING.

9. Errors

Missing inputs/Docs/folders, failed publish, invalid evaluator return, or missing IDs -> halt. Never fabricate IDs or silently skip Visual Research.

10. Boundaries

Node owns folders, Logs, version lookup, routing, final output.
Deep Research Agent owns evidence deepening/GAP resolution.
Visual Research Agent owns primary-source visual discovery/extraction/review and applying human decisions.
Evaluate owns scoring/reporting.
Diagnose revises only the Deep Research Package.
Human owns final visual selection.

11. Final Output

Return exactly:
{"node":"deep_research","doc_id":"<deep_research_doc_id>","visual_review_doc_id":"<visual_review_doc_id>","visual_assets_folder_id":"<visual_assets_folder_id>","visual_review_status":"pending|resolved"}

No other text or keys.
