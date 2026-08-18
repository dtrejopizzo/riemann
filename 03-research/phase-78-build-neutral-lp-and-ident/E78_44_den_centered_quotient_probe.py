#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
SRC_ZETA = PHASE77 / "E77_5ac_theta_logderiv_coupling_zeta.json"
SRC_PLANT = PHASE77 / "E77_5ac_theta_logderiv_coupling_plant.json"


def load_points(path: Path) -> dict[tuple[str, int], complex]:
    obj = json.loads(path.read_text())
    pts: dict[tuple[str, int], complex] = {}
    for case in obj["cases"]:
        for point in case["points"]:
            if point["tag"] != "new":
                continue
            sigma = point["sigma"]
            section_n = int(point["section_N"])
            theta = complex(float(point["theta"]["re"]), float(point["theta"]["im"]))
            pts[(sigma, section_n)] = theta
    return pts


def summarize(values: list[float]) -> dict[str, float]:
    ordered = sorted(values)
    n = len(ordered)
    median = ordered[n // 2] if n % 2 == 1 else 0.5 * (ordered[n // 2 - 1] + ordered[n // 2])
    return {
        "min": ordered[0],
        "median": median,
        "max": ordered[-1],
    }


def build_rows(points: dict[tuple[str, int], complex]) -> dict[str, object]:
    rows = []
    re_centered = []
    abs_im_centered = []
    abs_im_over_neg_re = []
    directional_errors = []
    max_reconstruction_error = 0.0

    for sigma in sorted({s for s, _ in points}, key=float):
        ns = sorted(n for s, n in points if s == sigma)
        for n in ns:
            key_new = (sigma, n + 2)
            if key_new not in points:
                continue

            d_n = 1 - points[(sigma, n)]
            d_np2 = 1 - points[key_new]
            delta_d = d_np2 - d_n

            centered = delta_d / d_n
            directional = centered.imag / abs(centered)
            angle = math.atan2(centered.imag, centered.real)
            reconstruction_error = abs(d_np2 / d_n - (1 + centered))
            max_reconstruction_error = max(max_reconstruction_error, reconstruction_error)

            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "centered_quotient_re": centered.real,
                    "centered_quotient_im": centered.imag,
                    "centered_quotient_abs": abs(centered),
                    "centered_quotient_arg": angle,
                    "directional_increment_defect": directional,
                    "im_over_abs": directional,
                    "im_over_neg_re": (
                        abs(centered.imag) / (-centered.real) if centered.real < 0 else math.nan
                    ),
                    "q_reconstruction_error": reconstruction_error,
                }
            )

            re_centered.append(centered.real)
            abs_im_centered.append(abs(centered.imag))
            directional_errors.append(abs(directional))
            if centered.real < 0:
                abs_im_over_neg_re.append(abs(centered.imag) / (-centered.real))

    return {
        "rows": rows,
        "stats": {
            "re_centered": summarize(re_centered),
            "abs_im_centered": summarize(abs_im_centered),
            "abs_directional_increment_defect": summarize(directional_errors),
            "abs_im_over_neg_re": summarize(abs_im_over_neg_re) if abs_im_over_neg_re else None,
            "min_neg_re_centered": min((-x for x in re_centered if x < 0), default=math.nan),
        },
        "max_q_reconstruction_error": max_reconstruction_error,
    }


def main() -> None:
    result = {
        "statement": (
            "Centered quotient form of the denominator direction law: "
            "Delta d_N / d_N controls the directional increment defect exactly."
        ),
        "sources": {
            "zeta": str(SRC_ZETA),
            "plant": str(SRC_PLANT),
        },
        "builds": {
            "zeta": build_rows(load_points(SRC_ZETA)),
            "plant": build_rows(load_points(SRC_PLANT)),
        },
    }

    out_path = HERE / "E78_44_den_centered_quotient_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
