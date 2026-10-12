# Visual Placement — preserve integrated writing

Read:
- Skill: `Book Orchestrator Agent/Chapter-writing-node/Visual Placement Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Chapter-writing-node/Visual Placement Agent/instruction.md`
- Image placement and preservation contract: `Book Orchestrator Agent/Chapter-writing-node/Visual Placement Agent/references/placement-contract.md`

Require:
- passing canonical Artifact A Doc ID;
- current resolved Unified Visual Review Doc ID;
- Visual Assets folder ID;
- Chapter Writing destination folder.

Any current VIS/GEN PENDING candidate blocks execution.

Create a NEW Artifact B; never overwrite or annotate Artifact A.

Preserve Artifact A reader-facing wording, voice and native formatting verbatim. Do not run a second LinkedIn rewrite. Preserve approved structure, evidence meaning, citations, statistics, examples, caveats, fixed punch lines, [TECH]/[WOW MOMENT], designated reader transformation, and counterargument. Conduct no new research.

Insert only human-KEEP assets and preserve candidate origin:
- `PRIMARY_SOURCE / VIS-*` -> exact approved primary-source asset; SOURCE-LINKED may be faithfully extracted now; no substitutes.
- `GENERATED_EXPLAINER / GEN-*` -> exact generated asset reviewed by the human; never rerun Adapt/Render, regenerate, restyle, edit or substitute it.

Omit EXCLUDE without replacement. If an exact KEEP asset cannot be inserted, record FAILED with a specific reason in the separate Visual Placement Report; never replace it with another image.

GEN figures are explanatory visuals based on already-cited subsection evidence. Caption/attribution must not present them as evidence or replace canonical citations.

Artifact B is clean reader-facing content only: no canonical Notes/Handoff/Completeness, evaluator metadata, candidate IDs, KEEP/EXCLUDE labels, extraction/generation state, or placement audit.

On final-artifact human feedback, regenerate Artifact B from Artifact A only for visual-placement/layout/caption changes. Route voice/prose/emphasis/formatting changes to integrated Chapter Writing via canonical revision. If feedback changes facts/evidence/citations/stats/claims/caveats/fixed punch lines/approved structure/designated transformation, return `Requires canonical revision` rather than creating a contradictory final-only patch.

Return final Doc ID + Placement Report metadata to Chapter Writing controller. Controller writes durable state.
