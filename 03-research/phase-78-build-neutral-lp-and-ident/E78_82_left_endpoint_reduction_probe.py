#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "E78_81_weighted_safedelta_sigma_monotonicity_results.json"


def main() -> None:
    rows = json.loads(SOURCE.read_text())["rows"]
    sigma1 = [{"N": int(r["N"]), "Y_sigma_1": float(r["Y_sigma_1"])} for r in rows]
    vals = sorted(r["Y_sigma_1"] for r in sigma1)
    n = len(vals)
    med = vals[n // 2] if n % 2 else 0.5 * (vals[n // 2 - 1] + vals[n // 2])
    worst = max(sigma1, key=lambda r: r["Y_sigma_1"])
    result = {
        "statement": (
            "Audit of the left-endpoint benchmark for the weighted safe-delta target."
        ),
        "source": str(SOURCE),
        "sigma_left": "1.0",
        "summary": {
            "min": vals[0],
            "median": med,
            "max": vals[-1],
        },
        "worst_row": worst,
        "rows": sigma1,
    }
    out_path = HERE / "E78_82_left_endpoint_reduction_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
