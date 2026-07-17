#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    prime = h_model - h_actual
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_model, prime, idx.astype(int), d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def q_second_matrix(idx, d, L, y):
    dm = d[:, None]
    dn = d[None, :]
    im = idx[:, None]
    inn = idx[None, :]
    mask = im == inn
    denom = np.pi * (inn - im)
    safe = np.where(mask, 1.0, denom)
    vals = (-dm * dm * np.sin(dm * y) + dn * dn * np.sin(dn * y)) / safe
    out = vals.astype(float)
    out[~mask] = vals[~mask]
    diag = 4.0 * d / L * np.sin(d * y) - 2.0 * (1.0 - y / L) * d * d * np.cos(d * y)
    np.fill_diagonal(out, diag)
    return out


def r0(y, L):
    return y * (1.0 - y / L)


def r1(y, L):
    return y * y * (1.0 - y / L)


def r0_second(_y, L):
    return -2.0 / L


def r1_second(y, L):
    return 2.0 - 6.0 * y / L


def arch_weight(y):
    if y < 1e-8:
        # W(y)=e^(y/2)+e^(-y/2)-e^(y/2)/(2sinh y) has a pole,
        # but K_L integrates (s-y)W(s) from t to L; this function is
        # never called in a singular product at y=0 except under quad.
        y = 1e-8
    return np.exp(y / 2.0) + np.exp(-y / 2.0) - np.exp(y / 2.0) / (2.0 * np.sinh(y))


def arch_dirichlet(func, deriv0, L):
    def wr(y):
        if y < 1e-8:
            return deriv0 / 2.0
        return np.exp(y / 2.0) * func(y) / (2.0 * np.sinh(y))

    a_re, _ = quad(lambda y: np.real(func(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    a_im, _ = quad(lambda y: np.imag(func(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    w_re, _ = quad(lambda y: np.real(wr(y)), 0, L, limit=250)
    w_im, _ = quad(lambda y: np.imag(wr(y)), 0, L, limit=250)
    return (a_re + 1j * a_im) - (w_re + 1j * w_im)


def prime_sum(func, L, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            total += lp * n ** -0.5 * func(k * lp)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def functional(func, deriv0, L, lam):
    return arch_dirichlet(func, deriv0, L) - prime_sum(func, L, lam)


def prime_power_rows(lam):
    rows = []
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            rows.append((k * lp, lp * n ** -0.5))
            if n > maxn // p:
                break
            n *= p
            k += 1
    return rows


def second_abel_kernel(t, L, rows):
    aw, _ = quad(lambda y: (y - t) * arch_weight(y), t, L, limit=250)
    ps = 0.0
    for y, coeff in rows:
        if y >= t:
            ps += coeff * (y - t)
    return aw - ps


def split_integral(func, points, L):
    total = 0.0
    grid = [0.0]
    for p in sorted(points):
        if 0.0 < p < L and (not grid or abs(p - grid[-1]) > 1e-10):
            grid.append(p)
    grid.append(L)
    for a, b in zip(grid[:-1], grid[1:]):
        if b <= a:
            continue
        val, _ = quad(func, a, b, limit=120)
        total += val
    return total


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.194 second Abel kernel")
    print("Checks F[Bbal]=int K_L(t) Bbal''(t) dt.")
    print(" lam     L gamma row totalB abelB relErr cAbsB")
    for lam, n_modes in [(12, 16), (16, 20)]:
        h_model, prime_op, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c = -f0 / f1
        rows = prime_power_rows(lam)

        # Precompute K on quadrature demand.  This is intentionally direct,
        # because the purpose is to verify the identity, not speed.
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for j in range(2):
                row = q[j]
                h = min(1e-6, L * 1e-7)
                # Exact B'(0) rank-one formula.
                bp0 = -(2.0 / L) * np.sum(row) * np.sum(eta)
                total = row @ ((h_model - prime_op) @ eta)

                def bbal_second(t):
                    return (
                        row @ (q_second_matrix(idx, d, L, t) @ eta)
                        - bp0 * (r0_second(t, L) + c * r1_second(t, L))
                    )

                def integrand_re(t):
                    return np.real(second_abel_kernel(t, L, rows) * bbal_second(t))

                def integrand_im(t):
                    return np.imag(second_abel_kernel(t, L, rows) * bbal_second(t))

                prime_points = [y for y, _coeff in rows]
                re = split_integral(integrand_re, prime_points, L)
                im = split_integral(integrand_im, prime_points, L)
                abel = re + 1j * im
                rel = abs(abel - total) / max(abs(total), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(total, L):7.2f} {bexp(abel, L):6.2f}"
                    f" {rel:8.1e} {bexp(c, L):6.2f}"
                )


if __name__ == "__main__":
    run()
