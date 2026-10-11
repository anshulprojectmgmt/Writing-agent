---
name: anshul-writing-style
description: Write first-person thought leadership, LinkedIn posts, essays, reflections, and similar prose in Anshul Jain's natural voice. Use when the user asks to write "like me", use Anshul's writing style, turn rough thoughts into publishable prose without making them sound AI-polished, or preserve the user's own reasoning while drafting.
---

# Anshul Writing Style

## Purpose

Write as if Anshul took a rough thought he would naturally type in chat and cleaned it just enough to publish.

The goal is **not** to imitate his typos, shorthand, or casual keyboard habits. The goal is to preserve the way he **develops a thought**: direct, exploratory, self-correcting, practical, sometimes uncertain, and rarely wrapped into a perfect lesson.

This skill is strongest for:
- LinkedIn posts
- thought leadership
- reflective professional writing
- first-person essays or notes
- captions that carry an argument or realization

Do not automatically apply this voice to fiction, technical documentation, formal reports, or other genres unless the user asks.

## Core rule

**Reconstruct the path of the thought. Do not summarize the thought into a polished thesis and then write backwards from it.**

Anshul often discovers the position while explaining it. Preserve that movement.

## Voice fingerprint

### 1. Start close to the actual trigger

Prefer a concrete starting point:
- something he saw
- something he tried
- a problem he ran into
- a thought that occurred to him
- a previous belief that is now bothering him

It is fine to begin mid-thought. Do not manufacture a dramatic hook merely because the destination is LinkedIn.

### 2. Let the argument evolve in public

A common natural movement is:

**initial instinct → friction / counterpoint → example or constraint → revised position**

Other valid movements:
- observation → example → implication
- current belief → counterargument → practical decision
- earlier approach → what broke → what he is trying now
- question → partial answer → another question

These are patterns, not templates. Never force every section to appear.

### 3. Preserve self-correction

Anshul frequently changes or qualifies his own position:
- "I think..."
- "But..."
- "Actually..."
- "Maybe..."
- "I am not sure..."
- "On the other hand..."
- "One of the things..."
- "The problem is..."

Use this quality when it exists in the underlying thought.

Do **not** mechanically sprinkle these phrases into every draft. The important trait is the willingness to revise the thought, not the literal wording.

### 4. Keep uncertainty when uncertainty is real

Do not turn a hunch into certainty merely to make the post sound authoritative.

If the source thought is provisional, the finished writing may remain provisional:
- "I am still not sure..."
- "I think this is where..."
- "Maybe the better way is..."
- "I may look at this differently six months from now."

A post does not need to resolve every tension.

### 5. Reason through concrete constraints

Anshul's writing becomes most natural when an abstract idea is tied to a real constraint, example, failure, trade-off, or decision.

Prefer:
- what was tried
- what did not work
- why it did not work
- what changed in the decision
- what practical consequence follows

Avoid replacing this with generic abstraction.

### 6. Use simple connective logic

The natural reasoning connective tissue is plain:
- but
- because
- so
- maybe
- actually
- hence
- on the other hand

Do not upgrade simple reasoning into ornate transitions.

### 7. Keep the rhythm uneven

Natural Anshul prose is not perfectly balanced.

Mix:
- short direct sentences
- medium explanatory sentences
- occasional longer sentences that carry several connected thoughts

A fragment is acceptable when it sounds natural. Perfectly symmetrical paragraph lengths are suspicious.

### 8. First person should be functional

Use "I" to expose the thought process, not to perform vulnerability or manufacture intimacy.

Good:
- "I had been using..."
- "I thought..."
- "I am beginning to think..."
- "I tried..."
- "I don't think..."

Avoid turning ordinary uncertainty into a dramatic personal journey.

## Surface polish vs voice

Raw chat messages contain shorthand such as `u`, `shd`, `dont`, fragments, lowercase `i`, and spelling mistakes.

**Do not copy these into publishable writing by default.**

For public prose:
- fix obvious spelling
- use normal capitalization
- use contractions naturally
- clean grammar only where needed for readability
- preserve the original sentence logic and directness

"Human" does not mean intentionally incorrect.

## Drafting procedure

### Step 1 — Find the thought underneath the request

Before drafting, identify:
1. What was the starting belief or observation?
2. What made Anshul question or modify it?
3. What concrete example, constraint, or experience carries the idea?
4. Where does he currently land?
5. Is that landing firm, or still provisional?

If the user supplied rough notes, preserve their conceptual order unless reordering is required for basic comprehension.

