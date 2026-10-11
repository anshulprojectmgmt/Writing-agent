# Canonical Research Contracts

## Contents

1. Shared mission and editorial standard
2. Question Map acceptance and evolution
3. Run configuration and search providers
4. Source discovery, screening and traceability
5. Stage outputs and worker handoffs
6. Native Google Docs and portable delivery
7. Original-skill provenance and deliberate adaptations

## 1. Shared mission and editorial standard

**Define plausible futures through diverse professional perspectives.** Present signals and evidence support reasoning about driving forces, future products/behaviors, competing outcomes, second-order consequences and constraints. These are thinking dimensions, not compulsory headings.

Write for the supplied audience and book scope. Keep verified facts, emerging signals, source interpretations, researcher inference and speculation distinguishable through natural wording and a compact evidence record. Do not equate a prediction with a fact, or a simulated professional lens with a real interview.

**Substance without bloat:** give consequential insights, mechanisms, examples and disagreements the space they merit. Keep routine context brief. Each paragraph must add understanding, evidence or reasoning. Bold meaningful takeaways selectively. Remove repeated ideas, ceremonial introductions, generic transitions, obvious observations and repeated caveats. Combine headings/fields when useful; never fill them with invented material. Word counts guide effort, not padding. Preserve reasoning, uncertainty and counterarguments while compressing.

Before accepting or saving each stage, ask: What matters most? What repeats? What adds no understanding? What deserves more explanation, and what deserves less? Edit accordingly. Apply this standard to skill instructions too.

**Completeness outranks brevity.** Remove filler and redundant wording, never a requirement, useful causal explanation, source channel, example, counterargument or output contract merely to make the skill/report shorter. Before changing a skill, check the full user brief and the provenance/adaptation table; record intentional departures instead of silently deleting capabilities.

### Future-first reasoning guide — background, experts and synthesis

Every expert explores the future through its professional lens. Use the following reasoning moves in proportion to importance; they are not compulsory report headings.

1. **Establish starting conditions.** What actually happens today? Identify observed pain points/behavior, current products/interaction forms, technical capabilities, business incentives and institutional constraints. Distinguish evidence from product positioning and untested user scenarios.
2. **Find the force or constraint that is changing.** Why might tomorrow differ? Examine capabilities/costs, context and memory, interoperability, user expectations, distribution, competitive incentives, organizational practices and regulation where relevant. A new product announcement is a signal to investigate, not a causal explanation by itself.
3. **Develop plausible future states.** What products, experiences, behaviors, architectures or market structures could result? Describe shape/form and mechanisms, not just a trend label. Explore alternatives: convergence versus specialization, complementary versus substitutive use, centralized versus distributed control, or another topic-specific distinction supported by inquiry.
4. **Trace consequences.** What changes next for users, teams, firms, markets or society? Who gains/loses value or authority? What new dependencies, bottlenecks, markets and business models follow? Separate first-order benefits from second-order effects.
5. **Challenge and qualify.** What must hold, what could prevent the outcome and what evidence would favor another path? Consider disagreement and counterevidence without letting present constraints consume the whole future exploration. Use the supplied horizon; distinguish nearer-term signals from more distant speculative possibilities when useful, without inventing dates/probabilities.

For an important future argument, the reader should understand **evidence/signal → changing force or mechanism → future possibility → consequence → conditions/alternative**. Do not force this chain onto minor supporting facts. State where the chain rests on researcher reasoning or speculation.

Example: a documented approval checkpoint is a current design fact. Changing verification capability could motivate an inference about task-dependent autonomy. A future control interface is a design possibility, and changed household responsibility a second-order hypothesis. Neither is a measured outcome merely because the starting fact is verified.

### Two-level roles and grounded expert questions

**Level 1 — Generic professional role:** Product Manager, UX Researcher, Product/Interaction Designer, Software/AI Engineer, Economist, Business Leader, Marketing Leader, Sales Leader, Risk & Governance Specialist or Domain Specialist.

**Level 2 — Domain-specific professional role:** use only when the background/topic justifies it. Examples: Economist → Labor Economist for employment; Macroeconomist for economy-wide effects; BFSI Economist for financial-services economics. Preserve the generic parent and explain what the specialization adds. Never use company names in identities or specialize merely for realism.

