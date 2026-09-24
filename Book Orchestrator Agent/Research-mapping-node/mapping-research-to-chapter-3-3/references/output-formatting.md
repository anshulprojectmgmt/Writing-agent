# Output Formatting Rules — Final Chapter Blueprint (HTML)

Applies to the HTML produced by the Research Mapping skill, after the Final
Chapter Blueprint (every section, sub-section, evidence block, GAP flag, and
creative-beat marker) and the Coverage Summary have been fully drafted per
the skill's own Output Format spec.

That HTML is sent to Google Docs as the document body, so **the markup
written here is the source of truth for how the Doc looks.** The converter
renders what the markup encodes and nothing more.

**This file governs layout only — never content.** Every content bullet
copied from the blueprint, every evidence point, every "how it serves"
explanation, every fit label, every GAP description, and every source URL
must reach the finished Doc with the exact wording produced during mapping.
Nothing here justifies shortening, merging, re-ranking, or rewording
anything to make it fit a template — least of all an evidence point, which
the skill's own rules require to be written out in full.

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
| `<p>` — a paragraph | `<blockquote>` — no reliable indent or rule survives |
| Emoji as literal characters (⚠️ ✅ 🎨 🔗) | Precise column widths — see the Coverage Summary note |

**CSS does not survive the conversion.** Do not write a single `style`
attribute. There is no color in this pipeline, so a HIGH fit, a MED fit, a
GAP, and a creative beat cannot be distinguished by shading or ink — the
distinction rests entirely on the label text and the emoji staying intact.
Spacing is created structurally, with the spacer paragraph below, and by no
other means.

**Tables convert, but column widths are best-effort.** A real `<table>`
element becomes a real Doc table — that part is reliable. There is no style
attribute to carry a width, and an HTML `width` attribute on a header cell
is only ever a hint the converter may or may not honor. Set it anyway on the
header row as the best available signal (see the Coverage Summary
templates), but do not treat the resulting widths as guaranteed.

**`<blockquote>` is not in the supported set.** The skill's own output spec
writes GAPs, the "GAP: none" line, creative-beat markers, the punch line,
and the chapter-level feedback as Markdown blockquotes (`>`). Those are a
chat-draft convention, not a delivery format. In the Doc they become
**bold-labeled paragraphs** per the templates below. Never emit a literal
`>` character at the start of a paragraph — it renders as a stray angle
bracket, not a quote.

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
every pair of blocks.** The failure this file exists to prevent is specific
to this skill: a sub-section title running into its purpose line, a content
bullet list running straight into the first `Evidence —` title, and an
evidence block running into the GAP flag beneath it — so that a reader
scanning the Doc cannot tell where the blueprint's own ideas end and the
mapped evidence begins.

**Wrong** — title, purpose, and evidence title stacked with no spacers:

```html
<p><strong>2.1 &mdash; What Does Personalization Promise?</strong>
<em>Sets up the gap between promise and delivery.</em></p>
<p><strong>Evidence &mdash; "Spotify Wrapped"</strong> <em>(Fit: HIGH)</em></p>
```

**Right** — every part its own paragraph, spacer after each:

```html
<p><strong>2.1 &mdash; What Does Personalization Promise?</strong></p>
<p>&nbsp;</p>
<p><em>Sets up the gap between promise and delivery.</em></p>
<p>&nbsp;</p>
<p><strong>Evidence &mdash; "Spotify Wrapped"</strong> <em>(Fit: HIGH)</em></p>
<p>&nbsp;</p>
```

Same wording, same order. The spacers and the paragraph breaks are the
entire difference between the two renders.

**On heading depth: `N —` section titles get `<h3>`; `N.X —` sub-section
titles do not get a heading at all.** The converter only turns `<h1>`–`<h3>`
into real Doc heading styles (see table above), so there is no heading level
left for the sub-section tier. Sub-section titles stay `<strong>` inside
their own `<p>`, exactly as they do in the Chapter Blueprint skill this
document extends, and as Theme and Concept titles do in the Broad Research
and Research Analysis skills — promoting 10–20+ sub-sections to real
headings would flood the Doc's outline pane and make it useless for
navigation. Evidence titles stay `<strong>` for the same reason, one tier
further down again.

---

## 1. Document title

