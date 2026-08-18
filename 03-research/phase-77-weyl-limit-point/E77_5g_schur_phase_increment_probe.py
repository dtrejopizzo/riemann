#!/usr/bin/env python3
"""E77.5g Schur theta phase and derivative increments.

E77.5f proved the exact shell decomposition

    T = t0 * (1 - theta),  theta = tau Sigma^{-1} kappa / t0.

This probe measures the section increments of log(1-theta) and of its
safe-axis logarithmic derivative.  The latter is the finite shell
contribution that must be controlled for DELTA-ENVELOPE.
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


def cserial(z: complex | mp.mpc, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def cnorm(z: complex | mp.mpc) -> mp.mpf:
    return abs(mp.mpc(z))


def wrapped_abs_phase(x: mp.mpf) -> mp.mpf:
    twopi = 2 * mp.pi
    y = mp.fmod(x + mp.pi, twopi)
    if y < 0:
        y += twopi
    return abs(y - mp.pi)


def shell_theta_data(H: mp.matrix, idx: list[int], L: mp.mpf, sigma: mp.mpf) -> dict:
    z = 1j * sigma
    _mu, A, db_idx, inner, _direct_x = right_transfer_data(H, idx)
    if len(inner) < 5:
        raise ValueError("need at least two shell nodes and a nontrivial core")

    core = A[1:-1, 1:-1]
    shell_nodes = [inner[0], inner[-1]]
    core_nodes = inner[1:-1]

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
    theta = corr / t0
    theta_p = corrp / t0 - theta * t0p / t0
    ell = mp.log(1 - theta)
    ellp = -theta_p / (1 - theta)
    safe_derivative = 2 * mp.re(1j * ellp)
    eigs = mp.eigsy(Sigma)[0]
    sigma_min = min(abs(eigs[j]) for j in range(eigs.rows))
    return {
        "sigma": serial(sigma),
        "theta": theta,
        "theta_abs": abs(theta),
        "one_minus_theta_abs": abs(1 - theta),
        "theta_arg": mp.arg(theta),
        "ell": ell,
        "ellp": ellp,
        "safe_derivative": safe_derivative,
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
        rows = [shell_theta_data(H, idx, L, sigma) for sigma in sigmas]
        sections[n_modes] = rows

    out_sections = []
    for n_modes, rows in sections.items():
        out_sections.append(
            {
                "N": n_modes,
                "max_theta_abs": serial(max(r["theta_abs"] for r in rows)),
                "min_one_minus_theta_abs": serial(min(r["one_minus_theta_abs"] for r in rows)),
                "max_safe_derivative_abs": serial(max(abs(r["safe_derivative"]) for r in rows)),
                "min_sigma_min_abs": serial(min(r["sigma_min_abs"] for r in rows)),
                "sigmas": [
                    {
                        "sigma": r["sigma"],
                        "theta": cserial(r["theta"]),
                        "theta_abs": serial(r["theta_abs"]),
                        "theta_arg": serial(r["theta_arg"]),
                        "log_one_minus_theta": cserial(r["ell"]),
                        "safe_derivative": serial(r["safe_derivative"]),
                        "sigma_min_abs": serial(r["sigma_min_abs"]),
                    }
                    for r in rows
                ],
            }
        )

    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        sigma_rows = []
        for a, b in zip(sections[n_modes], sections[n_modes + 2]):
            delta_ell = a["ell"] - b["ell"]
            delta_safe = a["safe_derivative"] - b["safe_derivative"]
            theta_step = a["theta"] - b["theta"]
            phase_jump = abs(mp.im(delta_ell))
            wrapped_phase_jump = wrapped_abs_phase(mp.im(delta_ell))
            sigma_rows.append(
                {
                    "sigma": a["sigma"],
                    "delta_log_one_minus_theta": cserial(delta_ell),
                    "delta_safe_derivative": serial(delta_safe),
                    "abs_delta_safe_derivative": serial(abs(delta_safe)),
                    "abs_delta_theta": serial(abs(theta_step)),
                    "phase_jump_abs": serial(phase_jump),
                    "wrapped_phase_jump_abs": serial(wrapped_phase_jump),
                }
            )
        max_delta_safe = max(mp.mpf(r["abs_delta_safe_derivative"]) for r in sigma_rows)
        max_phase_jump = max(mp.mpf(r["phase_jump_abs"]) for r in sigma_rows)
        max_wrapped_phase_jump = max(mp.mpf(r["wrapped_phase_jump_abs"]) for r in sigma_rows)
        max_delta_theta = max(mp.mpf(r["abs_delta_theta"]) for r in sigma_rows)
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "max_abs_delta_safe_derivative": serial(max_delta_safe),
                "max_phase_jump_abs": serial(max_phase_jump),
                "max_wrapped_phase_jump_abs": serial(max_wrapped_phase_jump),
                "max_abs_delta_theta": serial(max_delta_theta),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"dSafe={serial(max_delta_safe,8):>12s} "
            f"dTheta={serial(max_delta_theta,8):>12s} "
            f"dPhase={serial(max_phase_jump,8):>12s}",
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
        "sections": out_sections,
        "increments": increments,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5g_schur_phase_increment_results.json")
    args = parser.parse_args()
    if args.dps < 70:
        parser.error("E77.5g requires dps >= 70")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Schur theta phase and derivative increment audit",
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
