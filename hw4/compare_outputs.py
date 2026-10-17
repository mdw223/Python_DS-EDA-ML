from __future__ import annotations

import argparse
import difflib
import subprocess
import sys
from pathlib import Path


# Run this from hw4/:
# /home/malik/GitRepositories/python/.venv/bin/python compare_outputs.py HW4WensmanM.py inputs/input01.txt outputs/output01.txt
# python3 compare_outputs.py HW4WensmanM.py Inputs Outputs

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
        description="Run a Python program with an input file or input directory and compare stdout to expected output(s)."
    )
    parser.add_argument("program", type=Path, help="Python program to run")
    parser.add_argument(
        "input_path",
        type=Path,
        help="Input file or directory containing input files",
    )
    parser.add_argument(
        "expected_path",
        type=Path,
        nargs="?",
        help="Expected output file or directory (optional when input_path is a directory)",
    )
    args = parser.parse_args()

    # Single-file mode
    if args.input_path.is_file():
        if not args.expected_path or not args.expected_path.is_file():
            parser.error("When input is a file, expected output file must be provided.")

        actual = normalize(run_program(args.program, args.input_path.read_text()))
        expected = normalize(args.expected_path.read_text())

        if actual == expected:
            print(f"PASS: {args.input_path}")
            return 0

        print(f"FAIL: {args.input_path} did not match {args.expected_path}")
        diff = difflib.unified_diff(
            expected.splitlines(keepends=True),
            actual.splitlines(keepends=True),
            fromfile=str(args.expected_path),
            tofile="actual output",
        )
        sys.stdout.writelines(diff)
        return 1

    # Directory mode: compare each input file to a corresponding expected file
    if args.input_path.is_dir():
        inputs_dir = args.input_path
        # Determine outputs dir: use provided expected_path if directory, else try sibling directories
        if args.expected_path and args.expected_path.is_dir():
            outputs_dir = args.expected_path
        else:
            # try common names
            candidate1 = inputs_dir.parent / "outputs"
            candidate2 = inputs_dir.parent / "Outputs"
            candidate3 = inputs_dir.parent / "Outputs"
            if candidate1.is_dir():
                outputs_dir = candidate1
            elif candidate2.is_dir():
                outputs_dir = candidate2
            else:
                # fallback to an "Outputs" inside the same dir
                outputs_dir = inputs_dir.parent / "Outputs"

        failures = 0
        # collect input files (common pattern: start with 'input')
        input_files = sorted(f for f in inputs_dir.iterdir() if f.is_file())
        if not input_files:
            print(f"No input files found in {inputs_dir}")
            return 2

        for inp in input_files:
            # try to find matching expected file by replacing 'input' with 'output' in the name
            expected_candidate = None
            name = inp.name
            if name.lower().startswith("input"):
                expected_name = "output" + name[len("input"):]
                for candidate in (outputs_dir / expected_name, outputs_dir / expected_name.replace("input", "")):
                    if candidate.exists():
                        expected_candidate = candidate
                        break

            # fallback: try same filename inside outputs dir
            if expected_candidate is None:
                candidate_same = outputs_dir / name
                if candidate_same.exists():
                    expected_candidate = candidate_same

            if expected_candidate is None:
                print(f"SKIP: no expected output found for {inp}")
                failures += 1
                continue

            actual = normalize(run_program(args.program, inp.read_text()))
            expected = normalize(expected_candidate.read_text())

            if actual == expected:
                print(f"PASS: {inp.name}")
            else:
                print(f"FAIL: {inp.name} did not match {expected_candidate}")
                diff = difflib.unified_diff(
                    expected.splitlines(keepends=True),
                    actual.splitlines(keepends=True),
                    fromfile=str(expected_candidate),
                    tofile=f"actual {inp.name}",
                )
                sys.stdout.writelines(diff)
                failures += 1

        if failures:
            print(f"{failures} comparison(s) failed or skipped")
            return 1

        print("ALL PASS")
        return 0

    parser.error("input_path must be an existing file or directory")


if __name__ == "__main__":
    raise SystemExit(main())