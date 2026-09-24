---
name: research-analysis-skill-v2
description: >
  Analyze a broad-research brief (or any long, source-heavy research document) into a compact synthesis a book author can actually think with. Use when the user has a long research brief/doc that feels overwhelming and asks to "make sense of it," "pull out key themes," "summarize the research," "analyze the research," or "help me understand this before I write." Produces a fixed seven-section synthesis covering Central Concept, Themes, Mental Models, Technical Concepts, Retain/Downgrade/Remove, Chapter Synthesis Ideas, and Final Conclusion, opening with a framing check and carrying live tensions, disconfirming evidence, and a stated falsifier alongside the material they judge.
---

# Research Analysis

Turns a long, source-heavy research brief into a compact synthesis organized for
writing, not for research bookkeeping — material that is thorough but too raw
to write a chapter from directly.

---

## GenAI Lens *(standing rule, consistent with broad-research)*

This book's domain is generative AI, so when distilling Themes, Mental Models, and Technical Concepts, favor genAI-specific framings where the source material genuinely supports one, rather than defaulting to generic technology framing.

---

## Judgment *(standing rule)*

Organizing what a brief contains and thinking about what it claims are
different jobs, and this skill does both. Alongside the distillation,
interrogate what the brief *assumes*, what would *break* it, and what it leaves
genuinely unsettled: the framing the topic rests on, the constraint under each
mechanism, the evidence that would weaken the conclusion, and the places where
two well-supported claims disagree.

That judgment belongs next to the material it judges. A reader who skims
Section 5 should see the disconfirmation attempt there, not in an appendix they
may never reach.

**Research is a service to thinking, not a substitute for it.** Where the
judgment comes up empty — the framing holds, no counter-evidence surfaced, no
real tension exists — say so plainly in one line. An honest empty result is a
finding. A manufactured tension is not.

---

## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `broad_research_doc_link` | URL | Required | Google Doc produced by the `broad-research` skill — the research brief for this chapter topic. If unavailable, substitute a comparable long-form research document (.docx, .md, .pdf, or pasted text). |
| `research_analysis_folder_link` | URL | Required | The Drive subfolder under the main agent's workspace where this skill's output gets saved. |
| `book_state_doc_link` | URL | Optional | The book's running state document: frozen structural decisions, terminology already settled, rejected framings and why, and open tensions carried across chapters. Read it before drafting so the Framing Check does not reopen a settled decision and Section 5 does not re-raise a tension the author already parked. If absent, proceed without it and note that in the Completeness Summary. |

**Required content of the research document** — the skill needs at least
these to function; if any are missing, note it and proceed with what's
available rather than blocking:
- A stated research objective or topic framing
- A body of findings organized by source (rungs, categories, or sections)
- Some signal of evidence quality per finding (source type, authority rating,
  freshness, or an equivalent confidence marker)

A `broad-research` brief has exactly three sections: Research Objective, Query
Map, and Source Ladder Findings. Every finding carries its own
`SOURCE TYPE | AUTHORITY | FRESHNESS | USE` labels and an evidence card
(`CLAIM`, `WHY IT MATTERS`, `CONFIDENCE`). The brief has no synthesis sections —
no core concepts, case studies, risks, PM signals, gaps, strong/weak signal
lists or completeness summary. Do not look for them; building that synthesis
from the findings is this skill's job.

**Handling multiple files:** if more than one research document is provided
for the same topic, read all of them before starting Section 1 — the
Central Concept and Themes should reflect the combined material, not just
the first file opened.

---

---

## The sections

The output always follows the same seven core sections, in this order. Do not
reorder them, rename them, or skip one — the fixed structure is what makes this
usable across many chapters/topics. An eighth section, Research Gaps &
Opportunities, is optional and only appended when it earns its place.

Where a section carries judgment as well as material — the constraint under a
mechanism, the evidence that would weaken a claim — that judgment sits
alongside the material it judges and never restates, contradicts, or
restructures it.

