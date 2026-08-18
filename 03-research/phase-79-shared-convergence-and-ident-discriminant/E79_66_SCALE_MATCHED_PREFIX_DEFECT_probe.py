#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MOM = ROOT / "E79_59_ray_profile_moment_results.json"
EDGE = ROOT / "E79_58_ray_edge_intensity_results.json"
PROFILE = ROOT / "E79_3F_edge_profile_results.json"
OUT = ROOT / "E79_66_scale_matched_prefix_defect_results.json"


def fit_affine(rows, keys):
    y = [row["y"] for row in rows]
    p = len(keys)
    n = len(y)
    a = [[0.0 for _ in range(p + 1)] for _ in range(p + 1)]
    b = [0.0 for _ in range(p + 1)]
    for i in range(n):
        v = [1.0] + [rows[i][k] for k in keys]
        for r in range(p + 1):
            b[r] += v[r] * y[i]
            for c in range(p + 1):
                a[r][c] += v[r] * v[c]
    for i in range(p + 1):
        piv = a[i][i]
        for c in range(i, p + 1):
            a[i][c] /= piv
        b[i] /= piv
        for r in range(p + 1):
            if r == i:
                continue
            m = a[r][i]
            for c in range(i, p + 1):
                a[r][c] -= m * a[i][c]
            b[r] -= m * b[i]
    return b


def predict(beta, row, keys):
    return beta[0] + sum(beta[i + 1] * row[k] for i, k in enumerate(keys))


def max_rel(rows, beta, keys):
    return max(abs(row["y"] - predict(beta, row, keys)) / abs(row["y"]) for row in rows)


def loo(rows, keys):
    vals = []
    preds = []
    for i, row in enumerate(rows):
        train = [r for j, r in enumerate(rows) if j != i]
        beta = fit_affine(train, keys)
        pred = predict(beta, row, keys)
        rel = abs(row["y"] - pred) / abs(row["y"])
        vals.append(rel)
        preds.append(
            {
                "N": row["N"],
                "actual": row["y"],
                "predicted": pred,
                "relative_error": rel,
            }
        )
    return {
        "rows": preds,
        "max_relative_error": max(vals),
        "mean_relative_error": sum(vals) / len(vals),
    }


def corr(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) * (x - mx) for x in xs)
    vy = sum((y - my) * (y - my) for y in ys)
    if vx == 0.0 or vy == 0.0:
        return 0.0
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return cov / (vx * vy) ** 0.5


def main():
    mom = json.loads(MOM.read_text())
    edge = json.loads(EDGE.read_text())
    profile = json.loads(PROFILE.read_text())

    emap = {row["N"]: row for row in edge["rows"]}
    pmap = {}
    for case in profile["cases"]:
        if case["label"] != "zeta":
            continue
        for row in case["rows"]:
            sig = row["sigmas"]["1.0"]["edge_terms"]
            edge0frac = float(sig["0"]["abs_prefix_over_common"])
            edge1frac = float(sig["1"]["abs_prefix_over_common"])
            edge2frac = float(sig["2"]["abs_prefix_over_common"])
            pmap[row["N"]] = {
                "edge0frac": edge0frac,
                "edge1frac": edge1frac,
                "edge2frac": edge2frac,
                "prefix_gap_10": edge1frac - edge0frac,
                "prefix_gap_21": edge2frac - edge1frac,
            }

    rows = []
    for row in mom["rows"]:
        n = row["N"]
        e = emap[n]
        p = pmap[n]
        ratio0avg = e["edge0_N2"] / e["avg_N2_shell_90"]
        rel_def = 1.0 - ratio0avg
        rows.append(
            {
                "N": n,
                "y": row["abs_rho"],
                "slope": row["profile_slope"],
                "intensity": e["avg_N2_shell_90"],
                "ratio0avg": ratio0avg,
                "relDef": rel_def,
                **p,
            }
        )

    models = {
        "slope_intensity_ratio0avg": ["slope", "intensity", "ratio0avg"],
        "slope_intensity_relDef": ["slope", "intensity", "relDef"],
        "slope_intensity_edge0frac": ["slope", "intensity", "edge0frac"],
        "slope_intensity_edge1frac": ["slope", "intensity", "edge1frac"],
        "slope_intensity_edge2frac": ["slope", "intensity", "edge2frac"],
        "slope_intensity_prefix_gap_10": ["slope", "intensity", "prefix_gap_10"],
        "slope_intensity_prefix_gap_21": ["slope", "intensity", "prefix_gap_21"],
    }

    result = {
        "statement": "E79.66 scale-matched prefix-defect audit",
        "sources": [str(MOM), str(EDGE), str(PROFILE)],
        "rows": rows,
        "correlations_against_relDef": {},
        "models": {},
    }

    for key in ["edge0frac", "edge1frac", "edge2frac", "prefix_gap_10", "prefix_gap_21", "ratio0avg"]:
        result["correlations_against_relDef"][key] = corr(
            [row["relDef"] for row in rows],
            [row[key] for row in rows],
        )

    for name, keys in models.items():
        beta = fit_affine(rows, keys)
        result["models"][name] = {
            "keys": keys,
            "beta": beta,
            "in_sample_max_relative_error": max_rel(rows, beta, keys),
            "leave_one_out": loo(rows, keys),
        }

    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
