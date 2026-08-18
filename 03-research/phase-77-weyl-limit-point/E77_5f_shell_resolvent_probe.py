#!/usr/bin/env python3
"""E77.5f 2x2 shell-resolvent audit for the transfer log update.

For a section with right boundary b, split the inner shifted system into
core A and the two extreme inner shell modes.  The direct transfer is

    T = t0 - tau Sigma^{-1} kappa,

with the same formula for T'.  This probe verifies the identity for the
shifted Phase-77 transfer and measures the logarithmic contribution of the
2x2 shell correction.
"""

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
from P76_035_safe_log_derivative_probe import transfer_prime  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data, serial  # noqa: E402


def norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def solve_matrix(A: mp.matrix, B: mp.matrix) -> mp.matrix:
    X = mp.matrix(A.rows, B.cols)
    for c in range(B.cols):
        sol = mp.lu_solve(A, B[:, c])
        for r in range(A.rows):
            X[r, c] = sol[r]
    return X


def transfer(z, db_idx, inner_idx, x, L):
    db = 2 * mp.pi * db_idx / L
    return 1 / (z - db) - mp.fsum(
        x[j] / (z - 2 * mp.pi * inner_idx[j] / L) for j in range(x.rows)
    )


def shell_resolvent_data(H, idx, L, sigma):
    z = 1j * sigma
    mu, Hinner_shift, db_idx, inner, direct_x = right_transfer_data(H, idx)
    if len(inner) < 5:
        raise ValueError("need at least two shell nodes and a nontrivial core")

    core = Hinner_shift[1:-1, 1:-1]
    shell_nodes = [inner[0], inner[-1]]
    core_nodes = inner[1:-1]

    U = mp.matrix(core.rows, 2)
    for j in range(core.rows):
        U[j, 0] = Hinner_shift[j + 1, 0]
        U[j, 1] = Hinner_shift[j + 1, Hinner_shift.cols - 1]
    C = mp.matrix(
        [
            [Hinner_shift[0, 0], Hinner_shift[0, Hinner_shift.cols - 1]],
            [Hinner_shift[Hinner_shift.rows - 1, 0], Hinner_shift[Hinner_shift.rows - 1, Hinner_shift.cols - 1]],
        ]
    )
    core_solve_U = solve_matrix(core, U)
    Sigma = C - U.T * core_solve_U

    g_full = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    g_core = g_full[1:-1, :]
    g_shell = mp.matrix([g_full[0], g_full[g_full.rows - 1]])
    core_solve_g = mp.lu_solve(core, g_core)
    kappa = g_shell - U.T * core_solve_g

    db = 2 * mp.pi * db_idx / L
    core_d = [2 * mp.pi * n / L for n in core_nodes]
    shell_d = [2 * mp.pi * n / L for n in shell_nodes]
    r_core = mp.matrix([[1 / (z - d) for d in core_d]])
    rp_core = mp.matrix([[-1 / (z - d) ** 2 for d in core_d]])
    r_shell = mp.matrix([[1 / (z - d) for d in shell_d]])
    rp_shell = mp.matrix([[-1 / (z - d) ** 2 for d in shell_d]])

    t0 = 1 / (z - db) - (r_core * core_solve_g)[0]
    t0p = -1 / (z - db) ** 2 - (rp_core * core_solve_g)[0]
    tau = r_shell - r_core * core_solve_U
    taup = rp_shell - rp_core * core_solve_U
    shell_solution = mp.lu_solve(Sigma, kappa)
    corr = (tau * shell_solution)[0]
    corrp = (taup * shell_solution)[0]
    generated = t0 - corr
    generated_p = t0p - corrp

    direct_t = transfer(z, db_idx, inner, direct_x, L)
    direct_p = transfer_prime(z, db_idx, inner, direct_x, L)
    log_direct = direct_p / direct_t
    log_core = t0p / t0
    log_generated = generated_p / generated
    shell_log_update = log_generated - log_core
    identity_error = max(
        abs(generated - direct_t) / max(1, abs(direct_t)),
        abs(log_generated - log_direct) / max(1, abs(log_direct)),
    )
    return {
        "sigma": serial(sigma),
        "identity_error": serial(identity_error),
        "T_abs": serial(abs(generated)),
        "core_T_abs": serial(abs(t0)),
        "correction_abs": serial(abs(corr)),
        "correction_over_core": serial(abs(corr) / abs(t0) if t0 else mp.inf),
        "shell_log_update_abs": serial(abs(2 * mp.re(1j * shell_log_update))),
        "core_log_abs": serial(abs(2 * mp.re(1j * log_core))),
        "sigma_min_abs": serial(min(abs(mp.eigsy(Sigma)[0][j]) for j in range(Sigma.rows))),
        "shell_solution_norm": serial(norm(shell_solution)),
        "tau_norm": serial(norm(tau.T)),
    }


def run_build(label, lam, max_modes, dps, sigmas, planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for n_modes in range(8, max_modes + 1, 2):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        sigma_rows = [shell_resolvent_data(H, idx, L, sigma) for sigma in sigmas]
        max_id = max(mp.mpf(r["identity_error"]) for r in sigma_rows)
        max_shell = max(mp.mpf(r["shell_log_update_abs"]) for r in sigma_rows)
        max_corr = max(mp.mpf(r["correction_over_core"]) for r in sigma_rows)
        rows.append(
            {
                "N": n_modes,
                "max_identity_error": serial(max_id),
                "max_shell_log_update_abs": serial(max_shell),
                "max_correction_over_core": serial(max_corr),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} N={n_modes:2d} id={serial(max_id,8):>12s} "
            f"shellLog={serial(max_shell,8):>12s} corr/core={serial(max_corr,8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "N_max": max_modes,
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5f_shell_resolvent_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.5f requires dps >= 50")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "2x2 shell Schur resolvent for shifted transfer",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [
        (f"zeta-lam{args.lam}", None),
        (f"plant-lam{args.lam}", (GAMMA, "0.30", "5.0")),
    ]:
        print(f"BUILD {label}", flush=True)
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, sigmas, planted))
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
