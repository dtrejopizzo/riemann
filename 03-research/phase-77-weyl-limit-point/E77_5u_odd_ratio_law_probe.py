#!/usr/bin/env python3
"""E77.5u finite fit of Q_N against weighted odd/inserted ratio."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def points(path: Path):
    data = json.loads(path.read_text(encoding="ascii"))
    pts = []
    for case in data["cases"]:
        for row in case["rows"]:
            for s in row["sigmas"]:
                odd = float(s["lr_odd_abs"])
                ins = float(s["inserted_abs"])
                pts.append(
                    {
                        "label": case["label"],
                        "N": row["N"],
                        "mod4": row["mod4"],
                        "sigma": s["sigma"],
                        "ratio": odd / ins if ins else float("inf"),
                        "Q": float(s["Q"]),
                    }
                )
    return pts


def fit_linear(pts):
    n = len(pts)
    sx = sum(p["ratio"] for p in pts)
    sy = sum(p["Q"] for p in pts)
    sxx = sum(p["ratio"] ** 2 for p in pts)
    sxy = sum(p["ratio"] * p["Q"] for p in pts)
    den = n * sxx - sx * sx
    if den == 0:
        return 0.0, sy / n if n else 0.0
    a = (n * sxy - sx * sy) / den
    b = (sy - a * sx) / n
    return a, b


def apply_fit(pts, a, b):
    rows = []
    for p in pts:
        pred = a * p["ratio"] + b
        rows.append({**p, "pred": pred, "residual": p["Q"] - pred, "abs_residual": abs(p["Q"] - pred)})
    return rows


def summarize(rows):
    return {
        "count": len(rows),
        "max_abs_residual": max((r["abs_residual"] for r in rows), default=0.0),
        "mean_abs_residual": sum(r["abs_residual"] for r in rows) / len(rows) if rows else 0.0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeta", type=Path, default=HERE / "E77_5t_weighted_parity_cell_zeta.json")
    parser.add_argument("--plant", type=Path, default=HERE / "E77_5t_weighted_parity_cell_plant_n18.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5u_odd_ratio_law_results.json")
    args = parser.parse_args()
    zpts = points(args.zeta)
    ppts = points(args.plant)
    result = {"statement": "Q versus weighted odd/inserted ratio finite fit", "fits": []}
    for sigma in sorted({p["sigma"] for p in zpts}):
        train = [p for p in zpts if p["sigma"] == sigma]
        a, b = fit_linear(train)
        zrows = apply_fit(train, a, b)
        prows = apply_fit([p for p in ppts if p["sigma"] == sigma], a, b)
        result["fits"].append(
            {
                "sigma": sigma,
                "model": {"slope": a, "intercept": b},
                "zeta_summary": summarize(zrows),
                "plant_summary": summarize(prows),
                "zeta_rows": zrows,
                "plant_rows": prows,
            }
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for fit in result["fits"]:
        print(
            f"SIGMA {fit['sigma']} slope={fit['model']['slope']:.6g} "
            f"intercept={fit['model']['intercept']:.6g} "
            f"zMax={fit['zeta_summary']['max_abs_residual']:.6g} "
            f"pMax={fit['plant_summary']['max_abs_residual']:.6g}",
            flush=True,
        )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
