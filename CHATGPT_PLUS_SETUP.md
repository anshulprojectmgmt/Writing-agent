# ChatGPT Plus / Codex setup

This branch is the no-API subscription edition. The separately preserved
`codex-cloud-automation` branch contains the paid hosted/API service.

## What this edition provides

- Six sequential writing stages with evaluation and immutable diagnose revisions.
- Human approval after every stage and an additional Blueprint selection gate.
- Google Drive, Docs, Sheets, and comments as durable storage.
- A control workbook, chapter Logs workbook, and Resume Record.
- Scheduled wake-ups that resume safe transitions and stay quiet while waiting for review.
- Checkpoint recovery after app closure, interrupted tasks, or plan-limit resets.

## Important limitation

ChatGPT Plus includes a usage allowance; it is not unlimited infrastructure. The automation can run
in cloud tasks while allowance remains. When a limit is reached it pauses until the plan resets.
Scheduled tasks are wake-ups rather than a permanently running server, and exact per-step credits
are not exposed programmatically.

## Files to use

- Plugin: `plugins/writing-agent-plus/`
- Marketplace: `.agents/plugins/marketplace.json`
- Control workbook template: `Writing-Agent-Control-Template.xlsx` from the delivered outputs
- Original role instructions: `Book Orchestrator Agent/`

## Quick start

The repository and Workspace control center are already prepared:

- Repository: `anshulprojectmgmt/Writing-agent`
- Branch: `chatgpt-plus-automation`
- Cloud bootstrap: `WORK_START.md`
- Writable Drive folder: `1mP719oQYn8NI-cAbt4yVlDJJW9z6NvVW`
- Native control Sheet: `1LWX1fzmiTAcACGTNgusgJL34jXYyuNt1dQB-IArI_Kc`

To start, open a new ChatGPT Work chat on the web and send:

`Use GitHub repo anshulprojectmgmt/Writing-agent, branch chatgpt-plus-automation. Read WORK_START.md and start the writing-agent workflow for this chapter topic: <replace with topic>.`

The bootstrap instructs the Work chat to perform the Drive preflight, create or confirm the
30-minute recovery task, and begin Broad Research. Approve each linked Doc explicitly. Keep the
first two chapters supervised; do not remove Gumloop until Drive checkpoint recovery, comments,
approvals, and all six stages have succeeded twice.
