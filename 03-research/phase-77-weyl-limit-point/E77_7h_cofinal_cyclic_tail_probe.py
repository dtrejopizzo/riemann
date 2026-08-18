#!/usr/bin/env python3
"""E77.7h cofinal cyclic-tail stability probe."""

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
from E77_7h_cyclic_pole_capture_probe import analyze_reference  # noqa: E402
from E77_7h_feshbach_envelope_probe import GAMMA, serial  # noqa: E402


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def top_signature(row, top_k: int):
    output = []
    for pole in row["top_ritz_poles"][:top_k]:
        output.append(
            {
                "kappa": mp.mpf(pole["ritz_kappa"]),
                "fraction": mp.mpf(pole["ritz_fraction"]),
                "lower_denom": mp.mpf(pole["lower_denom_interval"]),
            }
        )
    return output


def compare_signature(prev, cur):
    if not prev:
        return []
    output = []
    for j, item in enumerate(cur):
        nearest = min(prev, key=lambda old: abs(old["kappa"] - item["kappa"]))
        output.append(
            {
                "rank": j + 1,
                "kappa": serial(item["kappa"]),
                "nearest_previous_kappa": serial(nearest["kappa"]),
                "relative_kappa_drift": serial(
                    abs(item["kappa"] - nearest["kappa"]) / max(abs(item["kappa"]), mp.mpf("1e-100"))
                ),
                "fraction": serial(item["fraction"]),
                "nearest_previous_fraction": serial(nearest["fraction"]),
                "fraction_drift": serial(item["fraction"] - nearest["fraction"]),
            }
        )
    return output


def run_build(label, lam, max_list, ref_modes, dps, lanczos_steps, top_k, planted):
    rows = []
    prev_signature = []
    prev_sigma = None
    prev_delta = None
    for max_modes in max_list:
        Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes, lanczos_steps)
        signature = top_signature(row, top_k)
        sigma = mp.mpf(row["exact_sigma_delta"])
        delta = mp.mpf(row["delta"])
        row["max_modes"] = max_modes
        row["L"] = serial(L)
        row["top_signature_drift_from_previous_M"] = compare_signature(prev_signature, signature)
        row["sigma_ratio_to_previous_M"] = (
            serial(sigma / prev_sigma) if prev_sigma not in (None, mp.mpf("0")) else "NA"
        )
        row["delta_ratio_to_previous_M"] = (
            serial(delta / prev_delta) if prev_delta not in (None, mp.mpf("0")) else "NA"
        )
        rows.append(row)
        print(
            f"{label:6s} M={max_modes:2d} R={ref_modes:2d} "
            f"dim={row['actual_lanczos_dimension']:2d} "
            f"delta={mp.nstr(delta, 8):>12s} "
            f"sigRatio={row['sigma_ratio_to_previous_M']:>12s} "
            f"top999={row['captured_counts']['0.999']['count']:>2} "
            f"top8={mp.nstr(mp.mpf(row['partial_interval_upper_top8_over_exact']), 8):>10s}",
            flush=True,
        )
        prev_signature = signature
        prev_sigma = sigma
        prev_delta = delta
    return {
        "label": label,
        "lambda": lam,
        "ref_modes": ref_modes,
        "max_modes_list": max_list,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-list", default="16,18")
    parser.add_argument("--ref-modes", type=int, default=14)
    parser.add_argument("--lanczos-steps", type=int, default=40)
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_cofinal_cyclic_tail_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h cofinal cyclic-tail audit requires dps >= 60")
    max_list = [int(value) for value in args.max_list.split(",") if value]
    if not max_list or min(max_list) <= args.ref_modes:
        parser.error("need all max modes strictly larger than ref-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h cofinal cyclic-tail stability probe",
        "parameters": {
            "lambda": args.lam,
            "max_list": max_list,
            "ref_modes": args.ref_modes,
            "lanczos_steps": args.lanczos_steps,
            "top_k": args.top_k,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite M-stability audit only. Stable dominant cyclic poles over these "
            "sections do not certify the infinite cofinal tail."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, max_list, args.ref_modes, args.dps, args.lanczos_steps, args.top_k, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
