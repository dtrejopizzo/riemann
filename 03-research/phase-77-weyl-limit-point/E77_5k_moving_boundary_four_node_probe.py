#!/usr/bin/env python3
"""E77.5k common-core moving-boundary block audit.

For the N -> N+2 step, use the common core [-N+2,...,N-2].  Then the old
section has a 2-node active block [-N+1,N-1], while the new section has a
6-node active block [-N-1,-N,-N+1,N-1,N,N+1].  This checks whether the
moving-boundary/four-node residual is naturally represented at transfer
level or at theta level.
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
from E77_5f_shell_resolvent_probe import transfer  # noqa: E402
from E77_5g_schur_phase_increment_probe import shell_theta_data  # noqa: E402


def solve_matrix(A: mp.matrix, B: mp.matrix) -> mp.matrix:
    X = mp.matrix(A.rows, B.cols)
    for c in range(B.cols):
        sol = mp.lu_solve(A, B[:, c])
        for r in range(A.rows):
            X[r, c] = sol[r]
    return X


def submatrix(A: mp.matrix, rows: list[int], cols: list[int]) -> mp.matrix:
    return mp.matrix([[A[i, j] for j in cols] for i in rows])


def subvector(v: mp.matrix, rows: list[int]) -> mp.matrix:
    return mp.matrix([v[i] for i in rows])


def common_core_transfer_data(H: mp.matrix, idx: list[int], L: mp.mpf, common_nodes: list[int], sigma: mp.mpf):
    z = 1j * sigma
    _mu, A, db_idx, inner, direct_x = right_transfer_data(H, idx)
    pos = {node: j for j, node in enumerate(inner)}
    core_cols = [pos[node] for node in common_nodes]
    active_nodes = [node for node in inner if node not in set(common_nodes)]
    active_cols = [pos[node] for node in active_nodes]
    g = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])

    Acc = submatrix(A, core_cols, core_cols)
    Aca = submatrix(A, core_cols, active_cols)
    Aac = submatrix(A, active_cols, core_cols)
    Aaa = submatrix(A, active_cols, active_cols)
    gc = subvector(g, core_cols)
    ga = subvector(g, active_cols)
    solve_Aca = solve_matrix(Acc, Aca)
    solve_gc = mp.lu_solve(Acc, gc)
    S = Aaa - Aac * solve_Aca
    k = ga - Aac * solve_gc

    db = 2 * mp.pi * db_idx / L
    core_d = [2 * mp.pi * node / L for node in common_nodes]
    active_d = [2 * mp.pi * node / L for node in active_nodes]
    r_core = mp.matrix([[1 / (z - d) for d in core_d]])
    r_active = mp.matrix([[1 / (z - d) for d in active_d]])
    rp_core = mp.matrix([[-1 / (z - d) ** 2 for d in core_d]])
    rp_active = mp.matrix([[-1 / (z - d) ** 2 for d in active_d]])

    t0 = 1 / (z - db) - (r_core * solve_gc)[0]
    t0p = -1 / (z - db) ** 2 - (rp_core * solve_gc)[0]
    tau = r_active - r_core * solve_Aca
    taup = rp_active - rp_core * solve_Aca
    y = mp.lu_solve(S, k)
    corr = (tau * y)[0]
    corrp = (taup * y)[0]
    T = t0 - corr
    Tp = t0p - corrp
    theta_common = corr / t0
    direct_T = transfer(z, db_idx, inner, direct_x, L)
    direct_Tp = transfer_prime(z, db_idx, inner, direct_x, L)
    identity_error = max(
        abs(T - direct_T) / max(1, abs(direct_T)),
        abs(Tp - direct_Tp) / max(1, abs(direct_Tp)),
    )
    return {
        "db": db_idx,
        "inner": inner,
        "active_nodes": active_nodes,
        "theta_common": theta_common,
        "T": T,
        "Tp": Tp,
        "log_derivative": Tp / T,
        "identity_error": identity_error,
        "corr_abs": abs(corr),
        "t0_abs": abs(t0),
    }


def section(Hmax: mp.matrix, idxmax: list[int], max_modes: int, n_modes: int):
    offset = max_modes - n_modes
    H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
    idx = idxmax[offset : len(idxmax) - offset]
    return H, idx


def run_build(label: str, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf], planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        common_nodes = list(range(-n_modes + 2, n_modes - 1))
        Hn, idxn = section(Hmax, idxmax, max_modes, n_modes)
        Hm, idxm = section(Hmax, idxmax, max_modes, n_modes + 2)
        sigma_rows = []
        active_old = None
        active_new = None
        for sigma in sigmas:
            old = common_core_transfer_data(Hn, idxn, L, common_nodes, sigma)
            new = common_core_transfer_data(Hm, idxm, L, common_nodes, sigma)
            sh_old = shell_theta_data(Hn, idxn, L, sigma)
            sh_new = shell_theta_data(Hm, idxm, L, sigma)
            active_old = old["active_nodes"]
            active_new = new["active_nodes"]
            delta_common_theta = old["theta_common"] - new["theta_common"]
            delta_shell_theta = sh_old["theta"] - sh_new["theta"]
            delta_logd = old["log_derivative"] - new["log_derivative"]
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "common_theta_delta_abs": serial(abs(delta_common_theta)),
                    "shell_theta_delta_abs": serial(abs(delta_shell_theta)),
                    "common_over_shell_delta": serial(
                        abs(delta_common_theta) / abs(delta_shell_theta)
                        if delta_shell_theta
                        else mp.inf
                    ),
                    "log_derivative_delta_abs": serial(abs(delta_logd)),
                    "old_identity_error": serial(old["identity_error"]),
                    "new_identity_error": serial(new["identity_error"]),
                    "old_corr_over_t0": serial(old["corr_abs"] / old["t0_abs"] if old["t0_abs"] else mp.inf),
                    "new_corr_over_t0": serial(new["corr_abs"] / new["t0_abs"] if new["t0_abs"] else mp.inf),
                }
            )
        max_common = max(mp.mpf(r["common_theta_delta_abs"]) for r in sigma_rows)
        max_shell = max(mp.mpf(r["shell_theta_delta_abs"]) for r in sigma_rows)
        min_ratio = min(mp.mpf(r["common_over_shell_delta"]) for r in sigma_rows)
        max_ratio = max(mp.mpf(r["common_over_shell_delta"]) for r in sigma_rows)
        max_id = max(
            max(mp.mpf(r["old_identity_error"]), mp.mpf(r["new_identity_error"]))
            for r in sigma_rows
        )
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "common_core": [common_nodes[0], common_nodes[-1]],
                "old_active_nodes": active_old,
                "new_active_nodes": active_new,
                "max_common_theta_delta_abs": serial(max_common),
                "max_shell_theta_delta_abs": serial(max_shell),
                "common_over_shell_delta_range": [serial(min_ratio), serial(max_ratio)],
                "max_identity_error": serial(max_id),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"oldAct={active_old} newAct={active_new} "
            f"dCommon={serial(max_common,8):>12s} dShell={serial(max_shell,8):>12s} "
            f"ratio=[{serial(min_ratio,6)},{serial(max_ratio,6)}] id={serial(max_id,5)}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam_int,
        "N_max": max_modes,
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "increments": increments,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5k_moving_boundary_four_node_results.json")
    args = parser.parse_args()
    if args.dps < 70:
        parser.error("E77.5k requires dps >= 70")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Common-core moving-boundary four/six-node block audit",
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
