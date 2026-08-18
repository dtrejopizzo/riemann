#!/usr/bin/env python3
"""Exact checks for 104_50 (integers and Fraction only)."""

from fractions import Fraction as Q
from math import comb, factorial, gcd


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(a, c):
    return [c * x for x in a]


def derivative(a):
    return [Q(i) * a[i] for i in range(1, len(a))] or [Q(0)]


def primitive(a):
    return [Q(0)] + [a[i] / Q(i + 1) for i in range(len(a))]


def x_times(a):
    return [Q(0)] + list(a)


def compose_scale(a, s):
    return [a[i] * s**i for i in range(len(a))]


def laguerre(m, alpha=0):
    return [Q((-1) ** j * comb(m + alpha, m - j), factorial(j))
            for j in range(m + 1)]


def poly_eval(a, x):
    ans = Q(0)
    for coefficient in reversed(a):
        ans = ans * x + coefficient
    return ans


def check_conditional_palm():
    # Formal logarithmic weights are rational; no approximation to logs is used.
    towers = [(Q(2), 2), (Q(3), 1)]  # (ell_p, exponent a_p)
    marks = [(ell, Q(k) * ell) for ell, exponent in towers
             for k in range(1, exponent + 1)]
    total = sum((ell * exponent for ell, exponent in towers), Q(0))
    assert total == Q(7)

    f = lambda x: Q(1) + 2 * x + x * x
    g = lambda x: Q(3) - x + 2 * x * x
    jf = sum((ell * f(x) for ell, x in marks), Q(0))
    jg = sum((ell * g(x) for ell, x in marks), Q(0))
    ef = jf / total
    eg = jg / total
    assert total * total * ef * eg == jf * jg


def check_lcm_covariance():
    s = 2
    # Distinct towers: lcm(d,e)=de, hence the centered coefficient is zero.
    d, e = 4, 9
    lcm = d * e // gcd(d, e)
    assert Q(1, lcm**s) - Q(1, (d * e) ** s) == 0
    # Same tower: the coefficient is strictly positive.
    d, e = 4, 8
    lcm = d * e // gcd(d, e)
    assert Q(1, lcm**s) - Q(1, (d * e) ** s) > 0


def check_continuous_covariance():
    # f=x^(r-1), g=x^(q-1), so C_f(Y)=Y^r/r under Exp(epsilon).
    r, q, eps = 2, 3, Q(5, 2)
    covariance = Q(factorial(r + q) - factorial(r) * factorial(q),
                   r * q) / eps ** (r + q)
    assert covariance > 0


def check_bilinear_completion():
    probabilities = [Q(1, 6), Q(1, 3), Q(1, 2)]
    df = [Q(-2), Q(1), Q(3)]
    dg = [Q(4), Q(-1), Q(2)]
    tf, tg = Q(7, 5), Q(-3, 7)

    mean_df = sum((p * x for p, x in zip(probabilities, df)), Q(0))
    mean_dg = sum((p * x for p, x in zip(probabilities, dg)), Q(0))
    mf, mg = mean_df + tf, mean_dg + tg
    raw_z = sum((p * (x + tf) * (y + tg)
                 for p, x, y in zip(probabilities, df, dg)), Q(0))
    covariance = sum((p * (x - mean_df) * (y - mean_dg)
                      for p, x, y in zip(probabilities, df, dg)), Q(0))
    assert raw_z == covariance + mf * mg

    # A deterministic budget shift still leaves only a product of margins.
    af, ag = Q(11, 13), Q(5, 17)
    shifted_raw = sum((p * (x + tf - af) * (y + tg - ag)
                       for p, x, y in zip(probabilities, df, dg)), Q(0))
    assert shifted_raw == covariance + (mf - af) * (mg - ag)


