# Output Formatting Rules — Broad Research Brief (HTML)

Applies to the HTML produced by the Broad Research skill, after the brief's
content (Sections 1–3) has been fully researched and drafted per the skill's
Research and Output-Format steps. The brief ends after Section 3 — nothing
follows the last rung.

That HTML is sent to Google Docs as the document body, so **the markup written
here is the source of truth for how the Doc looks.** The converter renders what
the markup encodes and nothing more.

**This file governs layout only — never content.** Every finding,
claim, description, label, and URL must appear with the exact wording
produced during research. Nothing here justifies shortening, merging,
or rewording a finding to make it fit a template.

Every block below is given as a template. **Emit the markup exactly**, including
every spacer paragraph. Replace only the `{placeholders}`.

---

## What the converter supports

This has been tested against the actual Google Docs conversion. Build only with
what is on the left column.

| Works | Does not work |
|---|---|
| `<h1>` `<h2>` `<h3>` — become real Doc heading styles | **`style="..."` attributes — silently stripped** |
| `<strong>` — bold | `<style>` blocks — ignored |
| `<em>` — italic | Any CSS margin, padding or spacing |
| `<a href="...">` — clickable hyperlink | `class=` — no stylesheet exists |
| `<hr>` — horizontal divider | Blank lines in the source — collapse to nothing |
| `<ul>` `<ol>` `<li>` — real Doc lists | Indentation in the source — ignored |
| `<p>` — a paragraph | |

**CSS does not survive the conversion.** Do not write a single `style` attribute.
Spacing is created structurally, with the spacer paragraph below, and by no
other means.

---

## Standing rule: the spacer paragraph

Google Docs renders consecutive `<p>` elements with **no gap between them**.
Whitespace in the source HTML changes nothing — the converter ignores it.

The only way to create a visible blank line is to emit a paragraph that holds a
non-breaking space:

```html
<p>&nbsp;</p>
```

This is the single spacing mechanism in this document. **Put one between every
pair of blocks.** A finding whose title, metadata, summary, card fields and
link are emitted as consecutive `<p>` elements with no spacers between them
renders as a dense, unreadable stack — that is the one failure this file exists
to prevent.

**Wrong** — no spacers, so every line stacks tight:

```html
<p><strong>{ID} &mdash; {Title}</strong></p>
<p>SOURCE TYPE: {…} | AUTHORITY: {…} | FRESHNESS: {…} | USE: {…}</p>
<p>{Summary.}</p>
<p><strong>CLAIM:</strong> {…}</p>
<p><strong>WHY IT MATTERS:</strong> {…}</p>
<p><strong>CONFIDENCE:</strong> {…}</p>
<p><a href="{URL}">{URL}</a></p>
```

**Right** — a spacer between every part:

```html
<p><strong>{ID} &mdash; {Title}</strong></p>
<p>&nbsp;</p>
<p>SOURCE TYPE: {…} | AUTHORITY: {…} | FRESHNESS: {…} | USE: {…}</p>
<p>&nbsp;</p>
<p>{Summary.}</p>
<p>&nbsp;</p>
<p><strong>CLAIM:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>WHY IT MATTERS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>CONFIDENCE:</strong> {…}</p>
<p>&nbsp;</p>
<p><a href="{URL}">{URL}</a></p>
```

Same markup, same order. The spacers are the entire difference between the two
renders.

---

## 1. Source Ladder Findings (Section 3)

Each finding is its own visually separated group, with its source quality
labels and its evidence card merged in:

```html
<h2>3. Source Ladder Findings</h2>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<h3>Rung {N} &mdash; {Rung Name}</h3>
<p>&nbsp;</p>
<p><strong>{ID} &mdash; {Title}</strong></p>
<p>&nbsp;</p>
<p>SOURCE TYPE: {…} | AUTHORITY: {…} | FRESHNESS: {…} | USE: {…}</p>
<p>&nbsp;</p>
<p>{The finding's summary, as one paragraph.}</p>
<p>&nbsp;</p>
<p><strong>CLAIM:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>WHY IT MATTERS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>CONFIDENCE:</strong> {…}</p>
<p>&nbsp;</p>
<p><a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<p><strong>{ID} &mdash; {Title}</strong></p>
<p>&nbsp;</p>
<p>SOURCE TYPE: {…} | AUTHORITY: {…} | FRESHNESS: {…} | USE: {…}</p>
<p>&nbsp;</p>
<p>{Summary.}</p>
<p>&nbsp;</p>
<p><strong>CLAIM:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>WHY IT MATTERS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>CONFIDENCE:</strong> {…}</p>
<p>&nbsp;</p>
<p><a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- **Seven spacers per finding** — after the title, after the metadata line,
  after the summary, after each of the three card fields, and after the link.
  A finding with fewer is wrong.
- **Fixed order, every finding:** title → metadata line → summary → `CLAIM` →
  `WHY IT MATTERS` → `CONFIDENCE` → link.
- The four metadata fields sit on **one line** inside one `<p>`, separated by
  ` | `, in this fixed order, with the label names exactly as written
  (`SOURCE TYPE`, `AUTHORITY`, `FRESHNESS`, `USE`) and **not bolded**. The
  values come from the research step; this file does not define them.
- The three card labels keep their all-caps wording (`CLAIM`,
  `WHY IT MATTERS`, `CONFIDENCE`), each wrapped in `<strong>`, **each starting
  its own paragraph.** Putting two card labels in one `<p>` is the most common
  defect in this block.
- There is no `SOURCE:` card field. The finding's link paragraph is its source.
- **The link text is the URL itself.** Write `<a href="{URL}">{URL}</a>` — the
  same address in both places. Never substitute a publication name, a date, or
  a title for the link text.
- `<hr>` separates findings, with a spacer before and after it.
- A finding with more than one source gets each link in its own `<p>`, with a
  spacer between them.
- A finding added by the Blind Spot Check is an ordinary finding in its rung —
  same block, no marker.

Where a rung falls below its minimum, the explanatory note is **a paragraph
under the last finding of that rung**, never a heading:

```html
<p>Note: {the reason this rung contains fewer findings than its target.}</p>
<p>&nbsp;</p>
```

A rung that was skipped entirely keeps its heading, with the note directly
under it:

```html
<h3>Rung {N} &mdash; {Rung Name}</h3>
<p>&nbsp;</p>
<p>Note: {the reason this rung was skipped.}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

