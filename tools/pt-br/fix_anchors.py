"""Rewrite English anchors in a translated locale to the translated heading slugs.

Heading outlines match between English and the locale (parity check), so the
i-th heading of an English page maps to the i-th heading of its translation.
Safe to rerun: anchors that already resolve are left alone.
Usage: python3 fix_anchors.py --docs-root <dir> --locale pt-br
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from locale_check import HEADING, prose_lines, slugify, split_frontmatter  # noqa: E402


def slug_list(path: Path) -> list[str]:
    seen: dict[str, int] = {}
    out = []
    for line in prose_lines(split_frontmatter(path.read_text())[1]):
        m = HEADING.match(line)
        if not m:
            continue
        base = slugify(m.group(2))
        n = seen.get(base, 0)
        seen[base] = n + 1
        out.append(base if n == 0 else f"{base}-{n}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs-root", type=Path, required=True)
    ap.add_argument("--locale", required=True)
    args = ap.parse_args()
    root: Path = args.docs_root
    loc = args.locale
    link = re.compile(rf"(\]\(|link:\s*)(/{re.escape(loc)}/docs/([^)#\s]*)|)#([^)\s]+)")
    fixed = unresolved = 0
    for page in sorted((root / loc).glob("*.mdx")):
        text = page.read_text()

        def repl(m: re.Match[str]) -> str:
            nonlocal fixed, unresolved
            target = m.group(3).strip("/") if m.group(2) else page.stem
            anchor = m.group(4)
            loc_file, en_file = root / loc / f"{target or 'index'}.mdx", root / f"{target or 'index'}.mdx"
            if not loc_file.exists() or not en_file.exists():
                return m.group(0)
            loc_slugs = slug_list(loc_file)
            if anchor in loc_slugs:
                return m.group(0)
            en_slugs = slug_list(en_file)
            if anchor not in en_slugs or len(en_slugs) != len(loc_slugs):
                unresolved += 1
                print(f"{page.name}: cannot map #{anchor} to {loc}/{loc_file.name}")
                return m.group(0)
            fixed += 1
            return m.group(0)[: -len(anchor)] + loc_slugs[en_slugs.index(anchor)]

        lines, in_code = [], False
        for line in text.split("\n"):
            if line.lstrip().startswith(("```", "~~~")):
                in_code = not in_code
            lines.append(line if in_code or line.lstrip().startswith(("```", "~~~")) else link.sub(repl, line))
        new = "\n".join(lines)
        if new != text:
            page.write_text(new)
    print(f"{fixed} anchors rewritten, {unresolved} unresolved")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
