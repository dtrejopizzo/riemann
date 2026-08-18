#!/usr/bin/env python3
"""E77.7h Krylov window-resolution audit."""

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


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def chebyshev_steps(condition: mp.mpf, tol: mp.mpf):
    if condition <= 1:
        return 1
    root = mp.sqrt(condition)
    q = (root - 1) / (root + 1)
    if q <= 0:
        return 1
    if q >= 1:
        return "inf"
    steps = mp.ceil(mp.log(tol / 2) / mp.log(q))
    return int(max(1, steps))


def eig_coeff_rows(K: mp.matrix, h: mp.matrix, mu_ref: mp.mpf, eta: mp.mpf):
    kvals, kvecs = mp.eigsy(K)
    coeffs = [abs((kvecs[:, j].T * h)[0]) for j in range(kvals.rows)]
    sigma, raw_rows = spectral_self_energy(kvals, coeffs, mu_ref, eta)
    rows = []
    for j, omega, denom, coeff, contrib in raw_rows:
        rows.append(
            {
                "j": j,
                "omega": omega,
                "kappa": omega - mu_ref,
                "denom": denom,
                "coeff": coeff,
                "contribution": contrib,
                "fraction": contrib / sigma if sigma else mp.mpf("0"),
            }
        )
    return rows, sigma


def lanczos_ritz_rows(K: mp.matrix, h: mp.matrix, mu_ref: mp.mpf, steps: int):
    alphas, betas, h_norm = lanczos_tridiagonal(K, h, steps)
    T = tridiagonal(alphas, betas, len(alphas))
    values, vectors = mp.eigsy(T)
    rows = []
    h_mass = h_norm**2
    for j in range(values.rows):
        weight = h_mass * abs(vectors[0, j]) ** 2
        rows.append({"j": j, "kappa": values[j] - mu_ref, "weight": weight})
    return rows


def summarize_capture(exact_rows, ritz_rows):
    top_exact = sorted(exact_rows, key=lambda row: row["contribution"], reverse=True)[:6]
    output = []
    for row in top_exact:
        nearest = min(ritz_rows, key=lambda item: abs(item["kappa"] - row["kappa"]))
        output.append(
            {
                "exact_j": row["j"],
                "exact_kappa": serial(row["kappa"]),
                "exact_fraction": serial(row["fraction"]),
                "nearest_ritz_j": nearest["j"],
                "nearest_ritz_kappa": serial(nearest["kappa"]),
                "kappa_error": serial(abs(nearest["kappa"] - row["kappa"])),
                "relative_kappa_error": serial(
                    abs(nearest["kappa"] - row["kappa"]) / max(abs(row["kappa"]), mp.mpf("1e-100"))
                ),
                "nearest_ritz_weight": serial(nearest["weight"]),
            }
        )
    return output


def analyze_reference(Hmax, idxmax, max_modes: int, ref_modes: int, lanczos_steps: int):
    K, h, mu_ref, mu_full, delta = build_complement_pair(Hmax, idxmax, max_modes, ref_modes)
    exact_rows, sigma = eig_coeff_rows(K, h, mu_ref, delta)
    denoms = [row["denom"] for row in exact_rows]
    a = min(denoms)
    b = max(denoms)
    condition = b / a if a > 0 else mp.inf
    ritz_rows = lanczos_ritz_rows(K, h, mu_ref, lanczos_steps)
    capture = summarize_capture(exact_rows, ritz_rows)
    top_sorted = sorted(exact_rows, key=lambda row: row["contribution"], reverse=True)
    cumulative = mp.mpf("0")
    support_counts = {}
    for target in [mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), mp.mpf("0.999")]:
        cumulative = mp.mpf("0")
        max_denom = mp.mpf("0")
        min_denom = mp.inf
        count = 0
        for row in top_sorted:
            cumulative += row["fraction"]
            max_denom = max(max_denom, row["denom"])
            min_denom = min(min_denom, row["denom"])
            count += 1
            if cumulative >= target:
                break
        support_counts[str(target)] = {
            "count": count,
            "min_denom": serial(min_denom),
            "max_denom": serial(max_denom),
            "window_condition": serial(max_denom / min_denom) if min_denom > 0 else "inf",
        }
    return {
        "reference_modes": ref_modes,
        "mu_ref": serial(mu_ref),
        "mu_full_max_section": serial(mu_full),
        "delta": serial(delta),
        "sigma_delta": serial(sigma),
        "shifted_min_denom_a": serial(a),
        "shifted_max_denom_b": serial(b),
        "ambient_condition_b_over_a": serial(condition),
        "ambient_condition_log10": log10_serial(condition),
        "chebyshev_steps_1e_minus_2": chebyshev_steps(condition, mp.mpf("1e-2")),
        "chebyshev_steps_1e_minus_8": chebyshev_steps(condition, mp.mpf("1e-8")),
        "top_support_counts": support_counts,
        "lanczos_steps": lanczos_steps,
        "top_pole_capture": capture,
    }


def run_build(label, lam, max_modes, dps, refs, lanczos_steps, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for ref_modes in refs:
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes, lanczos_steps)
        print(
            f"{label:6s} R={ref_modes:2d} "
            f"logCond={row['ambient_condition_log10']:>10s} "
            f"cheb1e-2={str(row['chebyshev_steps_1e_minus_2']):>8s} "
            f"cheb1e-8={str(row['chebyshev_steps_1e_minus_8']):>8s} "
            f"top90={row['top_support_counts']['0.9']['count']:>2}",
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
        default=HERE / "E77_7h_krylov_resolution_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h Krylov resolution audit requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) >= args.max_modes:
        parser.error("refs must be nonempty and strictly below max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h Krylov window-resolution audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "lanczos_steps": args.lanczos_steps,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite audit. Chebyshev counts are generic interval estimates; they "
            "are not proof of impossibility for cyclic pole-capture routes."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, refs, args.lanczos_steps, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
