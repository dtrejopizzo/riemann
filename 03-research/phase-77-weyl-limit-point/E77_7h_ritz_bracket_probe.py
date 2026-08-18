#!/usr/bin/env python3
"""E77.7h finite audits for Ritz bracketing and bracketed low-mode BTG."""

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


def matrix_norm_symmetric(A: mp.matrix) -> mp.mpf:
    if A.rows == 0 or A.cols == 0:
        return mp.mpf("0")
    vals, _ = mp.eigsy(A)
    return max(abs(vals[0]), abs(vals[vals.rows - 1]))


def rectangular_norm(C: mp.matrix) -> mp.mpf:
    if C.rows == 0 or C.cols == 0:
        return mp.mpf("0")
    gram = C.T * C if C.rows >= C.cols else C * C.T
    vals, _ = mp.eigsy(gram)
    return mp.sqrt(max(mp.mpf("0"), vals[vals.rows - 1]))


def spectral_low_mode(inner: mp.matrix, source: mp.matrix, mu_ref: mp.mpf, top_k: int):
    values, vectors = mp.eigsy(inner)
    total = mp.mpf("0")
    first = []
    for j in range(values.rows):
        vec = vectors[:, j]
        coeff = abs((vec.T * source)[0])
        gap = abs(values[j] - mu_ref)
        contribution = coeff**2 / gap**2
        total += contribution
        if j < top_k:
            first.append((j, values[j], coeff, gap, contribution))
    return values, vectors, total, first


def finite_gershgorin_lower(A: mp.matrix) -> mp.mpf:
    if A.rows == 0:
        return mp.inf
    lows = []
    for i in range(A.rows):
        radius = mp.fsum(abs(A[i, j]) for j in range(A.cols) if j != i)
        lows.append(A[i, i] - radius)
    return min(lows)


def analyze_reference(Hmax, idxmax, max_modes: int, ref_modes: int, top_k: int):
    Href, idx_ref = centered_section(Hmax, idxmax, max_modes, ref_modes)
    ref_values, ref_vectors = mp.eigsy(Href)
    mu_ref = ref_values[0]
    v_ref = ref_vectors[:, 0]
    if v_ref[ref_modes] < 0:
        v_ref = -v_ref

    diag = mp.diag([Hmax[i, i] for i in range(Hmax.rows)])
    Bmax = Hmax - diag
    finite_B_norm = matrix_norm_symmetric(Bmax)

    ref_pos = [i for i, n in enumerate(idxmax) if abs(n) <= ref_modes]
    tail_pos = [i for i, n in enumerate(idxmax) if abs(n) > ref_modes]
    tail_diag_min = min([Hmax[i, i] for i in tail_pos], default=mp.inf)
    tail_block = mp.matrix([[Hmax[i, j] for j in tail_pos] for i in tail_pos])
    finite_tail_gersh_lower = finite_gershgorin_lower(tail_block)
    finite_tail_values = None
    finite_tail_min = mp.inf
    if tail_block.rows:
        finite_tail_values, _ = mp.eigsy(tail_block)
        finite_tail_min = finite_tail_values[0]

    cross = mp.matrix([[Hmax[i, j] for j in tail_pos] for i in ref_pos])
    finite_cross_norm = rectangular_norm(cross)
    residual_tail = cross.T * v_ref if tail_pos else mp.matrix(0, 1)
    residual_norm = norm(residual_tail) if tail_pos else mp.mpf("0")

    coarse_tail_lower = tail_diag_min - finite_B_norm
    coarse_gap = coarse_tail_lower - mu_ref
    coarse_eps = mp.inf if coarse_gap <= 0 else finite_cross_norm**2 / coarse_gap

    directional_tail_gap = finite_tail_min - mu_ref
    directional_eps = mp.inf if directional_tail_gap <= 0 else residual_norm**2 / directional_tail_gap

    core_gap = ref_values[1] - ref_values[0] if ref_values.rows > 1 else mp.inf
    temple_denominator_proxy = min(core_gap, directional_tail_gap)
    temple_eps_proxy = (
        mp.inf
        if temple_denominator_proxy <= 0
        else residual_norm**2 / temple_denominator_proxy
    )

    inner = Href[1:-1, 1:-1]
    source = mp.matrix([Href[j + 1, Href.cols - 1] for j in range(Href.rows - 2)])
    inner_values, _inner_vectors, S_ref, first = spectral_low_mode(
        inner, source, mu_ref, top_k
    )
    low_modes = []
    bracket_lowmode_sum = mp.mpf("0")
    for j, nu, coeff, gap, contribution in first:
        denom = gap + coarse_eps if coarse_eps != mp.inf else mp.inf
        bracket_contribution = mp.mpf("0") if denom == mp.inf else coeff**2 / denom**2
        bracket_lowmode_sum += bracket_contribution
        low_modes.append(
            {
                "j": j,
                "nu_j": serial(nu),
                "gap_to_mu_ref": serial(gap),
                "coeff_abs": serial(coeff),
                "reference_contribution": serial(contribution),
                "reference_fraction": serial(contribution / S_ref) if S_ref else "0",
                "coarse_bracket_contribution": serial(bracket_contribution),
            }
        )

    return {
        "reference_modes": ref_modes,
        "reference_dim": Href.rows,
        "mu_ref_upper_bound_surrogate": serial(mu_ref),
        "finite_second_ritz_gap": serial(core_gap),
        "finite_B_norm_estimate": serial(finite_B_norm),
        "tail_diag_min_inside_max_section": serial(tail_diag_min),
        "tail_lower_by_diag_minus_B_estimate": serial(coarse_tail_lower),
        "finite_tail_gershgorin_lower": serial(finite_tail_gersh_lower),
        "finite_tail_lambda_min": serial(finite_tail_min),
        "finite_cross_norm": serial(finite_cross_norm),
        "ritz_tail_residual_norm": serial(residual_norm),
        "coarse_tail_gap_to_mu_ref": serial(coarse_gap),
        "coarse_global_bracket_epsilon": serial(coarse_eps),
        "directional_tail_gap_proxy": serial(directional_tail_gap),
        "directional_residual_epsilon_proxy": serial(directional_eps),
        "temple_denominator_proxy": serial(temple_denominator_proxy),
        "temple_epsilon_proxy": serial(temple_eps_proxy),
        "btg_reference_S": serial(S_ref),
        "btg_reference_log10_S": log10_serial(S_ref),
        "coarse_bracket_lowmode_sum_top_k": serial(bracket_lowmode_sum),
        "coarse_bracket_lowmode_log10_top_k": log10_serial(bracket_lowmode_sum),
        "low_modes": low_modes,
    }


