---
name: book-orchestrator-agent
description: Start, continue, resume, or approve the Products of Tomorrow six-stage writing-agent workflow in Codex with isolated workers, native Google Docs review and durable checkpoints.
---

# Book Orchestrator Agent

Read `references/codex-runtime.md` completely, then the source `instruction.md` completely. The runtime reference explicitly overrides legacy account IDs, Slack delivery and host-specific tool spellings; preserve every substantive artifact instruction, reference and rubric. Resolve source paths below against the pinned `workflow_source_root` recorded during WORK_START setup.

## Exact packages

| Node | Source path under Book Orchestrator Agent | Frontmatter skill name |
|---|---|---|
| broad_research | Broad-research-node/broad-research-agent | broad-research-skill-v2 |
| research_analysis | research-analysis-node/Research Analysis Agent | research-analysis-skill-v2 |
| chapter_blueprint | Chapter-blueprint-node/Chapter Blueprint Agent | chapter-blueprint-5 |
| research_mapping | Research-mapping-node/mapping-research-to-chapter-3-3 | mapping-research-to-chapter-3-3 |
| deep_research | Deep-research-node/deep-research-skill-3 | deep-research-skill-3 |
| chapter_writing | Chapter-writing-node/Chapter Writing Agent | anshul-chapter-writing-4 |
| Evaluate | Broad-research-node/Evaluate | evaluate-skill-v2 |
| Diagnose | Broad-research-node/Diagnose | diagnose-skill-v2 |

Before a node, read its parent's `instruction.md` as the controller contract. Each worker loads its complete SKILL.md and adjacent instruction.md, plus every required reference. Give each worker, evaluator and diagnoser a new context using `fork_turns="none"`; attach its instruction sources explicitly through the host's supported mechanism. If attachment is unavailable, supply only labelled instruction paths and runtime values and a closing instruction to load and follow those files. Do not relay chapter summaries, generated content or conversation history. Record the actual task ID/model/reasoning, not the intended ones.

## Required artifact references

| Stage | Bundled references |
|---|---|
| Broad Research | book-profile.md, output-formatting.md, writing-style.md |
| Research Analysis | output-formatting.md |
| Chapter Blueprint | output-formatting.md, section-design-guide.md, structural-patterns.md |
| Research Mapping | output-formatting.md |
| Deep Research | output-formatting.md |
| Chapter Writing | anshul-voice.md, output-formatting.md, writing-style.md |

Use the Broad Research book profile as the shared book-profile source where blueprint input requires it. Do not replace Anshul's bundled voice guidance with a generic style.

Evaluate in a separate context after every artifact or Diagnose version. Load its SKILL.md, instruction.md, rubric README and exactly the matching `<node>.yaml` rubric. Score section by section, insert findings into the reviewed Doc, create the report in that node's folder, and attach native comments last. Evaluation is not read-only. Log the report Doc ID separately from the artifact Doc ID.

Diagnose in a separate context on evaluation failure or human comments. Load its SKILL.md, instruction.md, rubric README and matching node rubric. Read comments directly, preserve untouched content and create the next version; never overwrite the reviewed version. Re-evaluate every revision. Do not modify approved upstream artifacts.

## Structure and approval

Run only broad_research → research_analysis → chapter_blueprint → research_mapping → deep_research → chapter_writing, sequentially, with explicit approval after each node. Preserve all upstream node/Doc ID mappings from instruction.md.

Blueprint requires an intermediate Block 1 choice: publish the foundation and three skeleton options in the Chapter Blueprint folder, checkpoint AWAITING_BLUEPRINT_CHOICE, show the choices in chat, and wait. Accept a named option or mixture. Record the decision; continue Block 2 in a fresh worker context using the saved options ID and choice. Preserve all three options in the completed evaluation artifact and clearly mark the chosen/mixed structure. This is a planned continuation, not a Diagnose revision. Evaluate the completed blueprint before final node approval.

Follow SKILL.md plus output-formatting.md when a blueprint instruction conflicts about Markdown/HTML. Use HTML for Google Docs. Blueprint permits 5–8 sections and at least two subsections each; do not impose a prior chapter's fixed counts. Chapter Writing executes the latest approved mapping structure without redesign and retains unresolved-gap caveats.

Use node controller final JSON exactly: {"node":"<expected node>","doc_id":"<actual artifact ID>"}. A malformed return is not success. Show artifact and evaluation links at the review gate. Do not approve on the user's behalf. Explicit exception approval is recorded with the failed verdict and caveats intact; it does not turn a failed score into a pass.

Upon final approval, reconcile all sheets, record WORKFLOW_COMPLETE, disable this run's recovery automation, and report topic, folder/Logs/control links and the six approved artifact IDs in order.
