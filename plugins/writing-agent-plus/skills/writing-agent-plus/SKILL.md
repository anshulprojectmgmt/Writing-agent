---
name: writing-agent-plus
description: Run or resume the Products of Tomorrow six-stage chapter workflow in ChatGPT Work or Codex using the signed-in ChatGPT plan and connected Google Drive. Use when the user starts a chapter, checks a run, approves a stage, requests a comment-driven revision, selects a blueprint, or resumes after a usage limit. Do not use an OpenAI API key or external cloud service.
---

# Writing Agent Plus

This is the subscription edition. It runs inside ChatGPT Work or Codex with the user's included
allowance. Never request an OpenAI API key, start the hosted FastAPI edition, or claim guaranteed
24x7 execution. Google Drive is the durable system of record; local files are recoverable scratch.

Before the first run, read `references/setup.md`. For a start, resume, approval, revision, status,
or scheduled check, read `references/workflow.md` and `references/sheet-schema.md`. Read the role
adapter for only the stage being executed. The original role packages live under
`Book Orchestrator Agent/` in the connected repository and remain authoritative for research,
rubrics, voice, formatting, and diagnosis details unless this subscription adapter replaces a
Gumloop, Slack, API, or storage instruction.

For every Evaluate or Diagnose role, also read `references/safe-evaluation.md`. Its read-only
artifact and report-first rules replace any original instruction to inject generated findings,
color text, or attach evaluator comments to the source artifact.

## Fixed pipeline

Run sequentially, never in parallel:

1. `broad_research`
2. `research_analysis`
3. `chapter_blueprint`
4. `research_mapping`
5. `deep_research`
6. `chapter_writing`

Each stage follows Create -> Evaluate -> Diagnose if failed -> Re-evaluate -> explicit human
approval. Every human revision also creates a new immutable version and must pass evaluation.
Chapter Blueprint has an additional structure-selection pause before its full V1 is completed.

## Invocation modes

- **Start:** require topic and useful chapter details. Resolve or create one chapter folder, its six
  stage folders, `Logs`, and `Automation Resume Record`. Stop on ambiguous folder matches.
- **Continue:** read the Run State row and Resume Record, reconcile the last operation with actual
  Drive artifacts, then perform only the recorded next transition.
- **Approve:** accept only an explicit decision for the exact latest pending Doc ID. Record it
  before advancing.
- **Revise:** require the reviewer to have added Google Docs comments. Run Diagnose on the exact
  pending Doc, publish a new version, evaluate it, and return to approval.
- **Status:** report metadata and links from the sheets. Do not read or summarize artifact prose.
- **Scheduled check:** process at most one eligible run transition. Leave approval rows untouched.

## Isolation and delegation

The controller carries identifiers and status only. Never place research, analysis, evidence,
draft prose, evaluation findings, or comment text into controller messages or the Queue sheet.
When isolated subagents are available, start a fresh context for every worker, evaluator, and
diagnose attempt and tell it to read the applicable adapter file. Do not fork conversation history.
When isolated execution is unavailable, perform one role at a time and clear role-specific scratch
before switching; retain only IDs and receipts in controller state.

## Google rules

Use the connected Google Drive, Docs, Sheets, and comments tools. Confirm the selected Google
account and project-root access before writes. Agents receive document functions, not raw Google
credentials. Every created artifact must be a native Google Doc or Sheet under the authorized
chapter folder. Verify ID, MIME type, parent, and readability after creation. Never overwrite a
prior version.

The workbook tabs and exact columns are defined in `references/sheet-schema.md`. Firestore does not
exist in this edition. The `Queue` and `Run State` tabs plus the Resume Record are authoritative.
Before and after each external side effect, write a checkpoint with a stable operation ID. On an
uncertain result, search for that operation ID and reconcile before retrying.

## Human gates

After a passing evaluation, set the run to `AWAITING_APPROVAL`, save the exact pending Doc ID, and
return a short notification containing stage, version, score, and Doc link. Do not advance because
the document passed evaluation. Silence, a scheduled wake-up, or an old approval never counts.

For Blueprint options, set `AWAITING_BLUEPRINT_SELECTION` and ask for A, B, C, a mixture, or
comment instructions. Resume the same blueprint operation with the recorded choice. The final
blueprint still needs evaluation and approval.

## Limits and recovery

The ChatGPT plan controls usage. Precise token or credit consumption is not programmatically
available to this skill. Record known task metadata and leave unavailable usage cells blank—never
write zero as a guess. If a limit interrupts work, the next scheduled run reconciles artifacts and
continues from the pre-side-effect checkpoint. Set `PAUSED_LIMIT`, record the visible reset time if
available, and never attempt to bypass the limit or purchase credits.

Scheduled tasks are wake-ups, not a continuously running server. They may be delayed or unable to
run while allowance is exhausted. Human approval always resumes from the same persistent chapter
chat when possible.

## Safety invariants

- Never advance after a failed, missing, or malformed evaluation.
- Never approve a stale or superseded document.
- Never exceed three Diagnose attempts in one review cycle.
- Never create the same external artifact twice for one operation ID.
- Never move an artifact outside the authorized project root.
- Never use Gumloop, Slack, OpenAI API keys, Agents API, Cloud Run, or Terraform in this edition.
- Never claim the full chapter is complete until all six latest Docs are explicitly approved.

On completion, report the topic, chapter folder, Logs workbook, Resume Record, and the six approved
Doc IDs/links.
