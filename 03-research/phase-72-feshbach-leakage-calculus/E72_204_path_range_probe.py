#!/usr/bin/env python3
import numpy as np

from E72_197_signed_green_word_probe import u_matrix


def signed_u(idx, L, a):
    if a >= 0:
        return u_matrix(idx, L, a)
    return u_matrix(idx, L, -a).conj().T


def dirichlet(idx, L, delta):
    d = 2.0 * np.pi * idx / L
    return np.sum(np.exp(1j * d * delta))


def path_length(L, shifts):
    partial = [0.0]
    s = 0.0
    for a in shifts:
        s += a
        partial.append(s)
    width = max(partial) - min(partial)
    return max(0.0, L - width), s


def trace_product(idx, L, shifts):
    prod = np.eye(len(idx), dtype=complex)
    for a in shifts:
        prod = prod @ signed_u(idx, L, a)
    return np.trace(prod)


def run():
    print("E72.204 bare path-range trace probe")
    print("checks Tr prod U_a = pathLength/L * Dirichlet_N(totalShift)")
    print("L N shifts direct formula relErr")
    L = 5.0
    for N in [8, 16, 32]:
        idx = np.arange(-N, N + 1)
        tests = [
            [0.7, -0.7],
            [1.1, 0.8, -1.9],
            [0.6, -1.4, 0.8],
            [1.2, -0.5, 0.9],
            [2.0, -0.7, -0.4, 0.3],
        ]
        for shifts in tests:
            plen, delta = path_length(L, shifts)
            direct = trace_product(idx, L, shifts)
            formula = (plen / L) * dirichlet(idx, L, delta)
            rel = abs(direct - formula) / max(abs(direct), 1e-30)
            sdesc = ",".join(f"{a:+.1f}" for a in shifts)
            print(
                f"{L:3.1f} {N:2d} {sdesc:22s} "
                f"{direct.real:+.12e} {formula.real:+.12e} {rel:.3e}"
            )


if __name__ == "__main__":
    run()
