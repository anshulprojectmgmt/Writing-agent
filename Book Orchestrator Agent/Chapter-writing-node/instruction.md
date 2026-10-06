Chapter Writing Node — Detailed Instructions

## 1. Inputs

Required normal-run inputs:
- previous_node_1, previous_doc_id_1 from Research Mapping
- previous_node_2, previous_doc_id_2 from Deep Research
- visual_review_doc_id
- visual_assets_folder_id
- chapter_topic, chapter_details
- main_drive_folder_id, tracking_sheet_id

Verify previous_node_1 = "research_mapping" and previous_node_2 = "deep_research" and that both upstream Docs, visual_review_doc_id, and visual_assets_folder_id are reachable. If any check fails, stop before writing.

The Visual Review is a hard gate. Before calling the Chapter Writing Worker, verify every FOUND candidate has HUMAN DECISION = KEEP or EXCLUDE. If any PENDING remains, stop and report that Chapter Writing is blocked.

Re-entry after user comments on final Artifact B additionally receives `doc_id` (the reviewed final chapter) and the standard human-feedback line. Follow §7.

## 2. Drive setup

Reuse/create exactly one folder named `Chapter Writing` under main_drive_folder_id as folder_id. Keep all Chapter Writing artifacts flat in this folder.

Upstream Research Mapping, Deep Research, Visual Review, and Visual Assets remain read-only except that Visual Placement may add a faithful exact-source extraction into Visual Assets when a KEEP candidate was SOURCE-LINKED and can be persisted without substitution.

## 3. Logs — node-owned

Columns remain Node | Version | Subagent | Doc ID | Comment.
Node is always `Chapter Writing`.

Allowed Subagent values:
- Chapter Writing
- Evaluate Canonical
- Visual Placement
- Evaluate Final
- Diagnose

Append exactly one row after every subagent return.

Artifact A row uses the canonical Chapter Writing Doc ID.
Visual Placement row uses Artifact B Doc ID and includes placement_report_doc_id in Comment.
Evaluation rows store their separate evaluation-report Doc IDs.

Determine version from the latest Chapter Writing row. First run begins V1. Never overwrite prior versions.

## 4. Artifact A — canonical Anshul chapter

Call the existing Chapter Writing Agent with:
- previous_doc_id_2 = approved Deep Research Package
- previous_doc_id_1 = approved Research Mapping artifact
- chapter_topic
- chapter_details
- folder_id
- version

The worker must follow the existing `anshul-chapter-writing-4` skill and its bundled `anshul-voice.md`, `writing-style.md`, and `output-formatting.md` references exactly.

Important separation rule: DO NOT pass, inject, or apply the LinkedIn-derived style to this worker. Artifact A must remain the canonical Anshul-style chapter package, including the canonical skill's own Notes/Handoff/Summary outputs.

Log `Chapter Writing` with Artifact A doc_id.

Evaluate Artifact A using:
- doc_id = Artifact A
- version
- folder_id
- node_name = `chapter_writing`
- annotation_mode = `report_only`

Log `Evaluate Canonical`.

If canonical evaluation fails: route to the existing Diagnose Agent on Artifact A, create the next canonical version, evaluate it again in report_only mode, and repeat within Diagnose limits. Do not run Visual Placement until the current Artifact A passes.

## 5. Artifact B — LinkedIn style + approved visuals

Only after Artifact A passes, call Visual Placement Agent with:
- canonical_chapter_doc_id = current passing Artifact A
- visual_review_doc_id
- visual_assets_folder_id
- chapter_writing_folder_id = folder_id
- version

The Visual Placement Agent must create a NEW document. It never edits Artifact A.

Artifact B contains only the reader-facing chapter, transformed to the approved LinkedIn-derived style and populated only with human-KEEP visuals. Workflow notes stay outside Artifact B.

Log `Visual Placement` using Artifact B doc_id and include its placement_report_doc_id in the Comment.

Evaluate Artifact B using:
- doc_id = Artifact B
- version
- folder_id
- node_name = `chapter_writing_final`
- annotation_mode = `report_only`
- canonical_chapter_doc_id = Artifact A
- visual_review_doc_id
- placement_report_doc_id

Log `Evaluate Final`.

If final evaluation fails, do not modify Artifact A. Regenerate Artifact B through the Visual Placement Agent using the same passing Artifact A and visual review, addressing only final-style/placement issues identified by the evaluation. Re-evaluate the new Artifact B. Never patch evidence or structure only in Artifact B to make the final evaluator pass.

## 6. First-run flow

Chapter Writing Worker -> Artifact A
-> Evaluate Canonical (report_only)
-> if failed: Diagnose canonical -> Evaluate Canonical
-> when pass: Visual Placement -> Artifact B + placement report
-> Evaluate Final (report_only)
-> if failed: regenerate Artifact B from same passing Artifact A -> Evaluate Final
-> when pass: notification -> final output.

Both Artifact A and Artifact B remain in Drive and Logs. Artifact A is never overwritten by Artifact B.

## 7. Re-entry after human comments on Artifact B

The reviewed doc_id is Artifact B.

Call Visual Placement Agent with:
- canonical_chapter_doc_id = latest passing Artifact A from Logs
- visual_review_doc_id
- visual_assets_folder_id
- chapter_writing_folder_id = folder_id
- version = next final version as determined by the node
- previous_final_doc_id = reviewed doc_id
- feedback_mode = human_feedback

The Visual Placement Agent reads the final Doc comments.

If comments are presentation/voice/formatting/visual-placement only, it creates a new Artifact B from the same canonical Artifact A and those comments, then Evaluate Final runs in report_only mode.

If it returns `Requires canonical revision`, stop and surface that result upward. Do not secretly alter evidence/claims/structure only in Artifact B. A substantive change must be made in the canonical source chapter before a new final presentation is generated.

## 8. Routing

Canonical evaluator failed -> Diagnose canonical.
Canonical evaluator pass -> Visual Placement.
Final evaluator failed -> regenerate final presentation from same canonical source unless the failure itself requires canonical evidence/structure changes, in which case stop/escalate.
Final evaluator pass -> final return.

no_rubric, failed_run, missing IDs, or unparseable evaluator metadata -> halt. Never guess.

## 9. Human review

The orchestrator owns the human approval gate after this node returns. This node does not wait for approval during its run.

## 10. Boundaries

Node owns folder setup, Logs, versioning, routing, notifications, and final envelope.
Chapter Writing Agent owns canonical Artifact A only.
Evaluate Canonical scores Artifact A only and runs report-only.
Visual Placement Agent owns Artifact B and placement report only.
Evaluate Final scores Artifact B against canonical/style/visual constraints and runs report-only.
Diagnose revises only canonical Artifact A when canonical content fails.
Human owns visual KEEP/EXCLUDE decisions upstream and final chapter approval downstream.

## 11. Final Output

Return exactly:
{"node":"chapter_writing","doc_id":"<passing_final_artifact_b_doc_id>"}

The final doc_id is Artifact B. Artifact A remains preserved in Logs/Drive.
No other text or keys.
