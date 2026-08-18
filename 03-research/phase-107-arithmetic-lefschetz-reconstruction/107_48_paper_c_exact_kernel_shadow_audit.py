#!/usr/bin/env python3
"""Exact audit for the finite exact-kernel shadow of Paper C.

This verifier audits a finite algebraic shadow of the kernel logic in
`107_11`.  It checks the precise pattern required of any future
realization map:

1. designated radical generators map to torsion classes;
2. after tensoring with R, those radical generators vanish;
3. non-radical witnesses survive in the free part and therefore do not
   vanish after realification;
4. the only real kernel is the span of the designated radical
   generators.

The scope is a finite exact-kernel shadow, not the full Picard/Jacobian
realization itself.
"""

from __future__ import annotations

from fractions import Fraction


def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def row_reduce(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    work = [row[:] for row in matrix]
    if not work:
        return work, []
    rows = len(work)
    cols = len(work[0])
    pivots: list[int] = []
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if work[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        work[r], work[pivot] = work[pivot], work[r]
        factor = work[r][c]
        work[r] = [value / factor for value in work[r]]
        for i in range(rows):
            if i == r or work[i][c] == 0:
                continue
            multiple = work[i][c]
            work[i] = [
                left - multiple * right
                for left, right in zip(work[i], work[r])
            ]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return work, pivots


def nullspace_basis(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = row_reduce(matrix)
    if not matrix:
        return []
    cols = len(matrix[0])
    free_cols = [c for c in range(cols) if c not in pivots]
    basis: list[list[Fraction]] = []
    for free in free_cols:
        vector = [Fraction(0) for _ in range(cols)]
        vector[free] = Fraction(1)
        for row_index, pivot_col in enumerate(pivots):
            vector[pivot_col] = -reduced[row_index][free]
        basis.append(vector)
    return basis


def is_in_span(vector: list[Fraction], basis: list[list[Fraction]]) -> bool:
    if not basis:
        return all(value == 0 for value in vector)
    rows = len(vector)
    cols = len(basis)
    system = [[basis[c][r] for c in range(cols)] + [vector[r]] for r in range(rows)]
    reduced, pivots = row_reduce(system)
    for row in reduced:
        if all(value == 0 for value in row[:-1]) and row[-1] != 0:
            return False
    return True


def torsion_image(vector: list[int], torsion_moduli: list[int]) -> tuple[int, ...]:
    return tuple(value % modulus for value, modulus in zip(vector, torsion_moduli))


def main() -> None:
    # Domain basis:
    # e0 = radical jet r0
    # e1 = radical jet r1
    # e2 = non-radical prime witness
    # e3 = non-radical diagonal witness
    # e4 = non-radical archimedean witness
    # e5 = non-radical mixed witness
    torsion_moduli = [2, 3]

    torsion_part = [
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
    ]
    free_part = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
    ]

    radical_vectors_int = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, -1, 0, 0, 0, 0],
    ]
    nonradical_witnesses_int = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
    ]

    free_matrix = [[Fraction(value) for value in row] for row in free_part]
    radical_basis = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
    ]

    print("Radical-to-torsion audit")
    radical_checks = 0
    for vector in radical_vectors_int:
        torsion = torsion_image(mat_vec(torsion_part, vector), torsion_moduli)
        free = mat_vec(free_matrix, [Fraction(v) for v in vector])
        assert all(entry == 0 for entry in free)
        radical_checks += 1
        print(f" vector={vector}  torsion={torsion}  free={free}")

    print("\nNon-radical survival audit")
    witness_checks = 0
    for vector in nonradical_witnesses_int:
        free = mat_vec(free_matrix, [Fraction(v) for v in vector])
        assert any(entry != 0 for entry in free)
        witness_checks += 1
        print(f" vector={vector}  free={free}")

    print("\nReal-kernel audit")
    kernel_basis = nullspace_basis(free_matrix)
    assert len(kernel_basis) == 2
    for basis_vector in kernel_basis:
        assert is_in_span(basis_vector, radical_basis)
    real_kernel_checks = len(kernel_basis)

    test_vectors = [
        [Fraction(3), Fraction(-2), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(2), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
    ]
    for vector in test_vectors:
        free = mat_vec(free_matrix, vector)
        in_radical = is_in_span(vector, radical_basis)
        if in_radical:
            assert all(entry == 0 for entry in free)
        else:
            assert any(entry != 0 for entry in free)
        real_kernel_checks += 1
        print(f" test={vector}  in_radical={in_radical}  free={free}")

    print("\nAdditivity audit")
    additivity_checks = 0
    left = [1, 0, 1, 0, 0, 0]
    right = [0, 1, 0, 1, 0, 1]
    summed = [a + b for a, b in zip(left, right)]
    torsion_sum = tuple(
        (a + b) % modulus
        for a, b, modulus in zip(
            torsion_image(mat_vec(torsion_part, left), torsion_moduli),
            torsion_image(mat_vec(torsion_part, right), torsion_moduli),
            torsion_moduli,
        )
    )
    torsion_direct = torsion_image(mat_vec(torsion_part, summed), torsion_moduli)
    free_sum = [
        a + b
        for a, b in zip(
            mat_vec(free_matrix, [Fraction(v) for v in left]),
            mat_vec(free_matrix, [Fraction(v) for v in right]),
        )
    ]
    free_direct = mat_vec(free_matrix, [Fraction(v) for v in summed])
    assert torsion_sum == torsion_direct
    assert free_sum == free_direct
    additivity_checks += 2
    print(f" left={left} right={right} summed={summed}")
    print(f" torsion={torsion_direct} free={free_direct}")

    print("\nAll exact Paper C kernel-shadow checks passed.")
    print(
        "Verified "
        f"{radical_checks} radical-to-torsion checks, "
        f"{witness_checks} non-radical survival checks, "
        f"{real_kernel_checks} real-kernel checks, and "
        f"{additivity_checks} additivity checks."
    )


if __name__ == "__main__":
    main()
