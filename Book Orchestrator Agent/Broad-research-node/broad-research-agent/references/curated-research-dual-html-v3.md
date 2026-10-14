# Curated Research & Dual-HTML Delivery — v3

This reference ADDS to the existing Broad Research skill. It changes the **selection, reading, synthesis, visual, and delivery behavior** only. All ten original Source Ladder definitions, platform checklists, primary-source preferences, source-quality fields, book profile, and blind-spot checks remain in force.

## Non-negotiable outputs

Every full research run yields **two separate, finished HTML files built from the SAME source-reading dataset**. Do not substitute a Google Doc, Markdown note, short text answer, or one combined file unless explicitly requested.

1. **Source-first:** ordered Rung 1 through Rung 10, then one article (R1.1, R1.2, …) at a time. A reader should learn what each selected article actually teaches. The primary reading organization is NEVER by research questions.
2. **Question-first:** ordered question map grouped by fundamentals and professional roles, then a genuine synthesized answer to each research question using the depth, frameworks, data, caveats, and figures captured in the source-first analysis. It must NOT merely shuffle article abstracts or attach a list of links.

Produce source-first first, question-first second. Deliver both downloadable HTML file paths/links; if a Drive folder was supplied, save each as a separate HTML file in THAT folder only. A Google Doc export is optional and is NOT a substitute for the two HTML originals.

## Research question map (replaces user-visible query/term map)

After a short ground-floor research scan, compose a future-first **question map**. Keep synonyms and search vocabulary as PRIVATE search scaffolding, never the primary output. The question map has two levels:

- **Level 1 — Foundational:** what exists today and is used by real people, current pain points, why the present pattern fails, definitions and boundaries, plausible evolution, differentiating examples, adoption evidence and counterexamples.
- **Level 2 — Professional roles:** Product Management, User Research, UX/UI Design, Engineering/Architecture, Finance/Pricing, Economics/Industry Structure, Marketing/Distribution/Sales, Risk/Security/Privacy/Legal/Governance, and Business/Organizational Leadership. Tailor roles when pertinent; do NOT leave out relevant major roles merely to shorten the map.

For EVERY role ask about the future, not only present practice: What changes? Which trade-offs, interfaces, user needs, operating models, incentives, capabilities, or safeguards emerge? What evidence would prove/disprove the anticipated future? Ground the questions in basic research, real named products, and concrete conflicts. Include competing possibilities; do not silently assume the chapter's thesis is true. Store stable question IDs (e.g., Q01–Q26) and use them for cross-references.

## Source selection: judgment before quotas

Search all ten rungs of the original Source Ladder for full chapter research (even if some yield no high-quality sources). The existing five-findings-per-rung threshold is a **discovery target, NOT a license to pad**: attempt five genuinely different strong sources; when fewer qualify, report the real count and explain why. Do not skip entire rungs or collapse rung identities. Include weak evidence only when it is itself analytically important, labeled clearly.

A source earns a place if it teaches at least one distinctive, useful thing: an original framework, causal mechanism, substantive case study, high-quality data, unexpected implication, or serious challenge to the thesis. Reject sources consisting mostly of generic agentic-AI hype, headline forecasts without mechanism, press-release repetition, or near-duplicates of stronger sources. A famous analyst brand is not enough. The previously rejected Gartner project-cancellation entry is an example of a source that should NOT be retained just to hit a rung count. Replace weak sources rather than summarizing them with more words.

Assess before selection:
- **Relevance & novelty:** Is the finding directly germane and non-redundant?
- **Depth:** Does the article explain a mechanism, a structured model, data, or an illuminating real case?
- **Evidence & authority:** Firsthand reporting, original methodology, named observations, well-scoped forecasts, or primarily opinion/marketing?
- **Future usefulness:** Can it help explain a future product, user experience, business, or systemic shift and its constraints?
- **Visual value:** Are original figures or tables relevant to its shortlisted key insights?

