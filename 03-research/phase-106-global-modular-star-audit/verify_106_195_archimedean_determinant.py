#!/usr/bin/env python3
"""Numerical checks for 106.195 (not used in its proofs).

Only the Python standard library is used.  The zeta determinant is
checked through its renormalized finite-product limit.
"""

import math


def finite_product_log(s, size):
    """log product_{m<size}(2m+s), evaluated by the Gamma identity."""
    a = s / 2.0
    return size * math.log(2.0) + math.lgamma(size + a) - math.lgamma(a)


def renormalized_log_det(s, size):
    """Finite-part approximation to log det_zeta(N_Gamma+s-1/2)."""
    a = s / 2.0
    divergent = (
        size * math.log(2.0)
        + (size + a - 0.5) * math.log(size)
        - size
    )
    return finite_product_log(s, size) - divergent + (0.5 - a) * math.log(2.0)


def closed_log_det(s):
    a = s / 2.0
    return 0.5 * math.log(2.0 * math.pi) + (0.5 - a) * math.log(2.0) - math.lgamma(a)


def arch_factor(s):
    return 0.5 * s * (s - 1.0) * math.pi ** (-s / 2.0) * math.gamma(s / 2.0)


def determinant_arch_factor(s):
    polar = s * (s - 1.0)
    return math.sqrt(math.pi) * (2.0 * math.pi) ** (-s / 2.0) * polar / math.exp(closed_log_det(s))


def heat_trace(u, terms=10000):
    return sum(math.exp(-u * (2 * m + 0.5)) for m in range(terms))


def closed_heat_trace(u):
    return math.exp(-u / 2.0) / (1.0 - math.exp(-2.0 * u))


def main():
    samples = [0.37, 0.5, 1.75, 4.0, 7.25]
    size = 2_000_000
    det_err = max(abs(renormalized_log_det(s, size) - closed_log_det(s)) for s in samples)
    arch_err = max(abs(determinant_arch_factor(s) / arch_factor(s) - 1) for s in samples)
    heat_err = max(
        abs(heat_trace(u) / closed_heat_trace(u) - 1)
        for u in [0.17, 1.2, 4.5]
    )
    print("max finite-part log-determinant error:", f"{det_err:.3e}")
    print("max relative archimedean factor error:", f"{arch_err:.3e}")
    print("max relative heat-trace error:", f"{heat_err:.3e}")


if __name__ == "__main__":
    main()
