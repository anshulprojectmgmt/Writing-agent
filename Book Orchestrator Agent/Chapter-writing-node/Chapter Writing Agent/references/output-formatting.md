# Output Formatting Rules — Chapter Writing (HTML)

Applies to the HTML produced by the Chapter Writing skill after the complete
chapter draft, the Chapter Writing Notes, the Manuscript Handoff Package and the
Completeness Summary have all been written, the Voice Pass has run, and the
bold/italic placement below has been decided.

That HTML is sent to Google Docs through Gumloop's `gdocs` → `create_doc` tool
(`content_format: "html"`) as the document body, so **the markup written here is
the source of truth for how the Doc looks.** The converter renders what the
markup encodes and nothing more.

**This file governs markup only — never content.** Prose, punch lines,
citations, headings, table cells and field values reach the Doc with the exact
wording produced while drafting. Nothing here justifies shortening, merging or
rewording anything to fit a template. The one thing this file *does* decide is
**which existing words carry `<strong>` and `<em>`** (the Emphasis section),
because emphasis is formatting, not wording.

Every block below is a template. **Emit the markup exactly**, including every
spacer paragraph and every `<font>` attribute. Replace only the `{placeholders}`.

---

## 1. What the converter accepts

### 1.1 Structural tags — verified in this pipeline

Tested against the actual Gumloop `create_doc` conversion by the sibling skills
(Broad Research, Research Analysis, Chapter Blueprint, Deep Research, Research
Mapping):

| Works | Does not work |
|---|---|
| `<h1>` `<h2>` `<h3>` — real Doc heading styles (outline pane) | **`style="..."` attributes — silently stripped** |
| `<strong>` — bold | `<style>` blocks — ignored |
| `<em>` — italic | `class=` — no stylesheet exists |
| `<a href="...">` — clickable hyperlink | Any CSS margin, padding, line-height or spacing |
| `<hr>` — horizontal divider | Blank lines or indentation in the source — collapse to nothing |
| `<ul>` `<ol>` `<li>` — real Doc lists | `<blockquote>` — no reliable indent or rule survives |
| `<table>` `<tr>` `<th>` `<td>` — real Doc table | `<h4>` and deeper — no heading style to map to |
| `<p>` — a paragraph (0pt space before/after) | Code fences / `<pre>` — collapse into one paragraph |

### 1.2 Presentational attributes — the book look

The typography (Georgia body, larger headings, one crimson accent, tinted table
headers) comes from **HTML presentational attributes, not CSS**:

| Markup | Renders as |
|---|---|
| `<font face="Georgia">` / `<font face="Arial">` | Font family |
| `<font size="N">` | Font size — see the size map below |
| `<font color="#8e1b1b">` | Text colour |
| `<th bgcolor="#f6f4f1">` | Cell shading |
| `<table border="1" bordercolor="#d9d4cc" cellpadding="5" width="100%">` | Light 1pt cell borders, 5pt cell padding, full width |
| `<th width="NN%">` | Column width hint (best effort, never guaranteed) |

These are **not** CSS and are not covered by the "no CSS" rule. They were
verified to render in a Google Doc built from this exact markup (the reference
chapter *Conversational + Live-Generated UI Fusion — Chapter V1*). Two things
follow:

- **Always emit them.** If a converter ever drops a presentational attribute,
  the document degrades to the plain structural version (default fonts, black
  headings) with no content lost — the structure in 1.1 still carries it. So
  there is no downside to emitting them and no reason to leave them out.
- **Never "upgrade" them to CSS.** `style="font-size:20pt"` is stripped;
  `<font size="6">` is the mechanism. Do not mix the two.

**Font size map** (Google Docs import of `<font size>`):

