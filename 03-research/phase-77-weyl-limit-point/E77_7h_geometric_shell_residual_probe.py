#!/usr/bin/env python3
"""E77.7h geometric shell-residual shape probe."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from E77_7h_feshbach_envelope_probe import GAMMA, norm, serial  # noqa: E402
from E77_7h_shell_stieltjes_increment_probe import (  # noqa: E402
    complement_data,
    parse_pairs,
    section_from_big,
    solve_matrix,
    stieltjes,
)
from P76_002_mp_entry_audit import build_mp  # noqa: E402


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def submatrix(A: mp.matrix, rows: list[int], cols: list[int]):
    out = mp.matrix(len(rows), len(cols))
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            out[i, j] = A[r, c]
    return out


def subvector(v: mp.matrix, rows: list[int]):
    out = mp.matrix(len(rows), 1)
    for i, r in enumerate(rows):
        out[i] = v[r]
    return out


def embedding_indices(old_labels, new_labels):
    position = {label: j for j, label in enumerate(new_labels)}
    old_in_new = [position[label] for label in old_labels]
    old_set = set(old_in_new)
    shell_in_new = [j for j in range(len(new_labels)) if j not in old_set]
    return old_in_new, shell_in_new


def parse_coord(label):
    kind, value = label
    if kind != "coord":
        return None
    return int(value)


def component_rows(labels, direct, mediated, residual):
    direct_norm = norm(direct)
    rows = []
    for j, label in enumerate(labels):
        g = direct[j]
        m = mediated[j]
        r = residual[j]
        rows.append(
            {
                "label": str(label),
                "coord": parse_coord(label),
                "direct": serial(g),
                "mediated": serial(m),
                "residual": serial(r),
                "residual_over_direct_norm": serial(r / direct_norm) if direct_norm else "inf",
                "abs_residual_over_abs_direct": serial(abs(r) / abs(g)) if g else "inf",
            }
        )
    return rows


def symmetry_metrics(labels, vector):
    by_coord = {}
    for j, label in enumerate(labels):
        coord = parse_coord(label)
        if coord is not None:
            by_coord[coord] = vector[j]
    pairs = []
    for coord in sorted([c for c in by_coord if c > 0]):
        if -coord not in by_coord:
            continue
        left = by_coord[-coord]
        right = by_coord[coord]
        even = left + right
        odd = right - left
        denom = max(abs(left), abs(right), mp.mpf("1e-100"))
        pairs.append(
            {
                "coord_abs": coord,
                "left": serial(left),
                "right": serial(right),
                "even_sum": serial(even),
                "odd_diff": serial(odd),
                "even_over_max": serial(abs(even) / denom),
                "odd_over_max": serial(abs(odd) / denom),
            }
        )
    return pairs


def analyze_pair(Hbig, idxbig, ref_modes: int, old_modes: int, new_modes: int):
    Hold, idx_old = section_from_big(Hbig, idxbig, old_modes)
    Hnew, idx_new = section_from_big(Hbig, idxbig, new_modes)
    old = complement_data(Hold, idx_old, ref_modes)
    new = complement_data(Hnew, idx_new, ref_modes)
    old_in_new, shell_in_new = embedding_indices(old["labels"], new["labels"])

    Koo = submatrix(new["K"], old_in_new, old_in_new)
    Kos = submatrix(new["K"], old_in_new, shell_in_new)
    Kss = submatrix(new["K"], shell_in_new, shell_in_new)
    ho = subvector(new["h"], old_in_new)
    hs = subvector(new["h"], shell_in_new)
    shell_labels = [new["labels"][j] for j in shell_in_new]

    eta = new["delta"]
    _sigma_old, x_old = stieltjes(Koo, ho, new["mu"], eta)
    Aoo = Koo - (new["mu"] - eta) * mp.eye(Koo.rows)
    X = solve_matrix(Aoo, Kos)
    mediated = Kos.T * x_old
    residual = hs - mediated
    schur = Kss - (new["mu"] - eta) * mp.eye(Kss.rows) - Kos.T * X
    y = mp.lu_solve(schur, residual)
    energy = (residual.T * y)[0]

    direct_norm = norm(hs)
    mediated_norm = norm(mediated)
    residual_norm = norm(residual)
    cancellation_ratio = residual_norm / max(direct_norm, mediated_norm, mp.mpf("1e-100"))
    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "ref_modes": ref_modes,
        "eta": serial(eta),
        "energy_over_eta": serial(energy / eta) if eta else "inf",
        "energy_over_eta_log10": log10_serial(energy / eta) if eta else "inf",
        "direct_norm": serial(direct_norm),
        "mediated_norm": serial(mediated_norm),
        "residual_norm": serial(residual_norm),
        "cancellation_ratio": serial(cancellation_ratio),
        "cancellation_ratio_log10": log10_serial(cancellation_ratio),
        "components": component_rows(shell_labels, hs, mediated, residual),
        "direct_symmetry": symmetry_metrics(shell_labels, hs),
        "mediated_symmetry": symmetry_metrics(shell_labels, mediated),
        "residual_symmetry": symmetry_metrics(shell_labels, residual),
    }


def add_trends(rows):
    previous = None
    for row in rows:
        energy = mp.mpf(row["energy_over_eta"])
        cancel = mp.mpf(row["cancellation_ratio"])
        if previous is None:
            row["energy_ratio_to_previous_shell"] = "NA"
            row["cancellation_ratio_to_previous_shell"] = "NA"
        else:
            row["energy_ratio_to_previous_shell"] = serial(energy / previous["energy"]) if previous["energy"] else "inf"
            row["cancellation_ratio_to_previous_shell"] = serial(cancel / previous["cancel"]) if previous["cancel"] else "inf"
        previous = {"energy": energy, "cancel": cancel}
    return rows


def run_build(label, lam, max_modes, pairs, ref_modes, dps, planted):
    Hbig, idxbig, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = [analyze_pair(Hbig, idxbig, ref_modes, old, new) for old, new in pairs]
    rows = add_trends(rows)
    for row in rows:
        print(
            f"{label:6s} R={ref_modes:2d} {row['old_modes']:2d}->{row['new_modes']:2d} "
            f"logE={row['energy_over_eta_log10']:>12s} "
            f"logCancel={row['cancellation_ratio_log10']:>12s} "
            f"cancelRatio={row['cancellation_ratio_to_previous_shell']:>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "ref_modes": ref_modes,
        "pairs": pairs,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--ref-modes", type=int, default=10)
    parser.add_argument("--pairs", default="12:14,14:16,16:18,18:20")
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_geometric_shell_residual_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h geometric shell residual requires dps >= 60")
    pairs = parse_pairs(args.pairs)
    if not pairs or max(new for _old, new in pairs) > args.max_modes:
        parser.error("pairs must fit inside max-modes")
    if min(old for old, _new in pairs) <= args.ref_modes:
        parser.error("all old modes must be larger than ref-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h geometric shell-residual shape probe",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite component-shape probe. It identifies vector patterns for the "
            "next theorem but does not prove the infinite residual law."
        ),
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        result["cases"].append(run_build(label, args.lam, args.max_modes, pairs, args.ref_modes, args.dps, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
