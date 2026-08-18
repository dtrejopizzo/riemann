#!/usr/bin/env python3
"""E77.7h posteriori audit for cyclic pole capture."""

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
from E77_7h_cyclic_lanczos_probe import (  # noqa: E402
    build_complement_pair,
    lanczos_tridiagonal,
    serial,
    tridiagonal,
)
from E77_7h_feshbach_envelope_probe import GAMMA, spectral_self_energy  # noqa: E402
from E77_7h_krylov_resolution_probe import eig_coeff_rows  # noqa: E402


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def nearest_gap(values: mp.matrix, j: int) -> mp.mpf:
    gaps = []
    if j > 0:
        gaps.append(abs(values[j] - values[j - 1]))
    if j + 1 < values.rows:
        gaps.append(abs(values[j + 1] - values[j]))
    return min(gaps) if gaps else mp.inf


def lanczos_poles(K: mp.matrix, h: mp.matrix, mu_ref: mp.mpf, eta: mp.mpf, steps: int):
    alphas, betas, h_norm = lanczos_tridiagonal(K, h, steps)
    m = len(alphas)
    T = tridiagonal(alphas, betas, m)
    values, vectors = mp.eigsy(T)
    h_mass = h_norm**2
    beta_out = betas[m - 1] if len(betas) >= m else mp.mpf("0")
    rows = []
    total = mp.mpf("0")
    for j in range(values.rows):
        theta = values[j]
        weight = h_mass * abs(vectors[0, j]) ** 2
        denom = theta - mu_ref + eta
        contribution = weight / denom if denom != 0 else mp.inf
        total += contribution
        residual = abs(beta_out * vectors[m - 1, j])
        gap = nearest_gap(values, j)
        angle_proxy = residual / gap if gap > 0 else mp.inf
        lower_denom_interval = denom - residual
        rows.append(
            {
                "j": j,
                "theta": theta,
                "kappa": theta - mu_ref,
                "weight": weight,
                "denom": denom,
                "contribution": contribution,
                "residual_width": residual,
                "nearest_ritz_gap": gap,
                "angle_proxy_residual_over_gap": angle_proxy,
                "lower_denom_interval": lower_denom_interval,
            }
        )
    for row in rows:
        row["fraction"] = row["contribution"] / total if total else mp.mpf("0")
    return rows, total, beta_out


def exact_top_rows(K: mp.matrix, h: mp.matrix, mu_ref: mp.mpf, eta: mp.mpf):
    rows, sigma = eig_coeff_rows(K, h, mu_ref, eta)
    return sorted(rows, key=lambda row: row["contribution"], reverse=True), sigma


def summarize_top(ritz_rows, exact_rows, exact_sigma):
    sorted_ritz = sorted(ritz_rows, key=lambda row: row["contribution"], reverse=True)
    output = []
    cumulative = mp.mpf("0")
    certified_upper = mp.mpf("0")
    for rank, row in enumerate(sorted_ritz[:8], start=1):
        cumulative += row["contribution"]
        if row["lower_denom_interval"] > 0:
            certified_upper += row["weight"] / row["lower_denom_interval"]
            interval_upper = row["weight"] / row["lower_denom_interval"]
        else:
            interval_upper = mp.inf
            certified_upper = mp.inf
        nearest_exact = min(exact_rows, key=lambda item: abs(item["kappa"] - row["kappa"]))
        output.append(
            {
                "rank": rank,
                "ritz_j": row["j"],
                "ritz_kappa": serial(row["kappa"]),
                "ritz_weight": serial(row["weight"]),
                "ritz_fraction": serial(row["fraction"]),
                "ritz_cumulative_fraction": serial(cumulative / exact_sigma)
                if exact_sigma
                else "0",
                "residual_width": serial(row["residual_width"]),
                "nearest_ritz_gap": serial(row["nearest_ritz_gap"]),
                "angle_proxy": serial(row["angle_proxy_residual_over_gap"]),
                "lower_denom_interval": serial(row["lower_denom_interval"]),
                "interval_upper_contribution": serial(interval_upper),
                "nearest_exact_j": nearest_exact["j"],
                "nearest_exact_kappa": serial(nearest_exact["kappa"]),
                "nearest_exact_fraction": serial(nearest_exact["fraction"]),
                "kappa_error_to_exact": serial(abs(nearest_exact["kappa"] - row["kappa"])),
            }
        )
    return output, certified_upper


