"""Reproducible finite-dimensional reconnaissance for the phase-115 audit.

This is diagnostic floating-point computation, not interval certification.
It restricts cell profiles to piecewise-constant bins and reports the full
generalized minimum, the mean-zero minimum, and the exact finite-dimensional
constant/mean-zero Schur correction fraction.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import random
from pathlib import Path


def load_diagnostic():
    path = Path(__file__).with_name("urg_negative_test.py")
    spec = importlib.util.spec_from_file_location("urg_negative_test", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=260)
    parser.add_argument("--random-count", type=int, default=12)
    parser.add_argument("--seed", type=int, default=115)
    parser.add_argument("--bins", type=int, default=6)
    parser.add_argument("--points-per-bin", type=int, default=5)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    anchors = {3, 5, 10, 20, 40, 80, 120, 160, 200, args.max_n}
    population = [n for n in range(3, args.max_n + 1) if n not in anchors]
    sample = set(rng.sample(population, min(args.random_count, len(population))))
    thresholds = sorted(anchors | sample)

    diagnostic = load_diagnostic()
    rows = []
    for n in thresholds:
        result = diagnostic.test_piecewise_extremizer(
            n,
            bins=args.bins,
            points_per_bin=args.points_per_bin,
            padding_factor=1.5,
        )
        rows.append(
            {
                "N": n,
                "bins": args.bins,
                "ratio_min": result["ratio_min"],
                "mean_zero_ratio_min": result["mean_zero_ratio_min"],
                "schur_cross_fraction": result["defect_cross_fraction"],
                "defect_schur": result["defect_schur"],
            }
        )
        print(rows[-1], flush=True)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()