Question-generating experts must read the frame, accepted background, concrete examples and relevant substantive source notes. Each proposed umbrella question needs its role, background anchors or explicitly uncovered dimension, significance and future change to explore. Examples can ground a question without becoming its whole scope. An uncovered dimension must be marked as such; do not invent background support. The planner's role-specific question examples guide breadth without predetermining the answers.

## 2. Question Map acceptance and evolution

Background starts with flexible guiding questions about meaning/significance, developments, changing forces, uncertainty and deeper inquiry. No fixed initial question count or detailed map is required. Give these prompts provisional BQ IDs for source associations; carry their links into the expert map.

Before expert research, inspect every top-level entry. Accept it only if it:
- Is an open-ended question, not a topic label, keyword cluster or search string.
- Explores consequential future change through its professional perspective.
- Is broad enough to support discovery rather than merely retrieve a named fact or test one use case.
- Has a clear reason its answer could alter understanding of the topic.

A question mark alone does not establish validity. Reject "Memory", "personal agent memory pricing" and "Find three agent products". A current-state question or holiday-booking check can be a supporting investigation beneath "How will personal agents evolve as products and change value, differentiation, distribution and competition?" Rewrite rejected top-level entries before launching expert research.

Use stable Q001-style IDs. A compact map needs:

| Q ID | Broad research question | Role/parent | Background anchors or uncovered dimension | Why consequential / future change | Source/insight links | Status |
|---|---|---|---|---|---|---|
| Q001 | Future-oriented open question | P01 or parent Q | BQ/E/source/example, or marked new dimension | Implication and change to explore | S/E IDs | open / partial / informed |

Future questions may remain uncertain even when well investigated; "informed" does not mean the future is settled. Supporting questions may be narrower. Search strings belong only in temporary retrieval logs beneath a question, never in a Term Map or Query Map.

At each pass, review additions, changed assumptions, merges and questions that lost relevance. Record only material revisions with their reason and prior ID/alias. Do not reuse a retired ID or discard its source associations. New insights may create new questions; retain the insight and link it before handoff. Every retained source connects to at least one BQ/Q, including counterarguments.

## 3. Run configuration and search providers

Record this portable configuration in the frame and each worker brief:

```yaml
run_id: topic-date
search_provider: native       # native | exa | compare
exa_authorization:
  authorized: false
  run_id: null
  user_instruction: null      # exact instruction naming Exa for this run
effective_search_provider: native
```

| Requested mode | Required decision before retrieval |
|---|---|
| native or omitted | Use native ChatGPT web search; do not call Exa |
| exa | Verify explicit user authorization naming Exa for this run and available connected tools |
| compare | Verify the same authorization; use equivalent question-led searches through native and Exa, deduplicate, compare usefulness |
| exa/compare without authorization | Leave Exa disabled; use native and disclose invalid configuration; if the user made non-native execution indispensable, return a blocker |
| Authorized Exa unavailable | Disclose unavailable tools; use native only if compatible with the user's fallback instructions, otherwise return a blocker |
| Unknown mode | Correct configuration before retrieval; never silently enable another provider |

"Use Exa for this research" or "Compare Exa with ChatGPT Search" qualifies. "Research deeply", "best sources" and "all available tools" do not. Authorization is run-specific and never carries forward. A configuration flag alone is not user authorization; confirm the recorded instruction applies to the current task/run.

Do not automatically call Exa during any stage, silently activate it after weak native results, invent credentials or assume connection. Discover available tools before use. Prefer a suitable connected plugin; do not separately use the Exa API without explicit authorization. Add no mandatory Exa dependency and no Tavily/Firecrawl integration. Provider ranking supports discovery, not article-quality judgment. Record requested/effective modes and any disclosed fallback.

## 4. Source discovery, screening and traceability

### Preserve the ten-category Source Ladder

| Rung | Category | Discovery emphasis |
|---|---|---|
| 1 | Consulting & Analyst | Market arguments, surveys, assumptions and methods |
| 2 | VC / Investor Research | Emerging models and ecosystems; investment incentives |
| 3 | Academic / Research | Original measured findings and mechanisms; relevant research pages/papers |
| 4 | Practitioner & Product | Firsthand PM, UX, engineering and deployment accounts |
| 5 | Big Platforms & Major Products | Official blogs/docs, founder/leader writing, keynotes and strategic signals |
| 6 | Case Studies | Named products/deployments; distinguish pilot, scale and measured outcomes |
| 7 | Ethics / Regulatory | Primary policy, jurisdiction-specific regulation, safety and governance |
| 8 | Trend & Futures | Dated forecasts, roadmaps and alternative futures |
| 9 | Newsletters & Long-form | Thoughtful essays, interviews/podcasts, critique and original arguments |
| 10 | General / Recent News | Developments, failures, criticism and original reporting; follow primary evidence |

