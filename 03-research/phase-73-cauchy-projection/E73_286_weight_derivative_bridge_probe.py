#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows, functional_scalar  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi.astype(complex)


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def weights(freqs, L, lam):
    W = np.array(
        [functional_scalar(lambda y, o=o: np.exp(1j * o * y), 1j * o, L, lam) for o in freqs],
        dtype=complex,
    )
    V = np.array(
        [functional_scalar(lambda y, o=o: y * np.exp(1j * o * y), 1.0 + 0j, L, lam) for o in freqs],
        dtype=complex,
    )
    return W, V


def coeff_arrays(const, linear, freqs):
    c = np.array([const.get(float(o), 0j) for o in freqs], dtype=complex)
    l = np.array([linear.get(float(o), 0j) for o in freqs], dtype=complex)
    return c, l


def central_derivative(arr, h):
    out = np.zeros_like(arr)
    out[1:-1] = (arr[2:] - arr[:-2]) / (2.0 * h)
    out[0] = (arr[1] - arr[0]) / h
    out[-1] = (arr[-1] - arr[-2]) / h
    return out


def adjoint_central(l, h):
    # Adjoints central_derivative under the Euclidean sum pairing, with
    # one-sided endpoint rows matching central_derivative above.
    n = len(l)
    out = np.zeros_like(l)
    if n == 1:
        return out
    # Boundary derivative rows.
    out[0] += -l[0] / h
    out[1] += l[0] / h
    out[-2] += -l[-1] / h
    out[-1] += l[-1] / h
    # Interior central rows.
    for j in range(1, n - 1):
        out[j - 1] += -l[j] / (2.0 * h)
        out[j + 1] += l[j] / (2.0 * h)
    return out


def run():
    print("E73.286 weight derivative bridge probe")
    print("Tests V_omega=(1/i)dW/domega and discrete integration-by-parts explanation of c/l cancellation.")
    print("dErr is finite-difference error for V; divErr tests c+(1/i)D^*l as effective W coefficient.")
    print(
        " lam     L gamma row nfreq dErrB pairB ibpB ibpErrB divNormB divPairB cancel"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        freqs = np.array(sorted(set([float(x) for x in d] + [float(-x) for x in d])), dtype=float)
        hstep = 2.0 * np.pi / L
        W, V = weights(freqs, L, lam)
        Wg = W - np.mean(W)
        Vg = V - np.mean(V)
        dW = central_derivative(Wg, hstep)
        V_from_W = dW / 1j
        d_err = norm(Vg - V_from_W) / max(norm(Vg), 1e-300)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (np.eye(len(d), dtype=complex) - projector(q)) @ xi
            for row_id in range(2):
                const, linear = packet_modes(q[row_id], idx, d, eta, L)
                c, l = coeff_arrays(const, linear, freqs)
                pair = np.dot(c, Wg) + np.dot(l, Vg)
                ibp = np.dot(c, Wg) + np.dot(l, V_from_W)
                # sum l*(1/i DW) = sum ((1/i)D^*l)*W in exact adjoint algebra.
                effective_c = c + adjoint_central(l, hstep) / 1j
                div_pair = np.dot(effective_c, Wg)
                cancel = abs(pair) / max(abs(np.dot(c, Wg)) + abs(np.dot(l, Vg)), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d} {len(freqs):5d}"
                    f" {bexp(d_err,L):6.2f} {bexp(pair,L):6.2f}"
                    f" {bexp(ibp,L):6.2f} {bexp(ibp-pair,L):8.2f}"
                    f" {bexp(norm(effective_c),L):8.2f}"
                    f" {bexp(div_pair,L):8.2f} {cancel:8.1e}"
                )


if __name__ == "__main__":
    run()
