#!/usr/bin/env python3
"""E77.7ao audit whether the live Schur object is full k or projected tau S^-1 k."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(HERE))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data, serial  # noqa: E402
from E77_5k_moving_boundary_four_node_probe import section, solve_matrix, submatrix, subvector  # noqa: E402
from E77_7h_shorted_shell_energy_probe import analyze_pair  # noqa: E402


def norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def cserial(z, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def schur_step_data(Hmax: mp.matrix, idxmax: list[int], max_modes: int, n_modes: int, sigma: mp.mpf):
    common_nodes = list(range(-n_modes + 2, n_modes - 1))
    H, idx = section(Hmax, idxmax, max_modes, n_modes)
    L = H[0, 0]
    z = 1j * sigma

    _mu, A, db_idx, inner, _direct_x = right_transfer_data(H, idx)
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

    db = 2 * mp.pi * db_idx / L
    core_d = [2 * mp.pi * node / L for node in common_nodes]
    active_d = [2 * mp.pi * node / L for node in active_nodes]
    r_core = mp.matrix([[1 / (z - d) for d in core_d]])
    r_active = mp.matrix([[1 / (z - d) for d in active_d]])
    tau = r_active - r_core * solve_Aca
    corr = (tau * y)[0]
    theta = corr / (1 / (z - db) - (r_core * solve_gc)[0])

    return {
        "N": n_modes,
        "active_nodes": active_nodes,
        "k_norm": norm(k),
        "y_norm": norm(y),
        "tau_y_abs": abs(corr),
        "theta_abs": abs(theta),
        "k": k,
        "y": y,
    }


def rel_change(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return abs(a - b) / max(mp.mpf("1e-100"), abs(a), abs(b))


def run_build(label: str, planted, lam: int, max_modes: int, dps: int, sigma: mp.mpf, shell_pairs: list[tuple[int, int]]):
    Hmax, idxmax, _L = build_mp(lam, max_modes, dps, planted=planted)
    schur_rows = []
    upper_n = max(max_modes, max(new_n for _old_n, new_n in shell_pairs))
    for n in range(8, upper_n + 1, 2):
        schur_rows.append(schur_step_data(Hmax, idxmax, max_modes, n, sigma))

    projected_rows = []
    for old_n, new_n in shell_pairs:
        old = next(row for row in schur_rows if row["N"] == old_n)
        new = next(row for row in schur_rows if row["N"] == new_n)
        projected_rows.append(
            {
                "from_N": old_n,
                "to_N": new_n,
                "k_norm_old": serial(old["k_norm"]),
                "k_norm_new": serial(new["k_norm"]),
                "y_norm_old": serial(old["y_norm"]),
                "y_norm_new": serial(new["y_norm"]),
                "tau_y_abs_old": serial(old["tau_y_abs"]),
                "tau_y_abs_new": serial(new["tau_y_abs"]),
                "theta_abs_old": serial(old["theta_abs"]),
                "theta_abs_new": serial(new["theta_abs"]),
                "k_rel_change": serial(rel_change(old["k_norm"], new["k_norm"])),
                "y_rel_change": serial(rel_change(old["y_norm"], new["y_norm"])),
                "tau_y_rel_change": serial(rel_change(old["tau_y_abs"], new["tau_y_abs"])),
            }
        )

    shell_rows = []
    for old_n, new_n in shell_pairs:
        shell = analyze_pair(Hmax, idxmax, 14, old_n, new_n)
        shell_rows.append(
            {
                "from_N": old_n,
                "to_N": new_n,
                "energy_over_eta": shell["energy_over_eta"],
                "cancellation_ratio": shell["cancellation_ratio"],
                "residual_norm": shell["residual_norm"],
                "direct_shell_norm": shell["direct_shell_norm"],
                "mediated_shell_norm": shell["mediated_shell_norm"],
            }
        )

    return {
        "label": label,
        "sigma": serial(sigma),
        "schur_rows": [
            {
                "N": row["N"],
                "active_nodes": row["active_nodes"],
                "k_norm": serial(row["k_norm"]),
                "y_norm": serial(row["y_norm"]),
                "tau_y_abs": serial(row["tau_y_abs"]),
                "theta_abs": serial(row["theta_abs"]),
            }
            for row in schur_rows
        ],
        "projected_rows": projected_rows,
        "shell_rows": shell_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--sigma", type=str, default="3.0")
    parser.add_argument("--pairs", type=str, default="16:18,18:20")
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_7ao_projected_schur_source_results.json")
    args = parser.parse_args()

    mp.mp.dps = args.dps
    sigma = mp.mpf(args.sigma)
    shell_pairs = []
    for token in args.pairs.split(","):
        left, right = token.split(":")
        shell_pairs.append((int(left), int(right)))

    result = {
        "statement": "Audit whether shell-facing control lives at k, y=S^-1k, or tau y",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigma": serial(sigma),
            "pairs": shell_pairs,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }

    specs = []
    if args.case in {"zeta", "both"}:
        specs.append(("zeta", None))
    if args.case in {"plant", "both"}:
        specs.append(("plant", (GAMMA, "0.30", "5.0")))
    for label, planted in specs:
        case = run_build(label, planted, args.lam, args.max_modes, args.dps, sigma, shell_pairs)
        result["cases"].append(case)
        print(f"CASE {label}", flush=True)
        for prow, srow in zip(case["projected_rows"], case["shell_rows"]):
            print(
                f"ROW {prow['from_N']:2d}->{prow['to_N']:2d} "
                f"dk={prow['k_rel_change']} dy={prow['y_rel_change']} dtauy={prow['tau_y_rel_change']} "
                f"E/eta={srow['energy_over_eta']} res={srow['cancellation_ratio']}",
                flush=True,
            )

    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}", flush=True)


if __name__ == "__main__":
    main()
