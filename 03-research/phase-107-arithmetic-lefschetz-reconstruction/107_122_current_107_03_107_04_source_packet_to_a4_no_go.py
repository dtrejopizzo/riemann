#!/usr/bin/env python3
"""No-go gate from the full current 107.03/107.04 source packet to A4.

The current finite connected source packet is

    (p, (1,p), p^(-1/2), log p)

and is tested here against the Frobenius coefficient a_p^flat used by
A4 on a fixed real atlas.
"""

from __future__ import annotations

import json
import math
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")
GENUS2_LABEL = "y^2 + y = x^5 + x^2 over Q"


@dataclass(frozen=True)
class Row:
    name: str
    packet: tuple[object, ...]
    a_p_flat: int


def run_sage_json() -> dict[str, object]:
    code = r"""
from sage.all import EllipticCurve, QQ, PolynomialRing, pari
import json

rows = []
for label, probe in [('14a1', 2), ('14a5', 7), ('21a1', 7), ('20a1', 2), ('36a4', 2)]:
    E = EllipticCurve(label)
    rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "a_p": int(E.ap(probe)),
    })

R = PolynomialRing(QQ, 'x')
x = R.gen()
g2 = str(pari([x**5 + x**2, 1]).genus2red())
print(json.dumps({"elliptic_rows": rows, "genus2red": g2}))
"""
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def current_packet(prime: int) -> tuple[object, ...]:
    return (prime, (1, prime), prime ** (-0.5), math.log(prime))


def parse_genus2red(raw: str) -> Row:
    factor_match = re.search(r"Mat\(\[(\d+),\s*(-?\d+)\]\)", raw)
    if factor_match is None:
        raise AssertionError(f"unexpected genus2red output: {raw}")
    bad_prime, _ = map(int, factor_match.groups())
    return Row(
        name=f"{GENUS2_LABEL}@{bad_prime}",
        packet=current_packet(bad_prime),
        a_p_flat=0,
    )


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


def certify_supersingular_genus2() -> None:
    q = 2
    g = 2
    n = 8
    n_points = count_artin_schreier_f2(n)
    a_n = q**n + 1 - n_points
    determinant = 4 * g * g * (q**n) - a_n * a_n
    assert a_n == 64
    assert determinant == 0


def build_rows() -> list[Row]:
    payload = run_sage_json()
    rows = [
        Row(
            name=entry["name"],
            packet=current_packet(entry["prime"]),
            a_p_flat=entry["a_p"],
        )
        for entry in payload["elliptic_rows"]
    ]
    rows.append(parse_genus2red(payload["genus2red"]))
    return rows


def main() -> None:
    certify_supersingular_genus2()
    rows = build_rows()
    assert len(rows) == 6

    fibers: dict[tuple[object, ...], list[Row]] = {}
    for row in rows:
        fibers.setdefault(row.packet, []).append(row)

    collisions = []
    for packet, bucket in fibers.items():
        ap_values = {row.a_p_flat for row in bucket}
        if len(ap_values) > 1:
            collisions.append((packet, bucket))

    print("Fixed atlas:")
    for row in rows:
        print(f"  {row.name}: packet={row.packet}, a_p_flat={row.a_p_flat}")

    print()
    print("Supersingular certification:")
    print("  genus-2 control y^2 + y = x^5 + x^2 over F_2 satisfies a_8 = 64 and det = 0")

    print()
    if collisions:
        print("VERDICT: NO")
        print("Reason: a_p_flat is not a function of the full current 107.03/107.04 finite source packet.")
        for packet, bucket in collisions:
            print(f"  Collision at packet {packet}:")
            for row in bucket:
                print(f"    {row.name} -> a_p_flat={row.a_p_flat}")
    else:
        print("VERDICT: YES")
        print("Reason: a_p_flat is constant on every current-source-packet fiber of the fixed atlas.")


if __name__ == "__main__":
    main()
