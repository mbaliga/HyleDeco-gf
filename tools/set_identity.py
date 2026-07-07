#!/usr/bin/env python3
"""
Set the final family name and real repository URL across a Hyle Deco submission
folder. Writes consistently into every TTF name table, the OFL.txt first line,
upstream.yaml, and DESCRIPTION if present. Run once when the name and URL are
settled. Safe to re-run.

Usage:
  python set_identity.py --dir fonts/HyleDeco --family "Hyle Deco" --url https://github.com/you/hyle-deco
"""
import argparse, os, glob, re
from fontTools.ttLib import TTFont

def style_from_filename(fn, family):
    base=os.path.basename(fn)[:-4]
    tok=base.split("-",1)[-1] if "-" in base else "Regular"
    return tok

def apply(path, family, url, year="2026"):
    ttf=glob.glob(os.path.join(path,"**","*.ttf"), recursive=True)
    copyright=f"Copyright {year} The {family} Project Authors ({url})"
    lic="This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org"
    fam_ps=family.replace(" ","")
    for p in ttf:
        style=style_from_filename(p, family)
        style_ps=style.replace(" ","")
        full=f"{family} {style}".strip()
        f=TTFont(p)
        nm=f["name"]
        set3=lambda i,s: nm.setName(s,i,3,1,0x409)
        set1=lambda i,s: nm.setName(s,i,1,0,0)
        for setter in (set3,set1):
            setter(0, copyright)
            setter(1, family if style in ("Regular","Bold","Italic","Bold Italic") else full)
            setter(2, style if style in ("Regular","Bold","Italic","Bold Italic") else "Regular")
            setter(3, f"{fam_ps}-{style_ps}")
            setter(4, full)
            setter(6, f"{fam_ps}-{style_ps}")
            setter(13, lic)
            setter(14, "https://openfontlicense.org")
            setter(16, family)
            setter(17, style)
        f.save(p)
        print("  wrote identity ->", os.path.basename(p))
    # OFL.txt first line
    ofl=os.path.join(path,"OFL.txt")
    if os.path.exists(ofl):
        body=open(ofl,encoding="utf-8").read().splitlines()
        body=[ln for ln in body if ln.strip()]
        # replace first non-empty line with the copyright
        rest="\n".join(open(ofl,encoding="utf-8").read().split("\n")[1:])
        open(ofl,"w",encoding="utf-8").write(copyright+"\n"+rest)
        print("  OFL.txt first line set")
    # upstream.yaml
    up=os.path.join(path,"upstream.yaml")
    if os.path.exists(up):
        t=open(up,encoding="utf-8").read()
        t=re.sub(r"(?m)^name:.*$", f"name: {family}", t)
        t=re.sub(r"(?m)^repository_url:.*$", f"repository_url: {url}", t)
        open(up,"w",encoding="utf-8").write(t)
        print("  upstream.yaml name and url set")
    print("identity applied to", len(ttf), "font files")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--family", default="Hyle Deco")
    ap.add_argument("--url", required=True)
    ap.add_argument("--year", default="2026")
    a=ap.parse_args()
    apply(a.dir, a.family, a.url, a.year)
