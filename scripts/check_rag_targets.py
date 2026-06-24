from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RAG = ROOT / "10_rag"
PATH_IN_BACKTICKS = re.compile(r"`([^`]+)`")

missing = []

for file in RAG.glob("*.md"):
    text = file.read_text(encoding="utf-8")
    for match in PATH_IN_BACKTICKS.finditer(text):
        raw = match.group(1).strip()
        if not raw or raw.endswith("/") or "*" in raw:
            continue
        if not (raw.endswith(".md") or raw.endswith(".pdf") or "/" in raw):
            continue
        target = raw.split("#", 1)[0]
        path = ROOT / target
        if not path.exists():
            missing.append((file.relative_to(ROOT), raw))

if missing:
    print("Missing RAG targets:")
    for file, target in missing:
        print(f"{file}: `{target}`")
    raise SystemExit(1)

print("OK: all RAG targets exist.")
