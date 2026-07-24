#!/usr/bin/env python3
"""E77.7g BTG-DIV audit under moving Ritz references."""

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


def log10_serial(value, digits: int = 18) -> str:
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def norm(vector: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vector[j]) ** 2 for j in range(vector.rows)))


def centered_section(Hmax: mp.matrix, idxmax: list[int], max_modes: int, modes: int):
    offset = max_modes - modes
    return (
        Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset],
        idxmax[offset : len(idxmax) - offset],
    )


def summarize_groups(rows):
    output = {}
    for label, selected in [
        ("even", [row for row in rows if row["N"] % 2 == 0]),
        ("odd", [row for row in rows if row["N"] % 2 == 1]),
        ("last4", rows[-4:]),
        ("all", rows),
    ]:
        if not selected:
            continue
        energies = [mp.mpf(row["S_value"]) for row in selected]
        ground_fracs = [mp.mpf(row["ground_fraction"]) for row in selected]
        output[label] = {
            "count": len(selected),
            "min_log10_S": log10_serial(min(energies)),
            "max_log10_S": log10_serial(max(energies)),
            "last_log10_S": log10_serial(energies[-1]),
            "min_ground_fraction": serial(min(ground_fracs)),
            "max_ground_fraction": serial(max(ground_fracs)),
        }
    return output


def spectral_decomposition(inner: mp.matrix, source: mp.matrix, mu_ref: mp.mpf, top_k: int):
    values, vectors = mp.eigsy(inner)
    contributions = []
    total = mp.mpf("0")
    for j in range(values.rows):
        vec = vectors[:, j]
        coeff = (vec.T * source)[0]
        signed_gap = values[j] - mu_ref
        contribution = abs(coeff) ** 2 / abs(signed_gap) ** 2
        total += contribution
        contributions.append(
            {
                "j": j,
                "nu_j": values[j],
                "gap_signed": signed_gap,
                "gap_abs": abs(signed_gap),
                "coeff_abs": abs(coeff),
                "contribution": contribution,
            }
        )
    dominant = max(contributions, key=lambda item: item["contribution"])
    cumulative = mp.mpf("0")
    first_modes = []
    for item in contributions[: min(top_k, len(contributions))]:
        cumulative += item["contribution"]
        first_modes.append(
            {
                "j": item["j"],
                "nu_j": serial(item["nu_j"]),
                "gap_abs": serial(item["gap_abs"]),
                "coeff_abs": serial(item["coeff_abs"]),
                "contribution": serial(item["contribution"]),
                "fraction": serial(item["contribution"] / total) if total else "0",
                "cumulative_fraction": serial(cumulative / total) if total else "0",
            }
        )
    top_sorted = sorted(contributions, key=lambda item: item["contribution"], reverse=True)[:top_k]
    return {
        "total": total,
        "dominant": dominant,
        "ground": contributions[0],
        "first_modes": first_modes,
        "top_modes": [
            {
                "j": item["j"],
                "gap_abs": serial(item["gap_abs"]),
                "coeff_abs": serial(item["coeff_abs"]),
                "contribution": serial(item["contribution"]),
                "fraction": serial(item["contribution"] / total) if total else "0",
            }
            for item in top_sorted
        ],
    }


