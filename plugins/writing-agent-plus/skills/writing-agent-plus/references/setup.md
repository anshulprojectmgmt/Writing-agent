# One-time setup

Use this preflight before the first real chapter or after upgrading the production plugin schema.

1. Confirm the user is signed into ChatGPT/Codex with the intended Plus account. This edition must not use an OpenAI API key.
2. Confirm Google Drive is connected and can access the managed book/project folder. Verify account identity before any write.
3. Confirm the connected repository contains `Book Orchestrator Agent/` and this plugin on the intended production branch.
4. Choose one Google Drive project root. Store its folder ID in the Project Configuration tab.
5. Create or verify a native Google Sheet named `Writing Agent Control` under that root.
   - New setup: create tabs and headers from `sheet-schema.md`.
   - Existing setup: compare current headers with `sheet-schema.md`; append any missing columns to the right without renaming, deleting, reordering, or overwriting existing columns/values. Add newly allowed states/actions without rewriting historical rows.
   - Verify headers after the migration before starting a run.
6. Create or verify a native Google Doc named `Writing Agent Operating Instructions` and record plugin version, repository branch, control-sheet ID, project-root ID, reviewer emails, and that Google Drive is authoritative.
7. Verify the production branch contains the role adapters for `visual_research` (Visual Extraction), `visual_generation`, `visual_placement`, and `chapter_clean_evaluate`, plus the Book Orchestrator source roles they reference.
8. Verify `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/skill-sources.json` resolves the pinned full installed Adapt and Render packages from `anshulprojectmgmt/anshul-skills-registry`, including required references/assets. Fail setup if the exact pinned dependency cannot be read; do not silently fall back to only `prod/SKILL.md` or to remembered prompt text.
9. Run a disposable test that creates and reads back one Doc, one Sheet row, and one native comment under a Test chapter folder. Also verify a `Visual Assets` child folder and `Visual Assets/Generated` child can be created inside a test Deep Research folder. Delete nothing automatically; the user may remove the test folder after inspection.
10. Confirm ChatGPT native image generation is available for Visual Generation. Do not configure Runway or another external renderer as a fallback.
11. Create/confirm the scheduled cloud task from `automation-prompt.md` at hourly cadence. Verify its actual prompt, schedule and enabled status; installed instructions alone do not create a task. Keep it disabled until live recovery is requested or a production run is started.

Read `execution-policy.md` before setup. Validate actual model/reasoning/fork settings and an exported snapshot before dispatch. Log actual fresh task IDs rather than intended settings. Missing legacy guard metadata must be verified from artifacts; never infer passing evaluations for historical runs.

If a connector/action required by the pinned visual package or current ChatGPT Work/Codex surface is unavailable, stop setup and report the missing capability. Do not silently fall back to a different image generator, local-only artifact, or browser workaround in production.

## Required repository files

The cloud task needs read access to:
- `plugins/writing-agent-plus/skills/writing-agent-plus/`
- `Book Orchestrator Agent/`
- pinned `anshulprojectmgmt/anshul-skills-registry` dependency paths named in the Visual Generation manifest
- `WORK_START.md`

Keep repositories private if book material is private. Every collaborator needs their own ChatGPT access, Google Drive permission, and repository permission required to read pinned skill dependencies; subscription allowance is not shared between users.

For the integrated Chapter Writing upgrade, verify contract version 1 with `scripts/validate_chapter_contract.py` against the pinned production snapshot before dispatch. Load both bundled writing dependencies and the internal humanizer, plus all inner references. Append new execution/provenance columns from sheet-schema.md; retain historical blanks as unknown. Do not resume visual handoff with a stale receipt.
