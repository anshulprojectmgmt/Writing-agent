# One-time setup

Use this preflight before the first real chapter or after upgrading the production plugin schema.

1. Confirm the user is signed into ChatGPT/Codex with the intended Plus account. This edition must not use an OpenAI API key.
2. Confirm Google Drive is connected and can access the managed book/project folder. Verify account identity before any write.
3. Confirm the connected repository contains `Book Orchestrator Agent/` and this plugin on the intended production branch.
4. Choose one Google Drive project root. Store its folder ID in the Project Configuration tab.
5. Create or verify a native Google Sheet named `Writing Agent Control` under that root.
   - New setup: create tabs and headers from `sheet-schema.md`.
   - Existing setup: compare current headers with `sheet-schema.md`; append any missing V2 columns to the right without renaming, deleting, reordering, or overwriting existing columns/values. Add newly allowed states/actions without rewriting historical rows.
   - Verify headers after the migration before starting a run.
6. Create or verify a native Google Doc named `Writing Agent Operating Instructions` and record plugin version, repository branch, control-sheet ID, project-root ID, reviewer emails, and that Google Drive is authoritative.
7. Verify the production branch contains the V2 role adapters for `visual_research`, `visual_placement`, and `chapter_clean_evaluate`, plus the Book Orchestrator source roles they reference.
8. Run a test that creates and reads back one Doc, one Sheet row, and one native comment under a disposable Test chapter folder. Also verify a `Visual Assets` child folder can be created inside a test Deep Research folder. Delete nothing automatically; the user may remove the test folder after inspection.
9. Create/confirm the scheduled cloud task from `automation-prompt.md`. A 30-minute cadence is recommended for recovery checks; it stays quiet when nothing is actionable.

If a connector action is unavailable in the selected ChatGPT Work/Codex surface, stop setup and report the missing capability. Do not silently fall back to local files or browser automation for production artifacts.

## Required repository files

The cloud task needs read access to:
- `plugins/writing-agent-plus/skills/writing-agent-plus/`
- `Book Orchestrator Agent/`
- `WORK_START.md`

Keep the repository private if book material is private. Every collaborator needs their own ChatGPT access and Google Drive permission; subscription allowance is not shared between users.