```html
<h1>{Chapter Title} &mdash; Final Chapter Blueprint</h1>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

The typed `━━━━━` rule rows in the skill's own output spec are a chat
convention — they become real `<hr>` dividers here and never survive as
typed characters.

---

## 2. Section

Each section is a heading, its purpose line, then its sub-sections.

```html
<h3>{N} &mdash; {SECTION NAME}</h3>
<p>&nbsp;</p>
<p><em>Purpose: {one clause, from the blueprint, unchanged}.</em></p>
<p>&nbsp;</p>
```

Rules for this block:

- The purpose line is italic and is always its own paragraph, never appended
  to the section title.
- `<hr>` separates full sections, with a spacer on both sides. Do not put an
  `<hr>` between sub-sections inside the same section — the spacer
  paragraphs do that work.

---

## 3. Sub-section with evidence

The core repeating unit of this document. A sub-section title, its italic
"what it does" line, its content bullets as a real list, then one evidence
block per assigned item, then its GAP line.

```html
<p><strong>{N}.{X} &mdash; {SUB-SECTION NAME}</strong></p>
<p>&nbsp;</p>
<p><em>{What it does &mdash; from the blueprint.}</em></p>
<p>&nbsp;</p>
<ul>
<li>{Content bullet, copied from the blueprint unchanged.}</li>
<li>{Content bullet, copied from the blueprint unchanged.}</li>
<li>{Content bullet, copied from the blueprint unchanged.}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Evidence &mdash; "{Item Name}"</strong> <em>(Fit: HIGH)</em></p>
<p>&nbsp;</p>
<ul>
<li>{Point 1, written out in full.} &rarr; <em>How it serves:</em> {one-line explanation specific to this point}</li>
<li>{Point 2, if this item has more than one usable point here.} &rarr; <em>How it serves:</em> {explanation specific to this point}</li>
</ul>
<p>&nbsp;</p>
<p>🔗 <strong>Source:</strong> <a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<p><strong>Evidence &mdash; "{Item Name 2}"</strong> <em>(Fit: MED)</em></p>
<p>&nbsp;</p>
<ul>
<li>{Point, written out in full.} &rarr; <em>How it serves:</em> {explanation}</li>
</ul>
<p>&nbsp;</p>
<p>🔗 <strong>Source:</strong> <a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<p><strong>⚠️ GAP:</strong> {Specific description of what evidence type is missing} &mdash; <em>for deep-research</em></p>
<p>&nbsp;</p>
```

Rules for this block:

- **A spacer after the sub-section title, after the "what it does" line,
  after the content-bullet `<ul>`, after every evidence title, after every
  point list, and after every Source line.** A sub-section with fewer is
  wrong — this is the defect this file exists to fix.
- **No spacer between `<li>` items** inside a list. The list is one block;
  the spacer goes after the closing `</ul>`.
- Content bullets are a real `<ul>`, never `•` characters typed into a
  paragraph. The `•` in the skill's own spec is a chat convention.
- The fit label stays exactly as scored — `<em>(Fit: HIGH)</em>` or
  `<em>(Fit: MED)</em>`, on the same line as the evidence title, in
  parentheses, italic. LOW items are never assigned, so `Fit: LOW` must
  never appear.
- Evidence points are real `<li>` items, each carrying its own
  `How it serves` clause after a `&rarr;`. One `How it serves` covering two
  points is a content error, not a formatting shortcut.
- The Source line is its own paragraph, closing each evidence block, with
  the 🔗 kept as a literal character and the URL as a real hyperlink.
- A sub-section with more than one assigned item repeats the whole evidence
  block — title, spacer, point list, spacer, Source, spacer — once per item.

---

## 4. GAP, no-GAP, and creative-beat lines

These three are the skill's Markdown blockquotes. All three become
bold-labeled paragraphs, each with its own spacer. The emoji is a literal
character and carries the distinction that color would otherwise carry — it
must survive intact.

**A real GAP:**

```html
<p><strong>⚠️ GAP:</strong> {Specific description of what evidence type is missing} &mdash; <em>for deep-research</em></p>
<p>&nbsp;</p>
```

**No GAP:**

```html
<p><strong>✅ GAP: none</strong></p>
<p>&nbsp;</p>
```

**Creative beat** — the sub-section title carries the parenthetical, and the
marker replaces the evidence block entirely:

```html
<p><strong>{N}.{X} &mdash; {SUB-SECTION NAME}</strong> <em>(Creative beat &mdash; analogy / humor / author framework)</em></p>
<p>&nbsp;</p>
<p><em>{What it does.}</em></p>
<p>&nbsp;</p>
<ul>
<li>{Content bullet.}</li>
</ul>
<p>&nbsp;</p>
<p><strong>🎨 EVIDENCE: none</strong> &mdash; creative beat, no source required</p>
<p>&nbsp;</p>
```

Rules for this block:

- Every sub-section closes with exactly one of these three lines, or with an
  evidence block followed by one of them. Nothing is left blank — that is a
  rule of the skill, and the formatting pass must not quietly drop a line
  that was drafted.
- A GAP description that says only "no evidence" is a content failure the
  skill's own Step 4 forbids. Do not emit it, and do not pad it here — send
  it back to be written properly.
- Never emit a literal `>` at the start of these paragraphs.

---

## 5. Punch line and chapter-level feedback

```html
<h2>Punch Line</h2>
<p>&nbsp;</p>
<p><em>"{Punch line, from the blueprint, unchanged.}"</em></p>
<p>&nbsp;</p>
<h2>Chapter-Level Feedback</h2>
<p>&nbsp;</p>
<p><em>"{Single chapter-level comment, from the blueprint, unchanged.}"</em></p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Both are quoted lines carried over verbatim from the blueprint — they stay
italic and inside quotation marks. The HTML comment marker
(`<!-- CHAPTER-LEVEL FEEDBACK -->`) in the skill's own spec is a drafting
annotation: emit the `<h2>` heading instead, never the comment.

