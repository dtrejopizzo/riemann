#!/usr/bin/env python3
"""E79.50 - centered-sigma autopsy for the affine residual level."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_48_affine_sigma_template_results.json"
CENTERS = [0.75, 1.0, 1.25, 1.5, 1.75, 2.0]


def main():
    data = json.loads(SRC.read_text())
    out = {"statement": "E79.50 centered sigma autopsy", "source": str(SRC), "cases": []}
    for case in data["cases"]:
        centers = []
        rows = case["rows"]
        for s0 in CENTERS:
            vals = []
            scaled = []
            for row in rows:
                a = float(row["least_squares"]["slope"])
                b = float(row["least_squares"]["intercept"])
                N = row["N"]
                c = a * s0 + b
                vals.append(abs(c))
                scaled.append(N * abs(c))
            centers.append(
                {
                    "sigma0": s0,
                    "band_c": max(vals) / min(vals),
                    "band_scaled_c": max(scaled) / min(scaled),
                    "mean_c": sum(vals) / len(vals),
                }
            )
        best_raw = min(centers, key=lambda r: r["band_c"])
        best_scaled = min(centers, key=lambda r: r["band_scaled_c"])
        out["cases"].append(
            {
                "label": case["label"],
                "centers": centers,
                "best_raw_band": best_raw,
                "best_scaled_band": best_scaled,
            }
        )

    out_path = HERE / "E79_50_centered_sigma_autopsy_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"])
        print(
            " best_raw",
            case["best_raw_band"]["sigma0"],
            f"band={case['best_raw_band']['band_c']:.6g}",
            " best_scaled",
            case["best_scaled_band"]["sigma0"],
            f"band={case['best_scaled_band']['band_scaled_c']:.6g}",
        )
        for row in case["centers"]:
            print(
                f"  s0={row['sigma0']:.2f} band(c)={row['band_c']:.6g} "
                f"band(Nc)={row['band_scaled_c']:.6g} mean(c)={row['mean_c']:.6g}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
