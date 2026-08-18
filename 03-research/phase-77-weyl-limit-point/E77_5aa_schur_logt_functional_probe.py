#!/usr/bin/env python3
"""E77.5aa exact Schur decomposition of the Q_logT functional."""

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
from E77_5k_moving_boundary_four_node_probe import section, solve_matrix, submatrix, subvector  # noqa: E402


def prepare_schur(H: mp.matrix, idx: list[int], common_nodes: list[int]):
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
    y = mp.lu_solve(S, k)
    return {
        "db_idx": db_idx,
        "common_nodes": common_nodes,
        "active_nodes": active_nodes,
        "solve_gc": solve_gc,
        "solve_Aca": solve_Aca,
        "y": y,
    }


def schur_logt_parts(prepared: dict, L: mp.mpf, sigma: mp.mpf):
    z = 1j * sigma
    db_idx = prepared["db_idx"]
    common_nodes = prepared["common_nodes"]
    active_nodes = prepared["active_nodes"]
    solve_gc = prepared["solve_gc"]
    solve_Aca = prepared["solve_Aca"]
    y = prepared["y"]
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
    corr = (tau * y)[0]
    corrp = (taup * y)[0]
    theta = corr / t0
    thetap = (corrp * t0 - corr * t0p) / (t0 * t0)
    t_part = t0p / t0
    theta_part = -thetap / (1 - theta)
    full = t_part + theta_part
    direct = (t0p - corrp) / (t0 - corr)
    err = abs(full - direct) / max(1, abs(direct))
    return {
        "active_nodes": active_nodes,
        "logd": full,
        "t0_part": t_part,
        "theta_part": theta_part,
        "theta": theta,
        "theta_prime": thetap,
        "identity_error": err,
        "theta_abs": abs(theta),
        "one_minus_theta_abs": abs(1 - theta),
    }


def safe_scalar(logd):
    return 2 * mp.re(1j * logd)


def q_reference(identity_data, label, sigma, n):
    for case in identity_data["cases"]:
        if case["label"] == label:
            for row in case["rows"]:
                if row["sigma"] == sigma and row["N"] == n:
                    return row
    return None


def num(x):
    return float(x)


def component_q(delta_rows):
    out = []
    by_key = {(r["sigma"], r["N"]): r for r in delta_rows}
    for row in delta_rows:
        n = row["N"]
        nxt = by_key.get((row["sigma"], n + 2))
        if nxt is None:
            continue
        q_t0 = n * n * (n * row["delta_t0"] - (n + 2) * nxt["delta_t0"])
        q_theta = n * n * (n * row["delta_theta"] - (n + 2) * nxt["delta_theta"])
        q_full = n * n * (n * row["delta_logt"] - (n + 2) * nxt["delta_logt"])
        out.append(
            {
                "sigma": row["sigma"],
                "N": n,
                "mod4": n % 4,
                "Q_logT_reconstructed": num(q_full),
                "Q_t0": num(q_t0),
                "Q_theta": num(q_theta),
                "Q_component_error": num(abs((q_t0 + q_theta) - q_full) / max(1, abs(q_full))),
                "theta_abs_old": num(row["theta_abs_old"]),
                "theta_abs_new": num(row["theta_abs_new"]),
                "one_minus_theta_abs_old": num(row["one_minus_theta_abs_old"]),
                "one_minus_theta_abs_new": num(row["one_minus_theta_abs_new"]),
            }
        )
    return out


