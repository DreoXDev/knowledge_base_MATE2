from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PRIORITY = ROOT / "06_oral_exam_discourses" / "01_discorsi_prioritari"
VISUAL_PATH = re.compile(r"`(08_visuals/figures/[^`]+)`")

missing = []

for path in sorted(PRIORITY.glob("*_discorso_completo.md")):
    text = path.read_text(encoding="utf-8")
    has_todo_visual = "TODO visual" in text
    for match in VISUAL_PATH.finditer(text):
        raw = match.group(1)
        target = ROOT / raw
        if not target.exists() and not has_todo_visual:
            missing.append((path.relative_to(ROOT), raw))

if missing:
    print("Missing priority discourse visuals:")
    for file, visual in missing:
        print(f"{file}: `{visual}`")
    raise SystemExit(1)

print("OK: priority discourse visual references exist or have TODO visual.")
