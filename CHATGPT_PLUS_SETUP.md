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

1. Push this branch to a private GitHub repository and connect that repository to Codex Cloud.
2. Install the repository marketplace and `writing-agent-plus` plugin in Codex.
3. Connect the official Google Drive plugin to the book's Google account.
4. Import the control workbook template as a native Google Sheet in the project root.
5. Start a new ChatGPT Work or Codex cloud chat in this repository.
6. Say: `Use $writing-agent-plus to set up my Writing Agent project in Google Drive.`
7. After the preflight test passes, create the scheduled task using the prompt in
   `references/automation-prompt.md`.
8. Start the first supervised chapter with a small topic and approve each linked Doc explicitly.

Keep the first two chapters supervised. Do not remove Gumloop until Drive checkpoint recovery,
comments, approvals, and all six stages have succeeded twice.
