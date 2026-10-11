# Google Sheets schema

Create one project-level `Writing Agent Control` workbook and one chapter-level `Logs` workbook.
All timestamps are ISO 8601 UTC. IDs are strings. Never reorder or rename columns after setup; when upgrading an existing workbook, append the V2 columns to the right and preserve existing values.

## Project Configuration

`Project ID | Project Name | Root Folder ID | Book Folder ID | Default Reviewers | Active | Updated At`

One active row per project. `Default Reviewers` is a comma-separated email list.

## Queue

`Run ID | Project ID | Topic | Details | Requested By | Chapter Folder ID | State | Current Stage | Pending Doc ID | Pending Visual Review Doc ID | Next Action | Not Before | Operation ID | Chat URL | Updated At`

Allowed queue states:
`READY`, `RUNNING`, `AWAITING_APPROVAL`, `AWAITING_BLUEPRINT_SELECTION`, `AWAITING_VISUAL_REVIEW`, `PAUSED_LIMIT`, `BLOCKED`, `COMPLETED`, `CANCELLED`.

Only READY, recoverable RUNNING, and due PAUSED_LIMIT rows are eligible for scheduled transition. Approval/selection/visual-review states are never advanced by a scheduled wake-up.

## Runs

`Run ID | Topic | Details | Requested By | Chapter Folder ID | Logs Sheet ID | Resume Doc ID | Current Stage | State | Approved Broad Research Doc ID | Approved Research Analysis Doc ID | Approved Chapter Blueprint Doc ID | Approved Research Mapping Doc ID | Approved Deep Research Doc ID | Visual Review Doc ID | Visual Assets Folder ID | Canonical Chapter Writing Doc ID | Approved Chapter Writing Doc ID | Pending Doc ID | Pending Visual Review Doc ID | Pending Version | Last Checkpoint | Next Action | Not Before | Error Code | Error Summary | Updated At`

`Canonical Chapter Writing Doc ID` is Artifact A (canonical Anshul style). `Approved Chapter Writing Doc ID` is Artifact B (preserved writing + human-KEEP visuals), because Artifact B is the main Chapter Writing stage output presented for approval.

`Visual Review Doc ID` and `Visual Assets Folder ID` are written after a passing Visual Research evaluation. If Deep Research is revised, replace these fields only after the fresh Visual Research artifacts are verified; old visual artifacts remain in Drive history but are stale for the run.

Approval columns are written only after explicit human approval for the matching pending artifact. A Visual Review is not an ordinary stage approval: its exact KEEP/EXCLUDE decisions are recorded in Decisions and the run may advance only when no PENDING candidate remains.

### Append-only Runs guard metadata

Append these missing columns at the far right of existing Runs and chapter Run State tabs; never reposition legacy columns:

`Visual Review Status | Visual Review Evaluation Status | Visual Review Evaluated Doc ID | Visual Review Deep Research Doc ID | Visual Candidate IDs | Visual Decisions | Visual Decisions Review Doc ID | Canonical Evaluation Status | Canonical Evaluated Doc ID | Final Chapter Writing Doc ID | Final Evaluation Status | Final Evaluated Doc ID | Final Canonical Doc ID | Final Visual Review Doc ID | Placement Report Doc ID`

Candidate IDs are a JSON array and decisions a JSON object. Store the corresponding snake_case fields listed in `execution-policy.md` in the Resume Record JSON snapshot. Populate statuses and provenance only after direct artifact/report verification. Historical rows retain unknown fields as blank; they are not silently upgraded to passing V2 runs. Compare headers by name before any write and verify readback.

## Decisions

`Timestamp | Run ID | Stage | Action | Doc ID | Actor | Choice | Source | Decision ID`

Allowed Action values:
- `APPROVE`
- `COMMENTS_READY`
- `BLUEPRINT_CHOICE`
- `VISUAL_DECISIONS`
- `RESUME`
- `CANCEL`

For `VISUAL_DECISIONS`, Doc ID is the exact current Visual Review Doc ID and Choice stores a compact exact VIS-ID decision payload or `REVIEW_EDITED_IN_DOC` when the user edited all decision fields directly and the controller verified no PENDING remains. Never record visual decisions against a stale review.

