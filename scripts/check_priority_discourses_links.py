from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PRIORITY = ROOT / "06_oral_exam_discourses" / "01_discorsi_prioritari"

REQUIRED_SECTION = "## 17. Link a teoria, theorem cards, esercizi, esami"
WIKI_LINK = re.compile(r"\[\[[^\]]+\]\]")
THEORY_PATH = re.compile(r"`04_theory/[^`]+`")
VISUAL_PATH = re.compile(r"`08_visuals/figures/[^`]+`")

warnings = []

for path in sorted(PRIORITY.glob("*_discorso_completo.md")):
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

    if REQUIRED_SECTION not in text:
        warnings.append(f"{rel}: missing required section")

    wiki_count = len(WIKI_LINK.findall(text))
    if wiki_count < 5:
        warnings.append(f"{rel}: only {wiki_count} wikilinks")

    theory_count = len(THEORY_PATH.findall(text))
    if theory_count < 2:
        warnings.append(f"{rel}: only {theory_count} theory paths")

    has_visual = bool(VISUAL_PATH.search(text))
    has_todo_visual = "TODO visual" in text
    if not (has_visual or has_todo_visual):
        warnings.append(f"{rel}: missing visual path or TODO visual")

if warnings:
    print("Priority discourse link warnings:")
    for warning in warnings:
        print(warning)
    raise SystemExit(1)

print("OK: priority discourses have required links and visual references.")