| `size` | Renders | Used for |
|---|---|---|
| `1` | 8pt | Spacer paragraphs only |
| `2` | 10pt | The `WOW MOMENT` label |
| `3` | 11pt | Notes, Handoff and Summary text, table cells |
| `4` | 12pt | Chapter body text and list items |
| `5` | 14pt | Subsection headings (`<h3>`), the Completeness Summary heading |
| `6` | 18pt | Section headings (`<h2>`) |
| `7` | 24pt | Chapter title and the Notes / Handoff output titles (`<h1>`) |

### 1.3 Palette — four values, nothing else

| Token | Hex | Used on |
|---|---|---|
| Accent | `#8e1b1b` | Section headings, `[TECH]` / `[WOW MOMENT]` tags in subsection headings, the `WOW MOMENT` label, the `Before:` / `After:` labels |
| Ink | `#1f1f1f` | Table header text |
| Tint | `#f6f4f1` | Table header cell shading |
| Rule | `#d9d4cc` | Table borders |

Body text, subsection headings and the chapter title take the default black —
no `color` attribute. No other colours, no highlight, no underline.

---

## 2. The spacing system

Google Docs gives every converted `<p>` **0pt of space before and after**, so
consecutive paragraphs touch. Space is created structurally, and only by these
mechanisms:

**The spacer paragraph** — a paragraph holding one non-breaking space at 8pt:

```html
<p><font size="1">&nbsp;</font></p>
```

It produces a gap of roughly 9pt, which is the book's paragraph gap. **Never use
the bare `<p>&nbsp;</p>`** — at the default 11pt it opens a full blank line,
which is what made earlier drafts feel spaced out at every point.

**Heading styles** — `<h2>` carries ~18pt above it and `<h3>` ~14–16pt above,
built into the Doc's heading styles. That is enough on its own.

**The rule** — `<hr>` between top-level sections.

### 2.1 Where a spacer goes — and where it never goes

| After this… | …emit a spacer? |
|---|---|
| A body paragraph | **Yes** |
| A punch line paragraph | **Yes** |
| The `Before:` paragraph and the `After:` paragraph | **Yes**, after each |
| A list (`</ul>` / `</ol>`) | **Yes** |
| A table (`</table>`) | **Yes** |
| A labelled line in the Notes / Handoff | **Yes** |
| An `<h1>`, `<h2>` or `<h3>` heading | **No** — the heading style already spaces it |
| An `<hr>` | **No** |
| The `WOW MOMENT` label | **No** — the label sits directly on its punch line |
| A list-introducing label line (`Your move:`) | **No** — the label sits directly on its list |
| The chapter title `<h1>` | **No** — it is followed directly by `<hr>` |

Never two spacers in a row. Never a spacer as the first element of the document.

### 2.2 Where a rule goes

- Directly after the chapter title `<h1>`.
- Directly before every chapter-section `<h2>` **except the first** (sections 2,
  3, … and the unnumbered closing section each get one).
- Directly before the `Chapter Writing Notes` `<h1>` and the
  `Manuscript Handoff Package` `<h1>`.
- **Not** before the `Completeness Summary` `<h2>` — it belongs to the Handoff.
- Never between subsections, never around a punch line, never around a WOW label.

---

## 3. Templates — chapter draft

### 3.1 Document title

```html
<h1><strong><font face="Arial" size="7">CHAPTER {N} {CHAPTER TITLE}</font></strong></h1>
<hr>
```

Chapter number and title only, no dash. When no chapter number is supplied, the
title stands alone (`CONVERSATIONAL + LIVE-GENERATED UI FUSION`). Never
invent a number.

### 3.2 Section heading

First section:

```html
<h2><strong><font face="Arial" size="6" color="#8e1b1b">{N} {Section title}</font></strong></h2>
```

Every later section, including the unnumbered closing section:

```html
<hr>
<h2><strong><font face="Arial" size="6" color="#8e1b1b">{N} {Section title}</font></strong></h2>
```

A `[TECH]` or `[WOW MOMENT]` tag on a section title stays inside the same
`<font>` — the whole heading is already accent-coloured:

