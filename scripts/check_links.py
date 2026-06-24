from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def normalize(name: str) -> str:
    return name.strip().lower().replace(" ", "_")


def markdown_files():
    ignored = {".git"}
    for path in ROOT.rglob("*.md"):
        if any(part in ignored for part in path.parts):
            continue
        yield path


def build_index():
    index = {}
    for path in markdown_files():
        stem = normalize(path.stem)
        index.setdefault(stem, []).append(path)
    return index


def main() -> int:
    index = build_index()
    broken = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in WIKI_LINK.finditer(text):
            target = normalize(match.group(1))
            if target in {"...", "todo"}:
                continue
            if target not in index:
                broken.append((path, match.group(1)))

    if broken:
        print("Broken wiki links:")
        for path, target in broken:
            print(f"- {path.relative_to(ROOT)} -> [[{target}]]")
        return 1

    print("No broken wiki links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

