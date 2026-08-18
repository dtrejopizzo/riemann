#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_47_den_radial_contraction_results.json"


def main() -> None:
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Logarithmic drift form of denominator radial contraction: "
            "-log(|d_{N+2}|/|d_N|) = -log|q_N| = -log(1-radial_deficit complement)."
        ),
        "source": str(SRC),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = []
        max_exact_error = 0.0
        for row in payload["rows"]:
            ratio = row["radial_ratio"]
            drift = -math.log(ratio)
            reconstructed = -math.log(1.0 - row["radial_deficit"])
            err = abs(drift - reconstructed)
            max_exact_error = max(max_exact_error, err)
            rows.append(
                {
                    **row,
                    "log_radial_drift": drift,
                    "reconstructed_from_deficit": reconstructed,
                    "reconstruction_error": err,
                    "drift_minus_deficit": drift - row["radial_deficit"],
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "max_exact_error": max_exact_error,
        }

    out_path = HERE / "E78_49_den_log_radial_drift_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
