#!/usr/bin/env python3
"""Probe regularized projective transfer near singular fixed-mu sections."""

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


def regularized_profile(db, inner, A, b, L, eta, sigmas, sigma0):
    x = mp.lu_solve(A - 1j * eta * mp.eye(A.rows), b)
    anchor = transfer(1j * sigma0, db, inner, x, L)
    values = [transfer(1j * sigma, db, inner, x, L) / anchor for sigma in sigmas]
    return anchor, values


def spectral_gap_data(A, b):
    vals, vecs = mp.eighe(A)
    min_abs_idx = min(range(len(vals)), key=lambda j: abs(vals[j]))
    lam0 = vals[min_abs_idx]
    coeff0 = mp.fsum(mp.conj(vecs[k, min_abs_idx]) * b[k] for k in range(A.rows))
    return lam0, coeff0


def run_build(label, lam, max_modes, dps, sigmas, sigma0, etas, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_vals, _ = mp.eigsy(Hmax)
    mu_reference = max_vals[0]
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        db, inner, A, b = inner_data(H, idx, mu_reference)
        lam0, coeff0 = spectral_gap_data(A, b)
        profiles = []
        prev = None
        for eta in etas:
            anchor, values = regularized_profile(db, inner, A, b, L, eta, sigmas, sigma0)
            max_step = mp.mpf("0")
            if prev is not None:
                max_step = max(abs(values[j] - prev[j]) for j in range(len(sigmas)))
            profiles.append(
                {
                    "eta": serial(eta),
                    "anchor_abs": serial(abs(anchor)),
                    "max_profile_step_from_previous_eta": serial(max_step),
                }
            )
            prev = values
        rows.append(
            {
                "N": modes,
                "mu_reference": serial(mu_reference),
                "nearest_inner_eigenvalue_to_zero": serial(lam0),
                "nearest_inner_gap_abs": serial(abs(lam0)),
                "boundary_overlap_nearest_mode_abs": serial(abs(coeff0)),
                "profiles": profiles,
            }
        )
        print(
            f"{label:8s} N={modes:2d} gap={serial(abs(lam0), 8):>12s} "
            f"|c0|={serial(abs(coeff0), 8):>12s} "
            f"eta_last_step={profiles[-1]['max_profile_step_from_previous_eta']}",
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
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7p_singular_section_results.json"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7p requires dps >= 50")
    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    sigma0 = mp.mpf(args.sigma0)
    etas = [mp.mpf(value) for value in args.etas.split(",") if value]
    result = {
        "statement": "Regularized projective profile near singular fixed-mu sections",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma0": serial(sigma0),
            "sigmas": [serial(sigma) for sigma in sigmas],
            "etas": [serial(eta) for eta in etas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "mu_reference is a finite frozen surrogate. The probe checks "
            "whether projective profiles stabilize under resolvent "
            "regularization as eta -> 0."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, sigmas, sigma0, etas, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
