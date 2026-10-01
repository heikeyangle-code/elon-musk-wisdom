<div align="center">

# Elon Musk Wisdom · An Operating System for Thinking

**Not a quote collection. A cognitive operating system with stated failure boundaries.**

11 principles · 275 situational playbook sections · 147 computational procedures · 132 verifiable cases · 1,113 verbatim evidence cards

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![Verified](https://img.shields.io/badge/verbatim%20check-1319%2F1319-brightgreen)](docs/BUILD-NOTES.md)
[![Corpus](https://img.shields.io/badge/corpus-258%20files%20%2F%209.2M%20chars-9cf)](skills/elon-musk-wisdom/corpus)

</div>

---

## What this actually is

Most "Elon Musk skills" work like this: **take what he said, sort it by topic, ship a quote library.** You ask a question, it pastes a few punchy lines back.

**This one is different.** It decomposes how Musk thinks into **four retrievable, verifiable layers — each carrying its own boundaries:**

| Layer | What it is | Size | Question it answers |
|---|---|---|---|
| **Principles** | How he sees the world | 11 | "Manufacturing is harder than design" |
| **Situational playbook** | What to do when you hit a specific situation | **275 sections** | "Production is stuck — now what?" |
| **Computational procedures** | What to compute first, what to compare against, when to stop | **147 entries** | "How deep should I break down this cost?" |
| **Cases** | Real precedents with outcomes | **132** | "Last time something like this happened, how did it end?" |
| **Evidence** | Verbatim quotes + source + confidence | **1,113 cards** | "Did he actually say that?" |

**Scale, against another open-sourced Musk skill:** principles 11 vs 5 · cases 132 vs 0 · procedures 147 vs 8 · verbatim evidence cards 1,113 vs 0 · raw corpus 258 files vs 0.

---

## Three design decisions that separate this from the rest

### 1 · Every method carries a **failure boundary**

This is the most commonly skipped — and the most important — part.

Most skills tell you *when to use* something. **This one tells you when not to.**

Take the "cost shape" test — he asks, `If our volume was a million units per year, would it still be expensive?` That test only holds in industries where **unit cost falls with volume**. He was building rockets when he said it. Apply it to a one-person craft business deciding whether to scale, and you get exactly the wrong answer.

So all 147 procedures state: **in what structure, at what magnitude, this will lie to you.**

> A mechanism that doesn't know its own boundary is more dangerous than no mechanism at all — it lets you execute a wrong answer with total conviction.

### 2 · The corpus is **evidence, not content**

There's a hard rule baked into the skill:

> **Borrow my judgment, not my biography.**
> You're asking about *your* situation, so the subject of the sentence has to be you.
> **Self-check:** replace every "I" in the answer with "he."
> If the sentence still holds → it's a judgment. If it collapses → it's just biography.

**This rule is what makes "Musk" actually borrowable.** A real mentor doesn't hand you his legend as your answer — he hands you the judgment and keeps the story as evidence.

### 3 · **No brute-force reading — routing and indexes**

275 playbook sections live in a 386 KB file. **Without an index, any model reads only ~13% of it (file readers truncate).**

So every large file opens with a **hand-built index**:

- `playbooks.md` → a **272-row section index**, each row stating "what question does this section answer"
- `cases.md` → a **132-row case index**
- `SKILL.md` → a **routing table** mapping "money / people / judgment / personal state" straight to section numbers

**Measured result:** with this structure, a model performed 17 file operations — all `grep`-locate plus `sed`-extract, **zero whole-file reads** — and landed precisely on the sections it needed.

---

## What's inside

### 11 principles
Each with: claim · mechanism · verbatim quote · failure boundary · concrete action.

First principles / Physics is the law / The five-step algorithm / The best part is no part / The idiot index / The machine that builds the machine / Question the requirement / Assume you're wrong / Thinking in limits / Hardcore cadence / Back up civilization.

Plus a **ten-gate decision filter** (each gate a decidable yes/no; any "no" stops the process) and **9 distinct reasoning patterns** (S-curve positioning · attack the constraint, not the average · conjunctive probability · complexity compounds · look at the artifact, not the effort · physical ceiling ≠ demand · reconcile the numbers first).

### 275 situational sections
From "what business to start" to "what to do when you're under attack," from "how to learn a new field" to "how to rank civilization-scale risks."

**Each section states four things:** when to use it · what he said (verbatim) · what it means · when it doesn't hold.

### 147 computational procedures
**Blind testing proved this is the highest-value layer.**

The finding: models could restate Musk's *opinions* after reading a skill, **but couldn't perform his *actions*.** This layer exists to close that gap.

Each entry: trigger → his words → numbered actions → failure boundary.

Examples: `Separate "build one" from "build ten thousand"` · `Kill serial dependencies before talking about speed` · `Make the person who decides and the person who understands the same person`.

### 132 verifiable cases
Each with situation, decision, outcome (including numbers), and **counter-example flags** — moments where a principle failed, a cost came due, or he publicly admitted a misjudgment. **The counter-examples are worth more than the successes.**

### 1,113 verbatim evidence cards
Each with one quote, its source, its position in the corpus, and a confidence level.

**Two confidence tiers:** `high` = in his own words (interviews, talks, official documents); `medium` = third-party paraphrase (biographies, book reviews, others' compilations).

**State the tier when you quote.** A `medium` line must not be presented as something he wrote.

### 70 voice samples + an expression-DNA profile
Sentence patterns, certainty calibration (absolute claims on physics, heavy hedging on timelines), humor register, forbidden vocabulary, paragraph rhythm.

### Stated blind spots and internal contradictions
The skill **documents its own limits and contradictions**:

- Timeline optimism is systematic — he admits it, and the skill marks his years as unusable
- The method is near-invincible in physical systems and **fails in human systems**
- **3 documented internal contradictions** — the same decision, two mutually exclusive accounts. They are *not* reconciled. Both are kept, with a warning not to treat either as a template.

---

## Install

### Pi

```bash
git clone https://github.com/<your-username>/elon-musk-wisdom ~/.pi/agent/skills/elon-musk-wisdom
```

### Claude Code / any agentskills.io-compatible runtime

Copy `skills/elon-musk-wisdom/` into that runtime's skills directory.

```
<runtime>/skills/elon-musk-wisdom/
├── SKILL.md
├── references/       ← 7 markdown files
└── corpus/           ← fetch it yourself (see below)
```

### The corpus **ships with the repo**

**258 source files / 9.2M characters / 1971–2026** — working immediately after clone.

```
corpus/   258 .txt files
```

All **2,079** `corpus/xxx.txt` references inside the skill resolve. Want the full context around any quote? Open the file directly.

**Integrity check:**

```bash
python3 tools/verify_corpus.py --dir skills/elon-musk-wisdom/corpus
```

Compares your copy against `tools/corpus-checksums.json` (filename, byte count, md5 per file).

**If files are missing or you want to re-fetch** (e.g. a source was updated upstream):

```bash
python3 tools/fetch_corpus.py --out skills/elon-musk-wisdom/corpus
```

Reads `tools/corpus-sources.json` (**254 of 258 entries carry their original URL**).

**On copyright, see [THIRD-PARTY.md](THIRD-PARTY.md)** — the material belongs to its original rights holders. This repo gathers it for research and citation purposes only.

---

## Verified facts

Not adjectives. Reproducible checks.

| Check | Result |
|---|---|
| **Verbatim quote audit** | **1,319 / 1,319 = 100%** (deterministic script, normalized-corpus substring match) |
| Corpus path resolution | 581 path references — **all resolvable, 0 dangling** |
| Terminology consistency | `原则 N` / `节 N` / `M N` / `案例 N` / `证据卡 N` — **zero mixing** |
| Corpus coverage | **258 files / 9.24M characters / 1971–2026** |
| Artifact integrity | 7 output files — **hashes match the installed package** |

The build process and every trap hit along the way are recorded in [`docs/BUILD-NOTES.md`](docs/BUILD-NOTES.md) (26 tool defects and their fixes). Architecture decisions are in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

---

## What this does NOT do (honestly)

**0 · The corpus is not ours to license.** The 258 files come from biographies, podcast transcripts, media reports, and official documents — copyright belongs to their original holders. This repo gathers them for research and citation. **It does not grant you the right to redistribute them.** For commercial use, verify each source's terms yourself.

**1 · The persona layer has holes.** Humor, anger, excitement, sarcasm, forms of address, public admissions of error, how he pushes back — these seven dimensions have **no dedicated samples**. Of the 70 voice samples, the count of laughter markers is zero. The expression-DNA section claims "humor: dry, deadpan, self-deprecating," but nothing backs it.

**2 · Playbook failure-boundary coverage is incomplete.** Procedures are 147/147 covered; the playbook is only 20/272. **This is the next thing to fix.**

**3 · Capability boundary.** Its corpus contains **nothing** about county-town small business, local social capital, or industry insider norms. **It is strong on resource allocation, cost structure, organization, trade-offs under decline, and high-pressure decisions. It knows nothing about how the street you live on actually works.**

**4 · English sources, Chinese framework.** Quotes are English originals; the framework and indexes are Chinese.

---

## How it was built

Built with the [Mind-Distill-Factory](https://github.com/) pipeline. All six gates pass (sources → principles → frameworks → skill → package → gallery).

**Core practice:** every quote is **sliced out of the corpus by anchor** rather than typed by hand, then re-checked by an independent script. **Changing one word in a quote fails the gate.**

The package documents 26 tool defects (F1–F26), including three textbook cases of *"the gate reported success but checked nothing"*:

- The P3 path gate never scanned `references/*.md`
- Its character class excluded CJK → every Chinese corpus filename was invisible
- Its regex excluded spaces → **and every corpus filename contains spaces**

**The lesson is written into the code:** a gate reporting "pass" is not evidence it checked anything. After adding any file, **count how many paths it actually scanned** — don't read its expression.

---

## License

**MIT** — covering this repo's original work (SKILL.md, the distilled text under `references/`, `tools/`, `docs/`).

**Third-party source material is not included** and is not distributed here. See [THIRD-PARTY.md](THIRD-PARTY.md).

This is an independent research project. It is **not affiliated with, authorized by, or endorsed by** Elon Musk or any of his companies.

---

<div align="center">

*"Like physics is the law, everything else is a recommendation."*

[中文 README →](README.md)

</div>
