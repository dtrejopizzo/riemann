#!/usr/bin/env python3
from __future__ import annotations

import json
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
            one_minus_theta = complex(
                float(point["one_minus_theta"]["re"]),
                float(point["one_minus_theta"]["im"]),
            )
            pts[(sigma, section_n)] = one_minus_theta
    return pts


def build_rows(points: dict[tuple[str, int], complex]) -> dict[str, object]:
    rows = []
    max_abs_ratio_error = 0.0

    for sigma in sorted({s for s, _ in points}, key=float):
        ns = sorted(n for s, n in points if s == sigma)
        for n in ns:
            key_new = (sigma, n + 2)
            if key_new not in points:
                continue

            d_n = points[(sigma, n)]
            d_np2 = points[key_new]
            q = d_np2 / d_n
            ratio = abs(d_np2) / abs(d_n)
            ratio_error = abs(abs(q) - ratio)
            max_abs_ratio_error = max(max_abs_ratio_error, ratio_error)

            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "quotient_abs": abs(q),
                    "radial_ratio": ratio,
                    "radial_ratio_error": ratio_error,
                    "radial_deficit": 1.0 - ratio,
                    "old_den_abs": abs(d_n),
                    "new_den_abs": abs(d_np2),
                }
            )

    return {
        "rows": rows,
        "max_abs_ratio_error": max_abs_ratio_error,
    }


def main() -> None:
    result = {
        "statement": (
            "Radial contraction form of the denominator modulus deficit: "
            "|q_N| = |1-theta_{N+2}| / |1-theta_N|."
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

    out_path = HERE / "E78_47_den_radial_contraction_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