def run_build(label, planted, lam_int, max_modes, dps, sigmas, identity_data):
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    deltas = []
    for n in range(8, max_modes - 1, 2):
        common_nodes = list(range(-n + 2, n - 1))
        Hn, idxn = section(Hmax, idxmax, max_modes, n)
        Hm, idxm = section(Hmax, idxmax, max_modes, n + 2)
        old_prepared = prepare_schur(Hn, idxn, common_nodes)
        new_prepared = prepare_schur(Hm, idxm, common_nodes)
        for sigma in sigmas:
            old = schur_logt_parts(old_prepared, L, sigma)
            new = schur_logt_parts(new_prepared, L, sigma)
            delta_logt = safe_scalar(old["logd"]) - safe_scalar(new["logd"])
            delta_t0 = safe_scalar(old["t0_part"]) - safe_scalar(new["t0_part"])
            delta_theta = safe_scalar(old["theta_part"]) - safe_scalar(new["theta_part"])
            deltas.append(
                {
                    "sigma": serial(sigma),
                    "N": n,
                    "to_N": n + 2,
                    "delta_logt": delta_logt,
                    "delta_t0": delta_t0,
                    "delta_theta": delta_theta,
                    "delta_component_error": abs((delta_t0 + delta_theta) - delta_logt)
                    / max(1, abs(delta_logt)),
                    "old_identity_error": old["identity_error"],
                    "new_identity_error": new["identity_error"],
                    "theta_abs_old": old["theta_abs"],
                    "theta_abs_new": new["theta_abs"],
                    "one_minus_theta_abs_old": old["one_minus_theta_abs"],
                    "one_minus_theta_abs_new": new["one_minus_theta_abs"],
                }
            )
    qrows = component_q(deltas)
    for row in qrows:
        ref = q_reference(identity_data, label, row["sigma"], row["N"])
        if ref:
            row["Q_logT_reference"] = ref["Q_logt_component"]
            row["Q_logT_reference_error"] = abs(row["Q_logT_reconstructed"] - ref["Q_logt_component"]) / max(
                1, abs(ref["Q_logt_component"])
            )
            row["Q_reference"] = ref["Q_reference"]
            row["Q_ext_reference"] = ref["Q_external_component"]
    serial_deltas = []
    for row in deltas:
        serial_deltas.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "to_N": row["to_N"],
                "delta_logt": num(row["delta_logt"]),
                "delta_t0": num(row["delta_t0"]),
                "delta_theta": num(row["delta_theta"]),
                "delta_component_error": num(row["delta_component_error"]),
                "old_identity_error": num(row["old_identity_error"]),
                "new_identity_error": num(row["new_identity_error"]),
                "theta_abs_old": num(row["theta_abs_old"]),
                "theta_abs_new": num(row["theta_abs_new"]),
                "one_minus_theta_abs_old": num(row["one_minus_theta_abs_old"]),
                "one_minus_theta_abs_new": num(row["one_minus_theta_abs_new"]),
            }
        )
    return {"label": label, "deltas": serial_deltas, "qrows": qrows}


def run(identity_path: Path, lam_int: int, max_modes: int, dps: int, sigmas, case_filter: str):
    mp.mp.dps = dps
    identity_data = json.loads(identity_path.read_text(encoding="ascii"))
    specs = []
    if case_filter in {"zeta", "both"}:
        specs.append((f"zeta-lam{lam_int}", None))
    if case_filter in {"plant", "both"}:
        specs.append((f"plant-lam{lam_int}", (GAMMA, "0.30", "5.0")))
    return {
        "statement": "Exact Schur decomposition Q_logT = Q_t0 + Q_theta",
        "identity_source": str(identity_path),
        "parameters": {
            "lambda": lam_int,
            "max_modes": max_modes,
            "dps": dps,
            "sigmas": [serial(s) for s in sigmas],
        },
        "cases": [run_build(label, planted, lam_int, max_modes, dps, sigmas, identity_data) for label, planted in specs],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--identity", type=Path, default=HERE / "E77_5y_q_functional_identity_results.json")
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--sigmas", default="1.0,3.0")
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5aa_schur_logt_functional_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = run(args.identity, args.lam, args.max_modes, args.dps, sigmas, args.case)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for row in case["qrows"]:
            ref_err = row.get("Q_logT_reference_error")
            print(
                f"ROW s={row['sigma']} N={row['N']:2d} mod{row['mod4']} "
                f"Qlog={serial(row['Q_logT_reconstructed'], 10)} "
                f"Qt0={serial(row['Q_t0'], 10)} Qtheta={serial(row['Q_theta'], 10)} "
                f"referr={serial(ref_err, 5) if ref_err is not None else 'na'} "
                f"|1-theta|new={serial(row['one_minus_theta_abs_new'], 8)}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
