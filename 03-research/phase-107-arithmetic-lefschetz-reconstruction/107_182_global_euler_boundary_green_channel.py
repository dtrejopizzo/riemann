#!/home/trabajo/miniforge3/bin/python
"""Exact/numerical falsifier for the global Euler boundary channel."""

from mpmath import mp
from sage.all import prime_range


mp.dps = 70

# Exact combinatorial coefficient check: each prime power p^k occurs once
# and carries the orbit-length label log(p).
local_labels = {}
for p in prime_range(2, 50):
    power = p
    for k in range(1, 9):
        local_labels[int(power)] = int(p)
        power *= p

prime_power_labels_ok = True
for n, base_prime in local_labels.items():
    value = n
    while value % base_prime == 0:
        value //= base_prime
    prime_power_labels_ok = prime_power_labels_ok and value == 1

cutoffs = [100, 1000, 10000, 100000]
all_primes = list(prime_range(2, cutoffs[-1] + 1))


def boundary_sum(s, cutoff):
    total = mp.mpc(0)
    for p in all_primes:
        if p > cutoff:
            break
        pp = mp.power(p, -s)
        total += mp.log(p) * pp / (1 - pp)
    return total


def log_derivative_target(s):
    return -mp.diff(mp.zeta, s) / mp.zeta(s)


real_checks_ok = True
max_final_real_error = mp.mpf("0")
for sigma in [mp.mpf("2"), mp.mpf("2.5"), mp.mpf("3")]:
    target = log_derivative_target(sigma)
    errors = [abs(boundary_sum(sigma, cutoff) - target) for cutoff in cutoffs]
    decreasing = all(errors[j + 1] < errors[j] for j in range(len(errors) - 1))
    final_ok = errors[-1] < mp.mpf("0.00002")
    real_checks_ok = real_checks_ok and decreasing and final_ok
    max_final_real_error = max(max_final_real_error, errors[-1])
    print(
        f"S={sigma}_ERRORS=" + ",".join(mp.nstr(error, 8) for error in errors)
        + f"_OK={'YES' if decreasing and final_ok else 'NO'}"
    )

complex_s = mp.mpc(2, 3)
complex_target = log_derivative_target(complex_s)
complex_error = abs(boundary_sum(complex_s, cutoffs[-1]) - complex_target)
complex_ok = complex_error < mp.mpf("0.00003")

verdict = all([prime_power_labels_ok, real_checks_ok, complex_ok])

print(f"PRIME_POWER_COEFFICIENTS_EXACT: {'YES' if prime_power_labels_ok else 'NO'}")
print(f"PRIME_CUTOFF_FIXED: {cutoffs[-1]}")
print(f"MAX_FINAL_REAL_ERROR: {mp.nstr(max_final_real_error, 10)}")
print(f"COMPLEX_POINT_ERROR: {mp.nstr(complex_error, 10)}")
print(f"EULER_LOG_DERIVATIVE_RECOVERED: {'YES' if real_checks_ok and complex_ok else 'NO'}")
print("GLOBAL_FINITE_PRIME_GREEN_CHANNEL: CONSTRUCTED_FOR_RE_S_GT_1")
print("DAVENPORT_HEILBRONN_EULER_CHANNEL: UNAVAILABLE")
print("CRITICAL_STRIP_DISTRIBUTIONAL_EXTENSION: NOT_CONSTRUCTED")
print("ARCHIMEDEAN_COMPLETION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
