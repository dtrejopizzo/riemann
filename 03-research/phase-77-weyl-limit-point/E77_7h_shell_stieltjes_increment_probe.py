#!/usr/bin/env python3
"""E77.7h shell Stieltjes-increment identity probe."""

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
from E77_7h_feshbach_envelope_probe import GAMMA, norm, serial  # noqa: E402


def log10_serial(value, digits: int = 18) -> str:
    value = abs(value)
    if value <= 0:
        return "-inf"
    return mp.nstr(mp.log10(value), digits)


def section_from_big(Hbig: mp.matrix, idxbig: list[int], modes: int):
    positions = [j for j, n in enumerate(idxbig) if abs(n) <= modes]
    H = mp.matrix(len(positions))
    for a, pa in enumerate(positions):
        for b, pb in enumerate(positions):
            H[a, b] = Hbig[pa, pb]
    idx = [idxbig[p] for p in positions]
    return H, idx


def complement_data(H: mp.matrix, idx: list[int], ref_modes: int):
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
    delta = mu - full_vals[0]
    return {
        "K": K,
        "h": h,
        "mu": mu,
        "delta": delta,
        "labels": labels,
        "full_mu": full_vals[0],
    }


def stieltjes(K: mp.matrix, h: mp.matrix, mu: mp.mpf, eta: mp.mpf):
    A = K - (mu - eta) * mp.eye(K.rows)
    x = mp.lu_solve(A, h)
    return (h.T * x)[0], x


def embedding_indices(old_labels, new_labels):
    position = {label: j for j, label in enumerate(new_labels)}
    old_in_new = [position[label] for label in old_labels]
    old_set = set(old_in_new)
    shell_in_new = [j for j in range(len(new_labels)) if j not in old_set]
    return old_in_new, shell_in_new


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


def solve_matrix(A: mp.matrix, B: mp.matrix):
    out = mp.matrix(A.rows, B.cols)
    for j in range(B.cols):
        col = mp.matrix([B[i, j] for i in range(B.rows)])
        solved = mp.lu_solve(A, col)
        for i in range(A.rows):
            out[i, j] = solved[i]
    return out


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

    eta_old = old["delta"]
    eta_new = new["delta"]
    sigma_old_at_old, _ = stieltjes(old["K"], old["h"], old["mu"], eta_old)
    sigma_old_at_new, x_old_new = stieltjes(Koo, ho, new["mu"], eta_new)
    sigma_new_at_new, _ = stieltjes(new["K"], new["h"], new["mu"], eta_new)

    Aoo = Koo - (new["mu"] - eta_new) * mp.eye(Koo.rows)
    X = solve_matrix(Aoo, Kos) if shell_in_new else mp.matrix(Koo.rows, 0)
    schur = Kss - (new["mu"] - eta_new) * mp.eye(Kss.rows) - Kos.T * X
    residual_shell = hs - Kos.T * x_old_new
    if shell_in_new:
        y = mp.lu_solve(schur, residual_shell)
        shell_increment = (residual_shell.T * y)[0]
        schur_values, _ = mp.eigsy(schur)
        schur_min = schur_values[0]
    else:
        shell_increment = mp.mpf("0")
        schur_min = mp.inf
    direct_fixed_increment = sigma_new_at_new - sigma_old_at_new
    eta_drift_increment = sigma_old_at_new - sigma_old_at_old
    total_increment = sigma_new_at_new - sigma_old_at_old
    identity_defect = abs(direct_fixed_increment - shell_increment) / max(
        mp.mpf("1"), abs(direct_fixed_increment), abs(shell_increment)
    )
    return {
        "old_modes": old_modes,
        "new_modes": new_modes,
        "ref_modes": ref_modes,
        "shell_labels": [str(new["labels"][j]) for j in shell_in_new],
        "mu_ref": serial(new["mu"]),
        "delta_old": serial(eta_old),
        "delta_new": serial(eta_new),
        "delta_ratio_new_over_old": serial(eta_new / eta_old) if eta_old else "inf",
        "sigma_old_at_eta_old": serial(sigma_old_at_old),
        "sigma_old_at_eta_new": serial(sigma_old_at_new),
        "sigma_new_at_eta_new": serial(sigma_new_at_new),
        "fixed_eta_shell_increment_direct": serial(direct_fixed_increment),
        "fixed_eta_shell_increment_schur": serial(shell_increment),
        "eta_drift_increment_old_space": serial(eta_drift_increment),
        "total_increment": serial(total_increment),
        "shell_increment_over_eta_new": serial(shell_increment / eta_new) if eta_new else "inf",
        "eta_drift_over_eta_new": serial(eta_drift_increment / eta_new) if eta_new else "inf",
        "total_increment_over_eta_new": serial(total_increment / eta_new) if eta_new else "inf",
        "identity_relative_defect": serial(identity_defect),
        "identity_log10_defect": log10_serial(identity_defect),
        "shell_residual_norm": serial(norm(residual_shell)),
        "schur_min_eigenvalue": serial(schur_min),
        "schur_dim": schur.rows,
    }


def run_build(label, lam, max_modes, pairs, ref_modes, dps, planted):
    Hbig, idxbig, L = build_mp(lam, max_modes, dps, planted=planted)
    rows = []
    for old_modes, new_modes in pairs:
        row = analyze_pair(Hbig, idxbig, ref_modes, old_modes, new_modes)
        print(
            f"{label:6s} {old_modes:2d}->{new_modes:2d} "
            f"shell/eta={mp.nstr(mp.mpf(row['shell_increment_over_eta_new']), 8):>12s} "
            f"drift/eta={mp.nstr(mp.mpf(row['eta_drift_over_eta_new']), 8):>12s} "
            f"total/eta={mp.nstr(mp.mpf(row['total_increment_over_eta_new']), 8):>12s} "
            f"def={row['identity_log10_defect']:>8s}",
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


def parse_pairs(text: str):
    pairs = []
    for item in text.split(","):
        if not item:
            continue
        left, right = item.split(":")
        pairs.append((int(left), int(right)))
    return pairs


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
        default=HERE / "E77_7h_shell_stieltjes_increment_results.json",
    )
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.7h shell Stieltjes increment requires dps >= 60")
    pairs = parse_pairs(args.pairs)
    if not pairs or max(new for _old, new in pairs) > args.max_modes:
        parser.error("pairs must be nonempty and fit inside max-modes")
    if min(old for old, _new in pairs) <= args.ref_modes:
        parser.error("all old modes must be larger than ref-modes")
    mp.mp.dps = args.dps
    result = {
        "statement": "E77.7h shell Stieltjes-increment identity probe",
        "parameters": {
            "lambda": args.lam,
            "max_modes": args.max_modes,
            "pairs": pairs,
            "ref_modes": args.ref_modes,
            "dps": args.dps,
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "warning": (
            "Finite shell Schur identity. It proves the exact finite decomposition "
            "but not the infinite shell summability theorem."
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
