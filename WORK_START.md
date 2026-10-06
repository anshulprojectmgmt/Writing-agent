# Writing Agent — ChatGPT Work bootstrap

This file is the cloud entry point for the subscription-only writing agent. It is intentionally separate from the paid hosted/API implementation on the `codex-cloud-automation` branch.

## Start contract

When a user supplies a chapter topic, act as the deterministic controller for the six-stage Products of Tomorrow writing pipeline. Use the connected GitHub repository for instructions and connected Google Drive work account for durable state/artifacts. Do not request an OpenAI API key, require a local process, or use Google Cloud.

Read these repository files before the first transition:

1. `plugins/writing-agent-plus/skills/writing-agent-plus/SKILL.md`
2. `plugins/writing-agent-plus/skills/writing-agent-plus/pipeline.json`
3. `plugins/writing-agent-plus/skills/writing-agent-plus/references/workflow.md`
4. `plugins/writing-agent-plus/skills/writing-agent-plus/references/sheet-schema.md`
5. The matching adapter under `plugins/writing-agent-plus/skills/writing-agent-plus/references/roles/` immediately before each worker/evaluator/diagnose/visual role.
6. Original role material under `Book Orchestrator Agent/` whenever the active adapter points to it.

The plugin adapters define subscription-runtime routing. The original Book Orchestrator role packages remain authoritative for research, writing, rubrics, formatting, visual rules, and diagnosis details referenced by the adapters.

## Connected Workspace resources

- Google account: `anuragsingh@realtyai.net`
- Writable automation root folder: `1mP719oQYn8NI-cAbt4yVlDJJW9z6NvVW`
- Control Sheet: `1LWX1fzmiTAcACGTNgusgJL34jXYyuNt1dQB-IArI_Kc`
- Control Sheet URL: `https://docs.google.com/spreadsheets/d/1LWX1fzmiTAcACGTNgusgJL34jXYyuNt1dQB-IArI_Kc/edit`
- Operating instructions Doc: `1IUW9iVeiydK5hhQMLitzI_f0yVqDkBzO_J7qUFzJX1U`
- Historical book folder (read-only reference): `15opxb3JylDl2S9gnlSXa9HiQ4ox_ycWq`
- Default reviewer: `anuragsingh@realtyai.net`

The historical book folder is readable but the connected work account cannot add children there. Create every new chapter folder, stage folder, Google Doc, Logs Sheet, Visual Assets folder, and Automation Resume Record under the writable automation root. Never fall back to a personal Drive account.

## First action for a new topic

1. Read `Project Configuration!A:G` in the Control Sheet and select the active `products-of-tomorrow` row.
2. Confirm the Control Sheet has `Project Configuration`, `Queue`, `Runs`, `Decisions`, `Activity & Usage`, and `Events` tabs, upgraded to the current schema where required.
3. Resolve existing runs by exact topic/project. If no active matching run exists, create a stable run ID, append queued row, and create one unambiguous chapter folder under writable root. If exactly one active run exists, resume it. If several active runs match, show a short picker instead of guessing.
4. Inside chapter folder create/reuse standard six stage folders, chapter Logs workbook, and `Automation Resume Record` Google Doc. Never overwrite an earlier artifact version.
5. Run one main stage at a time in this order:
   Broad Research → Research Analysis → Chapter Blueprint → Research Mapping → Deep Research → Chapter Writing.

Every main stage retains:
`Create → Evaluate → Diagnose if failed/revised → Re-evaluate → Human approval`

Blueprint additionally pauses for A/B/C/mix/comments before completing the selected blueprint.

## V2 boundaries and internal subflows

### Research Mapping
Evidence mapping only. No IMAGE NEEDED, image yes/no, visual candidates, visual reasons, visual recommendations, image search, or extraction.

### Deep Research
After the canonical Deep Research Package passes, continue inside the same main stage:

`Deep Research → Evaluate → Visual Research → Evaluate Visual → Human Visual Review`

Visual Research inspects only the exact primary sources mapped to each subsection plus a primary source added by Deep Research specifically to fill that subsection's mapped GAP.

Candidate selection uses only:
1. directly explains the subsection;
2. contains meaningful data, mechanism, or comparison;
3. strong enough to improve the chapter.

Selection precedes extraction. Do not reject a qualifying visual because extraction is difficult. Persist exact-source assets in `Deep Research/Visual Assets` where possible; otherwise keep the candidate FOUND + SOURCE-LINKED with exact source/locator.

Do not start Chapter Writing until:
- the exact Deep Research Package is explicitly approved; and
- every FOUND Visual Review candidate is KEEP or EXCLUDE.

### Chapter Writing
Produce and preserve two separate chapter artifacts:

Artifact A — canonical Anshul-style output from the unchanged `anshul-chapter-writing-4` worker and original bundled references.

Artifact B — NEW reader-facing output created only after Artifact A passes; Visual Placement rewrites presentation into the approved LinkedIn-derived style and inserts only human-KEEP visuals.

Evaluate both through the Chapter Clean Evaluate Agent. Evaluators write separate reports only and never inject findings into either chapter Doc.

Artifact B is the Chapter Writing main-stage pending/approved Doc. Preserve Artifact A separately in Logs/Run State.

## Durable state and recovery

Before and after every Drive write/workflow transition, update Control Sheet, chapter Logs, and Automation Resume Record using stable operation IDs. Reconcile uncertain operations before repeating them. Google Docs contain content; controller/chat messages carry only IDs, links, scores, decisions, and short status summaries.

At authorized live setup or production startup, create or confirm recurring ChatGPT Work task `Writing Agent Recovery` using `plugins/writing-agent-plus/skills/writing-agent-plus/references/automation-prompt.md` at hourly cadence. Verify its actual prompt, schedule and enabled status. Installation alone does not enable recovery. It processes at most one eligible transition and remains quiet when none is available. It must never bypass approval, blueprint-selection, or visual-review gates. Read `references/execution-policy.md` in the same skill for actual model settings, mandatory fresh role contexts, and transition guards.

If a temporary plan limit interrupts a run, checkpoint it. Resume later from exact pending transition after reconciliation. Subscription limits cannot be bypassed and no API credits may be purchased/used.

## User interaction

Do not ask the user to install/deploy/clone/run/configure anything during a workflow run. Ask only for genuine content decisions, stage approval, blueprint choice, visual KEEP/EXCLUDE decisions, or permissions the connected account lacks.

Notify the user when:
- a stage Doc needs approval;
- a Blueprint choice is needed;
- a Visual Review needs KEEP/EXCLUDE decisions;
- the run completes;
- the workflow is blocked.

The normal opening message is:
`Start the writing-agent workflow for this chapter topic: <topic>`

After receiving it, perform preflight and begin Broad Research.
