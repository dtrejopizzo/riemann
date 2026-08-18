#!/usr/bin/env python3
"""Numerical/algebraic certificates for D.94 determinant connection."""

import mpmath as mp


def main() -> None:
    mp.mp.dps = 60

    # Finite prime: radial derivative of the determinant logarithm.
    p = mp.mpf(5)
    sigma = mp.mpf("0.5")
    tau = mp.mpf("0.37")
    theta = mp.mpf("0.21")
    logp = mp.log(p)
    r = p ** (-sigma)
    angle = theta - tau * logp

    poisson_minus_one = (1 - r * r) / (
        1 - 2 * r * mp.cos(angle) + r * r
    ) - 1
    closed = logp * poisson_minus_one
    series = 2 * logp * mp.nsum(
        lambda k: r**k * mp.cos(k * angle), [1, mp.inf]
    )
    assert mp.almosteq(closed, series, rel_eps=mp.mpf("1e-50"))

    # Difference quotient checks -d_sigma Phi, where
    # Phi=-log|1-p^{-s}e^{i theta}|^2.
    def phi(sig: mp.mpf) -> mp.mpf:
        z = 1 - p ** (-(sig + 1j * tau)) * mp.e ** (1j * theta)
        return -mp.log(abs(z) ** 2)

    normal_derivative = -mp.diff(phi, sigma)
    assert mp.almosteq(normal_derivative, closed, rel_eps=mp.mpf("1e-48"))

    # Gamma: exact digamma formula versus oscillator series.
    gamma_closed = mp.log(mp.pi) - mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * tau / 2))
    m0 = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    ell = mp.nsum(
        lambda j: (tau**2) /
        ((j + mp.mpf(1) / 4) * (4 * (j + mp.mpf(1) / 4) ** 2 + tau**2)),
        [0, mp.inf],
    )
    assert mp.almosteq(gamma_closed, m0 - ell, rel_eps=mp.mpf("1e-48"))

    # Direct normal derivative of the completed archimedean determinant.
    def log_gamma_factor(sig: mp.mpf) -> mp.mpf:
        s = sig + 1j * tau
        return mp.log(abs(mp.pi ** (-s / 2) * mp.gamma(s / 2)) ** 2)

    gamma_normal = -mp.diff(log_gamma_factor, sigma)
    assert mp.almosteq(gamma_normal, gamma_closed, rel_eps=mp.mpf("1e-48"))

    print("D94 Quillen normal-connection certificates: PASS")
    print("prime closed/series/normal:", closed, series, normal_derivative)
    print("Gamma closed/oscillator/normal:", gamma_closed, m0 - ell, gamma_normal)


if __name__ == "__main__":
    main()
