# One-time setup

Use this preflight before the first real chapter.

1. Confirm the user is signed into ChatGPT/Codex with the intended Plus account. This edition must
   not use an OpenAI API key.
2. Confirm Google Drive is connected and can access the managed book/project folder. Verify the
   account identity before any write.
3. Confirm the connected repository contains `Book Orchestrator Agent/` and this plugin.
4. Choose one Google Drive project root. Store its folder ID in the Project Configuration tab.
5. Create or verify a native Google Sheet named `Writing Agent Control` under that root. Create the
   tabs and headers in `sheet-schema.md` exactly once.
6. Create a native Google Doc named `Writing Agent Operating Instructions` and record the plugin
   version, repository branch, control-sheet ID, project-root ID, reviewer emails, and the statement
   that Google Drive is authoritative.
7. Run a test that creates and reads back one Doc, one Sheet row, and one native comment under a
   disposable Test chapter folder. Delete nothing automatically; the user may remove the test
   folder after inspection.
8. Create the scheduled cloud task from `automation-prompt.md`. A 30-minute cadence is recommended
   for recovery checks; the task remains quiet when nothing is actionable.

If any connector action is unavailable in the chosen ChatGPT Work/Codex surface, stop setup and
report the missing capability. Do not silently fall back to local files or browser automation for
production artifacts.

## Required repository files

The cloud task needs read access to:

- `plugins/writing-agent-plus/skills/writing-agent-plus/`
- `Book Orchestrator Agent/`

Keep the repository private if the book material is private. Every invited collaborator needs
their own ChatGPT access and Google Drive permission; subscription allowance is not shared between
users.
