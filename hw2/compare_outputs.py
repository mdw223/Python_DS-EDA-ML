from __future__ import annotations

import argparse
import difflib
import subprocess
import sys
from pathlib import Path


# Run this from hw2/:
# /home/malik/GitRepositories/python/.venv/bin/python compare_outputs.py HW2WensmanM.py inputs/input-1.txt outputs/output-1.txt

def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip() + "\n"


def run_program(program: Path, input_text: str) -> str:
    result = subprocess.run(
        [sys.executable, str(program)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a Python program with an input file and compare stdout to an expected output file."
    )
    parser.add_argument("program", type=Path, help="Python program to run")
    parser.add_argument("input_file", type=Path, help="File containing test input")
    parser.add_argument("expected_output_file", type=Path, help="File containing expected output")
    args = parser.parse_args()

    actual = normalize(run_program(args.program, args.input_file.read_text()))
    expected = normalize(args.expected_output_file.read_text())

    if actual == expected:
        print("PASS")
        return 0

    print("FAIL: output did not match expected text")
    diff = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        fromfile=str(args.expected_output_file),
        tofile="actual output",
    )
    sys.stdout.writelines(diff)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())