def analyze_reference(Hmax, idxmax, max_modes: int, ref_modes: int, steps: int):
    K, h, mu_ref, mu_full, delta = build_complement_pair(Hmax, idxmax, max_modes, ref_modes)
    exact_rows, exact_sigma = exact_top_rows(K, h, mu_ref, delta)
    ritz_rows, ritz_sigma, beta_out = lanczos_poles(K, h, mu_ref, delta, steps)
    top_rows, partial_interval_upper = summarize_top(ritz_rows, exact_rows, exact_sigma)
    sorted_ritz = sorted(ritz_rows, key=lambda row: row["contribution"], reverse=True)
    captured = {}
    for target in [mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), mp.mpf("0.999")]:
        cumulative = mp.mpf("0")
        count = 0
        max_angle = mp.mpf("0")
        min_lower = mp.inf
        for row in sorted_ritz:
            cumulative += row["contribution"]
            count += 1
            max_angle = max(max_angle, row["angle_proxy_residual_over_gap"])
            min_lower = min(min_lower, row["lower_denom_interval"])
            if exact_sigma and cumulative / exact_sigma >= target:
                break
        captured[str(target)] = {
            "count": count,
            "max_angle_proxy": serial(max_angle),
            "min_lower_denom_interval": serial(min_lower),
        }
    return {
        "reference_modes": ref_modes,
        "mu_ref": serial(mu_ref),
        "mu_full_max_section": serial(mu_full),
        "delta": serial(delta),
        "steps": steps,
        "actual_lanczos_dimension": len(ritz_rows),
        "beta_out": serial(beta_out),
        "exact_sigma_delta": serial(exact_sigma),
        "ritz_sigma_delta": serial(ritz_sigma),
        "relative_sigma_error": serial(abs(ritz_sigma - exact_sigma) / max(abs(exact_sigma), mp.mpf("1e-100"))),
        "log10_relative_sigma_error": log10_serial(abs(ritz_sigma - exact_sigma) / max(abs(exact_sigma), mp.mpf("1e-100"))),
        "captured_counts": captured,
        "top_ritz_poles": top_rows,
        "partial_interval_upper_top8": serial(partial_interval_upper),
        "partial_interval_upper_top8_over_exact": serial(partial_interval_upper / exact_sigma)
        if exact_sigma and partial_interval_upper != mp.inf
        else "inf",
    }


def run_build(label, lam, max_modes, dps, refs, steps, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for ref_modes in refs:
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes, steps)
        print(
            f"{label:6s} R={ref_modes:2d} "
            f"dim={row['actual_lanczos_dimension']:2d} "
            f"relErr={mp.nstr(mp.mpf(row['relative_sigma_error']), 6):>10s} "
            f"betaOut={mp.nstr(mp.mpf(row['beta_out']), 6):>10s} "
            f"cap90={row['captured_counts']['0.9']['count']:>2} "
            f"ang90={row['captured_counts']['0.9']['max_angle_proxy']:>12s}",
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
    parser.add_argument("--refs", default="14,16")
    parser.add_argument("--lanczos-steps", type=int, default=32)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_cyclic_pole_capture_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h cyclic pole capture audit requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) >= args.max_modes:
        parser.error("refs must be nonempty and strictly below max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h posteriori audit for cyclic pole capture",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "lanczos_steps": args.lanczos_steps,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite posteriori audit. Ritz residual intervals certify pole "
            "locations only up to the assumptions stated in the companion note; "
            "weight certification remains a separate proof obligation."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, args.dps, refs, args.lanczos_steps, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
