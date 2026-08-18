#!/usr/bin/env python3
"""E77.7h finite Feshbach self-energy audit for the Ritz bracket."""

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
        offset,
    )


def padded_ref_vector(vec: mp.matrix, full_dim: int, offset: int) -> mp.matrix:
    out = mp.matrix(full_dim, 1)
    for j in range(vec.rows):
        out[offset + j] = vec[j]
    return out


def complement_basis(ref_vectors: mp.matrix, full_dim: int, offset: int) -> mp.matrix:
    ref_dim = ref_vectors.rows
    columns = []
    for j in range(1, ref_dim):
        columns.append(padded_ref_vector(ref_vectors[:, j], full_dim, offset))
    ref_positions = set(range(offset, offset + ref_dim))
    for pos in range(full_dim):
        if pos in ref_positions:
            continue
        e = mp.matrix(full_dim, 1)
        e[pos] = 1
        columns.append(e)
    W = mp.matrix(full_dim, len(columns))
    for col, vector in enumerate(columns):
        for row in range(full_dim):
            W[row, col] = vector[row]
    return W


def spectral_self_energy(kvals: mp.matrix, coeffs: list[mp.mpf], mu_ref: mp.mpf, eta: mp.mpf):
    total = mp.mpf("0")
    rows = []
    for j, kval in enumerate(kvals):
        denom = kval - mu_ref + eta
        if denom <= 0:
            return mp.inf, []
        contribution = coeffs[j] ** 2 / denom
        total += contribution
        rows.append((j, kval, denom, coeffs[j], contribution))
    return total, rows


def fixed_point_bisect(kvals: mp.matrix, coeffs: list[mp.mpf], mu_ref: mp.mpf, lo, hi):
    def g(eta):
        sigma, _rows = spectral_self_energy(kvals, coeffs, mu_ref, eta)
        return eta - sigma

    glo = g(lo)
    ghi = g(hi)
    if glo >= 0:
        return lo
    while ghi <= 0:
        hi *= 2
        ghi = g(hi)
        if hi > mp.mpf("1e100"):
            return mp.inf
    for _ in range(220):
        mid = (lo + hi) / 2
        gm = g(mid)
        if gm >= 0:
            hi = mid
        else:
            lo = mid
    return hi


def analyze_reference(Hmax, idxmax, max_modes: int, ref_modes: int, top_k: int):
    Href, _idx_ref, offset = centered_section(Hmax, idxmax, max_modes, ref_modes)
    ref_values, ref_vectors = mp.eigsy(Href)
    mu_ref = ref_values[0]
    v_ref = ref_vectors[:, 0]
    if v_ref[ref_modes] < 0:
        for j in range(v_ref.rows):
            v_ref[j] = -v_ref[j]
    v_full = padded_ref_vector(v_ref, Hmax.rows, offset)
    W = complement_basis(ref_vectors, Hmax.rows, offset)
    orth_defect = norm(W.T * v_full)
    K = W.T * Hmax * W
    h = W.T * Hmax * v_full
    kvals, kvecs = mp.eigsy(K)
    coeffs = [abs((kvecs[:, j].T * h)[0]) for j in range(kvals.rows)]
    full_values, _full_vectors = mp.eigsy(Hmax)
    mu_full = full_values[0]
    delta_full = mu_ref - mu_full
    sigma_at_full, sigma_rows = spectral_self_energy(kvals, coeffs, mu_ref, delta_full)
    fixed_eta = fixed_point_bisect(kvals, coeffs, mu_ref, mp.mpf("0"), max(delta_full, mp.mpf("1e-80")))
    min_gap = kvals[0] - mu_ref
    crude_eta = mp.inf
    h_norm = norm(h)
    if min_gap > 0:
        crude_eta = (mp.sqrt(min_gap**2 + 4 * h_norm**2) - min_gap) / 2

    top_contrib = sorted(sigma_rows, key=lambda item: item[4], reverse=True)[:top_k]
    low_kappa_rows = []
    for j in range(min(top_k, len(coeffs))):
        low_kappa_rows.append(
            {
                "j": j,
                "kappa_to_mu_ref": serial(kvals[j] - mu_ref),
                "coeff_abs": serial(coeffs[j]),
                "contribution_at_full_delta": serial(sigma_rows[j][4])
                if sigma_rows
                else "NA",
            }
        )
    return {
        "reference_modes": ref_modes,
        "reference_dim": Href.rows,
        "mu_ref": serial(mu_ref),
        "mu_full_max_section": serial(mu_full),
        "finite_delta_mu_ref_minus_mu_full": serial(delta_full),
        "finite_delta_log10": log10_serial(delta_full),
        "complement_min_kappa_to_mu_ref": serial(min_gap),
        "h_norm": serial(h_norm),
        "h_norm_log10": log10_serial(h_norm),
        "orthogonality_defect": serial(orth_defect),
        "crude_gap_eta": serial(crude_eta),
        "crude_gap_eta_log10": log10_serial(crude_eta),
        "weighted_fixed_point_eta": serial(fixed_eta),
        "weighted_fixed_point_log10": log10_serial(fixed_eta),
        "self_energy_at_full_delta": serial(sigma_at_full),
        "feshbach_identity_relative_defect": serial(
            abs(sigma_at_full - delta_full) / max(mp.mpf("1"), abs(sigma_at_full), abs(delta_full))
        ),
        "effective_denominator_hnorm2_over_delta": serial(h_norm**2 / delta_full)
        if delta_full > 0
        else "inf",
        "low_kappa_rows": low_kappa_rows,
        "top_self_energy_contributors": [
            {
                "j": item[0],
                "kappa_to_mu_ref": serial(item[1] - mu_ref),
                "denominator_at_full_delta": serial(item[2]),
                "coeff_abs": serial(item[3]),
                "contribution_at_full_delta": serial(item[4]),
                "fraction": serial(item[4] / sigma_at_full) if sigma_at_full else "0",
            }
            for item in top_contrib
        ],
    }


def run_build(label, lam, max_modes, dps, refs, top_k, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for ref_modes in refs:
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes, top_k)
        print(
            f"{label:6s} R={ref_modes:2d} "
            f"delta={serial(mp.mpf(row['finite_delta_mu_ref_minus_mu_full']), 8):>12s} "
            f"etaW={serial(mp.mpf(row['weighted_fixed_point_eta']), 8):>12s} "
            f"etaCrude={serial(mp.mpf(row['crude_gap_eta']), 8):>12s} "
            f"kmin={serial(mp.mpf(row['complement_min_kappa_to_mu_ref']), 8):>12s} "
            f"def={row['feshbach_identity_relative_defect']:>12s}",
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
    parser.add_argument("--top-k", type=int, default=6)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_feshbach_envelope_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h Feshbach audit requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) >= args.max_modes:
        parser.error("refs must be nonempty and strictly below max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h finite Feshbach self-energy envelope audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "top_k": args.top_k,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "This is a finite max-section identity probe. It identifies the exact "
            "weighted self-energy object needed for an infinite Ritz bracket, but "
            "does not certify the infinite envelope."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(
            run_build(label, args.lam, args.max_modes, args.dps, refs, args.top_k, planted)
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
