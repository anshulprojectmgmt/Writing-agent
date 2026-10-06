# Research Mapping adapter

Read these repository files for the active role:

- Worker skill: `Book Orchestrator Agent/Research-mapping-node/mapping-research-to-chapter-3-3/SKILL.md`
- Worker instruction: `Book Orchestrator Agent/Research-mapping-node/mapping-research-to-chapter-3-3/instruction.md`
- Evaluator: `Book Orchestrator Agent/Research-mapping-node/Evaluate/SKILL.md`
- Evaluator rubric: `Book Orchestrator Agent/Research-mapping-node/Evaluate/references/rubrics/research_mapping.yaml`
- Diagnose: `Book Orchestrator Agent/Research-mapping-node/Diagnose/SKILL.md`
- Node contract: `Book Orchestrator Agent/Research-mapping-node/instruction.md`

Require the exact approved Broad Research and Chapter Blueprint Docs. Preserve the approved blueprint structure. Map existing evidence by subsection purpose fit, retain exact source URLs, label HIGH/MED fit, prevent duplicate-point reuse, and identify specific evidence GAPs.

## V2 hard boundary

This stage is evidence-only.

Never output or infer:
- IMAGE NEEDED / YES / NO
- visual ID
- image reason
- visual candidate or recommendation
- figure/screenshot recommendation
- image search/extraction instructions
- Human Decision fields.

Do not inspect sources to decide whether they contain usable figures. The source URL is carried forward as evidence provenance; downstream Visual Research performs visual inspection only after Deep Research.

Do not perform Deep Research or resolve GAPs here.

Replace Gumloop/Slack with connected Google Drive tools and publish a native immutable Research Mapping Doc in the Research Mapping folder.

Evaluate with the updated `research_mapping` rubric, including the V2 visual-boundary gate. Failed evaluation or human comments route to Diagnose and mandatory re-evaluation, capped at three Diagnose attempts per review cycle. A revised map that introduces visual-planning fields must fail evaluation.

Never allow Deep Research to start from a failed or unapproved mapping.

Return metadata only. Controller owns Sheets, checkpoints, and approval.
