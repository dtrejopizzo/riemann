#!/usr/bin/env python3
"""E77.7h shell-transfer defect localization probe."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(HERE))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E77_7h_feshbach_envelope_probe import GAMMA, serial  # noqa: E402
from E77_7h_geometric_shell_residual_probe import add_trends, analyze_pair  # noqa: E402
from E77_7h_shell_stieltjes_increment_probe import parse_pairs  # noqa: E402


def summarize_outer_component(row):
    best = None
    for comp in row["components"]:
        coord = comp["coord"]
        if coord is None:
            continue
        if best is None or abs(coord) > abs(best["coord"]):
            best = comp
    return best or {}


def run_case(case, lam, max_modes, ref_modes, pairs, dps):
    Hbig, idxbig, L = build_mp(
        lam,
        max_modes,
        dps,
        include_arith=case["include_arith"],
        planted=case["planted"],
    )
    rows = [analyze_pair(Hbig, idxbig, ref_modes, old, new) for old, new in pairs]
    rows = add_trends(rows)
    for row in rows:
        outer = summarize_outer_component(row)
        row["outer_component_summary"] = outer
        print(
            f"{case['label']:10s} R={ref_modes:2d} "
            f"{row['old_modes']:2d}->{row['new_modes']:2d} "
            f"logE={row['energy_over_eta_log10']:>12s} "
            f"logCancel={row['cancellation_ratio_log10']:>12s} "
            f"outerAbs={outer.get('abs_residual_over_abs_direct', 'NA'):>12s}",
            flush=True,
        )
    return {
        "label": case["label"],
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "ref_modes": ref_modes,
        "pairs": pairs,
        "include_arith": case["include_arith"],
        "planted": None
        if case["planted"] is None
        else {"gamma": case["planted"][0], "beta": case["planted"][1], "strength": case["planted"][2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--ref-modes", type=int, default=10)
    parser.add_argument("--pairs", default="12:14,14:16,16:18,18:20")
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_shell_transfer_defect_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h shell-transfer defect requires dps >= 60")
    pairs = parse_pairs(args.pairs)
    if not pairs or max(new for _old, new in pairs) > args.max_modes:
        parser.error("pairs must fit inside max-modes")
    if min(old for old, _new in pairs) <= args.ref_modes:
        parser.error("all old modes must be larger than ref-modes")
    mp.mp.dps = args.dps
    cases = [
        {"label": "zeta", "include_arith": True, "planted": None},
        {"label": "arch_only", "include_arith": False, "planted": None},
        {"label": "plant", "include_arith": True, "planted": (GAMMA, "0.30", "5.0")},
    ]
    result = {
        "statement": "E77.7h shell-transfer defect localization probe",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite localization probe. It compares packages but does not prove "
            "the infinite Hilbert/cell transfer defect."
        ),
        "cases": [run_case(case, args.lam, args.max_modes, args.ref_modes, pairs, args.dps) for case in cases],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
