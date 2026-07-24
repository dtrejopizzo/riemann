#!/usr/bin/env python3
"""E77.7h cyclic spectral-measure profile for WFE-CYCLIC-TAIL."""

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
from E77_7h_feshbach_envelope_probe import (  # noqa: E402
    GAMMA,
    centered_section,
    complement_basis,
    fixed_point_bisect,
    norm,
    padded_ref_vector,
    serial,
    spectral_self_energy,
)


def log10_serial(value, digits: int = 18) -> str:
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def spectral_measure(Hmax: mp.matrix, idxmax: list[int], max_modes: int, ref_modes: int):
    Href, _idx_ref, offset = centered_section(Hmax, idxmax, max_modes, ref_modes)
    ref_values, ref_vectors = mp.eigsy(Href)
    mu_ref = ref_values[0]
    v_ref = ref_vectors[:, 0]
    if v_ref[ref_modes] < 0:
        for j in range(v_ref.rows):
            v_ref[j] = -v_ref[j]
    v_full = padded_ref_vector(v_ref, Hmax.rows, offset)
    W = complement_basis(ref_vectors, Hmax.rows, offset)
    K = W.T * Hmax * W
    h = W.T * Hmax * v_full
    kvals, kvecs = mp.eigsy(K)
    coeffs = [abs((kvecs[:, j].T * h)[0]) for j in range(kvals.rows)]
    full_values, _ = mp.eigsy(Hmax)
    mu_full = full_values[0]
    delta = mu_ref - mu_full
    sigma, rows = spectral_self_energy(kvals, coeffs, mu_ref, delta)
    eta2_sigma, _ = spectral_self_energy(kvals, coeffs, mu_ref, 2 * delta)
    eta4_sigma, _ = spectral_self_energy(kvals, coeffs, mu_ref, 4 * delta)
    eta10_sigma, _ = spectral_self_energy(kvals, coeffs, mu_ref, 10 * delta)
    fixed_eta = fixed_point_bisect(kvals, coeffs, mu_ref, mp.mpf("0"), max(delta, mp.mpf("1e-80")))
    return {
        "mu_ref": mu_ref,
        "mu_full": mu_full,
        "delta": delta,
        "kvals": kvals,
        "coeffs": coeffs,
        "rows": rows,
        "sigma": sigma,
        "eta2_sigma": eta2_sigma,
        "eta4_sigma": eta4_sigma,
        "eta10_sigma": eta10_sigma,
        "fixed_eta": fixed_eta,
        "h_norm": norm(h),
    }


def window_summary(rows, mu_ref: mp.mpf, delta: mp.mpf, total_mass: mp.mpf, sigma: mp.mpf):
    thresholds = [
        ("negative", None),
        ("kappa_le_delta", delta),
        ("kappa_le_sqrt_delta", mp.sqrt(delta) if delta > 0 else mp.mpf("0")),
        ("kappa_le_delta_quarter_root", mp.root(delta, 4) if delta > 0 else mp.mpf("0")),
        ("kappa_le_one", mp.mpf("1")),
    ]
    output = []
    for label, threshold in thresholds:
        mass = mp.mpf("0")
        contribution = mp.mpf("0")
        count = 0
        min_kappa = mp.inf
        max_kappa = -mp.inf
        for _j, omega, _denom, coeff, contrib in rows:
            kappa = omega - mu_ref
            take = kappa < 0 if threshold is None else kappa <= threshold
            if not take:
                continue
            count += 1
            mass += coeff**2
            contribution += contrib
            min_kappa = min(min_kappa, kappa)
            max_kappa = max(max_kappa, kappa)
        output.append(
            {
                "label": label,
                "count": count,
                "mass": serial(mass),
                "mass_fraction": serial(mass / total_mass) if total_mass else "0",
                "self_energy": serial(contribution),
                "self_energy_fraction": serial(contribution / sigma) if sigma else "0",
                "min_kappa": serial(min_kappa) if count else "NA",
                "max_kappa": serial(max_kappa) if count else "NA",
            }
        )
    return output


