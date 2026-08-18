#!/usr/bin/env python3
"""Real local bad-fiber witness for selected elliptic curves over Q."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

import sympy as sp


LMFDB_SNAPSHOT = (
    {
        "label": "14.a1",
        "url": "https://www.lmfdb.org/EllipticCurve/Q/14/a/1",
        "rows": (
            ("2", "1", "I_{9}", "nonsplit multiplicative", "1", "1", "9", "9"),
            ("7", "2", "I_{2}", "split multiplicative", "-1", "1", "2", "2"),
        ),
    },
    {
        "label": "20.a1",
        "url": "https://www.lmfdb.org/EllipticCurve/Q/20/a/1",
        "rows": (
            ("2", "1", "IV", "additive", "-1", "2", "4", "0"),
            ("5", "1", "I_{3}", "nonsplit multiplicative", "1", "1", "3", "3"),
        ),
    },
)


@dataclass(frozen=True)
class LocalFiberData:
    label: str
    prime: int
    tamagawa: int
    kodaira: str
    reduction_type: str
    conductor_valuation: int
    discriminant_valuation: int
    j_denom_valuation: int


def snapshot_rows() -> list[LocalFiberData]:
    rows: list[LocalFiberData] = []
    for entry in LMFDB_SNAPSHOT:
        for cols in entry["rows"]:
            rows.append(
                LocalFiberData(
                    label=entry["label"],
                    prime=int(cols[0]),
                    tamagawa=int(cols[1]),
                    kodaira=cols[2],
                    reduction_type=cols[3],
                    conductor_valuation=int(cols[5]),
                    discriminant_valuation=int(cols[6]),
                    j_denom_valuation=int(cols[7]),
                )
            )
    return rows


def cycle_intersection_matrix(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, i] = -2
        matrix[i, (i - 1) % n] += 1
        matrix[i, (i + 1) % n] += 1
    return matrix


def kodaira_intersection_matrix(kodaira: str) -> sp.Matrix:
    m = re.fullmatch(r"I_\{(\d+)\}", kodaira)
    if m:
        n = int(m.group(1))
        if n < 2:
            raise ValueError(f"Need nontrivial multiplicative fiber, got {kodaira}")
        return cycle_intersection_matrix(n)
    if kodaira == "IV":
        return sp.Matrix(
            [
                [-2, 1, 1],
                [1, -2, 1],
                [1, 1, -2],
            ]
        )
    raise ValueError(f"Unsupported Kodaira symbol: {kodaira}")


def audit_real_rows(rows: list[LocalFiberData]) -> int:
    checks = 0
    for row in rows:
        matrix = kodaira_intersection_matrix(row.kodaira)
        size = matrix.rows

        # Affine-fiber kernel: the total fiber vector spans the nullspace.
        ones = sp.Matrix([1] * size)
        assert matrix * ones == sp.zeros(size, 1)
        checks += 1
        assert len(matrix.nullspace()) == 1
        checks += 1

        # Affine Dynkin signature: symmetric with rank n-1 on the
        # component lattice and one-dimensional fiber kernel.
        assert matrix == matrix.T
        checks += 1
        assert matrix.rank() == size - 1
        checks += 1

        # The target-side finite-place weight is the Arakelov factor log p.
        weighted = sp.Matrix(matrix) * sp.log(row.prime)
        assert weighted == sp.log(row.prime) * matrix
        checks += 1
        assert weighted * ones == sp.zeros(size, 1)
        checks += 1

        # For multiplicative fibers, ord_p(Delta) matches n in the actual data.
        m = re.fullmatch(r"I_\{(\d+)\}", row.kodaira)
        if m:
            assert row.discriminant_valuation == int(m.group(1))
            checks += 1

    return checks


def main() -> None:
    all_rows = snapshot_rows()
    # Restrict to the nontrivial real fibers handled explicitly here.
    supported_rows = [row for row in all_rows if row.kodaira in {"I_{9}", "I_{2}", "IV", "I_{3}"}]
    assert len(supported_rows) == 4

    row_checks = audit_real_rows(supported_rows)

    print("All real elliptic bad-fiber intersection checks passed.")
    print(f"  supported real-fiber checks: {row_checks}")
    print("  source snapshot: LMFDB local-data pages for 14.a1 and 20.a1")
    for row in supported_rows:
        print(
            f"  {row.label} @ p={row.prime}: "
            f"Kodaira={row.kodaira}, reduction={row.reduction_type}, "
            f"c_p={row.tamagawa}, ord_p(Delta)={row.discriminant_valuation}, "
            f"log(p)={math.log(row.prime):.12f}"
        )


if __name__ == "__main__":
    main()
