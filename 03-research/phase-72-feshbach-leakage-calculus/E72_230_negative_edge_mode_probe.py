#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]
CANDIDATE_US = [0.60, 0.70, 0.80, 0.90, 1.00]


def full_even_phase_candidate(idx, k, bq, u):
    phase = np.cos(2.0 * np.pi * idx * u)
    phase = phase - np.dot(k, phase) * k
    coord = bq.T @ phase
    nrm = norm(coord)
    return coord / nrm if nrm > 1.0e-14 else coord


def coordinate_spread(v):
    weights = np.abs(v) ** 2
    total = np.sum(weights)
    cs = np.cumsum(np.sort(weights)[::-1]) / max(total, 1.0e-300)
    k50 = int(np.searchsorted(cs, 0.50) + 1)
    k90 = int(np.searchsorted(cs, 0.90) + 1)
    return k50, k90, float(weights.max() / max(total, 1.0e-300))


def run():
    print("E72.230 negative edge-mode probe")
    print("High block A_1. Candidate c_u=Q_even cos(2*pi*m*u) in bq coordinates.")
    print("lam minEig k50 k90 maxCoord bestU bestRayleigh eigAlign candAlign")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        vals, vecs = eigh(0.5 * (a + a.conj().T))
        vmin = vecs[:, 0]
        k50, k90, maxc = coordinate_spread(vmin)
        best = None
        for u in CANDIDATE_US:
            c = full_even_phase_candidate(idx, k, bq, u)
            rq = float(np.real(np.vdot(c, a @ c)))
            align = abs(np.vdot(c, vmin))
            item = (rq, u, align)
            if best is None or rq < best[0]:
                best = item
        eig_align = abs(np.vdot(full_even_phase_candidate(idx, k, bq, best[1]), vmin))
        print(
            f"{lam:3.0f} {vals[0]:+.6e} {k50:3d} {k90:3d} {maxc:.3f} "
            f"{best[1]:.2f} {best[0]:+.6e} {eig_align:.3f} {best[2]:.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
