# Research Mapping adapter

Read these repository files for the active role only:

- Worker: `Book Orchestrator Agent/Research-mapping-node/mapping-research-to-chapter-3-3/SKILL.md`
- Evaluator: `Book Orchestrator Agent/Research-mapping-node/Evaluate/SKILL.md`
- Diagnose: `Book Orchestrator Agent/Research-mapping-node/Diagnose/SKILL.md`
- Node contract: `Book Orchestrator Agent/Research-mapping-node/instruction.md`

Require the exact approved Broad Research and Chapter Blueprint Docs. Preserve the blueprint's
structure. Map existing evidence to chapter sections and identify evidence gaps; do not perform the
Deep Research stage here. Replace Gumloop and Slack with connected Google Drive tools and publish a
native immutable mapping Doc in the Research Mapping folder.

Evaluate with the research_mapping rubric. A failed evaluation or human comments routes to Diagnose,
which creates the next version followed by mandatory re-evaluation. Maximum three Diagnose attempts
per review cycle. Never allow Deep Research to start from a failed or unapproved mapping.

Return metadata only. The controller owns Sheets, checkpoints, and approval.
