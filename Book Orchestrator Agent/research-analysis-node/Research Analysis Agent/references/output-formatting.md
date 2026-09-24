# Output Formatting Rules — Research Analysis Synthesis (HTML)

Applies to the HTML produced by the Research Analysis skill, after the
synthesis's content (Framing Check + Sections 1–8 + Completeness Summary) has
been fully drafted per the skill's own section-by-section spec and Output
Format template.

That HTML is sent to Google Docs as the document body, so **the markup
written here is the source of truth for how the Doc looks.** The converter
renders what the markup encodes and nothing more.

**This file governs layout only — never content.** Every claim, label,
source, and figure must appear with the exact wording produced during
synthesis. Nothing here justifies shortening, merging, or rewording anything
to make it fit a template.

Every block below is given as a template. **Emit the markup exactly**,
including every spacer paragraph. Replace only the `{placeholders}`.

---

## What the converter supports

This has been tested against the actual Google Docs conversion. Build only
with what is on the left column.

| Works | Does not work |
|---|---|
| `<h1>` `<h2>` `<h3>` — become real Doc heading styles | **`style="..."` attributes — silently stripped** |
| `<strong>` — bold | `<style>` blocks — ignored |
| `<em>` — italic | Any CSS margin, padding or spacing |
| `<a href="...">` — clickable hyperlink | `class=` — no stylesheet exists |
| `<hr>` — horizontal divider | Blank lines in the source — collapse to nothing |
| `<ul>` `<ol>` `<li>` — real Doc lists | Indentation in the source — ignored |
| `<p>` — a paragraph | Text color — no `foregroundColor` equivalent survives |

**CSS does not survive the conversion.** Do not write a single `style`
attribute. There is no color equivalent in this pipeline, so the Palette
guidance from earlier versions of this file (navy headings, gray dividers)
does not apply here — headings, dividers, and field labels are unstyled
`<h1>`/`<h2>`/`<h3>`, `<hr>`, and `<strong>` only. Spacing is created
structurally, with the spacer paragraph below, and by no other means.

---

## Standing rule: the spacer paragraph

Google Docs renders consecutive `<p>` elements with **no gap between them**.
Whitespace in the source HTML changes nothing — the converter ignores it.

The only way to create a visible blank line is to emit a paragraph that holds
a non-breaking space:

```html
<p>&nbsp;</p>
```

This is the single spacing mechanism in this document. **Put one between
every pair of blocks.** A theme whose heading, gloss, explanation, example
and sources are emitted as five consecutive `<p>` elements with no spacers
between them renders as a dense, unreadable stack — the exact defect that
collapsed the original Completeness Summary, and the Technical Concepts and
Live Tensions sections, into a wall of text. That is the one failure this
file exists to prevent.

**Wrong** — no spacers, so all lines stack tight:

```html
<p><strong>Theme 1: {Short heading}</strong></p>
<p><em>{One-line gloss.}</em></p>
<p>{Explanatory paragraph.}</p>
<p><strong>Example:</strong> {…}</p>
<p><strong>Sources:</strong> {…}</p>
```

**Right** — a spacer between every part:

```html
<p><strong>Theme 1: {Short heading}</strong></p>
<p>&nbsp;</p>
<p><em>{One-line gloss.}</em></p>
<p>&nbsp;</p>
<p>{Explanatory paragraph.}</p>
<p>&nbsp;</p>
<p><strong>Example:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Sources:</strong> {…}</p>
<p>&nbsp;</p>
```

Same markup, same order. The spacers are the entire difference between the
two renders.

**On repeated titles: no `<h4>`.** The converter only turns `<h1>`–`<h3>`
into real Doc heading styles (see table above), so unlike an earlier,
Docs‑API‑driven version of this file, repeated entity titles — a Theme, a
Mental Model, a Technical Concept, a Tension, a Chapter Synthesis Idea, a
Research Gap — are **not** promoted to a heading level here. They stay
`<strong>` inside their own `<p>`, exactly as Finding titles do in the Broad
Research brief this skill consumes, and for the same reason: promoting every
repeated title to a real
heading would flood the Doc's outline pane and make it useless for
navigation. The spacer paragraph and the `<hr>` divider — not a heading
level — are what separate one theme, model, concept, tension, idea, or gap
from the next.

---

## 1. Framing Check (gate)

