#!/usr/bin/env python3
"""
校验本地语料与仓库发布的版本是否一致。

用法：
    python3 tools/verify_corpus.py --dir skills/elon-musk-wisdom/corpus
    python3 tools/verify_corpus.py --dir ./corpus --quiet

对照 tools/corpus-checksums.json（258 份文件的名字、字节数、md5）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
MANIFEST = HERE / "corpus-checksums.json"


def main() -> int:
    ap = argparse.ArgumentParser(description="校验语料完整性")
    ap.add_argument("--dir", required=True, help="corpus 目录")
    ap.add_argument("--quiet", action="store_true", help="只输出汇总")
    a = ap.parse_args()

    if not MANIFEST.exists():
        print(f"  ✗ 找不到校验清单 {MANIFEST}", file=sys.stderr)
        return 2

    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    d = pathlib.Path(a.dir).expanduser()

    missing: list[str] = []
    changed: list[str] = []
    ok = 0

    for r in man["files"]:
        p = d / r["file"]
        if not p.exists():
            missing.append(r["file"])
            continue
        b = p.read_bytes()
        if len(b) != r["bytes"] or hashlib.md5(b).hexdigest() != r["md5"]:
            changed.append(r["file"])
        else:
            ok += 1

    extra = sorted(
        p.name for p in d.glob("*.txt")
        if p.name not in {r["file"] for r in man["files"]}
    )

    total = man["count"]
    if not a.quiet:
        for f in missing:
            print(f"  ✗ 缺失   {f}")
        for f in changed:
            print(f"  ✗ 不一致 {f}")
        for f in extra:
            print(f"  + 多出   {f}")

    print(f"\n  语料校验：{ok}/{total} 一致", end="")
    if missing:
        print(f" / {len(missing)} 缺失", end="")
    if changed:
        print(f" / {len(changed)} 被改动", end="")
    if extra:
        print(f" / {len(extra)} 多出", end="")
    print()

    if ok == total:
        print("  ✅ 与仓库发布版本逐字节一致")
        return 0
    if missing and not changed:
        print("  补全方式：python3 tools/fetch_corpus.py --out " + str(d))
    return 1


if __name__ == "__main__":
    sys.exit(main())
