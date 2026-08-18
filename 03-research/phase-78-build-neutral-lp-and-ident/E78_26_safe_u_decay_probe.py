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
            "Audit of strict decay for A_N = N Delta safe_u_N, equivalent to "
            "SAFE-U-WEIGHTED-MONOTONICITY"
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
        for (sigma, N), row in deltas.items():
            nxt = deltas.get((sigma, N + 2))
            if nxt is None:
                continue
            a_n = N * row["delta_u_safe"]
            a_next = (N + 2) * nxt["delta_u_safe"]
            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "A_N": a_n,
                    "A_next": a_next,
                    "strict_decay": a_n > a_next,
                }
            )
        result["builds"][build] = {
            "rows": rows,
            "strict_decay_count": sum(1 for r in rows if r["strict_decay"]),
            "strict_decay_fail_count": sum(1 for r in rows if not r["strict_decay"]),
        }

    out_path = HERE / "E78_26_safe_u_decay_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