```html
<h2>Framing Check</h2>
<p>&nbsp;</p>
<p><strong>The stated question:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>The actual question:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>The assumption underneath:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>The constraint test:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>One serious alternative frame:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>FRAMING: {HOLDS / REFRAME PROPOSED}</strong></p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- **Five field paragraphs, one spacer after each** — `The stated question`
  through `One serious alternative frame`. Two of these fields sharing a
  paragraph is the specific defect this block exists to prevent.
- The verdict is its own bold paragraph, never appended to the fifth field.
- If `FRAMING: REFRAME PROPOSED`, the verdict paragraph is followed by the
  one‑sentence reframe summary as its own paragraph (with its own spacer)
  before the `<hr>` — this is the line that travels with the Doc link per
  the skill's gate behavior, so it must be visible, not buried.

---

## 2. Section 1 — Central Concept

```html
<h2>1. Central Concept</h2>
<p>&nbsp;</p>
<p>{Paragraph one.}</p>
<p>&nbsp;</p>
<p>{Paragraph two.}</p>
<p>&nbsp;</p>
<p>{Paragraph three, if present.}</p>
<p>&nbsp;</p>
<p><strong>Sources:</strong> {…}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Each paragraph the research step wrote is its own `<p>` with a spacer after
it — never merge the two or three paragraphs into one block. `Sources` is
always the closing field, in its own paragraph.

---

## 3. Section 2 — Themes

Each theme is its own visually separated group:

```html
<h2>2. Themes</h2>
<p>&nbsp;</p>
<p><strong>Theme 1: {Short heading}</strong></p>
<p>&nbsp;</p>
<p><em>{One-line plain-language gloss.}</em></p>
<p>&nbsp;</p>
<p>{Explanatory paragraph one.}</p>
<p>&nbsp;</p>
<p>{Explanatory paragraph two, if present.}</p>
<p>&nbsp;</p>
<p><strong>Example:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Sources:</strong> {…}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- **A spacer after the title, after the gloss, after each explanatory
  paragraph, after `Example`, and after `Sources`.** A theme with fewer is
  wrong.
- The one-line gloss is the only italicized line in this section — it is
  content, not a field label, so it gets `<em>`, not `<strong>`.
- Where the explanation runs 2–3 proper paragraphs (per the skill's own
  format rule), each is its own `<p>`, never one dense block.
- `<hr>` separates themes, with a spacer before and after it.

---

## 4. Section 3 — Mental Models

```html
<h2>3. Mental Models</h2>
<p>&nbsp;</p>
<p><strong>{Model Name} ({Theorist, if named})</strong></p>
<p>&nbsp;</p>
<p>{Explanatory paragraph one.}</p>
<p>&nbsp;</p>
<p>{Explanatory paragraph two, if present.}</p>
<p>&nbsp;</p>
<p><strong>Why it matters:</strong> {…}</p>
<p>&nbsp;</p>
<p><em>Source: {…}</em></p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- Models are ordered strongest‑explanatory‑leverage first, per the skill —
  this file does not reorder them, only marks them up in the order given.
- Where a model is fundamentally an X‑vs‑Y distinction, render the contrast
  as a `<ul>` inside the explanatory paragraph's position (a spacer before
  and after the list, no spacer between its `<li>` items):

```html
<p>&nbsp;</p>
<ul>
<li><strong>{X}:</strong> {…}</li>
<li><strong>{Y}:</strong> {…}</li>
</ul>
<p>&nbsp;</p>
```

- `Source` stays italic, matching the skill's own template — the one field
  in this section that is not bold.

---

## 5. Section 4 — Technical Concepts

**This section was the worst offender in earlier drafts** — concept names
written as bold plain text ran straight into the previous concept's last
bullet with no visible gap. The rules below exist specifically to prevent
that.

```html
<h2>4. Technical Concepts</h2>
<p>&nbsp;</p>
<p><strong>{Concept Name}</strong></p>
<p>&nbsp;</p>
<ul>
<li><strong>What it is:</strong> {…}</li>
<li><strong>Why it matters:</strong> {…}</li>
<li><strong>Source:</strong> {…}</li>
<li><strong>What changed:</strong> {…} <em>(when present)</em></li>
</ul>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- **A spacer after the concept's title, before the `<ul>`,** and a spacer
  after the closing `</ul>` before the `<hr>`.
- No spacer between the `<li>` items — a spacer inside a list breaks it into
  two lists.
- `What changed` is only emitted when the research step actually wrote it;
  never insert an empty `<li>` to keep a uniform four-bullet shape.
- `<hr>` separates concepts, with a spacer before and after it.

---

## 6. Section 5 — Retain / Downgrade / Remove, Live Tensions, Disconfirming Evidence

Three tiers first, each a bold label followed by its own list:

```html
<h2>5. What to Retain, Downgrade, or Remove</h2>
<p>&nbsp;</p>
<p><strong>Retain</strong></p>
<p>&nbsp;</p>
<ul>
<li>{Claim} &mdash; ({Source attribution})</li>
<li>{Claim} &mdash; ({Source attribution})</li>
</ul>
<p>&nbsp;</p>
<p><strong>Downgrade</strong></p>
<p>&nbsp;</p>
<ul>
<li>{Claim} &mdash; {One-line reason}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Remove</strong></p>
<p>&nbsp;</p>
<ul>
<li>{Claim} &mdash; {One-line reason}</li>
</ul>
<p>&nbsp;</p>
```

Then **Live Tensions** as its own subsection — promoted to `<h3>`, the same
way Rung subheadings sit inside Section 3 of the Broad Research brief,
because it is a distinct block within Section 5, not another tier:

```html
<h3>Live Tensions</h3>
<p>&nbsp;</p>
<p><strong>{Pole A} vs. {Pole B}</strong></p>
<p>&nbsp;</p>
<ul>
<li><strong>Side A:</strong> {…} <em>({source})</em></li>
<li><strong>Side B:</strong> {…} <em>({source})</em></li>
<li><strong>Why it stays open:</strong> {…}</li>
<li><strong>Chapter use:</strong> {…}</li>
</ul>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Repeat the tension block (title + list + divider) for each of the 1–3
tensions, or — where none exists — a single honest paragraph in place of the
block: `<p>{One line naming the closest thing to a disagreement, or stating
plainly that none was found.}</p>` followed by its spacer.

