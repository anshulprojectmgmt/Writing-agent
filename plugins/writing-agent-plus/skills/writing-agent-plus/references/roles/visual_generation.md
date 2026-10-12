# Visual Generation V3 adapter

Read:
- Skill: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/SKILL.md`
- Instruction: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/instruction.md`
- Selector rubric: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/generation-mode-selector.md`
- Data lock: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/data-lock-contract.md`
- Generated visual contract: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/generated-visual-contract.md`
- Unified review format: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/unified-visual-review-format.md`
- Generated evaluator rubric: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/rubrics/generated_visual.yaml`
- Unified review rubric: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/rubrics/unified_visual_review_v3.yaml`
- Pinned skill manifest: `Book Orchestrator Agent/Deep-research-node/Visual Generation Agent/references/skill-sources.json`

This is the third and final durable sub-agent inside Deep Research.

Require the current passing Deep Research Package and current passing Source Visual Review from Visual Extraction.

## Production behavior

1. Select fallback-generation targets only where the subsection has no usable EXTRACTED primary-source visual.
2. Apply the short DATA/TOPIC/HUMOUR selector and publish Visual Generation Plan.
3. For each target separately, run the full pinned installed `adapt-linkedin-visual-content` package in a fresh context using only that subsection's evidence.
4. For that candidate separately, run the full pinned installed `render-linkedin-visual-post` package in another fresh context using Article-section mode and ChatGPT native image generation.
5. Evaluate the actual rendered asset in another fresh context. Maximum two render attempts.
6. Publish Generated Visual Manifest.
7. Build Unified Visual Review from unchanged VIS candidates plus only passing GEN candidates.
8. Verify Unified Visual Review in a fresh context.

Do not expose one candidate's Adapt/Render/evaluation conversation to another candidate. Do not batch images or create a multi-section collage.

The installed Adapt/Render packages must be loaded from the exact pinned registry commit in `skill-sources.json`, including required references/assets. Do not reproduce the skills from memory or rewrite them into simplified prompts. The human does not manually supply style references.

Generated visuals are explanatory artifacts derived from approved evidence, not evidence sources.

Decision-application mode belongs to this role for V3. Apply only exact current VIS/GEN KEEP/EXCLUDE decisions to the current Unified Visual Review; never rerun extraction or generation just to apply decisions.

Return metadata only. Controller owns Sheets/checkpoints/main approvals.
