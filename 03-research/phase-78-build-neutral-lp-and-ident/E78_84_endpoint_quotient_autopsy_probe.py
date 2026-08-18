#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
QSOURCE = HERE / "E78_83_weighted_quotient_results.json"
CURVATURE = HERE / "E78_24_safe_u_curvature_results.json"
LEFT_ENDPOINT = HERE.parent / "phase-77-weyl-limit-point" / "E77_5ag_margin_lower_bound_zeta_sigma1_n24.json"


def corr(xs: list[float], ys: list[float]) -> float:
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    return num / ((denx * deny) ** 0.5)


def main() -> None:
    qrows = [r for r in json.loads(QSOURCE.read_text())["rows"] if r["sigma"] == "1.0"]
    cur = json.loads(CURVATURE.read_text())["builds"]["zeta"]["rows"]
    curmap = {(r["sigma"], int(r["N"])): r for r in cur}
    case = json.loads(LEFT_ENDPOINT.read_text())["cases"][0]
    ptmap = {(p["sigma"], int(p["step_N"]), p["tag"]): p for p in case["points"]}

    rows = []
    qs = []
    curv = []
    uabs_vals = []
    sector_vals = []
    m_vals = []
    for row in qrows:
        sigma = row["sigma"]
        N = int(row["N"])
        c = curmap.get((sigma, N))
        p = ptmap.get((sigma, N, "new"))
        if c is None or p is None:
            continue
        re = float(p["u"]["re"])
        im = float(p["u"]["im"])
        uabs = float(p["u_abs"])
        sector = im - abs(re)
        m_val = (im * im - re * re) / (uabs * uabs)
        curvature_scale = c["Q_theta"] / (N * N * row["Delta_safe_u"])
        quotient = row["quotient"]
        rows.append(
            {
                "N": N,
                "quotient": quotient,
                "curvature_scale": curvature_scale,
                "u_abs": uabs,
                "sector_margin": sector,
                "cone_ratio_M": m_val,
            }
        )
        qs.append(quotient)
        curv.append(curvature_scale)
        uabs_vals.append(uabs)
        sector_vals.append(sector)
        m_vals.append(m_val)

    result = {
        "statement": (
            "Autopsy of whether the left-endpoint quotient is carried more directly by curvature or by u-sector size."
        ),
        "sources": {
            "weighted_quotient": str(QSOURCE),
            "curvature": str(CURVATURE),
            "left_endpoint_points": str(LEFT_ENDPOINT),
        },
        "rows": rows,
        "correlations": {
            "quotient_vs_curvature_scale": corr(qs, curv),
            "quotient_vs_u_abs": corr(qs, uabs_vals),
            "quotient_vs_sector_margin": corr(qs, sector_vals),
            "quotient_vs_cone_ratio_M": corr(qs, m_vals),
        },
    }
    out_path = HERE / "E78_84_endpoint_quotient_autopsy_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
