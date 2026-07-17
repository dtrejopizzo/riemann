#!/usr/bin/env python3
import numpy as np

from E72_101_model_vs_actual_d2_probe import even_basis
from E72_197_signed_green_word_probe import u_matrix


def full_even_hs(N, u):
    idx = np.arange(-N, N + 1)
    eb = even_basis(idx)
    U = u_matrix(idx, 1.0, u)
    return float(np.real(np.trace(eb.T @ U.conj().T @ eb @ eb.T @ U @ eb)))


def harmonic(n):
    return sum(1.0 / k for k in range(1, n + 1))


def trace_log_bound(N, u):
    a = 1.0 - u
    # Tr(P_+ U^*U P_+) <= (N+1)a + 0.5/pi * H_N.
    return (N + 1) * a + 0.5 * harmonic(N) / np.pi


def run():
    print("E72.260 even-overlap logarithmic bound probe")
    print("bound=(N+1)(1-u)+H_N/(2pi), tested on ||E_+ U_u E_+||_HS^2")
    print("N u hs bound slack")
    for N in [16, 20, 24, 28, 36, 60, 100]:
        worst = (1e9, None, None, None)
        for u in np.linspace(0.0, 1.0, 101):
            hs = full_even_hs(N, u)
            bound = trace_log_bound(N, u)
            slack = bound - hs
            if slack < worst[0]:
                worst = (slack, u, hs, bound)
        print(f"{N:3d} {worst[1]:.2f} {worst[2]:.9e} {worst[3]:.9e} {worst[0]:+.3e}", flush=True)


if __name__ == "__main__":
    run()
