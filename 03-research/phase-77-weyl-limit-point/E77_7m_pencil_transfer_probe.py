#!/usr/bin/env python3
"""Probe projective mu-transfer compatibility on safe compacta."""

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
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def response(H, idx, mu):
    inner_matrix = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    source = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], mp.lu_solve(inner_matrix, source)


def projective_profile(db, inner, x, L, sigmas, sigma0):
    anchor = transfer(1j * sigma0, db, inner, x, L)
    values = []
    for sigma in sigmas:
        values.append(transfer(1j * sigma, db, inner, x, L) / anchor)
    return anchor, values


def run_build(label, lam, max_modes, dps, sigmas, sigma0, planted):
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
        anchor_m, prof_m = projective_profile(db, inner, moving, L, sigmas, sigma0)
        anchor_f, prof_f = projective_profile(db, inner, frozen, L, sigmas, sigma0)
        absolute_errors = [abs(prof_m[j] - prof_f[j]) for j in range(len(sigmas))]
        relative_errors = [
            abs(prof_m[j] - prof_f[j]) / max(1, abs(prof_m[j]), abs(prof_f[j]))
            for j in range(len(sigmas))
        ]
        rows.append(
            {
                "N": modes,
                "mu_moving": serial(mu_moving),
                "mu_reference": serial(mu_reference),
                "mu_difference": serial(abs(mu_moving - mu_reference)),
                "anchor_moving_abs": serial(abs(anchor_m)),
                "anchor_frozen_abs": serial(abs(anchor_f)),
                "max_projective_absolute_difference": serial(max(absolute_errors)),
                "max_projective_relative_difference": serial(max(relative_errors)),
            }
        )
        print(
            f"{label:8s} N={modes:2d} dmu={serial(abs(mu_moving - mu_reference), 8):>12s} "
            f"|a_m|={serial(abs(anchor_m), 8):>12s} "
            f"|a_f|={serial(abs(anchor_f), 8):>12s} "
            f"dProj={serial(max(relative_errors), 8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "reference_N": max_modes,
        "mu_reference": serial(mu_reference),
        "sigma0": serial(sigma0),
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
    parser.add_argument("--sigmas", default="0.6,1.0,2.0,3.0")
    parser.add_argument("--sigma0", default="1.0")
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7m_pencil_transfer_results.json"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7m requires dps >= 50")
    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    sigma0 = mp.mpf(args.sigma0)
    result = {
        "statement": "Projectively normalized moving-mu versus frozen-mu transfer",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma0": serial(sigma0),
            "sigmas": [serial(sigma) for sigma in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "The largest-section point is only a finite frozen reference. "
            "This probe audits whether projective normalization removes the "
            "moving/frozen resonance sensitivity."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, sigmas, sigma0, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
