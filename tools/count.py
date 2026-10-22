"""draft/ の各場面の字数を数える。見出し行と区切り線までのヘッダ部分は数えない。"""
import glob
import re

TARGETS = {1: 3500, 2: 4500, 3: 4500, 4: 6000, 5: 4000, 6: 4500}


def body(text):
    parts = text.split("\n---\n", 1)
    return parts[1] if len(parts) == 2 else ""


total = 0
for path in sorted(glob.glob("draft/scene*.md")):
    n = int(re.search(r"scene(\d+)", path).group(1))
    count = len(re.sub(r"\s", "", body(open(path, encoding="utf-8").read())))
    total += count
    print(f"場面{n}: {count:,} / {TARGETS.get(n, 0):,}")
print(f"合計: {total:,} / {sum(TARGETS.values()):,}（上限の目安 32,000）")