Then **Disconfirming Evidence**, also `<h3>`:

```html
<h3>Disconfirming Evidence</h3>
<p>&nbsp;</p>
<p><em>What would weaken this</em></p>
<p>&nbsp;</p>
<ul>
<li>{Specific, falsifiable condition}</li>
<li>{Specific, falsifiable condition}</li>
</ul>
<p>&nbsp;</p>
<p><em>Searches run</em></p>
<p>&nbsp;</p>
<ul>
<li>{What was searched} &rarr; {what came back, including null results}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Falsifier:</strong> stated at the close of Section 7.</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- `What would weaken this` and `Searches run` are italic labels, each its
  own paragraph, immediately followed by their own `<ul>` — never merged
  into one list.
- `Falsifier` is the closing paragraph of Section 5, bold label, plain text
  after it — it is a pointer to Section 7, not a repetition of it.
- Do not put `<p>&nbsp;</p>` between `<li>` elements anywhere in this
  section.

---

## 7. Section 6 — Chapter Synthesis Ideas

```html
<h2>6. Chapter Synthesis Ideas</h2>
<p>&nbsp;</p>
<p><strong>Idea 1: {Idea name}</strong></p>
<p>&nbsp;</p>
<p><strong>Core framing:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Chapter flow:</strong></p>
<p>&nbsp;</p>
<ul>
<li><strong>Opening:</strong> {…}</li>
<li><strong>Section 1:</strong> {…}</li>
<li><strong>Section 2:</strong> {…}</li>
<li><strong>Section 3:</strong> {…}</li>
<li><strong>Section 4:</strong> {…} <em>(if applicable)</em></li>
<li><strong>Closing:</strong> {…}</li>
</ul>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- `Core framing` is a normal paragraph. `Chapter flow` introduces the list
  and is never itself an `<li>`.
- No spacer between the `<li>` items inside `Chapter flow`.
- `<hr>` separates ideas, with a spacer before and after it.

---

## 8. Section 7 — Final Conclusion

```html
<h2>7. Final Conclusion</h2>
<p>&nbsp;</p>
<p>{Paragraph one.}</p>
<p>&nbsp;</p>
<p>{Paragraph two.}</p>
<p>&nbsp;</p>
<p>{Paragraph three, if present — the standalone closing claim.}</p>
<p>&nbsp;</p>
<p><strong>What would change this conclusion:</strong> {…}</p>
<p>&nbsp;</p>
<p><em>Sources supporting the conclusion: {…}</em></p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

The final paragraph — the one‑sentence claim the chapter builds toward —
stays its own `<p>`, never folded into the paragraph before it.
`Sources supporting the conclusion` stays italic, matching the skill's own
template.

---

## 9. Section 8 — Research Gaps & Opportunities *(omit entirely if not warranted)*

```html
<h2>8. Research Gaps &amp; Opportunities</h2>
<p>&nbsp;</p>
<p><strong>Gap 1: {Specific unanswered question}</strong></p>
<p>&nbsp;</p>
<p>{Explanatory paragraph.}</p>
<p>&nbsp;</p>
<p><strong>Web search findings:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Updated guidance for the chapter:</strong> {…}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

If Section 8 was correctly omitted from the synthesis per the skill's
inclusion rule, omit this heading and block entirely — do not emit an empty
`<h2>8. Research Gaps &amp; Opportunities</h2>` with nothing under it. A
divider between gaps only applies when there is more than one gap.

---

## 10. Completeness Summary

The single most common failure point in earlier drafts — up to 12 fields
collapsing into a wall of text. Every field is its own bold-labeled
paragraph, with a spacer after each:

