"""Rename one heading in a locale page and rewrite every anchor that points to it.

Usage: python3 rename_heading.py --docs-root <dir> --locale pt-br --page socket-api \
         --old "Relatório de estado do agente" --new "Informe de estado do agente"
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from locale_check import slugify  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs-root", type=Path, required=True)
    ap.add_argument("--locale", required=True)
    ap.add_argument("--page", required=True)
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    a = ap.parse_args()
    loc_dir = a.docs_root / a.locale
    page = loc_dir / f"{a.page}.mdx"
    text = page.read_text()
    pattern = re.compile(rf"^(#{{1,6}})\s+{re.escape(a.old)}[ \t]*$", re.M)
    if len(pattern.findall(text)) != 1:
        print(f"expected exactly one heading '{a.old}' in {page.name}")
        return 1
    page.write_text(pattern.sub(lambda m: f"{m.group(1)} {a.new}", text))

    old_slug, new_slug = slugify(a.old), slugify(a.new)
    cross = f"/{a.locale}/docs/{a.page}/#{old_slug}"
    count = 0
    for f in sorted(loc_dir.glob("*.mdx")):
        t = f.read_text()
        n = t.replace(cross + ")", f"/{a.locale}/docs/{a.page}/#{new_slug})")
        if f == page:
            n = n.replace(f"](#{old_slug})", f"](#{new_slug})")
        if n != t:
            count += t.count(cross + ")") + (t.count(f"](#{old_slug})") if f == page else 0)
            f.write_text(n)
    print(f"heading renamed, {count} anchors rewritten (#{old_slug} -> #{new_slug})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
