#!/usr/bin/env python3
"""E77.5i pair-cancellation anatomy of the Schur cocycle.

E77.5h showed that Delta theta is a signed three-term cocycle:

    A + B + C

where A is the tau increment package, B the Sigma^{-1}kappa package, and
C the core-transfer package.  This probe checks whether the cancellation
can be reduced to a dominant pair or whether it is genuinely ternary.
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


def cserial(z, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def cosine_phase(a, b) -> mp.mpf:
    denom = abs(a) * abs(b)
    if denom == 0:
        return mp.mpf("nan")
    return mp.re(a * mp.conj(b)) / denom


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
    Cmat = mp.matrix(
        [
            [A[0, 0], A[0, A.cols - 1]],
            [A[A.rows - 1, 0], A[A.rows - 1, A.cols - 1]],
        ]
    )
    core_solve_U = solve_matrix(core, U)
    Sigma = Cmat - U.T * core_solve_U

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
    return {"sigma": serial(sigma), "tau": tau, "v": v, "c": c, "theta": theta}


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
            Aterm = ((a["tau"] - b["tau"]) * a["v"])[0] * a["c"]
            Bterm = (b["tau"] * (a["v"] - b["v"]))[0] * a["c"]
            Cterm = (b["tau"] * b["v"])[0] * (a["c"] - b["c"])
            total = Aterm + Bterm + Cterm
            delta = a["theta"] - b["theta"]
            pair_ab = Aterm + Bterm
            pair_ac = Aterm + Cterm
            pair_bc = Bterm + Cterm
            max_part = max(abs(Aterm), abs(Bterm), abs(Cterm))
            best_pair_abs = min(abs(pair_ab), abs(pair_ac), abs(pair_bc))
            best_pair_name = min(
                [("AB", abs(pair_ab)), ("AC", abs(pair_ac)), ("BC", abs(pair_bc))],
                key=lambda item: item[1],
            )[0]
            sigma_rows.append(
                {
                    "sigma": a["sigma"],
                    "delta_theta": cserial(delta),
                    "total": cserial(total),
                    "total_error": serial(abs(total - delta) / max(1, abs(delta))),
                    "A_tau": cserial(Aterm),
                    "B_v": cserial(Bterm),
                    "C_core": cserial(Cterm),
                    "abs_delta": serial(abs(delta)),
                    "abs_A": serial(abs(Aterm)),
                    "abs_B": serial(abs(Bterm)),
                    "abs_C": serial(abs(Cterm)),
                    "pair_AB_abs": serial(abs(pair_ab)),
                    "pair_AC_abs": serial(abs(pair_ac)),
                    "pair_BC_abs": serial(abs(pair_bc)),
                    "best_pair": best_pair_name,
                    "best_pair_abs": serial(best_pair_abs),
                    "best_pair_over_delta": serial(best_pair_abs / abs(delta) if delta else mp.inf),
                    "max_part_over_delta": serial(max_part / abs(delta) if delta else mp.inf),
                    "cos_AB": serial(cosine_phase(Aterm, Bterm)),
                    "cos_AC": serial(cosine_phase(Aterm, Cterm)),
                    "cos_BC": serial(cosine_phase(Bterm, Cterm)),
                }
            )
        max_delta = max(mp.mpf(r["abs_delta"]) for r in sigma_rows)
        max_part_ratio = max(mp.mpf(r["max_part_over_delta"]) for r in sigma_rows)
        min_best_pair_ratio = min(mp.mpf(r["best_pair_over_delta"]) for r in sigma_rows)
        best_counts = {}
        for row in sigma_rows:
            best_counts[row["best_pair"]] = best_counts.get(row["best_pair"], 0) + 1
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "max_delta_theta_abs": serial(max_delta),
                "max_part_over_delta": serial(max_part_ratio),
                "min_best_pair_over_delta": serial(min_best_pair_ratio),
                "best_pair_counts": best_counts,
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"dTheta={serial(max_delta,8):>12s} "
            f"part/d={serial(max_part_ratio,8):>12s} "
            f"bestPair/d={serial(min_best_pair_ratio,8):>12s} "
            f"pairs={best_counts}",
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
    parser.add_argument("--output", type=Path, default=HERE / "E77_5i_schur_cocycle_cell_results.json")
    args = parser.parse_args()
    if args.dps < 70:
        parser.error("E77.5i requires dps >= 70")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Pair-cancellation anatomy of the Schur cocycle",
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
