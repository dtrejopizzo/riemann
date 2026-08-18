#!/usr/bin/env python3
"""Exact-scalar Hadamard phase counter-scaling for D.171."""
import math


def main():
    rows = []
    for exponent in (2, 4, 8, 12):
        eps = 10.0 ** (-exponent)
        cosine = -eps / (2 - eps)
        theta = math.acos(cosine)
        jplus2 = 1 + math.cos(theta)
        jminus2 = 1 - math.cos(theta)
        a2 = jplus2 / jminus2
        defect = 1 - a2
        y2 = math.sqrt(eps)
        capacity = y2 / defect
        assert math.isclose(a2, 1 - eps, rel_tol=2e-4, abs_tol=2e-16)
        assert 0.99 < jplus2 < 1.01 and 0.99 < jminus2 < 1.01
        assert y2 < 0.11
        rows.append((eps, theta, jplus2, jminus2, capacity))
    assert rows[-1][-1] > 9e5
    for eps, theta, jp, jm, cap in rows:
        print(f"eps={eps:.0e} theta={theta:.12g} "
              f"J+^2={jp:.12g} J-^2={jm:.12g} capacity={cap:.6g}")
    print("D171 Hadamard phase-defect counter-scaling: PASS")


if __name__ == "__main__":
    main()