**Do not skip any rung.** On every background, expert and targeted research pass, perform an actual question-led search or inspection of a potentially relevant source/channel for each of the ten categories. Preserve all ten rows in the coverage record. A relevance judgment alone does not count as an attempt. Record operation/date and finding, no useful result, blocked access or tool limitation. Try a reasonable accessible alternative for blocked channels within the authorized provider. If still blocked, preserve the limitation; never mark an unattempted rung complete.

Depth varies with relevance and intellectual value; mandatory coverage does not impose equal effort or source quotas. A reasonable attempt yielding no useful evidence is an honest result. Do not pad the reading layer, fabricate findings or duplicate claims. There is no five-per-rung, five-platform or fifty-finding quota. The ladder's order is a discovery framework, not an authority ranking.

Prioritize primary company/product evidence from relevant firms such as OpenAI, Anthropic, Google/DeepMind, Meta, Microsoft, Amazon, Apple and others warranted by the questions. Use blogs, documentation, technical reports, public keynotes, founder essays and IR transcripts. Company forecasts are strategy signals, not established future outcomes. Academic work remains valuable for original measured findings, without becoming the default source for current shipping behavior. Source lists are suggestions, not compulsory provider checklists.

### Concrete source channels inherited from Broad Research

Use the following examples to make rung attempts substantive. Verify current pages, relevance, dates and availability when researching; these are discovery anchors, not claims that a person still holds a particular job or that a URL is unchanged.

| Rung | Example sources/channels | Investigation emphasis |
|---|---|---|
| 1 | McKinsey, BCG, Gartner, Forrester, Deloitte, IDC, 451 Research, Omdia, CB Insights | Read survey methods, market-estimate assumptions and adoption denominators |
| 2 | a16z, NFX, Sequoia, Radical Ventures, Conviction | Original market arguments, new models and investor incentives |
| 3 | Original research pages, arXiv/ACM and named venues: NeurIPS, ICML, ICLR, AAAI/IJCAI; ACL/EMNLP/NAACL; CVPR/ICCV/ECCV; CHI/CSCW; FAccT/AIES | Select relevant disciplines: technical capability, user behavior, economics and governance; papers are not automatically superior evidence for shipping products |
| 4 | Named PM/UX/engineering accounts, official docs, design research, technical blogs, how-we-built posts and firsthand deployment failures | Separate what someone observed from their broader interpretation |
| 5 | Official blogs/product docs; founder/leader essays and interviews; vision/roadmap signals; keynotes; IR/shareholder material | Attempt official-product, leader-reasoning and future-direction channels; avoid one generic platform search standing for all three |
| 6 | Named shipped products, customer deployments, case studies, lessons learned and independently reported outcomes | Distinguish pilots, vendor-hosted outcomes, real scale and measured behavior |
| 7 | Primary regulator/legal texts and guidance, company safety/policy, public testimony, OECD, FAccT/AIES | Record jurisdiction/version; connect constraints to future product/market possibilities |
| 8 | Dated roadmap/strategy documents, futures essays, scenario work and forecasts | Identify mechanism, assumptions, alternative outcomes and what could break the forecast |
| 9 | Lenny's Newsletter, Ben's Bites, Latent Space, Import AI, Interconnects, Pragmatic Engineer; relevant long-form interviews/podcasts | Read distinctive arguments and conceptual models rather than collecting takeaways |
| 10 | Reuters, Bloomberg, FT, The Information, Wired, MIT Technology Review, The Verge and relevant general reporting | Original reporting on launches, adoption, failures/reversals and critique; follow repeated company claims back to the primary source |

For Rung 5, inspect relevant channels across **OpenAI, Anthropic, Google/DeepMind, Meta, Microsoft, Amazon/AWS, Apple, xAI, Mistral, NVIDIA, Salesforce, Databricks, Hugging Face, DeepSeek, Moonshot/Kimi, Zhipu and Qwen**. Choose relevant firms rather than inventing a fixed per-company quota. Do not omit a major relevant platform without a source-based reason.

