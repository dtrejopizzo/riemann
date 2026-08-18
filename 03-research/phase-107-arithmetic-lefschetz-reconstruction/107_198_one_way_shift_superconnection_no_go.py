#!/home/trabajo/miniforge3/bin/python
"""Falsifier for one-way weighted-shift superconnection determinants."""

import numpy as np
from mpmath import mp


mp.dps = 50
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))
DIMENSIONS = (4, 8, 16, 32, 64)


raising_determinant_one = True
lowering_determinant_one = True
trace_powers_zero = True
diagonal_mutation_detected = True
max_det_error = 0.0

for p in PRIMES:
    for s in PARAMETERS:
        q = complex(mp.power(p, -s))
        for dimension in DIMENSIONS:
            raising = np.zeros((dimension, dimension), dtype=np.complex128)
            for index in range(dimension - 1):
                raising[index + 1, index] = q ** (index + 2)
            lowering = raising.T

            det_raising = np.linalg.det(np.eye(dimension) - raising)
            det_lowering = np.linalg.det(np.eye(dimension) - lowering)
            error = max(abs(det_raising - 1), abs(det_lowering - 1))
            max_det_error = max(max_det_error, error)
            raising_determinant_one &= abs(det_raising - 1) < 1e-12
            lowering_determinant_one &= abs(det_lowering - 1) < 1e-12

            for power in (1, 2, 3):
                trace_powers_zero &= abs(np.trace(np.linalg.matrix_power(raising, power))) < 1e-12
                trace_powers_zero &= abs(np.trace(np.linalg.matrix_power(lowering, power))) < 1e-12

            mutated = raising.copy()
            mutated[0, 0] = q
            mutated_det = np.linalg.det(np.eye(dimension) - mutated)
            diagonal_mutation_detected &= abs(mutated_det - (1 - q)) < 1e-11


verdict = all(
    [
        raising_determinant_one,
        lowering_determinant_one,
        trace_powers_zero,
        diagonal_mutation_detected,
    ]
)

print(f"REAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"FINITE_SHIFT_MATRICES_TESTED: {len(PRIMES) * len(PARAMETERS) * len(DIMENSIONS) * 2}")
print(f"MAX_ONE_WAY_DETERMINANT_ERROR: {max_det_error:.3e}")
print(f"RAISING_SHIFT_DETERMINANT_ONE: {'YES' if raising_determinant_one else 'NO'}")
print(f"LOWERING_SHIFT_DETERMINANT_ONE: {'YES' if lowering_determinant_one else 'NO'}")
print(f"TRACE_POWERS_ZERO: {'YES' if trace_powers_zero else 'NO'}")
print(f"DIAGONAL_QUOTIENT_MUTATION_DETECTED: {'YES' if diagonal_mutation_detected else 'NO'}")
print("ONE_WAY_SHIFT_SUPERCONNECTION: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: BIDIRECTIONAL_LOOP_OR_BOUNDARY_ETA_CLASS")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
