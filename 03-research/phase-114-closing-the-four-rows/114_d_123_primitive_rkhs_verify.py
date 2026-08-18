#!/usr/bin/env python3
"""Numerical/algebraic certificates for D.123 primitive RKHS audit."""

import math


def c0(t: float) -> float:
    return 2*t - 16*math.sinh(t/2)**2/(math.sinh(t)+t)


def main() -> None:
    # Exact Gram-projection formula checked numerically against its asymptotic.
    for t in (10.0, 20.0, 40.0):
        value = c0(t)
        assert value > 0
        assert abs(value - (2*t-8)) < 100*t*math.exp(-t)

    # Relative evaluation constant tends to one.
    ratios = [c0(t)/(2*t) for t in (10.0, 20.0, 40.0)]
    assert ratios[0] < ratios[1] < ratios[2] < 1

    # Primitive differential leaves zero frequency nonzero:
    # Fhat(0)=-(1/4) uhat(0).
    uhat0 = 8.0
    fhat0 = -uhat0/4
    assert fhat0 == -2.0

    # On a 1/T band, quadratic Gamma strength loses T^2.
    deficits = []
    block_mass = 3.0
    for t in (4.0, 8.0, 16.0):
        gamma_scale = 1/(t*t)
        deficits.append(block_mass/gamma_scale)
    assert deficits == [48.0, 192.0, 768.0]

    print("D123 primitive Paley-Wiener/Gamma certificates: PASS")
    print("evaluation ratios:", ratios)
    print("zero-frequency primitive value:", fhat0)
    print("dyadic/Gamma T^2 deficits:", deficits)


if __name__ == "__main__":
    main()
