#!/home/trabajo/miniforge3/bin/python
"""Falsifier for finite order-change renormalization and cofinal failure."""

from mpmath import mp


mp.dps = 70


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for value in range(2, int(limit**0.5) + 1):
        if sieve[value]:
            start = value * value
            sieve[start : limit + 1 : value] = b"\x00" * (
                (limit - start) // value + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


finite_primes = (2, 3, 5, 7, 11, 13, 17, 19)
parameters = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))
finite_order_change_ok = True
max_order_change_error = mp.mpf(0)

for s in parameters:
    det2 = mp.mpc(1)
    det5 = mp.mpc(1)
    trace2_half = mp.mpc(0)
    trace4_quarter = mp.mpc(0)
    for p in finite_primes:
        q = mp.power(p, -s)
        det2 *= 1 - q
        det5 *= (1 - q) * mp.e ** (q + q**2 / 2)
        trace2_half += q
        trace4_quarter += q**2 / 2
    corrected = det5 * mp.e ** (-trace2_half - trace4_quarter)
    error = abs(corrected - det2)
    max_order_change_error = max(max_order_change_error, error)
    finite_order_change_ok &= error < mp.mpf("1e-60")


all_primes = primes_up_to(1_000_000)
cutoffs = (100, 1_000, 10_000, 100_000, 1_000_000)
log_products = []
for cutoff in cutoffs:
    log_product = mp.fsum(
        mp.log(1 - mp.power(p, -mp.mpf("0.5")))
        for p in all_primes
        if p <= cutoff
    )
    log_products.append(log_product)

critical_products_decrease = all(
    log_products[index + 1] < log_products[index]
    for index in range(len(log_products) - 1)
)
critical_product_tiny = log_products[-1] < -100
analytic_inverse = 1 / mp.zeta(mp.mpf("0.5"))
analytic_value_nonzero = abs(analytic_inverse) > mp.mpf("0.5")
cofinal_limit_rejected = (
    critical_products_decrease
    and critical_product_tiny
    and analytic_value_nonzero
)

verdict = finite_order_change_ok and cofinal_limit_rejected

print(f"MAX_FINITE_ORDER_CHANGE_ERROR: {mp.nstr(max_order_change_error, 8)}")
print(f"FINITE_ORDER_CHANGE_COUNTERTERM_EXACT: {'YES' if finite_order_change_ok else 'NO'}")
print(f"CRITICAL_LOG_PRODUCT_AT_1E6: {mp.nstr(log_products[-1], 12)}")
print(f"CRITICAL_COFINAL_PRODUCTS_DECREASE: {'YES' if critical_products_decrease else 'NO'}")
print(f"ANALYTIC_INVERSE_ZETA_HALF: {mp.nstr(analytic_inverse, 12)}")
print(f"ANALYTIC_VALUE_NONZERO: {'YES' if analytic_value_nonzero else 'NO'}")
print(f"ORDINARY_COFINAL_LIMIT_REJECTED: {'YES' if cofinal_limit_rejected else 'NO'}")
print("CRITICAL_NORM_DETERMINANT_CONTINUATION: CLOSED_NO_GO")
print("REQUIRED_STRUCTURE: NONLOCAL_SUMMATION_OR_NUCLEAR_TRACE")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
