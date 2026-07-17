#!/usr/bin/env python3
import numpy as np


def conv2(a, b, shape):
    out = np.zeros(shape, dtype=complex)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i, j] == 0:
                continue
            for k in range(b.shape[0]):
                for l in range(b.shape[1]):
                    if i + k < shape[0] and j + l < shape[1]:
                        out[i + k, j + l] += a[i, j] * b[k, l]
    return out


def inv_series_1d(u, order):
    # u[0] must be nonzero. Return coefficients of 1/u mod x^order.
    inv = np.zeros(order, dtype=complex)
    inv[0] = 1.0 / u[0]
    for n in range(1, order):
        acc = 0.0 + 0.0j
        for k in range(1, n + 1):
            if k < len(u):
                acc += u[k] * inv[n - k]
        inv[n] = -acc / u[0]
    return inv


def double_residue_projectors(delta, m, n, u, v):
    # Local coordinates x=z-a, y=w-b. Z=x^m U(x), W=y^n V(y).
    inv_u = inv_series_1d(u, m)
    inv_v = inv_series_1d(v, n)
    unit = np.zeros((m, n), dtype=complex)
    for i in range(m):
        for j in range(n):
            unit[i, j] = inv_u[i] * inv_v[j]
    reduced = conv2(delta[:m, :n], unit, (m, n))
    return reduced


def ideal_member_coeff(rng, deg_z, deg_w, m, n):
    out = np.zeros((deg_z + 1, deg_w + 1), dtype=complex)
    a = rng.normal(size=(deg_z - m + 1, deg_w + 1)) + 1j * rng.normal(size=(deg_z - m + 1, deg_w + 1))
    b = rng.normal(size=(deg_z + 1, deg_w - n + 1)) + 1j * rng.normal(size=(deg_z + 1, deg_w - n + 1))
    out[m:, :] += a
    out[:, n:] += b
    return out


def nonmember_coeff(rng, deg_z, deg_w, m, n):
    out = ideal_member_coeff(rng, deg_z, deg_w, m, n)
    out[rng.integers(0, m), rng.integers(0, n)] += 1.0 - 0.4j
    return out


def run():
    rng = np.random.default_rng(359)
    print("E72.359 double-residue projector probe")
    print("Uses nontrivial local units U,V and checks projector equivalence.")
    print("  m   n kind       taylorBlock   projector")
    for m, n in [(1, 1), (2, 2), (3, 1), (3, 3), (5, 2)]:
        deg_z = m + 5
        deg_w = n + 5
        u = np.array([1.2 + 0.3j] + list(0.1 * (rng.normal(size=m - 1) + 1j * rng.normal(size=m - 1))))
        v = np.array([0.8 - 0.2j] + list(0.1 * (rng.normal(size=n - 1) + 1j * rng.normal(size=n - 1))))
        for kind in ["member", "nonmember"]:
            if kind == "member":
                delta = ideal_member_coeff(rng, deg_z, deg_w, m, n)
            else:
                delta = nonmember_coeff(rng, deg_z, deg_w, m, n)
            block = np.linalg.norm(delta[:m, :n])
            proj = np.linalg.norm(double_residue_projectors(delta, m, n, u, v))
            print(f"{m:3d} {n:3d} {kind:>9s} {block:13.5e} {proj:13.5e}")


if __name__ == "__main__":
    run()
