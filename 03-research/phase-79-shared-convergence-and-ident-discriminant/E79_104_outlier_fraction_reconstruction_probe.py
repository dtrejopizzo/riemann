#!/usr/bin/env python3
"""Audit whether outlier_fraction is reconstructed once the zeta-side outlier lock is granted."""

from __future__ import annotations

import json
from pathlib import Path


BASE = Path(__file__).resolve().parent


def load_json(name: str) -> dict:
    return json.loads((BASE / name).read_text())


def to_num(value):
    if isinstance(value, str):
        return float(value)
    return value


def main() -> None:
    section_data = load_json("E79_90_escape_balance_split_results.json")
    spectral_data = load_json("E79_101_outlier_escape_agreement_results.json")

    section_rows = {
        case["label"]: {
            int(row["N"]): {k: to_num(v) for k, v in row.items()}
            for row in case["rows"]
        }
        for case in section_data["cases"]
    }
    spectral_rows = {
        case["label"]: {
            int(row["N"]): {k: to_num(v) for k, v in row.items()}
            for row in case["rows"]
        }
        for case in spectral_data["cases"]
    }

    output = {
        "statement": "E79.104 outlier-fraction reconstruction audit",
        "source_files": [
            "E79_90_escape_balance_split_results.json",
            "E79_101_outlier_escape_agreement_results.json",
        ],
        "identity": (
            "outlier_fraction = (outlier_abs / (mesh_radius * spectral_reading))^2 "
            "= (escape_ratio / spectral_reading)^2 * (outlier_abs/escape_scale)^2"
        ),
        "cases": [],
    }

    for label in spectral_rows:
        rows = []
        approx_errors = []
        lock_deviations = []
        for N in sorted(spectral_rows[label]):
            srow = spectral_rows[label][N]
            crow = section_rows[label][N]
            outlier_fraction = crow["outlier_fraction"]
            spectral_exact = (srow["outlier_abs"] / (srow["mesh_radius"] * srow["spectral_reading"])) ** 2
            spectral_approx = (crow["escape_ratio"] / srow["spectral_reading"]) ** 2
            lock_ratio = srow["outlier_over_escape"]
            exact_rel = spectral_exact / outlier_fraction
            approx_rel = spectral_approx / outlier_fraction
            row = {
                "N": N,
                "outlier_fraction": outlier_fraction,
                "spectral_exact_reconstruction": spectral_exact,
                "exact_relative_ratio": exact_rel,
                "escape_spectral_approximation": spectral_approx,
                "approx_relative_ratio": approx_rel,
                "outlier_over_escape": lock_ratio,
            }
            rows.append(row)
            approx_errors.append(abs(approx_rel - 1.0))
            lock_deviations.append(abs(lock_ratio - 1.0))

        output["cases"].append(
            {
                "label": label,
                "rows": rows,
                "summary": {
                    "mean_abs_lock_deviation": sum(lock_deviations) / len(lock_deviations),
                    "max_abs_lock_deviation": max(lock_deviations),
                    "mean_abs_approx_rel_error": sum(approx_errors) / len(approx_errors),
                    "max_abs_approx_rel_error": max(approx_errors),
                },
            }
        )

    out_path = BASE / "E79_104_outlier_fraction_reconstruction_results.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
