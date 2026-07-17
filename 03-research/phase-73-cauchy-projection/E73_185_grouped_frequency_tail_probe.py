#!/usr/bin/env python3
import math
import sys

import numpy as np
from scipy.special import polygamma

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import (  # noqa: E402
    cauchy_rows,
    eval_modes,
    integrate_modes,
    packet_modes,
    setup,
)
from E73_184_high_order_wr_tail_probe import (  # noqa: E402
    accelerated_wra,
    f_derivative_bound,
    odd_power_tail,
)


def grouped_f_derivative_bound(const, linear, order, L):
    # F(y)=exp(y/2)B(y)-B(0). For order >= 1 the constant subtraction vanishes.
    # If B(y)=sum c_w exp(iwy)+y sum l_w exp(iwy), then
    # F^(s)(y)=sum exp((1/2+iw)y)[c_w lambda^s + s l_w lambda^(s-1) + y l_w lambda^s].
    total = 0.0
    omegas = set(const) | set(linear)
    for om in omegas:
        lam = 0.5 + 1j * om
        c = const.get(om, 0j)
        ell = linear.get(om, 0j)
        if order == 0:
            a = c
            b = ell
        else:
            a = c * (lam**order) + order * ell * (lam ** (order - 1))
            b = ell * (lam**order)
        total += abs(a) + L * abs(b)
    return math.exp(L / 2.0) * total


def tail_bound_grouped(const, linear, L, r_terms, order):
    s = order + 1
    return grouped_f_derivative_bound(const, linear, s, L) * odd_power_tail(r_terms, s + 1)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.185 grouped-frequency WR tail probe")
    print("Compares binomial absolute derivative bound with direct frequency-grouped bound.")
    print(" lam     L gamma row K actualB oldB newB gainB ratioNewB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (32, 36)]:
        _h_model, idx, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:2]:
            plane = cauchy_rows(-1j * gamma, d)
            for j in range(2):
                const, linear = packet_modes(plane[j], idx, d, xi, L)
                for order in [4, 6, 8, 10]:
                    r_terms = 80
                    ref = accelerated_wra(const, linear, L, 8000, order)
                    val = accelerated_wra(const, linear, L, r_terms, order)
                    actual = abs(ref - val)
                    old = f_derivative_bound(const, linear, order + 1, L) * odd_power_tail(r_terms, order + 2)
                    new = tail_bound_grouped(const, linear, L, r_terms, order)
                    ratio = actual / max(new, 1e-300)
                    gain = old / max(new, 1e-300)
                    print(
                        f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d} {order:2d}"
                        f" {bexp(actual, L):8.2f} {bexp(old, L):6.2f}"
                        f" {bexp(new, L):6.2f} {bexp(gain, L):6.2f}"
                        f" {bexp(ratio, L):10.2f}"
                    )


if __name__ == "__main__":
    run()
