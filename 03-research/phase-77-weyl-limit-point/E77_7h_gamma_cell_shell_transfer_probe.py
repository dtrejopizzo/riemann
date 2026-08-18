#!/usr/bin/env python3
"""E77.7h Gamma/cell shell-transfer decomposition probe."""

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

from P76_002_mp_entry_audit import build_mp, primes_upto  # noqa: E402
from E77_7h_feshbach_envelope_probe import GAMMA, norm, serial  # noqa: E402
from E77_7h_geometric_shell_residual_probe import embedding_indices, parse_coord, subvector  # noqa: E402
from E77_7h_shell_stieltjes_increment_probe import (  # noqa: E402
    parse_pairs,
    section_from_big,
    solve_matrix,
    stieltjes,
)


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def package_functional(f, f0, fp0, L, lam, include_arith=True, planted=None):
    w02 = mp.quad(lambda y: f(y) * (mp.exp(y / 2) + mp.exp(-y / 2)), [0, L])

    def wr_integrand(y):
        if y == 0:
            return (fp0 + f0 / 2) / 2
        return (mp.exp(y / 2) * f(y) - f0) / (2 * mp.sinh(y))

    wr = (
        (mp.log(4 * mp.pi) + mp.euler) * f0 / 2
        + mp.quad(wr_integrand, [0, L])
        + f0 * mp.log(mp.tanh(L / 2)) / 2
    )
    arith = mp.mpf(0)
    if include_arith:
        maxn = int(lam * lam)
        for p in primes_upto(maxn):
            lp = mp.log(p)
            pm = p
            exponent = 1
            while pm <= maxn:
                arith += lp * mp.power(pm, mp.mpf("-0.5")) * f(exponent * lp)
                pm *= p
                exponent += 1
    value = w02 - wr - arith
    if planted is not None:
        gamma0, beta, strength = (mp.mpf(x) for x in planted)
        spectral_point = gamma0 - 1j * beta
        qhat = mp.quad(lambda y: f(y) * mp.cos(spectral_point * y), [0, L])
        value += strength * 2 * mp.re(qhat)
    return value


def package_s_symbol(t, L, lam, include_arith=True, planted=None):
    return package_functional(
        lambda y: mp.sin(t * y),
        mp.mpf(0),
        t,
        L,
        lam,
        include_arith=include_arith,
        planted=planted,
    )


def complement_extended(H: mp.matrix, idx: list[int], ref_modes: int):
    ref_positions = [j for j, n in enumerate(idx) if abs(n) <= ref_modes]
    Href = mp.matrix(len(ref_positions))
    for a, pa in enumerate(ref_positions):
        for b, pb in enumerate(ref_positions):
            Href[a, b] = H[pa, pb]
    vals, vecs = mp.eigsy(Href)
    mu = vals[0]
    v = vecs[:, 0]
    center_in_ref = ref_modes
    if v[center_in_ref] < 0:
        for j in range(v.rows):
            v[j] = -v[j]
    columns = []
    labels = []
    for j in range(1, vecs.cols):
        full = mp.matrix(H.rows, 1)
        for a, pa in enumerate(ref_positions):
            full[pa] = vecs[a, j]
        columns.append(full)
        labels.append(("ref", j))
    for pos, n in enumerate(idx):
        if abs(n) <= ref_modes:
            continue
        full = mp.matrix(H.rows, 1)
        full[pos] = 1
        columns.append(full)
        labels.append(("coord", n))
    W = mp.matrix(H.rows, len(columns))
    for col, vector in enumerate(columns):
        for row in range(H.rows):
            W[row, col] = vector[row]
    v_full = mp.matrix(H.rows, 1)
    for a, pa in enumerate(ref_positions):
        v_full[pa] = v[a]
    K = W.T * H * W
    h = W.T * H * v_full
    full_vals, _ = mp.eigsy(H)
    return {
        "K": K,
        "h": h,
        "mu": mu,
        "delta": mu - full_vals[0],
        "labels": labels,
        "W": W,
        "v_full": v_full,
        "full_mu": full_vals[0],
    }


