# Hyle Deco: multi-platform porting note

> Part of the constellation porting program (`Personal-Tracker/PORTING_PROGRAM.md`, 2026-10-06). Status: PLAN, a short
> disposition note; nothing here was built, rendered or run on a device. Evidence labels: program section 2 (`PLAN`, NDV, ...).

## 1. What this repo is
A font family, not an app: a hairline display face (constant 44-unit stroke) packaged as a Google Fonts upstream: UFO 3 source in `sources/`, two
static TTFs in `fonts/ttf/` (Regular 60,184 B, Italic 70,632 B, v1.024), `upstream.yaml`, `OFL.txt`, Fontbakery reports in `QA/` (FAIL 0, WARN 27).
`README.md`: "submission ready, version 1.024". No code, UI toolkit or tests; the only workflow deletes old Actions artifacts and builds nothing.

## 2. Portable core vs platform-bound layers
All of it is platform-neutral data; no platform API appears in the tree. The implied rebuild toolchain (fontTools, fontmake,
fontbakery) is pure Python, but no build config is checked in, so no CI can regenerate the TTFs. Loading on each OS (section 4) is inferred
from TrueType being a static format; a per-OS visual check is NDV and is the consuming app's gate.

## 3. Binding rules this note must not break
- `upstream.yaml` is the Google Fonts contract: GF pulls both TTFs from `main`; do not rename, move or regenerate them. `README.md`:
  the UFO is the source of truth and must round-trip with fontmake before a submission. The approved v12 outlines (commit f9bfca4) stay.
- OFL 1.1: a modified build must be renamed. `Hyle-Design-System/TRADEMARKS.md` reserves the Hyle family names; Hyle Deco Pro is a
  different, non-GF family, never conflated. Fontbakery googlefonts profile stays at 0 FAIL (`ISSUE_SUBMISSION.md` promises it).
- Program rules: no telemetry (nothing here can phone home); environment honesty (no render was observed); colour-never-alone is
  not engaged (no UI). No em dashes in handoff prose, per the repo's deleted `tools/style_guard.py` (commit f38a073).

## 4. Target matrix (owner's order)
| Target | Feasibility | Approach | Blockers | Effort (est.) | Evidence today |
|---|---|---|---|---|---|
| Ubuntu Touch | not-applicable | A consuming click bundles the TTFs and loads them with QML `FontLoader`; no click for a font | none | 0 w | PLAN; NOT-APPLICABLE (static font) |
| Linux desktop | not-applicable | Expected to load from fontconfig or an app bundle; `.deb` or Flatpak optional, not recommended (Q5) | none | 0 w | PLAN; NOT-APPLICABLE (static font) |
| iOS / iPadOS | not-applicable | Apps embed the TTFs (`UIAppFonts` or Compose resources); no system install without a profile | none | 0 w | PLAN; NOT-APPLICABLE (static font) |
| macOS | not-applicable | Font Book install or an app bundle | none | 0 w | PLAN; NOT-APPLICABLE (static font) |
| Windows | not-applicable | Install or bundle; a `gasp` table is already present; small-size hairline legibility is a design question, not a port | none | 0 w | PLAN; NOT-APPLICABLE (static font) |

## 5. Tier and sequencing
Tier **skip** (program section 5, HyleDeco-gf row): n/a on all five targets; it joins no wave in program section 7. The row's
gate note is Q1 and Q2 below. No master OQ id covers either; Q2 is adjacent to OQ-24 (sharing non-Gradle artefacts, directive I-6).

## 6. Work breakdown
Nothing is scheduled. Two PROPOSALS, owner-gated, neither started. (a) Tag the commit Google Fonts reviews (for example `v1.024`)
so consumers cite a tag plus md5 instead of copying bytes (Q2). (b) Later, one new workflow file (R3) running fontmake and
fontbakery on `ubuntu-latest`, check-only: no commits to `fonts/ttf/`, no artifact upload (R6), est. 0.5 w, blocked on Q3.

## 7. Shared foundation
Consumes none of F1 to F12. Provides raw input only: the TTFs that `Hyle-Design-System/fonts/HyleDeco` mirrors and Typewright embeds.

## 8. Open questions for the owner
1. **Q1. Was the google/fonts PR filed?** `PR_DRAFT.md` and `METADATA.pb` were deleted at af0d761; `ISSUE_SUBMISSION.md` is still a
   draft and nothing on disk records a filing. Blocks: knowing whether `fonts/ttf/` may still change.
2. **Q2. One canonical home and pin.** Three copies diverge: here (v1.024, Regular md5 `7ab27b47...`); `Hyle-Design-System/fonts/HyleDeco`
   (TTFs md5-identical, its UFO still reads `github.com/CONFIRM/hyle-deco`); `Typewright/fonts/` (Regular 57,692 B, Italic 67,708 B, no
   GDEF or gasp). Proposed, not ruled: this repo is canonical (GF pulls from it) and consumers cite a tag. Typewright needs a written reason
   to move (point counts unverified against 1.024). `README.md` points to a design-system `CLAUDE.md` that does not exist. Blocks: any consumer pin; adjacent OQ-24.
3. **Q3. Italic source and UFO round-trip.** No Italic UFO exists anywhere; the Regular UFO still has scaffold names, weight class 400
   (TTF: 100) and VendorID `????`. Blocks: proposal (b) and the README's own round-trip condition.
4. **Q4. Complete `OFL.txt`** (it is a stub); declare "Hyle Deco" a Reserved Font Name or rely on `TRADEMARKS.md`? Blocks: filing.
5. **Q5. System font package (`.deb` or Flatpak)?** Recommendation: no; GF onboarding plus per-app bundling suffices. Blocks: nothing.

## 9. Sources read
`README.md`, `ISSUE_SUBMISSION.md`, `upstream.yaml`, `OFL.txt`, `DESCRIPTION.en_us.html`, `.github/workflows/cleanup-artifacts.yml`, `QA/fontbakery-final.txt`,
`sources/HyleDeco-Regular.ufo`, both TTFs (table directory, md5), git history; siblings `Hyle-Design-System/{fonts/HyleDeco,TRADEMARKS.md}`, `Typewright/fonts`.
