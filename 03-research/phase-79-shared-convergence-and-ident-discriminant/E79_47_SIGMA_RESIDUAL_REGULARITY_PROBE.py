#!/usr/bin/env python3
"""E79.47 - sigma-regularity audit of the first-packet residual.

Use the audited multisigma mismatches from E79.44 and ask whether the residual
left by the first raw packet obeys a simple sigma-profile law.
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_44_multisigma_coupled_packet_results.json"
SIGMAS = [0.75, 1.0, 1.5, 2.0]


def monotone_direction(values):
    nondec = all(values[i] <= values[i + 1] for i in range(len(values) - 1))
    noninc = all(values[i] >= values[i + 1] for i in range(len(values) - 1))
    if nondec and noninc:
        return "flat"
    if nondec:
        return "nondecreasing"
    if noninc:
        return "nonincreasing"
    return "mixed"


def total_variation(values):
    return sum(abs(values[i + 1] - values[i]) for i in range(len(values) - 1))


def curvature(values):
    return [values[i + 2] - 2 * values[i + 1] + values[i] for i in range(len(values) - 2)]


def main():
    data = json.loads(SRC.read_text())
    out = {
        "statement": "E79.47 sigma residual regularity audit",
        "source": str(SRC),
        "cases": [],
    }
    for case in data["cases"]:
        rows = []
        for row in case["rows"]:
            rules = [v for v in row["rules"].values() if v["aggregator"] == "mean"]
            best = min(rules, key=lambda v: float(v["mean_mismatch"]))
            vals = [float(best["mismatches"][str(s)]) for s in SIGMAS]
            curv = curvature(vals)
            scale = max(abs(v) for v in vals) or 1.0
            rows.append(
                {
                    "N": row["N"],
                    "support_abs": best["support_abs"],
                    "mismatches": {str(s): best["mismatches"][str(s)] for s in SIGMAS},
                    "direction": monotone_direction(vals),
                    "total_variation": total_variation(vals),
                    "curvature": curv,
                    "max_abs_curvature": max(abs(c) for c in curv) if curv else 0.0,
                    "normalized_max_curvature": (max(abs(c) for c in curv) if curv else 0.0) / scale,
                }
            )
        out["cases"].append({"label": case["label"], "rows": rows})

    out_path = HERE / "E79_47_sigma_residual_regularity_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"])
        for row in case["rows"]:
            print(
                f" N={row['N']:2d} dir={row['direction']:13s} "
                f"TV={row['total_variation']:.6g} "
                f"ncurv={row['normalized_max_curvature']:.6g} "
                f"support={row['support_abs']}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