def contribution_summary(rows, mu_ref: mp.mpf, sigma: mp.mpf):
    sorted_rows = sorted(rows, key=lambda item: item[4], reverse=True)
    output = []
    cumulative = mp.mpf("0")
    for rank, row in enumerate(sorted_rows[:10], start=1):
        j, omega, denom, coeff, contrib = row
        cumulative += contrib
        output.append(
            {
                "rank": rank,
                "j": j,
                "kappa": serial(omega - mu_ref),
                "denominator_at_delta": serial(denom),
                "coeff_abs": serial(coeff),
                "contribution": serial(contrib),
                "fraction": serial(contrib / sigma) if sigma else "0",
                "cumulative_fraction": serial(cumulative / sigma) if sigma else "0",
            }
        )
    needed = {}
    for target in [mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), mp.mpf("0.999")]:
        cumulative = mp.mpf("0")
        count = 0
        for row in sorted_rows:
            cumulative += row[4]
            count += 1
            if sigma and cumulative / sigma >= target:
                break
        needed[str(target)] = count
    return output, needed


def analyze_reference(Hmax, idxmax, max_modes: int, ref_modes: int):
    data = spectral_measure(Hmax, idxmax, max_modes, ref_modes)
    mu_ref = data["mu_ref"]
    rows = []
    # Replace the rows from spectral_self_energy with explicit kappa values.
    for j, omega, denom, coeff, contrib in data["rows"]:
        rows.append((j, omega, denom, coeff, contrib))
    total_mass = data["h_norm"] ** 2
    contrib_rows, needed = contribution_summary(rows, mu_ref, data["sigma"])
    windows = window_summary(rows, mu_ref, data["delta"], total_mass, data["sigma"])
    min_kappa = min((row[1] - mu_ref for row in rows), default=mp.inf)
    neg_mass = mp.fsum(row[3] ** 2 for row in rows if row[1] - mu_ref < 0)
    neg_sigma = mp.fsum(row[4] for row in rows if row[1] - mu_ref < 0)
    return {
        "reference_modes": ref_modes,
        "mu_ref": serial(mu_ref),
        "mu_full_max_section": serial(data["mu_full"]),
        "delta": serial(data["delta"]),
        "delta_log10": log10_serial(data["delta"]),
        "fixed_eta": serial(data["fixed_eta"]),
        "h_mass": serial(total_mass),
        "h_mass_log10": log10_serial(total_mass),
        "min_kappa": serial(min_kappa),
        "negative_mass": serial(neg_mass),
        "negative_mass_fraction": serial(neg_mass / total_mass) if total_mass else "0",
        "negative_self_energy_fraction": serial(neg_sigma / data["sigma"]) if data["sigma"] else "0",
        "sigma_at_delta": serial(data["sigma"]),
        "sigma_at_delta_defect": serial(
            abs(data["sigma"] - data["delta"]) / max(mp.mpf("1"), abs(data["sigma"]), abs(data["delta"]))
        ),
        "sigma_2delta_over_2delta": serial(data["eta2_sigma"] / (2 * data["delta"]))
        if data["delta"] > 0
        else "inf",
        "sigma_4delta_over_4delta": serial(data["eta4_sigma"] / (4 * data["delta"]))
        if data["delta"] > 0
        else "inf",
        "sigma_10delta_over_10delta": serial(data["eta10_sigma"] / (10 * data["delta"]))
        if data["delta"] > 0
        else "inf",
        "contribution_top10": contrib_rows,
        "contributors_needed": needed,
        "window_summary": windows,
    }


def run_build(label, lam, max_modes, dps, refs, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for ref_modes in refs:
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes)
        print(
            f"{label:6s} R={ref_modes:2d} "
            f"delta={mp.nstr(mp.mpf(row['delta']), 8):>12s} "
            f"negMass={mp.nstr(mp.mpf(row['negative_mass_fraction']), 6):>10s} "
            f"negSelf={mp.nstr(mp.mpf(row['negative_self_energy_fraction']), 6):>10s} "
            f"need90={row['contributors_needed']['0.9']:>3} "
            f"sig2/2d={mp.nstr(mp.mpf(row['sigma_2delta_over_2delta']), 8):>10s}",
            flush=True,
        )
        rows.append(row)
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "max_dim": Hmax.rows,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "references": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--refs", default="8,10,12,14,16")
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_wfe_cyclic_tail_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h cyclic tail audit requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) >= args.max_modes:
        parser.error("refs must be nonempty and strictly below max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h cyclic spectral-measure profile for WFE-CYCLIC-TAIL",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite spectral-measure profile only. It audits where a certified "
            "cyclic tail majorant must act; it does not certify the infinite tail."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, refs, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
