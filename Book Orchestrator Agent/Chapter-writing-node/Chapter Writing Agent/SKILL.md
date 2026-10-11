---
name: anshul-chapter-writing-4
description: Execute an approved research-backed chapter using storytelling-article for argument and story development, then anshul-writing-style for one integrated writing, formatting and internal ai-humanizer-core pass. Preserve approved evidence and structure, verify the fully formatted Google Doc, and hand the passing chapter to Visual Placement without a second voice rewrite.
---

# Chapter Writing — integrated story, writing, formatting and humanisation

Use the existing Chapter Writing role. Do not register an additional skill or add a main-stage approval gate. This contract replaces the former untouched-canonical-worker / later LinkedIn-rewrite split for newly generated chapters. Historical artifacts remain immutable.

## Required inputs

- `chapter_blueprint_doc_id`: exact approved Research Mapping, the structural authority.
- `deep_research_doc_id`: exact approved Deep Research, the evidence authority.
- `chapter_writing_folder_id`: authorised destination.
- Supplied topic, version and chapter details. Resolve audience from details, then blueprint/topic, then a sharp nontechnical professional reader. Do not ask in an unattended node.

The controller separately verifies approved Deep Research and resolved current Visual Review. Any PENDING visual blocks this stage.

## Read every dependency before writing

Read these complete files, not only their names, summaries or metadata:

1. `references/storytelling-article.md` — the exact bundled production registry skill; owns argument/story architecture and story-integrity review.
2. `references/anshul-writing-style.md` — the exact bundled production registry skill; owns writing, voice, paragraph construction, visible formatting and humanisation.
3. `references/ai-humanizer-core.md` — its internal final-pass dependency, inside the same writing pass.
4. `references/anshul-voice.md` — thought movement, first-person policy, honest uncertainty and voice QA.
5. `references/writing-style.md` — simple language, explained jargon, paragraph rhythm and book craft.
6. `references/output-formatting.md` — typography, heading levels, spacing, emphasis, lists, tables and native-document verification.
7. `references/presentation-contract.md` and `references/presentation-profile.json` — mandatory approved presentation, native verification and baseline provenance.
8. `references/skill-sources.json` — pinned registry sources, blob SHAs and local SHA-256 values. Verify bundled dependencies before dispatch with the plugin contract validator.

All are mandatory on start, resume, diagnose or human-comment revision. If a dependency is missing or integrity validation fails, block. Do not substitute personal formatting logic.

## Precedence

1. Explicit author instruction and supplied author samples.
2. Factual accuracy, approved structure/order, evidence assignments, citations, numbers, caveats, fixed punchlines and designated reader transformation.
3. `storytelling-article` for developing the story within those fixed commitments.
4. `anshul-writing-style` for writing, voice and visible presentation; `ai-humanizer-core` is subordinate and runs internally.
5. Bundled book craft, voice and output references within their territories.

This author-approved integration supersedes former per-paragraph bold quotas, minimum section bold counts, italic quotas, a mandatory later LinkedIn voice rewrite and a blanket emoji prohibition. Do not improvise a compromise between obsolete rules. Use functional heading icons sparingly when consistent with the supplied author reference; never invent a recurring icon template. Preserve approved heading words/order and internal commitment mapping; render heading levels, numbering, icons and citation presentation exactly under `presentation-contract.md`. That contract overrides conflicting legacy templates. Main headings use 1., 2., etc.; subsection numbers and internal markers stay in Notes, not reader headings. Use native bold, not Unicode bold in Google Docs.

Typical full-chapter length is 4,000–7,000 words unless the approved brief specifies otherwise. Use assigned evidence selectively rather than forcing every available source.

## Execution inside this worker

### 1. Ground the chapter

Read the approved Mapping and Deep Research directly. Extract ordered sections/subsections, opening commitments, central tension, fixed punchlines, counterargument, transformation point, assigned evidence, citation locators and unresolved GAPs. Read supplied durable book baseline/context references when present. Do not rely on chat memory.

Preserve source meaning. Do not add research, sources, statistics, personal experiences or stronger claims. Use honest conditional wording for unresolved gaps. Respect EVIDENCE: NONE beats. Preserve the Tech/PM lens and its purpose.

### 2. Develop the argument with storytelling-article

Use the skill's adaptive route: upstream research, analysis and blueprint already exist. Do not restart THINK/RESEARCH/ARTICULATE as separate mandatory agents or call new research tools. Recover the existing argument spine and plan the reader journey within the approved sections.

Develop the central tension, causal connections, progression, necessary internal L1/L2 beats, opening and honest ending. L1/L2 planning does not add visible headings or redesign approved structure. A missing evidence item stays a gap. An argument improvement means better development of supported ideas, not a new claim.

Keep the compact story plan inside this worker and later its Notes, not the controller conversation. If the approved structure cannot support a necessary substantive change, return a blocking reason rather than silently rewriting commitments.

