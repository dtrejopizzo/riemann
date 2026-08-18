#!/usr/bin/env python3
"""E79.49 - transport band audit for the affine residual slope."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_48_affine_sigma_template_results.json"


def main():
    data = json.loads(SRC.read_text())
    out = {"statement": "E79.49 slope transport band audit", "source": str(SRC), "cases": []}
    for case in data["cases"]:
        rows = []
        scaled = []
        raw = []
        for row in case["rows"]:
            a = float(row["least_squares"]["slope"])
            N = row["N"]
            rows.append(
                {
                    "N": N,
                    "support_abs": row["support_abs"],
                    "slope": a,
                    "scaled_signed": N * a,
                    "scaled_abs": N * abs(a),
                }
            )
            scaled.append(N * abs(a))
            raw.append(N * a)
        out["cases"].append(
            {
                "label": case["label"],
                "rows": rows,
                "mean_scaled_abs": sum(scaled) / len(scaled),
                "min_scaled_abs": min(scaled),
                "max_scaled_abs": max(scaled),
                "band_ratio": max(scaled) / min(scaled),
                "mean_scaled_signed": sum(raw) / len(raw),
            }
        )

    out_path = HERE / "E79_49_slope_transport_band_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"])
        print(
            " mean_scaled_abs", f"{case['mean_scaled_abs']:.6g}",
            "band_ratio", f"{case['band_ratio']:.6g}",
            "mean_scaled_signed", f"{case['mean_scaled_signed']:.6g}",
        )
        for row in case["rows"]:
            print(
                f"  N={row['N']:2d} a={row['slope']:.6g} "
                f"N|a|={row['scaled_abs']:.6g} Na={row['scaled_signed']:.6g}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
