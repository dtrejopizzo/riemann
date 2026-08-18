#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "E78_78_radial_average_coupling_results.json"


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None, "spread": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {
        "count": len(vals),
        "min": vals[0],
        "median": med,
        "max": vals[-1],
        "spread": vals[-1] / vals[0],
    }


def main() -> None:
    rows = json.loads(SOURCE.read_text())["rows"]
    out_rows = []
    raw = []
    nweighted = []
    sqrtweighted = []
    sigmaweighted = []
    for row in rows:
        N = int(row["N"])
        sigma = float(row["sigma"])
        val = float(row["minus_delta_safe_over_A"])
        sigma_weight = sigma - 0.55
        out_rows.append(
            {
                "sigma": row["sigma"],
                "N": N,
                "raw": val,
                "N_weighted": N * val,
                "sqrtN_weighted": (N ** 0.5) * val,
                "sigma_weighted": val / sigma_weight,
            }
        )
        raw.append(val)
        nweighted.append(N * val)
        sqrtweighted.append((N ** 0.5) * val)
        sigmaweighted.append(val / sigma_weight)

    result = {
        "statement": (
            "Audit of candidate normalizations for (-SAFEDELTA_N)/A_N on the common zeta ladder."
        ),
        "source": str(SOURCE),
        "rows": out_rows,
        "summary": {
            "raw": summarize(raw),
            "N_weighted": summarize(nweighted),
            "sqrtN_weighted": summarize(sqrtweighted),
            "sigma_weighted": summarize(sigmaweighted),
        },
    }
    out_path = HERE / "E78_79_weighted_normalized_safedelta_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
