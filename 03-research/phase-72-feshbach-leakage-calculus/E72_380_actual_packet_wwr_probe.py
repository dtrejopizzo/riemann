#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def q_matrix_fast(idx, d, L, y):
    dm = d[:, None]
    dn = d[None, :]
    im = idx[:, None]
    inn = idx[None, :]
    mask = im == inn
    denom = np.pi * (inn - im)
    safe = np.where(mask, 1.0, denom)
    vals = (np.sin(dm * y) - np.sin(dn * y)) / safe
    out = vals.astype(float)
    out[~mask] = vals[~mask]
    np.fill_diagonal(out, 2.0 * (1.0 - y / L) * np.cos(d * y))
    return out


def a_vec(z, L, d):
    return (1.0 - cmath.exp(z * L)) / (1j * z - d)


def packet_B(y, z, idx, d, L, xi, avec=None):
    if y < 0 or y > L:
        return 0j
    if avec is None:
        avec = a_vec(z, L, d)
    q = q_matrix_fast(idx, d, L, y)
    return avec @ (q @ xi)


def von_mangoldt_prime_powers(maxn):
    rows = []
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        while n <= maxn:
            rows.append((n, lp, math.log(n)))
            if n > maxn // p:
                break
            n *= p
    rows.sort()
    return rows


def D_T(x, T):
    if abs(x) < 1e-12:
        return T / math.pi
    return math.sin(T * x) / (math.pi * x)


def wall_coeff_from_samples(u, ts, gs, T):
    # Trapezoid is sufficient for this diagnostic; ts is uniform.
    vals = gs * np.array([D_T(t - u, T) for t in ts])
    return np.trapezoid(vals, ts)


def sample_packet(z, idx, d, L, xi, grid_n):
    avec = a_vec(z, L, d)
    ts = np.linspace(-L, L, grid_n)
    bs = np.array([packet_B(abs(t), z, idx, d, L, xi, avec) for t in ts], dtype=complex)
    return ts, bs


def local_modulus(samples_t, samples_b, u, delta):
    b0 = np.interp(u, samples_t, samples_b.real) + 1j * np.interp(u, samples_t, samples_b.imag)
    lo = max(0.0, u - delta)
    hi = min(samples_t[-1], u + delta)
    mask = (samples_t >= lo) & (samples_t <= hi)
    if not np.any(mask):
        return 0.0
    return float(np.max(np.abs(samples_b[mask] - b0)))


def run():
    print("E72.380 actual packet WWR probe")
    print(" lam  dim     z                  T    cells    errPrime    nearWeighted  crudeVar   mass")
    cases = [
        (6, 10, 0.25 + 1.0j, 50.0),
        (8, 12, 0.25 + 1.0j, 70.0),
        (10, 14, 0.25 + 1.0j, 90.0),
        (12, 16, 0.25 + 1.0j, 110.0),
    ]
    c = 0.8
    for lam, n_modes, z, T in cases:
        idx, d, L, xi = setup(lam, n_modes)
        rows = von_mangoldt_prime_powers(int(math.exp(L)))
        grid_n = 2401
        ts_full, bs_full = sample_packet(z, idx, d, L, xi, grid_n)
        # Right-wall gauge for finite coefficient computation.
        gs = np.exp(c * ts_full) * bs_full
        # Positive-side packet samples for local modulus.
        pos_mask = ts_full >= 0
        ts_pos = ts_full[pos_mask]
        bs_pos = bs_full[pos_mask]
        err = 0j
        mass = 0.0
        omega = 0.0
        delta = 1.0 / math.sqrt(T)
        for n, lamn, u in rows:
            if u > L:
                continue
            coeff = lamn * n ** (-0.5 - c)
            wc = wall_coeff_from_samples(u, ts_full, gs, T)
            b_u = packet_B(u, z, idx, d, L, xi)
            err += coeff * wc - lamn * n ** (-0.5) * b_u
            mass += lamn * n ** (-0.5) * abs(b_u)
            omega += lamn * n ** (-0.5) * local_modulus(ts_pos, bs_pos, u, delta)
        near = math.log(2 + T * delta) * (omega + c * delta * mass)
        crude_var = float(np.sum(np.abs(np.diff(gs))))
        print(
            f"{lam:4.0f} {len(idx):4d} {z!s:18s} {T:5.0f} {len(rows):6d} "
            f"{abs(err):11.3e} {near:13.3e} {crude_var:10.3e} {mass:8.3e}"
        )


if __name__ == "__main__":
    run()
