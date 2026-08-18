#!/usr/bin/env python3

import json
from math import sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAY = ROOT / "E79_56_ray_amplitude_autopsy_results.json"
MOM = ROOT / "E79_59_ray_profile_moment_results.json"
OUT = ROOT / "E79_60_profile_moment_predictor_results.json"


def fit_affine(columns, y):
    p = len(columns)
    n = len(y)
    A = [[0.0 for _ in range(p + 1)] for _ in range(p + 1)]
    b = [0.0 for _ in range(p + 1)]
    for i in range(n):
        v = [1.0] + [col[i] for col in columns]
        for r in range(p + 1):
            b[r] += v[r] * y[i]
            for c in range(p + 1):
                A[r][c] += v[r] * v[c]
    for i in range(p + 1):
        piv = A[i][i]
        for c in range(i, p + 1):
            A[i][c] /= piv
        b[i] /= piv
        for r in range(p + 1):
            if r == i:
                continue
            m = A[r][i]
            for c in range(i, p + 1):
                A[r][c] -= m * A[i][c]
            b[r] -= m * b[i]
    return b


def predict(beta, xs):
    return beta[0] + sum(beta[i + 1] * xs[i] for i in range(len(xs)))


def metrics(y, yh):
    errs = [y[i] - yh[i] for i in range(len(y))]
    return {
        "max_relative_error": max(abs(errs[i]) / abs(y[i]) for i in range(len(y))),
        "rms_error": sqrt(sum(e * e for e in errs) / len(errs)),
        "errors": errs,
    }


def row_map(label, ray_cases, moment_rows):
    ray = {row["N"]: row["abs_rho"] for row in next(c for c in ray_cases if c["label"] == label)["rows"]}
    return [
        {
            "N": row["N"],
            "abs_rho": ray[row["N"]],
            "profile_slope": row["profile_slope"],
            "front_back_gap": row["front_back_gap"],
            "profile_centroid": row["profile_centroid"],
            "profile_avg": row["profile_avg"],
        }
        for row in moment_rows
        if row["N"] in ray
    ]


def main():
    ray = json.loads(RAY.read_text())
    mom = json.loads(MOM.read_text())
    zeta_rows = row_map("zeta", ray["cases"], mom["rows"])
    plant_rows = row_map("plant", ray["cases"], mom["rows"])

    predictors = {
        "gap_only": ["front_back_gap"],
        "slope_only": ["profile_slope"],
        "gap_plus_slope": ["front_back_gap", "profile_slope"],
    }

    result = {
        "statement": "E79.60 explicit profile-moment predictors for |rho_N|",
        "sources": [str(RAY), str(MOM)],
        "zeta_rows": zeta_rows,
        "plant_rows": plant_rows,
        "fits": {},
    }

    for name, keys in predictors.items():
        cols = [[row[k] for row in zeta_rows] for k in keys]
        y = [row["abs_rho"] for row in zeta_rows]
        beta = fit_affine(cols, y)
        zeta_pred = [predict(beta, [row[k] for k in keys]) for row in zeta_rows]
        plant_pred = [predict(beta, [row[k] for k in keys]) for row in plant_rows]
        result["fits"][name] = {
            "keys": keys,
            "beta": beta,
            "zeta": {
                "rows": [
                    {"N": row["N"], "actual": row["abs_rho"], "predicted": zeta_pred[i]}
                    for i, row in enumerate(zeta_rows)
                ],
                **metrics(y, zeta_pred),
            },
            "plant_diagnostic": {
                "rows": [
                    {"N": row["N"], "actual": row["abs_rho"], "predicted_from_zeta_fit": plant_pred[i]}
                    for i, row in enumerate(plant_rows)
                ]
            },
        }

    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