```html
<h2>Completeness Summary</h2>
<p>&nbsp;</p>
<p><strong>Sections written:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Section 8 included:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Word count:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Duplication check run:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Retain / Downgrade / Remove counts:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Input completeness:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Framing verdict:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Live tensions logged:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Disconfirming searches run:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Falsifier stated in Section 7:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Section 4 "What changed" lines:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>Book state document:</strong> {…}</p>
<p>&nbsp;</p>
```

Count the fields before finishing: there must be exactly twelve field
paragraphs, one per field. Two labels sharing a paragraph is the defect that
made this section unreadable in earlier drafts — it is the one this file
exists to prevent, here most of all.

---

## 11. General

**Document skeleton.** The synthesis opens with the title carrying the
topic, then runs the Framing Check gate and the numbered sections in order:

```html
<h1>{Topic} &mdash; Research Synthesis</h1>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<h2>Framing Check</h2>
<p>&nbsp;</p>
...
```

**Heading levels.** Headings become the Doc's real Heading styles, which is
what makes the outline pane work:

| Tag | Used for |
|---|---|
| `<h1>` | The document title, carrying the topic |
| `<h2>` | `Framing Check`, the numbered sections 1 through 8, and `Completeness Summary` |
| `<h3>` | `Live Tensions` and `Disconfirming Evidence`, the two subsections inside Section 5 |
| `<strong>` | Theme / Model / Concept / Tension / Idea / Gap titles, and every field label — body text, not headings |

Repeated titles stay `<strong>` inside a `<p>` on purpose: promoting each one
to a heading would flood the Doc's outline pane and make it useless for
navigation — see the spacer-paragraph rule above.

**No escaped section numbers.** Write `<h2>1. Central Concept</h2>`, not an
escaped or backslashed form.

**Escape HTML special characters in content.** `&` becomes `&amp;` — this
matters in `Research Gaps &amp; Opportunities` and any claim or source name
containing an ampersand. `<` becomes `&lt;` and `>` becomes `&gt;`. Em dashes
are written `&mdash;`; the "leads to" arrow in `Searches run` bullets is
written `&rarr;`.

**Never emit an empty heading.** A heading with no text — or a Section 8
heading emitted with nothing under it because the section was correctly
omitted — renders as blank space and shows in the outline pane as an empty
entry.

**Hyperlinks.** Where a source is a real URL rather than a short in-text
citation, write it as `<a href="{URL}">{URL}</a>`, the address in both
places. Never leave a bare URL as plain text, and never replace the link
text with a publication name or title. Where the skill's own format gives a
short parenthetical or in-line citation instead of a URL, keep it as plain
text — do not invent a link.

**No CSS, anywhere.** No `style` attributes, no `<style>` blocks, no
`class`, and no color. They are stripped in conversion and their presence
gives a false impression that spacing or emphasis is handled by something
other than the markup itself. `<p>&nbsp;</p>` is the only spacing mechanism,
and `<strong>`/`<em>` are the only emphasis mechanisms.

**Verify before delivering.** Re-read the generated HTML and confirm:

1. The Framing Check has a spacer after each of its five fields and after
   the verdict paragraph.
2. Every theme has a spacer after its title, its gloss, each explanatory
   paragraph, `Example`, and `Sources` — and no two of these fields share a
   paragraph.
3. Every mental model has a spacer after its title, each explanatory
   paragraph, `Why it matters`, and the italic `Source` line.
4. Every technical concept has a spacer after its title, before its `<ul>`,
   and after the `<ul>` — with `What it is`, `Why it matters`, `Source`, and
   (when present) `What changed` as real `<li>` items, not `<p>` lines.
5. Retain, Downgrade, and Remove are each a bold label followed by a real
   `<ul>`, with no spacer between `<li>` items.
6. Live Tensions is a real `<h3>`, each tension has a bold title and a
   four-item `<ul>` (`Side A`, `Side B`, `Why it stays open`, `Chapter use`),
   and a divider sits between tensions.
7. Disconfirming Evidence is a real `<h3>`, with `What would weaken this` and
   `Searches run` as their own italic-labeled paragraphs each followed by
   their own `<ul>`, and `Falsifier` as its own closing bold-labeled
   paragraph.
8. Every chapter synthesis idea has `Core framing` as a paragraph and
   `Chapter flow` as a labeled paragraph followed by a real `<ul>` with no
   spacers between its items.
9. The Final Conclusion's closing claim is its own paragraph, and
   `Sources supporting the conclusion` stays italic.
10. Section 8 is either fully formatted with dividers between multiple gaps,
    or entirely absent — never an empty heading.
11. The Completeness Summary has exactly twelve field paragraphs, one per
    field.
12. Not one `style`, `class`, `<style>`, or color attribute appears in the
    output, and no literal Markdown characters (`#`, `**`, `-`, `---`)
    survive anywhere in the Doc text.
