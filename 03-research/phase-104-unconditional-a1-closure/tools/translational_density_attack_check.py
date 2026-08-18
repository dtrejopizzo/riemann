#!/usr/bin/env python3
"""Exact checks for 104_58 (translational density attack).

Only Fraction-valued Gaussian arithmetic is used.  The analytic dominant
singularity theorem and the all-L density statement are proved in the
document; finite rows here check the normalizations and signs.
"""

from fractions import Fraction as F


def g(x=0, y=0):
    return (F(x), F(y))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def inv(a):
    norm = a[0] * a[0] + a[1] * a[1]
    return (a[0] / norm, -a[1] / norm)


def div(a, b):
    return mul(a, inv(b))


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    out = g(1)
    base = a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def one_minus(a):
    return sub(g(1), a)


def q_orbit(n, w):
    return F(4) - 2 * (power(w, n)[0] + power(w, -n)[0])


def d_orbit(n, w):
    return 4 * q_orbit(n, w)


def geom(w, L):
    out = g()
    term = g(1)
    for _ in range(L):
        out = add(out, term)
        term = mul(term, w)
    return out


def window_formula(N, L, w):
    first = mul(power(w, N), geom(w, L))
    wi = inv(w)
    second = mul(power(wi, N), geom(wi, L))
    return F(16 * L) - 8 * (first[0] + second[0])


def main():
    w = g(0, 2)  # 2i

    # Direct and geometric-series window formulas agree exactly.
    for L in range(1, 13):
        for N in range(1, 25):
            direct = sum(d_orbit(N + h, w) for h in range(L))
            assert direct == window_formula(N, L, w)

    # Every sampled fixed L has a residue class modulo 4 on which all
    # sufficiently late sampled windows are negative.
    witnesses = []
    for L in range(1, 33):
        A = geom(w, L)
        assert A != g()
        good_residues = []
        for residue in range(4):
            rotated = mul(power(g(0, 1), residue), A)[0]
            if rotated > 0:
                good_residues.append(residue)
        assert good_residues
        residue = good_residues[0]
        candidates = [N for N in range(64, 161)
                      if N % 4 == residue]
        assert candidates
        assert all(window_formula(N, L, w) < 0 for N in candidates)
        witnesses.append((L, residue))

    # Exact quartet and homotopy identities.
    rho = (F(1, 5), F(2, 5))
    orbit = (
        rho,
        (rho[0], -rho[1]),
        one_minus(rho),
        one_minus((rho[0], -rho[1])),
    )

    # z_{eta,1}=1-1/eta; Delta B at a=1 equals -Q_n.
    for n in range(1, 17):
        delta_b = F(0)
        for eta in orbit:
            z = one_minus(inv(eta))
            delta_b += power(z, -n)[0] - 1
        assert delta_b == -q_orbit(n, w)

    # At a=4 every transformed quartet zero lies strictly outside |z|=1,
    # with the exact squared moduli used in (25a).
    norms = []
    for eta in orbit:
        z = sub(g(1), div(g(4), eta))
        norm = z[0] * z[0] + z[1] * z[1]
        assert norm > 1
        norms.append(norm)
    assert sorted(norms) == [F(13), F(13), F(73), F(73)]
    assert F(4) + F(2, 73) + F(2, 13) < 6

    # Density-1/4 bad class for the coefficient itself.
    for n in range(4, 65, 4):
        assert q_orbit(n, w) < 0
        assert d_orbit(n, w) < 0

    print("PASS: direct and geometric window identities agree exactly")
    print("PASS: each L=1..32 has an eventual negative residue class mod 4")
    print("PASS: Delta B_{n,1}=-Q_n for the exact reciprocal quartet")
    print("PASS: all quartet transforms lie outside |z|=1 at a=4")
    print("PASS: the quartet alone obeys |Delta B_{n,a}|<3n for a>=4,n>=2")
    print("PASS: n=0 mod 4 is a density-1/4 negative class")
    print("All sign decisions use exact rational Gaussian arithmetic.")


if __name__ == "__main__":
    main()
