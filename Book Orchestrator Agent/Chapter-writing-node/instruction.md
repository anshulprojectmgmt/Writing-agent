Chapter Writing Node — Detailed Instructions

## 1. Inputs

Required normal-run inputs:
- previous_node_1, previous_doc_id_1 from Research Mapping
- previous_node_2, previous_doc_id_2 from Deep Research
- visual_review_doc_id
- visual_assets_folder_id
- chapter_topic, chapter_details
- main_drive_folder_id, tracking_sheet_id

Verify previous_node_1 = "research_mapping" and previous_node_2 = "deep_research" and all upstream Docs/folders open. The Visual Review is a hard gate: every FOUND candidate must be KEEP or EXCLUDE. Any PENDING blocks Chapter Writing.

Re-entry after comments on final Artifact B additionally receives doc_id plus the standard human-feedback line.

## 2. Drive setup

Reuse/create exactly one `Chapter Writing` folder as folder_id. Keep Chapter Writing artifacts flat. Upstream Research Mapping, Deep Research, and Visual Review remain read-only. Visual Placement may add only a faithful exact-source extraction to Visual Assets for a SOURCE-LINKED KEEP candidate.

## 3. Logs

Columns remain Node | Version | Subagent | Doc ID | Comment. Node is always Chapter Writing.

Allowed Subagent values:
- Chapter Writing
- Evaluate Canonical
- Visual Placement
- Evaluate Final
- Diagnose

Append one row after every subagent return. Artifact A row uses canonical chapter doc_id. Visual Placement row uses Artifact B doc_id and includes placement_report_doc_id in Comment. Evaluation rows store separate evaluation-report doc IDs.

First run starts V1. Never overwrite earlier versions.

## 4. Artifact A — canonical Anshul chapter

Call the existing Chapter Writing Agent with approved Deep Research + approved Research Mapping + chapter context + folder_id + version.

It must follow only the existing `anshul-chapter-writing-4` skill and its bundled `anshul-voice.md`, `writing-style.md`, and `output-formatting.md` references.

DO NOT pass, inject, or apply the LinkedIn-derived style to this worker. Artifact A is the canonical Anshul-style chapter package, including the canonical skill's Notes/Handoff/Summary outputs.

Log `Chapter Writing`.

Call **Chapter Clean Evaluate Agent** on Artifact A with:
- doc_id = Artifact A
- version
- folder_id
- node_name = `chapter_writing`

The clean evaluator is report-only by design; it never inserts findings/comments into Artifact A.

Log `Evaluate Canonical`.

If canonical evaluation fails: use the existing Diagnose Agent on Artifact A, create the next canonical version, then call Chapter Clean Evaluate Agent again. Repeat within Diagnose limits. Do not run Visual Placement until Artifact A passes.

## 5. Artifact B — LinkedIn style + approved visuals

Only after Artifact A passes, call Visual Placement Agent with:
- canonical_chapter_doc_id = current passing Artifact A
- visual_review_doc_id
- visual_assets_folder_id
- chapter_writing_folder_id = folder_id
- version

Visual Placement creates a NEW document. It never edits Artifact A.
Artifact B contains only reader-facing chapter content in the approved LinkedIn-derived style plus human-KEEP visuals. Workflow notes stay in separate artifacts.

Log `Visual Placement` using Artifact B doc_id and include placement_report_doc_id in Comment.

Call **Chapter Clean Evaluate Agent** on Artifact B with:
- doc_id = Artifact B
- version
- folder_id
- node_name = `chapter_writing_final`
- canonical_chapter_doc_id = Artifact A
- visual_review_doc_id
- placement_report_doc_id

The clean evaluator reads all four artifacts for cross-document checks and writes only a separate evaluation report.

Log `Evaluate Final`.

If final evaluation fails, keep Artifact A unchanged. Regenerate Artifact B through Visual Placement from the same passing Artifact A, addressing only presentation/placement issues. Re-run Chapter Clean Evaluate Agent. Never change evidence or approved structure only in Artifact B to force a pass.

## 6. First-run flow

Chapter Writing Worker -> Artifact A
-> Chapter Clean Evaluate (canonical)
-> canonical fail: Diagnose canonical -> clean evaluate again
-> canonical pass: Visual Placement -> Artifact B + placement report
-> Chapter Clean Evaluate (final)
-> final fail: regenerate Artifact B from same canonical source -> clean evaluate again
-> final pass: notification -> final output.

Artifact A and Artifact B both remain in Drive and Logs.

## 7. Re-entry after human comments on Artifact B

Call Visual Placement Agent with latest passing Artifact A, visual_review_doc_id, visual_assets_folder_id, folder_id, next version, previous_final_doc_id=reviewed doc_id, feedback_mode=human_feedback.

Visual Placement reads open human comments.
- Presentation/voice/formatting/visual-placement feedback -> regenerate Artifact B from the same canonical source and run final clean evaluation.
- Any feedback that changes facts, evidence, citations, statistics, claims, caveats, fixed punch lines, approved structure, or the designated transformation -> Visual Placement must return `Requires canonical revision`; stop and surface that result rather than patching a contradictory final document.

## 8. Errors/routing

Canonical failed -> Diagnose canonical.
Canonical pass -> Visual Placement.
Final failed -> regenerate final from canonical when failure is presentation/placement only; otherwise stop/escalate.
Final pass -> final return.

Missing IDs, no_rubric, failed_run, unparseable metadata, or unresolved visual decisions -> halt. Never guess or fabricate.

## 9. Boundaries

Node: folder setup, Logs, versioning, routing, notification, final envelope.
Chapter Writing Agent: canonical Artifact A only.
Chapter Clean Evaluate Agent: report-only evaluation of A and B.
Visual Placement Agent: Artifact B + placement report only.
Diagnose Agent: canonical Artifact A revisions only.
Human: upstream KEEP/EXCLUDE decisions and downstream final approval.

## 10. Final Output

Return exactly:
{"node":"chapter_writing","doc_id":"<passing_final_artifact_b_doc_id>"}

Artifact A remains preserved in Logs/Drive. No other text or keys.
