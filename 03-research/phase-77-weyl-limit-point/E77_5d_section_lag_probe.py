#!/usr/bin/env python3
"""E77.5d SECTION-LAG consecutive-N audit."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent


def serial(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def load_lambda6_zeta_rows():
    data = json.loads((HERE / "E77_5c_n22_core_results.json").read_text())
    case = next(c for c in data["cases"] if c["planted"] is None)
    rows = []
    for row in case["rows"]:
        rows.append(
            {
                "N": row["N"],
                "max_error": mp.mpf(row["max_zeta_target_relative_error"]),
                "sigma_errors": [
                    (mp.mpf(s["sigma"]), mp.mpf(s["target_relative_error"]))
                    for s in row["sigmas"]
                ],
            }
        )
    return rows


def main() -> None:
    rows = load_lambda6_zeta_rows()
    deltas = []
    for prev, cur in zip(rows, rows[1:]):
        delta = prev["max_error"] - cur["max_error"]
        ratio = cur["max_error"] / prev["max_error"]
        sigma_delta = []
        for (sigma, prev_err), (_, cur_err) in zip(prev["sigma_errors"], cur["sigma_errors"]):
            sigma_delta.append({"sigma": serial(sigma), "delta": serial(prev_err - cur_err)})
        deltas.append(
            {
                "from_N": prev["N"],
                "to_N": cur["N"],
                "max_error_delta": serial(delta),
                "error_ratio": serial(ratio),
                "sigma_deltas": sigma_delta,
            }
        )
    tail_deltas = [mp.mpf(d["max_error_delta"]) for d in deltas[-4:]]
    tail_ratios = [
        tail_deltas[i + 1] / tail_deltas[i]
        for i in range(len(tail_deltas) - 1)
        if tail_deltas[i] != 0
    ]
    result = {
        "statement": "Consecutive-N SECTION-LAG audit at lambda 6, N=8..22",
        "rows": [
            {"N": row["N"], "max_error": serial(row["max_error"])}
            for row in rows
        ],
        "deltas": deltas,
        "tail_delta_ratios": [serial(r) for r in tail_ratios],
        "tail_delta_min": serial(min(tail_deltas)),
        "tail_delta_max": serial(max(tail_deltas)),
        "verdict": (
            "Deltas are positive but slowly decreasing; the measured tail "
            "is compatible with summability only if an external cofinal "
            "envelope controls the ratios."
        ),
    }
    out = HERE / "E77_5d_section_lag_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