**Never put two findings in one paragraph.** If the raw research output
concatenated two entries, split them into their own blocks — including
cross-reference-only entries, which get a title and the cross-reference, with
no metadata line and no card fields:

```html
<p><strong>{ID} &mdash; {Title}</strong></p>
<p>&nbsp;</p>
<p>(see {Other ID})</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

---

## 2. Query Map (Section 2)

The Query Map has exactly seven fields. Every label is bold, every field is its
own paragraph, with a spacer between each:

```html
<h2>2. Query Map</h2>
<p>&nbsp;</p>
<p><strong>PRIMARY TERM:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>SYNONYMS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>TECHNICAL TERMS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>PRODUCT TERMS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>BUSINESS TERMS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>ETHICS TERMS:</strong> {…}</p>
<p>&nbsp;</p>
<p><strong>CONTRARIAN TERMS:</strong> {…}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Count the paragraphs before moving on: there must be exactly seven field
paragraphs, one per field. Two labels in one `<p>` is a defect.

---

## 3. General

**Document skeleton.** The brief opens with the title carrying the topic, a
metadata paragraph, and a divider, then runs the three numbered sections in
order:

```html
<h1>Broad Research Brief: {Topic}</h1>
<p>&nbsp;</p>
<p><strong>Version:</strong> {…} <strong>Skill:</strong> {…} <strong>Topic:</strong> {…}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<h2>1. Research Objective</h2>
<p>&nbsp;</p>
<p>{…}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Section 2 (Query Map) follows, then Section 3 (Source Ladder Findings). The
document ends with the closing `<hr>` and spacer of the last finding (or rung
note) in Section 3. **No section, summary or heading comes after it.**

**Heading levels.** Headings become the Doc's real Heading styles, which is what
makes the outline pane work:

| Tag | Used for |
|---|---|
| `<h1>` | The document title, carrying the topic |
| `<h2>` | The numbered sections 1 through 3 |
| `<h3>` | Rung subheadings inside Section 3 |
| `<strong>` | Finding titles, card field labels, Query Map field labels — body text, not headings |

Finding titles stay `<strong>` inside a `<p>` on purpose: promoting them to
headings floods the Doc's outline pane and makes it useless for navigation.

**No escaped section numbers.** Write `<h2>1. Research Objective</h2>`. The
backslash escape needed in the markdown version is not needed here and would
render as a visible character.

**Escape HTML special characters in content.** `&` becomes `&amp;` — this
matters in every rung name containing an ampersand, such as
`Consulting &amp; Analyst`. `<` becomes `&lt;` and `>` becomes `&gt;`. Em
dashes are written `&mdash;`.

**Never emit an empty heading.** A heading with no text renders as blank space
and shows in the outline pane as an empty entry.

**Hyperlinks.** Every URL is `<a href="{URL}">{URL}</a>`, the address in both
places. Never leave a bare URL as plain text, and never replace the link text
with a name or title.

**No CSS, anywhere.** No `style` attributes, no `<style>` blocks, no `class`.
They are stripped in conversion and their presence gives a false impression that
spacing is handled. `<p>&nbsp;</p>` is the only spacing mechanism.

**Verify before delivering.** Re-read the generated HTML and confirm:

1. Every finding has a `<p>&nbsp;</p>` after its title, after its metadata
   paragraph, after its summary, after each of its three card fields, and after
   its link.
2. Every finding runs in the fixed order: title, metadata, summary, `CLAIM`,
   `WHY IT MATTERS`, `CONFIDENCE`, link.
3. Every card label is bold, all-caps, and starts its own paragraph; no finding
   has a `SOURCE:` card field.
4. No two findings share a paragraph.
5. An `<hr>` sits between every pair of findings and sections, with a spacer
   before and after it.
6. Every link is `<a href="{URL}">{URL}</a>`, with no bare URLs anywhere.
7. The Query Map is exactly seven field paragraphs.
8. Every rung below its minimum, or skipped, has a `Note:` paragraph.
9. Nothing follows Section 3 — no Source Quality Labels, Blind Spot, Evidence
   Cards, synthesis or summary section.
10. Not one `style`, `class`, or `<style>` appears in the output.
11. Every `&` in body text is written `&amp;`.
12. No empty `<li>` and no empty heading survives.
13. Rung notes and other explanatory text are paragraphs, not headings.
