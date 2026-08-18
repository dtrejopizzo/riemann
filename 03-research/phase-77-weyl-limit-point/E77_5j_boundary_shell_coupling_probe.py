#!/usr/bin/env python3
"""E77.5j boundary/shell coupling audit for consecutive sections.

The N -> N+2 step is not a pure addition of two shell coordinates: the
right boundary itself moves from d_N to d_{N+2}, and the old boundary
becomes an interior coordinate.  This probe measures that migration and
compares its pole scale with the certified Schur-cocycle delta.
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
from E77_5g_schur_phase_increment_probe import shell_theta_data  # noqa: E402


def section(Hmax: mp.matrix, idxmax: list[int], max_modes: int, n_modes: int):
    offset = max_modes - n_modes
    H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
    idx = idxmax[offset : len(idxmax) - offset]
    _mu, _A, db_idx, inner, _x = right_transfer_data(H, idx)
    return H, idx, db_idx, inner


def run_build(label: str, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf], planted):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    sections = {}
    for n_modes in range(8, max_modes + 1, 2):
        H, idx, db_idx, inner = section(Hmax, idxmax, max_modes, n_modes)
        theta_rows = [shell_theta_data(H, idx, L, sigma) for sigma in sigmas]
        sections[n_modes] = {"H": H, "idx": idx, "db": db_idx, "inner": inner, "theta": theta_rows}

    increments = []
    for n_modes in range(8, max_modes - 1, 2):
        a = sections[n_modes]
        b = sections[n_modes + 2]
        old_inner = set(a["inner"])
        new_inner = set(b["inner"])
        entered_inner = sorted(new_inner - old_inner)
        old_boundary_enters = a["db"] in new_inner
        left_boundary_enters = a["idx"][0] in new_inner
        sigma_rows = []
        for ra, rb, sigma in zip(a["theta"], b["theta"], sigmas):
            z = 1j * sigma
            d_old = 2 * mp.pi * a["db"] / L
            d_new = 2 * mp.pi * b["db"] / L
            boundary_pole_shift = abs(1 / (z - d_old) - 1 / (z - d_new))
            delta_theta = abs(ra["theta"] - rb["theta"])
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "delta_theta_abs": serial(delta_theta),
                    "boundary_pole_shift_abs": serial(boundary_pole_shift),
                    "boundary_shift_over_delta": serial(boundary_pole_shift / delta_theta if delta_theta else mp.inf),
                }
            )
        max_delta = max(mp.mpf(r["delta_theta_abs"]) for r in sigma_rows)
        max_shift = max(mp.mpf(r["boundary_pole_shift_abs"]) for r in sigma_rows)
        min_shift_ratio = min(mp.mpf(r["boundary_shift_over_delta"]) for r in sigma_rows)
        max_shift_ratio = max(mp.mpf(r["boundary_shift_over_delta"]) for r in sigma_rows)
        increments.append(
            {
                "from_N": n_modes,
                "to_N": n_modes + 2,
                "old_boundary": a["db"],
                "new_boundary": b["db"],
                "entered_inner": entered_inner,
                "old_boundary_enters_new_inner": old_boundary_enters,
                "old_left_boundary_enters_new_inner": left_boundary_enters,
                "max_delta_theta_abs": serial(max_delta),
                "max_boundary_pole_shift_abs": serial(max_shift),
                "min_boundary_shift_over_delta": serial(min_shift_ratio),
                "max_boundary_shift_over_delta": serial(max_shift_ratio),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:10s} {n_modes:2d}->{n_modes+2:2d} "
            f"db={a['db']}->{b['db']} enters={entered_inner} "
            f"dTheta={serial(max_delta,8):>12s} "
            f"pole/d=[{serial(min_shift_ratio,6)},{serial(max_shift_ratio,6)}]",
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
    parser.add_argument("--output", type=Path, default=HERE / "E77_5j_boundary_shell_coupling_results.json")
    args = parser.parse_args()
    if args.dps < 70:
        parser.error("E77.5j requires dps >= 70")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Boundary migration plus shell coupling audit",
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
