# Visual Placement + LinkedIn Style adapter

Read:
- Skill: `Book Orchestrator Agent/Chapter-writing-node/Visual Placement Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Chapter-writing-node/Visual Placement Agent/instruction.md`
- LinkedIn style reference: `Book Orchestrator Agent/Chapter-writing-node/Visual Placement Agent/references/linkedin-writing-style.md`

Require:
- passing canonical Artifact A Doc ID;
- current resolved Visual Review Doc ID;
- Visual Assets folder ID;
- Chapter Writing destination folder.

Any PENDING candidate blocks execution.

Create a NEW Artifact B; never overwrite or annotate Artifact A.

Transform only reader-facing presentation/voice to the approved LinkedIn-derived style. Preserve approved structure, evidence meaning, citations, statistics, examples, caveats, fixed punch lines, [TECH]/[WOW MOMENT], designated reader transformation, and counterargument. Conduct no new research.

Insert only human-KEEP visuals. Omit EXCLUDE without replacement. For KEEP, use exact primary-source assets only. If exact-source insertion cannot be completed, record FAILED with a specific reason in the separate Visual Placement Report; never substitute, redraw, regenerate, or use a secondary copy.

Artifact B is clean reader-facing content only: no canonical Notes/Handoff/Completeness, evaluator metadata, VIS IDs, KEEP/EXCLUDE labels, extraction state, or placement audit.

On final-artifact human feedback, regenerate Artifact B from Artifact A only for presentation/voice/formatting/visual-placement changes. If feedback changes facts/evidence/citations/stats/claims/caveats/fixed punch lines/approved structure/designated transformation, return `Requires canonical revision` rather than creating a contradictory final-only patch.

Return final Doc ID + Placement Report metadata to the Chapter Writing controller. The controller writes durable state.
