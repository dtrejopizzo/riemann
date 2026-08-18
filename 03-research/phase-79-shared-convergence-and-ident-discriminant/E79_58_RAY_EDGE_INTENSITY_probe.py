#!/usr/bin/env python3

import json
from math import sqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAY = ROOT / "E79_56_ray_amplitude_autopsy_results.json"
EDGE_PROFILE = ROOT / "E79_3F_edge_profile_results.json"
EDGE_BUDGET = ROOT / "E79_3G_edge_budget_results.json"
EDGE_WIDTH = ROOT / "E79_3I_effective_edge_width_results.json"
OUT = ROOT / "E79_58_ray_edge_intensity_results.json"


def corr(xs, ys):
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    return num / sqrt(denx * deny)


def main():
    ray = json.loads(RAY.read_text())
    edge_profile = json.loads(EDGE_PROFILE.read_text())
    edge_budget = json.loads(EDGE_BUDGET.read_text())
    edge_width = json.loads(EDGE_WIDTH.read_text())

    zeta_ray = {row["N"]: row for row in next(c for c in ray["cases"] if c["label"] == "zeta")["rows"]}
    zeta_profile = next(c for c in edge_profile["cases"] if c["label"] == "zeta")["rows"]
    zeta_budget = next(c for c in edge_budget["cases"] if c["label"] == "zeta")["rows"]
    zeta_width = next(c for c in edge_width["cases"] if c["label"] == "zeta")["rows"]

    rows = []
    for row in zeta_profile:
        n = row["N"]
        if n not in zeta_ray:
            continue
        sigma_profile = row["sigmas"]["1.0"]
        sigma_budget = next(x for x in zeta_budget if x["N"] == n)["sigmas"]["1.0"]
        sigma_width = next(x for x in zeta_width if x["N"] == n)["sigmas"]["1.0"]
        thr90 = sigma_budget["thresholds"]["0.9"]
        wid90 = sigma_width["thresholds"]["0.9"]
        rows.append(
            {
                "N": n,
                "abs_rho": zeta_ray[n]["abs_rho"],
                "common_total": float(sigma_profile["common_total"]),
                "edge0_N2": float(sigma_profile["edge_terms"]["0"]["N2_term"]),
                "edge1_N2": float(sigma_profile["edge_terms"]["1"]["N2_term"]),
                "edge2_N2": float(sigma_profile["edge_terms"]["2"]["N2_term"]),
                "N_abs_common": float(sigma_budget["N_abs_common"]),
                "m90": int(thr90["m"]),
                "m90_over_N": float(thr90["m_over_N"]),
                "avg_N2_shell_90": float(thr90["avg_N2_shell"]),
                "peak_N2_shell_90": float(wid90["peak_N2_shell"]),
                "effective_width_90": float(wid90["effective_width"]),
                "effective_over_N_90": float(wid90["effective_over_N"]),
            }
        )

    xs = [r["abs_rho"] for r in rows]
    keys = [k for k in rows[0] if k not in {"N", "abs_rho"}]
    result = {
        "statement": "E79.58 ray-amplitude vs primitive edge observables",
        "sources": [str(RAY), str(EDGE_PROFILE), str(EDGE_BUDGET), str(EDGE_WIDTH)],
        "rows": rows,
        "correlations_against_abs_rho": {k: corr(xs, [r[k] for r in rows]) for k in keys},
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
