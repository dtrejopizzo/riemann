#!/usr/bin/env python3
"""Probe a nonspectral Krylov resonant block for singular regularization."""

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


def norm(vec):
    return mp.sqrt(mp.fsum(abs(vec[j]) ** 2 for j in range(vec.rows)))


def proj_coeff(u, v):
    return mp.fsum(mp.conj(u[j]) * v[j] for j in range(u.rows))


def orthonormalize(candidates, tol=mp.mpf("1e-30")):
    basis = []
    for vec in candidates:
        w = mp.matrix(vec)
        for u in basis:
            coeff = proj_coeff(u, w)
            w -= coeff * u
        nrm = norm(w)
        if nrm > tol:
            basis.append(w / nrm)
    return basis


def krylov_basis(A, b, block_size):
    vectors = []
    current = mp.matrix(b)
    for _ in range(block_size):
        vectors.append(current)
        current = A * current
    return orthonormalize(vectors)


def basis_projector_action(basis, vec):
    result = mp.matrix(vec.rows, 1)
    for u in basis:
        result += proj_coeff(u, vec) * u
    return result


def regularized_vectors(A, b, basis, eta):
    x = mp.lu_solve(A - 1j * eta * mp.eye(A.rows), b)
    block = basis_projector_action(basis, x)
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
        basis = krylov_basis(A, b, block_size)
        raw_prev = None
        reg_prev = None
        profiles = []
        for eta in etas:
            x, block, regular = regularized_vectors(A, b, basis, eta)
            raw_anchor, raw_vals = profile_from_vec(db, inner, x, L, sigmas, sigma0)
            reg_anchor, reg_vals = profile_from_vec(db, inner, regular, L, sigmas, sigma0)
            raw_step = mp.mpf("0") if raw_prev is None else max(
                abs(raw_vals[j] - raw_prev[j]) for j in range(len(sigmas))
            )
            reg_step = mp.mpf("0") if reg_prev is None else max(
                abs(reg_vals[j] - reg_prev[j]) for j in range(len(sigmas))
            )
            profiles.append(
                {
                    "eta": serial(eta),
                    "basis_size": len(basis),
                    "raw_anchor_abs": serial(abs(raw_anchor)),
                    "regular_anchor_abs": serial(abs(reg_anchor)),
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
                "basis_size": len(basis),
                "profiles": profiles,
            }
        )
        print(
            f"{label:8s} N={modes:2d} basis={len(basis):1d} "
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
        "--output", type=Path, default=HERE / "E77_7v_nonspectral_krylov_results.json"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7v requires dps >= 50")
    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    sigma0 = mp.mpf(args.sigma0)
    etas = [mp.mpf(value) for value in args.etas.split(",") if value]
    result = {
        "statement": "Nonspectral Krylov resonant block audit",
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
            "mu_reference is a finite frozen surrogate. The probe uses a "
            "genuinely nonspectral Krylov block generated from the boundary "
            "source b_N."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, sigmas, sigma0, etas, planted, args.block_size)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