def check_laguerre_anchors():
    s = Q(7, 3)
    for n in range(2, 12):
        fn = compose_scale(laguerre(n - 1, 1), s)

        # f'_n = -s sum_{k=1}^{n-1} f_k.
        rhs = [Q(0)]
        for k in range(1, n):
            rhs = add(rhs, compose_scale(laguerre(k - 1, 1), s))
        rhs = scale(rhs, -s)
        assert derivative(fn) == rhs

        # Integral f_n=(f_1-f_{n+1}+f_n)/s, with zero integration constant.
        f1 = compose_scale(laguerre(0, 1), s)
        fn1 = compose_scale(laguerre(n, 1), s)
        primitive_rhs = scale(add(add(f1, scale(fn1, -1)), fn), Q(1, 1) / s)
        assert primitive(fn) == primitive_rhs

        # Equivalent primitive  (1-L_n(sx))/s.
        one_minus_ln = add([Q(1)], scale(compose_scale(laguerre(n, 0), s), -1))
        assert primitive(fn) == scale(one_minus_ln, Q(1, 1) / s)

        # P_n+xP'_n-xP_n=n(P_{n+1}-P_n), the polynomial core of (34c).
        pn = laguerre(n - 1, 1)
        pn1 = laguerre(n, 1)
        lhs = add(add(pn, x_times(derivative(pn))), scale(x_times(pn), -1))
        rhs_flow = scale(add(pn1, scale(pn, -1)), Q(n))
        assert lhs == rhs_flow


def local_kernel(q):
    return [[q ** max(k, ell) - q ** (k + ell)
             for ell in (1, 2)] for k in (1, 2)]


def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def assert_psd_2x2(a):
    assert a[0][0] >= 0 and a[1][1] >= 0
    assert a[0][0] * a[1][1] - a[0][1] * a[1][0] >= 0


def check_shifted_gate():
    r = Q(2)
    b0 = Q(1)
    b1 = r + 1 / r
    b2 = r * r + 1 + 1 / (r * r)
    assert b1 == Q(5, 2) and b2 == Q(21, 4)

    # Local renewal at exponent two.
    weight1 = (r + 1 / r) * b1
    weight2 = (r * r + 1 / (r * r)) * b0
    assert weight1 + weight2 == 2 * b2
    pi1, pi2 = weight1 / (2 * b2), weight2 / (2 * b2)
    assert (pi1, pi2) == (Q(25, 42), Q(17, 42))
    variance = pi1 * pi2  # K takes the two adjacent integer values 1 and 2.
    assert variance == Q(425, 1764)
    assert Q(1, 4) - variance == Q(4, 441)

    # At p=5, s=2, 5^c=2, the two latent geometric colors have rational
    # rates.  This is their pre-conditioning covariance kernel, not an
    # asserted identity with the covariance of the conditioned selector.
    q_minus, q_plus = Q(2, 25), Q(1, 50)
    km, kp = local_kernel(q_minus), local_kernel(q_plus)
    assert_psd_2x2(km)
    assert_psd_2x2(kp)
    assert_psd_2x2(add_matrix(km, kp))

    # The latent-color covariance is not generally the covariance after
    # conditioning on the total exponent.  For f(k)=k and total exponent 2,
    # the three splits have latent scores 3,2,3 and all have positive mass.
    split_weights = [q_plus**2, q_minus * q_plus, q_minus**2]
    split_scores = [Q(3), Q(2), Q(3)]
    total_weight = sum(split_weights, Q(0))
    mean = sum(
        weight * score for weight, score in zip(split_weights, split_scores)
    ) / total_weight
    conditional_variance = sum(
        weight * (score - mean) ** 2
        for weight, score in zip(split_weights, split_scores)
    ) / total_weight
    assert conditional_variance > 0


def main():
    check_conditional_palm()
    check_lcm_covariance()
    check_continuous_covariance()
    check_bilinear_completion()
    check_laguerre_anchors()
    check_shifted_gate()
    print("PASS: exact second-order unit-Palm covariance checks")


if __name__ == "__main__":
    main()
