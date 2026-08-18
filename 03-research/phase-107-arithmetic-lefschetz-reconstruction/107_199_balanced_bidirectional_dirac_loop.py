#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the balanced bidirectional local Dirac loop."""

import numpy as np
from mpmath import mp


mp.dps = 70
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))
ASYMMETRIC_EXPONENTS = (mp.mpf(1) / 3, mp.mpf(1) / 4, mp.mpf(2) / 3)

determinant_ok = True
transpose_balance_ok = True
eigenvalue_ok = True
green_connection_ok = True
asymmetric_determinant_collision_ok = True
asymmetric_balance_rejected = True
max_det_error = mp.mpf(0)
max_green_error = mp.mpf(0)

for p in PRIMES:
    for s in PARAMETERS:
        q = mp.power(p, -s)
        half = mp.power(p, -s / 2)
        matrix = mp.matrix([[0, half], [half, 0]])
        identity = mp.eye(2)

        determinant = mp.det(identity - matrix)
        det_error = abs(determinant - (1 - q))
        max_det_error = max(max_det_error, det_error)
        determinant_ok &= det_error < mp.mpf("1e-65")
        transpose_balance_ok &= matrix == matrix.T

        numpy_matrix = np.array(
            [[0, complex(half)], [complex(half), 0]], dtype=np.complex128
        )
        eigenvalues = sorted(np.linalg.eigvals(numpy_matrix), key=lambda z: z.real)
        expected = sorted([-complex(half), complex(half)], key=lambda z: z.real)
        eigenvalue_ok &= max(
            abs(left - right) for left, right in zip(eigenvalues, expected)
        ) < 1e-12

        def determinant_at(w):
            weight = mp.power(p, -w / 2)
            return mp.det(mp.eye(2) - mp.matrix([[0, weight], [weight, 0]]))

        computed_green = mp.diff(lambda w: mp.log(determinant_at(w)), s)
        expected_green = mp.log(p) * q / (1 - q)
        green_error = abs(computed_green - expected_green)
        max_green_error = max(max_green_error, green_error)
        green_connection_ok &= green_error < mp.mpf("1e-60")

        for theta in ASYMMETRIC_EXPONENTS:
            left = mp.power(q, theta)
            right = mp.power(q, 1 - theta)
            asymmetric = mp.matrix([[0, left], [right, 0]])
            asymmetric_determinant_collision_ok &= abs(
                mp.det(identity - asymmetric) - (1 - q)
            ) < mp.mpf("1e-60")
            asymmetric_balance_rejected &= asymmetric != asymmetric.T


verdict = all(
    [
        determinant_ok,
        transpose_balance_ok,
        eigenvalue_ok,
        green_connection_ok,
        asymmetric_determinant_collision_ok,
        asymmetric_balance_rejected,
    ]
)

print(f"REAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"BALANCED_DIRAC_MATRICES_TESTED: {len(PRIMES) * len(PARAMETERS)}")
print(f"MAX_LOCAL_DETERMINANT_ERROR: {mp.nstr(max_det_error, 8)}")
print(f"TRANSPOSE_BALANCED_HALF_WEIGHT: {'YES' if transpose_balance_ok else 'NO'}")
print(f"DIRAC_EIGENVALUES_PLUS_MINUS_HALF_WEIGHT: {'YES' if eigenvalue_ok else 'NO'}")
print(f"MAX_GREEN_CONNECTION_ERROR: {mp.nstr(max_green_error, 8)}")
print(f"LOCAL_GREEN_CONNECTION_RECOVERED: {'YES' if green_connection_ok else 'NO'}")
print(f"ASYMMETRIC_DETERMINANT_COLLISIONS_FOUND: {'YES' if asymmetric_determinant_collision_ok else 'NO'}")
print(f"ASYMMETRIC_BALANCE_REJECTED: {'YES' if asymmetric_balance_rejected else 'NO'}")
print("BALANCED_BIDIRECTIONAL_DIRAC_LOOP: CONSTRUCTED")
print("SECONDARY_CURRENT_AND_GLOBAL_GLUE: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
