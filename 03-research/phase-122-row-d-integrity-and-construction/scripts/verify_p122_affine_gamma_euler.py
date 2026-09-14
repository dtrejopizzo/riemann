#!/usr/bin/env python3
"""Finite and high-precision checks for P122.024.

These checks reproduce algebra and special-function identities only; they
are not evidence for row (d).
"""

import mpmath as mp


def gauss_determinant_error(p: int, a: mp.mpf) -> mp.mpf:
    det_a = mp.sqrt(2 * mp.pi) / mp.gamma(a)
    product = mp.mpf(1)
    for r in range(p):
        b = (r + a) / p
        det_b = mp.sqrt(2 * mp.pi) / mp.gamma(b)
        product *= p ** (mp.mpf("0.5") - b) * det_b
    return abs(det_a - product)


def digamma_anomaly_error(p: int, a: mp.mpf) -> mp.mpf:
    rhs = mp.log(p) + sum(mp.digamma((r + a) / p) for r in range(p)) / p
    return abs(mp.digamma(a) - rhs)


def check_affine_relation(p: int, k: int) -> bool:
    # Basis index after V_p S and after S^p V_p.
    return p * ((k + 1) + 1) - 1 == (p * (k + 1) - 1) + p


def path_inner(m: int, n: int) -> mp.mpf:
    last = min(m, n) - 1
    return sum(
        mp.log(mp.mpf(j + 1) / mp.mpf(j)) for j in range(1, last + 1)
    )


def main() -> None:
    mp.mp.dps = 80
    tolerance = mp.mpf("1e-70")
    for p in (2, 3, 5, 11):
        assert all(check_affine_relation(p, k) for k in range(20))
        for a in (mp.mpf(1) / 4, mp.mpf(2) / 3, mp.mpf(7) / 5):
            det_error = gauss_determinant_error(p, a)
            psi_error = digamma_anomaly_error(p, a)
            assert det_error < tolerance, (p, a, det_error)
            assert psi_error < tolerance, (p, a, psi_error)
        print(f"p={p}: affine relation and Gauss/digamma anomaly PASS")
    for m, n in ((2, 3), (3, 11), (5, 7), (11, 11)):
        inner = path_inner(m, n)
        assert abs(inner - mp.log(min(m, n))) < tolerance
        norm_difference = mp.log(m) + mp.log(n) - 2 * inner
        assert abs(norm_difference - abs(mp.log(m) - mp.log(n))) < tolerance
    print("successor-path logarithmic Gram: PASS")
    print("PASS: P122 affine Gamma--Euler identities")


if __name__ == "__main__":
    main()