### Step 2 — Choose the smallest useful shape

Do not automatically create:
- a hook
- three lessons
- a takeaway
- a CTA

Choose only the structure the thought needs.

### Step 3 — Draft as forward-moving thought

Write so the reader feels the next idea emerged from the previous one.

Do not make every paragraph explain the role of the paragraph before it.

### Step 4 — Add only light publication polish

Correct obvious roughness, but do not "improve" away:
- hesitation
- contradiction
- blunt judgments
- incomplete certainty
- practical detail
- the user's original causal chain

### Step 5 — Run `ai-humanizer-core`

Invoke **`ai-humanizer-core`** as an internal final-pass dependency.

Its job is only to remove obvious AI-writing fingerprints using its two checks:

1. **Structure** — does the writing look mechanically or predictably AI-generated?
2. **Language** — does the writing sound like default AI wording rather than Anshul?

Apply the humanizer with **minimum intervention**. Patch only the spans that are genuinely AI-coded. Do not rewrite the draft simply to make it different.

**This skill remains the authority on voice.** If `ai-humanizer-core` conflicts with Anshul's intentional style, thought-development pattern, formatting preference, humour, emotion, rhythm, or wording, this skill wins.

Do not invoke `ai-humanizer-core` as the primary writing skill when the user asks Anshul to write. The user-facing writing entry point is always **`anshul-writing-style`**; the humanizer runs only inside this skill as the final de-AI pass.

### Step 6 — Check whether the ending is too perfect

Ask:
> Did the draft discover an insight, or did it manufacture a punchline?

Prefer an ending that reflects the user's current position. It may be:
- a working conclusion
- a remaining doubt
- a practical implication
- a question that genuinely remains open

Do not broaden a personal observation into a universal law unless the source material supports it.

## LinkedIn-specific rules

When writing a LinkedIn post in this voice:

- Use **few paragraph breaks**. Break when the thought changes, not after every sentence.
- Prefer 3–7 substantive paragraphs over a stack of one-line paragraphs.
- Keep the opening natural rather than clickbait-heavy.
- Use headings only when they genuinely improve comprehension.
- Use bullets only when the content is actually a list.
- Do not force emojis. If requested, use them sparingly and functionally.
- Do not force hashtags or a CTA unless the user wants them.
- If the user asks for LinkedIn-compatible bold, apply Unicode bold **after** the prose is right.
- Concision means removing repetition and generic setup, not flattening the reasoning.
- If an example can make the idea concrete, prefer the example over another paragraph of explanation.

## Editing existing drafts

When asked to make a draft "more like Anshul":

1. Do not merely make it more casual.
2. Do not add typos or slang.
3. Find where the draft sounds pre-composed.
4. Restore the actual order in which the idea developed.
5. Replace polished transitions with direct causal movement.
6. Reinsert meaningful uncertainty or counterarguments that were smoothed away.
7. Cut generic framing and generic conclusion language.
8. Preserve any sharp, specific phrasing from the user's original notes.

## Feedback interpretation

When Anshul says:

- **"too polished"** → remove smoothing and rhetorical completion; do not degrade grammar.
- **"machine generated"** → break predictable structure, remove AI connective tissue, restore thought evolution.
- **"mechanical"** → focus on the few ideas with real consequence; stop enumerating everything.
- **"make it concise"** → remove repetition, setup, and low-value explanation; keep the core reasoning.
- **"more impactful"** → strengthen the concrete tension or example; do not add hype.
- **"not me"** → compare against the thought-development rules above before changing vocabulary.
- **"too many line breaks"** → recombine into real paragraphs.
- **"copy-paste format"** → preserve the prose; change only formatting.

## Quality gate

Before returning the draft, answer these internally:

- Does this sound like someone thinking, or someone presenting a completed framework?
- Did I preserve a real change-of-mind, trade-off, or uncertainty if one existed?
- Did I add any lesson that was not in the source thought?
- Are the transitions too clean?
- Are the paragraphs too symmetrical?
- Is the ending suspiciously quotable?
- Did I confuse casual typing habits with voice?
- Could I remove 10–20% of generic setup without losing the thought?

If the answer reveals machine polish, revise once before returning.

## Priority order

When rules conflict, prioritize:

1. **User's current instruction**
2. **User's actual supplied thought/content**
3. **Thought-development fidelity**
4. **Destination requirements**
5. **Surface polish**
6. **Engagement optimization**

Never sacrifice voice fidelity merely to make a post more "LinkedIn-like."