Each section below is specified the same way: **Purpose** (why it exists),
**Format** (exactly how to write it), and **Source signal** (what part of the
input it draws on).

**Every named concept gets ONE full write-up, in exactly one section.**
Repetition across Themes, Mental Models, Technical Concepts, and Retain is
the most common failure mode of this skill — a concept like "contextual
integrity" genuinely satisfies more than one section's definition, and
without a rule forcing a single home, it's easy to give it a full write-up
in two or three places. To prevent this:

1. **Keep a running registry** while drafting Sections 2-4. Before writing a
   new entry, check the name against everything already written up in this
   pass. If it's already been given a full write-up, it does not get another
   one.
2. **Decide the single best-fit section using this order of preference:**
   a named theory/mechanism with a clear "how it's built or works" answer →
   Technical Concepts (4). A named, transferable, reader-applicable
   framework or X-vs-Y distinction → Mental Models (3). A recurring
   claim/argument without a clean transferable framework → Themes (2).
   Apply this test once per concept and commit to the answer.
3. **Everywhere else, cross-reference instead of re-explaining.** If a
   concept placed in Section 3 needs to come up again in Section 2 or 7, name
   it in a single clause ("...which is really an application of the
   Contextual Integrity model above...") — never repeat its definition,
   example, or source citation a second time.
4. **Run a final duplication check before writing Section 5.** Re-scan
   Sections 1-4 specifically for: the same named concept with a full
   write-up twice, two differently-worded entries describing the same
   underlying idea, or the same concrete example reused as "the" example in
   more than one section. Merge or cut duplicates before moving on — do not
   carry them into Retain/Downgrade/Remove, where a duplicated claim would
   look like two independent claims.
5. **The registry covers the Framing Check and Section 5 as well.** Both name
   concepts constantly — a framing rests on a mental model, a tension sits
   between two technical concepts. Name them in a clause
   and point back ("...the Contextual Integrity model in Section 3..."). Never
   re-explain a concept that already has a full write-up above.

### Framing Check *(gate — opens the document)*
- **Purpose:** Test the chapter's framing before accepting it. The seven
  sections answer "what does this research contain?" This gate answers "is the
  chapter asking the right question of it?" It is the only place in the
  pipeline licensed to say the topic itself is wrong, and it runs before the
  synthesis is drafted, not after.
- **Format:** Five short blocks, one to three sentences each, then a verdict:
  - **The stated question** — the chapter topic as given.
  - **The actual question** — what the material suggests is really at stake.
    These are often the same; say so when they are.
  - **The assumption underneath** — what must be true for the stated framing
    to make sense.
  - **The constraint test** — what condition made the current practice or
    belief rational, whether that condition still holds, and what changed if
    it doesn't. This is where the non-obvious insight usually sits.
  - **One serious alternative frame** — a genuinely different way to organize
    the chapter, argued in good faith, not a strawman. If none is credible,
    write one line saying the framing survived a real attempt to break it.
  - Verdict on its own line: **`FRAMING: HOLDS`** or
    **`FRAMING: REFRAME PROPOSED`**.
- **Gate behavior:** `REFRAME PROPOSED` is a stop, not a note. Surface it to
  the author before the synthesis is used for drafting, and let them accept or
  reject it. Do not reframe the seven sections on your own judgment, and do not
  quietly proceed as if the check had passed. A rejected reframe is a useful
  result: record it in the book state document as a rejected framing with its
  reason, so no later chapter reopens it.
- **Length:** Keep it under 200 words. It is a gate, not a section — if it runs
  long, the framing is being argued rather than tested.
- **Source signal:** The stated research objective, the framing that recurs
  across rungs, and the book state document's frozen decisions and rejected
  framings if one was supplied.

### 1. Central Concept
- **Purpose:** State what the entire research topic actually reduces to —
  the thing every other section should visibly serve.
- **Format:** Write as 2-3 clear paragraphs separated by blank lines. The
  first paragraph covers one curve/aspect, the second covers the other, and
  the third (if needed) states the combined insight. End with a **Sources**
  line listing the key sources that support this framing. Test: if a reader
  only reads this section, they should be able to explain the topic's core
  tension to someone else.
- **Source signal:** The stated research objective, plus whatever framing
  recurs independently across multiple source-ladder rungs or sections.

### 2. Themes
- **Purpose:** Surface the recurring narrative threads the research is
  *arguing* — distinct from the frameworks in Section 3, which are *how*
  it explains itself.
- **Format:** 4-6 themes. For each theme:
  1. Use a **short heading** (2-5 words, a label rather than a sentence).
  2. Add a one-line plain-language explanation in italics immediately below
     the heading (e.g. *"Products are shifting from scheduled releases to
     continuous improvement"*).
  3. Follow with 3-5 sentences of prose broken into 2-3 proper paragraphs
     (separated by blank lines), explaining what the theme actually claims.
  4. Include a **concrete example** on its own line prefixed with
     `- **Example:**` as a bullet point.
  5. Include a **Sources** line prefixed with `- **Sources:**` as a bullet
     point.
  6. Separate each theme from the next with a `---` horizontal rule.
  The insight belongs in the explanation, not the heading.
- **Source signal:** Ideas restated by multiple independent sources in the
  brief — repetition across unrelated sources is the signal a theme is real
  rather than a single source's pet framing.

### 3. Mental Models
- **Purpose:** Extract the reusable, transferable frameworks a reader could
  apply to a product or example they've never seen.
- **Format:** Prefer models the source document already names explicitly
  (frameworks, dichotomies, named principles) over models you invent. Use
  bullet-pointed contrasts where a model is fundamentally a distinction
  (X vs. Y). Write the description as 2-3 proper paragraphs separated by
  blank lines, not a single dense block. Include a **Why it matters** line
  and a **Source** line. Separate each model from the next with a `---`
  horizontal rule.
- **Source signal:** Named frameworks, dichotomies, or principles in the
  research. If the source's core-concepts section blends a conceptual model
  with a narrower technical mechanism, split them — models go here,
  mechanisms go in Section 4.

### 4. Technical Concepts
- **Purpose:** Explain the mechanisms, architectures, named studies, and
  named theories that explain *how* the phenomenon works or gets built, as
  opposed to how to think about it.
- **Format:** For each concept: **What it is** (one sentence), **Why it
  matters** (one sentence), and **Source/Provenance** (one sentence of
  provenance if traced to a named theorist/paper). Use bullet points.
- **What changed:** where the brief genuinely supports it, add a fourth line
  to each concept: the constraint that made this mechanism necessary, and where
  it breaks (one sentence). Documenting a mechanism is not the same as
  understanding it, and this line is what the chapter's
  tension-before-mechanism structure is later built from. Omit it rather than
  speculate — three fields is a complete concept.
- **Source signal:** Named theorists, papers, or mechanisms in the research,
  plus any outside grounding verified in "Before starting" — if a concept
  traces back to a named academic theorist or a specific paper, say so and
  give one sentence of correct provenance.

### 5. What to Retain, Downgrade, or Remove
- **Purpose:** Apply a confidence filter over everything above so the writer
  knows what to lean on and what to treat as color.
- **Format:** Three labeled lists:
  - **Retain** — claims with strong, independent, or legally/empirically
    settled backing. State these plainly in the eventual chapter. Include
    source attribution in parentheses.
  - **Downgrade** — real but early: single-source frameworks, unscaled
    products, academic-only frameworks not yet adopted anywhere. Usable,
    but must be flagged as emerging, not settled. Include a one-line reason.
  - **Remove** — marketing copy, single unverified figures (especially
    market-sizing numbers, which vary wildly by analyst and should never be
    cited as a specific figure), practitioner opinion pieces, or claims of
    demand/behavior not actually observed. Keep at most as color, never as
    evidence. Include a one-line reason.
  Never silently drop a claim the source document flagged as evidenced —
  downgrade or explicitly remove it with a one-line reason instead.
- **Live Tensions:** the three lists above sort claims by *credibility*; this
  one sorts by *disagreement*. Two claims that are both well-sourced and
  genuinely conflict belong here rather than in a tier, and the chapter writer
  needs at least one preserved tension with both sides argued fairly. For each
  tension: a bold one-line title naming the two poles (e.g. **Help vs.
  Surveillance**); **Side A** and **Side B** at one to three sentences each,
  each with its own source and each given its strongest case; **Why it stays
  open** in one sentence; and **Chapter use** in one sentence. Usually one to
  three. **Do not resolve them** — resolving toward the thesis is the writer's
  job, and flattening a real tension here removes exactly the substance the
  list exists to carry. If the evidence *does* settle it, it is not a tension:
  it is a Retain plus a Downgrade. If there is genuinely none, write one line
  saying so and naming the closest thing to a disagreement in the material.
- **Disconfirming Evidence:** the tiers above test whether sources are
  *credible*; this tests whether the framing built on them is *right*. A
  well-sourced claim can still be a wrong claim. Three short parts: **What would weaken this** — two
  or three specific, falsifiable conditions, concrete rather than vague ("no
  shipped product has retained this behaviour past a pilot" beats "the trend
  might not continue"); **Searches run** — what was actually searched, in plain
  language, and what came back, null results included; and a pointer to the
  falsifier stated in Section 7. "Searched for counter-evidence on X and Y,
  found none of substance" is a complete and valuable answer — never invent a
  weak counter-argument to fill it, and never let it become a hedge that
  undercuts a conclusion the evidence genuinely supports.
- **Source signal:** The source document's own evidence-quality signals on
  each finding — its source ladder rung, its `AUTHORITY` and `USE` labels, and
  its evidence card `CONFIDENCE`. For Live Tensions and
  Disconfirming Evidence:
  sources that disagree across Sections 2-4, findings in the brief that cut
  against its likely thesis (typically surfaced by its Query Map's contrarian
  terms or its ethics/regulatory rung), Downgrades whose reason was conflict
  rather than thinness,
  the open tensions in the book state document, and one to three targeted
  searches run against the Central Concept.

### 6. Chapter Synthesis Ideas
- **Purpose:** Give the writer concrete, actionable next steps for turning
  this material into an actual chapter. Present 3-4 distinct structural
  ideas the writer could choose from.
- **Format:** For each idea, use the following two-part structure:
  - **Core framing:** 2-3 sentences explaining what the idea is about —
    the central organizing principle, the reader's takeaway, and why this
    structure works for this material.
  - **Chapter flow:** Bullet-pointed breakdown of the chapter's arc:
    - **Opening:** The hook or framing device
    - **Section 1:** What the first section covers
    - **Section 2:** What the second section covers
    - **Section 3:** What the third section covers
    - **Section 4:** What the fourth section covers (if applicable)
    - **Closing:** How the chapter ends and what the reader takes away
  Each bullet should be 1-2 sentences — enough to convey the idea, not
  a full outline. The section should read like advice from a writing
  partner, not another summary of the research.
- **Source signal:** Synthesized from Sections 1-5 — this section shouldn't
  introduce new claims, only new structural/narrative suggestions.

### 7. Final Conclusion
- **Purpose:** Close the loop opened in Section 1.
- **Format:** 2-3 short paragraphs stating the single defensible claim the
  entire research converges on. Separate paragraphs clearly with blank lines.
  The final sentence should be a standalone paragraph that states the one
  thing the chapter builds toward. Section 1 opens the frame, Section 7
  closes it, everything between is how you get from one to the other.
  Include a **Sources** line listing the key sources supporting the
  conclusion.
- **The falsifier:** close the section with one sentence naming what
  would change this conclusion. Stating a defensible claim and stating its
  breaking point are the same act of judgment; a conclusion nobody can say is
  wrong is not a conclusion. Keep it to one sentence, and keep it specific
  enough that someone could go looking for it.
- **Source signal:** The cumulative weight of Sections 1-6, filtered through
  the Retain tier specifically — the conclusion should be buildable
  entirely from Retain-level material.

### 8. Research Gaps & Opportunities (optional)
- **Purpose:** Flag what the research doesn't cover well enough to write the
  chapter from — the only section that works in the opposite direction from
  1-7, which organize what the research *does* contain.
- **Format:** For each real gap:
  - A **bold gap title** stating the specific unanswered question
  - 2-3 sentences explaining why it matters for the chapter and where the
    source document hints at it without resolving it
  - **Web search findings:** Summarize what 1-3 web searches found to
    partially fill the gap. If nothing was found, say so.
  - **Updated guidance for the chapter:** A concrete recommendation for
    how the chapter should handle this gap — cite the new evidence, frame
    it as an open question, or write around it.
- **Source signal:** The brief's weakest ground — findings marked
  `CONFIDENCE: Low`, rungs carrying a `Note:` for a shortfall or a skip, and
  any claim named in the Research Objective that no finding supports — plus
  any question a careful reader of the finished synthesis would obviously
  still have.
- **Inclusion rule:** Only include this section when a real gap exists that
  would materially weaken the chapter if left unaddressed. Don't manufacture
  a gap for the sake of completeness — an empty or thin "gaps" section is
  worse than omitting it. If nothing meets that bar, skip the section
  entirely and say nothing about it in the output.

---

## Output format

Draft the synthesis's content against the structure below — this is the
content and section spec, not the delivery format. The finished document is
meant to be reused while drafting the chapter, not read once, so once the
content is complete it is rendered as HTML and delivered as a Google Doc per
**Render & Deliver** below, using `references/output-formatting.md` for the
markup. Nothing here is saved as a standalone `.md` file.

Always use this exact structure (omit Section 8 entirely if it doesn't earn
its place — don't leave a header with no content under it):

```markdown
# [Topic] — Research Synthesis

## Framing Check

**The stated question:** [The chapter topic as given.]

**The actual question:** [What is really at stake, or "same as stated" with one line of why.]

**The assumption underneath:** [What must be true for the stated framing to hold.]

**The constraint test:** [What made the current practice rational, whether that still holds, what changed.]

**One serious alternative frame:** [A genuinely different organizing frame, argued fairly — or one line stating the framing survived a real attempt to break it.]

**FRAMING: HOLDS** *(or)* **FRAMING: REFRAME PROPOSED**

---

## 1. Central Concept
[One tight paragraph, anchored by one quotable sentence.]

**Sources:** [key sources supporting this framing]

---

## 2. Themes

**Theme 1: [Short heading, 2-5 words]**

[3-5 sentences explaining what the theme means — the insight lives here, not in the heading.]

*Example: [Concrete example showing the theme in action]*
*Sources: [source parts]*

[Repeat for 4-6 themes]

---

## 3. Mental Models

**Contextual Integrity (Helen Nissenbaum)**

[What it means, in plain language. Use bullet-pointed contrasts for X vs. Y distinctions.]

**Why it matters:** [One sentence on why this model is useful.]

*Source: [citation]*

[Repeat, ranked by explanatory leverage — strongest first]

---

## 4. Technical Concepts

**Ephemeral-by-Design Architecture (EAAI)**

- **What it is:** [One sentence]
- **Why it matters:** [One sentence]
- **Source:** [Citation with provenance note]

[Repeat]

---

## 5. What to Retain, Downgrade, or Remove

**Retain**
- [claim] — [source attribution in parentheses]

**Downgrade**
- [claim] — [one-line reason]

**Remove**
- [claim] — [one-line reason]

**Live Tensions**

**[Pole A] vs. [Pole B]**
- **Side A:** [Strongest version of this case.] *(source)*
- **Side B:** [Strongest version of this case.] *(source)*
- **Why it stays open:** [One sentence.]
- **Chapter use:** [Where this does work in the arc.]

[Repeat for 1-3 tensions, or one honest line if there is none]

**Disconfirming Evidence**

*What would weaken this*
- [Specific, falsifiable condition]
- [Specific, falsifiable condition]

*Searches run*
- [What was searched] → [what came back, including null results]

*Falsifier: stated at the close of Section 7.*

---

## 6. Chapter Synthesis Ideas

**Idea 1: [Idea name]**

**Core framing:** [2-3 sentences explaining what the idea is about.]

**Chapter flow:**
- **Opening:** [The hook or framing device]
- **Section 1:** [What the first section covers]
- **Section 2:** [What the second section covers]
- **Section 3:** [What the third section covers]
- **Section 4:** [What the fourth section covers]
- **Closing:** [How the chapter ends]

[Repeat for 3-4 ideas]

---

## 7. Final Conclusion

[2-3 short paragraphs. Section 1 opens the frame, Section 7 closes it.]

**What would change this conclusion:** [One specific sentence.]

*Sources supporting the conclusion: [key sources]*

---

## 8. Research Gaps & Opportunities  *(only if warranted — omit otherwise)*

**Gap 1: [Specific unanswered question]**

[2-3 sentences explaining why it matters.]

**Web search findings:** [What 1-3 searches found.]

**Updated guidance for the chapter:** [Concrete recommendation.]

[Repeat for each real gap]
```

**Length target:** the synthesis should typically run 1,500-3,000 words
regardless of how long the source research is — a 20,000-word brief and a
6,000-word brief should both produce a synthesis in roughly that range. If a
section is running long, that's a signal to push more material into
Downgrade/Remove in Section 5 rather than to keep everything at full length.
Depth of judgment, not word count, is what makes a section useful here.
Note: including Section 8 with web-search findings and Section 6 with
bullet-pointed chapter flows may push the total toward 3,000-4,000 words —
this is acceptable as long as each section earns its length.

The Framing Check and the two judgment lists in Section 5 carry roughly 400-600
words between them, **over and above the section budget** — do not compress
Themes or Mental Models to make room for judgment about them. If they run long,
the usual cause is re-explaining a concept that already has a full write-up
above, which rule 5 of the duplication registry forbids.

**Tone:** plain and direct. Avoid restating the source document's own
scaffolding language (source ladder, evidence cards, rung numbers) in the
output — those are research-process artifacts, not writing material.
Translate them into confidence judgments (Section 5) instead of exposing the
machinery. Each section should include inline source citations so the
writer knows where every claim comes from without having to cross-reference
the original research brief.

---

## Completeness Summary

Immediately before saving, append a short machine-readable summary block —
this lets the evaluator run its cheap structural checks (section count,
word count, duplication check status) without re-reading the full
synthesis:

```
COMPLETENESS SUMMARY
Sections written: [1-7, plus 8 if included]
Section 8 included: [yes / no — reason if omitted]
Word count: [count]
Duplication check run: [yes — N merges made / yes — none found]
Retain / Downgrade / Remove counts: [R: n, D: n, Rm: n]
Input completeness: [full brief / thin input — note which required elements were missing, if any]
Framing verdict: [HOLDS / REFRAME PROPOSED — one-line summary if proposed]
Live tensions logged: [N — titles, or "none found"]
Disconfirming searches run: [N — findings / none of substance]
Falsifier stated in Section 7: [yes / no]
Section 4 "What changed" lines: [N of M concepts]
Book state document: [read and reconciled / not supplied]
```

---


---

## Render & Deliver

Your input includes `research_analysis_folder_link` — the exact Drive folder
to use. Do not resolve, create, or guess at a different location.

**1. Produce the complete synthesis**, including the Completeness Summary
above.

**2. Render the synthesis as HTML per `references/output-formatting.md`.**
Apply its markup to every block — the Framing Check gate, Sections 1
through 8, and the Completeness Summary — without changing any wording,
claim, label, source, or figure from Step 1. This is a markup pass only.

The output is **HTML, not Markdown**. Three rules decide whether it renders:

- **No CSS.** No `style` attributes, no `<style>` blocks, no `class`. They
  are stripped during conversion, and writing them creates a false
  impression that spacing is handled.
- **Every blank line is a `<p>&nbsp;</p>` spacer paragraph.** Whitespace and
  newlines in the source HTML are ignored by the converter. The spacer is
  the only spacing mechanism that survives.
- **Escape `&` as `&amp;`** in all content, and write em dashes as
  `&mdash;`.

**3. Write the HTML to a file** in the sandbox, e.g.
`/home/user/synthesis.html`. Build it in parts if that is easier;
concatenate to one file before the next step.

**4. Create the Google Doc from code, reading that file into a variable.**

> **Never pass the HTML as a literal tool-call parameter.** A synthesis can
> run to several thousand words once rendered as HTML. Typing it into a
> tool call means re-emitting the whole document as tokens, which
> truncates, fails, and leads to placeholder text being sent instead. The
> document body must reach the tool as a **variable read from the file**,
> never as text you retype. Do not print the HTML to inspect it, and do not
> try to copy it out of a previous output — open the file and pass the
> handle's contents.

```python
with open('/home/user/synthesis.html') as f:
    content = f.read()

from gumloop import Gumloop
client = Gumloop()

result = client.mcp.execute("gdocs", "create_doc", {
    "title": "{Topic} — Research Synthesis",
    "content_format": "html",
    "content": content,
    "folder_id": "{the folder id from research_analysis_folder_link}"
}).results[0]

print("status:", result.status)
if result.status != "success":
    print("error:", result.error)
print(result.decoded_content)
```

Nothing is written anywhere outside that folder.

If the created document ever ends up holding placeholder text, do not
create another one. Fix the same document in place with `update_doc`,
passing `operation: "replace"` and the content read from the file exactly
as above.

**5. Return only the Doc link.** Not the content, not a summary — the Doc
link is your entire output. Nothing else gets returned, and nothing gets
saved or uploaded anywhere outside `research_analysis_folder_link`. The one
thing that travels with the link is a `FRAMING: REFRAME PROPOSED` verdict
and its one-sentence summary, because a gate the author never sees is not a
gate.

---

## References

- `references/output-formatting.md` — defines the **HTML** markup for the
  generated synthesis: how the Framing Check gate, Themes, Mental Models,
  Technical Concepts, Retain/Downgrade/Remove, Live Tensions, Disconfirming
  Evidence, Chapter Synthesis Ideas, Research Gaps, and the Completeness
  Summary must be marked up (never how the content is worded). This
  synthesis is delivered as HTML, not Markdown, following the same
  procedure as the Broad Research skill's own `output-formatting.md`. CSS
  does not survive the Google Docs conversion, so all spacing comes from
  `<p>&nbsp;</p>` spacer paragraphs and never from `style` attributes.
  Apply this at the formatting step in **Render & Deliver** above, after
  the synthesis's content is fully drafted.

---

## Output

| Field | Type | Description |
|---|---|---|
| `doc_link` | URL | Link to the Google Doc containing the completed seven-section (or eight, if Section 8 earns its place) research synthesis, opening with the Framing Check gate. This is the skill's return value — no content, summary, or word count is returned alongside it. |
| `framing_verdict` | String | Returned **only** when the Framing Check concludes `FRAMING: REFRAME PROPOSED` — the verdict line plus a one-sentence summary of the proposed reframe, so the author can accept or reject it before the synthesis is used for drafting. Omitted entirely when the framing holds. |
