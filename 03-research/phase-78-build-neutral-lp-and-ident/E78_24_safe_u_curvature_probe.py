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
            "Exact reconstruction of Q_theta as second drift of safe_u: "
            "Q_theta,N = N^2 (N Delta safe_u_N - (N+2) Delta safe_u_{N+2})"
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
        for qrow in case["qrows"]:
            sigma = qrow["sigma"]
            N = qrow["N"]
            row = deltas[(sigma, N)]
            nxt = deltas.get((sigma, N + 2))
            reconstructed = None
            err = None
            if nxt is not None:
                reconstructed = N * N * (
                    N * row["delta_u_safe"] - (N + 2) * nxt["delta_u_safe"]
                )
                err = abs(reconstructed - qrow["Q_theta"])
            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "mod4": qrow["mod4"],
                    "delta_u_safe": row["delta_u_safe"],
                    "delta_u_safe_next": None if nxt is None else nxt["delta_u_safe"],
                    "Q_theta": qrow["Q_theta"],
                    "reconstructed_Q_theta": reconstructed,
                    "reconstruction_error": err,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "max_reconstruction_error": max(
                (row["reconstruction_error"] for row in rows if row["reconstruction_error"] is not None),
                default=0.0,
            ),
        }

    out_path = HERE / "E78_24_safe_u_curvature_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
