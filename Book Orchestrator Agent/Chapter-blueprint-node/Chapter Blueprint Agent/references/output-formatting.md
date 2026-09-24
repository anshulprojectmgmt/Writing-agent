# Output Formatting Rules — Chapter Blueprint (HTML)

Applies to the HTML produced by the Chapter Blueprint skill, after Block 0,
Block 1 (once the user has picked/mixed an alternative), Block 2, and the
Completeness Summary have all been drafted per the skill's own format specs.

That HTML is sent to Google Docs as the document body, so **the markup
written here is the source of truth for how the Doc looks.** The converter
renders what the markup encodes and nothing more.

**This file governs layout only — never content.** Every element name,
conclusion, description, pattern name, and modification note must reach the
finished Doc with the exact wording produced during blueprinting. Nothing
here justifies shortening, merging, or rewording anything to make it fit a
template.

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
| `<table>` `<tr>` `<th>` `<td>` — a real Doc table | Text color — no `foregroundColor` equivalent survives |
| `<p>` — a paragraph | Precise column widths — see the Block 1 note below |

**CSS does not survive the conversion.** Do not write a single `style`
attribute. There is no color equivalent in this pipeline, so the Palette
guidance from earlier versions of this file (navy headings, amber
WOW‑MOMENT titles, gray field labels and dividers) does not apply here —
headings, dividers, and field labels are unstyled `<h1>`/`<h2>`/`<h3>`,
`<hr>`, and `<strong>` only. Spacing is created structurally, with the
spacer paragraph below, and by no other means.

**Tables convert, but column widths are best‑effort.** A real `<table>`
element becomes a real Doc table — that part is reliable. What the earlier
Docs‑API version got from `updateTableColumnProperties` (exact,
enforced‑to‑the‑point column widths) has no equivalent here: there is no
style attribute to carry a width, and an HTML `width` attribute on `<col>`
or `<td>` is only ever a hint the converter may or may not honor. Set it
anyway on the header row's cells as the best available signal (see the
Block 1 template), but do not treat the resulting widths as guaranteed —
this is a real limitation of the HTML pipeline relative to the Docs‑API
pass, not something to paper over.

---

## Standing rule: the spacer paragraph, and no title ever shares a paragraph with its content

Google Docs renders consecutive `<p>` elements with **no gap between them**.
Whitespace in the source HTML changes nothing — the converter ignores it.

The only way to create a visible blank line is to emit a paragraph that holds
a non-breaking space:

```html
<p>&nbsp;</p>
```

This is the single spacing mechanism in this document. **Put one between
every pair of blocks.** The original defect in this skill's output was every
`N —` section title running directly into its `Conclusion:` line, and every
`N.X —` sub-section title running directly into its description, inside a
single paragraph. That is the one failure this file exists to prevent:
**a title is always its own paragraph, followed by a spacer, followed by its
content as a separate paragraph.**

**Wrong** — title and content share a paragraph:

```html
<p><strong>2.1 — What Does Personalization Actually Promise?</strong> The
section introduces the gap between the promise of tailored experience and
what most products actually deliver.</p>
```

**Right** — title, spacer, content, spacer:

```html
<p><strong>2.1 — What Does Personalization Actually Promise?</strong></p>
<p>&nbsp;</p>
<p>The section introduces the gap between the promise of tailored
experience and what most products actually deliver.</p>
<p>&nbsp;</p>
```

Same wording, same order. The spacer and the paragraph break are the entire
difference between the two renders.

**On heading depth: `N —` section titles get `<h3>`; `N.X —` sub-section
titles do not get a heading at all.** The converter only turns `<h1>`–`<h3>`
into real Doc heading styles (see table above), so unlike an earlier,
Docs‑API‑driven version of this file — which had `HEADING_3` for section
titles and `HEADING_4` for sub-section titles — there is no heading level
left for the sub-section tier. Sub-section titles stay `<strong>` inside
their own `<p>`, exactly as Theme and Technical Concept titles do in the
Broad Research and Research Analysis skills, and for the same reason:
promoting every sub-section title to a real heading would flood the Doc's
outline pane with 10-20+ entries and make it useless for navigation. The
title-then-spacer-then-content structure above — not a heading level — is
what keeps sub-sections from running together.

**On the WOW MOMENT tag: the bracketed text carries the distinction, not
color.** The earlier Docs‑API version colored `[WOW MOMENT]` sub-section
titles amber so they visually jumped out. There is no color in this
pipeline, so that distinction now rests entirely on the `[WOW MOMENT]` text
itself staying intact and bolded like every other sub-section title — do
not compensate by adding emphasis this file doesn't specify (no all-caps,
no extra asterisks, no inserted exclamation marks). The label is doing the
work that color used to do.

---

## 1. Document title

