#!/usr/bin/env python3
"""E77.7b moving-mu versus fixed-mu R3 audit."""

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


def norm(vector: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vector[j]) ** 2 for j in range(vector.rows)))


def section(Hmax, idxmax, max_modes, modes):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def response(H, idx, mu):
    inner_matrix = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    source = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], mp.lu_solve(inner_matrix, source)


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
        moving_energy = norm(moving) ** 2
        frozen_energy = norm(frozen) ** 2
        transfer_errors = []
        for sigma in sigmas:
            z = 1j * sigma
            tm = transfer(z, db, inner, moving, L)
            tf = transfer(z, db, inner, frozen, L)
            transfer_errors.append(abs(tm - tf) / max(1, abs(tm)))
        rows.append(
            {
                "N": modes,
                "mu_moving": serial(mu_moving),
                "mu_reference": serial(mu_reference),
                "mu_difference": serial(abs(mu_moving - mu_reference)),
                "moving_energy": serial(moving_energy),
                "frozen_energy": serial(frozen_energy),
                "energy_ratio_frozen_over_moving": serial(frozen_energy / moving_energy),
                "max_safe_transfer_relative_difference": serial(max(transfer_errors)),
            }
        )
        print(
            f"{label:8s} N={modes:2d} mu={serial(mu_moving, 8):>13s} "
            f"dmu={serial(abs(mu_moving-mu_reference), 8):>12s} "
            f"Ef/Em={serial(frozen_energy/moving_energy, 8):>12s} "
            f"dT={serial(max(transfer_errors), 8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "reference_N": max_modes,
        "mu_reference": serial(mu_reference),
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
    parser.add_argument("--sigmas", default="0.6,1.0,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_7b_mu_limit_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7b requires dps >= 50")
    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    result = {
        "statement": "Moving finite ground point versus largest-section frozen point",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(sigma) for sigma in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": "The largest-section point is a numerical reference, not a proved infinite-volume limit.",
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
