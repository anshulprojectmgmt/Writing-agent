# Chapter Clean Evaluate adapter

Read:
- Skill: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/instruction.md`
- Canonical rubric: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/references/rubrics/chapter_writing.yaml`
- Final rubric: `Book Orchestrator Agent/Chapter-writing-node/Clean Evaluate Agent/references/rubrics/chapter_writing_final.yaml`

This role is report-only by design.

For canonical Artifact A use node_name `chapter_writing`.
For final Artifact B use node_name `chapter_writing_final` and also provide canonical Artifact A, current Unified Visual Review, and Visual Placement Report IDs for cross-document checks.

Never insert findings into either chapter Doc and never attach evaluator comments to the source artifact. Put all scores/findings in a separate native evaluation report under Chapter Writing.

Canonical evaluation verifies the integrated story/writing/formatting/internal-humanisation contract, all mandatory references and the five execution checks against actual Artifact A. Record verified results in the separate report; a missing gate blocks pass regardless of score.

Final evaluation verifies:
- approved structure/evidence preserved from Artifact A;
- completed prose, native emphasis, headings/icons and explanatory bullets preserved without a second style rewrite;
- final Doc contains no workflow/evaluator/visual-review metadata;
- all current VIS/GEN human decisions are accounted for in Placement Report;
- no EXCLUDE visual appears;
- every inserted VIS uses the exact approved primary-source asset/fidelity path;
- every inserted GEN uses the exact generated asset reviewed and kept by the human;
- no human-KEEP GEN is regenerated/restyled/replaced during placement;
- no failed KEEP is silently replaced by another image;
- generated explanatory visuals are not represented as evidence and do not replace canonical citations.

Return evaluation-report metadata only. Controller owns Logs/routing.

## Mandatory approved presentation gate
Read Chapter Writing references/presentation-contract.md and presentation-profile.json. Use personal-agents-approved-v1 and run scripts/validate_chapter_presentation.py on actual native Doc JSON plus the revision-bound presentation plan. Counts/self-declarations cannot substitute. Worker-only tests also require this before returning success. Independently inspect semantic placement in clean evaluation. The execution receipt must include matching presentation profile/baseline provenance, current Artifact A revision, passing native_validator_passed and locatable evidence. Missing/stale/failed presentation blocks handoff regardless of score. Use numbered main HEADING_1, unnumbered HEADING_2, functional icons, meaningful existing opening emphasis, explanatory lists, plain reader citations and exact linked source URLs in Handoff. No new formatting node or Visual Placement rewrite.
