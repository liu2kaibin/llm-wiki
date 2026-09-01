#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""arXiv → Obsidian 论文笔记生成器。

用法:
    python arxiv_note.py 1706.03762 [more_id ...] [domain=<领域>]

仅用标准库，无第三方依赖。从 arXiv API 抓取元数据，
在 content/20-Papers/ 生成论文卡（标题作为文件名）。
已存在同名文件时跳过，避免覆盖。
domain 参数可选（如 domain=database），默认留空。
"""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent / "content"
PAPERS_DIR = VAULT / "20-Papers"
API = "http://export.arxiv.org/api/query?id_list={ids}&max_results={n}"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


def fetch(ids: list[str]) -> str:
    url = API.format(ids=",".join(ids), n=len(ids))
    req = urllib.request.Request(url, headers={"User-Agent": "llm-wiki-seeder/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def clean(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r'[<>:"/\\|?*]', " ", s)


def parse(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    papers = []
    for entry in root.findall("atom:entry", NS):
        arxiv_id = entry.findtext("atom:id", "", NS).rsplit("/", 1)[-1]
        title = clean(entry.findtext("atom:title", "", NS))
        if not title:
            continue
        authors = [a.findtext("atom:name", "", NS) for a in entry.findall("atom:author", NS)]
        published = entry.findtext("atom:published", "", NS)[:10]
        abstract = clean(entry.findtext("atom:summary", "", NS))
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "published": published,
            "year": published[:4],
            "abstract": abstract,
        })
    return papers


TPL = """---
type: paper
domain: "{domain}"
tags:
  - paper
status: seed
created: {created}
authors: [{authors}]
year: {year}
arxiv: "{arxiv_id}"
url: "https://arxiv.org/abs/{arxiv_id}"
venue: ""
---
# {title}

> [!abstract] 一句话结论
> （读完再写）

## 摘要速览

{abstract}

## 解决的问题

## 核心方法

## 关键结果

## 为什么重要 / 对我有什么用

## 局限与后续

## 相关笔记
- 

## 出处
- https://arxiv.org/abs/{arxiv_id}
- 作者：{author_str}
- 发布：{published}
"""


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    domain = ""
    ids = []
    for a in sys.argv[1:]:
        if a.startswith("domain="):
            domain = a.split("=", 1)[1].strip().lower()
        else:
            ids.append(re.sub(r"v\d+$", "", a))
    xml_text = fetch(ids)
    papers = parse(xml_text)
    if not papers:
        print("未从 arXiv 返回任何条目，请检查 ID。")
        sys.exit(2)
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    created = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d")
    for p in papers:
        path = PAPERS_DIR / f"{p['title']}.md"
        if path.exists():
            print(f"跳过（已存在）: {path.name}")
            continue
        author_list = "、".join(p["authors"])
        content = TPL.format(
            created=created,
            domain=domain,
            authors=", ".join(f'"{a}"' for a in p["authors"]),
            author_str=author_list,
            year=p["year"],
            arxiv_id=p["arxiv_id"],
            title=p["title"],
            abstract=p["abstract"],
            published=p["published"],
        )
        path.write_text(content, encoding="utf-8")
        print(f"已生成: {path.name}  ({len(p['authors'])} 位作者, {p['published']})")


if __name__ == "__main__":
    main()
