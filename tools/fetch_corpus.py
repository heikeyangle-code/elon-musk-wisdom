#!/usr/bin/env python3
"""
从原始出处抓取语料，重建成技能期望的扁平文件名。

用法：
    python3 tools/fetch_corpus.py --out ~/.pi/agent/skills/elon-musk-wisdom/corpus
    python3 tools/fetch_corpus.py --out ./corpus --from-cache ~/我的网页存档

为什么需要这个脚本：
    本仓库不分发第三方语料（见 THIRD-PARTY.md）。技能里的引文都带
    `corpus/<文件名>` 出处，要对得上，你得自己把语料取回来。
    脚本读 tools/corpus-sources.json（258 条来源清单），
    逐条抓取并保存成技能期望的文件名。

依赖：无（只用标准库）。若装了 requests / beautifulsoup4 会自动用，取不到则退回 urllib。
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
SOURCES = HERE / "corpus-sources.json"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0 Safari/537.36"
)
DELAY = 1.5          # 每次请求之间的间隔秒数，别把人家站点打垮
TIMEOUT = 40


def clean_html(raw: str) -> str:
    """从 HTML 里抠出正文文本。优先用 bs4，没有就退回正则。"""
    try:
        from bs4 import BeautifulSoup  # type: ignore
        soup = BeautifulSoup(raw, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text("\n")
    except Exception:
        text = re.sub(r"(?is)<(script|style|nav|footer|header|aside)[^>]*>.*?</\1>", " ", raw)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = re.sub(r"&nbsp;?", " ", text)
        text = re.sub(r"&amp;", "&", text)
        text = re.sub(r"&lt;", "<", text)
        text = re.sub(r"&gt;", ">", text)
        text = re.sub(r"&#39;|&apos;", "'", text)
        text = re.sub(r"&quot;", '"', text)
    lines = [ln.strip() for ln in text.splitlines()]
    out, blank = [], 0
    for ln in lines:
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        out.append(ln)
    return "\n".join(out).strip()


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en,zh;q=0.8"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        raw = r.read()
        charset = r.headers.get_content_charset() or "utf-8"
    html = raw.decode(charset, errors="replace")
    if "<html" in html[:2000].lower() or "<!doctype" in html[:2000].lower():
        return clean_html(html)
    return html


def main() -> int:
    ap = argparse.ArgumentParser(description="抓取马斯克技能所需的原始语料")
    ap.add_argument("--out", required=True, help="输出目录（技能的 corpus/）")
    ap.add_argument("--from-cache", help="可选：先从本地缓存目录找同名文件，找到就跳过联网")
    ap.add_argument("--only", help="只抓文件名包含该子串的条目")
    ap.add_argument("--delay", type=float, default=DELAY, help=f"请求间隔，默认 {DELAY}s")
    ap.add_argument("--dry-run", action="store_true", help="只列出会抓什么，不联网")
    a = ap.parse_args()

    out = pathlib.Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    cache = pathlib.Path(a.from_cache).expanduser() if a.from_cache else None

    rows = json.loads(SOURCES.read_text(encoding="utf-8"))
    if a.only:
        rows = [r for r in rows if a.only in r["file"]]

    ok = skip = fail = nolink = 0
    missing: list[dict] = []

    for i, r in enumerate(rows, 1):
        target = out / r["file"]
        tag = f"[{i}/{len(rows)}] {r['file'][:58]}"

        if target.exists() and target.stat().st_size > 400:
            print(f"  跳过（已有）  {tag}")
            skip += 1
            continue

        if cache:
            for cand in cache.rglob(pathlib.Path(r["file"]).name):
                target.write_bytes(cand.read_bytes())
                print(f"  取自缓存      {tag}")
                skip += 1
                break
            else:
                pass
            if target.exists():
                continue

        if not r.get("url"):
            print(f"  无来源 URL    {tag}")
            nolink += 1
            missing.append(r)
            continue

        if a.dry_run:
            print(f"  将抓取        {tag}\n                 {r['url']}")
            continue

        try:
            text = fetch(r["url"])
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            print(f"  失败          {tag}  —— {e}")
            fail += 1
            missing.append(r)
            time.sleep(a.delay)
            continue

        header = f"# SOURCE: {r['url']}\n"
        if r.get("title"):
            header += f"# TITLE: {r['title']}\n"
        header += "# FETCHED: fetch_corpus.py\n\n"
        target.write_text(header + text, encoding="utf-8")

        print(f"  已抓取 {len(text):>8,} 字  {tag}")
        ok += 1
        time.sleep(a.delay)

    print(f"\n  完成：新抓 {ok} / 跳过 {skip} / 无链接 {nolink} / 失败 {fail}")
    if missing:
        p = out.parent / "corpus-missing.json"
        p.write_text(json.dumps(missing, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  未取得的条目已记录到 {p}")
        print("  这几份没 URL 的多为出版物（传记、书籍），请自行合法获取后放进 corpus/：")
        for r in missing[:10]:
            print(f"    · {r['file']}   {r.get('title') or ''}")
    if skip < len(rows):
        print("\n  提示：把所有文件凑齐后，用 --only 可只补缺失的那几条。")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
