---
name: ai-humanizer-core
description: Final-pass skill to remove obvious AI-writing fingerprints while preserving the author's voice. Focuses on two things only: structure and language. Uses cluster-based judgment and minimum intervention.
---

# AI Humanizer Core

## Purpose

Make writing feel less AI-generated **without changing the author's voice**.

This is not a writing-style skill.  
It is a final editing pass.

It checks only two things:

1. **Structure** — does the writing *look* AI-generated?
2. **Language** — does the writing *sound* AI-generated?

The writer creates the voice.  
This skill only removes obvious AI fingerprints.

---

## Core principle

**Humanize by subtraction, not invention.**

Do not add personality, slang, anecdotes, emotion, quirks, or fake imperfections.

Do not rewrite just because something *could* be improved.

Make the **smallest possible change** needed to remove obvious AI-ness.

If the writing already feels natural, leave it alone.

---

# 1. STRUCTURE CHECK

Ask:

> **Does this look mechanically or predictably AI-written?**

Look at the shape and rhythm of the writing before judging individual words.

Common structural signals include:

- excessive or unnatural line breaks
- putting nearly every sentence on a separate line
- overuse of `-` bullets where normal prose would read better
- too many headings, subheadings, or bold labels
- repetitive formatting patterns
- emoji use that feels templated, excessive, or unnaturally absent for the author
- overly uniform sentence lengths
- paragraphs that all have the same shape or size
- repeated punchy fragments
- repeated rhetorical templates such as “not X, but Y”
- repeated groups of three
- repeated rhetorical questions
- excessive use of em-dashes, colons, or similar punctuation patterns
- formulaic openings or transitions
- generic summary conclusions that neatly restate everything
- writing that feels too perfectly organized, balanced, or symmetrical
- listification: turning ideas into bullets simply because bullets are easy to generate
- superficial `-ing` clauses such as “highlighting…”, “showcasing…”, “underscoring…” added after a simple statement
- chatbot residue such as “Great question”, “Let’s dive in”, or “I hope this helps”

## Structural judgment rule

**Do not flag a structure just because AI often uses it.**

Humans also use:

- bullets
- emojis
- fragments
- em-dashes
- groups of three
- rhetorical questions
- “not X, but Y”
- bold headings

A structural element becomes suspicious when it is:

- repetitive
- mechanically regular
- overly neat
- templated
- unnecessary
- inconsistent with the author's natural style

**One tell means little. A cluster of tells is the signal.**

---

# 2. LANGUAGE CHECK

Ask:

> **Does this sound like wording an AI would choose instead of how a person would naturally say it?**

Look for language that is:

- unnecessarily sophisticated
- abstract when it could be concrete
- corporate or buzzword-heavy
- inflated beyond the importance of the idea
- vague but made to sound profound
- verbose when a common phrase would say the same thing
- built from stock AI transitions or clichés

## High-signal AI vocabulary

Treat these as **watchlist words**, not banned words:

- delve
- pivotal
- tapestry
- realm
- landscape
- underscore
- testament
- foster
- embark
- meticulous
- vibrant
- showcase
- robust
- seamless
- leverage
- transformative
- multifaceted
- navigate
- harness
- elevate
- empower
- streamline
- bolster
- facilitate
- nuanced
- ecosystem
- myriad
- plethora
- holistic
- synergy
- paradigm
- cornerstone
- paramount
- scalable
- compelling
- innovative

## Common AI phrases

Watch for phrases such as:

- “In today’s rapidly evolving…”
- “It is important to note…”
- “It is worth noting…”
- “Moreover…”
- “Furthermore…”
- “Additionally…”
- “At its core…”
- “It’s not X, it’s Y”
- “serves as…”
- “stands as…”
- “serves as a testament to…”
- “plays a crucial role…”
- “marking a pivotal moment…”
- “Let’s dive in…”
- “Let’s explore…”
- “Here’s what you need to know…”
- “The future looks bright…”
- “Experts believe…”
- “Studies show…” without a source
- “Whether you’re X or Y…”

## Language judgment rule

**Do not mechanically replace a word just because it appears on the watchlist.**

Keep it when:

- it is the most precise word
- it is standard terminology in the domain
- the author naturally uses it
- replacing it would reduce clarity or meaning

The strongest signal is **clustering**.

For example:

> “A transformative platform that leverages a robust ecosystem to empower teams and unlock seamless collaboration.”

is strongly AI-coded because several watchlist terms cluster together.

But:

> “We need a scalable database.”

is completely normal.

Prefer common language when meaning stays the same.

---

# Editing rules

When humanizing:

1. **Preserve meaning.**
2. **Preserve facts.**
3. **Preserve the author's voice.**
4. Preserve intentional humour, emotion, roughness, fragments, emphasis, formatting, and quirks.
5. Never invent anecdotes, details, emotions, numbers, examples, or opinions.
6. Do not add slang just to sound human.
7. Do not deliberately introduce grammar mistakes.
8. Do not remove all polish or structure.
9. Do not optimize for AI-detector scores.
10. Do not enforce mechanical rules such as “no em-dashes”, “no triads”, or “always vary sentence length”.
11. Prefer a local edit over a sentence rewrite.
12. Prefer a sentence rewrite over a paragraph rewrite.
13. Prefer a paragraph rewrite over a full-document rewrite.
14. Rewrite the whole piece only when AI patterns are pervasive and local fixes would make the result incoherent.

---

# Process

## Step 1 — Scan structure

Read the piece visually and rhythmically.

Ask:

> **Does this look predictably generated?**

Identify only the structural patterns creating that impression.

## Step 2 — Scan language

Read for vocabulary and phrasing.

Ask:

> **Does this sound like default AI language rather than natural language for this author and context?**

Identify only the words or phrases creating that impression.

## Step 3 — Look for clusters

Do not react to isolated signals.

Prioritize areas where **multiple AI tells appear together**.

## Step 4 — Patch minimally

Change only the affected spans.

Do not “improve” unrelated writing.

## Step 5 — Protect voice

Re-read the edited version and ask:

> **Did I remove AI fingerprints without making this less like the original author?**

If not, restore the author's original phrasing or structure.

---

# Priority order

When instructions conflict, use this order:

1. **Author's explicit writing style**
2. **Meaning and factual accuracy**
3. **Intentional voice and formatting choices**
4. **Humanization rules in this skill**

This skill must never override a deliberate author preference merely because that preference also appears in AI writing.

---

# Output behavior

### Default mode

Return only the minimally humanized text.

### Diagnose mode

If explicitly asked to diagnose before editing, return:

**Structure**
- specific patterns that feel AI-generated

**Language**
- specific words or phrases that feel AI-generated

**Action**
- minimum changes recommended

Do not rewrite unless asked.

---

# Final test

Before returning the result, ask:

> **Would a reasonable reader notice the writing less because of AI-like structure or wording, while still recognizing the same author?**

If yes, stop.

Do not keep optimizing.

---

## Guiding principle

**The writer creates the voice. The humanizer removes the fingerprints.**
