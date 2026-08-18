#!/usr/bin/env python3
"""E77.7h mesh numerator profile for the S-weighted Cauchy match."""

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
from E77_7h_barycentric_symbol_match_probe import cauchy_sums  # noqa: E402
from E77_7h_feshbach_envelope_probe import GAMMA, norm, serial  # noqa: E402
from E77_7h_gamma_cell_shell_transfer_probe import (  # noqa: E402
    complement_extended,
    package_functional,
    package_s_symbol,
    reconstruct_old_vector,
    submatrix,
)
from E77_7h_geometric_shell_residual_probe import embedding_indices, subvector  # noqa: E402
from E77_7h_shell_stieltjes_increment_probe import parse_pairs, section_from_big, stieltjes  # noqa: E402


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def package_c_symbol(t, L, lam, include_arith=True, planted=None):
    return package_functional(
        lambda y: mp.cos(t * y),
        mp.mpf(1),
        mp.mpf(0),
        L,
        lam,
        include_arith=include_arith,
        planted=planted,
    )


def reconstruct_case_with_lambda(Hbig, idxbig, ref_modes, old_modes, new_modes):
    Hnew, idx_new = section_from_big(Hbig, idxbig, new_modes)
    old_positions = [j for j, n in enumerate(idx_new) if abs(n) <= old_modes]
    old_labels_section = [n for n in idx_new if abs(n) <= old_modes]
    Hold = mp.matrix(len(old_positions))
    for a, pa in enumerate(old_positions):
        for b, pb in enumerate(old_positions):
            Hold[a, b] = Hnew[pa, pb]
    old = complement_extended(Hold, old_labels_section, ref_modes)
    new = complement_extended(Hnew, idx_new, ref_modes)
    old_in_new, _shell_in_new = embedding_indices(old["labels"], new["labels"])
    Koo = submatrix(new["K"], old_in_new, old_in_new)
    ho = subvector(new["h"], old_in_new)
    eta = new["delta"]
    spectral_lambda = new["mu"] - eta
    _sigma_old, x_old = stieltjes(Koo, ho, new["mu"], eta)
    u = reconstruct_old_vector(new, old_in_new, x_old)
    return Hnew, idx_new, old_positions, u, spectral_lambda


def finite_part_sums(pos, idx_new, old_positions, u, s_values, L):
    z = 2 * mp.pi * idx_new[pos] / L
    s = s_values[pos]
    A = mp.mpf(0)
    B = mp.mpf(0)
    for j in old_positions:
        if j == pos:
            continue
        d = 2 * mp.pi * idx_new[j] / L
        coeff = u[j] / (z - d)
        A += coeff
        B += s_values[j] * coeff
    return A, B - s * A


def analyze_pair(Hbig, idxbig, L, lam, ref_modes, old_modes, new_modes, include_arith, planted):
    Hnew, idx_new, old_positions, u, spectral_lambda = reconstruct_case_with_lambda(
        Hbig, idxbig, ref_modes, old_modes, new_modes
    )
    s_values = [package_s_symbol(2 * mp.pi * n / L, L, lam, include_arith, planted) for n in idx_new]
    c_values = [package_c_symbol(2 * mp.pi * n / L, L, lam, include_arith, planted) for n in idx_new]

    rows = []
    old_set = set(old_positions)
    for pos, n in enumerate(idx_new):
        if abs(n) <= ref_modes:
            kind = "ref"
            continue
        elif pos in old_set:
            kind = "old"
            _A, numerator = finite_part_sums(pos, idx_new, old_positions, u, s_values, L)
            diag_term = (L / 2) * (2 * c_values[pos] - spectral_lambda) * u[pos]
            residual_row = (Hnew[pos, :] * u)[0]
        else:
            kind = "shell"
            z = 2 * mp.pi * n / L
            A, B = cauchy_sums(z, idx_new, old_positions, u, s_values, L)
            numerator = B - s_values[pos] * A
            diag_term = mp.mpf(0)
            residual_row = (Hnew[pos, :] * u)[0]
        scale = max(abs(numerator), abs(diag_term), mp.mpf("1e-100"))
        rows.append(
            {
                "kind": kind,
                "coord": n,
                "u": serial(u[pos]),
                "numerator_B_minus_SA": serial(numerator),
                "numerator_log10": log10_serial(numerator),
                "diag_part_L_over_2_2C_u": serial(diag_term),
                "Hu_row": serial(residual_row),
                "H_minus_lambda_u_row": serial(residual_row - spectral_lambda * u[pos]),
                "loewner_row_identity_log10": log10_serial(
                    residual_row + (2 / L) * numerator - 2 * c_values[pos] * u[pos]
                ),
                "feshbach_old_row_log10": log10_serial(residual_row - spectral_lambda * u[pos])
                if kind == "old"
                else "NA",
                "diag_balance_relative": serial(abs(numerator - diag_term) / scale),
            }
        )
    shell_logs = [mp.mpf(row["numerator_log10"]) for row in rows if row["kind"] == "shell"]
    old_logs = [mp.mpf(row["numerator_log10"]) for row in rows if row["kind"] == "old"]
    shell_abs = [abs(mp.mpf(row["numerator_B_minus_SA"])) for row in rows if row["kind"] == "shell"]
    old_abs = [abs(mp.mpf(row["numerator_B_minus_SA"])) for row in rows if row["kind"] == "old"]
    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "ref_modes": ref_modes,
        "old_max_numerator_log10": serial(max(old_logs)) if old_logs else "NA",
        "shell_max_numerator_log10": serial(max(shell_logs)) if shell_logs else "NA",
        "shell_over_old_max": serial(max(shell_abs) / max(old_abs)) if old_abs and max(old_abs) else "inf",
        "rows": rows,
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
    for old_modes, new_modes in pairs:
        row = analyze_pair(
            Hbig,
            idxbig,
            L,
            mp.mpf(lam),
            ref_modes,
            old_modes,
            new_modes,
            case["include_arith"],
            case["planted"],
        )
        rows.append(row)
        print(
            f"{case['label']:10s} R={ref_modes:2d} {old_modes:2d}->{new_modes:2d} "
            f"oldMax={row['old_max_numerator_log10']:>12s} "
            f"shellMax={row['shell_max_numerator_log10']:>12s} "
            f"shell/old={row['shell_over_old_max']:>12s}",
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
    parser.add_argument("--dps", type=int, default=50)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_mesh_numerator_profile_results.json",
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7h mesh numerator profile requires dps >= 50")
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
        "statement": "E77.7h mesh numerator profile for weighted Cauchy match",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": "Finite mesh profile probe; it does not prove cofinal decay.",
        "cases": [run_case(case, args.lam, args.max_modes, args.ref_modes, pairs, args.dps) for case in cases],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