```html
<h1>{Chapter Topic} &mdash; Chapter Blueprint</h1>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

---

## 2. Block 0 — Chapter Foundation

Plain labeled text, never a table — six short labels against six long,
multi-sentence definitions reads as cramped and top-heavy in a table.

```html
<h2>Block 0 &mdash; Chapter Foundation</h2>
<p>&nbsp;</p>
<p><strong>Chapter Purpose</strong></p>
<p>&nbsp;</p>
<p>{Definition.}</p>
<p>&nbsp;</p>
<p><strong>Core Argument</strong></p>
<p>&nbsp;</p>
<p>{Definition.}</p>
<p>&nbsp;</p>
<p><strong>Reader Transformation</strong></p>
<p>&nbsp;</p>
<p>{Before → After definition.}</p>
<p>&nbsp;</p>
<p><strong>Primary Tension</strong></p>
<p>&nbsp;</p>
<p>{Definition.}</p>
<p>&nbsp;</p>
<p><strong>Main Counterargument</strong></p>
<p>&nbsp;</p>
<p>{Definition.}</p>
<p>&nbsp;</p>
<p><strong>Chapter Promise</strong></p>
<p>&nbsp;</p>
<p>{Definition.}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Each of the six elements is title-paragraph, spacer, definition-paragraph,
spacer — never title and definition sharing a line.

---

## 3. Block 1 — Structural Alternatives

Each option's name and one-line reader's-journey sentence are paragraphs;
the skeleton is a real `<table>`.

```html
<h2>Block 1 &mdash; Structural Alternatives</h2>
<p>&nbsp;</p>
<h3>Option A &mdash; {Name / Angle in 3&ndash;5 words}</h3>
<p>&nbsp;</p>
<p><strong>{Pattern X (&hellip;)} &mdash; modified.</strong> {The rest of the
pattern/modification paragraph.}</p>
<p>&nbsp;</p>
<p>{The reader's-journey sentence.}</p>
<p>&nbsp;</p>
<table>
<tr>
<th width="5%">#</th>
<th width="18%">Section</th>
<th width="19%">Core Idea or Concept</th>
<th width="29%">What It's About</th>
<th width="29%">What is the Conclusion</th>
</tr>
<tr>
<td>1</td>
<td><strong>{Section name}</strong></td>
<td>{Unique 2&ndash;7 word label specific to this section's logic}</td>
<td>{What this section does &mdash; one clause}</td>
<td>{The specific conclusion for this chapter topic}</td>
</tr>
<tr>
<td>2</td>
<td><strong>{Section name}</strong></td>
<td>{&hellip;}</td>
<td>{&hellip;}</td>
<td>{&hellip;}</td>
</tr>
<tr>
<td>3</td>
<td><strong>[TECH] {Section name}</strong></td>
<td>{&hellip;}</td>
<td>{&hellip;}</td>
<td>{&hellip;}</td>
</tr>
<tr>
<td>{N}</td>
<td><strong>{Section name}</strong></td>
<td>{&hellip;}</td>
<td>{&hellip;}</td>
<td>{&hellip;}</td>
</tr>
</table>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Repeat the full block (`<h3>` title, pattern paragraph, journey paragraph,
table, spacer, `<hr>`) for Options B and C.

Rules for this block:

- **The header row uses `<th>`, not `<td>`** — that alone is what makes it
  read as a header once color/shading (unavailable here) is off the table.
  Bold the `Section` column's cell text on every data row too, matching the
  earlier spec's intent to keep section names visually prominent.
- The `width` attributes on the header cells are the best-effort signal
  described above — set them to the same proportions the Docs‑API version
  used (5/18/19/29/29), but do not depend on them landing exactly.
- One table per option; a real `<hr>` divider (with spacers on both sides)
  between options, never just blank space.
- After all three options are rendered, close with the hand-off line as a
  plain paragraph:

```html
<p>Pick an option, mix elements from two, or tell me what to change &mdash;
then I will expand it fully in Block 2.</p>
<p>&nbsp;</p>
```

This HTML/table rendering only happens once — Block 1 itself is presented to
the user in chat to choose from (see the skill's own gate behavior); render
and deliver the Doc after Block 2 is complete, with Block 1's chosen/mixed
version included as a record of what was decided.

---

## 4. Block 2 — Full Expansion

Each full section is its own visually separated group: a heading, its
conclusion, then two or more sub-sections.

```html
<h2>Block 2 &mdash; Full Expansion</h2>
<p>&nbsp;</p>
<h3>{N} &mdash; {SECTION NAME}</h3>
<p>&nbsp;</p>
<p><em>{One line &mdash; what is the conclusion for this section.}</em></p>
<p>&nbsp;</p>
<p><strong>{N}.1 &mdash; {Sub-section name, phrased as a question, &le;5&ndash;6 words}</strong></p>
<p>&nbsp;</p>
<p>{1-2 line description of what this sub-section covers conceptually.}</p>
<p>&nbsp;</p>
<p><strong>{N}.2 &mdash; {Sub-section name, phrased as a question, &le;5&ndash;6 words}</strong></p>
<p>&nbsp;</p>
<p>{1-2 line description.}</p>
<p>&nbsp;</p>
<p><strong>{N}.X &mdash; [WOW MOMENT] {Sub-section name, phrased as a question, &le;5&ndash;6 words}</strong></p>
<p>&nbsp;</p>
<p>{Description of what the surprising, sourced finding demonstrates
conceptually &mdash; never the finding itself.}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- **A spacer after the section title, after the conclusion, after every
  sub-section title, and after every sub-section description.** A section
  with fewer is wrong — this is the specific defect (title running into
  conclusion, sub-section title running into description) this file exists
  to fix.
