#!/usr/bin/env python3

import json
from math import sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MOM = ROOT / "E79_59_ray_profile_moment_results.json"
EDGE = ROOT / "E79_58_ray_edge_intensity_results.json"
OUT = ROOT / "E79_62_third_coordinate_audit_results.json"


def fit_affine(rows, keys):
    y = [row["y"] for row in rows]
    p = len(keys)
    n = len(y)
    A = [[0.0 for _ in range(p + 1)] for _ in range(p + 1)]
    b = [0.0 for _ in range(p + 1)]
    for i in range(n):
        v = [1.0] + [rows[i][k] for k in keys]
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


def predict(beta, row, keys):
    return beta[0] + sum(beta[i + 1] * row[k] for i, k in enumerate(keys))


def max_rel(rows, beta, keys):
    return max(abs(row["y"] - predict(beta, row, keys)) / abs(row["y"]) for row in rows)


def loo(rows, keys):
    preds = []
    for i, row in enumerate(rows):
        train = [r for j, r in enumerate(rows) if j != i]
        beta = fit_affine(train, keys)
        pred = predict(beta, row, keys)
        preds.append(
            {
                "N": row["N"],
                "actual": row["y"],
                "predicted": pred,
                "relative_error": abs(row["y"] - pred) / abs(row["y"]),
            }
        )
    return {
        "rows": preds,
        "max_relative_error": max(p["relative_error"] for p in preds),
        "mean_relative_error": sum(p["relative_error"] for p in preds) / len(preds),
    }


def main():
    mom = json.loads(MOM.read_text())
    edge = json.loads(EDGE.read_text())
    emap = {row["N"]: row for row in edge["rows"]}
    rows = []
    for row in mom["rows"]:
        e = emap[row["N"]]
        rows.append(
            {
                "N": row["N"],
                "y": row["abs_rho"],
                "slope": row["profile_slope"],
                "intensity": e["avg_N2_shell_90"],
                "centroid": row["profile_centroid"],
                "edge0": e["edge0_N2"],
            }
        )

    models = {
        "slope_plus_intensity": ["slope", "intensity"],
        "slope_intensity_centroid": ["slope", "intensity", "centroid"],
        "slope_intensity_edge0": ["slope", "intensity", "edge0"],
    }

    result = {
        "statement": "E79.62 third-coordinate audit for the modal-amplitude law",
        "sources": [str(MOM), str(EDGE)],
        "rows": rows,
        "models": {},
    }
    for name, keys in models.items():
        beta = fit_affine(rows, keys)
        result["models"][name] = {
            "keys": keys,
            "beta": beta,
            "in_sample_max_relative_error": max_rel(rows, beta, keys),
            "in_sample_rows": [
                {"N": row["N"], "actual": row["y"], "predicted": predict(beta, row, keys)}
                for row in rows
            ],
            "leave_one_out": loo(rows, keys),
        }

    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
