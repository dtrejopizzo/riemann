#!/usr/bin/env python3
"""Exact checks for 104_46; floats are display-only diagnostics."""

from fractions import Fraction as Q
from math import comb, factorial


def laguerre_coeff(r, alpha, scale=Q(1)):
    """Coefficients of L_r^(alpha)(scale*x), low degree first."""
    return [
        Q((-1) ** j * comb(r + alpha, r - j), factorial(j)) * scale**j
        for j in range(r + 1)
    ]


def poly_eval(a, x):
    ans = Q(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans


def dilation_coeffs(r, beta):
    """L_r^1(beta*y)=sum_j a[r,j] L_j(y)."""
    out = []
    for j in range(r + 1):
        out.append(
            beta**j
            * sum(
                Q(comb(k, j)) * (1 - beta) ** (k - j)
                for k in range(j, r + 1)
            )
        )
    return out


def ordinary_laguerre_value(j, y):
    return poly_eval(laguerre_coeff(j, 0), y)


def exp_moment(k, eps):
    return Q(factorial(k), 1) / eps**k


def gamma2_moment(k, eps):
    return Q(factorial(k + 1), 1) / eps**k


def continuous_gamma_quotient(r, s):
    eps = s - 1
    beta = s / eps
    a = dilation_coeffs(r, beta)
    den = sum(x * x for x in a[1:])
    num = sum(a[j] * a[j] / (j + 1) for j in range(1, r + 1))
    return num / den


def direct_gamma_quotient(r, s):
    """Independent monomial-moment calculation of (31)."""
    eps = s - 1
    c = laguerre_coeff(r, 1, s)
    mu = sum(c[j] * exp_moment(j, eps) for j in range(r + 1))
    ein2 = sum(
        c[j] * c[k] * exp_moment(j + k, eps)
        for j in range(r + 1)
        for k in range(r + 1)
    )
    hard = [c[j] / (j + 1) for j in range(r + 1)]
    eout2 = sum(
        hard[j] * hard[k] * gamma2_moment(j + k, eps)
        for j in range(r + 1)
        for k in range(r + 1)
    )
    return (eout2 - mu * mu) / (ein2 - mu * mu)


def check_dilation():
    beta = Q(3)
    for r in range(9):
        a = dilation_coeffs(r, beta)
        for y in (Q(0), Q(1, 3), Q(2), Q(7, 2)):
            lhs = poly_eval(laguerre_coeff(r, 1, beta), y)
            rhs = sum(a[j] * ordinary_laguerre_value(j, y) for j in range(r + 1))
            assert lhs == rhs
        # Exact l1 identity (15), valid here because beta>2.
        assert sum(abs(x) for x in a) == ((2 * beta - 1) ** (r + 1) + (-1) ** r) / (2 * beta)


def check_gamma():
    s = Q(3, 2)
    rows = []
    for r in (1, 2, 4, 8, 16, 24):
        q1 = continuous_gamma_quotient(r, s)
        q2 = direct_gamma_quotient(r, s)
        assert q1 == q2
        assert Q(0) < q1 <= Q(1, 2)
        rows.append((r, q1))
    return rows


def check_shift_blindness():
    # A finite conditional-expectation model, entirely rational.
    # D,K are independent Bernoulli variables and N=D+K.
    pd = (Q(2, 5), Q(3, 5))
    pk = (Q(1, 4), Q(3, 4))
    f = (Q(-7, 3), Q(11, 5))

    def quotient(values):
        mu = sum(pd[d] * values[d] for d in (0, 1))
        vin = sum(pd[d] * (values[d] - mu) ** 2 for d in (0, 1))
        pn = [Q(0), Q(0), Q(0)]
        joint_sum = [Q(0), Q(0), Q(0)]
        for d in (0, 1):
            for k in (0, 1):
                w = pd[d] * pk[k]
                pn[d + k] += w
                joint_sum[d + k] += w * values[d]
        vout = sum(
            pn[n] * (joint_sum[n] / pn[n] - mu) ** 2
            for n in (0, 1, 2)
            if pn[n]
        )
        return vout / vin

    q0 = quotient(f)
    for c in (Q(-100), Q(7, 9), Q(2001, 17)):
        assert quotient(tuple(x + c for x in f)) == q0

    # The signed two-channel mean is not shift invariant.
    L = Q(13, 7)
    inv_eps = Q(9, 5)
    c = Q(17, 11)
    before = L * Q(2, 3) - inv_eps * Q(-4, 5)
    after = L * (Q(2, 3) + c) - inv_eps * (Q(-4, 5) + c)
    assert after - before == c * (L - inv_eps)


def check_pk_row():
    # Equation (22), with x=log p and c=log k treated symbolically as rationals.
    x, c = Q(17, 3), Q(5, 4)
    fp, ck, mu = Q(-19, 7), Q(23, 8), Q(11, 6)
    centered = (x * fp + ck) / (x + c) - mu
    assert centered == (x * (fp - mu) + ck - c * mu) / (x + c)


def check_offline():
    for n in range(1, 25):
        quartet = Q(8) - Q(4) * (Q(2) ** n + Q(1, 2) ** n)
        assert quartet < 0


def main():
    check_dilation()
    rows = check_gamma()
    check_shift_blindness()
    check_pk_row()
    check_offline()
    print("104_46 exact identities: PASS")
    print("Gamma quotient diagnostics (exact rationals, decimal display only):")
    for r, q in rows:
        print(f"  r={r:2d}  Q_gamma={float(q):.12f}")
    print("translation blindness and off-line quartet: PASS")


if __name__ == "__main__":
    main()