Preserve the broad skill's diverse primary-voice channels:
- **Official blogs/docs and technical research:** news/engineering/research/product pages and company research publications.
- **Founder/leader writing:** essays such as those by Sam Altman and Dario Amodei, public company-leader posts and long-form strategic reasoning; verify attribution/current context.
- **Interviews/podcasts:** Lex Fridman, Dwarkesh Patel, No Priors, 20VC, Logan Bartlett Show, Hard Fork, Eye on AI, BG2, Acquired, All-In or a topic-relevant alternative. Prefer transcripts or verified passages over remembered quotes.
- **Keynotes/talks:** DevDay, Connect, I/O, Cloud Next, Build, re:Invent, GTC, TED/TED AI and WEF where relevant. Distinguish demonstration, announced intent and actual availability.
- **Earnings/shareholder material:** official company IR and shareholder letters first; transcript services/reporting for discovery and corroboration.
- **Social/real-time signals:** verified public posts, tied to an actual date/source; use as signals, not unsupported proof of scale.
- **Policy/testimony:** Congress, EU official materials, FTC, OECD, UK AISI, G7/OECD reporting and company safety/policy documents as relevant.
- **Independent reporting and unconventional essays:** useful counterarguments and firsthand observations deserve attention even when ranked low; do not confuse independence with automatic correctness.

Derive retrieval strings from the question and these channels. Adjacent vocabulary may help find material, but never create a separate keyword/synonym map or hardcode stale years into search templates.

### Three lightweight gates

1. **Relevance:** materially helps answer a guiding/research question.
2. **Intellectual value:** adds original reasoning, credible observations, mechanisms, concrete examples, useful future possibilities, distinctions or serious counterarguments.
3. **Evidence quality:** identify facts, firsthand observation, measured research, opinion or speculation; assess scope, methods, incentives and provenance.

Internally classify sources considered for use as **Deep Read**, **Selective Read** or **Skip**. Record a short rationale for consequential selection/rejection decisions; no numerical rubric or mandatory card for every result. Retain strong primary evidence or serious counterarguments even when ranked low. Do not rely on snippets for material claims. Read important arguments deeply enough to preserve their reasoning.

### Two output layers

**Reading layer:** substantive notes grouped by ideas/themes, inline clickable source citations and selective bold takeaways. For a major insight cover central idea, motivation/reasoning, supporting evidence/examples, future implications, writer's value and limitations in coherent paragraphs. These dimensions are a quality check, not six repeated headings. Minor sources may support a short sentence.

**Traceability layer:** compact appendix or structured handoff embedded in the stage artifact. Use Q/BQ for questions, P for professional roles, S for sources, E for important observations/insights and G for gaps. Allocate exclusive namespaces to parallel workers; preserve existing IDs/aliases.

Keep these compact records where applicable:
- Source: S ID, canonical URL/title, author/organization, publication date (unknown if unavailable), access date, source category/type, authority/scope and confidence assessment, disposition/rationale, Q/BQ links and provenance limits.
- Insight: E ID, claim/idea, supporting S/Q links, evidence versus inference/speculation, material uncertainty and observation period where different from publication.
- Coverage: all ten categories, actual operation/date, useful finding / no useful result / blocked / tool limitation, with evidence pointers and limitation. Never use considered-not-pursued or skipped as completed coverage.
- Search log: Q/BQ, provider, date, actual retrieval operation, material result/null/blocked status. Keep bounded notes, not an exhaustive dump of search hits.

Canonicalize URLs and shared claims. Multiple outlets repeating one announcement are not independent corroboration. Keep original historic evidence IDs/labels when referencing prior artifacts; attach reassessments rather than rewriting history. New outputs use these lean records rather than the old mandatory evidence-card fields.

## 5. Stage outputs and worker handoffs

Each accepted stage needs a dedicated format below. Required information must be present. Background/expert headings may combine naturally; synthesis keeps its seven core headings, with an honest brief explanation when a core section has no justified material. Only optional sections are omitted. Store step, round, focus, status, next dependency and artifact links in the compact index/appendix rather than above every paragraph.

