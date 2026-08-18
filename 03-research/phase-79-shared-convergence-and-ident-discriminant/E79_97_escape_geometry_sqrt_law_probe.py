#!/usr/bin/env python3
"""E79.97 - Derived audit of the escape/geometry square-root law.

Reads the existing E79.90 audited ladder only.  It tests whether the normalized
rank-one escape scale couples to the geometric defect D_N through the product

    escape_ratio * sqrt(D_N).

No matrix rebuild is performed.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main():
    data = json.loads((HERE / "E79_90_escape_balance_split_results.json").read_text())
    report = {
        "statement": "E79.97 escape/geometry square-root law audit",
        "source": "E79_90_escape_balance_split_results.json",
        "cases": [],
    }
    for case in data["cases"]:
        rows = []
        vals = []
        for row in case["rows"]:
            escape_ratio = float(row["escape_ratio"])
            d_n = float(row["D_N"])
            value = escape_ratio * math.sqrt(d_n)
            vals.append(value)
            rows.append(
                {
                    "N": int(row["N"]),
                    "escape_ratio": row["escape_ratio"],
                    "D_N": row["D_N"],
                    "escape_times_sqrt_D": f"{value:.15g}",
                }
            )
        mean_val = sum(vals) / len(vals)
        rel_spread = (max(vals) - min(vals)) / mean_val if mean_val else 0.0
        report["cases"].append(
            {
                "label": case["label"],
                "rows": rows,
                "summary": {
                    "min_escape_times_sqrt_D": f"{min(vals):.15g}",
                    "max_escape_times_sqrt_D": f"{max(vals):.15g}",
                    "mean_escape_times_sqrt_D": f"{mean_val:.15g}",
                    "relative_spread": f"{rel_spread:.15g}",
                },
            }
        )
    out = HERE / "E79_97_escape_geometry_sqrt_law_results.json"
    out.write_text(json.dumps(report, indent=2))
    print(out)


if __name__ == "__main__":
    main()
