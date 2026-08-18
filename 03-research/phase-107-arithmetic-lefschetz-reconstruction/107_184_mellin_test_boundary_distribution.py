#!/home/trabajo/miniforge3/bin/python
"""Independent contour/sum falsifier for the Mellin boundary distribution."""

import math

import numpy as np
from sage.all import prime_range


prime_cutoff = 100
primes = np.array([int(p) for p in prime_range(2, prime_cutoff + 1)], dtype=float)
contour_real_part = 2.0
mesh_points = 32769
max_prime_power_exponent = 39
tests = [
    (math.log(2), 0.30, 20.0),
    (math.log(5), 0.35, 18.0),
    (math.log(30), 0.50, 14.0),
]


def contour_value(mu, sigma, height):
    ordinates = np.linspace(-height, height, mesh_points)
    s = contour_real_part + 1j * ordinates
    transform = (
        math.sqrt(2 * math.pi)
        * sigma
        * np.exp(mu * s + (sigma**2) * (s**2) / 2)
    )
    channel = np.zeros(mesh_points, dtype=complex)
    for p in primes:
        local_character = np.exp(-s * math.log(p))
        channel += math.log(p) * local_character / (1 - local_character)
    return np.trapezoid(transform * channel, ordinates) / (2 * math.pi)


def prime_power_value(mu, sigma):
    total = 0.0
    for p in primes:
        for exponent in range(1, max_prime_power_exponent + 1):
            orbit_length = exponent * math.log(p)
            test_value = math.exp(-((orbit_length - mu) ** 2) / (2 * sigma**2))
            total += math.log(p) * test_value
    return total


errors = []
imaginary_parts = []
for index, (mu, sigma, height) in enumerate(tests, start=1):
    contour = contour_value(mu, sigma, height)
    prime_sum = prime_power_value(mu, sigma)
    error = abs(contour - prime_sum)
    errors.append(error)
    imaginary_parts.append(abs(contour.imag))
    print(
        f"TEST={index}_MU={mu:.12g}_SIGMA={sigma}_HEIGHT={height}"
        f"_CONTOUR_REAL={contour.real:.15g}_PRIME_SUM={prime_sum:.15g}"
        f"_ERROR={error:.6g}_OK={'YES' if error < 1e-7 else 'NO'}"
    )

contour_sum_match = max(errors) < 1e-7
reality_ok = max(imaginary_parts) < 1e-10
verdict = contour_sum_match and reality_ok

print(f"PRIME_CUTOFF_FIXED: {prime_cutoff}")
print(f"CONTOUR_REAL_PART_FIXED: {contour_real_part}")
print(f"MESH_POINTS_FIXED: {mesh_points}")
print(f"MAX_CONTOUR_PRIME_SUM_ERROR: {max(errors):.12g}")
print(f"CONTOUR_VALUES_REAL: {'YES' if reality_ok else 'NO'}")
print(f"MELLIN_INVERSION_RECOVERS_PRIME_DISTRIBUTION: {'YES' if contour_sum_match else 'NO'}")
print("MELLIN_TEST_DISTRIBUTION: CONSTRUCTED")
print("GREEN_CURRENT_REALIZATION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