---

## 6. Coverage Summary

Three real tables, each under its own `<h3>`, all inside one `<h2>`. This is
the section a reader scans to decide what goes to deep-research, so the
tables must be real tables, not tab-aligned text.

```html
<h2>Coverage Summary</h2>
<p>&nbsp;</p>
<h3>Metrics</h3>
<p>&nbsp;</p>
<table>
<tr>
<th width="70%">Category</th>
<th width="30%">Count</th>
</tr>
<tr><td>Total sub-sections</td><td>{N}</td></tr>
<tr><td>Fully evidenced (HIGH fit)</td><td>{N}</td></tr>
<tr><td>Partial (MED fit only)</td><td>{N}</td></tr>
<tr><td>Creative beats (no source)</td><td>{N}</td></tr>
<tr><td>GAPs for deep-research</td><td>{N}</td></tr>
</table>
<p>&nbsp;</p>
<h3>GAPs</h3>
<p>&nbsp;</p>
<table>
<tr>
<th width="35%">Sub-section</th>
<th width="65%">What's Missing</th>
</tr>
<tr>
<td><strong>{N}.{X} &mdash; {Sub-section name}</strong></td>
<td>{One-line description of the missing evidence type.}</td>
</tr>
</table>
<p>&nbsp;</p>
<h3>Unplaced Items</h3>
<p>&nbsp;</p>
<table>
<tr>
<th width="35%">Item</th>
<th width="65%">Reason Excluded</th>
</tr>
<tr>
<td><strong>"{Item name}"</strong></td>
<td>{Why it did not fit anywhere.}</td>
</tr>
</table>
<p>&nbsp;</p>
<p>The unplaced items list tells the user what the research covered that did
not make it into the chapter. They can decide whether to add a sub-section,
swap an existing item, or let it go.</p>
<p>&nbsp;</p>
```

Rules for this block:

- **The header row uses `<th>`, not `<td>`** — that alone is what makes it
  read as a header once shading (unavailable here) is off the table.
- The five Metrics rows are fixed: emit all five, in that order, even when a
  count is `0`. A missing row reads as an oversight, not a zero.
- The GAPs table carries one row per GAP flagged in the blueprint, and the
  counts in Metrics must agree with the rows below them. If there are no
  GAPs, emit the table with a single row reading `None` and
  `All sub-sections evidenced or marked as creative beats` — never a
  header-only table.
- Same for Unplaced Items: one row per item, or a single `None` row.
- The closing explanatory paragraph stays — it tells the reader what the
  third table is for.

---

## 7. General