def submatrix(A: mp.matrix, rows: list[int], cols: list[int]):
    out = mp.matrix(len(rows), len(cols))
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            out[i, j] = A[r, c]
    return out


def reconstruct_old_vector(new, old_in_new, x_old):
    u = -new["v_full"].copy()
    for col, coeff in zip(old_in_new, x_old):
        for row in range(u.rows):
            u[row] += new["W"][row, col] * coeff
    return u


def shell_loewner_row(idx_new, old_positions, shell_pos, u, s_values, L):
    n_shell = idx_new[shell_pos]
    d_shell = 2 * mp.pi * n_shell / L
    s_shell = s_values[shell_pos]
    cauchy_u = mp.mpf(0)
    cauchy_su = mp.mpf(0)
    for pos in old_positions:
        n = idx_new[pos]
        d = 2 * mp.pi * n / L
        coeff = u[pos] / (d_shell - d)
        cauchy_u += coeff
        cauchy_su += s_values[pos] * coeff
    term_a = s_shell * cauchy_u
    term_b = cauchy_su
    predicted = -(2 / L) * (term_a - term_b)
    return term_a, term_b, predicted


def analyze_pair(Hbig, idxbig, lam, ref_modes, old_modes, new_modes, include_arith, planted):
    Hnew, idx_new = section_from_big(Hbig, idxbig, new_modes)
    old_positions = [j for j, n in enumerate(idx_new) if abs(n) <= old_modes]
    old_labels_section = [n for n in idx_new if abs(n) <= old_modes]
    Hold = mp.matrix(len(old_positions))
    for a, pa in enumerate(old_positions):
        for b, pb in enumerate(old_positions):
            Hold[a, b] = Hnew[pa, pb]
    old = complement_extended(Hold, old_labels_section, ref_modes)
    new = complement_extended(Hnew, idx_new, ref_modes)
    old_in_new, shell_in_new = embedding_indices(old["labels"], new["labels"])

    Koo = submatrix(new["K"], old_in_new, old_in_new)
    Kos = submatrix(new["K"], old_in_new, shell_in_new)
    ho = subvector(new["h"], old_in_new)
    hs = subvector(new["h"], shell_in_new)
    eta = new["delta"]
    _sigma_old, x_old = stieltjes(Koo, ho, new["mu"], eta)
    u = reconstruct_old_vector(new, old_in_new, x_old)
    mediated = Kos.T * x_old
    residual = hs - mediated

    s_values = [
        package_s_symbol(2 * mp.pi * n / new["L"], new["L"], lam, include_arith, planted)
        for n in idx_new
    ] if "L" in new else None
    return old, new, shell_in_new, old_positions, u, residual, s_values


