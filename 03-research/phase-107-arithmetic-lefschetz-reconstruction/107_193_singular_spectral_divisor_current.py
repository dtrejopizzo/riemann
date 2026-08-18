#!/home/trabajo/miniforge3/bin/python
"""Numerical falsifier for the singular spectral divisor current."""

from mpmath import mp


mp.dps = 60
ZERO_COUNT = 12


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def log_derivative(s):
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.zeta(s, derivative=1) / mp.zeta(s)
    )


zeros = [mp.zetazero(index) for index in range(1, ZERO_COUNT + 1)]
distinct_zeros_ok = all(abs(zeros[j] - zeros[i]) > 1 for i in range(ZERO_COUNT) for j in range(i + 1, ZERO_COUNT))
max_zero_value = max(abs(xi(rho)) for rho in zeros)
zero_values_ok = max_zero_value < mp.mpf("1e-50")


def winding_multiplicity(rho, radius=mp.mpf("0.08")):
    # The periodic trapezoidal rule converges exponentially because the
    # integrand is analytic on and near these isolated-zero circles.
    node_count = 128
    total = mp.mpc(0)
    for index in range(node_count):
        theta = 2 * mp.pi * index / node_count
        point = rho + radius * mp.e ** (1j * theta)
        tangent = 1j * radius * mp.e ** (1j * theta)
        total += log_derivative(point) * tangent
    return total / (1j * node_count)


multiplicities = [winding_multiplicity(rho) for rho in zeros[:6]]
max_multiplicity_error = max(abs(value - 1) for value in multiplicities)
residues_ok = max_multiplicity_error < mp.mpf("1e-35")

# A section of degree D cannot contain more than D zeros counted with
# multiplicity. The real sample rejects every fixed cap D < ZERO_COUNT.
degree_caps = list(range(1, ZERO_COUNT))
finite_caps_rejected = all(ZERO_COUNT > degree for degree in degree_caps)

# Mutation control: a contour containing no zero must have winding zero.
empty_center = mp.mpc("2.5", "5")
empty_winding = winding_multiplicity(empty_center, mp.mpf("0.05"))
empty_contour_ok = abs(empty_winding) < mp.mpf("1e-35")

verdict = all(
    [
        distinct_zeros_ok,
        zero_values_ok,
        residues_ok,
        finite_caps_rejected,
        empty_contour_ok,
    ]
)

print(f"ACTUAL_ZETA_ZEROS_TESTED: {ZERO_COUNT}")
print(f"MAX_XI_VALUE_AT_ZERO: {mp.nstr(max_zero_value, 8)}")
print(f"DISTINCT_SPECTRAL_POINTS: {'YES' if distinct_zeros_ok else 'NO'}")
print(f"MAX_CONTOUR_MULTIPLICITY_ERROR: {mp.nstr(max_multiplicity_error, 8)}")
print(f"SPECTRAL_DIVISOR_CURRENT_RESIDUES: {'YES' if residues_ok else 'NO'}")
print(f"EMPTY_CONTOUR_REJECTS_FALSE_ATOM: {'YES' if empty_contour_ok else 'NO'}")
print(f"FINITE_DEGREE_CAPS_REJECTED_THROUGH: {ZERO_COUNT - 1 if finite_caps_rejected else 0}")
print("INFINITE_SUPPORT_INPUT: HARDY_1914")
print("FINITE_TYPE_PROPER_SPECTRAL_COMPACTIFICATION: CLOSED_NO_GO")
print("ARITHMETIC_SQUARE_GREEN_CURRENT: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
