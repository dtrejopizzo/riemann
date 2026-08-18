#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
TAIL = HERE / "E78_75_fractional_budget_results.json"
SAFEU = HERE / "E78_28_safe_u_geometric_envelope_results.json"


def corr(xs: list[float], ys: list[float]) -> float:
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    denx = sum((x - mx) ** 2 for x in xs)
    deny = sum((y - my) ** 2 for y in ys)
    return num / ((denx * deny) ** 0.5)


def main() -> None:
    tail_rows = {
        (row["sigma"], int(row["N"])): row
        for row in json.loads(TAIL.read_text())["builds"]["zeta"]["rows"]
    }
    safe_rows = json.loads(SAFEU.read_text())["builds"]["zeta"]["rows"]

    rows = []
    rho_values = []
    amp_values = []
    tail_values = []
    for row in safe_rows:
        key = (row["sigma"], int(row["N"]))
        if key not in tail_rows:
            continue
        tail = tail_rows[key]
        tau = float(tail["tail_ratio"])
        rho = float(row["ratio"])
        amp = float(row["A_N"])
        rows.append(
            {
                "sigma": row["sigma"],
                "N": int(row["N"]),
                "safeu_amplitude_A_N": amp,
                "safeu_ratio_rho_N": rho,
                "tail_over_base": tau,
            }
        )
        rho_values.append(rho)
        amp_values.append(amp)
        tail_values.append(tau)

    result = {
        "statement": (
            "Autopsy of the shortcut 'safe_u geometric ratio controls radial "
            "tail/base'."
        ),
        "sources": {
            "fractional_budget": str(TAIL),
            "safeu_geometric_envelope": str(SAFEU),
        },
        "rows": rows,
        "correlations": {
            "rho_vs_tail_over_base": corr(rho_values, tail_values),
            "A_vs_tail_over_base": corr(amp_values, tail_values),
        },
    }
    out_path = HERE / "E78_76_safeu_tail_autopsy_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
