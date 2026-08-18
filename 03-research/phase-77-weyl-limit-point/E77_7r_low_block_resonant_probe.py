#!/usr/bin/env python3
"""Probe low-block resonant subtraction for singular-section regularization."""

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


def inner_data(H, idx, mu):
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return idx[-1], idx[1:-1], A, b


def cauchy_apply(db, inner, vec, L, sigma):
    return transfer(1j * sigma, db, inner, vec, L)


def spectral_block_data(A, b, block_size):
    vals, vecs = mp.eighe(A)
    order = sorted(range(len(vals)), key=lambda j: abs(vals[j]))
    chosen = order[: min(block_size, len(order))]
    resonant = []
    for j in chosen:
        lam = vals[j]
        u = mp.matrix([vecs[k, j] for k in range(A.rows)])
        coeff = mp.fsum(mp.conj(u[k]) * b[k] for k in range(A.rows))
        resonant.append((lam, u, coeff))
    return resonant


def regularized_vectors(A, b, resonant_block, eta):
    x = mp.lu_solve(A - 1j * eta * mp.eye(A.rows), b)
    block = mp.matrix(A.rows, 1)
    for lam, u, coeff in resonant_block:
        block += (coeff / (lam - 1j * eta)) * u
    regular = x - block
    return x, block, regular


def profile_from_vec(db, inner, vec, L, sigmas, sigma0):
    anchor = cauchy_apply(db, inner, vec, L, sigma0)
    values = [cauchy_apply(db, inner, vec, L, sigma) / anchor for sigma in sigmas]
    return anchor, values


def run_build(label, lam, max_modes, dps, sigmas, sigma0, etas, planted, block_size):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_vals, _ = mp.eigsy(Hmax)
    mu_reference = max_vals[0]
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        db, inner, A, b = inner_data(H, idx, mu_reference)
        resonant_block = spectral_block_data(A, b, block_size)
        raw_prev = None
        reg_prev = None
        profiles = []
        for eta in etas:
            x, block, regular = regularized_vectors(A, b, resonant_block, eta)
            raw_anchor, raw_vals = profile_from_vec(db, inner, x, L, sigmas, sigma0)
            reg_anchor, reg_vals = profile_from_vec(db, inner, regular, L, sigmas, sigma0)
            block_anchor = cauchy_apply(db, inner, block, L, sigma0)
            raw_step = mp.mpf("0") if raw_prev is None else max(
                abs(raw_vals[j] - raw_prev[j]) for j in range(len(sigmas))
            )
            reg_step = mp.mpf("0") if reg_prev is None else max(
                abs(reg_vals[j] - reg_prev[j]) for j in range(len(sigmas))
            )
            profiles.append(
                {
                    "eta": serial(eta),
                    "raw_anchor_abs": serial(abs(raw_anchor)),
                    "regular_anchor_abs": serial(abs(reg_anchor)),
                    "block_anchor_abs": serial(abs(block_anchor)),
                    "raw_max_profile_step_from_previous_eta": serial(raw_step),
                    "regular_max_profile_step_from_previous_eta": serial(reg_step),
                }
            )
            raw_prev = raw_vals
            reg_prev = reg_vals
        rows.append(
            {
                "N": modes,
                "mu_reference": serial(mu_reference),
                "block_size": len(resonant_block),
                "resonant_eigenvalues_abs": [serial(abs(item[0])) for item in resonant_block],
                "resonant_overlaps_abs": [serial(abs(item[2])) for item in resonant_block],
                "profiles": profiles,
            }
        )
        print(
            f"{label:8s} N={modes:2d} block={len(resonant_block):1d} "
            f"raw_last={profiles[-1]['raw_max_profile_step_from_previous_eta']} "
            f"reg_last={profiles[-1]['regular_max_profile_step_from_previous_eta']}",
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
        "etas": [serial(eta) for eta in etas],
        "block_size": block_size,
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
    parser.add_argument("--etas", default="1e-2,1e-4,1e-6,1e-8")
    parser.add_argument("--block-size", type=int, default=3)
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7r_low_block_resonant_results.json"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7r requires dps >= 50")
    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    sigma0 = mp.mpf(args.sigma0)
    etas = [mp.mpf(value) for value in args.etas.split(",") if value]
    result = {
        "statement": "Low-block resonant subtraction audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma0": serial(sigma0),
            "sigmas": [serial(sigma) for sigma in sigmas],
            "etas": [serial(eta) for eta in etas],
            "block_size": args.block_size,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "mu_reference is a finite frozen surrogate. The probe checks "
            "whether subtracting a low-dimensional resonant block stabilizes "
            "the regularized projective profile."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(
                label,
                args.lam,
                args.max_modes,
                args.dps,
                sigmas,
                sigma0,
                etas,
                planted,
                args.block_size,
            )
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
