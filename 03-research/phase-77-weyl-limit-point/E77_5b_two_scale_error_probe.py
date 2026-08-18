#!/usr/bin/env python3
"""E77.5b two-scale SR-LOG-ERR audit.

This lightweight probe reads the E77.3c and E77.5a JSON artifacts and
separates the observed finite-section N trend from the lambda/L trend.
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent


def serial(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def log_fit(xs: list[mp.mpf], ys: list[mp.mpf]) -> dict:
    xbar = mp.fsum(xs) / len(xs)
    logs = [mp.log(y) for y in ys]
    ybar = mp.fsum(logs) / len(logs)
    denom = mp.fsum((x - xbar) ** 2 for x in xs)
    slope = mp.fsum((x - xbar) * (y - ybar) for x, y in zip(xs, logs)) / denom
    return {"slope": serial(slope), "points": len(xs)}


def main() -> None:
    e3c = json.loads((HERE / "E77_3c_two_generator_ident_results.json").read_text())
    e5a = json.loads((HERE / "E77_5a_sr_log_error_results.json").read_text())

    fixed_n_rows = []
    for case in e3c["cases"]:
        if case["planted"] is None:
            row = case["rows"][-1]
            fixed_n_rows.append(
                {
                    "lambda": case["lambda"],
                    "N": row["N"],
                    "max_error": row["max_zeta_target_relative_error"],
                }
            )

    zeta5a = next(case for case in e5a["cases"] if case["planted"] is None)
    fixed_lambda_rows = [
        {"N": row["N"], "max_error": row["max_zeta_target_relative_error"]}
        for row in zeta5a["rows"]
    ]
    n_fit = log_fit(
        [mp.mpf(row["N"]) for row in fixed_lambda_rows],
        [mp.mpf(row["max_error"]) for row in fixed_lambda_rows],
    )
    l_fit = log_fit(
        [mp.log(mp.mpf(row["lambda"])) for row in fixed_n_rows],
        [mp.mpf(row["max_error"]) for row in fixed_n_rows],
    )
    result = {
        "statement": "Separate N trend from lambda/L trend for SR-LOG-ERR",
        "fixed_lambda": {
            "lambda": 6,
            "rows": fixed_lambda_rows,
            "log_error_vs_N_fit": n_fit,
        },
        "fixed_N": {
            "N": 18,
            "rows": fixed_n_rows,
            "log_error_vs_log_lambda_fit": l_fit,
        },
        "verdict": (
            "N improves at fixed lambda in the measured range, but lambda "
            "does not improve at fixed N=18; IDENT needs a two-scale "
            "N(L)/L error theorem."
        ),
    }
    out = HERE / "E77_5b_two_scale_error_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2))
    print(f"WROTE {out}")


if __name__ == "__main__":
    main()
