# Output Formatting Rules — Deep Research Package (HTML)

Applies to the HTML produced by the Deep Research skill, after the Deep
Research Package (every subsection's EVIDENCE, GAP FILLED, and GAP
UNRESOLVED blocks), the Research Summary, and the Writing Handoff have been
fully drafted per the skill's own Output Format spec.

That HTML is sent to Google Docs as the document body, so **the markup
written here is the source of truth for how the Doc looks.** The converter
renders what the markup encodes and nothing more.

**This file governs layout only — never content.** Every fact, statistic,
mechanism, quote, surprising detail, caveat, citation field, search log, and
recommendation must reach the finished Doc with the exact wording produced
during research. Nothing here justifies shortening, merging, paraphrasing,
or rewording anything to make it fit a template — least of all a quote or a
citation, which are the two things the writing phase cannot reconstruct if
this document gets them wrong.

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
| | Precise column widths — see the Research Summary note |

**CSS does not survive the conversion.** Do not write a single `style`
attribute. There is no color in this pipeline, so a GAP FILLED and a GAP
UNRESOLVED cannot be distinguished by shading or ink — the distinction rests
entirely on the block-label text staying intact and bolded. Spacing is
created structurally, with the spacer paragraph below, and by no other
means.

**Tables convert, but column widths are best-effort.** A real `<table>`
element becomes a real Doc table — that part is reliable. There is no style
attribute to carry a width, and an HTML `width` attribute on a header cell
is only ever a hint the converter may or may not honor. Set it anyway on the
header row as the best available signal (see the Research Summary template),
but do not treat the resulting widths as guaranteed.

**`<blockquote>` is not in the supported set.** Where the package carries a
direct quote from a source, it stays inline inside its bullet, in quotation
marks, never in a `<blockquote>` and never as an indented paragraph. Never
emit a literal `>` at the start of a paragraph — it renders as a stray angle
bracket, not a quote.

---

## Standing rule: the spacer paragraph, and no label ever shares a paragraph with its content

Google Docs renders consecutive `<p>` elements with **no gap between them**.
Whitespace in the source HTML changes nothing — the converter ignores it.

The only way to create a visible blank line is to emit a paragraph that holds
a non-breaking space:

```html
<p>&nbsp;</p>
```

This is the single spacing mechanism in this document. **Put one between
every pair of blocks.** The failure this file exists to prevent is specific
to this skill: an evidence item's name running into its `Citation` line, the
citation running into the `Deep Bullets` list, and one subsection's last
caveat running into the next subsection's title — so that a writer scanning
the Doc for the evidence behind one claim cannot tell where one item ends
and the next begins.

**Wrong** — item name, citation, and bullets label stacked with no spacers:

```html
<p><strong>Spotify Wrapped</strong> <strong>Citation</strong> Smith /
Harvard Business Review / 2024 / {URL}</p>
<p><strong>Deep Bullets</strong></p>
```

**Right** — every part its own paragraph, spacer after each:

```html
<p><strong>Spotify Wrapped</strong></p>
<p>&nbsp;</p>
<p><strong>Citation:</strong> Smith / Harvard Business Review / 2024 /
<a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<p><strong>Deep Bullets</strong></p>
<p>&nbsp;</p>
```

Same wording, same order. The spacers and the paragraph breaks are the
entire difference between the two renders.

**On heading depth: `N.X —` subsection titles get `<h3>`; evidence item
names and block labels do not get a heading at all.** This is a deliberate
divergence from the sibling skills, and the reason is worth stating. In
Broad Research, Research Analysis, Chapter Blueprint, and Research Mapping,
repeated titles stay `<strong>` because a heading level above them already
carries the document's navigational spine. This package has no such tier —
the subsection **is** the spine, and the one thing a writer does with this
Doc is jump to the subsection they are drafting. So `N.X —` titles are real
`<h3>` headings and belong in the outline pane. Everything below them —
evidence item names, `EVIDENCE` / `GAP FILLED` / `GAP UNRESOLVED` labels,
and field labels — stays `<strong>` inside its own `<p>`, for the same
reason the siblings give: promoting them would flood the outline pane and
make it useless.

---

## 1. Document title

