#!/usr/bin/env python3
"""Audit the two-scale affine reading of the zeta-side outlier lock."""

from __future__ import annotations

import json
import math
from pathlib import Path


BASE = Path(__file__).resolve().parent
LAMBDA = 6.0


def load_json(name: str) -> dict:
    return json.loads((BASE / name).read_text())


def to_num(value):
    if isinstance(value, str):
        return float(value)
    return value


def main() -> None:
    spectral_data = load_json("E79_101_outlier_escape_agreement_results.json")
    cases = {
        case["label"]: [
            {k: to_num(v) for k, v in row.items()}
            for row in case["rows"]
        ]
        for case in spectral_data["cases"]
    }

    # Fit alpha only on the honest zeta ladder, as a descriptive compression of
    # the observed affine law after peeling off the deterministic mean(d) shift.
    num = 0.0
    den = 0.0
    for row in cases["zeta"]:
        N = int(row["N"])
        outlier_abs = row["outlier_abs"]
        escape_scale = outlier_abs / row["outlier_over_escape"]
        mean_d = math.pi * (N - 1) / LAMBDA
        residual = outlier_abs - (escape_scale + mean_d)
        second_abs = row["second_abs"]
        num += residual * second_abs
        den += second_abs * second_abs
    alpha = num / den

    output = {
        "statement": "E79.105 two-scale outlier law audit",
        "source_files": ["E79_101_outlier_escape_agreement_results.json"],
        "lambda": LAMBDA,
        "zeta_alpha_least_squares": alpha,
        "model": "outlier_abs ~= escape_scale + mean(d) + alpha * second_abs",
        "cases": [],
    }

    for label, rows in cases.items():
        case_rows = []
        rel_errors = []
        local_alphas = []
        for row in rows:
            N = int(row["N"])
            outlier_abs = row["outlier_abs"]
            escape_scale = outlier_abs / row["outlier_over_escape"]
            mean_d = math.pi * (N - 1) / LAMBDA
            second_abs = row["second_abs"]
            residual = outlier_abs - (escape_scale + mean_d)
            local_alpha = residual / second_abs
            predicted = escape_scale + mean_d + alpha * second_abs
            rel_error = predicted / outlier_abs - 1.0
            case_rows.append(
                {
                    "N": N,
                    "outlier_abs": outlier_abs,
                    "escape_scale": escape_scale,
                    "mean_d": mean_d,
                    "second_abs": second_abs,
                    "residual_after_mean_shift": residual,
                    "local_alpha": local_alpha,
                    "predicted_outlier_abs": predicted,
                    "prediction_relative_error": rel_error,
                }
            )
            rel_errors.append(abs(rel_error))
            local_alphas.append(local_alpha)

        mean_alpha = sum(local_alphas) / len(local_alphas)
        var_alpha = sum((a - mean_alpha) ** 2 for a in local_alphas) / len(local_alphas)
        output["cases"].append(
            {
                "label": label,
                "rows": case_rows,
                "summary": {
                    "mean_local_alpha": mean_alpha,
                    "std_local_alpha": math.sqrt(var_alpha),
                    "mean_abs_prediction_rel_error": sum(rel_errors) / len(rel_errors),
                    "max_abs_prediction_rel_error": max(rel_errors),
                },
            }
        )

    out_path = BASE / "E79_105_two_scale_outlier_law_results.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
