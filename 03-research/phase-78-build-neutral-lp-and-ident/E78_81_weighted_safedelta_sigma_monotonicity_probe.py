#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE_AC = HERE.parent / "phase-77-weyl-limit-point" / "E77_5ac_theta_logderiv_coupling_zeta.json"
PHASE_G = HERE.parent / "phase-77-weyl-limit-point" / "E77_5g_schur_phase_increment_results.json"


def main() -> None:
    acase = json.loads(PHASE_AC.read_text())["cases"][0]
    gcase = [c for c in json.loads(PHASE_G.read_text())["cases"] if not c["planted"]][0]
    pts = {
        (p["sigma"], int(p["step_N"]), p["tag"]): float(p["safe_u"])
        for p in acase["points"]
    }

    rows = []
    ratios = []
    for inc in gcase["increments"]:
        N = int(inc["from_N"])
        vals = {}
        for row in inc["sigmas"]:
            sigma = row["sigma"]
            old = pts.get((sigma, N, "old"))
            new = pts.get((sigma, N, "new"))
            if old is None or new is None:
                continue
            A = N * (old - new)
            vals[sigma] = N * (-float(row["delta_safe_derivative"])) / A
        if "1.0" in vals and "3.0" in vals:
            rows.append(
                {
                    "N": N,
                    "Y_sigma_1": vals["1.0"],
                    "Y_sigma_3": vals["3.0"],
                    "sigma3_over_sigma1": vals["3.0"] / vals["1.0"],
                    "difference": vals["1.0"] - vals["3.0"],
                    "monotone_nonincreasing": vals["1.0"] >= vals["3.0"],
                }
            )
            ratios.append(vals["3.0"] / vals["1.0"])

    result = {
        "statement": (
            "Audit of sigma monotonicity for Y_N(sigma)=N*(-SAFEDELTA_N)/A_N on the common safe slices."
        ),
        "sources": {
            "theta_coupling_points": str(PHASE_AC),
            "schur_phase_increment": str(PHASE_G),
        },
        "rows": rows,
        "global": {
            "all_monotone_nonincreasing": all(r["monotone_nonincreasing"] for r in rows),
            "max_Y": max(max(r["Y_sigma_1"], r["Y_sigma_3"]) for r in rows),
            "min_sigma_ratio": min(ratios),
            "max_sigma_ratio": max(ratios),
        },
    }
    out_path = HERE / "E78_81_weighted_safedelta_sigma_monotonicity_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
