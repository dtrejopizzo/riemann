#!/usr/bin/env python3
"""Exact checks for 104_47 (integers and Fraction only)."""

from fractions import Fraction as F
from math import comb, factorial


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(p, q):
    out = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)


def pscale(c, p):
    return trim([c * x for x in p])


def pder(p):
    if len(p) == 1:
        return [F(0)]
    return trim([F(k) * p[k] for k in range(1, len(p))])


def px(p):
    return [F(0)] + list(p)


def laguerre(n, alpha):
    """Coefficients of L_n^(alpha), for alpha in {-1,0,1}."""
    assert n >= 0 and alpha in (-1, 0, 1)
    if alpha == -1:
        if n == 0:
            return [F(1)]
        return [F(0)] + [
            F((-1) ** k * comb(n - 1, n - k), factorial(k))
            for k in range(1, n + 1)
        ]
    return [
        F((-1) ** k * comb(n + alpha, n - k), factorial(k))
        for k in range(n + 1)
    ]


def prefix(n):
    assert n >= 1
    return laguerre(n - 1, 1)


def check_laguerre_identities():
    for n in range(1, 31):
        pn = prefix(n)
        pnext = prefix(n + 1)
        ln = laguerre(n, 0)

        # P_{n+1}-P_n=L_n.
        assert padd(pnext, pscale(F(-1), pn)) == ln

        # P_n+xP_n'-xP_n=nL_n.
        lhs = padd(pn, padd(px(pder(pn)), pscale(F(-1), px(pn))))
        assert lhs == pscale(F(n), ln)

        # L_n^(-1)=-(x/n)P_n.
        lm = laguerre(n, -1)
        assert lm == pscale(F(-1, n), px(pn))

        # (d/dx-1)L_n^(-1)=-L_n.
        assert padd(pder(lm), pscale(F(-1), lm)) == pscale(F(-1), ln)


def polar(n, a):
    eps = a - 1
    return F(1) - (-F(1) / eps) ** n


def polar_derivative(n, a):
    eps = a - 1
    return F(n) * F((-1) ** n) * eps ** (-n - 1)


def check_polar_flow():
    for a in (F(5, 4), F(3, 2), F(2), F(4)):
        for n in range(1, 21):
            lhs = a * polar_derivative(n, a)
            rhs = n * (polar(n + 1, a) - polar(n, a))
            assert lhs == rhs


# Gaussian rationals are pairs (real, imaginary).
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gneg(x):
    return (-x[0], -x[1])


def gsub(x, y):
    return gadd(x, gneg(y))


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def gscale(c, x):
    return (c * x[0], c * x[1])


def ginv(x):
    den = x[0] * x[0] + x[1] * x[1]
    assert den != 0
    return (x[0] / den, -x[1] / den)


def gpow(x, n):
    assert n >= 0
    out = ONE
    base = x
    k = n
    while k:
        if k & 1:
            out = gmul(out, base)
        base = gmul(base, base)
        k >>= 1
    return out


def gabs2(x):
    return x[0] * x[0] + x[1] * x[1]


RHO = (F(4, 5), F(2, 5))
ORBIT = (
    RHO,
    (RHO[0], -RHO[1]),
    (F(1) - RHO[0], -RHO[1]),
    (F(1) - RHO[0], RHO[1]),
)


def zeta_point(eta, a):
    return gsub(ONE, gscale(a, ginv(eta)))


def quartet_q(n, a):
    out = (F(-4), F(0))
    for eta in ORBIT:
        out = gadd(out, gpow(ginv(zeta_point(eta, a)), n))
    return out


def quartet_flow_lhs(n, a):
    out = ZERO
    for eta in ORBIT:
        zinv = ginv(zeta_point(eta, a))
        term = gmul(ginv(eta), gpow(zinv, n + 1))
        out = gadd(out, gscale(a * n, term))
    return out


def quartet_polynomial_on_line(t):
    s = (F(1, 2), t)
    out = ONE
    for eta in ORBIT:
        out = gmul(out, gsub(s, eta))
    return out


def check_quartet():
    for a in (F(1), F(6, 5), F(8, 5), F(2), F(4)):
        for n in (1, 2, 3, 7, 12):
            lhs = quartet_flow_lhs(n, a)
            rhs = gscale(F(n), gsub(quartet_q(n + 1, a), quartet_q(n, a)))
            assert lhs == rhs

    points_at_one = {zeta_point(eta, F(1)) for eta in ORBIT}
    assert points_at_one == {
        (F(0), F(1, 2)),
        (F(0), F(-1, 2)),
        (F(0), F(2)),
        (F(0), F(-2)),
    }

    for eta in ORBIT:
        assert gabs2(zeta_point(eta, F(4))) > 1

    n = 152
    q1 = quartet_q(n, F(1))
    expected = F(2 * (2 ** n) - 4) + F(2, 2 ** n)
    assert q1 == (expected, F(0))
    assert q1[0] > 2 ** 153 - 4

    q4 = quartet_q(n, F(4))
    pulse = q4[0] - q1[0]
    assert q4[1] == 0
    assert pulse < -(2 ** 152)

    for t in (F(-10), F(-1), F(0), F(1, 3), F(2), F(10)):
        value = quartet_polynomial_on_line(t)
        assert value[1] == 0 and value[0] > 0

    return expected, pulse


def main():
    check_laguerre_identities()
    check_polar_flow()
    expected, pulse = check_quartet()
    print("104_47 exact checks: PASS")
    print("Laguerre identities: n=1..30")
    print("polar flow: exact at a=5/4,3/2,2,4")
    print("quartet q_152(1) numerator digits:", len(str(expected.numerator)))
    print("quartet integrated pulse is negative:", pulse < 0)


if __name__ == "__main__":
    main()
