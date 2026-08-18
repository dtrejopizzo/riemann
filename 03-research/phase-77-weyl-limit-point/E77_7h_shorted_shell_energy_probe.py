#!/usr/bin/env python3
"""E77.7h shorted shell-energy anatomy probe."""

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


def dot(u: mp.matrix, v: mp.matrix):
    return (u.T * v)[0]


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

    eta = new["delta"]
    sigma_old, x_old = stieltjes(Koo, ho, new["mu"], eta)
    sigma_new, _ = stieltjes(new["K"], new["h"], new["mu"], eta)
    Aoo = Koo - (new["mu"] - eta) * mp.eye(Koo.rows)
    X = solve_matrix(Aoo, Kos)
    mediated = Kos.T * x_old
    residual = hs - mediated
    schur = Kss - (new["mu"] - eta) * mp.eye(Kss.rows) - Kos.T * X
    y = mp.lu_solve(schur, residual)
    energy = dot(residual, y)
    schur_values, schur_vectors = mp.eigsy(schur)
    schur_min = schur_values[0]
    crude_bound = norm(residual) ** 2 / schur_min if schur_min > 0 else mp.inf
    hs_norm = norm(hs)
    med_norm = norm(mediated)
    res_norm = norm(residual)
    cos_g_med = dot(hs, mediated) / (hs_norm * med_norm) if hs_norm and med_norm else mp.mpf("0")
    cancellation_ratio = res_norm / max(hs_norm, med_norm, mp.mpf("1e-100"))
    source_energy = dot(hs, mp.lu_solve(schur, hs))
    mediated_energy = dot(mediated, mp.lu_solve(schur, mediated))
    cross_energy = dot(hs, mp.lu_solve(schur, mediated))
    identity_defect = abs((sigma_new - sigma_old) - energy) / max(mp.mpf("1"), abs(sigma_new - sigma_old), abs(energy))
    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "ref_modes": ref_modes,
        "shell_labels": [str(new["labels"][j]) for j in shell_in_new],
        "eta": serial(eta),
        "fixed_shell_increment": serial(sigma_new - sigma_old),
        "shorted_energy": serial(energy),
        "energy_over_eta": serial(energy / eta) if eta else "inf",
        "identity_relative_defect": serial(identity_defect),
        "identity_log10_defect": log10_serial(identity_defect),
        "direct_shell_norm": serial(hs_norm),
        "mediated_shell_norm": serial(med_norm),
        "residual_norm": serial(res_norm),
        "cancellation_ratio": serial(cancellation_ratio),
        "cos_direct_mediated": serial(cos_g_med),
        "schur_min_eigenvalue": serial(schur_min),
        "schur_max_eigenvalue": serial(schur_values[schur_values.rows - 1]),
        "schur_condition": serial(schur_values[schur_values.rows - 1] / schur_min)
        if schur_min > 0
        else "inf",
        "crude_residual_bound": serial(crude_bound),
        "crude_bound_over_energy": serial(crude_bound / energy) if energy else "inf",
        "direct_energy": serial(source_energy),
        "mediated_energy": serial(mediated_energy),
        "cross_energy": serial(cross_energy),
        "energy_expansion_defect": serial(
            abs((source_energy + mediated_energy - 2 * cross_energy) - energy)
            / max(mp.mpf("1"), abs(energy))
        ),
    }


def run_build(label, lam, max_modes, pairs, ref_modes, dps, planted):
    Hbig, idxbig, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for old_modes, new_modes in pairs:
        row = analyze_pair(Hbig, idxbig, ref_modes, old_modes, new_modes)
        print(
            f"{label:6s} {old_modes:2d}->{new_modes:2d} "
            f"E/eta={mp.nstr(mp.mpf(row['energy_over_eta']), 8):>12s} "
            f"res/direct={mp.nstr(mp.mpf(row['cancellation_ratio']), 8):>12s} "
            f"cos={mp.nstr(mp.mpf(row['cos_direct_mediated']), 8):>12s} "
            f"crude/E={mp.nstr(mp.mpf(row['crude_bound_over_energy']), 8):>12s}",
            flush=True,
        )
        rows.append(row)
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "max_modes": max_modes,
        "ref_modes": ref_modes,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--pairs", default="16:18,18:20")
    parser.add_argument("--ref-modes", type=int, default=14)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "E77_7h_shorted_shell_energy_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h shorted shell energy requires dps >= 60")
    pairs = parse_pairs(args.pairs)
    if not pairs or max(new for _old, new in pairs) > args.max_modes:
        parser.error("pairs must be nonempty and fit inside max-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h shorted shell-energy anatomy probe",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "pairs": pairs,
            "ref_modes": args.ref_modes,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite anatomy probe. It identifies the cancellation object but does "
            "not prove the infinite shorted-shell energy estimate."
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
