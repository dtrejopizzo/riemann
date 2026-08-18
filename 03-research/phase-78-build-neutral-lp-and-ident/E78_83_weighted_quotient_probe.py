#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "E78_81_weighted_safedelta_sigma_monotonicity_results.json"
PHASE_AC = HERE.parent / "phase-77-weyl-limit-point" / "E77_5ac_theta_logderiv_coupling_zeta.json"
PHASE_G = HERE.parent / "phase-77-weyl-limit-point" / "E77_5g_schur_phase_increment_results.json"


def main() -> None:
    weighted = {
        int(row["N"]): {"Y1": float(row["Y_sigma_1"]), "Y3": float(row["Y_sigma_3"])}
        for row in json.loads(SOURCE.read_text())["rows"]
    }
    acase = json.loads(PHASE_AC.read_text())["cases"][0]
    gcase = [c for c in json.loads(PHASE_G.read_text())["cases"] if not c["planted"]][0]
    deltas = {(row["sigma"], int(row["N"])): float(row["delta_u_safe"]) for row in acase["deltas"]}

    rows = []
    errors = []
    for inc in gcase["increments"]:
        N = int(inc["from_N"])
        for row in inc["sigmas"]:
            sigma = row["sigma"]
            if sigma not in {"1.0", "3.0"} or (sigma, N) not in deltas or N not in weighted:
                continue
            safe = -float(row["delta_safe_derivative"])
            dsu = deltas[(sigma, N)]
            quotient = safe / dsu
            y = weighted[N]["Y1" if sigma == "1.0" else "Y3"]
            err = abs(quotient - y)
            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "minus_SAFEDELTA": safe,
                    "Delta_safe_u": dsu,
                    "quotient": quotient,
                    "weighted_Y": y,
                    "identity_error": err,
                }
            )
            errors.append(err)

    result = {
        "statement": (
            "Audit of the exact quotient law Y_N = (-SAFEDELTA_N)/Delta safe_u_N."
        ),
        "sources": {
            "weighted_sigma_monotonicity": str(SOURCE),
            "theta_coupling": str(PHASE_AC),
            "schur_phase_increment": str(PHASE_G),
        },
        "rows": rows,
        "max_identity_error": max(errors) if errors else None,
    }
    out_path = HERE / "E78_83_weighted_quotient_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
