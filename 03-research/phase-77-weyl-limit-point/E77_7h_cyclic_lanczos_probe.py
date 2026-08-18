#!/usr/bin/env python3
"""E77.7h cyclic Lanczos/Stieltjes probe for mass certification."""

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
    norm,
    padded_ref_vector,
    serial,
    spectral_self_energy,
)


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def build_complement_pair(Hmax: mp.matrix, idxmax: list[int], max_modes: int, ref_modes: int):
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
    full_values, _ = mp.eigsy(Hmax)
    mu_full = full_values[0]
    delta = mu_ref - mu_full
    return K, h, mu_ref, mu_full, delta


def stieltjes_from_matrix(A: mp.matrix, h_mass: mp.mpf, mu_ref: mp.mpf, eta: mp.mpf):
    if A.rows == 0 or h_mass == 0:
        return mp.mpf("0")
    shift = A - (mu_ref - eta) * mp.eye(A.rows)
    e0 = mp.matrix(A.rows, 1)
    e0[0] = 1
    try:
        y = mp.lu_solve(shift, e0)
    except ZeroDivisionError:
        return mp.inf
    return h_mass * y[0]


def exact_self_energy(K: mp.matrix, h: mp.matrix, mu_ref: mp.mpf, eta: mp.mpf):
    kvals, kvecs = mp.eigsy(K)
    coeffs = [abs((kvecs[:, j].T * h)[0]) for j in range(kvals.rows)]
    sigma, _rows = spectral_self_energy(kvals, coeffs, mu_ref, eta)
    return sigma