### 3. Write + format + humanise with anshul-writing-style

Pass original material, argument spine, story beats, tension, assigned evidence, audience and protected phrases into the writing skill. Execute its complete procedure in the same worker context. Do not add separate formatting or humanizer nodes.

Explain to a sharp reader without technical training. Use familiar words; introduce unavoidable jargon with an immediate explanation. Preserve factual precision and qualification. Keep one developing idea per paragraph, normally 3–7 sentences, with deliberate shorter bridges or fixed punchlines; never stack one-liners to imitate a social post.

Format as part of writing. Selectively bold existing important opening claims or comparison phrases so the following explanation is legible on a skim. Do not invent summary-label sentences or repeat the next sentence. Do not preview every paragraph. Leave ordinary setup, evidence narration and bridges plain. Useful emphasis may occur in the middle or end. A complete existing claim may be bold when the author sample and its argumentative importance warrant it; ordinary sentences are not automatically bold. No numerical preview or bold-density quota.

Use explanatory bullets only for genuinely parallel items. Give each important item a meaningful bold lead-in followed by a complete explanation or question. Do not turn the chapter into short fragment lists. Maximum two lists per section unless explicitly instructed otherwise.

Integrate evidence into reasoning. Italicise a concise source/study attribution where useful to distinguish evidence; preserve its citation, finding, scope and caveat. Never colour evidence text or add a background highlight. Avoid whole paragraphs in italics and overlapping bold/italic runs. Preserve useful inline emphasis and fixed punchlines.

Run `ai-humanizer-core` internally: inspect structural clusters and language clusters; patch minimally; never invent detail or remove intentional author choices. Exempt fixed punchlines and source quotations from rewriting.

### 4. Verify story integrity

Run storytelling-article's story-integrity review against the written and formatted chapter: progression, causal bridges, central tension, visible structure and honest ending. Correct only affected spans through the writing skill and recheck once. Do not regenerate passing work merely to produce another version.

The storytelling skill's visualization stage is fulfilled by this pipeline's Visual Research, human KEEP/EXCLUDE gate and downstream Visual Placement. Do not invoke another visual skill, image search or image generation here.

### 5. Deliver a fully formatted Artifact A

Execute `references/presentation-contract.md`: plan the chosen presentation opportunities, apply them, then run `validate_chapter_presentation.py` on actual native Doc readback and the revision-bound plan. Missing icons, zero selected opening emphasis, unimplemented explanatory lists or heading/citation profile drift block worker success, including worker-only tests. Generic feature counts are insufficient.

Produce the complete chapter once, Chapter Writing Notes, Manuscript Handoff Package and Completeness Summary in one native Google Doc. Notes contain the story spine/transition decisions, evidence/gap decisions, voice/humanizer changes and execution audit. Handoff includes verified word counts, citation list, evidence coverage and unresolved decisions. Summary covers protected structure, punchlines, transformation, tension, sources, language, story integrity and formatting.

In Notes record `chapter_writing_contract_version: 1`, exact dependency paths/source SHAs, and evidence for these completed checks: `references_verified`, `story_architecture`, `write_format_humanize`, `story_integrity`, `formatted_document_verified`. Record what changed or why no change was needed. A declaration is not proof: the evaluator must inspect actual prose and rendered presentation.

Use output-formatting typography and spacing templates. Render/verify with available native Google Docs tools; the subscription adapter replaces Gumloop and Slack. Do not require obsolete converters or an API key. Inspect native headings, fonts, bold/italic runs, lists, captions, links and spacing after creation. Inspect exported PDF pages when layout/page fit is material. Fix the same unpublished Doc for conversion errors; do not create a new version solely for rendering repair. Evaluation starts only after this full formatting check.

Never modify upstream Docs or overwrite earlier published versions. Return metadata only using the instruction envelope. The controller logs and checkpoints; the separate clean evaluator scores; Diagnose revises only after failed evaluation or explicit human feedback.

## Visual Placement handoff

Artifact A is already the completed story, voice, formatting and humanisation result. After its clean evaluation and execution audit pass, Visual Placement creates separate Artifact B by preserving reader prose and native emphasis, stripping Notes/Handoff/Summary, and inserting only human-KEEP source visuals with captions and accessibility text. Visual Placement does not rerun storytelling, rewrite the voice or replace these formatting decisions.

## Final quality gate

- Every section earns the next within the approved order.
- Language works for a nontechnical reader and jargon is explained.
- Evidence, citations, figures, caveats and fixed phrases are faithful.
- Emphasis identifies meaningful claims instead of repeating a preview template.
- Bullets explain actual parallel points; headings/icons do not fragment the story.
- Humanisation preserves Anshul's thought development and uncertainty.
- All mandatory reference and execution checks are complete and verified.
- Fully formatted Artifact A exists before evaluation.
