#!/usr/bin/env python3
import numpy as np


def random_poly_coeff(rng, deg_z, deg_w, scale=1.0):
    return scale * (rng.normal(size=(deg_z + 1, deg_w + 1)) + 1j * rng.normal(size=(deg_z + 1, deg_w + 1)))


def ideal_member_coeff(rng, deg_z, deg_w, m, n):
    a = random_poly_coeff(rng, max(deg_z - m, 0), deg_w)
    b = random_poly_coeff(rng, deg_z, max(deg_w - n, 0))
    out = np.zeros((deg_z + 1, deg_w + 1), dtype=complex)
    if deg_z >= m:
        out[m : m + a.shape[0], : a.shape[1]] += a
    if deg_w >= n:
        out[: b.shape[0], n : n + b.shape[1]] += b
    return out


def nonmember_coeff(rng, deg_z, deg_w, m, n):
    out = ideal_member_coeff(rng, deg_z, deg_w, m, n)
    # Inject one forbidden Taylor coefficient.
    r = rng.integers(0, m)
    s = rng.integers(0, n)
    out[r, s] += 1.0 + 0.25j
    return out


def remainder_norm(coeff, m, n):
    return np.linalg.norm(coeff[:m, :n])


def principal_part_coeff(coeff, m, n):
    # For Z=z^m, W=w^n, Delta/(ZW) has negative exponents exactly from this block.
    return coeff[:m, :n]


def run():
    rng = np.random.default_rng(357)
    print("E72.357 local ideal principal-part probe")
    print("Delta in ((z-a)^m,(w-b)^n) iff forbidden Taylor block vanishes.")
    print("  m   n degZ degW kind       remNorm       ppNorm")
    for m, n in [(1, 1), (2, 1), (1, 3), (3, 2), (4, 3)]:
        deg_z = m + 4
        deg_w = n + 4
        for kind in ["member", "nonmember"]:
            if kind == "member":
                coeff = ideal_member_coeff(rng, deg_z, deg_w, m, n)
            else:
                coeff = nonmember_coeff(rng, deg_z, deg_w, m, n)
            rem = remainder_norm(coeff, m, n)
            pp = np.linalg.norm(principal_part_coeff(coeff, m, n))
            print(f"{m:3d} {n:3d} {deg_z:4d} {deg_w:4d} {kind:>9s} {rem:13.5e} {pp:13.5e}")


if __name__ == "__main__":
    run()