```html
<h1>{Chapter Name} &mdash; Deep Research Package</h1>
<p>&nbsp;</p>
<p><strong>Chapter:</strong> {Chapter Name}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

The typed `---` rule rows in the skill's own output spec are a chat
convention — they become real `<hr>` dividers here and never survive as
typed characters.

---

## 2. Subsection

Each subsection is a heading, then its EVIDENCE blocks, then its GAP blocks,
in that order.

```html
<h3>{N}.{X} &mdash; {SUBSECTION NAME}</h3>
<p>&nbsp;</p>
```

Rules for this block:

- Subsections run in blueprint order, and the numbering matches the mapped
  blueprint exactly — this Doc is read side by side with it.
- `<hr>` separates subsections, with a spacer on both sides. Do not put an
  `<hr>` between the EVIDENCE and GAP blocks inside the same subsection —
  the spacer paragraphs do that work.
- A subsection the mapping marked `EVIDENCE: NONE` with no GAP is skipped
  entirely, per the skill's own rule. Do not emit an empty heading for it.

---

## 3. EVIDENCE block

The core repeating unit of this document. One block per assigned evidence
item: the block label, the item name, its citation, and its deep bullets.

```html
<p><strong>EVIDENCE</strong></p>
<p>&nbsp;</p>
<p><strong>{Evidence Item Name}</strong></p>
<p>&nbsp;</p>
<p><strong>Citation:</strong> {Author} / {Publication} / {Year} / <a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<p><strong>Deep Bullets</strong></p>
<p>&nbsp;</p>
<ul>
<li><strong>Fact:</strong> {Specific fact, finding, or observation.}</li>
<li><strong>Mechanism:</strong> {How it works, why it works, what caused the result.}</li>
<li><strong>Statistic:</strong> {Metric, percentage, benchmark, or outcome.}</li>
<li><strong>Quote:</strong> "{Short, directly usable quote.}"</li>
<li><strong>Surprising detail:</strong> {Counterintuitive or non-obvious finding.}</li>
<li><strong>Caveat:</strong> {Limitation, failure mode, criticism, or contradictory evidence.}</li>
</ul>
<p>&nbsp;</p>
```

Rules for this block:

- **A spacer after the `EVIDENCE` label, after the item name, after the
  citation, after the `Deep Bullets` label, and after the closing `</ul>`.**
  A block with fewer is wrong — this is the defect this file exists to fix.
- **No spacer between `<li>` items.** The list is one block; the spacer goes
  after the closing `</ul>`.
- Deep bullets are a real `<ul>`, never `→` characters typed into
  paragraphs. The `→` in the skill's own spec is a chat bullet marker and is
  replaced by the list marker — do not emit both.
- **Each bullet carries its kind as a bold label**, from the skill's own
  six: `Fact`, `Mechanism`, `Statistic`, `Quote`, `Surprising detail`,
  `Caveat`. The label is what lets a writer scan for the statistic without
  reading the whole block.
- **Emit only the kinds the research actually produced.** Statistic, Quote,
  and Surprising detail are conditional in the skill's own spec — a block
  with four real bullets is correct; a block padded to six with an empty or
  invented bullet is not. Never emit a label with nothing after it.
- Quotes stay inline inside their bullet, in quotation marks, with no
  `<blockquote>` and no invented attribution beyond the citation line above.
- The citation is one paragraph with all four fields in the skill's order —
  Author / Publication / Year / URL — and the URL is a real hyperlink. A
  field the source genuinely does not carry is written `n/a`, never dropped
  silently and never guessed at.
- A subsection with more than one assigned item repeats the whole block —
  `EVIDENCE` label, item name, citation, bullets — once per item.

---

## 4. GAP FILLED block

```html
<p><strong>GAP FILLED</strong></p>
<p>&nbsp;</p>
<p><em>{Original GAP, copied from the mapped blueprint unchanged.}</em></p>
<p>&nbsp;</p>
<p><strong>Source:</strong> {Publication} / <a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<p><strong>Citation:</strong> {Author} / {Publication} / {Year} / <a href="{URL}">{URL}</a></p>
<p>&nbsp;</p>
<p><strong>Deep Bullets</strong></p>
<p>&nbsp;</p>
<ul>
<li><strong>Supporting fact:</strong> {&hellip;}</li>
<li><strong>Supporting evidence:</strong> {&hellip;}</li>
<li><strong>Supporting statistic:</strong> {&hellip;}</li>
<li><strong>Caveat:</strong> {&hellip;}</li>
</ul>
<p>&nbsp;</p>
```

Rules for this block:

- The original GAP is italic and carried over **verbatim** from the mapped
  blueprint, so the writer can see what was asked for and judge whether the
  answer actually meets it. Do not rewrite it to match what was found.
- `Source` and `Citation` are separate paragraphs, as in the skill's own
  spec — do not merge them because they overlap.
- The four bullet kinds follow the same rules as the EVIDENCE block: real
  `<ul>`, bold kind labels, no `→`, and no padding with empty bullets.

---

## 5. GAP UNRESOLVED block

```html
<p><strong>GAP UNRESOLVED</strong></p>
<p>&nbsp;</p>
<p><em>{Original GAP, copied from the mapped blueprint unchanged.}</em></p>
<p>&nbsp;</p>
<p><strong>Searches Conducted</strong></p>
<p>&nbsp;</p>
<ul>
<li>{Search term or query, as run.}</li>
<li>{Search term or query, as run.}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Findings:</strong> {What was found, and why it does not close the gap.}</p>
<p>&nbsp;</p>
<p><strong>Recommendation:</strong> {Cut claim / Soften claim / Mark uncertainty / Leave for future research}</p>
<p>&nbsp;</p>
```

Rules for this block:

- `Searches Conducted` is a labeled paragraph introducing a real `<ul>`, and
  is never itself an `<li>`. The searches are the evidence that the gap was
  genuinely worked — a vague "searched widely" paragraph is a content
  failure, not a formatting one.
- `Findings` and `Recommendation` are each their own bold-labeled paragraph.
  Two labels sharing a paragraph is the defect this block exists to prevent.
- The recommendation is exactly one of the skill's four options, written out
  in full — not abbreviated, not hedged into two.

---

## 6. Research Summary

The metrics are a real table; the five "Strongest / Remaining" fields are
labeled paragraphs each introducing a real list.

```html
<h2>Research Summary</h2>
<p>&nbsp;</p>
<table>
<tr>
<th width="70%">Metric</th>
<th width="30%">Count</th>
</tr>
<tr><td>Total Evidence Items Expanded</td><td>{N}</td></tr>
<tr><td>GAPs Resolved</td><td>{N}</td></tr>
<tr><td>GAPs Partially Resolved</td><td>{N}</td></tr>
<tr><td>GAPs Unresolved</td><td>{N}</td></tr>
</table>
<p>&nbsp;</p>
<p><strong>Strongest New Findings</strong></p>
<p>&nbsp;</p>
<ul>
<li>{&hellip;}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Strongest Statistics</strong></p>
<p>&nbsp;</p>
<ul>
<li>{&hellip;}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Strongest Case Studies</strong></p>
<p>&nbsp;</p>
<ul>
<li>{&hellip;}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Strongest Academic Findings</strong></p>
<p>&nbsp;</p>
<ul>
<li>{&hellip;}</li>
</ul>
<p>&nbsp;</p>
<p><strong>Remaining Research Needs</strong></p>
<p>&nbsp;</p>
<ul>
<li>{&hellip;}</li>
</ul>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
```

Rules for this block:

- **The header row uses `<th>`, not `<td>`** — that alone is what makes it
  read as a header once shading (unavailable here) is off the table.
- The four metric rows are fixed: emit all four, in that order, even when a
  count is `0`. A missing row reads as an oversight, not a zero.
- The counts must agree with the document above them — the GAPs Unresolved
  count and the number of `GAP UNRESOLVED` blocks are the same number.
- All five labeled fields are emitted, each as a bold paragraph followed by
  its own `<ul>`. A field with nothing to report gets a single `<li>` saying
  `None` — never an empty list, and never a dropped label.

---

## 7. Writing Handoff

```html
<h2>Writing Handoff</h2>
<p>&nbsp;</p>
<p>{The handoff paragraph &mdash; what this package provides for the writing
phase.}</p>
<p>&nbsp;</p>
<ul>
<li>Supporting evidence</li>
<li>Citation trail</li>
<li>Facts</li>
<li>Statistics</li>
<li>Quotes</li>
<li>Caveats</li>
</ul>
<p>&nbsp;</p>
```

The checklist stays a real `<ul>` — it is what the writing phase reads to
confirm the package is usable before drafting starts.

---

## 8. General

**Document skeleton.** The package opens with the title and the chapter
field, then runs the subsections in blueprint order, then the Research
Summary and the Writing Handoff:

```html
<h1>{Chapter Name} &mdash; Deep Research Package</h1>
<p>&nbsp;</p>
<p><strong>Chapter:</strong> {Chapter Name}</p>
<p>&nbsp;</p>
<hr>
<p>&nbsp;</p>
<h3>1.1 &mdash; {SUBSECTION NAME}</h3>
<p>&nbsp;</p>
...
<h2>Research Summary</h2>
<p>&nbsp;</p>
...
<h2>Writing Handoff</h2>
<p>&nbsp;</p>
...
```

**Heading levels.** Headings become the Doc's real Heading styles, which is
what makes the outline pane work:

| Tag | Used for |
|---|---|
| `<h1>` | The document title, carrying the chapter name |
| `<h2>` | `Research Summary` and `Writing Handoff` |
| `<h3>` | Each `N.X —` subsection title — the document's navigational spine |
| `<strong>` | `EVIDENCE` / `GAP FILLED` / `GAP UNRESOLVED` labels, evidence item names, bullet kind labels, and every field label — body text, not headings |

Subsection titles are real headings here on purpose — see the heading-depth
note above for why this skill diverges from its siblings. Everything below
that tier stays `<strong>`, for the reason the siblings give.

**No escaped subsection numbers.** Write `<h3>2.1 &mdash; What Does
Personalization Promise?</h3>`, not an escaped or backslashed form.

**Escape HTML special characters in content.** `&` becomes `&amp;` — this
matters in publication names like `Wired &amp; Co`. `<` becomes `&lt;` and
`>` becomes `&gt;`. Em dashes are written `&mdash;`, en dashes (in year
ranges like "2019–2024") `&ndash;`, ellipses `&hellip;`, and percent figures
stay as typed.

**Hyperlinks.** Every citation and source URL is written
`<a href="{URL}">{URL}</a>` — the address in both places. Never leave a bare
URL as plain text, and never replace the link text with a publication name
or article title; the publication already appears in its own field of the
citation line. A source with genuinely no URL (a print work, a paywalled
report cited from its abstract) keeps its other citation fields and writes
the URL field as `n/a`.

**Never emit an empty heading, an empty table row, a table with only a
header row, or an empty list.** A subsection heading with no blocks under
it, a `Deep Bullets` label with no bullets, or a bullet label with nothing
after it all mean something was dropped between research and rendering.

**No CSS, anywhere.** No `style` attributes, no `<style>` blocks, no
`class`, and no color. They are stripped in conversion and their presence
gives a false impression that spacing, shading, or the FILLED/UNRESOLVED
distinction is handled by something other than the markup and the label text
itself. `<p>&nbsp;</p>` is the only spacing mechanism, and
`<strong>`/`<em>` are the only emphasis mechanisms.

**Verify before delivering.** Re-read the generated HTML and confirm:

1. No evidence item name shares a paragraph with its citation, and no
   citation shares a paragraph with its `Deep Bullets` label, anywhere in
   the document.
2. Every `N.X —` subsection title is a real `<h3>`; no `EVIDENCE`,
   `GAP FILLED`, `GAP UNRESOLVED`, or item-name line is a heading of any
   level — all stay `<strong>` inside their own `<p>`.
3. Every deep-bullet list is a real `<ul>` with bold kind labels, no `→`
   characters, no spacer paragraphs between items, and a spacer after each
   closing `</ul>`.
4. Every EVIDENCE and GAP FILLED block carries a `Citation` paragraph with
   all four fields in order, and every URL in the document is a real
   `<a href>`, not bare text.
5. Every GAP UNRESOLVED block has `Searches Conducted` as a labeled
   paragraph above a real list, and `Findings` and `Recommendation` as two
   separate bold-labeled paragraphs.
6. Every original GAP line is italic and matches the mapped blueprint's
   wording exactly.
7. No literal `>` blockquote character and no typed `---` or `━━━` divider
   row survives anywhere in the Doc text — these are all `<hr>` dividers or
   spacer paragraphs by this point.
8. The Research Summary's metrics table is a real `<table>` with a `<th>`
   header row and all four rows, its counts agree with the blocks above it,
   and all five labeled lists are present.
9. Not one `style`, `class`, `<style>`, `<blockquote>`, or color attribute
   appears in the output, and no literal Markdown characters (`#`, `**`,
   `-`, `---`) survive anywhere in the Doc text.
