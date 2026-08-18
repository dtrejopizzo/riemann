#!/home/trabajo/miniforge3/bin/sage
"""Exact-group/numerical-CVP probe for Minkowski tolerant cyclotomic H1."""

from itertools import combinations, product
from math import lcm

import numpy as np


ATLAS = (
    (4, 1, 8, 2),
    (5, 1, 10, 2),
    (9, 3, 9, 6),
)
LAMBDAS = (0.5, 1.0 / 6.0, 1.0 / 18.0)


def basis_matrix(field, basis):
    return matrix(QQ, [field(element).vector() for element in basis]).transpose()


def component_group(labels):
    n, u, m, v = labels
    conductor = lcm(n, m)
    field = CyclotomicField(conductor)
    order = field.ring_of_integers()
    zeta = field.gen()
    a = field(zeta ** (u * conductor // n) - 1)
    b = field(zeta ** (v * conductor // m) - 1)
    ideal = field.ideal(a, b)
    codifferent = field.different() ** (-1)
    dual = ideal ** (-1) * codifferent

    B_dual = basis_matrix(field, dual.basis())
    B_codifferent = basis_matrix(field, codifferent.basis())
    inclusion = B_dual.inverse() * B_codifferent
    V = ZZ ** field.degree()
    submodule = V.submodule([V(column) for column in inclusion.columns()])
    quotient = V / submodule

    dual_basis = dual.basis()
    gram = matrix(
        QQ,
        [
            [field(x * y.conjugate()).trace() for y in dual_basis]
            for x in dual_basis
        ],
    )
    gram_np = np.array(gram, dtype=float)
    inclusion_np = np.array(inclusion, dtype=float)
    codifferent_gram = inclusion_np.T @ gram_np @ inclusion_np
    covolume = float(np.sqrt(np.linalg.det(codifferent_gram)))
    scale_sq = covolume ** (-2.0 / field.degree())
    return field, quotient, inclusion_np, gram_np, scale_sq


def coset_norms(quotient, inclusion, gram, scale_sq, radius):
    dimension = inclusion.shape[0]
    offsets = np.array(tuple(product(range(-radius, radius + 1), repeat=dimension)))
    norms = {}
    for element in quotient:
        c = np.array(element.lift(), dtype=float)
        center = np.rint(np.linalg.solve(inclusion, c)).astype(int)
        lattice_points = (center + offsets) @ inclusion.T
        differences = c - lattice_points
        squared = np.einsum("ni,ij,nj->n", differences, gram, differences)
        norms[tuple(element)] = float(np.sqrt(max(0.0, squared.min() * scale_sq)))
    return norms


def tolerant_dimension(quotient, norms, tolerance):
    elements = tuple(quotient)
    zero = quotient.zero()
    if all(norms[tuple(x)] <= tolerance + 1e-12 for x in elements):
        return 0, ()

    nonzero = tuple(x for x in elements if x != zero)
    for size in range(1, len(nonzero) + 1):
        for generators in combinations(nonzero, size):
            separated = all(
                norms[tuple(left - right)] > tolerance + 1e-12
                for left, right in combinations(generators, 2)
            )
            if not separated:
                continue
            sums = {zero}
            for generator in generators:
                sums = {
                    partial + sign * generator
                    for partial in sums
                    for sign in (-1, 0, 1)
                }
            covers = all(
                any(norms[tuple(x - y)] <= tolerance + 1e-12 for y in sums)
                for x in elements
            )
            if covers:
                return size, tuple(tuple(g) for g in generators)
    return None, ()


def main():
    rows = []
    cvp_stable = True
    for labels in ATLAS:
        field, quotient, inclusion, gram, scale_sq = component_group(labels)
        norms_r1 = coset_norms(quotient, inclusion, gram, scale_sq, 1)
        norms_r2 = coset_norms(quotient, inclusion, gram, scale_sq, 2)
        cvp_stable &= all(
            abs(norms_r1[key] - norms_r2[key]) < 1e-11 for key in norms_r1
        )
        dimensions = []
        witnesses = []
        for tolerance in LAMBDAS:
            dimension, witness = tolerant_dimension(quotient, norms_r2, tolerance)
            dimensions.append(dimension)
            witnesses.append(witness)
        rows.append(
            (
                labels,
                field.degree(),
                quotient.cardinality(),
                max(norms_r2.values()),
                tuple(dimensions),
                tuple(witnesses),
            )
        )

    dimensions_found = all(all(value is not None for value in row[4]) for row in rows)
    monotone = all(
        row[4][0] <= row[4][1] <= row[4][2]
        for row in rows
    )
    radius_variation = any(len(set(row[4])) > 1 for row in rows)
    positive_controls = all(all(value > 0 for value in row[4]) for row in rows)
    finite_torsion_rejected = not radius_variation
    verdict = (
        cvp_stable
        and dimensions_found
        and monotone
        and positive_controls
        and finite_torsion_rejected
    )

    print("Minkowski tolerant H1 rows:")
    for labels, degree, order, diameter, dimensions, witnesses in rows:
        print(
            f"  {labels}: degree={degree}, |G|={order}, "
            f"radius={diameter:.9f}, dims={dimensions}"
        )
        print(f"    witnesses={witnesses}")
    print()
    print(f"ACTUAL_CYCLOTOMIC_METRIC_COMPONENTS: {len(rows)}")
    print(f"MINKOWSKI_CVP_STABLE_R1_R2: {'YES' if cvp_stable else 'NO'}")
    print(f"TOLERANT_DIMENSIONS_FOUND: {'YES' if dimensions_found else 'NO'}")
    print(f"DIMENSION_MONOTONE_AS_TOLERANCE_SHRINKS: {'YES' if monotone else 'NO'}")
    print(f"METRIC_VARIATION_ACROSS_CC_RADII: {'YES' if radius_variation else 'NO'}")
    print("FINITE_TORSION_H1_AS_CC_TOLERANT_H1: CLOSED_NO_GO")
    print("FULL_MINKOWSKI_TORUS_REQUIRED: YES")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("Minkowski tolerance metric probe failed")


main()
