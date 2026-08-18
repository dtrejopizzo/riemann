#!/usr/bin/env python3
"""
108_52 verifier.

Re-runs the two prerequisite Stage-5 verifiers (108_50, 108_51) as
subprocesses and confirms each exits 0, then reprints the closing table of
108_52_STAGE_5_STATUS.md as a consistency summary. This script does not
re-derive any mathematical content; it only checks that the prerequisite
scripts are present and ran cleanly.
"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

PREREQS = [
    "108_50_no_comparison_map_at_generator_level.py",
    "108_51_toy_regularized_pairing_divergence.py",
]


def run_prereq(name):
    path = HERE / name
    assert path.is_file(), f"missing prerequisite verifier: {name}"
    print(f"=== running {name} ===")
    result = subprocess.run([sys.executable, str(path)], cwd=str(HERE),
                             capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
    assert result.returncode == 0, f"{name} exited {result.returncode}"
    return True


def print_closing_table():
    rows = [
        ("comparison map at generator level, forward direction",
         "impossible, proved (108_50 Thm 1.2)"),
        ("comparison map at generator level, reverse direction",
         "impossible, proved (108_50 Thm 2.2)"),
        ("regularized route: cutoff family (Condition I)",
         "architecturally clear, not formally constructed"),
        ("regularized route: convergence (Condition II)",
         "open; toy model diverges (108_51 Prop. 3.1)"),
        ("regularized route: radicals correspond (Condition III)",
         "open; not examinable here"),
        ("design-condition pre-test on the regularized route",
         "passes (108_51 sec 4)"),
        ("Stage 3 assembly shown to be an intersection number",
         "no"),
        ("Stage 3 assembly shown NOT to be an intersection number",
         "no -- only the naive route is excluded"),
    ]
    print("\n=== Stage 5 closing table ===")
    width = max(len(a) for a, _ in rows)
    for a, b in rows:
        print(f"  {a.ljust(width)} : {b}")


def main():
    ok = True
    for name in PREREQS:
        ok = run_prereq(name) and ok
    assert ok
    print_closing_table()
    print("\nVERDICT: both prerequisite Stage-5 verifiers (108_50, 108_51) "
          "exit 0; Stage 5 is partially closed -- the naive comparison map "
          "is proved impossible (closed), the regularized route passes the "
          "design-condition pre-test but its convergence (Condition II) "
          "remains open (not closed).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
