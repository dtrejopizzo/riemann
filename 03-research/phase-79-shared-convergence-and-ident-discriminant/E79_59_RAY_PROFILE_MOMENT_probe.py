#!/usr/bin/env python3

import json
from math import sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAY = ROOT / "E79_56_ray_amplitude_autopsy_results.json"
PROFILE = ROOT / "E79_3J_normalized_edge_profile_results.json"
BLOCKS = ROOT / "E79_3K_signed_edge_blocks_results.json"
OUT = ROOT / "E79_59_ray_profile_moment_results.json"


def corr(xs, ys):
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    return num / sqrt(denx * deny)


def main():
    ray = json.loads(RAY.read_text())
    profile = json.loads(PROFILE.read_text())
    blocks = json.loads(BLOCKS.read_text())

    zeta_ray = {row["N"]: row for row in next(c for c in ray["cases"] if c["label"] == "zeta")["rows"]}
    zeta_profile = next(c for c in profile["cases"] if c["label"] == "zeta")
    zeta_blocks = next(c for c in blocks["cases"] if c["label"] == "zeta")["rows"]

    rows = []
    for row in zeta_profile["rows"]:
        n = row["N"]
        if n not in zeta_ray:
            continue
        means = row["sigmas"]["1.0"]["thresholds"]["0.9"]["bin_means"]
        vals = [(float(u), float(v)) for u, v in means.items() if v is not None]
        avg = sum(v for _, v in vals) / len(vals)
        centroid = sum(u * v for u, v in vals) / sum(v for _, v in vals)
        slope_num = sum((u - 0.5) * (v - avg) for u, v in vals)
        slope_den = sum((u - 0.5) ** 2 for u, _ in vals)
        slope = slope_num / slope_den
        front = sum(v for u, v in vals if u <= 0.4)
        back = sum(v for u, v in vals if u >= 0.6)
        alt_ratio = float(next(x for x in zeta_blocks if x["N"] == n)["sigmas"]["1.0"]["thresholds"]["0.9"]["alt_abs_over_abs_mass"])
        rows.append(
            {
                "N": n,
                "abs_rho": zeta_ray[n]["abs_rho"],
                "profile_avg": avg,
                "profile_centroid": centroid,
                "profile_slope": slope,
                "front_back_gap": front - back,
                "alt_ratio": alt_ratio,
            }
        )

    xs = [r["abs_rho"] for r in rows]
    result = {
        "statement": "E79.59 ray-amplitude vs normalized profile moments",
        "sources": [str(RAY), str(PROFILE), str(BLOCKS)],
        "rows": rows,
        "correlations_against_abs_rho": {
            "profile_avg": corr(xs, [r["profile_avg"] for r in rows]),
            "profile_centroid": corr(xs, [r["profile_centroid"] for r in rows]),
            "profile_slope": corr(xs, [r["profile_slope"] for r in rows]),
            "front_back_gap": corr(xs, [r["front_back_gap"] for r in rows]),
            "alt_ratio": corr(xs, [r["alt_ratio"] for r in rows]),
        },
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
