#!/usr/bin/env python3
"""E77.7h barycentric symbol-match probe."""

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
from E77_7h_feshbach_envelope_probe import GAMMA, serial  # noqa: E402
from E77_7h_gamma_cell_shell_transfer_probe import (  # noqa: E402
    complement_extended,
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


def cauchy_sums(z, idx_new, old_positions, u, s_values, L):
    cauchy_u = mp.mpf(0)
    cauchy_su = mp.mpf(0)
    for pos in old_positions:
        d = 2 * mp.pi * idx_new[pos] / L
        coeff = u[pos] / (z - d)
        cauchy_u += coeff
        cauchy_su += s_values[pos] * coeff
    return cauchy_u, cauchy_su


def reconstruct_case(Hbig, idxbig, L, ref_modes, old_modes, new_modes):
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
    _sigma_old, x_old = stieltjes(Koo, ho, new["mu"], eta)
    u = reconstruct_old_vector(new, old_in_new, x_old)
    return Hnew, idx_new, old_positions, u


def eval_points(L, old_modes, new_modes):
    points = []
    for n in range(old_modes + 1, new_modes + 1):
        for sign in (-1, 1):
            points.append((f"node:{sign*n}", 2 * mp.pi * sign * n / L))
    for half in (old_modes + mp.mpf("0.5"), old_modes + mp.mpf("1.5"), new_modes + mp.mpf("0.5")):
        for sign in (-1, 1):
            points.append((f"mid:{mp.nstr(sign*half, 8)}", 2 * mp.pi * sign * half / L))
    return points


def analyze_pair(Hbig, idxbig, L, lam, ref_modes, old_modes, new_modes, include_arith, planted):
    _Hnew, idx_new, old_positions, u = reconstruct_case(Hbig, idxbig, L, ref_modes, old_modes, new_modes)
    s_values = [package_s_symbol(2 * mp.pi * n / L, L, lam, include_arith, planted) for n in idx_new]
    rows = []
    for label, z in eval_points(L, old_modes, new_modes):
        A, B = cauchy_sums(z, idx_new, old_positions, u, s_values, L)
        S = package_s_symbol(z, L, lam, include_arith, planted)
        defect = B - S * A
        scale = max(abs(B), abs(S * A), mp.mpf("1e-100"))
        rows.append(
            {
                "point": label,
                "z": serial(z),
                "A": serial(A),
                "B": serial(B),
                "S": serial(S),
                "defect": serial(defect),
                "relative_defect": serial(abs(defect) / scale),
                "relative_defect_log10": log10_serial(abs(defect) / scale),
            }
        )
    node_logs = [mp.mpf(row["relative_defect_log10"]) for row in rows if row["point"].startswith("node:")]
    mid_logs = [mp.mpf(row["relative_defect_log10"]) for row in rows if row["point"].startswith("mid:")]
    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "ref_modes": ref_modes,
        "max_node_relative_log10": serial(max(node_logs)),
        "max_mid_relative_log10": serial(max(mid_logs)),
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
            f"nodeMax={row['max_node_relative_log10']:>12s} "
            f"midMax={row['max_mid_relative_log10']:>12s}",
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
        default=HERE / "E77_7h_barycentric_symbol_match_results.json",
    )
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.7h barycentric match probe requires dps >= 50")
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
        "statement": "E77.7h barycentric S-symbol match probe",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite interpolation probe. It tests whether the shell match is "
            "nodal or locally off-node; it does not prove a cofinal theorem."
        ),
        "cases": [run_case(case, args.lam, args.max_modes, args.ref_modes, pairs, args.dps) for case in cases],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