| Stage | Human-facing output | Compact handoff/appendix |
|---|---|---|
| 01 Frame | Topic, future objective, audience/scope, horizon and assumptions | Frozen decisions, mode, provider record, run folder and artifact index |
| 02 Background | Brief narrative: significance, developments/examples, forces, uncertainties and promising deeper dimensions; usually up to 1,000–1,500 words when warranted, no minimum | Provisional guiding-question/source links, ten-category relevance/coverage notes |
| 03 Expert panel | Roles and what each distinct lens can reveal | P ID, Level 1 generic role, Level 2 specialization or none, justification, background anchors, distinct contribution/blind spot |
| 04 Question Map | Broad future questions through each role | Stable Q IDs, rationale/parents, visible background/example anchors or uncovered dimensions, future change, validation/revision notes |
| 05 Expert research | Role-specific argument, thematic substantive notes, future possibilities, counterarguments and writing opportunities | Current question statuses/revisions, screened sources, coverage and concise search/provenance notes |
| 06 Synthesis 1 | Framing Check and Research Analysis-derived sections 1–7, optional 8 | Concept registry/relationships, question updates, Completeness Summary, significant gaps or no-targeted-work decision |
| 07 Gap decision | Only consequential gaps and why they matter; brief no-gap decision is valid | G/Q, prior evidence, priority, owner, evidence need and exit condition |
| 08 Targeted research (conditional) | New insight/evidence, changed answers and remaining uncertainty | G/Q outcomes, actual searches/nulls, exit-condition status |
| 09 Final synthesis | Fresh integrated picture using the same seven-section contract, whether or not targeted retrieval occurred | Strengthened/weakened/reversed/unchanged views, concept/question/gap outcomes and Completeness Summary |
| 10 Final package | Linked reading guide, strongest future insights, chapter connections and material uncertainty | Reconciled stage/source index, current map/history, save/check status and skipped-stage reasons |

### Synthesis contract — adapted from Research Analysis

Use these stable headings in initial and final synthesis: **Framing Check; 1. Central Concept; 2. Themes; 3. Mental Models; 4. Technical Concepts; 5. What to Retain, Downgrade, or Remove; 6. Chapter Synthesis Ideas; 7. Final Conclusion**. Add **8. Research Gaps & Opportunities** only when consequential gaps exist. Preserve the core headings; if a core section lacks justified material, say so briefly rather than inventing it. Counts and paragraph lengths are guidance, not quotas.

**Framing Check:** five short blocks—stated question, actual question, assumption underneath, constraint test, serious alternative—then HOLDS or REFRAME PROPOSED. Test what made today's practice rational and what changed. Respect frozen decisions. Surface proposed reframes visibly; in autonomous mode continue under the authorized frame, in requested stepwise mode follow the user's checkpoint. Do not silently change the chapter thesis.

**1. Central Concept:** explain the main shift and core tension, usually two or three coherent paragraphs. Make the topic intelligible if this is all the writer reads. Integrate evidence across perspectives and name the important source links. Distinguish the factual starting point from the inferred future.

**2. Themes:** recurring arguments, not mere topic labels. Use a short title, plain-language explanation, substantive reasoning, concrete example and sources. Develop emerging future forms/behaviors, competing possibilities, market changes or second-order consequences where earned. Explain mechanisms and independent reinforcement. There is no four-to-six-theme requirement.

**3. Mental Models:** reusable frameworks/distinctions with explanation, why they help reason about tomorrow, source/provenance and limits. Prefer useful source-derived models; label original models as researcher-created. Do not give a technical mechanism a duplicate framework write-up.

**4. Technical Concepts:** for each earned mechanism/theory/study, give What it is, Why it matters, Source/Provenance, and What changed where supported. Explain the prior constraint, enabling change, limitations and implication for future capability or product design. Omit an unsupported What changed line rather than guessing. Do not fill a glossary quota.

**5. What to Retain, Downgrade, or Remove:** make confidence judgments beside the material being judged:
- **Retain:** well-supported facts/observations and clearly attributed reasoning appropriate to their scope. An original argument can be retained as an argument; a future inference remains an inference even with strong factual premises.
- **Downgrade:** emerging signals, narrow studies, dependent reports, unscaled products, uncertain generalizations or speculative forecasts; specify the qualification and why. A single source can establish its own product fact without establishing a market outcome.
- **Remove:** unsupported factual/quantitative claims, misattributed outcomes, duplicated material, empty marketing and low-value arguments. Thoughtful practitioner opinion is not removed automatically: evaluate its reasoning and use it as interpretation, not observed population evidence.

Account explicitly for important prior claims whose status changes. Do not silently drop inconvenient evidence or erase original records.

