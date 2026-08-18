#!/usr/bin/env python3

import json
from math import sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MOM = ROOT / "E79_59_ray_profile_moment_results.json"
EDGE = ROOT / "E79_58_ray_edge_intensity_results.json"
OUT = ROOT / "E79_63_boundary_correction_locality_results.json"


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
    vals = []
    for i, row in enumerate(rows):
        train = [r for j, r in enumerate(rows) if j != i]
        beta = fit_affine(train, keys)
        pred = predict(beta, row, keys)
        vals.append(abs(row["y"] - pred) / abs(row["y"]))
    return {"max_relative_error": max(vals), "mean_relative_error": sum(vals) / len(vals)}


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
                "edge0": e["edge0_N2"],
                "edge1": e["edge1_N2"],
                "edge2": e["edge2_N2"],
                "edge01_avg": 0.5 * (e["edge0_N2"] + e["edge1_N2"]),
                "edge12_avg": 0.5 * (e["edge1_N2"] + e["edge2_N2"]),
                "edge012_avg": (e["edge0_N2"] + e["edge1_N2"] + e["edge2_N2"]) / 3.0,
                "delta10": e["edge1_N2"] - e["edge0_N2"],
                "delta21": e["edge2_N2"] - e["edge1_N2"],
                "ratio10": e["edge1_N2"] / e["edge0_N2"],
                "ratio21": e["edge2_N2"] / e["edge1_N2"],
                "front2_mass": e["edge0_N2"] + e["edge1_N2"],
            }
        )

    extras = [
        "edge0",
        "edge1",
        "edge2",
        "edge01_avg",
        "edge12_avg",
        "edge012_avg",
        "delta10",
        "delta21",
        "ratio10",
        "ratio21",
        "front2_mass",
    ]

    result = {
        "statement": "E79.63 locality audit for the one-shell correction",
        "sources": [str(MOM), str(EDGE)],
        "rows": rows,
        "baseline_keys": ["slope", "intensity"],
        "extras": {},
    }

    for extra in extras:
        keys = ["slope", "intensity", extra]
        beta = fit_affine(rows, keys)
        result["extras"][extra] = {
            "keys": keys,
            "beta": beta,
            "in_sample_max_relative_error": max_rel(rows, beta, keys),
            "leave_one_out": loo(rows, keys),
        }

    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
