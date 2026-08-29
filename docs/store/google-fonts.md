# Hyle Deco — Google Fonts submission runbook

> This repo is already submission-ready. This page is the **runbook for opening the
> submission**, not a rewrite of what exists. Nothing here duplicates
> `DESCRIPTION.en_us.html`, `ISSUE_SUBMISSION.md` or `upstream.yaml`.
>
> House conventions: `Personal-Tracker/store/`. There are no graphics to produce;
> Google Fonts generates its own specimens.

## What is already done

| Requirement | State |
|---|---|
| `OFL.txt` (SIL Open Font License 1.1) | ✅ present |
| `DESCRIPTION.en_us.html` | ✅ present, written |
| `upstream.yaml` pointing at this repo | ✅ present |
| Static TTFs, Regular and Italic | ✅ `fonts/ttf/` |
| Source of truth | ✅ `sources/HyleDeco-Regular.ufo` |
| Fontbakery googlefonts profile | ✅ **zero failures**, both styles (`QA/fontbakery-final.txt`) |
| Glyph coverage | ✅ GF Latin Core, 319 of 319 |
| Submission issue text | ✅ drafted in `ISSUE_SUBMISSION.md` |
| Version | 1.024 |

## What is left

**Opening the submission.** The ASOC roster records this as "submission prepared but
not yet opened", and that is still true. It is one issue and, if you want to move
faster, one pull request.

### 1. Re-run fontbakery before filing
The committed report is a snapshot. Google Fonts checks evolve, and a report that
passed months ago can fail today on new checks. Re-run and re-commit:

```sh
pip install -U fontbakery
fontbakery check-googlefonts -x com.google.fonts/check/description/broken_links \
  fonts/ttf/*.ttf > QA/fontbakery-final.txt
```

Zero failures is the bar. Warnings are usually acceptable; read them anyway.

### 2. Verify the source round-trips
The README flags this as unverified: *"verify it round-trips with fontmake before
submitting"*. The UFO was extracted rather than authored, so confirm it actually
builds the shipped TTFs.

```sh
pip install -U fontmake
fontmake -u sources/HyleDeco-Regular.ufo -o ttf --output-dir /tmp/hyledeco-check
# then diff the metrics and glyph count against fonts/ttf/HyleDeco-Regular.ttf
```

If it does not round-trip, fix that first. Google Fonts expects the upstream source
to be the real source, and a mismatch surfaces later as an unbuildable update.

### 3. File the issue
`ISSUE_SUBMISSION.md` is ready to paste into a new issue on `google/fonts`, titled
**"Add Hyle Deco"**. It already includes the proactive name-collision disclosure
about the unrelated academic Greek face "Hyle 2.0", which is the right call and
saves a reviewer's round trip.

Confirm before filing that the repository URL in the issue is the real one
(`https://github.com/mbaliga/HyleDeco-gf`) and that the repo is **public**. A
private upstream fails immediately.

### 4. `METADATA.pb`
Not in this repo, and that is fine: Google Fonts generates it during onboarding.
If a reviewer asks for one, it is written on their side, not here. Do not
hand-author one speculatively.

### 5. Expect a slow queue
Google Fonts onboarding takes weeks to months, and the first review usually asks
for something. The common asks for a first-time family:
- a designer bio and a `designers/` entry,
- vertical-metrics adjustments,
- a hinting or `gasp` question on a hairline face, which is the likeliest one here
  given a 44-unit stroke on a 1000-unit em,
- article or specimen copy.

Answer in the issue and push fixes to this repo; the `upstream.yaml` files are what
they pull from.

## A hairline-specific risk worth knowing about

At a 44/1000 stroke, this face is close to the limit of what renders at small sizes
on low-DPI screens. Reviewers may raise it. The honest answer is that it is a
**display** face, drawn for one thin line of light carrying an identity, and it is
not proposed as a text face. `DESCRIPTION.en_us.html` already frames it that way;
keep that framing in any reply.

## Also on the roadmap, but not here

`CONSTELLATION.md` lists a planned **Hyle-fonts** repo for the design system's other
typefaces. Google Fonts requires each family to live in its own OFL-licensed repo,
which is exactly why this one is standalone. Do not merge them.
