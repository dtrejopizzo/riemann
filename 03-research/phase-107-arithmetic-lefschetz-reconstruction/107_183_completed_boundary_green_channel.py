#!/home/trabajo/miniforge3/bin/python
"""High-precision falsifier for the completed boundary Green channel."""

from mpmath import mp


mp.dps = 80


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def direct_channel(s):
    return -mp.diff(xi, s) / xi(s)


def decomposed_channel(s):
    finite = -mp.diff(mp.zeta, s) / mp.zeta(s)
    archimedean = -1 / s - 1 / (s - 1) + mp.log(mp.pi) / 2 - mp.digamma(s / 2) / 2
    return finite + archimedean


comparison_points = [
    mp.mpf("2"),
    mp.mpf("2.5"),
    mp.mpc(2, 3),
    mp.mpc(3, -2),
]
decomposition_errors = [abs(direct_channel(s) - decomposed_channel(s)) for s in comparison_points]
decomposition_ok = max(decomposition_errors) < mp.mpf("1e-65")

symmetry_points = [
    mp.mpc("2.0", "0.7"),
    mp.mpc("-1.0", "2.0"),
    mp.mpc("0.3", "3.0"),
    mp.mpc("0.8", "1.4"),
]
symmetry_errors = [abs(direct_channel(1 - s) + direct_channel(s)) for s in symmetry_points]
symmetry_ok = max(symmetry_errors) < mp.mpf("1e-65")

# The completed channel remains finite near 0 and 1 and obeys the same
# antisymmetry; individual terms in the decomposition are singular there.
endpoint_ok = True
endpoint_values = []
for exponent in [8, 12, 16, 20]:
    eps = mp.mpf(10) ** (-exponent)
    left = direct_channel(eps)
    right = direct_channel(1 - eps)
    row_ok = mp.isfinite(left) and mp.isfinite(right) and abs(left + right) < mp.mpf("1e-50")
    endpoint_ok = endpoint_ok and row_ok
    endpoint_values.append(max(abs(left), abs(right)))

verdict = all([decomposition_ok, symmetry_ok, endpoint_ok])

print(f"DECOMPOSITION_POINTS: {len(comparison_points)}")
print(f"MAX_DECOMPOSITION_ERROR: {mp.nstr(max(decomposition_errors), 12)}")
print(f"COMPLETED_CHANNEL_DECOMPOSITION: {'YES' if decomposition_ok else 'NO'}")
print(f"FUNCTIONAL_SYMMETRY_POINTS: {len(symmetry_points)}")
print(f"MAX_FUNCTIONAL_SYMMETRY_ERROR: {mp.nstr(max(symmetry_errors), 12)}")
print(f"FUNCTIONAL_SYMMETRY_ODD: {'YES' if symmetry_ok else 'NO'}")
print(f"ENDPOINT_CANCELLATION: {'YES' if endpoint_ok else 'NO'}")
print(f"MAX_ENDPOINT_SAMPLE_MAGNITUDE: {mp.nstr(max(endpoint_values), 12)}")
print("COMPLETED_BOUNDARY_GREEN_CHANNEL: CONSTRUCTED")
print("MELLIN_TEST_DISTRIBUTION: NOT_CONSTRUCTED")
print("GLOBAL_DIVISOR_REALIZATION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
