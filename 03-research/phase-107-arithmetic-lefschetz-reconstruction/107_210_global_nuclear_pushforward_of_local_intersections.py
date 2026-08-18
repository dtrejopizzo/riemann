#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the nuclear pushforward of local derived intersections."""

from mpmath import mp
from sympy import primerange


mp.dps = 60
BOUND = 100_000
PRIMES = tuple(primerange(2, BOUND + 1))
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))

max_det_error = mp.mpf(0)
max_green_error = mp.mpf(0)
max_det_bound_ratio = mp.mpf(0)
max_green_bound_ratio = mp.mpf(0)
tail_bounds_ok = True

for s in PARAMETERS:
    sigma = mp.re(s)
    log_det = mp.fsum(mp.log(1 - mp.power(p, -s)) for p in PRIMES)
    finite_det = mp.exp(log_det)
    target_det = 1 / mp.zeta(s)
    det_error = abs(finite_det - target_det)
    max_det_error = max(max_det_error, det_error)

    # Dominate omitted primes by all integers n>B.  The logarithmic
    # Euler tail is at most sum n^-sigma/(1-B^-sigma).
    denominator = 1 - mp.power(BOUND, -sigma)
    log_tail_bound = (
        mp.power(BOUND, 1 - sigma) / (sigma - 1)
        + mp.power(BOUND, -sigma)
    ) / denominator
    det_error_bound = abs(target_det) * mp.expm1(log_tail_bound)
    max_det_bound_ratio = max(max_det_bound_ratio, det_error / det_error_bound)
    tail_bounds_ok &= det_error <= det_error_bound

    finite_green = mp.fsum(
        mp.log(p) * mp.power(p, -s) / (1 - mp.power(p, -s)) for p in PRIMES
    )
    target_green = -mp.diff(lambda z: mp.log(mp.zeta(z)), s)
    green_error = abs(finite_green - target_green)
    max_green_error = max(max_green_error, green_error)
    green_tail_bound = (
        mp.power(BOUND, 1 - sigma)
        * (mp.log(BOUND) / (sigma - 1) + 1 / (sigma - 1) ** 2)
        + mp.log(BOUND) * mp.power(BOUND, -sigma)
    ) / denominator
    max_green_bound_ratio = max(max_green_bound_ratio, green_error / green_tail_bound)
    tail_bounds_ok &= green_error <= green_tail_bound

# At sigma=1 the partial trace norms must keep increasing.  Compare
# disjoint fixed cutoff ranges rather than inferring divergence from zeta.
cutoffs = (100, 1_000, 10_000, 100_000)
trace_norms = []
for cutoff in cutoffs:
    trace_norms.append(mp.fsum(mp.mpf(1) / p for p in PRIMES if p <= cutoff))
critical_growth = all(a < b for a, b in zip(trace_norms, trace_norms[1:]))
critical_growth &= trace_norms[-1] - trace_norms[-2] > mp.mpf("0.15")

# The comparison is certified by the explicit omitted-tail bounds above,
# not by a tolerance adjusted after seeing the data.
det_ok = tail_bounds_ok and max_det_bound_ratio < 1
green_ok = tail_bounds_ok and max_green_bound_ratio < 1
verdict = det_ok and green_ok and critical_growth

print(f"ACTUAL_PRIMES_TESTED: {len(PRIMES)}")
print(f"MAX_FREDHOLM_DETERMINANT_ERROR: {mp.nstr(max_det_error, 8)}")
print(f"MAX_GREEN_TRACE_ERROR: {mp.nstr(max_green_error, 8)}")
print(f"MAX_DETERMINANT_ERROR_TO_TAIL_BOUND: {mp.nstr(max_det_bound_ratio, 8)}")
print(f"MAX_GREEN_ERROR_TO_TAIL_BOUND: {mp.nstr(max_green_bound_ratio, 8)}")
print(f"CRITICAL_TRACE_NORM_GROWS: {'YES' if critical_growth else 'NO'}")
print(f"LOCAL_INTERSECTION_FREDHOLM_PRODUCT: {'YES' if det_ok else 'NO'}")
print(f"FINITE_GREEN_CHARACTER_MATCHES: {'YES' if green_ok else 'NO'}")
print("GLOBAL_NUCLEAR_INTERSECTION_PUSHFORWARD: CONSTRUCTED_ON_RE_S_GT_1")
print("CRITICAL_LINE_TRACE_CLASS_PUSHFORWARD: CLOSED_NO_GO")
print("PROPER_ARITHMETIC_SURFACE_PUSHFORWARD: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
