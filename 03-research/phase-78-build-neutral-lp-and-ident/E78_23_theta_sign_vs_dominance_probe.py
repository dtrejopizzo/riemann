#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_json(name: str):
    return json.loads((PHASE77 / name).read_text())


def main():
    phase_cases = load_json("E77_5ad_u_phase_law_results.json")["cases"]
    schur_builds = {
        "zeta": load_json("E77_5aa_schur_logt_functional_zeta.json")["cases"][0]["qrows"],
        "plant": load_json("E77_5aa_schur_logt_functional_plant.json")["cases"][0]["qrows"],
    }

    result = {
        "statement": (
            "Audit of the split THETA-DOMINANCE = THETA-SIGN-STABILITY + "
            "T0-SMALLNESS: u-sector tracks the sign of Q_theta more robustly "
            "than the dominance ratio |Q_theta|/|Q_t0|"
        ),
        "sources": {
            "phase_law": str(PHASE77 / "E77_5ad_u_phase_law_results.json"),
            "schur_zeta": str(PHASE77 / "E77_5aa_schur_logt_functional_zeta.json"),
            "schur_plant": str(PHASE77 / "E77_5aa_schur_logt_functional_plant.json"),
        },
        "builds": {},
    }

    for case, build in zip(phase_cases, ("zeta", "plant")):
        phase_map = {(row["sigma"], row["N"]): row for row in case["rows"]}
        rows = []
        for row in schur_builds[build]:
            if row["sigma"] not in ("1.0", "3.0"):
                continue
            phase = phase_map[(row["sigma"], row["N"])]
            safe_u = phase["safe_u"]
            q_theta = row["Q_theta"]
            q_t0 = row["Q_t0"]
            theta_sign_from_u = (
                True
                if safe_u == 0 or q_theta == 0
                else ((safe_u < 0) == (q_theta > 0))
            )
            theta_dominates = abs(q_theta) > abs(q_t0)
            rows.append(
                {
                    "sigma": row["sigma"],
                    "N": row["N"],
                    "mod4": row["mod4"],
                    "safe_u": safe_u,
                    "sector_margin": phase["sector_margin"],
                    "signed_vertical_model_rel_error": phase["signed_vertical_model_rel_error"],
                    "Q_theta": q_theta,
                    "Q_t0": q_t0,
                    "theta_sign_from_u": theta_sign_from_u,
                    "theta_dominates": theta_dominates,
                    "dominance_ratio": abs(q_theta) / abs(q_t0) if q_t0 else None,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "theta_sign_from_u_count": sum(1 for r in rows if r["theta_sign_from_u"]),
            "theta_sign_from_u_fail_count": sum(1 for r in rows if not r["theta_sign_from_u"]),
            "theta_dominance_count": sum(1 for r in rows if r["theta_dominates"]),
            "theta_dominance_fail_count": sum(1 for r in rows if not r["theta_dominates"]),
        }

    out_path = HERE / "E78_23_theta_sign_vs_dominance_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
