#!/usr/bin/env python3
"""E77.7h shell residual-cancellation scaling probe."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from E77_7h_feshbach_envelope_probe import GAMMA, serial  # noqa: E402
from E77_7h_shell_stieltjes_increment_probe import parse_pairs  # noqa: E402
from E77_7h_shorted_shell_energy_probe import analyze_pair  # noqa: E402
from P76_002_mp_entry_audit import build_mp  # noqa: E402


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def add_trends(rows):
    previous = None
    for row in rows:
        energy = mp.mpf(row["energy_over_eta"])
        ratio = mp.mpf(row["cancellation_ratio"])
        residual = mp.mpf(row["residual_norm"])
        direct = mp.mpf(row["direct_shell_norm"])
        if previous is None:
            row["energy_over_eta_ratio_to_previous_shell"] = "NA"
            row["cancellation_ratio_to_previous_shell"] = "NA"
            row["residual_norm_ratio_to_previous_shell"] = "NA"
            row["direct_norm_ratio_to_previous_shell"] = "NA"
        else:
            row["energy_over_eta_ratio_to_previous_shell"] = serial(energy / previous["energy"]) if previous["energy"] else "inf"
            row["cancellation_ratio_to_previous_shell"] = serial(ratio / previous["ratio"]) if previous["ratio"] else "inf"
            row["residual_norm_ratio_to_previous_shell"] = serial(residual / previous["residual"]) if previous["residual"] else "inf"
            row["direct_norm_ratio_to_previous_shell"] = serial(direct / previous["direct"]) if previous["direct"] else "inf"
        row["energy_over_eta_log10"] = log10_serial(energy)
        row["cancellation_ratio_log10"] = log10_serial(ratio)
        row["residual_norm_log10"] = log10_serial(residual)
        previous = {
            "energy": energy,
            "ratio": ratio,
            "residual": residual,
            "direct": direct,
        }
    return rows


def run_build(label, lam, max_modes, pairs, ref_modes, dps, planted):
    Hbig, idxbig, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for old_modes, new_modes in pairs:
        row = analyze_pair(Hbig, idxbig, ref_modes, old_modes, new_modes)
        row["shell_distance_from_ref"] = new_modes - ref_modes
        rows.append(row)
    rows = add_trends(rows)
    for row in rows:
        print(
            f"{label:6s} R={ref_modes:2d} {row['old_modes']:2d}->{row['new_modes']:2d} "
            f"logE={row['energy_over_eta_log10']:>12s} "
            f"logCancel={row['cancellation_ratio_log10']:>12s} "
            f"Eratio={row['energy_over_eta_ratio_to_previous_shell']:>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "ref_modes": ref_modes,
        "pairs": pairs,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
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
        default=HERE / "E77_7h_shell_residual_cancellation_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h shell residual cancellation requires dps >= 60")
    pairs = parse_pairs(args.pairs)
    if not pairs or max(new for _old, new in pairs) > args.max_modes:
        parser.error("pairs must fit inside max-modes")
    if min(old for old, _new in pairs) <= args.ref_modes:
        parser.error("all old modes must be larger than ref-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h shell residual-cancellation scaling probe",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite scaling probe. Trends across a short shell range suggest the "
            "next theorem but do not prove cofinal summability."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, pairs, args.ref_modes, args.dps, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
