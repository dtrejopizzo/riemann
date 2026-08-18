#!/usr/bin/env python3
"""E79.51 - ladder-mean subtraction autopsy for the residual level."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "E79_48_affine_sigma_template_results.json"
SIGMA0 = 0.75


def summarize(vals):
    mags = [abs(v) for v in vals]
    return {
        "mean": sum(vals) / len(vals),
        "mean_abs": sum(mags) / len(mags),
        "band_abs": max(mags) / min(mags) if min(mags) > 0 else None,
    }


def main():
    data = json.loads(SRC.read_text())
    out = {"statement": "E79.51 ladder-mean level autopsy", "source": str(SRC), "cases": []}
    for case in data["cases"]:
        raw_c = []
        raw_b = []
        base_rows = []
        for row in case["rows"]:
            a = float(row["least_squares"]["slope"])
            b = float(row["least_squares"]["intercept"])
            c = a * SIGMA0 + b
            raw_c.append(c)
            raw_b.append(b)
            base_rows.append({"N": row["N"], "support_abs": row["support_abs"], "c": c, "b": b})
        mean_c = sum(raw_c) / len(raw_c)
        mean_b = sum(raw_b) / len(raw_b)
        rows = []
        for row, c, b in zip(base_rows, raw_c, raw_b):
            N = row["N"]
            dc = c - mean_c
            db = b - mean_b
            rows.append(
                {
                    "N": N,
                    "support_abs": row["support_abs"],
                    "c": c,
                    "dc": dc,
                    "N_abs_dc": N * abs(dc),
                    "b": b,
                    "db": db,
                    "N_abs_db": N * abs(db),
                }
            )
        out["cases"].append(
            {
                "label": case["label"],
                "sigma0": SIGMA0,
                "mean_c": mean_c,
                "mean_b": mean_b,
                "summary_c": summarize(raw_c),
                "summary_dc": summarize([r["dc"] for r in rows]),
                "summary_b": summarize(raw_b),
                "summary_db": summarize([r["db"] for r in rows]),
                "rows": rows,
            }
        )

    out_path = HERE / "E79_51_ladder_mean_level_autopsy_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    for case in out["cases"]:
        print(case["label"])
        print(
            " c_band", case["summary_c"]["band_abs"],
            " dc_band", case["summary_dc"]["band_abs"],
            " b_band", case["summary_b"]["band_abs"],
            " db_band", case["summary_db"]["band_abs"],
        )
        for row in case["rows"]:
            print(
                f"  N={row['N']:2d} N|dc|={row['N_abs_dc']:.6g} "
                f"N|db|={row['N_abs_db']:.6g}"
            )
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
