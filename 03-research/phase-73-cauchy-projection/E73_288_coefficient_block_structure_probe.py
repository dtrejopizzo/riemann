#!/usr/bin/env python3
import sys
from collections import defaultdict

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows  # noqa: E402
from E73_287_closed_weight_formula_probe import closed_V, closed_W  # noqa: E402


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


def split_packet_modes(row, idx, d, eta, L):
    c_diag = defaultdict(complex)
    c_off = defaultdict(complex)
    lin = defaultdict(complex)
    n = len(idx)
    for a in range(n):
        for b in range(n):
            coeff = row[a] * eta[b]
            if a == b:
                omega = float(d[a])
                c_diag[omega] += coeff
                c_diag[-omega] += coeff
                lin[omega] += -coeff / L
                lin[-omega] += -coeff / L
            else:
                den = np.pi * (idx[b] - idx[a])
                c_off[float(d[a])] += coeff / (2j * den)
                c_off[float(-d[a])] += -coeff / (2j * den)
                c_off[float(d[b])] += -coeff / (2j * den)
                c_off[float(-d[b])] += coeff / (2j * den)
    return dict(c_diag), dict(c_off), dict(lin)


def arr(mapping, freqs):
    return np.array([mapping.get(float(o), 0j) for o in freqs], dtype=complex)


def run():
    print("E73.288 coefficient block structure probe")
    print("Splits exact packet coefficients into diagonal c_diag, off-diagonal c_off, and linear l.")
    print("diagRel tests l_omega = -c_diag_omega/L.")
    print(
        " lam     L gamma row nfreq diagRel cDiagB cOffB lB pairDiagB pairOffB pairVB totalB cancel"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        freqs = np.array(sorted(set([float(x) for x in d] + [float(-x) for x in d])), dtype=float)
        W = np.array([closed_W(o, L, lam) for o in freqs], dtype=complex)
        V = np.array([closed_V(o, L, lam) for o in freqs], dtype=complex)
        Wg = W - np.mean(W)
        Vg = V - np.mean(V)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (np.eye(len(d), dtype=complex) - projector(q)) @ xi
            for row_id in range(2):
                cdiag_m, coff_m, lin_m = split_packet_modes(q[row_id], idx, d, eta, L)
                cdiag = arr(cdiag_m, freqs)
                coff = arr(coff_m, freqs)
                lin = arr(lin_m, freqs)
                diag_rel = norm(lin + cdiag / L) / max(norm(lin), 1e-300)
                pdiag = np.dot(cdiag, Wg)
                poff = np.dot(coff, Wg)
                pv = np.dot(lin, Vg)
                total = pdiag + poff + pv
                cancel = abs(total) / max(abs(pdiag) + abs(poff) + abs(pv), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d} {len(freqs):5d}"
                    f" {diag_rel:7.1e} {bexp(norm(cdiag),L):6.2f}"
                    f" {bexp(norm(coff),L):6.2f} {bexp(norm(lin),L):5.2f}"
                    f" {bexp(pdiag,L):9.2f} {bexp(poff,L):8.2f}"
                    f" {bexp(pv,L):7.2f} {bexp(total,L):7.2f}"
                    f" {cancel:8.1e}"
                )


if __name__ == "__main__":
    run()
