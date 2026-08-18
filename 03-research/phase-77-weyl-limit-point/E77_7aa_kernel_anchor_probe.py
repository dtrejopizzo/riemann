#!/usr/bin/env python3
"""Probe the fixed-section kernel-anchor coupling in the intrinsic Schur block."""

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


def cserial(z, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def section(Hmax, idxmax, max_modes, modes):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def schur_packet(H: mp.matrix, idx: list[int], L: mp.mpf, sigma: mp.mpf, mu_reference: mp.mpf):
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


def kernel_anchor_data(packet):
    Sigma = packet["Sigma"]
    vals, vecs = mp.eighe(Sigma)
    idx0 = min(range(len(vals)), key=lambda j: abs(vals[j]))
    lam0 = vals[idx0]
    u0 = mp.matrix([[vecs[j, idx0]] for j in range(2)])
    overlap = mp.fsum(mp.conj(u0[j]) * packet["kappa"][j] for j in range(2))
    tau_u0 = (packet["tau"] * u0)[0]
    A0 = -overlap * tau_u0
    return lam0, overlap, tau_u0, A0


def run_build(label, lam, max_modes, dps, sigma0, planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_vals, _ = mp.eigsy(Hmax)
    mu_reference = max_vals[0]
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        packet = schur_packet(H, idx, L, sigma0, mu_reference)
        lam0, overlap, tau_u0, A0 = kernel_anchor_data(packet)
        rows.append(
            {
                "N": modes,
                "mu_reference": serial(mu_reference),
                "sigma0": serial(sigma0),
                "sigma_min_abs": serial(abs(lam0)),
                "kappa_overlap_abs": serial(abs(overlap)),
                "tau_u0_abs": serial(abs(tau_u0)),
                "A0_abs": serial(abs(A0)),
                "A0_over_overlap_tau": serial(abs(A0) / max(mp.mpf("1e-80"), abs(overlap) * abs(tau_u0))),
                "overlap": cserial(overlap),
                "tau_u0": cserial(tau_u0),
                "A0": cserial(A0),
            }
        )
        print(
            f"{label:8s} N={modes:2d} "
            f"|lam0|={serial(abs(lam0),8):>12s} "
            f"|<u0,k>|={serial(abs(overlap),8):>12s} "
            f"|tau u0|={serial(abs(tau_u0),8):>12s} "
            f"|A0|={serial(abs(A0),8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "reference_N": max_modes,
        "mu_reference": serial(mu_reference),
        "sigma0": serial(sigma0),
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
    parser.add_argument("--sigma0", default="1.0")
    parser.add_argument(
        "--output", type=Path, default=HERE / "E77_7aa_kernel_anchor_results.json"
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7aa requires dps >= 60")
    sigma0 = mp.mpf(args.sigma0)
    result = {
        "statement": "Fixed-section kernel-anchor coupling audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma0": serial(sigma0),
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, sigma0, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
