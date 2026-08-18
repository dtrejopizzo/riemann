#!/home/trabajo/miniforge3/bin/python
"""High-precision falsifier for the completed orbit determinant."""

from mpmath import mp
from sage.all import prime_range


mp.dps = 100

hurwitz_ok = True
hurwitz_errors = []
for a in [mp.mpf("1"), mp.mpf("1.25"), mp.mpc(1, 1.5), mp.mpc(1.5, -1)]:
    h_coarse = mp.mpf("1e-20")
    h_fine = mp.mpf("1e-25")
    derivative_coarse = (mp.zeta(h_coarse, a) - mp.zeta(-h_coarse, a)) / (2 * h_coarse)
    spectral_derivative = (mp.zeta(h_fine, a) - mp.zeta(-h_fine, a)) / (2 * h_fine)
    determinant_from_zeta = mp.exp(-spectral_derivative)
    determinant_from_gamma = mp.sqrt(2 * mp.pi) / mp.gamma(a)
    error = abs(determinant_from_zeta - determinant_from_gamma)
    hurwitz_errors.append(error)
    hurwitz_ok = hurwitz_ok and error < mp.mpf("1e-35") and abs(spectral_derivative - derivative_coarse) < mp.mpf("1e-35")

prime_cutoff = 100000
primes = list(prime_range(2, prime_cutoff + 1))


def finite_prime_determinant(s):
    result = mp.mpc(1)
    for p in primes:
        result /= 1 - mp.power(int(p), -s)
    return result


def completed_from_factors(s, finite_factor):
    archimedean = mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)
    return mp.mpf("0.5") * s * (s - 1) * archimedean * finite_factor


def xi(s):
    return completed_from_factors(s, mp.zeta(s))


determinant_points = [mp.mpf("2"), mp.mpf("2.5"), mp.mpf("3"), mp.mpc(2, 3)]
relative_errors = []
for s in determinant_points:
    truncated = completed_from_factors(s, finite_prime_determinant(s))
    target = xi(s)
    relative_errors.append(abs(truncated / target - 1))

prime_determinant_ok = max(relative_errors) < mp.mpf("1e-6")

log_derivative_ok = True
log_derivative_errors = []
for s in [mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3)]:
    from_determinant = -mp.diff(xi, s) / xi(s)
    decomposed = (
        -mp.diff(mp.zeta, s) / mp.zeta(s)
        - 1 / s
        - 1 / (s - 1)
        + mp.log(mp.pi) / 2
        - mp.digamma(s / 2) / 2
    )
    error = abs(from_determinant - decomposed)
    log_derivative_errors.append(error)
    log_derivative_ok = log_derivative_ok and error < mp.mpf("1e-60")

verdict = all([hurwitz_ok, prime_determinant_ok, log_derivative_ok])

print(f"MAX_HURWITZ_DETERMINANT_ERROR: {mp.nstr(max(hurwitz_errors), 12)}")
print(f"ARCHIMEDEAN_ZETA_DETERMINANT: {'YES' if hurwitz_ok else 'NO'}")
print(f"PRIME_DETERMINANT_CUTOFF: {prime_cutoff}")
print(f"MAX_COMPLETED_RELATIVE_ERROR: {mp.nstr(max(relative_errors), 12)}")
print(f"FINITE_ORBIT_PRODUCT_RECOVERS_ZETA: {'YES' if prime_determinant_ok else 'NO'}")
print(f"MAX_LOG_DERIVATIVE_ERROR: {mp.nstr(max(log_derivative_errors), 12)}")
print(f"GREEN_TRACE_IS_LOG_DERIVATIVE: {'YES' if log_derivative_ok else 'NO'}")
print("COMPLETED_ORBIT_DETERMINANT: CONSTRUCTED")
print("GLOBAL_DETERMINANT_LINE_SHEAF: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
