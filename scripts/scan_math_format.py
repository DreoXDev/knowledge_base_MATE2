from pathlib import Path

bad_patterns = ["\\(", "\\)", "\\[", "\\]"]
roots = [
    "03_maps",
    "04_theory",
    "05_theorem_cards",
    "06_oral_exam_discourses",
    "07_exercises",
    "09_exam_questions",
    "10_rag",
    "11_exams",
    "12_final_review",
]

errors = []

for root in roots:
    path = Path(root)
    if not path.exists():
        continue
    for file in path.rglob("*.md"):
        text = file.read_text(encoding="utf-8")
        for pattern in bad_patterns:
            if pattern in text:
                errors.append((str(file), pattern))

if errors:
    print("Found non-Obsidian math delimiters:")
    for file, pattern in errors:
        print(f"{file}: {pattern}")
    raise SystemExit(1)

print("OK: no non-Obsidian math delimiters found.")
