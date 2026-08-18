#!/usr/bin/env python3

import json
from math import sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAY = ROOT / "E79_56_ray_amplitude_autopsy_results.json"
PROFILE = ROOT / "E79_3J_normalized_edge_profile_results.json"
EDGE = ROOT / "E79_58_ray_edge_intensity_results.json"
OUT = ROOT / "E79_61_intensity_normalized_predictor_results.json"


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


def max_rel(y, yh):
    return max(abs(y[i] - yh[i]) / abs(y[i]) for i in range(len(y)))


def build_rows(label, ray_cases, profile_cases, edge_rows):
    rmap = {row["N"]: row["abs_rho"] for row in next(c for c in ray_cases if c["label"] == label)["rows"]}
    prow = next(c for c in profile_cases if c["label"] == label)["rows"]
    emap = {row["N"]: row for row in edge_rows}
    rows = []
    for row in prow:
        n = row["N"]
        if n not in rmap:
            continue
        means = row["sigmas"]["1.0"]["thresholds"]["0.9"]["bin_means"]
        vals = [(float(u), float(v)) for u, v in means.items() if v is not None]
        avg = sum(v for _, v in vals) / len(vals)
        slope_num = sum((u - 0.5) * (v - avg) for u, v in vals)
        slope_den = sum((u - 0.5) ** 2 for u, _ in vals)
        slope = 0.0 if slope_den == 0 else slope_num / slope_den
        gap = sum(v for u, v in vals if u <= 0.4) - sum(v for u, v in vals if u >= 0.6)
        intensity = emap[n]["avg_N2_shell_90"]
        rows.append(
            {
                "N": n,
                "abs_rho": rmap[n],
                "gap": gap,
                "slope": slope,
                "intensity": intensity,
                "gap_over_intensity": gap / intensity,
                "slope_over_intensity": slope / intensity,
            }
        )
    return rows


def main():
    ray = json.loads(RAY.read_text())
    profile = json.loads(PROFILE.read_text())
    edge = json.loads(EDGE.read_text())
    zeta_rows = build_rows("zeta", ray["cases"], profile["cases"], edge["rows"])
    plant_rows = build_rows("plant", ray["cases"], profile["cases"], edge["rows"])

    models = {
        "gap_plus_slope": ["gap", "slope"],
        "gap_and_intensity": ["gap", "intensity"],
        "slope_and_intensity": ["slope", "intensity"],
        "gap_slope_over_intensity": ["gap_over_intensity", "slope_over_intensity"],
    }

    result = {
        "statement": "E79.61 intensity-normalized modal-amplitude predictors",
        "sources": [str(RAY), str(PROFILE), str(EDGE)],
        "zeta_rows": zeta_rows,
        "plant_rows": plant_rows,
        "models": {},
    }

    for name, keys in models.items():
        beta = fit_affine([[row[k] for row in zeta_rows] for k in keys], [row["abs_rho"] for row in zeta_rows])
        zpred = [predict(beta, [row[k] for k in keys]) for row in zeta_rows]
        ppred = [predict(beta, [row[k] for k in keys]) for row in plant_rows]
        result["models"][name] = {
            "keys": keys,
            "beta": beta,
            "zeta_max_relative_error": max_rel([row["abs_rho"] for row in zeta_rows], zpred),
            "zeta_rows": [
                {"N": row["N"], "actual": row["abs_rho"], "predicted": zpred[i]}
                for i, row in enumerate(zeta_rows)
            ],
            "plant_diagnostic_rows": [
                {"N": row["N"], "actual": row["abs_rho"], "predicted_from_zeta_fit": ppred[i]}
                for i, row in enumerate(plant_rows)
            ],
        }

    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
