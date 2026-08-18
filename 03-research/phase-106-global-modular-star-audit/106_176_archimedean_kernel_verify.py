#!/usr/bin/env python3
"""Numerical audit of the archimedean kernel identity in 106.176."""

from __future__ import annotations

import math


def main() -> None:
    errors = []
    for j in range(1, 1001):
        t = 0.002 + 0.02 * j
        k_plus = 1.0 / (2.0 * math.sinh(t / 2.0))
        k_minus = 1.0 / (2.0 * math.cosh(t / 2.0))
        gamma_density = math.exp(-t / 2.0) / (1.0 - math.exp(-2.0 * t))
        errors.append(abs((k_plus + k_minus) - 2.0 * gamma_density))
    print(f"max |K_+ + K_- - 2 g_Gamma|  {max(errors):.3e}")


if __name__ == "__main__":
    main()