Within Section 5 include:
- **Live Tensions:** name both poles; strongest sourced Side A and Side B; why unresolved; chapter use. Usually a few, but no quota. Preserve genuine disagreement without forcing a resolution or false balance. If no live tension survives scrutiny, say so briefly.
- **Disconfirming Evidence:** specific observable conditions that would weaken the main claim; actual question-led searches/source inspections and results, including nulls; pointer to Section 7's falsifier. Prior evidence can satisfy the check if it addresses the conditions. If not, perform a small bounded native/authorized-provider check or flag the consequential gap. Never fabricate a disconfirmation search to complete the template.

**6. Chapter Synthesis Ideas:** give earned alternatives with Core framing and Chapter flow: Opening, meaningful sections, Closing. Connect to the supplied book outline/themes. Show why a narrative works and what argument, surprising example, distinction or tension it could develop. No mandatory three/four ideas and no new factual claims.

**7. Final Conclusion:** state the defensible view of tomorrow, causal conditions and material uncertainty. Close the Central Concept, using retained factual premises while labeling the future scenario/inference. End with What would change this conclusion: a specific observable breaking condition, followed by key sources. Avoid an inevitable-future claim or a conclusion so hedged it says nothing.

**8. Research Gaps & Opportunities:** only consequential unanswered questions. For each: why it matters; what supplied or newly checked evidence/searches show; chapter guidance. Handoff G/Q IDs, evidence needed, professional owner and exit condition. Absence of a source-category finding is not automatically a substantive gap, but an unattempted rung is a research-process omission to correct.

### Integrate future forms without losing the seven sections

Put future product forms/interaction models and second-order arguments in Themes; reusable scenario distinctions in Mental Models; enabling capabilities/constraints in Technical Concepts; competing evidence and unresolved scenarios in Section 5; chapter uses in Section 6; the conditional integrated future in Section 7. A scenario can sit under the theme it explains. Do not duplicate its full discussion in several sections.

Show cross-perspective dependencies: capability can enable a design; observed user needs can change the viable product; economics/distribution can shape adoption; governance can change permissible action. Sources support premises, and clearly labeled reasoning connects them. The seven sections organize this intellectual work rather than suppressing future exploration.

### Concept registry, relationships and Completeness Summary

Give each concept one full home: mechanism/theory → Section 4; transferable framework/distinction → Section 3; recurring argument → Section 2. Check aliases, synonymous entries and reused examples before Section 5. Cross-reference the home elsewhere, including the Framing Check and confidence judgment. Keep a compact registry: `concept | aliases | home | example | Q/E/source links`.

Where useful keep `force/concept/question | relation (enables/constrains/depends-on/contradicts) | future form/outcome | evidence/inference | confidence/uncertainty`. Preserve stable question/source links and meaningful revisions.

Append the original twelve-field **Completeness Summary** in the traceability appendix; fill it from actual checks:
1. Sections written.
2. Section 8 included, or why omitted.
3. Actual word count.
4. Duplication check and merges.
5. Retain / Downgrade / Remove counts.
6. Input completeness and material omissions.
7. Framing verdict.
8. Live tensions logged or none found.
9. Disconfirming searches/source inspections and results.
10. Falsifier stated in Section 7.
11. What changed lines: count versus technical concepts.
12. Book state read/reconciled or not supplied.

Add current Q/G coverage, all-ten-rung input coverage and pass-specific changes where needed. This is a short audit record, not another prose report or a substitute for source quality. Typical synthesis length 1,500–3,000 words is guidance; richer material can justify more. Never remove substantive evidence or inflate Downgrade/Remove simply to hit a length target.

### Fresh worker brief

```text
Task/mode: future-oriented objective; background/expert/targeted/synthesis
Role: Level 1 generic professional lens, Level 2 specialization/justification or none
Frame: topic, audience, scope, horizon/as-of date, frozen decisions
Questions: guiding BQs or broad validated Q IDs/text; G/exit conditions if targeted
Read: exact frame/background/examples/source-notes/panel/question-rationale paths and immutable snapshot, shared contract, supplied book context
Write: exclusive artifact path(s); never the planner's running index
IDs: allocated namespace and prior IDs to preserve
Provider: requested/effective provider; run-specific Exa authorization record
Done: dedicated stage output, substantive notes, all-ten-rung attempts for retrieval passes, compact traceability and checks
```

Use fresh contexts and immutable handoffs; run independent expert work in parallel when supported. Return artifact paths, question/gap status, material limitations and next handoff. The planner alone merges the canonical map/index and saves accepted stage documents.

## 6. Native Google Docs and portable delivery

