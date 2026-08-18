#!/usr/bin/env python3
"""E77.5h factor decomposition of Delta theta.

For theta_N = tau_N v_N c_N with

    v_N = Sigma_N^{-1} kappa_N,   c_N = 1/t0_N,

measure the exact telescoping decomposition

    theta_N - theta_M
      = (tau_N-tau_M) v_N c_N
      + tau_M (v_N-v_M) c_N
      + tau_M v_M (c_N-c_M),

where M=N+2.  This names which finite Schur factor carries THETA-REG.
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
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data, serial  # noqa: E402
from E77_5f_shell_resolvent_probe import solve_matrix  # noqa: E402


def row_norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[0, j]) ** 2 for j in range(v.cols)))


def col_norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def factor_data(H: mp.matrix, idx: list[int], L: mp.mpf, sigma: mp.mpf) -> dict:
    z = 1j * sigma
    _mu, A, db_idx, inner, _direct_x = right_transfer_data(H, idx)
    core = A[1:-1, 1:-1]
    core_nodes = inner[1:-1]
    shell_nodes = [inner[0], inner[-1]]

    U = mp.matrix(core.rows, 2)
    for j in range(core.rows):
        U[j, 0] = A[j + 1, 0]
        U[j, 1] = A[j + 1, A.cols - 1]
    C = mp.matrix(
        [
            [A[0, 0], A[0, A.cols - 1]],
            [A[A.rows - 1, 0], A[A.rows - 1, A.cols - 1]],
        ]
    )
    core_solve_U = solve_matrix(core, U)
    Sigma = C - U.T * core_solve_U

    g_full = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    g_core = g_full[1:-1, :]
    g_shell = mp.matrix([g_full[0], g_full[g_full.rows - 1]])
    core_solve_g = mp.lu_solve(core, g_core)
    kappa = g_shell - U.T * core_solve_g
    v = mp.lu_solve(Sigma, kappa)

    db = 2 * mp.pi * db_idx / L
    core_d = [2 * mp.pi * n / L for n in core_nodes]
    shell_d = [2 * mp.pi * n / L for n in shell_nodes]
    r_core = mp.matrix([[1 / (z - d) for d in core_d]])
    r_shell = mp.matrix([[1 / (z - d) for d in shell_d]])
    tau = r_shell - r_core * core_solve_U
    t0 = 1 / (z - db) - (r_core * core_solve_g)[0]
    c = 1 / t0
    theta = (tau * v)[0] * c
    eigs = mp.eigsy(Sigma)[0]
    sigma_min = min(abs(eigs[j]) for j in range(eigs.rows))
    return {
        "sigma": serial(sigma),
        "tau": tau,
        "v": v,
        "c": c,
        "theta": theta,
        "tau_norm": row_norm(tau),
        "v_norm": col_norm(v),
        "c_abs": abs(c),
        "theta_abs": abs(theta),
        "sigma_min_abs": sigma_min,
    }


def run_build(label: str, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf], planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    sections = {}
    for n_modes in range(8, max_modes + 1, 2):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        sections[n_modes] = [factor_data(H, idx, L, sigma) for sigma in sigmas]

    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        sigma_rows = []
        for a, b in zip(sections[n_modes], sections[n_modes + 2]):
            tau_part = ((a["tau"] - b["tau"]) * a["v"])[0] * a["c"]
            v_part = (b["tau"] * (a["v"] - b["v"]))[0] * a["c"]
            c_part = (b["tau"] * b["v"])[0] * (a["c"] - b["c"])
            delta = a["theta"] - b["theta"]
            recon = tau_part + v_part + c_part
            err = abs(delta - recon) / max(1, abs(delta))
            sigma_rows.append(
                {
                    "sigma": a["sigma"],
                    "delta_theta_abs": serial(abs(delta)),
                    "tau_part_abs": serial(abs(tau_part)),
                    "v_part_abs": serial(abs(v_part)),
                    "c_part_abs": serial(abs(c_part)),
                    "max_part_over_delta": serial(
                        max(abs(tau_part), abs(v_part), abs(c_part)) / abs(delta)
                        if delta
                        else mp.inf
                    ),
                    "telescoping_error": serial(err),
                }
            )
        max_delta = max(mp.mpf(r["delta_theta_abs"]) for r in sigma_rows)
        max_tau = max(mp.mpf(r["tau_part_abs"]) for r in sigma_rows)
        max_v = max(mp.mpf(r["v_part_abs"]) for r in sigma_rows)
        max_c = max(mp.mpf(r["c_part_abs"]) for r in sigma_rows)
        max_err = max(mp.mpf(r["telescoping_error"]) for r in sigma_rows)
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "max_delta_theta_abs": serial(max_delta),
                "max_tau_part_abs": serial(max_tau),
                "max_v_part_abs": serial(max_v),
                "max_c_part_abs": serial(max_c),
                "max_telescoping_error": serial(max_err),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"dTheta={serial(max_delta,8):>12s} "
            f"tau={serial(max_tau,8):>12s} "
            f"v={serial(max_v,8):>12s} "
            f"c={serial(max_c,8):>12s}",
            flush=True,
        )
    section_summary = []
    for n_modes, rows in sections.items():
        section_summary.append(
            {
                "N": n_modes,
                "max_tau_norm": serial(max(r["tau_norm"] for r in rows)),
                "max_v_norm": serial(max(r["v_norm"] for r in rows)),
                "max_c_abs": serial(max(r["c_abs"] for r in rows)),
                "max_theta_abs": serial(max(r["theta_abs"] for r in rows)),
                "min_sigma_min_abs": serial(min(r["sigma_min_abs"] for r in rows)),
            }
        )
    return {
        "label": label,
        "lambda": lam_int,
        "N_max": max_modes,
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "sections": section_summary,
        "increments": increments,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5h_schur_factor_regularizer_results.json")
    args = parser.parse_args()
    if args.dps < 70:
        parser.error("E77.5h requires dps >= 70")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Schur factor decomposition of Delta theta",
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
