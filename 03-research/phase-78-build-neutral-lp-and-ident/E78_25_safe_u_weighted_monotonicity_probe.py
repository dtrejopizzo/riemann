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
            "Audit of weighted monotonicity for Delta safe_u: "
            "sign(Q_theta,N) = sign(N Delta safe_u_N - (N+2) Delta safe_u_{N+2})"
        ),
        "sources": {
            "theta_coupling_zeta": str(PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"),
            "theta_coupling_plant": str(PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"),
        },
        "builds": {},
    }

    for build in ("zeta", "plant"):
        case = load_json(f"E77_5ac_theta_logderiv_coupling_{build}.json")["cases"][0]
        deltas = {(row["sigma"], row["N"]): row for row in case["deltas"]}
        qrows = {(row["sigma"], row["N"]): row for row in case["qrows"]}
        rows = []
        for (sigma, N), row in deltas.items():
            nxt = deltas.get((sigma, N + 2))
            q = qrows.get((sigma, N))
            if nxt is None or q is None:
                continue
            weighted_diff = N * row["delta_u_safe"] - (N + 2) * nxt["delta_u_safe"]
            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "mod4": q["mod4"],
                    "delta_u_safe": row["delta_u_safe"],
                    "delta_u_safe_next": nxt["delta_u_safe"],
                    "weighted_diff": weighted_diff,
                    "Q_theta": q["Q_theta"],
                    "same_sign_as_Q_theta": (
                        True
                        if weighted_diff == 0 or q["Q_theta"] == 0
                        else ((weighted_diff > 0) == (q["Q_theta"] > 0))
                    ),
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "same_sign_count": sum(1 for r in rows if r["same_sign_as_Q_theta"]),
            "fail_count": sum(1 for r in rows if not r["same_sign_as_Q_theta"]),
        }

    out_path = HERE / "E78_25_safe_u_weighted_monotonicity_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
