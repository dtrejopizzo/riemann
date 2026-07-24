#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"


def load_json(name: str):
    return json.loads((PHASE77 / name).read_text())


def main():
    result = {
        "statement": (
            "Audit of theta-dominance: sign coherence of Q_logT follows from "
            "|Q_theta| > |Q_t0| together with sign(Q_logT)=sign(Q_theta)"
        ),
        "sources": {
            "schur_zeta": str(PHASE77 / "E77_5aa_schur_logt_functional_zeta.json"),
            "schur_plant": str(PHASE77 / "E77_5aa_schur_logt_functional_plant.json"),
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        rows = load_json(f"E77_5aa_schur_logt_functional_{build}.json")["cases"][0]["qrows"]
        out_rows = []
        for row in rows:
            q_t0 = row["Q_t0"]
            q_theta = row["Q_theta"]
            q_log = row["Q_logT_reconstructed"]
            dominance_ratio = abs(q_theta) / abs(q_t0) if q_t0 else None
            theta_dominates = abs(q_theta) > abs(q_t0)
            same_sign_log_theta = (
                True if q_log == 0 or q_theta == 0 else ((q_log > 0) == (q_theta > 0))
            )
            out_rows.append(
                {
                    "sigma": row["sigma"],
                    "N": row["N"],
                    "mod4": row["mod4"],
                    "Q_t0": q_t0,
                    "Q_theta": q_theta,
                    "Q_logT": q_log,
                    "dominance_ratio": dominance_ratio,
                    "theta_dominates": theta_dominates,
                    "same_sign_log_theta": same_sign_log_theta,
                }
            )
        result["builds"][build] = {
            "rows": out_rows,
            "dominance_count": sum(1 for r in out_rows if r["theta_dominates"]),
            "nondominance_count": sum(1 for r in out_rows if not r["theta_dominates"]),
            "same_sign_count": sum(1 for r in out_rows if r["same_sign_log_theta"]),
            "opposite_sign_count": sum(1 for r in out_rows if not r["same_sign_log_theta"]),
            "min_dominance_ratio": min(r["dominance_ratio"] for r in out_rows if r["dominance_ratio"] is not None),
            "max_dominance_ratio": max(r["dominance_ratio"] for r in out_rows if r["dominance_ratio"] is not None),
        }

    out_path = HERE / "E78_22_theta_dominance_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
