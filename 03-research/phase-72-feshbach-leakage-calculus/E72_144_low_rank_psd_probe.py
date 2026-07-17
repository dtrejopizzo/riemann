#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def relative_eigs(c_actual, c_model):
    delta = c_actual - c_model
    chol = cholesky(c_model)
    x = solve(chol, delta)
    rel = solve(chol, x.T).T
    rel = 0.5 * (rel + rel.T)
    return eigvalsh(rel)


def min_positive_rank_for_distance(eigs, threshold=1.0):
    neg = eigs[eigs < 0.0]
    pos = np.sort(eigs[eigs > 0.0])[::-1]
    neg2 = float(np.sum(neg * neg))
    pos2_total = float(np.sum(pos * pos))
    kept = 0.0
    if neg2 + pos2_total < threshold:
        return 0, np.sqrt(neg2 + pos2_total)
    for r, val in enumerate(pos, start=1):
        kept += float(val * val)
        dist2 = neg2 + pos2_total - kept
        if dist2 < threshold:
            return r, np.sqrt(dist2)
    return len(pos), np.sqrt(neg2)


def run():
    print("E72.144 low-rank PSD certificate probe")
    print(" lam   L  dim  posRank  minRank<1  dist@rank  optDist  topPos  tailPosHS")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        eigs = relative_eigs(c_actual, c_model)
        pos = np.sort(eigs[eigs > 0.0])[::-1]
        neg = eigs[eigs < 0.0]
        min_rank, dist = min_positive_rank_for_distance(eigs)
        opt = np.sqrt(np.sum(neg * neg))
        tail = np.sqrt(max(np.sum(pos[min_rank:] ** 2), 0.0)) if len(pos) else 0.0
        top = pos[0] if len(pos) else 0.0
        print(
            f"{lam:4.0f} {L:5.2f} {len(eigs):4d} {len(pos):8d} "
            f"{min_rank:9d} {dist:10.3f} {opt:8.3f} {top:7.3f} {tail:9.3f}"
        )


if __name__ == "__main__":
    run()