Choose sources after this evaluation, not based on alphabetical results or publisher prestige alone. Retain source-quality labels SOURCE TYPE, AUTHORITY, FRESHNESS, USE and explicit CONFIDENCE/claims in your internal evidence record. Link to exact verified source URLs and publication dates; do not invent citations.

**Exa** is an optional discovery/fetch engine. Use Exa ONLY when the user explicitly requests it for that run. Otherwise use available normal search/read tools. No firecrawl/tavily/external paid vendor assumed or used without authorization.

## Per-article deep-reading and curation

READ the available full article or source, including meaningful figures, not solely search snippets. First privately extract its full arguments, statistics, mechanisms, named examples, models, caveats, and competing implications. Then SELECT the genuinely useful parts.

For each accepted article, normally show **3–4 distinct high-value insights and 200–260 words of main explanatory copy in total**. This is a CALIBRATION from the approved Rung 1 curated-essentials example, not a rigid word quota: use 2 insights for a narrow article; up to 5 for a truly substantive one; let graphics/tables carry appropriate detail without piling on prose. Never copy most of the article or merely restate its abstract. Avoid repeated general observations across sources. Write in accessible, concrete language.

Use this order WITHIN EACH SOURCE:
1. Stable source ID, publisher, full article title, date, exact clickable original link; short source-quality metadata.
2. One-line **core idea**: the article's actual argument (not just its relevance to the chapter).
3. **3–4 numbered key insights** with 2–5 explanatory sentences apiece where needed. Capture the causal WHY, surprising or useful mechanisms, concrete examples, properly bounded numbers, and conditions, not only a one-line conclusion.
4. **Relevant source figure(s)/framework/table(s)** inline at the point of explanation; preserve stages/axes/comparison alternatives instead of flattening into generic prose. Add a clean HTML comparison table when that improves comprehension.
5. One concise **future/book implication**, visually distinguished as interpretation, never disguised as something the article proved.
6. Optional concise **limitation/disagreement** and/or expandable evidence audit (specific claim, confidence, source type). Do not present long metadata blocks as visible essay copy.

When an original figure carries most of the point, shorten surrounding text. If material is interesting but redundant or weak, exclude it.

## Mandatory original-image audit for each chosen article

For EACH selected insight, inspect whether the source article has a relevant original chart, diagram, figure, table, or timeline. If so, **retrieve/download and embed the source figure** wherever technically and legally possible. This is required source investigation, not an instruction to add decorative imagery.

- Prefer the publisher's original figure or an official PDF image. Confirm the figure really belongs to that URL and illustrates the exact selected idea.
- Embed actual image bytes as data URI in the standalone HTML when available and suitable; optimize resolution/size and preserve readable text. Provide a click-to-zoom view; make mobile figures readable and accessible.
- Include caption, publisher/source citation, link to article, and useful alt text. Attribute adaptations honestly (e.g., "Adapted from McKinsey" rather than claiming original).
- If an image is inaccessible, paywalled, disallowed for reuse, too blurry, or impossible to obtain, do NOT fake an original or silently substitute a stock/AI picture. Recreate only a clearly labeled explanatory diagram from verified facts, or use a legible HTML table and record the limitation.
- When a source has no relevant figure, omit imagery; no decoration requirement.
- Images must work in the delivered offline HTML wherever possible. Check that every embedded image decodes and is rendered, not just that the <img> tag exists.
- Keep figures and their prose within that article or question section; never dump unrelated pictures into a gallery.

## Source-first HTML — editorial specification

Make one beautiful HTML document, not a Google Docs converter fragment. It should match the approved curated Rung 1 visual character: restrained warm off-white canvas, elegant editorial headings, deep navy type, teal and selective warm accent color, generous whitespace, large readable body text and figure captions.

