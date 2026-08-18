#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SRC = HERE / "E78_69_logq_barrier_results.json"


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(rows: list[dict[str, object]]) -> dict[str, object]:
    out = []
    quad_margins = []
    betas = []
    max_beta = 0.0
    for row in rows:
        a = float(row["re_delta_ell"])
        beta = float(row["wrapped_im_delta_ell_abs"])
        quad_barrier = beta * beta
        quad_margin = a - quad_barrier
        max_beta = max(max_beta, beta)
        betas.append(beta)
        quad_margins.append(quad_margin)
        out.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "to_N": row["to_N"],
                "re_delta_ell": a,
                "wrapped_im_delta_ell_abs": beta,
                "quadratic_barrier": quad_barrier,
                "quadratic_margin": quad_margin,
                "angular_barrier": float(row["angular_barrier"]),
                "barrier_margin": float(row["barrier_margin"]),
            }
        )
    return {
        "rows": out,
        "summary": {
            "wrapped_im_delta_ell_abs": summarize(betas),
            "quadratic_margin": summarize(quad_margins),
        },
        "max_beta": max_beta,
    }


def main() -> None:
    src = json.loads(SRC.read_text())
    result = {
        "statement": (
            "Quadratic sufficient barrier audit: on |beta|<=1, "
            "-log cos(beta) <= beta^2, so Re Delta ell > beta^2 implies the exact logq barrier."
        ),
        "sources": {"logq_barrier": str(SRC)},
        "builds": {
            "zeta": build_rows(src["builds"]["zeta"]["rows"]),
            "plant": build_rows(src["builds"]["plant"]["rows"]),
        },
    }
    out_path = HERE / "E78_70_logq_quadratic_barrier_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