def run_build(label, lam, max_modes, dps, refs, top_k, planted):
    Hmax, idxmax, L = build_mp(lam, max_modes, dps, planted=planted)
    max_values, _max_vectors = mp.eigsy(Hmax)
    rows = []
    for ref_modes in refs:
        if ref_modes >= max_modes:
            continue
        row = analyze_reference(Hmax, idxmax, max_modes, ref_modes, top_k)
        finite_delta_to_max = mp.mpf(row["mu_ref_upper_bound_surrogate"]) - max_values[0]
        row["finite_delta_to_max_section"] = serial(finite_delta_to_max)
        row["finite_delta_to_max_log10"] = log10_serial(abs(finite_delta_to_max))
        print(
            f"{label:6s} R={ref_modes:2d} "
            f"muR={serial(mp.mpf(row['mu_ref_upper_bound_surrogate']), 10):>14s} "
            f"dMax={serial(finite_delta_to_max, 8):>12s} "
            f"epsCoarse={serial(mp.mpf(row['coarse_global_bracket_epsilon']), 8):>12s} "
            f"epsDir={serial(mp.mpf(row['directional_residual_epsilon_proxy']), 8):>12s} "
            f"logSref={row['btg_reference_log10_S']:>10s}",
            flush=True,
        )
        rows.append(row)
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
        "references": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--refs", default="8,10,12,14,16")
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_ritz_bracket_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h requires dps >= 60")
    refs = [int(value) for value in args.refs.split(",") if value]
    if not refs or max(refs) >= args.max_modes:
        parser.error("refs must be nonempty and strictly below max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h Ritz-bracket and bracketed low-mode BTG audit",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "refs": refs,
            "top_k": args.top_k,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite norms, finite tail eigenvalues, and finite B norms are diagnostics. "
            "Only the written tail-bracket theorem states what would require certified "
            "infinite D+B constants. The probe audits scale compatibility."
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
