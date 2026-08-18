#!/usr/bin/env python3
"""E77.7c min-max and uniform real-interval contraction audit."""

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


GAMMA = "14.134725141734693790"


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def norm2(vector: mp.matrix) -> mp.mpf:
    return mp.fsum(abs(vector[j]) ** 2 for j in range(vector.rows))


def section(Hmax, idxmax, max_modes, modes):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def energy(H, mu):
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    try:
        x = mp.lu_solve(A, b)
    except ZeroDivisionError:
        return mp.inf
    return norm2(x)


def run_build(label, lam, max_modes, dps, radius, grid_size, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    vals_max, _ = mp.eigsy(Hmax)
    mu_ref = vals_max[0]
    grid = [mu_ref - radius + 2 * radius * j / (grid_size - 1) for j in range(grid_size)]
    rows = []
    previous_mu = None
    for modes in range(6, max_modes + 1):
        H, _idx = section(Hmax, idxmax, max_modes, modes)
        vals, _ = mp.eigsy(H)
        mu = vals[0]
        energies = [energy(H, point) for point in grid]
        finite_energies = [value for value in energies if mp.isfinite(value)]
        min_energy = min(finite_energies) if finite_energies else mp.inf
        monotone_defect = mp.mpf(0) if previous_mu is None else max(mp.mpf(0), mu - previous_mu)
        rows.append(
            {
                "N": modes,
                "mu_N": serial(mu),
                "mu_drop_from_previous": None if previous_mu is None else serial(previous_mu - mu),
                "minmax_monotonicity_defect": serial(monotone_defect),
                "interval_radius": serial(radius),
                "minimum_grid_energy": serial(min_energy),
                "maximum_grid_radius_proxy": serial(1 / min_energy if min_energy else mp.inf),
                "grid_argmin_mu": serial(grid[energies.index(min_energy)]),
            }
        )
        previous_mu = mu
        print(
            f"{label:6s} N={modes:2d} mu={serial(mu, 9):>14s} "
            f"minE(I)={serial(min_energy, 9):>14s} maxRad={serial(1/min_energy, 9):>14s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "mu_reference": serial(mu_ref),
        "interval": [serial(mu_ref - radius), serial(mu_ref + radius)],
        "grid_size": grid_size,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument("--radius", type=str, default="0.05")
    parser.add_argument("--grid-size", type=int, default=21)
    parser.add_argument("--output", type=Path, default=HERE / "E77_7c_uniform_interval_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7c requires dps >= 50")
    if args.grid_size < 3 or args.grid_size % 2 == 0:
        parser.error("grid-size must be odd and at least 3")
    mp.mp.dps = args.dps
    radius = mp.mpf(args.radius)
    result = {
        "statement": "Nested min-max and fixed real-interval contraction audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "radius": args.radius,
            "grid_size": args.grid_size,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": "A finite real grid is a falsifier only; it does not prove interval-uniform contraction.",
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, radius, args.grid_size, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