**Document skeleton.** The document opens with the title, then runs the
sections in blueprint order, then the punch line, the chapter-level
feedback, and the Coverage Summary:

```html
<h1>{Chapter Title} &mdash; Final Chapter Blueprint</h1>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<h3>1 &mdash; {SECTION NAME}</h3>
<p>&nbsp;</p>
...
<h2>Punch Line</h2>
<p>&nbsp;</p>
...
<h2>Coverage Summary</h2>
<p>&nbsp;</p>
...
```

**Heading levels.** Headings become the Doc's real Heading styles, which is
what makes the outline pane work:

| Tag | Used for |
|---|---|
| `<h1>` | The document title, carrying the chapter title |
| `<h2>` | `Punch Line`, `Chapter-Level Feedback`, and `Coverage Summary` |
| `<h3>` | Each `N —` section title, and the three Coverage Summary table titles |
| `<strong>` | Sub-section (`N.X —`) titles, `Evidence — "…"` titles, GAP / no-GAP / creative-beat labels, and `Source` labels — body text, not headings |

Sub-section and evidence titles stay `<strong>` inside a `<p>` on purpose:
promoting them to headings would flood the Doc's outline pane and make it
useless for navigation — see the spacer-paragraph rule above.

**No escaped section numbers.** Write `<h3>2 &mdash; Why Does Personalization
Stall?</h3>`, not an escaped or backslashed form.

**Escape HTML special characters in content.** `&` becomes `&amp;`. `<`
becomes `&lt;` and `>` becomes `&gt;`. Em dashes are written `&mdash;`, en
dashes `&ndash;`, ellipses `&hellip;`, and the "how it serves" arrow
`&rarr;`. The emoji (⚠️ ✅ 🎨 🔗) are literal characters and are not escaped.

**Hyperlinks.** Every evidence block's Source is a real URL, written
`<a href="{URL}">{URL}</a>` — the address in both places. Never leave a bare
URL as plain text, and never replace the link text with a publication name
or article title. A source that broad-research gave as a short in-text
citation with no URL stays plain text — do not invent a link.

**Never emit an empty heading, an empty table row, or a table with only a
header row.** A section with no sub-sections, an evidence block with no
points, or a Coverage Summary table with a header and nothing under it all
mean something was dropped between drafting and rendering.

**No CSS, anywhere.** No `style` attributes, no `<style>` blocks, no
`class`, and no color. They are stripped in conversion and their presence
gives a false impression that spacing, shading, or the HIGH/MED and GAP
distinctions are handled by something other than the markup and the label
text itself. `<p>&nbsp;</p>` is the only spacing mechanism, and
`<strong>`/`<em>` are the only emphasis mechanisms.

**Verify before delivering.** Re-read the generated HTML and confirm:

1. No sub-section title shares a paragraph with its "what it does" line, and
   no evidence title shares a paragraph with its points, anywhere in the
   document.
2. Every `N —` section title is a real `<h3>`; no sub-section title and no
   evidence title is a heading of any level — all stay `<strong>` inside
   their own `<p>`.
3. Every sub-section ends with exactly one of: `⚠️ GAP:`, `✅ GAP: none`, or
   `🎨 EVIDENCE: none` — none is missing, and the emoji are intact.
4. No literal `>` blockquote character and no typed `━━━` or `═══` divider
   row survives anywhere in the Doc text — these are all `<hr>` dividers,
   bold-labeled paragraphs, or spacer paragraphs by this point.
5. Content bullets and evidence points are real `<ul>` / `<li>` lists, with
   no spacer paragraphs between items and a spacer after each closing
   `</ul>`.
6. Every evidence point carries its own `&rarr; How it serves:` clause, and
   every evidence block closes with a 🔗 Source paragraph whose URL is a
   real `<a href>`.
7. Every fit label reads `(Fit: HIGH)` or `(Fit: MED)` — never `LOW`, never
   missing.
8. The Coverage Summary is three real `<table>` elements with `<th>` header
   rows, the Metrics table has all five rows, and its counts agree with the
   GAP rows listed beneath it.
9. Not one `style`, `class`, `<style>`, `<blockquote>`, or color attribute
   appears in the output, and no literal Markdown characters (`#`, `**`,
   `-`, `---`, `•`) survive anywhere in the Doc text.
