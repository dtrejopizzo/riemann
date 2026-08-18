#!/usr/bin/env python3
"""E78.8 audit the denominator 1+W on the safe axis for both builds."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_3c_two_generator_ident_probe import (  # noqa: E402
    GAMMA,
    generated_values,
    right_transfer_data,
    serial,
    two_generator_data,
)


def cserial(z, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def run_case(label: str, planted, lam_int: int, max_modes: int, dps: int, sigmas: list[mp.mpf]):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    rows = []
    for n_modes in range(8, max_modes + 1, 2):
        H, idx = section(Hmax, idxmax, max_modes, n_modes)
        _mu, A, db_idx, inner, _x = right_transfer_data(H, idx)
        d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
        sigma_rows = []
        min_abs = None
        for sigma in sigmas:
            z = 1j * sigma
            _T, _logd, F, W = generated_values(z, d, u, v, db, aa, bb, ub, vb)
            Fabs = abs(F)
            min_abs = Fabs if min_abs is None else min(min_abs, Fabs)
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "F_abs": serial(Fabs),
                    "W_abs": serial(abs(W)),
                    "F": cserial(F),
                    "W": cserial(W),
                }
            )
        rows.append(
            {
                "N": n_modes,
                "min_F_abs": serial(min_abs),
                "sigmas": sigma_rows,
            }
        )
    return {
        "label": label,
        "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E78_8_w_denominator_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E78.8 requires dps >= 60")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Safe-axis denominator audit for F=1+W",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        case = run_case(label, planted, args.lam, args.max_modes, args.dps, sigmas)
        result["cases"].append(case)
        print(f"CASE {label}", flush=True)
        for row in case["rows"]:
            print(f"N={row['N']:2d} min|1+W|={serial(mp.mpf(row['min_F_abs']),8)}", flush=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
