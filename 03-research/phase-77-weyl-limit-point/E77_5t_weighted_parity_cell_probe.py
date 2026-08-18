#!/usr/bin/env python3
"""E77.5t weighted parity packages in the common-core active block."""

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


def cserial(z, digits=24):
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def active_detail(H, idx, L, common_nodes, sigma):
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
    core_d = [2 * mp.pi * node / L for node in common_nodes]
    active_d = [2 * mp.pi * node / L for node in active_nodes]
    r_core = mp.matrix([[1 / (z - d) for d in core_d]])
    r_active = mp.matrix([[1 / (z - d) for d in active_d]])
    tau = r_active - r_core * solve_Aca
    contribs = [(tau[0, j] * y[j]) for j in range(len(active_nodes))]
    return active_nodes, contribs


def package(active_nodes, contribs, n):
    by_node = {node: contribs[j] for j, node in enumerate(active_nodes)}
    inserted = [-n - 1, -n, n, n + 1]
    old_boundary_pair = [-n, n]
    outer_pair = [-n - 1, n + 1]
    old_shell_pair = [-n + 1, n - 1]

    def s(nodes):
        return mp.fsum(by_node.get(node, 0) for node in nodes)

    left = s([node for node in active_nodes if node < 0])
    right = s([node for node in active_nodes if node > 0])
    return {
        "left": left,
        "right": right,
        "lr_odd": right - left,
        "lr_even": right + left,
        "inserted": s(inserted),
        "old_boundary_pair": s(old_boundary_pair),
        "outer_pair": s(outer_pair),
        "old_shell_pair": s(old_shell_pair),
        "total": s(active_nodes),
    }


def q_lookup(qcase, sigma, n):
    for profile in qcase["profiles"]:
        if profile["sigma"] == sigma:
            cls = str(n % 4)
            for q in profile["classes"][cls]["Q_values"]:
                if q["N"] == n:
                    return q["value"]
    return None


def run(q_path: Path, lam_int: int, max_modes: int, dps: int, sigmas, case_filter: str):
    mp.mp.dps = dps
    qdata = json.loads(q_path.read_text(encoding="ascii"))
    out = {"statement": "Weighted common-core active parity packages", "cases": []}
    specs = []
    if case_filter in {"zeta", "both"}:
        specs.append(("zeta-lam6", None, qdata["cases"][0]))
    if case_filter in {"plant", "both"}:
        specs.append(("plant-lam6", (GAMMA, "0.30", "5.0"), qdata["cases"][1]))
    for label, planted, qcase in specs:
        Hm, idxm, LL = build_mp(lam_int, max_modes, dps, planted=planted)
        rows = []
        for n in range(8, max_modes - 1, 2):
            common_nodes = list(range(-n + 2, n - 1))
            H, idx = section(Hm, idxm, max_modes, n + 2)
            sigma_rows = []
            for sigma in sigmas:
                active_nodes, contribs = active_detail(H, idx, LL, common_nodes, sigma)
                pkg = package(active_nodes, contribs, n)
                qv = q_lookup(qcase, serial(sigma), n)
                sigma_rows.append(
                    {
                        "sigma": serial(sigma),
                        "Q": qv,
                        "active_nodes": active_nodes,
                        "lr_odd_abs": serial(abs(pkg["lr_odd"])),
                        "lr_even_abs": serial(abs(pkg["lr_even"])),
                        "inserted_abs": serial(abs(pkg["inserted"])),
                        "old_boundary_pair_abs": serial(abs(pkg["old_boundary_pair"])),
                        "outer_pair_abs": serial(abs(pkg["outer_pair"])),
                        "old_shell_pair_abs": serial(abs(pkg["old_shell_pair"])),
                        "total_abs": serial(abs(pkg["total"])),
                        "lr_odd": cserial(pkg["lr_odd"]),
                    }
                )
            rows.append({"N": n, "mod4": n % 4, "sigmas": sigma_rows})
        out["cases"].append({"label": label, "rows": rows})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=Path, default=HERE / "E77_5q_mod4_drift_split_results.json")
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--sigmas", default="1.0,3.0")
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5t_weighted_parity_cell_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = run(args.q, args.lam, args.max_modes, args.dps, sigmas, args.case)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for row in case["rows"]:
            vals = []
            for srow in row["sigmas"]:
                vals.append(
                    f"s={srow['sigma']} Q={srow['Q']} |odd|={srow['lr_odd_abs']} |ins|={srow['inserted_abs']}"
                )
            print(f"ROW N={row['N']:2d} mod4={row['mod4']} " + " ; ".join(vals), flush=True)
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
