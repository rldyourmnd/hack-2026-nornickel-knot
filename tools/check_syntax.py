"""Check the existing Python source without importing it or writing bytecode."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    files = sorted((ROOT / "src").rglob("*.py"))
    if not files:
        raise SystemExit("No Python source files were found")
    failed = False
    for source in files:
        try:
            compile(source.read_bytes(), str(source), "exec", dont_inherit=True)
        except (SyntaxError, ValueError) as error:
            failed = True
            if isinstance(error, SyntaxError):
                print(
                    f"{source.relative_to(ROOT)}:{error.lineno}: {error.msg}",
                    file=sys.stderr,
                )
            else:
                print(
                    f"{source.relative_to(ROOT)}: invalid Python source",
                    file=sys.stderr,
                )
    if failed:
        return 1
    print(f"Python syntax valid: {len(files)} source files; no application imports")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
