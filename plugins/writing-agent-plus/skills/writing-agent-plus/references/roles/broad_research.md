# Broad Research adapter

Read these repository files for the active role only:

- Worker: `Book Orchestrator Agent/Broad-research-node/broad-research-agent/SKILL.md`
- Evaluator: `Book Orchestrator Agent/Broad-research-node/Evaluate/SKILL.md`
- Diagnose: `Book Orchestrator Agent/Broad-research-node/Diagnose/SKILL.md`
- Node contract: `Book Orchestrator Agent/Broad-research-node/instruction.md`

Replace all Gumloop, Slack, and raw API actions with connected web research and Google Drive tools.
The worker receives topic, details, Broad Research folder ID, version, and operation ID. It performs
fresh web research from real sources, preserves the Source Ladder and evidence-card rules, and
publishes a native versioned Doc. Web search is permitted.

Evaluate the resulting Doc with the broad_research rubric. A pass requires a valid score/verdict
and all mandatory checks; contradictory metadata is blocked. A failure routes to Diagnose against
the research Doc and evaluation report. Diagnose reads evaluation findings or human comments from
Drive and creates the next immutable version. Maximum three Diagnose attempts per review cycle.

Return only version, artifact Doc ID, evaluation report ID/score/verdict when applicable, and the
operation receipt. The controller, not this role, writes Sheets or collects approval.
