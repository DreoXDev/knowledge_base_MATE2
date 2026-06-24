from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BAD_PATTERNS = ("\\(", "\\)", "\\[", "\\]")


def markdown_files():
    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            yield path


def main() -> int:
    findings = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for pattern in BAD_PATTERNS:
                if pattern in line:
                    findings.append((path, line_no, pattern, line.strip()))

    if findings:
        print("Non-Obsidian math delimiters found:")
        for path, line_no, pattern, line in findings:
            print(f"- {path.relative_to(ROOT)}:{line_no}: contains {pattern!r}: {line}")
        print("Use $...$ for inline math and $$...$$ for block math.")
        return 1

    print("Math delimiter format looks good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

