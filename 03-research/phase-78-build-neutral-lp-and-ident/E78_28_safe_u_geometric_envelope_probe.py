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
            "Audit of the geometric-envelope form 0 < A_{N+2} <= rho_* A_N "
            "for A_N = N Delta safe_u_N"
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
        rows = []
        rho_star = None
        for (sigma, N), row in deltas.items():
            nxt = deltas.get((sigma, N + 2))
            if nxt is None:
                continue
            a_n = N * row["delta_u_safe"]
            a_next = (N + 2) * nxt["delta_u_safe"]
            ratio = a_next / a_n if a_n != 0 else None
            positive_envelope = (a_n > 0) and (a_next > 0) and (ratio is not None) and (ratio < 1)
            if positive_envelope:
                rho_star = ratio if rho_star is None else max(rho_star, ratio)
            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "A_N": a_n,
                    "A_next": a_next,
                    "ratio": ratio,
                    "positive_envelope": positive_envelope,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "positive_envelope_count": sum(1 for r in rows if r["positive_envelope"]),
            "positive_envelope_fail_count": sum(1 for r in rows if not r["positive_envelope"]),
            "rho_star_observed": rho_star,
        }

    out_path = HERE / "E78_28_safe_u_geometric_envelope_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
