import sys, re, glob
BANNED = {
    "em_dash": r"\u2014",
    "en_dash_as_sep": r"\s\u2013\s",
    "curly_apos_in_prose": None,  # allow in font data, flag in md only
}
TELLS = [
    r"\bit'?s worth noting\b", r"\bdelve\b", r"\bdelves\b", r"\btapestry\b",
    r"\bin conclusion\b", r"\bfurthermore\b", r"\bmoreover\b",
    r"\bnavigat(e|ing) the\b", r"\bin the (?:ever-)?evolving\b",
    r"\bunlock(?:ing)? the\b", r"\ba testament to\b", r"\bunderscore(?:s|d)?\b",
    r"\bboast(?:s|ing)?\b", r"\bseamless(?:ly)?\b", r"\brobust\b",
    r"\bleverag(?:e|ing)\b", r"\brealm\b", r"\bplethora\b",
    r"\bfoster(?:ing)?\b", r"\bwhether you'?re\b", r"\bnot only\b.*\bbut also\b",
    r"\bempower(?:s|ing|ed)?\b", r"\bfacilitat(?:e|es|ing)\b",
    r"\bcrucial\b", r"\bvital\b", r"\bcomprehensive\b",
    r"::contentReference", r"\bat the end of the day\b",
]
issues=[]
for path in glob.glob("handoff/**/*.md", recursive=True)+glob.glob("handoff/**/*.txt", recursive=True):
    txt=open(path,encoding="utf-8").read()
    for i,line in enumerate(txt.splitlines(),1):
        if "\u2014" in line:
            issues.append(f"{path}:{i} EM DASH: {line.strip()[:70]}")
        if re.search(r"\s\u2013\s", line):
            issues.append(f"{path}:{i} EN DASH SEP: {line.strip()[:70]}")
        for pat in TELLS:
            if re.search(pat, line, re.I):
                issues.append(f"{path}:{i} TELL /{pat}/: {line.strip()[:60]}")
if issues:
    print("STYLE ISSUES:\n"+"\n".join(issues)); sys.exit(1)
print("style_guard: clean (no em dashes, no en-dash separators, no AI tells)")
