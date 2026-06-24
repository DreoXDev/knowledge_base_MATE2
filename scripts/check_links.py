from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def normalize(name: str) -> str:
    name = name.strip()
    if "/" in name or "\\" in name:
        name = Path(name).stem
    return name.lower().replace(" ", "_")


def markdown_files():
    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


index = {}
for path in markdown_files():
    index.setdefault(normalize(path.stem), []).append(path)

broken = []
for path in markdown_files():
    text = path.read_text(encoding="utf-8")
    for match in WIKI_LINK.finditer(text):
        target = normalize(match.group(1))
        if target in {"...", "todo"}:
            continue
        if target not in index:
            broken.append((path.relative_to(ROOT), match.group(1)))

if broken:
    print("Broken wiki links:")
    for file, target in broken:
        print(f"{file}: [[{target}]]")
    raise SystemExit(1)

print("No broken wiki links found.")
