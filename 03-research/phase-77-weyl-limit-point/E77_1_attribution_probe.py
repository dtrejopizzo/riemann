#!/usr/bin/env python3
"""E77.1 attribution run for finite-section Weyl-disk contraction.

Each case is built once at maximum size with the Phase-76 multiprecision
harness.  Central principal sections are then extracted so every row in a
case belongs to one genuinely nested family.
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


GAMMA = "14.134725141734693790"
BETAS = ("0.10", "0.20", "0.30", "0.40")
STRENGTH = "5.0"


def canonical_solution(H: mp.matrix) -> mp.matrix:
    """Return the Phase-76 canonical inner solution for one section."""
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    return mp.lu_solve(A, b)


def energy(x: mp.matrix) -> mp.mpf:
    return mp.fsum(abs(x[j]) ** 2 for j in range(x.rows))


def shell_mass(x: mp.matrix, width: int = 2) -> mp.mpf:
    total = energy(x)
    indices = list(range(width)) + list(range(x.rows - width, x.rows))
    return mp.fsum(abs(x[j]) ** 2 for j in indices) / total


def log_linear_fit(ns: list[int], ss: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf]:
    """Least-squares fit log(S_N)=intercept+slope*N at current precision."""
    nbar = mp.fsum(ns) / len(ns)
    logs = [mp.log(s) for s in ss]
    ybar = mp.fsum(logs) / len(logs)
    denominator = mp.fsum((n - nbar) ** 2 for n in ns)
    slope = mp.fsum((n - nbar) * (y - ybar) for n, y in zip(ns, logs)) / denominator
    return ybar - slope * nbar, slope


def serial(value: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def run_case(
    label: str,
    planted: tuple[str, str, str] | None,
    lam: int,
    min_modes: int,
    max_modes: int,
    dps: int,
) -> dict:
    print(f"BUILD {label}: lambda={lam} Nmax={max_modes} dps={dps}", flush=True)
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    ns: list[int] = []
    ss: list[mp.mpf] = []
    previous = None
    for n_modes in range(min_modes, max_modes + 1):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        x = canonical_solution(H)
        s_value = energy(x)
        radius = 1 / s_value
        mass = shell_mass(x)
        ratio = mp.nan if previous is None else s_value / previous
        ns.append(n_modes)
        ss.append(s_value)
        slope = mp.nan
        if len(ns) >= 3:
            _, slope = log_linear_fit(ns, ss)
        row = {
            "N": n_modes,
            "S_N": serial(s_value),
            "radius": serial(radius),
            "shellMass": serial(mass),
            "ratio": None if previous is None else serial(ratio),
            "c_prefix": None if len(ns) < 3 else serial(slope),
        }
        rows.append(row)
        print(
            f"ROW {label:13s} {n_modes:2d} {serial(s_value, 12):>16s} "
            f"{serial(radius, 12):>16s} {serial(mass, 10):>13s} "
            f"{('-' if previous is None else serial(ratio, 10)):>13s} "
            f"{('-' if len(ns) < 3 else serial(slope, 10)):>13s}",
            flush=True,
        )
        previous = s_value

    intercept, slope = log_linear_fit(ns, ss)
    tail_count = min(6, len(ns))
    tail_intercept, tail_slope = log_linear_fit(ns[-tail_count:], ss[-tail_count:])
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "lambda": lam,
        "L": serial(L),
        "dps": dps,
        "N_min": min_modes,
        "N_max": max_modes,
        "fit_all": {"intercept": serial(intercept), "c": serial(slope)},
        "fit_last_6": {"intercept": serial(tail_intercept), "c": serial(tail_slope)},
        "rows": rows,
    }


def write_outputs(result: dict, output_stem: Path) -> None:
    output_stem.with_suffix(".json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii"
    )
    lines = ["case\tbeta\tN\tS_N\tradius\tshellMass\tratio\tc_prefix"]
    for case in result["cases"]:
        beta = "" if case["planted"] is None else case["planted"]["beta"]
        for row in case["rows"]:
            lines.append(
                "\t".join(
                    [
                        case["label"], beta, str(row["N"]), row["S_N"],
                        row["radius"], row["shellMass"], row["ratio"] or "",
                        row["c_prefix"] or "",
                    ]
                )
            )
    output_stem.with_suffix(".tsv").write_text("\n".join(lines) + "\n", encoding="ascii")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--min-modes", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=16)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument(
        "--output-stem", type=Path, default=HERE / "E77_1_attribution_results"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.1 requires dps >= 50")
    if args.max_modes < 16:
        parser.error("E77.1 requires max-modes >= 16")

    cases = [("zeta", None)] + [
        (f"planted-b{beta}", (GAMMA, beta, STRENGTH)) for beta in BETAS
    ]
    result = {
        "probe": "E77.1 attribution run",
        "method": "one build per case; nested central principal sections",
        "parameters": {
            "lambda": args.lam,
            "dps": args.dps,
            "N_min": args.min_modes,
            "N_max": args.max_modes,
            "gamma": GAMMA,
            "strength": STRENGTH,
            "betas": list(BETAS),
            "shell_width": 2,
        },
        "cases": [],
    }
    for label, planted in cases:
        result["cases"].append(
            run_case(label, planted, args.lam, args.min_modes, args.max_modes, args.dps)
        )
        write_outputs(result, args.output_stem)
    print(f"WROTE {args.output_stem.with_suffix('.json')}")
    print(f"WROTE {args.output_stem.with_suffix('.tsv')}")


if __name__ == "__main__":
    main()
