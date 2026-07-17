#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def summarize(idx, f, topk=8):
    weights = np.abs(f) ** 2
    order = np.argsort(weights)[::-1]
    rows = []
    used_abs = set()
    for j in order:
        m = int(abs(idx[j]))
        if m in used_abs:
            continue
        used_abs.add(m)
        rows.append((m, float(weights[j]), float(np.real(f[j]))))
        if len(rows) >= topk:
            break
    return rows


def run():
    print("E72.231 min-mode Fourier profile probe")
    print("High block minimum eigenvector lifted as f=bq vmin; reports dominant |m| modes")
    print("lam minEig top_abs_modes")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        vals, vecs = eigh(0.5 * (a + a.conj().T))
        f = bq @ vecs[:, 0]
        rows = summarize(idx, f)
        payload = " ".join(f"{m}:{w:.3f}:{sgn:+.2f}" for m, w, sgn in rows)
        print(f"{lam:3.0f} {vals[0]:+.6e} {payload}", flush=True)


if __name__ == "__main__":
    run()
