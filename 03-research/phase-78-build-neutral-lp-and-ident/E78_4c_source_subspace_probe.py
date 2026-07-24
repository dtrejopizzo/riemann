#!/usr/bin/env python3
"""E78.4c probe the source/subspace side of neutral-ground-Cauchy."""

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
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def cserial(value, digits: int = 24) -> dict[str, str]:
    return {"re": serial(mp.re(value), digits), "im": serial(mp.im(value), digits)}


def section(Hmax, idxmax, max_modes, modes):
    off = max_modes - modes
    return (
        Hmax[off : Hmax.rows - off, off : Hmax.cols - off],
        idxmax[off : len(idxmax) - off],
    )


def inner_source_overlap(H: mp.matrix, idx: list[int]):
    mu, A, _db_idx, _inner, _x = right_transfer_data(H, idx)
    vals, vecs = mp.eighe(A)
    j0 = min(range(len(vals)), key=lambda j: abs(vals[j]))
    v0 = mp.matrix([[vecs[j, j0]] for j in range(vecs.rows)])
    g_right = mp.matrix([[H[j + 1, H.cols - 1]] for j in range(H.rows - 2)])
    overlap = mp.fsum(mp.conj(v0[j]) * g_right[j] for j in range(v0.rows))
    return mu, vals[j0], overlap


def full_ground_boundary_data(H: mp.matrix):
    vals, vecs = mp.eighe(H)
    mu_full = vals[0]
    xi = vecs[:, 0]
    return mu_full, xi[0], xi[H.rows - 1]


def run_case(label: str, planted, lam: int, max_modes: int, dps: int):
    mp.mp.dps = dps
    Hmax, idxmax, _L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for modes in range(6, max_modes + 1):
        H, idx = section(Hmax, idxmax, max_modes, modes)
        mu_inner, lam0, overlap = inner_source_overlap(H, idx)
        mu_full, left_bdry, right_bdry = full_ground_boundary_data(H)
        rows.append(
            {
                "N": modes,
                "mu_section": serial(mu_full),
                "mu_inner_shift_reference": serial(mu_inner),
                "lambda0_abs": serial(abs(lam0)),
                "source_overlap_abs": serial(abs(overlap)),
                "source_overlap": cserial(overlap),
                "left_boundary_abs": serial(abs(left_bdry)),
                "right_boundary_abs": serial(abs(right_bdry)),
                "left_boundary": cserial(left_bdry),
                "right_boundary": cserial(right_bdry),
            }
        )
    return {
        "label": label,
        "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=14)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E78_4c_source_subspace_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E78.4c requires dps >= 60")
    result = {
        "statement": "Source/subspace-side audit for neutral-ground-Cauchy",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        case = run_case(label, planted, args.lam, args.max_modes, args.dps)
        result["cases"].append(case)
        print(f"CASE {label}", flush=True)
        for row in case["rows"]:
            print(
                f"N={row['N']:2d} |lam0|={serial(mp.mpf(row['lambda0_abs']),8):>12s} "
                f"|v*g|={serial(mp.mpf(row['source_overlap_abs']),8):>12s} "
                f"|xiL|={serial(mp.mpf(row['left_boundary_abs']),8):>12s}",
                flush=True,
            )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
