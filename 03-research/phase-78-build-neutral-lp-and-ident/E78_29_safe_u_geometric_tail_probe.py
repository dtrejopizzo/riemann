#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE78 = HERE


def load_json(name: str):
    return json.loads((PHASE78 / name).read_text())


def main():
    src = load_json("E78_28_safe_u_geometric_envelope_results.json")
    result = {
        "statement": (
            "Audit of the transfer SAFE-U-GEOMETRIC-ENVELOPE => geometric tail "
            "control for Delta safe_u via A_N = N Delta safe_u_N"
        ),
        "source": str(PHASE78 / "E78_28_safe_u_geometric_envelope_results.json"),
        "builds": {},
    }

    for build, payload in src["builds"].items():
        rows = [r for r in payload["rows"] if r["sigma"] in ("1.0", "3.0")]
        rho_star = payload["rho_star_observed"]
        out_rows = []
        for row in rows:
            N = row["N"]
            a_n = row["A_N"]
            if a_n == 0:
                continue
            delta_bound = abs(a_n) / N
            out_rows.append(
                {
                    "sigma": row["sigma"],
                    "N": N,
                    "A_N": a_n,
                    "A_next": row["A_next"],
                    "ratio": row["ratio"],
                    "abs_delta_safe_bound_from_A": delta_bound,
                    "positive_envelope": row["positive_envelope"],
                }
            )
        result["builds"][build] = {
            "rows": out_rows,
            "rho_star_observed": rho_star,
        }

    out_path = HERE / "E78_29_safe_u_geometric_tail_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
