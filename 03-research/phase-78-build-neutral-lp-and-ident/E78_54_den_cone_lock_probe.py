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
            pts[(point["sigma"], int(point["section_N"]))] = complex(
                float(point["one_minus_theta"]["re"]),
                float(point["one_minus_theta"]["im"]),
            )
    return pts


def build_rows(points: dict[tuple[str, int], complex]) -> dict[str, object]:
    rows = []
    max_reconstruction_error = 0.0
    for sigma in sorted({s for s, _ in points}, key=float):
        ns = sorted(n for s, n in points if s == sigma)
        for n in ns:
            nxt = (sigma, n + 2)
            if nxt not in points:
                continue
            d_n = points[(sigma, n)]
            d_np2 = points[nxt]
            delta = d_np2 - d_n
            delta_abs = abs(delta)
            d_abs = abs(d_n)
            size_ratio = delta_abs / d_abs
            cos_theta = ((delta.real * d_n.real) + (delta.imag * d_n.imag)) / (delta_abs * d_abs)
            cone_margin = -(size_ratio + 2.0 * cos_theta)
            euclidean_margin = -2.0 * ((delta.real * d_n.real) + (delta.imag * d_n.imag)) - delta_abs**2
            reconstructed = euclidean_margin / (delta_abs * d_abs)
            err = abs(cone_margin - reconstructed)
            max_reconstruction_error = max(max_reconstruction_error, err)
            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": n + 2,
                    "delta_abs": delta_abs,
                    "old_den_abs": d_abs,
                    "size_ratio": size_ratio,
                    "cos_increment_angle": cos_theta,
                    "cone_margin": cone_margin,
                    "euclidean_margin": euclidean_margin,
                    "normalized_euclidean_margin": reconstructed,
                    "reconstruction_error": err,
                }
            )
    return {
        "rows": rows,
        "max_reconstruction_error": max_reconstruction_error,
    }


def main() -> None:
    result = {
        "statement": (
            "Cone form of the denominator Euclidean lock: "
            "-2<Delta d_N,d_N> > |Delta d_N|^2 iff |Delta d_N|/|d_N| + 2 cos(angle)<0."
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

    out_path = HERE / "E78_54_den_cone_lock_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
