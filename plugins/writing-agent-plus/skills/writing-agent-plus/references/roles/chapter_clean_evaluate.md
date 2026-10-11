# Chapter Clean Evaluate adapter

Read:
- Skill: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/instruction.md`
- Canonical rubric: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/references/rubrics/chapter_writing.yaml`
- Final rubric: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/references/rubrics/chapter_writing_final.yaml`

This role is report-only by design.

For canonical Artifact A use node_name `chapter_writing`.
For final Artifact B use node_name `chapter_writing_final` and also provide canonical Artifact A, Visual Review, and Visual Placement Report IDs for cross-document checks.

Never insert findings into either chapter Doc and never attach evaluator comments to the source artifact. Put all scores/findings in a separate native evaluation report under Chapter Writing.

Canonical evaluation verifies the integrated story/writing/formatting/internal-humanisation contract, all mandatory references and the five execution checks against actual Artifact A. Record verified results in the separate report; a missing gate blocks pass regardless of score.

Final evaluation verifies:
- approved structure/evidence preserved from Artifact A;
- completed prose, native emphasis, headings/icons and explanatory bullets preserved without a second style rewrite;
- final Doc contains no workflow/evaluator/visual-review metadata;
- all human visual decisions are accounted for in Placement Report;
- no EXCLUDE visual appears;
- failed KEEP visuals have explicit reasons and no substitute/generated/redrawn replacements.

Return evaluation-report metadata only. Controller owns Logs/routing.
