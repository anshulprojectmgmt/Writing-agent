# Google Sheets schema

Create one project-level `Writing Agent Control` workbook and one chapter-level `Logs` workbook.
All timestamps are ISO 8601 UTC. IDs are strings. Never reorder or rename columns after setup.

## Project Configuration

`Project ID | Project Name | Root Folder ID | Book Folder ID | Default Reviewers | Active | Updated At`

One active row per project. `Default Reviewers` is a comma-separated email list.

## Queue

`Run ID | Project ID | Topic | Details | Requested By | Chapter Folder ID | State | Current Stage | Pending Doc ID | Next Action | Not Before | Operation ID | Chat URL | Updated At`

Allowed queue states: `READY`, `RUNNING`, `AWAITING_APPROVAL`,
`AWAITING_BLUEPRINT_SELECTION`, `PAUSED_LIMIT`, `BLOCKED`, `COMPLETED`, and `CANCELLED`.

Only `READY`, recoverable `RUNNING`, and due `PAUSED_LIMIT` rows are eligible for a scheduled
transition. A user-facing command may also resume one selected row. Never guess when multiple rows
match.

## Runs

`Run ID | Topic | Details | Requested By | Chapter Folder ID | Logs Sheet ID | Resume Doc ID | Current Stage | State | Approved Broad Research Doc ID | Approved Research Analysis Doc ID | Approved Chapter Blueprint Doc ID | Approved Research Mapping Doc ID | Approved Deep Research Doc ID | Approved Chapter Writing Doc ID | Pending Doc ID | Pending Version | Last Checkpoint | Next Action | Not Before | Error Code | Error Summary | Updated At`

This row is the compact recovery record. Approval columns are written only after an explicit human
decision for the matching pending document.

## Decisions

`Timestamp | Run ID | Stage | Action | Doc ID | Actor | Choice | Source | Decision ID`

`Action` is `APPROVE`, `COMMENTS_READY`, `BLUEPRINT_CHOICE`, `RESUME`, or `CANCEL`. `Decision ID`
is stable and unique. Duplicate decisions with the same ID are ignored.

## Activity & Usage

`Started At | Finished At | Run ID | Stage | Role | Version | Attempt | Chat or Task ID | Model | Reasoning | Operation ID | Plan Usage Before | Plan Usage After | Estimated Effort | Outcome | Notes`

The ChatGPT plan does not expose reliable per-step token or credit usage to this workflow. Leave
unknown values blank. `Estimated Effort` may be `LOW`, `MEDIUM`, or `HIGH`; label it as an estimate.
Never convert an estimate into dollars or write an unavailable value as zero.

## Events

`Timestamp | Run ID | Event Type | Actor | Operation ID | Stage | Doc ID | Details`

Append-only. Include starts, checkpoints, artifact creation, evaluations, retries, pauses,
notifications, approvals, selections, resumptions, cancellations, and completion.

## Chapter Logs workbook: Artifact Log

`Node | Version | Subagent | Doc ID | Comment | Run ID | Attempt ID | Status | Created At | Operation ID`

## Chapter Logs workbook: Run State

Use the same columns as the project-level `Runs` tab for the selected run. This is an audit mirror;
the project workbook row and Resume Record control recovery if they disagree. Stop on disagreement
instead of overwriting either side.

## Chapter Logs workbook: Activity & Usage

Use the same columns as the project-level tab, filtered to this run.

## Chapter Logs workbook: Events

Use the same columns as the project-level tab, filtered to this run.
