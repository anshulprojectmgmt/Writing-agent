# Codex runtime contract

This reference captures the runtime decisions used for the completed Codex rerun. It is authoritative for host integration only. Keep all original stage skills, instructions, voice references and rubrics unchanged. Do not allow a legacy folder ID, Slack requirement, Gumloop tool spelling or older model table to override this contract.

## Models

| Role | Actual model | Reasoning |
|---|---|---|
| Main orchestrator and node controllers | gpt-6-terra | medium |
| Broad Research worker | gpt-6-sol | low |
| Research Analysis worker | gpt-6-sol | medium |
| Chapter Blueprint worker, including options continuation | gpt-6-sol | medium |
| Research Mapping worker | gpt-6-sol | low |
| Deep Research worker | gpt-6-sol | low |
| Chapter Writing worker | gpt-6-sol | medium |
| Evaluate and Diagnose | gpt-6-sol | low |

Never use Astra, Luna or GPT-5.x. If Terra cannot be selected, disclose the substitution and use Sol low for controllers only. If a required Sol worker or reasoning setting is unavailable, stop before it, explain, and ask for direction. Set model/reasoning in actual host controls, not worker prose. If the host cannot set the main session's model, tell the user what selection is required; do not falsely record Terra.

## Account, location and adapters

- Resolve the receiving user's connected Google account at setup and pass its real connector selector to every Drive/Docs/Sheets call. If several accounts are possible, get a choice. Never carry over any account or artifact ID from another run.
- Create a fresh standalone chapter folder at My Drive root unless the user supplies a parent. The legacy book-folder ID in instruction.md is inactive for Codex. Create Logs inside the chapter folder. Create/reuse only the receiving user's own Writing Agent Control; inspect its schema before writing. If an existing same-title sheet is ambiguous, ask instead of picking one.
- Node folders are Broad Research, Research Analysis, Chapter Blueprint, Research Mapping, Deep Research and Chapter Writing. Put each node's artifact, HTML source and evaluation report there, flat, not in the chapter root. Approved upstream Docs are read-only.
- Legacy Gumloop gdocs, Drive, web_search/firecrawl and filesystem names denote required operations, not callable Codex tools. Use exposed equivalent tools for direct document reads, HTML-file-to-native-Doc conversion, section edits, comment reads/writes, folder management and real web research. Discover real tool schemas; do not invent calls or use unrelated credentials.
- Read applicable Google Drive/Docs/Sheets/comment skills before operations. HTML import must preserve the stage formatting reference. Verify the resulting native Doc and folder placement. An HTML file or DOCX link alone is not a completed node.
- Verify native comments on the Setup Verification Doc before research. If only unanchored file comments are available, disclose the missing anchor capability and stop for permission to accept a deviation; do not label them anchored or silently treat them as equivalent. Keep all content writes before the final comment pass, as Evaluate specifies.
- Deliver review notifications and collect decisions in the active chat. Slack is not required; do not send external notifications without the receiving user's request. Node controller final JSON remains unchanged.

## Sheets: exact schemas from the completed run

Use row 1 as headers. Resolve columns by header name, never remembered letters. A newly created sheet uses the exact ordered headers below. For an existing sheet, preserve formulas/formatting and map its actual headers; do not blindly replace it. Inspect metadata and bounded target ranges before writes, then read back.

Logs: Node | Version | Subagent | Doc ID | Comment

Project Configuration: Project ID | Project Name | Root Folder ID | Book Folder ID | Default Reviewers | Active | Updated At

Queue: Run ID | Project ID | Topic | Details | Requested By | Chapter Folder ID | State | Current Stage | Pending Doc ID | Next Action | Not Before | Operation ID | Chat URL | Updated At

Runs: Run ID | Topic | Details | Requested By | Chapter Folder ID | Logs Sheet ID | Resume Doc ID | Current Stage | State | Approved Broad Research Doc ID | Approved Research Analysis Doc ID | Approved Chapter Blueprint Doc ID | Approved Research Mapping Doc ID | Approved Deep Research Doc ID | Approved Chapter Writing Doc ID | Pending Doc ID | Pending Version | Last Checkpoint | Next Action | Not Before | Error Code | Error Summary | Updated At

Decisions: Timestamp | Run ID | Stage | Action | Doc ID | Actor | Choice | Source | Decision ID

