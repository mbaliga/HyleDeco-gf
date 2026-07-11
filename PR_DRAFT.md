# google/fonts submission — staged, not pushed

## Target
- Base: `google/fonts` : `main`
- Branch: `add-hyle-deco`
- Family directory: `ofl/hyledeco/`
- Commit message: `Add Hyle Deco`

## Files placed in ofl/hyledeco/
- HyleDeco-Regular.ttf
- HyleDeco-Italic.ttf
- OFL.txt
- DESCRIPTION.en_us.html
- METADATA.pb

## Draft PR title
Add Hyle Deco

## Draft PR body
**Font family name:** Hyle Deco
**Designer:** Madhav
**License:** SIL Open Font License 1.1
**Upstream repository:** https://github.com/mbaliga/hyledeco-gf
**Styles:** Regular, Italic (static, weight 400)
**Category:** Display
**Subsets:** latin, latin-ext
**Glyph coverage:** GF Latin Core

Hyle Deco is a hairline deco display face built on a constant 44 unit stroke,
drawn from hand made vector letterforms. The single upright weight is filed as
the family Regular per the Google Fonts single-weight-families spec.

Fontbakery (googlefonts profile) passes with zero failures on both styles. gasp, weight class, naming, and combining-mark attachment were corrected during finishing; the full report is in the upstream repository's QA/ folder.

Disclosure: a niche academic Greek typeface named "Hyle 2.0" exists elsewhere.
It is not on Google Fonts, is unrelated in design and origin, and the two-word
name "Hyle Deco" is distinct. Raised proactively to save reviewer time.

## Exact steps for you to push (I did not push, per instruction)
```
# 1. Fork google/fonts on GitHub (if not already forked), then:
git clone https://github.com/<you>/fonts.git && cd fonts
git remote add upstream https://github.com/google/fonts.git
git fetch upstream && git checkout -b add-hyle-deco upstream/main

# 2. Copy the family in (from the hyledeco-gf checkout):
mkdir -p ofl/hyledeco
cp <hyledeco-gf>/fonts/ttf/HyleDeco-Regular.ttf ofl/hyledeco/
cp <hyledeco-gf>/fonts/ttf/HyleDeco-Italic.ttf  ofl/hyledeco/
cp <hyledeco-gf>/OFL.txt <hyledeco-gf>/DESCRIPTION.en_us.html <hyledeco-gf>/METADATA.pb ofl/hyledeco/

# 3. Commit + push + open the PR against google/fonts:main
git add ofl/hyledeco
git commit -m "Add Hyle Deco"
git push -u origin add-hyle-deco
```
