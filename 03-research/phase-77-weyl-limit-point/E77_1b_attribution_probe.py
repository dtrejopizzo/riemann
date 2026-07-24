#!/usr/bin/env python3
"""E77.1b enlarged attribution run.

This extends E77.1 without changing the Phase-76 build mechanism:
one maximum-size multiprecision CCM build per case and nested central
principal sections.  The extra diagnostics are designed to distinguish
slow divergence from bounded resonant spikes: parity fits, moving-window
fits, and block-minimum lower envelopes.
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
DEFAULT_BETAS = ("0.10", "0.20", "0.30", "0.40")
DEFAULT_STRENGTHS = ("5.0", "2.5", "10.0")
DEFAULT_LAMBDAS = (6, 7, 8)


def canonical_solution(H: mp.matrix) -> mp.matrix:
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


def log_linear_fit(ns: list[int], ss: list[mp.mpf]) -> dict | None:
    if len(ns) < 3:
        return None
    nbar = mp.fsum(ns) / len(ns)
    logs = [mp.log(s) for s in ss]
    ybar = mp.fsum(logs) / len(logs)
    denominator = mp.fsum((n - nbar) ** 2 for n in ns)
    slope = mp.fsum((n - nbar) * (y - ybar) for n, y in zip(ns, logs)) / denominator
    intercept = ybar - slope * nbar
    return {"intercept": serial(intercept), "c": serial(slope), "points": len(ns)}


def serial(value: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def window_fits(rows: list[dict], width: int) -> list[dict]:
    out = []
    for start in range(0, len(rows) - width + 1):
        chunk = rows[start : start + width]
        fit = log_linear_fit(
            [int(row["N"]) for row in chunk],
            [mp.mpf(row["S_N"]) for row in chunk],
        )
        assert fit is not None
        out.append({"N_start": chunk[0]["N"], "N_end": chunk[-1]["N"], **fit})
    return out


def block_minima(rows: list[dict], width: int) -> list[dict]:
    out = []
    for start in range(0, len(rows) - width + 1):
        chunk = rows[start : start + width]
        best = min(chunk, key=lambda row: mp.mpf(row["S_N"]))
        out.append(
            {
                "N_start": chunk[0]["N"],
                "N_end": chunk[-1]["N"],
                "min_N": best["N"],
                "min_S": best["S_N"],
                "min_radius": best["radius"],
            }
        )
    return out


def summarize(rows: list[dict]) -> dict:
    ns = [int(row["N"]) for row in rows]
    ss = [mp.mpf(row["S_N"]) for row in rows]
    even = [(n, s) for n, s in zip(ns, ss) if n % 2 == 0]
    odd = [(n, s) for n, s in zip(ns, ss) if n % 2 == 1]
    minima3 = block_minima(rows, 3)
    min_ns = [int(row["N_end"]) for row in minima3]
    min_ss = [mp.mpf(row["min_S"]) for row in minima3]
    return {
        "fit_all": log_linear_fit(ns, ss),
        "fit_last_6": log_linear_fit(ns[-6:], ss[-6:]),
        "fit_even": log_linear_fit([n for n, _ in even], [s for _, s in even]),
        "fit_odd": log_linear_fit([n for n, _ in odd], [s for _, s in odd]),
        "moving_window_5": window_fits(rows, 5),
        "block_minima_3": minima3,
        "block_minima_3_fit": log_linear_fit(min_ns, min_ss),
        "endpoint_growth": serial(ss[-1] / ss[0]),
        "endpoint_radius": rows[-1]["radius"],
        "endpoint_shellMass": rows[-1]["shellMass"],
    }


def run_case(label: str, planted: tuple[str, str, str] | None, lam: int, args) -> dict:
    print(f"BUILD {label}: lambda={lam} Nmax={args.max_modes} dps={args.dps}", flush=True)
    Hmax, _idxmax, L = build_mp(lam, args.max_modes, args.dps, planted=planted)
    rows = []
    previous = None
    for n_modes in range(args.min_modes, args.max_modes + 1):
        offset = args.max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        x = canonical_solution(H)
        s_value = energy(x)
        radius = 1 / s_value
        mass = shell_mass(x)
        ratio = None if previous is None else s_value / previous
        row = {
            "N": n_modes,
            "S_N": serial(s_value),
            "radius": serial(radius),
            "shellMass": serial(mass),
            "ratio": None if ratio is None else serial(ratio),
        }
        rows.append(row)
        print(
            f"ROW {label:18s} lam={lam:2d} N={n_modes:2d} "
            f"S={serial(s_value, 12):>16s} r={serial(radius, 12):>16s} "
            f"shell={serial(mass, 10):>13s} ratio={('-' if ratio is None else serial(ratio, 10)):>13s}",
            flush=True,
        )
        previous = s_value
    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "lambda": lam,
        "L": serial(L),
        "dps": args.dps,
        "N_min": args.min_modes,
        "N_max": args.max_modes,
        "rows": rows,
        "summary": summarize(rows),
    }


def write_outputs(result: dict, output_stem: Path) -> None:
    output_stem.with_suffix(".json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii"
    )
    lines = ["case\tlambda\tstrength\tbeta\tN\tS_N\tradius\tshellMass\tratio"]
    for case in result["cases"]:
        planted = case["planted"] or {}
        for row in case["rows"]:
            lines.append(
                "\t".join(
                    [
                        case["label"],
                        str(case["lambda"]),
                        planted.get("strength", ""),
                        planted.get("beta", ""),
                        str(row["N"]),
                        row["S_N"],
                        row["radius"],
                        row["shellMass"],
                        row["ratio"] or "",
                    ]
                )
            )
    output_stem.with_suffix(".tsv").write_text("\n".join(lines) + "\n", encoding="ascii")


def parse_csv(values: str, cast):
    return [cast(item.strip()) for item in values.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambdas", default=",".join(str(x) for x in DEFAULT_LAMBDAS))
    parser.add_argument("--betas", default=",".join(DEFAULT_BETAS))
    parser.add_argument("--strengths", default=",".join(DEFAULT_STRENGTHS))
    parser.add_argument("--min-modes", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument(
        "--output-stem", type=Path, default=HERE / "E77_1b_attribution_results"
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.1b requires dps >= 50")
    if args.max_modes < 18:
        parser.error("E77.1b requires max-modes >= 18")

    lambdas = parse_csv(args.lambdas, int)
    betas = parse_csv(args.betas, str)
    strengths = parse_csv(args.strengths, str)
    cases: list[tuple[str, tuple[str, str, str] | None, int]] = []
    for lam in lambdas:
        cases.append((f"zeta-lam{lam}", None, lam))
        for strength in strengths:
            for beta in betas:
                cases.append(
                    (
                        f"plant-lam{lam}-b{beta}-s{strength}",
                        (GAMMA, beta, strength),
                        lam,
                    )
                )

    result = {
        "probe": "E77.1b enlarged attribution run",
        "method": "one build per case; nested central principal sections",
        "parameters": {
            "lambdas": lambdas,
            "dps": args.dps,
            "N_min": args.min_modes,
            "N_max": args.max_modes,
            "gamma": GAMMA,
            "betas": betas,
            "strengths": strengths,
            "shell_width": 2,
        },
        "cases": [],
    }
    for label, planted, lam in cases:
        result["cases"].append(run_case(label, planted, lam, args))
        write_outputs(result, args.output_stem)
    print(f"WROTE {args.output_stem.with_suffix('.json')}")
    print(f"WROTE {args.output_stem.with_suffix('.tsv')}")


if __name__ == "__main__":
    main()
