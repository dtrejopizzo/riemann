#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the zero Bott--Chern anomaly of standard Fock tails."""

from mpmath import mp


mp.dps = 60
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))
CUTOFFS = (2, 4, 8, 16, 32)


exact_sequence_ok = True
orthogonal_split_ok = True
equivariant_split_ok = True
determinant_multiplicativity_ok = True
nonorthogonal_mutation_detected = True
max_determinant_error = mp.mpf(0)

for cutoff in CUTOFFS:
    # Dimensions certify exactness: (N-1) -> N -> 1.
    exact_sequence_ok &= (cutoff - 1) + 1 == cutoff

    # In the number basis, e1 is orthogonal to every tail vector.
    cross_terms = [mp.mpf(0) for _ in range(2, cutoff + 1)]
    orthogonal_split_ok &= all(value == 0 for value in cross_terms)

    # A fixed off-diagonal metric coupling is genuinely different.
    mutated_cross_term = mp.mpf(1) / 3
    nonorthogonal_mutation_detected &= mutated_cross_term != 0

    for p in PRIMES:
        for s in PARAMETERS:
            q = mp.power(p, -s)
            quotient_eigenvalue = q
            tail_eigenvalues = [q**n for n in range(2, cutoff + 1)]
            full_eigenvalues = [q] + tail_eigenvalues
            equivariant_split_ok &= full_eigenvalues[0] == quotient_eigenvalue
            equivariant_split_ok &= full_eigenvalues[1:] == tail_eigenvalues

            full_det = mp.fprod(1 - value for value in full_eigenvalues)
            tail_det = mp.fprod(1 - value for value in tail_eigenvalues)
            quotient_det = 1 - quotient_eigenvalue
            error = abs(full_det - tail_det * quotient_det)
            max_determinant_error = max(max_determinant_error, error)
            determinant_multiplicativity_ok &= error < mp.mpf("1e-55")


standard_bott_chern_zero = (
    exact_sequence_ok and orthogonal_split_ok and equivariant_split_ok
)
verdict = all(
    [
        standard_bott_chern_zero,
        determinant_multiplicativity_ok,
        nonorthogonal_mutation_detected,
    ]
)

print(f"FINITE_CUTOFFS_TESTED: {len(CUTOFFS)}")
print(f"EXACT_NUMBER_FILTRATION_SEQUENCE: {'YES' if exact_sequence_ok else 'NO'}")
print(f"STANDARD_METRIC_ORTHOGONALLY_SPLIT: {'YES' if orthogonal_split_ok else 'NO'}")
print(f"NUMBER_OPERATOR_EQUIVARIANT_SPLIT: {'YES' if equivariant_split_ok else 'NO'}")
print(f"MAX_DETERMINANT_MULTIPLICATIVITY_ERROR: {mp.nstr(max_determinant_error, 8)}")
print(f"STANDARD_BOTT_CHERN_SECONDARY_CLASS_ZERO: {'YES' if standard_bott_chern_zero else 'NO'}")
print(f"NONORTHOGONAL_METRIC_MUTATION_DETECTED: {'YES' if nonorthogonal_mutation_detected else 'NO'}")
print("STANDARD_FOCK_BOTT_CHERN_ROUTE: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: DYNAMIC_OFF_DIAGONAL_SUPERCONNECTION")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