def reference_run(Hmax, idxmax, max_modes, ref_modes, min_modes, top_k):
    Href, _idx_ref = centered_section(Hmax, idxmax, max_modes, ref_modes)
    ref_values, _ref_vectors = mp.eigsy(Href)
    mu_ref = ref_values[0]
    rows = []
    previous_S = None
    for modes in range(min_modes, ref_modes + 1):
        H, _idx = centered_section(Hmax, idxmax, max_modes, modes)
        inner = H[1:-1, 1:-1]
        source = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
        spec = spectral_decomposition(inner, source, mu_ref, top_k)
        S_value = spec["total"]
        growth = mp.mpf("0") if previous_S is None else S_value / previous_S
        previous_S = S_value
        ground = spec["ground"]
        dominant = spec["dominant"]
        row = {
            "N": modes,
            "parity": "even" if modes % 2 == 0 else "odd",
            "mu_ref": serial(mu_ref),
            "S_value": serial(S_value),
            "log10_S": log10_serial(S_value),
            "radius_proxy": serial(1 / S_value) if S_value else "inf",
            "growth_ratio": serial(growth),
            "source_norm": serial(norm(source)),
            "ground_gap_abs": serial(ground["gap_abs"]),
            "ground_coeff_abs": serial(ground["coeff_abs"]),
            "ground_trace_over_gap": serial(
                ground["coeff_abs"] / max(mp.mpf("1e-100"), ground["gap_abs"])
            ),
            "ground_fraction": serial(ground["contribution"] / S_value) if S_value else "0",
            "dominant_j": dominant["j"],
            "dominant_gap_abs": serial(dominant["gap_abs"]),
            "dominant_coeff_abs": serial(dominant["coeff_abs"]),
            "dominant_fraction": serial(dominant["contribution"] / S_value) if S_value else "0",
            "first_modes": spec["first_modes"],
            "top_modes": spec["top_modes"],
        }
        rows.append(row)
    return {
        "reference_modes": ref_modes,
        "reference_dim": Href.rows,
        "mu_ref": serial(mu_ref),
        "next_ritz_gap": serial(ref_values[1] - ref_values[0]) if ref_values.rows > 1 else "NA",
        "rows": rows,
        "group_summary": summarize_groups(rows),
    }


def run_build(label, lam, max_modes, dps, refs, min_modes, top_k, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_values, _max_vectors = mp.eigsy(Hmax)
    reference_data = []
    for ref_modes in refs:
        reference_data.append(reference_run(Hmax, idxmax, max_modes, ref_modes, min_modes, top_k))
    sensitivity_rows = []
    common_Ns = range(min_modes, min(refs) + 1)
    for modes in common_Ns:
        values = []
        for ref_data in reference_data:
            row = next(row for row in ref_data["rows"] if row["N"] == modes)
            values.append(mp.mpf(row["S_value"]))
        sensitivity_rows.append(
            {
                "N": modes,
                "min_log10_S_over_refs": log10_serial(min(values)),
                "max_log10_S_over_refs": log10_serial(max(values)),
                "spread_log10_S": serial(mp.log10(max(values)) - mp.log10(min(values)))
                if min(values) > 0
                else "inf",
            }
        )
    print(f"{label}: max ref mu={serial(max_values[0], 18)}")
    for ref_data in reference_data:
        last = ref_data["rows"][-1]
        print(
            f"{label:6s} R={ref_data['reference_modes']:2d} "
            f"mu={serial(mp.mpf(ref_data['mu_ref']), 10):>14s} "
            f"N={last['N']:2d} logS={last['log10_S']:>12s} "
            f"j*={last['dominant_j']:2d} frac*={serial(mp.mpf(last['dominant_fraction']), 6):>10s} "
            f"frac0={serial(mp.mpf(last['ground_fraction']), 6):>10s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "max_dim": Hmax.rows,
        "max_section_mu": serial(max_values[0]),
        "max_section_gap": serial(max_values[1] - max_values[0])
        if max_values.rows > 1
        else "NA",
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "references": reference_data,
        "common_reference_sensitivity": sensitivity_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--refs", default="12,14,16,18")
    parser.add_argument("--min-modes", type=int, default=6)
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7g_btg_mu_sensitivity_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7g requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) > args.max_modes:
        parser.error("refs must be nonempty and <= max-modes")
    if args.min_modes < 2 or args.min_modes > min(refs):
        parser.error("need 2 <= min-modes <= min(refs)")
    mp.mp.dps = args.dps
    result = {
        "statement": "BTG-DIV spectral decomposition and sensitivity to Ritz references",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "min_modes": args.min_modes,
            "top_k": args.top_k,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Every mu_ref here is a finite Ritz upper bound for the unknown mu_L. "
            "The probe measures stability and spectral anatomy; it does not "
            "identify the true infinite-volume value."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, refs, args.min_modes, args.top_k, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
