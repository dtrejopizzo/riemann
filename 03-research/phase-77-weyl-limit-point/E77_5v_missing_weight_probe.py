#!/usr/bin/env python3
"""E77.5v candidate weighted observables for the mod2 spike."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_points(path: Path):
    data = json.loads(path.read_text(encoding="ascii"))
    pts = []
    for case in data["cases"]:
        for row in case["rows"]:
            for s in row["sigmas"]:
                ins = float(s["inserted_abs"])
                pts.append(
                    {
                        "label": case["label"],
                        "N": row["N"],
                        "mod4": row["mod4"],
                        "sigma": s["sigma"],
                        "Q": float(s["Q"]),
                        "odd_ratio": float(s["lr_odd_abs"]) / ins if ins else float("inf"),
                        "old_boundary_ratio": float(s["old_boundary_pair_abs"]) / ins if ins else float("inf"),
                        "outer_ratio": float(s["outer_pair_abs"]) / ins if ins else float("inf"),
                        "old_shell_ratio": float(s["old_shell_pair_abs"]) / ins if ins else float("inf"),
                    }
                )
    return pts


def corr(xs, ys):
    n = len(xs)
    if n < 2:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx == 0 or vy == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (vx * vy) ** 0.5


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeta", type=Path, default=HERE / "E77_5t_weighted_parity_cell_zeta.json")
    parser.add_argument("--plant", type=Path, default=HERE / "E77_5t_weighted_parity_cell_plant_n18.json")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5v_missing_weight_results.json")
    args = parser.parse_args()
    pts = load_points(args.zeta) + load_points(args.plant)
    variables = ["odd_ratio", "old_boundary_ratio", "outer_ratio", "old_shell_ratio"]
    result = {"statement": "Candidate weighted observables for mod2 Q spike", "groups": []}
    for label in sorted({p["label"] for p in pts}):
        for sigma in sorted({p["sigma"] for p in pts if p["label"] == label}):
            for mod4 in [0, 2]:
                rows = [p for p in pts if p["label"] == label and p["sigma"] == sigma and p["mod4"] == mod4]
                if not rows:
                    continue
                scores = {}
                for var in variables:
                    scores[var] = corr([r[var] for r in rows], [r["Q"] for r in rows])
                result["groups"].append(
                    {
                        "label": label,
                        "sigma": sigma,
                        "mod4": mod4,
                        "rows": rows,
                        "correlations": scores,
                    }
                )
                print(f"GROUP {label} sigma={sigma} mod4={mod4} corr={scores}", flush=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