Reading hierarchy: Topic overview → 10-rung index → **one source at a time** within its rung → previous/next source. Each source page contains only that source's insights, useful tables, figures, and a concise implication. Show rung headings and missing/weak-rung notes without inventing five sources. Use good mobile responsive layouts, contrast, semantic headings, keyboard-friendly navigation, image zoom, clickable original links, and print styles. Embed local CSS and JS, no external assets critical to functioning; if JS is disabled, keep content recoverable. Search/filter is nice when useful but must not replace clear source navigation.

**Never organize Output 1 by research questions.**

## Question-first HTML — answer depth is mandatory

Use the SAME curated full-source insights (not just the source one-liners) to answer each original question. A question is included because it matters, so actually answer it.

Structure: Question map overview → role category → Question ID/title → **direct evidence-backed answer** → 2–5 deeper supporting insights/causal mechanisms/trade-offs where supported → relevant original figures or legible tables → "What this suggests for the future" → uncertainty/gaps → inline linked article IDs and publisher/source URLs.

The length is calibrated to COMPLETENESS OF DISTINCTIVE LEARNING, not a fixed 200-word limit per question. Some questions need 120 words; cross-disciplinary questions merit more. Prefer several succinct but substantive paragraphs over long essays. The second output should communicate the SAME intellectual depth as the first across relevant sources, while avoiding duplication and repetition. It is synthesis, NOT a thin Q&A index and NOT an article-by-article restatement. Where sources disagree or discuss different contexts, explain that clearly, with citations and confidence. Reuse a relevant figure if and only if it advances that particular answer, retaining attribution.

Cross-reference each key claim back to source IDs/links. Expose missing evidence rather than inventing a confident answer. Distinguish observed adoption, scenario forecast, company intention, expert opinion, and the book author's own extrapolation.

Use the same editorial design language as source-first, optimized for navigable questions/roles; offer a question index and accessible responsive figures.

## Integrity and quality assurance — both outputs

1. Confirm all 10 rungs were searched and source-first displays them, including honest shortfall notes.
2. Every included source has an actual exact URL, checked title/date/publisher, 3–4 curated insights unless justified otherwise, and explicit source/interpretation separation.
3. Compare each key point with the full original source. Numbers retain population, period, units, methodology and "forecast vs observed" labels.
4. For each selected insight, audit its available source imagery; if relevant figures exist, embed them and validate rendering, or record exact reason unavailable.
5. The original diagram/table's meaningful structure remains readable; captions clearly attribute ownership.
6. All foundational and applicable professional-role questions are answered directly, with full evidence depth and source links; do not simply rearrange article cards.
7. Check both HTML files on desktop AND mobile: no overflow, clipped charts, unreachable navigation, unreadable image text, broken links or blank source panels.
8. Verify HTML is standalone, includes all assets it promises, and delivers TWO distinct filenames.
9. Re-read as an editor: "Did this source teach a distinct, valuable idea in two minutes?" and "Could the reader meaningfully answer this question without opening every source?"
10. Do not claim a file was uploaded, installed, or committed unless that action actually succeeded.

## Original Google Docs fallback (legacy only)

The original `references/output-formatting.md` is retained as a LEGACY Google Docs-compatible converter template, for use ONLY when the user explicitly requests an additional Google Doc. It does **not** govern either required standalone HTML output: they use CSS, JS, responsive typography and images by design. If an explicit Drive folder is supplied, save two separate HTML artifacts there and do not choose another destination. If a Google Doc conversion is additionally requested and image/style fidelity cannot be preserved, describe the tradeoff; never reduce the HTML design to the legacy CSS-free layout.

## Handoff to next agent

The source-first and question-first HTMLs are two views of one internally structured research dataset: question IDs, role, source IDs, title, publisher, URL, date, metadata, raw deep-reading notes, curated insights, claims, statistics/caveats, visual image records, and source-to-question links. Preserve this map as an internal machine-readable working artifact when possible so the later research-analysis agent does not have to rediscover or reinterpret sources. The user-facing outputs remain exactly the two mandatory HTML files unless more were requested.
