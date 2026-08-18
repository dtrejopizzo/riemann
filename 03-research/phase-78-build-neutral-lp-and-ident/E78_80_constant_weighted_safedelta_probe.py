#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "E78_79_weighted_normalized_safedelta_results.json"


def main() -> None:
    rows = json.loads(SOURCE.read_text())["rows"]
    by_n: dict[int, dict[str, float]] = {}
    vals = []
    for row in rows:
        N = int(row["N"])
        sigma = row["sigma"]
        val = float(row["N_weighted"])
        vals.append(val)
        by_n.setdefault(N, {})[sigma] = val

    sigma_ratios = []
    for N in sorted(by_n):
        if "1.0" in by_n[N] and "3.0" in by_n[N]:
            sigma_ratios.append(
                {
                    "N": N,
                    "sigma3_over_sigma1": by_n[N]["3.0"] / by_n[N]["1.0"],
                    "difference": by_n[N]["1.0"] - by_n[N]["3.0"],
                }
            )

    vals_sorted = sorted(vals)
    n = len(vals_sorted)
    med = vals_sorted[n // 2] if n % 2 else 0.5 * (vals_sorted[n // 2 - 1] + vals_sorted[n // 2])
    result = {
        "statement": (
            "Audit of the constant-envelope candidate for N*(-SAFEDELTA_N)/A_N."
        ),
        "source": str(SOURCE),
        "global_summary": {
            "min": vals_sorted[0],
            "median": med,
            "max": vals_sorted[-1],
        },
        "sigma_ratios": sigma_ratios,
    }
    out_path = HERE / "E78_80_constant_weighted_safedelta_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