- The section's conclusion line is italic; sub-section descriptions are
  plain text.
- Every section needs at least two sub-sections, in order, each following
  the same title/spacer/description shape.
- `<hr>` separates full sections, replacing the typed `═══════` divider row
  — never leave a typed `═══` or `━━━` row in the output text; it renders as
  a wrapped, glitchy-looking line, not a deliberate separator.
- Do not add a divider between sub-sections within the same section — only
  the spacer paragraphs, and the section boundary itself gets the `<hr>`.

---

## 5. Completeness Summary

The recurring failure point across every skill in this pipeline — do not
leave it as one paragraph. Every field is its own bold-labeled paragraph,
with a spacer after each:

```html
<h2>Completeness Summary</h2>
<p>&nbsp;</p>
<p><strong>Sections:</strong> {N}</p>
<p>&nbsp;</p>
<p><strong>Sub-sections per section:</strong> {counts}</p>
<p>&nbsp;</p>
<p><strong>WOW MOMENT present:</strong> {yes &mdash; section N.X / no}</p>
<p>&nbsp;</p>
<p><strong>[TECH] section present:</strong> {yes / no}</p>
<p>&nbsp;</p>
<p><strong>Anti-redundancy check:</strong> {pass &mdash; no issues / issues found and fixed: &hellip;}</p>
<p>&nbsp;</p>
<p><strong>Evidence-free check:</strong> {pass &mdash; no citations/products/case studies present / issues found}</p>
<p>&nbsp;</p>
```

Count the fields before finishing: there must be exactly six field
paragraphs, one per field. Two labels sharing a paragraph is the defect that
made this section unreadable in earlier drafts.

---

## 6. General

**Document skeleton.** The blueprint opens with the title, then runs Block
0, Block 1 (the chosen/mixed alternative, as decided in chat), Block 2, and
the Completeness Summary, in that order:

```html
<h1>{Chapter Topic} &mdash; Chapter Blueprint</h1>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<h2>Block 0 &mdash; Chapter Foundation</h2>
<p>&nbsp;</p>
...
```

**Heading levels.** Headings become the Doc's real Heading styles, which is
what makes the outline pane work:

| Tag | Used for |
|---|---|
| `<h1>` | The document title, carrying the chapter topic |
| `<h2>` | `Block 0`, `Block 1`, `Block 2`, and `Completeness Summary` |
| `<h3>` | Each Option (`Option A/B/C`) inside Block 1, and each `N —` section title inside Block 2 |
| `<strong>` | Sub-section (`N.X —`) titles, field labels, and pattern lead-ins — body text, not headings |

Sub-section titles stay `<strong>` inside a `<p>` on purpose: promoting each
one to a heading would flood the Doc's outline pane and make it useless for
navigation — see the spacer-paragraph rule above.

**No escaped block/section numbers.** Write `<h2>Block 1 &mdash; Structural
Alternatives</h2>` and `<h3>2 &mdash; What Does Personalization Promise?</h3>`,
not an escaped or backslashed form.

**Escape HTML special characters in content.** `&` becomes `&amp;`. `<`
becomes `&lt;` and `>` becomes `&gt;`. Em dashes are written `&mdash;`, en
dashes (in ranges like "5–8 sections") `&ndash;`, and ellipses `&hellip;`.

**Never emit an empty heading, an empty table row, or a table with only a
header row.** Every `<tr>` in a Block 1 skeleton must carry real section
data — if a skeleton genuinely has only, say, five sections, emit five data
rows and stop; never pad with placeholder rows.

**No CSS, anywhere.** No `style` attributes, no `<style>` blocks, no
`class`, and no color. They are stripped in conversion and their presence
gives a false impression that spacing, shading, or the WOW‑MOMENT
distinction is handled by something other than the markup and the text
itself. `<p>&nbsp;</p>` is the only spacing mechanism, and
`<strong>`/`<em>` are the only emphasis mechanisms.

**Verify before delivering.** Re-read the generated HTML and confirm:

1. No section or sub-section title shares a paragraph with its
   conclusion/description anywhere in Block 2.
2. Every `N —` section title is a real `<h3>`; no sub-section title is a
   heading of any level — all stay `<strong>` inside their own `<p>`.
3. Every `[WOW MOMENT]` sub-section title has the bracketed tag intact and
   bolded, since no color is available to distinguish it.
4. Block 0 is plain labeled text, not a table; each of Block 1's three
   skeletons is a real `<table>` with a `<th>` header row, not evenly
   auto-split cells rendered as plain text.
5. No typed `═══` or `━━━` divider rows remain in the Doc text — these
   should all be real `<hr>` dividers or spacer paragraphs by this point.
6. The Completeness Summary has exactly six field paragraphs, one per
   field.
7. Not one `style`, `class`, `<style>`, or color attribute appears in the
   output, and no literal Markdown characters (`#`, `**`, `-`, `---`)
   survive anywhere in the Doc text.
