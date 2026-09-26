# Chapter Blueprint adapter

Read these repository files for the active role only:

- Worker: `Book Orchestrator Agent/Chapter-blueprint-node/Chapter Blueprint Agent/SKILL.md`
- Evaluator: `Book Orchestrator Agent/Chapter-blueprint-node/Evaluate/SKILL.md`
- Diagnose: `Book Orchestrator Agent/Chapter-blueprint-node/Diagnose/SKILL.md`
- Node contract: `Book Orchestrator Agent/Chapter-blueprint-node/instruction.md`

Use the exact approved Research Analysis Doc as primary source and approved Broad Research Doc as
secondary source. Do not run fresh research. Replace Gumloop and Slack with connected Drive tools.

The worker first publishes a native `Chapter Blueprint Options V1` Doc with three structural
alternatives and returns an options checkpoint. The controller records
`AWAITING_BLUEPRINT_SELECTION` and asks for A, B, C, a mixture, or comments. Resume the same worker
operation with the exact recorded choice. The complete blueprint retains all three alternatives,
an explicit selection record, and the fully expanded selected structure.

Evaluate only the complete canonical blueprint with the chapter_blueprint rubric. Failed evaluation
or human feedback routes to Diagnose and mandatory re-evaluation, capped at three Diagnose attempts
per review cycle. The final passing Doc still requires explicit approval.

Return metadata only. The controller owns Sheets, checkpoints, selection records, and approval.
