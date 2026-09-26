# Writing Agent — ChatGPT Work bootstrap

This file is the cloud entry point for the subscription-only writing agent. It is intentionally
separate from the paid hosted/API implementation on the `codex-cloud-automation` branch.

## Start contract

When a user supplies a chapter topic, act as the deterministic controller for the six-stage
Products of Tomorrow writing pipeline. Use the connected GitHub repository for instructions and
the connected Google Drive work account for durable state and artifacts. Do not request an OpenAI
API key, do not require a local process, and do not use Google Cloud.

Read these repository files before the first transition:

1. `plugins/writing-agent-plus/skills/writing-agent-plus/SKILL.md`
2. `plugins/writing-agent-plus/skills/writing-agent-plus/pipeline.json`
3. `plugins/writing-agent-plus/skills/writing-agent-plus/references/workflow.md`
4. `plugins/writing-agent-plus/skills/writing-agent-plus/references/sheet-schema.md`
5. The matching file in `plugins/writing-agent-plus/skills/writing-agent-plus/references/roles/`
   immediately before each stage.
6. The original Gumloop role material under `Book Orchestrator Agent/` only when a migrated role
   file points to it or a style comparison is required.

## Connected Workspace resources

- Google account: `anuragsingh@realtyai.net`
- Writable automation root folder: `1mP719oQYn8NI-cAbt4yVlDJJW9z6NvVW`
- Control Sheet: `1LWX1fzmiTAcACGTNgusgJL34jXYyuNt1dQB-IArI_Kc`
- Control Sheet URL:
  `https://docs.google.com/spreadsheets/d/1LWX1fzmiTAcACGTNgusgJL34jXYyuNt1dQB-IArI_Kc/edit`
- Operating instructions Doc: `1IUW9iVeiydK5hhQMLitzI_f0yVqDkBzO_J7qUFzJX1U`
- Historical book folder (read-only reference): `15opxb3JylDl2S9gnlSXa9HiQ4ox_ycWq`
- Default reviewer: `anuragsingh@realtyai.net`

The historical book folder is readable but the connected work account cannot add children there.
Create every new chapter folder, stage folder, Google Doc, Logs Sheet, and Automation Resume Record
under the writable automation root. Never fall back to a personal Drive account.

## First action for a new topic

1. Read `Project Configuration!A:G` in the Control Sheet and select the active
   `products-of-tomorrow` row.
2. Confirm the Control Sheet has `Project Configuration`, `Queue`, `Runs`, `Decisions`,
   `Activity & Usage`, and `Events` tabs.
3. Resolve existing runs by exact topic and project. If no active matching run exists, create a
   stable run ID, append a queued row, and create one unambiguous chapter folder under the writable
   automation root. If exactly one active run exists, resume it. If several active runs match, show
   a short picker instead of guessing.
4. Inside the chapter folder create the standard stage folders, the chapter Logs workbook, and an
   `Automation Resume Record` Google Doc. Never overwrite an earlier artifact version.
5. Run one stage at a time in this order:
   Broad Research → Research Analysis → Chapter Blueprint → Research Mapping → Deep Research →
   Chapter Writing.

Every stage must follow:

`Create → Evaluate → Diagnose if failed or revised → Re-evaluate → Human approval`

Do not start a downstream stage unless the expected artifact exists in the authorized chapter
folder, evaluation passes, the approved document is the latest immutable version, and the reviewer
explicitly approves that exact document. The Blueprint stage additionally waits for A, B, C, a
mixture, or comments before completing the chosen blueprint.

## Durable state and recovery

Before and after every Drive write or workflow transition, update the Control Sheet, chapter Logs,
and Automation Resume Record using stable operation IDs. Reconcile an uncertain operation before
repeating it. Google Docs contain the content; chat messages carry only IDs, links, scores, and
short status summaries.

At startup, create or confirm a recurring ChatGPT Work task named `Writing Agent Recovery` using
the prompt in
`plugins/writing-agent-plus/skills/writing-agent-plus/references/automation-prompt.md` with a
30-minute cadence. The recovery task processes at most one eligible transition and must stay quiet
when no action is available. It must never bypass a human approval or blueprint-selection gate.

If a temporary ChatGPT plan limit interrupts a run, leave the run checkpointed. On the next
scheduled invocation after capacity returns, reconcile Drive and continue from the exact pending
transition. A subscription limit cannot be bypassed and no API credits may be purchased or used.

## User interaction

Do not ask the user to install, deploy, clone, run, or configure anything. Ask only for a genuine
content decision, approval, blueprint choice, or a permission that the connected account actually
lacks. Notify the user when a document needs review, a blueprint choice is needed, the run
completes, or the workflow is blocked.

The normal opening message is:

`Start the writing-agent workflow for this chapter topic: <topic>`

After receiving that message, perform the preflight and begin Broad Research.
