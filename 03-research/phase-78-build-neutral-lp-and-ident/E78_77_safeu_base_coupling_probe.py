#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE = HERE / "E78_73_basepoint_radial_results.json"
TAIL = HERE / "E78_75_fractional_budget_results.json"
SAFEU = HERE / "E78_28_safe_u_geometric_envelope_results.json"


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def main() -> None:
    base = {
        int(row["N"]): float(row["re_delta_ell_base"])
        for row in json.loads(BASE.read_text())["builds"]["zeta"]["rows"]
    }
    tail = {
        (row["sigma"], int(row["N"])): row
        for row in json.loads(TAIL.read_text())["builds"]["zeta"]["rows"]
    }
    safe = json.loads(SAFEU.read_text())["builds"]["zeta"]["rows"]

    rows = []
    tail_over_a = []
    a_over_base = []
    for row in safe:
        sigma = row["sigma"]
        N = int(row["N"])
        if (sigma, N) not in tail or N not in base:
            continue
        A = float(row["A_N"])
        B = base[N]
        tau = float(tail[(sigma, N)]["tail_ratio"])
        T = tau * B
        rows.append(
            {
                "sigma": sigma,
                "N": N,
                "safeu_amplitude_A_N": A,
                "basepoint_reserve": B,
                "tail_over_A": T / A,
                "A_over_base": A / B,
                "tail_over_base": tau,
            }
        )
        tail_over_a.append(T / A)
        a_over_base.append(A / B)

    result = {
        "statement": (
            "Candidate scale-coupled law for the radial shell budget: "
            "TAIL <= kappa(sigma) A_N, together with A_N <= C' BASE."
        ),
        "sources": {
            "basepoint": str(BASE),
            "fractional_budget": str(TAIL),
            "safeu_geometric_envelope": str(SAFEU),
        },
        "rows": rows,
        "summary": {
            "tail_over_A": summarize(tail_over_a),
            "A_over_base": summarize(a_over_base),
        },
    }
    out_path = HERE / "E78_77_safeu_base_coupling_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