Activity & Usage: Started At | Finished At | Run ID | Stage | Role | Version | Attempt | Chat or Task ID | Model | Reasoning | Operation ID | Plan Usage Before | Plan Usage After | Estimated Effort | Outcome | Notes

Events: Timestamp | Run ID | Event Type | Actor | Operation ID | Stage | Doc ID | Details

Populate ALL tabs from setup onward; they are not decorative placeholders. Project Configuration identifies this account's project and location; standalone mode leaves Book Folder ID blank. Queue and Runs contain one row per run. Decisions and Events append auditable rows. Activity & Usage records each actual controller/worker/evaluator/diagnoser attempt, including errors; distinguish intended settings from verified actual settings. Plan usage is unknown when not exposed; never infer token/credit counts from prose length. Estimated Effort is qualitative, not measured credits.

Each artifact/evaluator/diagnoser return gets a Logs row before further routing. Evaluate rows contain the evaluation report ID, reviewed version and score/verdict. Approval rows record the artifact ID; do not overwrite evaluator rows. Use a deterministic operation ID per run/stage/role/version/attempt and decision ID per decision to prevent duplicate appends on resume. Inspect for an already recorded operation before appending. Separate IDs for artifact, report and approved output.

Use one distinct, readable light row fill for this chapter across tabs, and a different fill for any earlier chapter. Preserve headers; use a legend/notes for the colour mapping. Do not colour or overwrite unrelated columns. Native formatting must not encode workflow state instead of explicit values.

## Durable recovery

Create a Resume State Google Doc in the chapter folder and record its ID in Runs. Store source commit, workflow_source_root (environment-local and re-resolvable), runtime version, account email/selector, folder/sheet IDs, actual settings, all approved outputs, pending artifact/report/version, blueprint choice, latest operation, and recovery automation ID/status. Account selectors may change in a new host: re-resolve by account email, never reuse a stale selector blindly. Keep credentials out of checkpoints and source control.

Write checkpoint state after setup, before dispatch, after artifact creation, after evaluation, after revision and after approval. Use BEFORE_WORKER, AFTER_WORKER, AFTER_EVALUATE, AWAITING_BLUEPRINT_CHOICE, AWAITING_APPROVAL, AFTER_DIAGNOSE, BLOCKED or WORKFLOW_COMPLETE. State is RUNNING, AWAITING_BLUEPRINT_CHOICE, AWAITING_APPROVAL, BLOCKED, RETRYABLE or COMPLETED as appropriate. Pending IDs are never promoted to approved without a recorded explicit decision.

If real automations are exposed, create one recovery task for this run, at most hourly. Its prompt must name the receiving run ID and control/Logs IDs, reconcile state, and never cross a human gate. Record actual task ID, enabled state, schedule and notification context in Resume State and Events; show these in chat. A rate-limit checkpoint may set Not Before to five hours after the observed failure; the hourly recovery task respects that timestamp. Do not claim exact-time execution, a guaranteed limit reset or unavailable credits.

Automatic recovery reconciles metadata only when headless and unable to gather human approval. Resume production only when the host supports the required interactive review handoff and execution tools; otherwise notify the user to return to the original chat. Never start a new production run in a detached context without a review path.

On resume: re-resolve account, pinned instructions and all actual artifacts; check latest Decisions and Logs; respect Not Before; reconcile completed external writes before retrying. Never duplicate workers because a return was lost. If a task is still active, wait/check rather than start another. Record lease owner and expiry in Resume State, verify ownership before dispatch, and use a single recovery task; if competing runners are observed, stop. Sheets/Docs are not transactional locks—do not claim exactly-once execution or concurrent-runner safety from this lease alone.

If automations are absent, state AUTO_RECOVERY_UNAVAILABLE and offer manual resume using the control link. Do not call a sheet a working scheduler. Disable only this run's real automation after final approval. Do not alter someone else's automation.

## Human exceptions

Evaluation failures normally route to Diagnose and fresh Evaluate. A user may explicitly approve a named version as an exception. Record APPROVE_EXCEPTION, failed verdict/score, unresolved issues and required downstream caveats in Decisions, Events, Logs and Resume State. Never reuse the completed run's exception approvals as precedent or fabricate a pass. Do not expand blueprint structure to hide an evidence gap.