Create one dedicated run folder and a separate native Google Doc for every completed stage. Keep parallel investigations as clearly separated expert sections in the corresponding numbered stage document, preserving full substantive notes. Only targeted research Step 08 may be skipped when unwarranted; record the reason in the index, and still complete a fresh final synthesis at Step 09. The final package links accepted stages, avoiding repeated full reports.

Use the current Google Drive/Docs skill for the native creation route. Use Title, Heading 1 and Heading 2 styles, short readable paragraphs, moderate spacing, selective bold and clickable citations. Insert page breaks between major expert sections when useful. Group findings by ideas, not categories; keep process/evidence metadata in compact appendices. Do not simulate formatting with raw Markdown headings, spacer paragraphs, repeated blank lines or evidence IDs dominating the narrative.

After saving, verify content, native MIME type, actual heading styles/links and run-folder membership before recording success. Update existing stage docs by ID. Keep portable Markdown and structured handoffs for migration; when native persistence is unavailable, disclose the limitation and use an authorized equivalent destination.

## 7. Original-skill provenance and deliberate adaptations

Sources inspected at Writing-agent commit `3e47309c5d25d4493fb5e844caba992c20fb7602`:
- [Broad Research](https://github.com/anshulprojectmgmt/Writing-agent/blob/3e47309c5d25d4493fb5e844caba992c20fb7602/Book%20Orchestrator%20Agent/Broad-research-node/broad-research-agent/SKILL.md).
- [Research Analysis](https://github.com/anshulprojectmgmt/Writing-agent/blob/3e47309c5d25d4493fb5e844caba992c20fb7602/Book%20Orchestrator%20Agent/research-analysis-node/Research%20Analysis%20Agent/SKILL.md) and its [formatting reference](https://github.com/anshulprojectmgmt/Writing-agent/blob/3e47309c5d25d4493fb5e844caba992c20fb7602/Book%20Orchestrator%20Agent/research-analysis-node/Research%20Analysis%20Agent/references/output-formatting.md).

| Original capability | Preserve | Deliberate adaptation |
|---|---|---|
| Broad Research ten rungs and primary-voice channels | All ten categories, named source/channel examples, ground-floor and blind-spot checks | All rungs attempted on every retrieval pass; relevance-driven depth, no finding quotas |
| Term/Query Map | Retrieval vocabulary only as temporary search operations | Question Map with future-oriented umbrella questions, background grounding and evolving links |
| Per-finding source labels/evidence cards | Source type, provenance, dates, authority/scope, confidence, concrete claim and why it matters | Substantive narrative notes; compact source/insight records instead of repetitive cards |
| Research Analysis Framing Check | Five reasoning blocks and visible verdict | Autonomous/stepwise behavior follows the user's instructions; no silent reframe |
| Seven core sections | Central Concept, Themes, Mental Models, Technical Concepts, Retain/Downgrade/Remove, Chapter Synthesis Ideas, Final Conclusion | Explicit future forms/scenarios and cross-perspective integration; no fixed item quotas |
| Concept deduplication | One full write-up per concept, aliases, reused-example check, registry | Compact appendix; preserve useful knowledge relationships |
| Evidence judgment | Attribution, explicit reassessment, strong facts versus weak generalization | Practitioner/analytical arguments assessed on reasoning rather than automatically excluded; future inference remains labeled |
| Live Tensions / Disconfirming Evidence | Both sides, source-backed disagreement, actual checks/nulls, strongest challenges | No fabricated tension or mandatory number of searches; consequential gaps handed off |
| Final falsifier | Specific observable condition that would change the conclusion | Future scenarios stated conditionally; evidence validates premises without pretending to prove tomorrow |
| Optional gaps / chapter ideas | Material gaps, chapter implications, narrative opening/flow/closing | Conditional targeted retrieval; fresh final synthesis still required |
| Twelve-field Completeness Summary | Real section/count/check fields | Compact traceability appendix, separated from the reading flow |
| HTML/Gumloop rendering | Readable hierarchy, separated paragraphs, emphasis, source links, complete content | Current native Google Docs adapter, verified styles/links/folder placement; portable Markdown, no legacy spacer template |

The legacy skills remain unchanged as separate workflows. This canonical contract governs the three Research-workflow skills; do not import contradictory legacy quotas, Query Maps or formatting rules. Question-grounded multi-perspective exploration is also inspired by Stanford OVAL Co-STORM, but this workflow neither installs nor claims to execute its engine.

