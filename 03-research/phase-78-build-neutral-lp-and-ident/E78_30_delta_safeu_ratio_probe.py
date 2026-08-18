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
            "Exact factorization rho_N = ((N+2)/N) * "
            "(Delta safe_u_{N+2}/Delta safe_u_N)"
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
            delta_n = row["delta_u_safe"]
            delta_next = nxt["delta_u_safe"]
            raw_ratio = delta_next / delta_n if delta_n != 0 else None
            rho = ((N + 2) / N) * raw_ratio if raw_ratio is not None else None
            rows.append(
                {
                    "sigma": sigma,
                    "N": N,
                    "delta_safeu_ratio": raw_ratio,
                    "weight_factor": (N + 2) / N,
                    "rho_reconstructed": rho,
                }
            )
        result["builds"][build] = {"rows": rows}

    out_path = HERE / "E78_30_delta_safeu_ratio_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
