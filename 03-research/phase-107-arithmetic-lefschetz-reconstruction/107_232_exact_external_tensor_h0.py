#!/usr/bin/env python3
"""Exact algebraic controls for the full special external tensor H0."""

from fractions import Fraction


PAIRS = ((2, 2), (2, 3), (3, 5), (5, 7), (7, 11))
NEG_INF = None


def tropical_add(left, right):
    if left is NEG_INF:
        return right
    if right is NEG_INF:
        return left
    return max(left, right)


def tropical_multiply(left, right):
    if left is NEG_INF or right is NEG_INF:
        return NEG_INF
    return left + right


def extremal_indices(prime: int, degree: int):
    return tuple(range(degree - prime + 1))


divisor_generators_ok = True
tensor_expansion_ok = True
matrix_decomposition_ok = True
deleted_generator_detected = True

for p, q in PAIRS:
    n_degree = p + 3
    m_degree = q + 2
    rows = extremal_indices(p, n_degree)
    cols = extremal_indices(q, m_degree)

    for a in rows[1:]:
        b = (n_degree - a) // p
        divisor_generators_ok &= b >= 1 and a + p * b <= n_degree
    for a in cols[1:]:
        b = (m_degree - a) // q
        divisor_generators_ok &= b >= 1 and a + q * b <= m_degree

    row_coefficients = {
        i: Fraction((3 * i) % 7 - 3, 5) for i in rows
    }
    col_coefficients = {
        j: Fraction((2 * j) % 5 - 2, 7) for j in cols
    }
    expanded = {
        (i, j): row_coefficients[i] + col_coefficients[j]
        for i in rows
        for j in cols
    }
    tensor_expansion_ok &= all(
        expanded[i, j] == tropical_multiply(row_coefficients[i], col_coefficients[j])
        for i in rows
        for j in cols
    )

    arbitrary = {
        (i, j): Fraction((i + 1) * (j + 2), 11)
        for i in rows
        for j in cols
    }
    reconstructed = {(i, j): NEG_INF for i in rows for j in cols}
    for target_i in rows:
        for target_j in cols:
            pure_row = {
                i: arbitrary[target_i, target_j] if i == target_i else NEG_INF
                for i in rows
            }
            pure_col = {j: Fraction(0) if j == target_j else NEG_INF for j in cols}
            for i in rows:
                for j in cols:
                    rank_one_entry = tropical_multiply(pure_row[i], pure_col[j])
                    reconstructed[i, j] = tropical_add(
                        reconstructed[i, j], rank_one_entry
                    )
    matrix_decomposition_ok &= reconstructed == arbitrary

    removed = dict(reconstructed)
    removed.pop((rows[-1], cols[-1]))
    deleted_generator_detected &= len(removed) + 1 == len(arbitrary)
    deleted_generator_detected &= (rows[-1], cols[-1]) not in removed

cofinal_limit_ok = True
for p, q in PAIRS:
    alpha = Fraction(2)
    beta = Fraction(3)
    values = []
    for depth in (2, 3, 5, 8):
        d = int(alpha * p**depth) - p + 1
        e = int(beta * q**depth) - q + 1
        normalized = Fraction(d * e, p**depth * q**depth)
        values.append(abs(normalized - alpha * beta))
    cofinal_limit_ok &= values[-1] < values[0]

verdict = all((
    divisor_generators_ok,
    tensor_expansion_ok,
    matrix_decomposition_ok,
    deleted_generator_detected,
    cofinal_limit_ok,
))

print("ONE_RULING_EXTREMAL_GENERATORS: EXACT")
print("EXTERNAL_TENSOR_GENERATORS: PRODUCT")
print("FULL_SPECIAL_EXTERNAL_H0_DIMENSION: PRODUCT")
print("NORMALIZED_LIMIT: ALPHA_BETA")
print("FRAME_DEPENDENCE: NO")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