Decision ID is stable and unique; duplicates are ignored.

## Activity & Usage

`Started At | Finished At | Run ID | Stage | Role | Version | Attempt | Chat or Task ID | Model | Reasoning | Operation ID | Plan Usage Before | Plan Usage After | Estimated Effort | Outcome | Notes`

Precise plan token/credit usage is not programmatically exposed. Leave unknown values blank. Estimated Effort may be LOW, MEDIUM, HIGH and must stay labeled as an estimate. Never convert it to dollars or use zero for unavailable data.

## Events

`Timestamp | Run ID | Event Type | Actor | Operation ID | Stage | Doc ID | Details`

Append-only. Include starts, checkpoints, artifact creation, evaluations, retries, pauses, notifications, approvals, blueprint selections, visual-review creation/evaluation/decisions, Visual Assets creation, Artifact A creation/evaluation, Artifact B creation/evaluation, resumptions, cancellations, and completion.

## Chapter Logs workbook: Artifact Log

`Node | Version | Subagent | Doc ID | Comment | Run ID | Attempt ID | Status | Created At | Operation ID`

V2 expected Subagent values include:
- Research Mapping: Research Mapping, Evaluate, Diagnose
- Deep Research: Deep Research, Evaluate, Visual Research, Evaluate Visual, Apply Visual Decisions, Diagnose
- Chapter Writing: Chapter Writing, Evaluate Canonical, Visual Placement, Evaluate Final, Diagnose

For a Visual Research row, Doc ID is Visual Review Doc ID and Comment includes Visual Assets Folder ID plus candidate/status summary.
For Visual Placement, Doc ID is Artifact B and Comment includes Placement Report Doc ID.
Artifact A always has its own Chapter Writing row and is never overwritten by Artifact B.

## Chapter Logs workbook: Run State

Use the same columns as the project-level Runs tab for the selected run. This is an audit mirror. Project Runs row + Resume Record control recovery if they disagree; stop on disagreement rather than overwriting either side.

## Chapter Logs workbook: Activity & Usage

Use the same columns as the project-level tab, filtered to this run.

## Chapter Logs workbook: Events

Use the same columns as the project-level tab, filtered to this run.

## Integrated Chapter Writing execution guards (append only)

Append missing fields at the right of Runs and chapter Run State; preserve historical values and headers:
`Chapter Writing Contract Version | Chapter Writing Execution Doc ID | Chapter Writing Execution Report Doc ID | Chapter Writing Execution Checks`

Resume JSON names: `chapter_writing_contract_version` (integer 1), `chapter_writing_execution_doc_id` (current Artifact A), `chapter_writing_execution_report_doc_id` (independent canonical clean evaluation report), `chapter_writing_execution_checks` (JSON object with exactly references_verified, story_architecture, write_format_humanize, story_integrity, formatted_document_verified set to true only after report and artifact verification). Blank historical values are unknown, not passing. Never advance an old snapshot into new Visual Placement by inventing receipts; complete targeted integrated writing/re-evaluation first. Preserve completed historical runs.

Append `Canonical Evaluation Report Doc ID | Canonical Revision ID | Chapter Writing Execution Receipt` to the same guard metadata. Resume JSON uses `canonical_evaluation_report_doc_id`, `canonical_revision_id`, `chapter_writing_execution_receipt`. Read back current A revision before handoff. The receipt is copied only from the matching independent evaluation report and contains `report_doc_id`, `artifact_doc_id`, `artifact_revision_id`, `status`, and `checks` with the five names each holding {passed: true, evidence: <specific section/paragraph or verification locator>}. The execution report ID must equal the current canonical evaluation report ID; revision and artifact IDs must match current A. Do not manufacture locators or reuse old report results after revision. These receipts prove recorded verified execution, not guaranteed model quality.


Presentation evidence is nested in chapter_writing_execution_receipt.presentation; record profile_id, baseline_doc_id/revision_id, current artifact_revision_id, native_validator_passed and locatable evidence. Store the revision-bound presentation plan/validator results with Notes and execution report. No new worksheet or pipeline node is required. Never backfill historical receipts with invented passing presentation evidence.
