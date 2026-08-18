#!/usr/bin/env python3
"""Exact genus-2 controls for Phase 107 diagonal sensitivity.

This script isolates the falsifier:
whether the primitive diagonal entries scale with genus g, rather than
being frozen at the elliptic values -2 and -2 q^n.

It includes two independent genus-2 controls:

1. a supersingular Artin--Schreier curve over F_2
      y^2 + y = x^5 + x^2
   whose n=8 line saturates the Weil/Hodge determinant exactly;
2. an ordinary hyperelliptic curve over F_3
      y^2 = x^5 + x
   which tests a non-extremal ordinary configuration.
"""

from __future__ import annotations


GENUS = 2


def poly_trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_divmod(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    work = a[:]
    quotient = [0] * max(1, len(a) - len(b) + 1)
    inv_lc = pow(b[-1], -1, p)
    while len(work) >= len(b) and work != [0]:
        coeff = (work[-1] * inv_lc) % p
        shift = len(work) - len(b)
        quotient[shift] = coeff
        for i, value in enumerate(b):
            work[shift + i] = (work[shift + i] - coeff * value) % p
        poly_trim(work)
    return poly_trim(quotient), poly_trim(work)


def poly_mod(a: list[int], modulus: list[int], p: int) -> list[int]:
    return poly_divmod(a, modulus, p)[1]


def find_irreducible(p: int, degree: int) -> list[int]:
    if degree == 1:
        return [1, 1]
    start = p**degree
    end = p ** (degree + 1)
    for raw in range(start, end):
        coeffs = []
        value = raw
        for _ in range(degree + 1):
            coeffs.append(value % p)
            value //= p
        if coeffs[-1] != 1:
            continue
        candidate = poly_trim(coeffs)
        reducible = False
        for d in range(1, degree // 2 + 1):
            for raw_divisor in range(p**d, p ** (d + 1)):
                divisor = []
                value = raw_divisor
                for _ in range(d + 1):
                    divisor.append(value % p)
                    value //= p
                if divisor[-1] != 1:
                    continue
                _, remainder = poly_divmod(candidate, poly_trim(divisor), p)
                if remainder == [0]:
                    reducible = True
                    break
            if reducible:
                break
        if not reducible:
            return candidate
    raise RuntimeError(f"no irreducible polynomial found for F_{p}^{degree}")


def int_to_coeffs(x: int, p: int) -> list[int]:
    if x == 0:
        return [0]
    coeffs = []
    while x:
        coeffs.append(x % p)
        x //= p
    return poly_trim(coeffs)


def coeffs_to_int(coeffs: list[int], p: int) -> int:
    out = 0
    factor = 1
    for coeff in coeffs:
        out += coeff * factor
        factor *= p
    return out


def gf_add(a: int, b: int, p: int) -> int:
    aa = int_to_coeffs(a, p)
    bb = int_to_coeffs(b, p)
    n = max(len(aa), len(bb))
    out = [0] * n
    for i in range(n):
        out[i] = ((aa[i] if i < len(aa) else 0) + (bb[i] if i < len(bb) else 0)) % p
    return coeffs_to_int(poly_trim(out), p)


def gf_mul(a: int, b: int, p: int, modulus: list[int]) -> int:
    aa = int_to_coeffs(a, p)
    bb = int_to_coeffs(b, p)
    out = [0] * (len(aa) + len(bb) - 1)
    for i, x in enumerate(aa):
        for j, y in enumerate(bb):
            out[i + j] = (out[i + j] + x * y) % p
    return coeffs_to_int(poly_mod(poly_trim(out), modulus, p), p)


def gf_pow(a: int, e: int, p: int, modulus: list[int]) -> int:
    out = 1
    while e:
        if e & 1:
            out = gf_mul(out, a, p, modulus)
        a = gf_mul(a, a, p, modulus)
        e >>= 1
    return out


def count_artin_schreier_f2(n: int) -> int:
    p = 2
    modulus = find_irreducible(p, n)
    qn = p**n
    total = 1
    for x in range(qn):
        rhs = gf_add(gf_pow(x, 5, p, modulus), gf_pow(x, 2, p, modulus), p)
        trace = 0
        cur = rhs
        for _ in range(n):
            trace ^= cur & 1
            cur = gf_mul(cur, cur, p, modulus)
        total += 2 if trace == 0 else 0
    return total


def count_hyperelliptic_odd(n: int) -> int:
    p = 3
    modulus = find_irreducible(p, n)
    qn = p**n
    squares = {gf_mul(y, y, p, modulus) for y in range(qn)}
    total = 1
    for x in range(qn):
        rhs = gf_add(gf_pow(x, 5, p, modulus), x, p)
        if rhs == 0:
            total += 1
        elif rhs in squares:
            total += 2
    return total


def run_curve(name: str, q: int, max_n: int, counter) -> list[tuple[int, int, int, int, float]]:
    rows = []
    print(name)
    print(" n       N_n       a_n       det(G_n^0)        Weil bound")
    for n in range(1, max_n + 1):
        qn = q**n
        n_points = counter(n)
        a_n = qn + 1 - n_points
        determinant = 4 * GENUS * GENUS * qn - a_n * a_n
        bound = 2 * GENUS * (qn ** 0.5)
        assert determinant >= 0
        assert abs(a_n) <= bound + 1e-12
        rows.append((n, n_points, a_n, determinant, bound))
        print(
            f"{n:2d} {n_points:9d} {a_n:9d} {determinant:15d}"
            f" {bound:15.6f}"
        )
    print()
    return rows


def main() -> None:
    supersingular = run_curve(
        "Supersingular genus-2 control: y^2 + y = x^5 + x^2 over F_2",
        2,
        8,
        count_artin_schreier_f2,
    )
    assert supersingular[-1][0] == 8
    assert supersingular[-1][2] == 64
    assert supersingular[-1][3] == 0

    ordinary = run_curve(
        "Ordinary genus-2 control: y^2 = x^5 + x over F_3",
        3,
        6,
        count_hyperelliptic_odd,
    )
    _, n1, _, _, _ = ordinary[0]
    _, n2, _, _, _ = ordinary[1]
    s1 = 3 + 1 - n1
    s2 = 3**2 + 1 - n2
    e2 = (s1 * s1 - s2) // 2
    assert e2 % 3 != 0
    print(f"Ordinary witness: e2 = {e2}, so e2 mod 3 = {e2 % 3} != 0.")
    print("Genus-2 diagonal sensitivity controls passed.")


if __name__ == "__main__":
    main()
