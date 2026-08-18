#!/usr/bin/env python3
"""Probe intrinsic Schur regularizations of the singular fixed-mu section."""

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
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E77_5f_shell_resolvent_probe import solve_matrix  # noqa: E402


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def section(Hmax, idxmax, max_modes, modes):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def shell_data(H: mp.matrix, idx: list[int], L: mp.mpf, sigma: mp.mpf, mu_reference: mp.mpf):
    z = 1j * sigma
    Hshift = H - mu_reference * mp.eye(H.rows)
    _mu, A, db_idx, inner, _direct_x = right_transfer_data(Hshift, idx)
    core = A[1:-1, 1:-1]
    shell_nodes = [inner[0], inner[-1]]
    core_nodes = inner[1:-1]

    U = mp.matrix(core.rows, 2)
    for j in range(core.rows):
        U[j, 0] = A[j + 1, 0]
        U[j, 1] = A[j + 1, A.cols - 1]
    Cmat = mp.matrix(
        [
            [A[0, 0], A[0, A.cols - 1]],
            [A[A.rows - 1, 0], A[A.rows - 1, A.cols - 1]],
        ]
    )
    core_solve_U = solve_matrix(core, U)
    Sigma = Cmat - U.T * core_solve_U

    g_full = mp.matrix([Hshift[j + 1, Hshift.cols - 1] for j in range(Hshift.rows - 2)])
    g_core = g_full[1:-1, :]
    g_shell = mp.matrix([g_full[0], g_full[g_full.rows - 1]])
    core_solve_g = mp.lu_solve(core, g_core)
    kappa = g_shell - U.T * core_solve_g

    db = 2 * mp.pi * db_idx / L
    core_d = [2 * mp.pi * n / L for n in core_nodes]
    shell_d = [2 * mp.pi * n / L for n in shell_nodes]
    r_core = mp.matrix([[1 / (z - d) for d in core_d]])
    r_shell = mp.matrix([[1 / (z - d) for d in shell_d]])
    tau = r_shell - r_core * core_solve_U
    t0 = 1 / (z - db) - (r_core * core_solve_g)[0]
    return {"Sigma": Sigma, "kappa": kappa, "tau": tau, "t0": t0}


def solve_shifted(Sigma: mp.matrix, kappa: mp.matrix, eta: mp.mpf) -> mp.matrix:
    return mp.lu_solve(Sigma - 1j * eta * mp.eye(2), kappa)


def smallest_mode_deflated(Sigma: mp.matrix, kappa: mp.matrix) -> tuple[mp.matrix, mp.mpf, mp.matrix]:
    vals, vecs = mp.eighe(Sigma)
    idx0 = min(range(len(vals)), key=lambda j: abs(vals[j]))
    lam0 = vals[idx0]
    u0 = mp.matrix([[vecs[j, idx0]] for j in range(2)])
    coeff = mp.fsum(mp.conj(u0[j]) * kappa[j] for j in range(2))
    residual = mp.matrix(kappa - coeff * u0)
    return residual, lam0, u0


def theta_from_v(tau: mp.matrix, v: mp.matrix, t0):
    return (tau * v)[0] / t0


