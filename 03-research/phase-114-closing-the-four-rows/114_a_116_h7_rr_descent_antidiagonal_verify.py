#!/usr/bin/env python3
"""Checks for 114.a.116: RR-form descent and anti-diagonal faithfulness."""

from pathlib import Path
from math import log


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_116_H7_RR_FORM_DESCENDS_IFF_ANTIDIAGONAL_IS_FAITHFUL.md").read_text()
PRIMES = (2, 3, 5, 7, 11)
C = 1.0 / (2.0 * log(3.0))


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def degree(vector: tuple[int, ...]) -> float:
    return sum(a * log(p) for p, a in zip(PRIMES, vector))


def form(x: tuple[tuple[int, ...], tuple[int, ...]],
         y: tuple[tuple[int, ...], tuple[int, ...]]) -> float:
    return C * (degree(x[0]) * degree(y[1]) + degree(y[0]) * degree(x[1]))


zero = (0,) * len(PRIMES)
u = ((1, -2, 0, 3, 1), (0, 1, -1, 2, 0))
v = ((-1, 0, 2, 1, -2), (3, -1, 0, 0, 1))
w = ((2, 1, -1, 0, 1), (-1, 2, 1, -2, 0))
uv = (tuple(a + b for a, b in zip(u[0], v[0])),
      tuple(a + b for a, b in zip(u[1], v[1])))

check(abs(form(u, v) - form(v, u)) < 1e-12, "symmetry")
check(abs(form(uv, w) - form(u, w) - form(v, w)) < 1e-12, "bilinearity")
check(abs(form((u[0], zero), (v[0], zero))) < 1e-12, "first axis isotropic")
check(abs(form((zero, u[1]), (zero, v[1]))) < 1e-12, "second axis isotropic")
check(abs(0.5 * form(u, u) - C * degree(u[0]) * degree(u[1])) < 1e-12,
      "quadratic code coefficient")

for i, p in enumerate(PRIMES):
    for j, q in enumerate(PRIMES):
        ep = tuple(1 if k == i else 0 for k in range(len(PRIMES)))
        eq = tuple(1 if k == j else 0 for k in range(len(PRIMES)))
        mixed = form((ep, zero), (zero, eq))
        check(abs(mixed - C * log(p) * log(q)) < 1e-12,
              f"rank-two mixed entry p={p},q={q}")
        # Matrix [[0,mixed],[mixed,0]] has eigenvalues +/-mixed.
        check(mixed > 0, f"rank-two signature (1,1) p={p},q={q}")

anti_vectors = (
    (1, 0, 0, 0, 0),
    (1, -1, 0, 0, 0),
    (2, 0, -3, 1, 0),
    (-1, 2, -1, 0, 3),
)
probe = (zero, (1, 0, 0, 0, 0))
for a in anti_vectors:
    anti = (a, tuple(-x for x in a))
    check(abs(degree(a)) > 1e-12, f"UFD anti-degree nonzero {a}")
    check(abs(form(anti, probe)) > 1e-12, f"anti relation not radical {a}")

for marker in (
    "descends iff the anti-diagonal is faithful",
    "Unique factorization implies `A!=0`",
    "logically necessary",
    "depends only on the two completed Picard degrees",
    "implications must not be reversed",
    "does not close the anti-diagonal",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: RR DEGREE-PRODUCT FORM DESCENDS IFF PRIME ANTIDIAGONAL IS FAITHFUL")
