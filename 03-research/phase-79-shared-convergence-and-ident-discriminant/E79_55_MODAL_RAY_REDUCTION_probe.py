#!/usr/bin/env python3

import json
from pathlib import Path
from math import atan2, sqrt


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "E79_52_two_mode_sigma_template_results.json"
OUT = ROOT / "E79_55_modal_ray_reduction_results.json"


def mean(values):
    return sum(values) / len(values)


def build_summary(rows):
    pts = []
    for row in rows:
        n = row["N"]
        coeffs = row["coefficients"]
        x = n * coeffs["slope"]
        y = n * coeffs["curvature_mode"]
        pts.append(
            {
                "N": n,
                "Na": x,
                "Ng": y,
                "ratio": x / y if y != 0 else None,
                "abs_ratio": abs(x / y) if y != 0 else None,
                "angle": atan2(y, x),
            }
        )

    mx = mean([p["Na"] for p in pts])
    my = mean([p["Ng"] for p in pts])
    cov_xx = mean([(p["Na"] - mx) ** 2 for p in pts])
    cov_yy = mean([(p["Ng"] - my) ** 2 for p in pts])
    cov_xy = mean([(p["Na"] - mx) * (p["Ng"] - my) for p in pts])
    corr = cov_xy / sqrt(cov_xx * cov_yy)

    k_signed = sum(p["Na"] * p["Ng"] for p in pts) / sum(p["Na"] ** 2 for p in pts)
    signed_line = []
    for p in pts:
        err = p["Ng"] - k_signed * p["Na"]
        rel = abs(err) / abs(p["Ng"]) if p["Ng"] != 0 else 0.0
        signed_line.append(
            {
                "N": p["N"],
                "predicted_Ng": k_signed * p["Na"],
                "error": err,
                "relative_error": rel,
            }
        )

    abs_pts = [{"N": p["N"], "u": abs(p["Na"]), "v": abs(p["Ng"])} for p in pts]
    k_abs = sum(p["u"] * p["v"] for p in abs_pts) / sum(p["u"] ** 2 for p in abs_pts)
    abs_line = []
    for p in abs_pts:
        err = p["v"] - k_abs * p["u"]
        rel = abs(err) / abs(p["v"]) if p["v"] != 0 else 0.0
        abs_line.append(
            {
                "N": p["N"],
                "predicted_abs_Ng": k_abs * p["u"],
                "error": err,
                "relative_error": rel,
            }
        )

    return {
        "points": pts,
        "corr_Na_Ng": corr,
        "signed_ray_slope": k_signed,
        "signed_ray_max_relative_error": max(item["relative_error"] for item in signed_line),
        "signed_ray_fit": signed_line,
        "abs_ray_slope": k_abs,
        "abs_ray_max_relative_error": max(item["relative_error"] for item in abs_line),
        "abs_ray_fit": abs_line,
        "sign_pattern": ["+" if p["Na"] > 0 else "-" for p in pts],
    }


def main():
    data = json.loads(SOURCE.read_text())
    result = {
        "statement": "E79.55 modal-ray reduction audit",
        "source": str(SOURCE),
        "cases": [],
    }
    for case in data["cases"]:
        result["cases"].append(
            {
                "label": case["label"],
                **build_summary(case["rows"]),
            }
        )
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
