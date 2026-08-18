#!/usr/bin/env python3
"""E77.7 fixed-L Tricomi-LP setup and arithmetic-tail audit.

At a fixed arithmetic cutoff lambda, the diagonal prime-power contribution is
an explicit finite trigonometric polynomial in the Fourier index.  This probe
checks the formula against independently integrated CCM entries and measures
its tail block RMS.  A nonzero tail RMS falsifies the proposed decomposition
"pure Cauchy+diagonal operator plus a decaying arithmetic perturbation".
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

from P76_002_mp_entry_audit import entry, primes_upto  # noqa: E402


GAMMA = "14.134725141734693790"
PLANT = (GAMMA, "0.30", "5.0")


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def prime_power_terms(lam: int, L: mp.mpf):
    terms = []
    for p in primes_upto(lam * lam):
        logp = mp.log(p)
        power = p
        exponent = 1
        while power <= lam * lam:
            y = exponent * logp
            coefficient = -2 * logp * mp.power(power, mp.mpf("-0.5")) * (1 - y / L)
            if coefficient:
                terms.append(
                    {
                        "p": p,
                        "k": exponent,
                        "power": power,
                        "y": y,
                        "alpha": y / L,
                        "coefficient": coefficient,
                    }
                )
            if power > (lam * lam) // p:
                break
            power *= p
            exponent += 1
    return terms


def arithmetic_diagonal(n: int, terms) -> mp.mpf:
    return mp.fsum(
        term["coefficient"] * mp.cos(2 * mp.pi * n * term["alpha"])
        for term in terms
    )


def block_stats(values: list[mp.mpf], start: int, stop: int):
    block = values[start:stop]
    rms = mp.sqrt(mp.fsum(value**2 for value in block) / len(block))
    mean = mp.fsum(block) / len(block)
    return {
        "start": start,
        "stop": stop - 1,
        "mean": serial(mean),
        "rms": serial(rms),
        "max_abs": serial(max(abs(value) for value in block)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-index", type=int, default=4000)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--output", type=Path, default=HERE / "E77_7_tricomi_lp_results.json")
    args = parser.parse_args()
    if args.max_index < 400:
        parser.error("max-index must be at least 400")
    if args.dps < 50:
        parser.error("E77.7 requires dps >= 50")

    mp.mp.dps = args.dps
    L = 2 * mp.log(args.lam)
    terms = prime_power_terms(args.lam, L)
    values = [arithmetic_diagonal(n, terms) for n in range(args.max_index + 1)]
    edges = [0, 100, 500, 1000, 2000, args.max_index + 1]
    edges = sorted(set(edge for edge in edges if edge <= args.max_index + 1))
    if edges[-1] != args.max_index + 1:
        edges.append(args.max_index + 1)
    blocks = [block_stats(values, a, b) for a, b in zip(edges, edges[1:]) if b > a]

    validation = []
    for n in (0, 4, 8, 12, 16, 24):
        full = entry(n, n, L, mp.mpf(args.lam), include_arith=True)
        arch = entry(n, n, L, mp.mpf(args.lam), include_arith=False)
        formula = arithmetic_diagonal(n, terms)
        planted = entry(n, n, L, mp.mpf(args.lam), include_arith=True, planted=PLANT)
        defect = abs((full - arch) - formula) / max(1, abs(formula))
        validation.append(
            {
                "n": n,
                "integrated_arithmetic_diagonal": serial(full - arch),
                "formula_arithmetic_diagonal": serial(formula),
                "formula_relative_defect": serial(defect),
                "planted_extra_diagonal": serial(planted - full),
            }
        )

    term_rows = [
        {
            "p": term["p"],
            "k": term["k"],
            "power": term["power"],
            "alpha": serial(term["alpha"]),
            "coefficient": serial(term["coefficient"]),
        }
        for term in terms
    ]
    result = {
        "statement": "Fixed-L arithmetic diagonal is a nondecaying finite trigonometric polynomial",
        "parameters": {
            "lambda": args.lam,
            "L": serial(L),
            "max_index": args.max_index,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "exact_formula": "-2 sum_{p^k<=lambda^2} log(p) p^(-k/2) (1-k log(p)/L) cos(2 pi n k log(p)/L)",
        "terms": term_rows,
        "block_statistics": blocks,
        "validation": validation,
        "verdict": (
            "The zeta prime-power diagonal does not decay with Fourier index. "
            "The planted addition does not remove this base obstruction."
        ),
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"terms={len(terms)} max_formula_defect={serial(max(mp.mpf(row['formula_relative_defect']) for row in validation), 8)}")
    for block in blocks:
        print(
            f"n={block['start']:4d}..{block['stop']:4d} "
            f"mean={serial(block['mean'], 8):>12s} rms={serial(block['rms'], 8):>12s} "
            f"max={serial(block['max_abs'], 8):>12s}"
        )
    print("plant extras", " ".join(f"n={row['n']}:{serial(row['planted_extra_diagonal'], 6)}" for row in validation))
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
