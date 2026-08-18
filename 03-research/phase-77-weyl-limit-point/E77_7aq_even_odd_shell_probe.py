#!/usr/bin/env python3
"""E77.7aq decompose shell shorted energy into even/odd channels."""

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
        raise ValueError(f"non-coordinate shell label {label!r}")
    return int(value)


def dot(u: mp.matrix, v: mp.matrix):
    return (u.T * v)[0]


def frob_norm(A: mp.matrix):
    return mp.sqrt(mp.fsum(abs(A[i, j]) ** 2 for i in range(A.rows) for j in range(A.cols)))


def even_odd_basis(labels):
    coords = [parse_coord(label) for label in labels]
    pos = {c: j for j, c in enumerate(coords)}
    mags = sorted({abs(c) for c in coords})
    if len(mags) != 2:
        raise ValueError(f"expected 4-node shell with two radii, got {coords!r}")
    cols = []
    names = []
    for m in mags:
        vm_even = mp.matrix(len(coords), 1)
        vm_odd = mp.matrix(len(coords), 1)
        vm_even[pos[-m]] = mp.mpf("1") / mp.sqrt(2)
        vm_even[pos[m]] = mp.mpf("1") / mp.sqrt(2)
        vm_odd[pos[-m]] = -mp.mpf("1") / mp.sqrt(2)
        vm_odd[pos[m]] = mp.mpf("1") / mp.sqrt(2)
        cols.extend([vm_even, vm_odd])
        names.extend([f"even_{m}", f"odd_{m}"])
    U = mp.matrix(len(coords), len(cols))
    for j, col in enumerate(cols):
        for i in range(len(coords)):
            U[i, j] = col[i]
    return U, names


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
    energy = dot(residual, y)

    U, names = even_odd_basis(shell_labels)
    schur_u = U.T * schur * U
    residual_u = U.T * residual
    y_u = mp.lu_solve(schur_u, residual_u)
    energy_u = dot(residual_u, y_u)

    even_idx = [j for j, name in enumerate(names) if name.startswith("even_")]
    odd_idx = [j for j, name in enumerate(names) if name.startswith("odd_")]
    re = subvector(residual_u, even_idx)
    ro = subvector(residual_u, odd_idx)
    see = submatrix(schur_u, even_idx, even_idx)
    soo = submatrix(schur_u, odd_idx, odd_idx)
    seo = submatrix(schur_u, even_idx, odd_idx)
    soe = submatrix(schur_u, odd_idx, even_idx)

    ye = mp.lu_solve(see, re)
    yo = mp.lu_solve(soo, ro)
    e_even_decoupled = dot(re, ye)
    e_odd_decoupled = dot(ro, yo)
    coupling_norm = frob_norm(seo)
    odd_res_norm = norm(ro)
    even_res_norm = norm(re)

    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "shell_labels": [str(x) for x in shell_labels],
        "eta": serial(eta),
        "shorted_energy": serial(energy),
        "energy_over_eta": serial(energy / eta) if eta else "inf",
        "transformed_energy_defect": serial(abs(energy_u - energy) / max(1, abs(energy))),
        "residual_norm": serial(norm(residual)),
        "even_residual_norm": serial(even_res_norm),
        "odd_residual_norm": serial(odd_res_norm),
        "odd_over_even_residual": serial(odd_res_norm / even_res_norm) if even_res_norm else "inf",
        "even_energy_decoupled": serial(e_even_decoupled),
        "odd_energy_decoupled": serial(e_odd_decoupled),
        "even_energy_over_total": serial(abs(e_even_decoupled) / max(mp.mpf("1e-100"), abs(energy))),
        "odd_energy_over_total": serial(abs(e_odd_decoupled) / max(mp.mpf("1e-100"), abs(energy))),
        "even_odd_block_norm": serial(coupling_norm),
        "schur_u": [[serial(schur_u[i, j]) for j in range(schur_u.cols)] for i in range(schur_u.rows)],
        "residual_u": {names[j]: serial(residual_u[j]) for j in range(len(names))},
        "basis_names": names,
        "seo_norm_over_schur": serial(coupling_norm / max(frob_norm(schur_u), mp.mpf('1e-100'))),
        "see_det": serial(mp.det(see)),
        "soo_det": serial(mp.det(soo)),
    }


def run_build(label, lam, max_modes, pairs, ref_modes, dps, planted):
    mp.mp.dps = dps
    Hbig, idxbig, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for old_modes, new_modes in pairs:
        row = analyze_pair(Hbig, idxbig, ref_modes, old_modes, new_modes)
        print(
            f"{label:6s} {old_modes:2d}->{new_modes:2d} "
            f"odd/even={row['odd_over_even_residual']} "
            f"oddE/tot={row['odd_energy_over_total']} "
            f"seo={row['seo_norm_over_schur']}",
            flush=True,
        )
        rows.append(row)
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "ref_modes": ref_modes,
        "pairs": pairs,
        "planted": None if planted is None else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--ref-modes", type=int, default=10)
    parser.add_argument("--pairs", default="16:18,18:20")
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_7aq_even_odd_shell_results.json")
    args = parser.parse_args()
    pairs = parse_pairs(args.pairs)
    result = {
        "statement": "Even/odd channel decomposition of shell shorted energy",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "ref_modes": args.ref_modes,
            "pairs": pairs,
            "dps": args.dps,
        },
        "cases": [],
    }
    specs = []
    if args.case in {"zeta", "both"}:
        specs.append(("zeta", None))
    if args.case in {"plant", "both"}:
        specs.append(("plant", (GAMMA, "0.30", "5.0")))
    for label, planted in specs:
        result["cases"].append(run_build(label, args.lam, args.max_modes, pairs, args.ref_modes, args.dps, planted))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
