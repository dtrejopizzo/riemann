#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PHASE_G = PHASE77 / "E77_5g_schur_phase_increment_results.json"
SIGMA0 = "0.550000000000000044408921"


def wrap_to_pi(x: float) -> float:
    return math.atan2(math.sin(x), math.cos(x))


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(build_is_plant: bool) -> dict[str, object]:
    obj = json.loads(PHASE_G.read_text())
    case = None
    for candidate in obj["cases"]:
        if bool(candidate["planted"]) == build_is_plant:
            case = candidate
            break
    assert case is not None

    base_by_n: dict[int, float] = {}
    rows = []
    margins = []
    tail_losses = []
    phase_squares = []

    for inc in case["increments"]:
        n = int(inc["from_N"])
        for row in inc["sigmas"]:
            sigma = row["sigma"]
            re_delta = float(row["delta_log_one_minus_theta"]["re"])
            im_delta = float(row["delta_log_one_minus_theta"]["im"])
            if sigma == SIGMA0:
                base_by_n[n] = re_delta

    for inc in case["increments"]:
        n = int(inc["from_N"])
        for row in inc["sigmas"]:
            sigma = row["sigma"]
            re_delta = float(row["delta_log_one_minus_theta"]["re"])
            im_delta = float(row["delta_log_one_minus_theta"]["im"])
            beta = abs(wrap_to_pi(im_delta))
            beta_sq = beta * beta
            base = base_by_n[n]
            tail_loss = base - re_delta
            reserve_margin = base - tail_loss - beta_sq
            direct_margin = re_delta - beta_sq
            err = abs(reserve_margin - direct_margin)
            margins.append(reserve_margin)
            tail_losses.append(tail_loss)
            phase_squares.append(beta_sq)
            rows.append(
                {
                    "sigma": sigma,
                    "N": n,
                    "to_N": int(inc["to_N"]),
                    "basepoint_reserve": base,
                    "tail_loss": tail_loss,
                    "wrapped_phase_abs": beta,
                    "wrapped_phase_square": beta_sq,
                    "reserve_margin": reserve_margin,
                    "direct_quadratic_margin": direct_margin,
                    "reconstruction_error": err,
                }
            )

    return {
        "rows": rows,
        "summary": {
            "reserve_margin": summarize(margins),
            "tail_loss": summarize(tail_losses),
            "wrapped_phase_square": summarize(phase_squares),
        },
        "max_reconstruction_error": max(row["reconstruction_error"] for row in rows),
    }


def main() -> None:
    result = {
        "statement": (
            "Reserve-budget identity at sigma0=0.55: "
            "Re Delta ell_N(i sigma) - |wrap Im Delta ell_N(i sigma)|^2 = "
            "BASE_N(0.55) - TAIL_N(0.55,sigma) - |wrap Im Delta ell_N(i sigma)|^2."
        ),
        "sources": {"phase_g": str(PHASE_G)},
        "builds": {
            "zeta": build_rows(False),
            "plant": build_rows(True),
        },
    }
    out_path = HERE / "E78_74_reserve_budget_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