def lanczos_tridiagonal(K: mp.matrix, h: mp.matrix, max_steps: int):
    h_norm = norm(h)
    if h_norm == 0:
        return [], [], mp.mpf("0")
    n = K.rows
    q_prev = mp.matrix(n, 1)
    q = h / h_norm
    basis = []
    alphas = []
    betas = []
    beta_prev = mp.mpf("0")
    for _ in range(min(max_steps, n)):
        basis.append(q.copy())
        z = K * q
        alpha = (q.T * z)[0]
        z = z - alpha * q - beta_prev * q_prev
        # Full reorthogonalization keeps the tiny zeta couplings honest.
        for old_q in basis:
            z = z - (old_q.T * z)[0] * old_q
        beta = norm(z)
        alphas.append(alpha)
        if beta <= mp.mpf("1e-" + str(max(20, mp.mp.dps // 2))):
            break
        betas.append(beta)
        q_prev = q
        q = z / beta
        beta_prev = beta
    return alphas, betas, h_norm


def tridiagonal(alphas: list[mp.mpf], betas: list[mp.mpf], steps: int):
    T = mp.matrix(steps)
    for i in range(steps):
        T[i, i] = alphas[i]
        if i + 1 < steps:
            T[i, i + 1] = betas[i]
            T[i + 1, i] = betas[i]
    return T


def fixed_point_from_tridiagonal(T: mp.matrix, h_mass: mp.mpf, mu_ref: mp.mpf, seed: mp.mpf):
    lo = mp.mpf("0")
    hi = max(seed, mp.mpf("1e-80"))

    def g(eta):
        return eta - stieltjes_from_matrix(T, h_mass, mu_ref, eta)

    try:
        glo = g(lo)
        ghi = g(hi)
    except ZeroDivisionError:
        return mp.inf
    if glo >= 0:
        return lo
    for _ in range(120):
        if ghi > 0:
            break
        hi *= 2
        ghi = g(hi)
    if ghi <= 0:
        return mp.inf
    for _ in range(180):
        mid = (lo + hi) / 2
        if g(mid) >= 0:
            hi = mid
        else:
            lo = mid
    return hi


def analyze_reference(Hmax, idxmax, max_modes: int, ref_modes: int, lanczos_steps: int):
    K, h, mu_ref, mu_full, delta = build_complement_pair(Hmax, idxmax, max_modes, ref_modes)
    alphas, betas, h_norm = lanczos_tridiagonal(K, h, lanczos_steps)
    h_mass = h_norm**2
    exact_delta = exact_self_energy(K, h, mu_ref, delta)
    exact_2delta = exact_self_energy(K, h, mu_ref, 2 * delta)
    exact_4delta = exact_self_energy(K, h, mu_ref, 4 * delta)
    step_rows = []
    for steps in range(1, len(alphas) + 1):
        T = tridiagonal(alphas, betas, steps)
        approx_delta = stieltjes_from_matrix(T, h_mass, mu_ref, delta)
        approx_2delta = stieltjes_from_matrix(T, h_mass, mu_ref, 2 * delta)
        approx_4delta = stieltjes_from_matrix(T, h_mass, mu_ref, 4 * delta)
        fp = fixed_point_from_tridiagonal(T, h_mass, mu_ref, max(delta, mp.mpf("1e-80")))
        rel_delta = abs(approx_delta - exact_delta) / max(abs(exact_delta), mp.mpf("1e-100"))
        rel_2delta = abs(approx_2delta - exact_2delta) / max(abs(exact_2delta), mp.mpf("1e-100"))
        rel_4delta = abs(approx_4delta - exact_4delta) / max(abs(exact_4delta), mp.mpf("1e-100"))
        step_rows.append(
            {
                "steps": steps,
                "approx_sigma_delta": serial(approx_delta),
                "rel_error_delta": serial(rel_delta),
                "log10_rel_error_delta": log10_serial(rel_delta),
                "approx_sigma_2delta": serial(approx_2delta),
                "rel_error_2delta": serial(rel_2delta),
                "log10_rel_error_2delta": log10_serial(rel_2delta),
                "approx_sigma_4delta": serial(approx_4delta),
                "rel_error_4delta": serial(rel_4delta),
                "log10_rel_error_4delta": log10_serial(rel_4delta),
                "fixed_point_eta": serial(fp),
                "fixed_point_ratio_to_delta": serial(fp / delta) if delta > 0 else "inf",
            }
        )
    thresholds = {}
    for label, tol in [
        ("1e-2", mp.mpf("1e-2")),
        ("1e-4", mp.mpf("1e-4")),
        ("1e-8", mp.mpf("1e-8")),
        ("1e-12", mp.mpf("1e-12")),
    ]:
        hit = "NA"
        for row in step_rows:
            if mp.mpf(row["rel_error_delta"]) <= tol:
                hit = row["steps"]
                break
        thresholds[label] = hit
    return {
        "reference_modes": ref_modes,
        "mu_ref": serial(mu_ref),
        "mu_full_max_section": serial(mu_full),
        "delta": serial(delta),
        "h_mass": serial(h_mass),
        "lanczos_dimension": len(alphas),
        "exact_sigma_delta": serial(exact_delta),
        "exact_sigma_2delta": serial(exact_2delta),
        "exact_sigma_4delta": serial(exact_4delta),
        "threshold_steps_delta": thresholds,
        "alpha_first": serial(alphas[0]) if alphas else "NA",
        "beta_first": serial(betas[0]) if betas else "NA",
        "step_rows": step_rows,
    }


def run_build(label, lam, max_modes, dps, refs, lanczos_steps, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for ref_modes in refs:
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes, lanczos_steps)
        last = row["step_rows"][-1]
        print(
            f"{label:6s} R={ref_modes:2d} "
            f"dimL={row['lanczos_dimension']:2d} "
            f"hit1e-8={str(row['threshold_steps_delta']['1e-8']):>3s} "
            f"lastErr={mp.nstr(mp.mpf(last['rel_error_delta']), 6):>10s} "
            f"fp/d={mp.nstr(mp.mpf(last['fixed_point_ratio_to_delta']), 8):>10s}",
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
    parser.add_argument("--lanczos-steps", type=int, default=14)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_cyclic_lanczos_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h cyclic Lanczos audit requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) >= args.max_modes:
        parser.error("refs must be nonempty and strictly below max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h cyclic Lanczos/Stieltjes probe for mass certification",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "lanczos_steps": args.lanczos_steps,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite cyclic Lanczos probe only. It tests whether Stieltjes/moment "
            "data can replace spectral-window diagonalization."
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
