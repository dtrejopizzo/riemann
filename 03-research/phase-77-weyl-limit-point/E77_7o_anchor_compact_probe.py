#!/usr/bin/env python3
"""Probe anchor nonvanishing on a safe sigma compact."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_018_boundary_characteristic_probe import transfer  # noqa: E402


GAMMA = "14.134725141734693790"


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def section(Hmax, idxmax, max_modes, modes):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : len(idxmax) - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def response(H, idx, mu):
    inner_matrix = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    source = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], mp.lu_solve(inner_matrix, source)


def sample_anchor_curve(db, inner, x, L, sigmas):
    values = [abs(transfer(1j * sigma, db, inner, x, L)) for sigma in sigmas]
    min_idx = min(range(len(values)), key=lambda j: values[j])
    return values, min_idx


def run_build(label, lam, max_modes, dps, sigmas, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_eigenvalues, _ = mp.eigsy(Hmax)
    mu_reference = max_eigenvalues[0]
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        eigenvalues, _ = mp.eigsy(H)
        mu_moving = eigenvalues[0]
        db, inner, moving = response(H, idx, mu_moving)
        _db, _inner, frozen = response(H, idx, mu_reference)
        moving_vals, moving_min_idx = sample_anchor_curve(db, inner, moving, L, sigmas)
        frozen_vals, frozen_min_idx = sample_anchor_curve(db, inner, frozen, L, sigmas)
        rows.append(
            {
                "N": modes,
                "mu_moving": serial(mu_moving),
                "mu_reference": serial(mu_reference),
                "min_anchor_moving_abs": serial(moving_vals[moving_min_idx]),
                "min_anchor_moving_sigma": serial(sigmas[moving_min_idx]),
                "min_anchor_frozen_abs": serial(frozen_vals[frozen_min_idx]),
                "min_anchor_frozen_sigma": serial(sigmas[frozen_min_idx]),
                "max_anchor_ratio_moving_over_frozen": serial(
                    max(
                        moving_vals[j] / frozen_vals[j] if frozen_vals[j] != 0 else mp.inf
                        for j in range(len(sigmas))
                    )
                ),
                "min_anchor_ratio_moving_over_frozen": serial(
                    min(
                        moving_vals[j] / frozen_vals[j] if frozen_vals[j] != 0 else mp.inf
                        for j in range(len(sigmas))
                    )
                ),
            }
        )
        print(
            f"{label:8s} N={modes:2d} "
            f"min|a_m|={serial(moving_vals[moving_min_idx], 8):>12s}@{serial(sigmas[moving_min_idx],4):>4s} "
            f"min|a_f|={serial(frozen_vals[frozen_min_idx], 8):>12s}@{serial(sigmas[frozen_min_idx],4):>4s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "reference_N": max_modes,
        "mu_reference": serial(mu_reference),
        "sigmas": [serial(sigma) for sigma in sigmas],
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigma-min", default="0.6")
    parser.add_argument("--sigma-max", default="3.0")
    parser.add_argument("--sigma-steps", type=int, default=13)
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7o_anchor_compact_results.json"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7o requires dps >= 50")
    mp.mp.dps = args.dps
    sigma_min = mp.mpf(args.sigma_min)
    sigma_max = mp.mpf(args.sigma_max)
    sigmas = [
        sigma_min + (sigma_max - sigma_min) * j / (args.sigma_steps - 1)
        for j in range(args.sigma_steps)
    ]
    result = {
        "statement": "Safe-compact anchor nonvanishing audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma_min": serial(sigma_min),
            "sigma_max": serial(sigma_max),
            "sigma_steps": args.sigma_steps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "This is a finite safe-compact audit of the anchor |T_N(i sigma;mu)|. "
            "It does not prove nonvanishing at the true mu_L."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, sigmas, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