def analyze_pair_with_L(Hbig, idxbig, L, lam, ref_modes, old_modes, new_modes, include_arith, planted):
    Hnew, idx_new = section_from_big(Hbig, idxbig, new_modes)
    old_positions = [j for j, n in enumerate(idx_new) if abs(n) <= old_modes]
    old_labels_section = [n for n in idx_new if abs(n) <= old_modes]
    Hold = mp.matrix(len(old_positions))
    for a, pa in enumerate(old_positions):
        for b, pb in enumerate(old_positions):
            Hold[a, b] = Hnew[pa, pb]
    old = complement_extended(Hold, old_labels_section, ref_modes)
    new = complement_extended(Hnew, idx_new, ref_modes)
    old_in_new, shell_in_new = embedding_indices(old["labels"], new["labels"])

    Koo = submatrix(new["K"], old_in_new, old_in_new)
    Kos = submatrix(new["K"], old_in_new, shell_in_new)
    ho = subvector(new["h"], old_in_new)
    hs = subvector(new["h"], shell_in_new)
    eta = new["delta"]
    _sigma_old, x_old = stieltjes(Koo, ho, new["mu"], eta)
    u = reconstruct_old_vector(new, old_in_new, x_old)
    mediated = Kos.T * x_old
    residual = hs - mediated
    s_values = [package_s_symbol(2 * mp.pi * n / L, L, lam, include_arith, planted) for n in idx_new]

    rows = []
    actual = mp.matrix(len(shell_in_new), 1)
    predicted = mp.matrix(len(shell_in_new), 1)
    coord_to_position = {n: pos for pos, n in enumerate(idx_new)}
    for row, col in enumerate(shell_in_new):
        label = new["labels"][col]
        coord = parse_coord(label)
        if coord is None:
            raise ValueError(f"shell column is not a coordinate label: {label}")
        pos = coord_to_position[coord]
        term_a, term_b, pred = shell_loewner_row(idx_new, old_positions, pos, u, s_values, L)
        actual[row] = (Hnew[pos, :] * u)[0]
        predicted[row] = pred
        res = residual[row]
        denom = max(abs(term_a), abs(term_b), mp.mpf("1e-100"))
        rows.append(
            {
                "label": str(label),
                "coord": coord,
                "actual_shell_Hu": serial(actual[row]),
                "negative_residual": serial(-res),
                "loewner_predicted": serial(pred),
                "term_Sa_A": serial(term_a),
                "term_B": serial(term_b),
                "loewner_cancel_ratio": serial(abs(term_a - term_b) / denom),
                "residual_over_term_scale": serial(abs(res) / denom),
            }
        )
    identity_defect = norm(actual - predicted) / max(mp.mpf(1), norm(actual), norm(predicted))
    residual_identity_defect = norm(actual + residual) / max(mp.mpf(1), norm(actual), norm(residual))
    cancel = norm(actual) / max(
        norm(mp.matrix([mp.mpf(row["term_Sa_A"]) for row in rows])),
        norm(mp.matrix([mp.mpf(row["term_B"]) for row in rows])),
        mp.mpf("1e-100"),
    )
    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "ref_modes": ref_modes,
        "identity_defect_log10": log10_serial(identity_defect),
        "residual_identity_defect_log10": log10_serial(residual_identity_defect),
        "shell_norm_log10": log10_serial(norm(actual)),
        "term_cancel_ratio_log10": log10_serial(cancel),
        "components": rows,
    }


def run_case(case, lam, max_modes, ref_modes, pairs, dps):
    Hbig, idxbig, L = build_mp(
        lam,
        max_modes,
        dps,
        include_arith=case["include_arith"],
        planted=case["planted"],
    )
    rows = []
    for old, new in pairs:
        row = analyze_pair_with_L(
            Hbig,
            idxbig,
            L,
            mp.mpf(lam),
            ref_modes,
            old,
            new,
            case["include_arith"],
            case["planted"],
        )
        rows.append(row)
        print(
            f"{case['label']:10s} R={ref_modes:2d} {old:2d}->{new:2d} "
            f"id={row['identity_defect_log10']:>10s} "
            f"residId={row['residual_identity_defect_log10']:>10s} "
            f"shell={row['shell_norm_log10']:>10s} "
            f"termCancel={row['term_cancel_ratio_log10']:>10s}",
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
    parser.add_argument("--pairs", default="16:18,18:20")
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_gamma_cell_shell_transfer_results.json",
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7h Gamma/cell shell-transfer probe requires dps >= 50")
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
        "statement": "E77.7h Gamma/cell Loewner shell-transfer decomposition",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite exact Loewner decomposition probe. It localizes the algebraic "
            "cancellation but does not prove the cofinal transfer estimate."
        ),
        "cases": [run_case(case, args.lam, args.max_modes, args.ref_modes, pairs, args.dps) for case in cases],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
