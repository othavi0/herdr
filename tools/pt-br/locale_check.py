"""Structural checks for a translated docs locale against the English source.

Checks per page: frontmatter keys, import lines, fenced code blocks, internal
link targets, and that every in-locale anchor resolves to a heading slug.
Usage: python3 locale_check.py --docs-root <dir> --locale pt-br [--files a.mdx,b.mdx]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FENCE = re.compile(r"^(```+|~~~+)")
LINK = re.compile(r"\]\(([^)\s]+)\)|link:\s*(\S+)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def split_frontmatter(text: str) -> tuple[str, str]:
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        return text[4:end], text[end + 5 :]
    return "", text


def fm_keys(fm: str) -> list[str]:
    return [line.split(":", 1)[0].strip() for line in fm.splitlines() if re.match(r"^\s*[\w-]+:", line)]


def code_blocks(body: str) -> list[str]:
    blocks, cur, fence = [], None, None
    for line in body.splitlines():
        m = FENCE.match(line.strip())
        if cur is None and m:
            cur, fence = [], m.group(1)
        elif cur is not None and line.strip().startswith(fence) and line.strip().strip(fence[0]) == "":
            blocks.append("\n".join(cur))
            cur = None
        elif cur is not None:
            cur.append(line)
    return blocks


def prose_lines(body: str) -> list[str]:
    out, in_code = [], False
    for line in body.splitlines():
        if FENCE.match(line.strip()):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    return out


def slugify(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("`", "").replace("*", "")
    text = text.lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def heading_slugs(body: str) -> set[str]:
    seen: dict[str, int] = {}
    slugs = set()
    for line in prose_lines(body):
        m = HEADING.match(line)
        if not m:
            continue
        base = slugify(m.group(2))
        n = seen.get(base, 0)
        seen[base] = n + 1
        slugs.add(base if n == 0 else f"{base}-{n}")
    return slugs


def links(body: str, fm: str) -> list[str]:
    found = []
    for line in prose_lines(body) + fm.splitlines():
        for m in LINK.finditer(line):
            found.append(m.group(1) or m.group(2))
    return [t for t in found if t.startswith(("/", "#"))]


def normalize(target: str, locale: str) -> str:
    target = target.split("#", 1)[0]
    prefix = f"/{locale}/"
    return "/" + target[len(prefix) :] if target.startswith(prefix) else target


INLINE = re.compile(r"(`+)(.+?)\1")


def inline_code(body: str) -> list[str]:
    return sorted(m.group(2) for line in prose_lines(body) for m in INLINE.finditer(line))


def inline_code_warnings(en_path: Path, loc_path: Path) -> list[str]:
    from collections import Counter
    en = Counter(inline_code(split_frontmatter(en_path.read_text())[1]))
    lo = Counter(inline_code(split_frontmatter(loc_path.read_text())[1]))
    out = []
    for k in sorted(set(en) | set(lo)):
        if en[k] != lo[k]:
            out.append(f"{loc_path.name}: inline code `{k}` appears {en[k]}x in English, {lo[k]}x in translation")
    return out


def check_page(en_path: Path, loc_path: Path, locale: str, docs_root: Path) -> list[str]:
    errs: list[str] = []
    en_fm, en_body = split_frontmatter(en_path.read_text())
    lo_fm, lo_body = split_frontmatter(loc_path.read_text())
    name = loc_path.name

    if fm_keys(en_fm) != fm_keys(lo_fm):
        errs.append(f"{name}: frontmatter keys differ: {fm_keys(en_fm)} vs {fm_keys(lo_fm)}")

    en_imports = [l for l in en_body.splitlines() if l.startswith("import ")]
    lo_imports = [l for l in lo_body.splitlines() if l.startswith("import ")]
    expected = [l.replace("'../", "'../../").replace('"../', '"../../') for l in en_imports]
    if lo_imports != expected:
        errs.append(f"{name}: imports differ: expected {expected}, got {lo_imports}")

    en_code, lo_code = code_blocks(en_body), code_blocks(lo_body)
    if len(en_code) != len(lo_code):
        errs.append(f"{name}: code block count {len(en_code)} (en) vs {len(lo_code)}")
    else:
        for i, (a, b) in enumerate(zip(en_code, lo_code), 1):
            if a != b:
                errs.append(f"{name}: code block {i} differs from English")

    en_links = sorted(normalize(t, locale) for t in links(en_body, en_fm))
    lo_links = links(lo_body, lo_fm)
    if en_links != sorted(normalize(t, locale) for t in lo_links):
        errs.append(f"{name}: link targets differ (ignoring anchors): en={en_links} {locale}={sorted(normalize(t, locale) for t in lo_links)}")

    for t in lo_links:
        path = t.split("#", 1)[0]
        if path.startswith("/docs/"):
            errs.append(f"{name}: link {t} points to the English page, expected /{locale}{path}")
        for other in ("/ja/", "/zh-cn/"):
            if path.startswith(other) and other != f"/{locale}/":
                errs.append(f"{name}: link {t} points to another locale")
        if "#" in t and path.startswith(f"/{locale}/docs/"):
            anchor = t.split("#", 1)[1]
            page = path[len(f"/{locale}/docs/") :].strip("/")
            target = docs_root / locale / f"{page or 'index'}.mdx"
            if not target.exists():
                errs.append(f"{name}: link {t} targets missing page {target.name}")
                continue
            if anchor not in heading_slugs(split_frontmatter(target.read_text())[1]):
                errs.append(f"{name}: anchor #{anchor} not found in {locale}/{target.name}")
        if t.startswith("#"):
            if t[1:] not in heading_slugs(lo_body):
                errs.append(f"{name}: same-page anchor {t} not found")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs-root", type=Path, required=True)
    ap.add_argument("--locale", required=True)
    ap.add_argument("--files", default="")
    ap.add_argument("--inline-code", action="store_true", help="also list inline code count differences as warnings")
    args = ap.parse_args()
    root: Path = args.docs_root
    names = [f for f in args.files.split(",") if f] or sorted(p.name for p in root.glob("*.mdx"))
    errs: list[str] = []
    for n in names:
        loc = root / args.locale / n
        if not loc.exists():
            errs.append(f"{n}: missing in {args.locale}")
            continue
        errs += check_page(root / n, loc, args.locale, root)
        if args.inline_code:
            for w in inline_code_warnings(root / n, loc):
                print("warning:", w)
    for e in errs:
        print(e)
    print(f"{len(names)} pages checked, {len(errs)} problems")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