```html
<h2><strong><font face="Arial" size="6" color="#8e1b1b">4 [TECH] How does the model draw the screen?</font></strong></h2>
```

### 3.3 Subsection heading

```html
<h3><strong><font face="Arial" size="5">{N}.{X} {Subsection title}</font></strong></h3>
```

With a blueprint tag, the tag alone takes the accent:

```html
<h3><strong><font face="Arial" size="5">1.3 <font color="#8e1b1b">[WOW MOMENT]</font> How much does navigation really cost?</font></strong></h3>
```

Scene beats (The Setup, The Magic, The Razor's Edge) use the same `<h3>`
template, unnumbered.

### 3.4 Body paragraph

```html
<p><font face="Georgia" size="4">{Prose, with its <strong>bold</strong> and <em>italic</em> runs inline.}</font></p>
<p><font size="1">&nbsp;</font></p>
```

One `<font>` wraps the whole paragraph. `<strong>` and `<em>` sit **inside** it.
A section's opening paragraph follows its heading with no spacer between them.

### 3.5 Punch line

```html
<p><font face="Georgia" size="4"><strong>{Punch line, verbatim from the blueprint.}</strong></font></p>
<p><font size="1">&nbsp;</font></p>
```

Always its own paragraph, always fully bold, always black. It closes the
subsection it belongs to.

### 3.6 WOW moment

Inside a `[WOW MOMENT]` subsection only, the subsection's punch line — its
central finding — carries a small accent label directly above it:

```html
<p><font face="Arial" size="2" color="#8e1b1b"><strong>WOW MOMENT</strong></font></p>
<p><font face="Georgia" size="4"><strong>{The WOW subsection's punch line, verbatim.}</strong></font></p>
<p><font size="1">&nbsp;</font></p>
```

- No spacer between the label and the punch line.
- No table, box, shading, border or blockquote. Earlier versions put the WOW
  finding in a tinted one-cell table; it read as a heavy block and was removed.
- Exactly one label per `[WOW MOMENT]` subsection. Never a label anywhere else.
- Prose that follows the finding in the same subsection (a caveat, a turn) is an
  ordinary body paragraph after the spacer.

### 3.7 Reader transformation — Before and After

At the single designated transformation point, the Before and After are **two
paragraphs**, each opening with a bold accent run-in label:

```html
<p><font face="Georgia" size="4"><strong><font color="#8e1b1b">Before:</font></strong> {The Before, in one or two sentences.}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Georgia" size="4"><strong><font color="#8e1b1b">After:</font></strong> {The After, in one or two sentences.}</font></p>
<p><font size="1">&nbsp;</font></p>
```

- Never one paragraph holding both labels. Never a table (an earlier two-column
  Before | After table was removed for the same reason as the WOW box).
- Only the label word and its colon are bold and coloured; the sentence is plain.
- These labels appear once in the chapter.

### 3.8 List

A list introduced by a label line (the Your Move questions):

```html
<p><font face="Georgia" size="4"><strong>Your move:</strong></font></p>
<ul><li><font face="Georgia" size="4">{Question one.}</font></li><li><font face="Georgia" size="4">{Question two.}</font></li><li><font face="Georgia" size="4">{Question three.}</font></li></ul>
<p><font size="1">&nbsp;</font></p>
```

A list following a prose paragraph that announces the count: the paragraph and
its spacer, then the `<ul>`/`<ol>`, then a spacer. `<ol>` when the prose names an
order; `<ul>` otherwise. Every `<li>` wraps its text in the Georgia size-4 font.
Never nest lists.

### 3.9 Manuscript table (rare)

Only for a genuine two-axis comparison the prose would otherwise walk through
twice — at most one in the chapter, never as a layout device, never for the WOW
moment or the Before/After. Use the table template in 4.1 with the chapter's
columns.

---

## 4. Templates — Notes, Handoff, Summary

These outputs are working material, so they switch to Arial size 3 (11pt).

### 4.1 Chapter Writing Notes

```html
<hr>
<h1><strong><font face="Arial" size="7">Chapter Writing Notes</font></strong></h1>
<table border="1" bordercolor="#d9d4cc" cellpadding="5" width="100%">
<tr>
<th width="14%" bgcolor="#f6f4f1"><p><font face="Arial" size="3" color="#1f1f1f">Section</font></p></th>
<th width="22%" bgcolor="#f6f4f1"><p><font face="Arial" size="3" color="#1f1f1f">Evidence Used</font></p></th>
<th width="22%" bgcolor="#f6f4f1"><p><font face="Arial" size="3" color="#1f1f1f">Gaps Managed</font></p></th>
<th width="20%" bgcolor="#f6f4f1"><p><font face="Arial" size="3" color="#1f1f1f">Tension Logged</font></p></th>
<th width="22%" bgcolor="#f6f4f1"><p><font face="Arial" size="3" color="#1f1f1f">Cut Decisions</font></p></th>
</tr>
<tr>
<td><p><font face="Arial" size="3">{Section}</font></p></td>
<td><p><font face="Arial" size="3">{Citation tags}</font></p></td>
<td><p><font face="Arial" size="3">{How unresolved gaps were handled}</font></p></td>
<td><p><font face="Arial" size="3">{Which tensions were preserved}</font></p></td>
<td><p><font face="Arial" size="3">{What was removed, and why}</font></p></td>
</tr>
</table>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Transformation Point:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Voice Pass:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Formatting Audit:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Book Profile Source:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
```

- One data `<tr>` per section of the draft, in draft order (the WOW or TECH
  subsection may take its own row when its handling differs).
- Header cells are `<th>` with shading; header text is not bold-tagged (the
  shading carries the header). Data cells are `<td>` with no shading.
- Table first, then the four labelled lines — this order is fixed.

### 4.2 Manuscript Handoff Package

```html
<hr>
<h1><strong><font face="Arial" size="7">Manuscript Handoff Package</font></strong></h1>
<p><font face="Arial" size="3"><strong>Word count:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Section word counts:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Citation list:</strong> {every inline reference, separated by semicolons}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Evidence coverage map:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Gaps requiring author decision:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Suggested line edits:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
```

Six labelled lines, in this order, one per paragraph. Only the label and its
colon are bold.

### 4.3 Completeness Summary

No rule before it. A two-column table, one row per check the skill lists, in the
skill's order:

```html
<h2><strong><font face="Arial" size="5">Completeness Summary</font></strong></h2>
<table border="1" bordercolor="#d9d4cc" cellpadding="5" width="100%">
<tr><th width="60%" bgcolor="#f6f4f1"><font face="Arial" size="3" color="#1f1f1f">Check</font></th><th width="40%" bgcolor="#f6f4f1"><font face="Arial" size="3" color="#1f1f1f">Result</font></th></tr>
<tr><td><font face="Arial" size="3">Word count</font></td><td><font face="Arial" size="3">{count}</font></td></tr>
<tr><td><font face="Arial" size="3">Section count</font></td><td><font face="Arial" size="3">{N, vs. blueprint's N}</font></td></tr>
<tr><td><font face="Arial" size="3">{Check name}</font></td><td><font face="Arial" size="3">{Result}</font></td></tr>
</table>
<p><font size="1">&nbsp;</font></p>
```

Never a code fence. The check name is the label from the skill's summary block
without its colon; the result is everything after the colon.

---

## 5. Emphasis — where bold and italic go

Emphasis is decided **after** the Voice Pass, on the finished wording, and never
changes a word. It is the difference between a grey page and a page whose
argument can be found on a skim.

### 5.1 Bold

**Density.** The chapter is bold-rich by design:

- **Every substantive body paragraph (three or more sentences) carries one or
  two bold phrases.** A paragraph with none is the exception and needs a reason
  (a pure bridge, a Scene beat whose force is in its rhythm).
- **Short bridge paragraphs (one or two sentences)** carry zero or one.
- **A typical section lands at roughly 10–20 bold items** counting punch lines
  and its subsection headings' own `<strong>`. A section under 8 is
  under-formatted; go back through its paragraphs.

**What gets bolded — the load-bearing phrase**, in this priority:

1. **The paragraph's claim** — the phrase the paragraph exists to deliver:
   *whether you know where the thing lives*, *sending data, not code*,
   *a compiler constrained by a design system*, *govern that output, not design
   the screens*.
2. **The hard number that is the paragraph's evidence** — bold the figure with
   its unit and what it measures, not the citation: *41% increase in onboarding
   completion*, *702 accessibility-related issues across 288 screens*,
   *over 40% abandonment within ten seconds*. When a paragraph reports a cluster
   of results, each result may be bolded (up to three).
3. **A key term at first definition** where the chapter reuses it:
   *progressive enhancement*, *the control plane*, *finite state machines*,
   *a runtime pattern*, *bounded catalog*.
4. **A paired contrast** — both halves when the paragraph turns on them:
   *Search demands recall* … *Navigation supports recognition*;
   *fragmenting, not consolidating*; *direction, not gospel*.
5. **The turn** — a very short sentence (five words or fewer) that flips the
   paragraph, bolded without its full stop: *It is a number*, *It got bypassed*,
   *It is shipped*, *It is a count*.

**Bold phrase length:** two to about ten words. The punch line is the only
full-sentence bold, plus the ≤5-word turn in rule 5.

**Never bold:**

- whole ordinary sentences,
- citations or attributions — `(a16z, 2024)` stays plain,
- text already in `<em>` (never nest `<strong>` and `<em>`),
- the Your Move list items,
- anything in the Notes, Handoff or Summary except the field labels,
- the same phrase twice in the chapter — bold the first occurrence only.

**Placement must not become a template.** Do not bold the first words of every
paragraph, do not bold the last sentence of every paragraph, and do not let two
adjacent paragraphs open with bold. The run-in opener (a bold two-to-six word
phrase that opens a paragraph) is allowed a few times per chapter, never in
consecutive paragraphs.

### 5.2 Italic

Unchanged from the skill's Formatting section: **two to four per section**,
each doing one job — a defined technical term at first use, a line voiced as the
product's or the user's own (*"do you know where this lives?"*), a single pivotal
word (*what* … *when*), or a phrase held at arm's length. Never a whole paragraph
of ordinary prose, never twice in one paragraph, never combined with bold.

### 5.3 Worked example

Prose as drafted:

> An adaptive, AI-powered onboarding redesign for a B2B SaaS ERP used GPT-4 and
> real-time behavioral signals to adjust steps and generate dynamic onboarding
> paths by user role. It reported a 41% increase in onboarding completion, 2.3x
> faster time-to-task, and an 82% lift in three-week retention (Harashyn, 2025).
> The time-to-task figure is the one to stare at.

Rendered:

```html
<p><font face="Georgia" size="4">An adaptive, AI-powered onboarding redesign for a B2B SaaS ERP used GPT-4 and real-time behavioral signals to adjust steps and generate dynamic onboarding paths by user role. It reported a <strong>41% increase in onboarding completion</strong>, <strong>2.3x faster time-to-task</strong>, and an <strong>82% lift in three-week retention</strong> (Harashyn, 2025). The time-to-task figure is the one to stare at.</font></p>
<p><font size="1">&nbsp;</font></p>
```

---

## 6. Document skeleton

```html
<h1><strong><font face="Arial" size="7">CHAPTER {N} {CHAPTER TITLE}</font></strong></h1>
<hr>
<h2><strong><font face="Arial" size="6" color="#8e1b1b">1 {Section title}</font></strong></h2>
<p><font face="Georgia" size="4">{Section opening paragraph.}</font></p>
<p><font size="1">&nbsp;</font></p>
<h3><strong><font face="Arial" size="5">1.1 {Subsection title}</font></strong></h3>
<p><font face="Georgia" size="4">{Paragraph.}</font></p>
<p><font size="1">&nbsp;</font></p>
<p><font face="Georgia" size="4"><strong>{Punch line.}</strong></font></p>
<p><font size="1">&nbsp;</font></p>
<h3><strong><font face="Arial" size="5">1.2 {Subsection title}</font></strong></h3>
...
<hr>
<h2><strong><font face="Arial" size="6" color="#8e1b1b">2 {Section title}</font></strong></h2>
...
<hr>
<h2><strong><font face="Arial" size="6" color="#8e1b1b">{Unnumbered closing section title}</font></strong></h2>
...
<p><font face="Georgia" size="4"><strong>Your move:</strong></font></p>
<ul><li><font face="Georgia" size="4">{Question.}</font></li></ul>
<p><font size="1">&nbsp;</font></p>
<hr>
<h1><strong><font face="Arial" size="7">Chapter Writing Notes</font></strong></h1>
<table border="1" bordercolor="#d9d4cc" cellpadding="5" width="100%">...</table>
<p><font size="1">&nbsp;</font></p>
<p><font face="Arial" size="3"><strong>Transformation Point:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
...
<hr>
<h1><strong><font face="Arial" size="7">Manuscript Handoff Package</font></strong></h1>
<p><font face="Arial" size="3"><strong>Word count:</strong> {value}</font></p>
<p><font size="1">&nbsp;</font></p>
...
<h2><strong><font face="Arial" size="5">Completeness Summary</font></strong></h2>
<table border="1" bordercolor="#d9d4cc" cellpadding="5" width="100%">...</table>
<p><font size="1">&nbsp;</font></p>
```

No `<html>`, `<head>` or `<body>` wrapper is required; the body markup is the
document. Nothing precedes the title `<h1>`.

---

## 7. Heading levels

| Tag | Font | Used for |
|---|---|---|
| `<h1>` | Arial size 7, black, bold | The chapter title; the `Chapter Writing Notes` and `Manuscript Handoff Package` output titles |
| `<h2>` | Arial size 6, **accent**, bold | Every chapter section, numbered or not |
| `<h2>` | Arial size 5, black, bold | `Completeness Summary` only |
| `<h3>` | Arial size 5, black, bold; tag in accent | Every subsection and Scene beat |
| `<strong>` in `<p>` | — | Punch lines, WOW label, Before/After labels, list labels, field labels, and in-paragraph emphasis |

Headings carry no dashes: number, single space, title. `[TECH]` and
`[WOW MOMENT]` are the only bracket tags that reach a heading.

---

## 8. Escaping

- `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;` in all content.
- Em dash `&mdash;`, en dash `&ndash;`, ellipsis `&hellip;`, arrow `&rarr;`.
  (The prose itself avoids mid-sentence em dashes per the house rules; this
  governs any that legitimately remain, e.g. in a quoted title.)
- Straight apostrophes and quotation marks may be written literally.
- Non-breaking spaces from drafting become ordinary spaces, except inside the
  spacer paragraph.

---

## 9. Verify before creating the Doc

Run this against the HTML file in the sandbox before calling `create_doc`. Fix
and re-run until it prints `OK`.

```python
import re

html = open('/home/user/chapter.html', encoding='utf-8').read()
problems = []
SP = '<p><font size="1">&nbsp;</font></p>'
FENCE = chr(96) * 3

# 1. No CSS of any kind
if re.search(r'\sstyle=|\sclass=|<style', html):
    problems.append('CSS found (style / class / <style>)')

# 2. Only the allowed tags
allowed = {'h1', 'h2', 'h3', 'p', 'strong', 'em', 'a', 'hr', 'ul', 'ol', 'li',
           'table', 'tr', 'th', 'td', 'font'}
used = set(re.findall(r'<([a-z0-9]+)[\s>]', html))
if used - allowed:
    problems.append(f'disallowed tags: {sorted(used - allowed)}')

# 3. No bare full-height spacer, no doubled spacer
if '<p>&nbsp;</p>' in html:
    problems.append('bare <p>&nbsp;</p> spacer: use the size-1 spacer')
if re.search(re.escape(SP) + r'\s*' + re.escape(SP), html):
    problems.append('two spacers in a row')

# 4. No spacer directly after a heading, a rule or the WOW label
if re.search(r'</h[123]>\s*' + re.escape(SP), html):
    problems.append('spacer after a heading')
if re.search(r'<hr>\s*' + re.escape(SP), html):
    problems.append('spacer after <hr>')
if re.search(r'WOW MOMENT</strong></font></p>\s*' + re.escape(SP), html):
    problems.append('spacer between the WOW label and its punch line')

# 5. Every paragraph outside tables is followed by a spacer,
#    except the WOW label and a list label line such as "Your move:"
outside = re.sub(r'<table.*?</table>', '<table></table>', html, flags=re.S)
for m in re.finditer(r'<p><font face="(?:Georgia|Arial)" size="([234])"[^>]*>(.*?)</font></p>', outside, re.S):
    inner = m.group(2).strip()
    if 'WOW MOMENT' in inner or re.fullmatch(r'<strong>[^<]*:</strong>', inner):
        continue
    if not outside[m.end():].lstrip().startswith(SP):
        problems.append('paragraph without a following spacer: '
                        + re.sub(r'<[^>]+>', '', inner)[:60])

# 6. Rules: after the title, before every chapter section, before Notes and Handoff
if not re.match(r'\s*<h1>.*?</h1>\s*<hr>', html, re.S):
    problems.append('the title <h1> must be followed directly by <hr>')
for m in re.finditer(r'<h2><strong><font face="Arial" size="6"', html):
    if not html[:m.start()].rstrip().endswith('<hr>'):
        problems.append('a section heading is not directly preceded by <hr>')
for title in ('Chapter Writing Notes', 'Manuscript Handoff Package'):
    if not re.search(r'<hr>\s*<h1><strong><font face="Arial" size="7">' + title, html):
        problems.append(f'<hr> missing before {title}')

# 7. Emphasis and leftovers
if re.search(r'<strong>[^<]*<em>|<em>[^<]*<strong>', html):
    problems.append('bold and italic nested')
if '<blockquote' in html or FENCE in html:
    problems.append('blockquote or code fence present')
if html.count('WOW MOMENT</strong>') != len(re.findall(r'\[WOW MOMENT\]</font>', html)):
    problems.append('WOW labels do not match the number of [WOW MOMENT] subsections')

# 8. Bold density per chapter section
chapter = html.split('Chapter Writing Notes')[0]
for sec in re.split(r'<h2><strong><font face="Arial" size="6"[^>]*>', chapter)[1:]:
    name = re.sub(r'<[^>]+>', '', sec[:sec.find('</h2>')])
    n = sec.count('<strong>')
    if n < 8:
        problems.append(f'under-bolded section ({n} bold): {name[:50]}')

print('OK' if not problems else '\n'.join(problems))
```

Then confirm by reading, not by script:

1. No section or subsection title shares a paragraph with its prose.
2. Every punch line is bold, on its own paragraph, verbatim from the blueprint.
3. Each `[WOW MOMENT]` subsection has exactly one `WOW MOMENT` label, sitting
   directly on that subsection's punch line.
4. Before and After are two separate paragraphs with accent labels, at the
   designated transformation point only.
5. Bold phrases are load-bearing (claim, number, term, contrast, turn), not
   decoration, and do not land in the same position paragraph after paragraph.
6. No typed `═══`, `━━━`, `---` or literal Markdown (`#`, `**`, `>`) remains.
