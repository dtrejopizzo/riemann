#!/usr/bin/env python3
"""E79.53 - transport-band audit for the curvature coefficient g_N."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_52_two_mode_sigma_template_results.json"
POWERS = [1.0, 1.5, 2.0, 2.5, 3.0]


def summarize(vals):
    return {
        "mean": sum(vals) / len(vals),
        "min": min(vals),
        "max": max(vals),
        "band_ratio": max(vals) / min(vals),
    }


def main():
    data = json.loads(SRC.read_text())
    out = {"statement": "E79.53 curvature transport band audit", "source": str(SRC), "cases": []}
    for case in data["cases"]:
        rows = case["rows"]
        powers = []
        for p in POWERS:
            vals = []
            for row in rows:
                N = row["N"]
                g = abs(float(row["coefficients"]["curvature_mode"]))
                vals.append((N ** p) * g)
            powers.append({"power": p, "values": vals, **summarize(vals)})
        best = min(powers, key=lambda r: r["band_ratio"])
        out["cases"].append({"label": case["label"], "powers": powers, "best_band": best})

    out_path = HERE / "E79_53_curvature_transport_band_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"], "best power", case["best_band"]["power"], "band", case["best_band"]["band_ratio"])
        for row in case["powers"]:
            print(
                f"  p={row['power']:.1f} band={row['band_ratio']:.6g} "
                f"mean={row['mean']:.6g}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
