#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE = HERE / "E78_73_basepoint_radial_results.json"
FRAC = HERE / "E78_75_fractional_budget_results.json"
SAFEU = HERE / "E78_28_safe_u_geometric_envelope_results.json"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point" / "E77_5g_schur_phase_increment_results.json"
SIGMA0 = 0.55


def corr(xs: list[float], ys: list[float]) -> float:
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    return num / ((denx * deny) ** 0.5)


def main() -> None:
    base = {
        int(row["N"]): float(row["re_delta_ell_base"])
        for row in json.loads(BASE.read_text())["builds"]["zeta"]["rows"]
    }
    frac = {
        (row["sigma"], int(row["N"])): row
        for row in json.loads(FRAC.read_text())["builds"]["zeta"]["rows"]
    }
    safe = {
        (row["sigma"], int(row["N"])): row
        for row in json.loads(SAFEU.read_text())["builds"]["zeta"]["rows"]
    }
    case = [c for c in json.loads(PHASE77.read_text())["cases"] if not c["planted"]][0]

    rows = []
    avg_vals = []
    point_vals = []
    for inc in case["increments"]:
        N = int(inc["from_N"])
        for row in inc["sigmas"]:
            sigma_str = row["sigma"]
            sigma = float(sigma_str)
            key = (sigma_str, N)
            if key not in frac or key not in safe or sigma <= SIGMA0:
                continue
            A = float(safe[key]["A_N"])
            T = float(frac[key]["tail_ratio"]) * base[N]
            point = (-float(row["delta_safe_derivative"])) / A
            avg = (T / A) / (sigma - SIGMA0)
            rows.append(
                {
                    "sigma": sigma_str,
                    "N": N,
                    "tail_over_A": T / A,
                    "tail_over_A_per_length": avg,
                    "minus_delta_safe_over_A": point,
                }
            )
            avg_vals.append(avg)
            point_vals.append(point)

    result = {
        "statement": (
            "TAIL/A is a radial-average problem for (-SAFEDELTA)/A on the safe axis."
        ),
        "sources": {
            "basepoint": str(BASE),
            "fractional_budget": str(FRAC),
            "safeu_geometric_envelope": str(SAFEU),
            "schur_phase_increment": str(PHASE77),
        },
        "rows": rows,
        "correlation": corr(avg_vals, point_vals),
    }
    out_path = HERE / "E78_78_radial_average_coupling_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
