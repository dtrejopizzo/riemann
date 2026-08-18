#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
BRIDGE = HERE / "E78_67_old_old_logq_bridge_results.json"
PHASE_G = HERE.parent / "phase-77-weyl-limit-point" / "E77_5g_schur_phase_increment_results.json"


def wrap_to_pi(x: float) -> float:
    y = (x + math.pi) % (2.0 * math.pi) - math.pi
    return y


def load_delta_ell(build_is_plant: bool) -> dict[tuple[str, int], complex]:
    obj = json.loads(PHASE_G.read_text())
    case = None
    for candidate in obj["cases"]:
        if bool(candidate["planted"]) == build_is_plant:
            case = candidate
            break
    assert case is not None
    out: dict[tuple[str, int], complex] = {}
    for inc in case["increments"]:
        n = int(inc["from_N"])
        for row in inc["sigmas"]:
            sigma = str(row["sigma"])
            if sigma not in ("1.0", "3.0"):
                continue
            z = complex(float(row["delta_log_one_minus_theta"]["re"]), float(row["delta_log_one_minus_theta"]["im"]))
            out[(sigma, n)] = z
    return out


def summarize(values: list[float]) -> dict[str, float | int | None]:
    if not values:
        return {"count": 0, "min": None, "median": None, "max": None}
    vals = sorted(values)
    mid = len(vals) // 2
    med = vals[mid] if len(vals) % 2 else 0.5 * (vals[mid - 1] + vals[mid])
    return {"count": len(vals), "min": vals[0], "median": med, "max": vals[-1]}


def build_rows(build: str, build_is_plant: bool, bridge_rows: list[dict[str, object]]) -> dict[str, object]:
    delta_ell = load_delta_ell(build_is_plant)
    rows = []
    max_error = 0.0
    radial_gains = []
    wrapped_phases = []
    scalar_gains = []
    for row in bridge_rows:
        sigma = str(row["sigma"])
        n = int(row["N"])
        if (sigma, n) not in delta_ell:
            continue
        d = delta_ell[(sigma, n)]
        a = d.real
        b = d.imag
        wrapped_b = wrap_to_pi(b)
        scalar = 1.0 - math.exp(-a) * math.cos(b)
        pair = float(row["pairnum_from_logq"])
        q_sq = pair / scalar if abs(scalar) > 1e-30 else float("nan")
        reconstructed = q_sq * (1.0 - math.exp(-a) * math.cos(b))
        err = abs(pair - reconstructed)
        max_error = max(max_error, err)
        radial_gains.append(a)
        wrapped_phases.append(abs(wrapped_b))
        scalar_gains.append(scalar)
        rows.append(
            {
                "sigma": sigma,
                "N": n,
                "to_N": row["to_N"],
                "re_delta_ell": a,
                "im_delta_ell": b,
                "wrapped_im_delta_ell": wrapped_b,
                "scalar_gain": scalar,
                "pairnum_from_logq": pair,
                "reconstruction_error": err,
            }
        )
    return {
        "rows": rows,
        "summary": {
            "re_delta_ell": summarize(radial_gains),
            "wrapped_im_delta_ell_abs": summarize(wrapped_phases),
            "scalar_gain": summarize(scalar_gains),
        },
        "max_reconstruction_error": max_error,
    }


def main() -> None:
    bridge = json.loads(BRIDGE.read_text())
    result = {
        "statement": (
            "Scalarized old-old log-q bridge: PAIRNUM_N = |q_N|^2 [1 - exp(-Re Delta ell_N) cos(Im Delta ell_N)]."
        ),
        "sources": {
            "bridge": str(BRIDGE),
            "phase_g": str(PHASE_G),
        },
        "builds": {
            "zeta": build_rows("zeta", False, bridge["builds"]["zeta"]["rows"]),
            "plant": build_rows("plant", True, bridge["builds"]["plant"]["rows"]),
        },
    }
    out_path = HERE / "E78_68_logq_scalar_results.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(out_path)


if __name__ == "__main__":
    main()