def run_build(label, lam, max_modes, dps, sigmas, sigma0, etas, planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_vals, _ = mp.eigsy(Hmax)
    mu_reference = max_vals[0]
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        sigma_packets = {}
        for sigma in [sigma0] + [s for s in sigmas if s != sigma0]:
            sigma_packets[str(sigma)] = shell_data(H, idx, L, sigma, mu_reference)
        base = sigma_packets[str(sigma0)]
        Sigma = base["Sigma"]
        kappa = base["kappa"]
        residual, lam0, u0 = smallest_mode_deflated(Sigma, kappa)
        coeff0 = mp.fsum(mp.conj(u0[j]) * kappa[j] for j in range(2))

        eta_profiles = []
        prev_shift = None
        for eta in etas:
            shift_anchor = None
            shift_values = []
            for sigma in sigmas:
                packet = sigma_packets[str(sigma)]
                v_shift = solve_shifted(packet["Sigma"], packet["kappa"], eta)
                theta_shift = theta_from_v(packet["tau"], v_shift, packet["t0"])
                if sigma == sigma0:
                    shift_anchor = 1 - theta_shift
                shift_values.append(1 - theta_shift)
            shift_profile = [value / shift_anchor for value in shift_values]
            shift_step = mp.mpf("0") if prev_shift is None else max(
                abs(shift_profile[j] - prev_shift[j]) for j in range(len(sigmas))
            )
            eta_profiles.append(
                {
                    "eta": serial(eta),
                    "shift_anchor_abs": serial(abs(shift_anchor)),
                    "shift_max_profile_step_from_previous_eta": serial(shift_step),
                }
            )
            prev_shift = shift_profile

        deflated_anchor = None
        deflated_values = []
        raw_anchor = None
        raw_values = []
        min_sigma_eig = mp.inf
        for sigma in sigmas:
            packet = sigma_packets[str(sigma)]
            vals = mp.eigsy(packet["Sigma"])[0]
            min_sigma_eig = min(min_sigma_eig, min(abs(vals[j]) for j in range(vals.rows)))
            v_raw = mp.lu_solve(packet["Sigma"], packet["kappa"])
            theta_raw = theta_from_v(packet["tau"], v_raw, packet["t0"])
            v_deflated = mp.lu_solve(packet["Sigma"], residual)
            theta_deflated = theta_from_v(packet["tau"], v_deflated, packet["t0"])
            raw_factor = 1 - theta_raw
            def_factor = 1 - theta_deflated
            if sigma == sigma0:
                raw_anchor = raw_factor
                deflated_anchor = def_factor
            raw_values.append(raw_factor)
            deflated_values.append(def_factor)
        raw_profile = [value / raw_anchor for value in raw_values]
        deflated_profile = [value / deflated_anchor for value in deflated_values]
        deflated_vs_raw = max(
            abs(deflated_profile[j] - raw_profile[j]) / max(1, abs(raw_profile[j]), abs(deflated_profile[j]))
            for j in range(len(sigmas))
        )
        rows.append(
            {
                "N": modes,
                "mu_reference": serial(mu_reference),
                "nearest_sigma_eigenvalue_abs": serial(abs(lam0)),
                "nearest_sigma_mode_overlap_abs": serial(abs(coeff0)),
                "min_sigma_eigenvalue_abs_across_sigmas": serial(min_sigma_eig),
                "raw_anchor_abs": serial(abs(raw_anchor)),
                "deflated_anchor_abs": serial(abs(deflated_anchor)),
                "max_deflated_vs_raw_projective_relative_difference": serial(deflated_vs_raw),
                "eta_profiles": eta_profiles,
            }
        )
        print(
            f"{label:8s} N={modes:2d} "
            f"|lam0|={serial(abs(lam0),8):>12s} "
            f"|<u0,k>|={serial(abs(coeff0),8):>12s} "
            f"shift_last={eta_profiles[-1]['shift_max_profile_step_from_previous_eta']:>12s} "
            f"def/raw={serial(deflated_vs_raw,8):>12s}",
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
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--sigmas", default="0.6,1.0,2.0,3.0")
    parser.add_argument("--sigma0", default="1.0")
    parser.add_argument("--etas", default="1e-2,1e-4,1e-6,1e-8")
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7y_intrinsic_schur_regularization_results.json"
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7y requires dps >= 60")
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    sigma0 = mp.mpf(args.sigma0)
    etas = [mp.mpf(value) for value in args.etas.split(",") if value]
    result = {
        "statement": "Intrinsic Schur regularization audit",
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
            "mu_reference is a finite frozen surrogate. The probe acts only on "
            "the intrinsic 2x2 Schur package Sigma^{-1}kappa and the paired "
            "factor 1-theta."
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
