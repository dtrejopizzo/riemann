#!/home/trabajo/miniforge3/bin/python
"""Falsifier for higher Schatten determinant counterterms."""

from mpmath import mp


mp.dps = 60
PRIMES = (2, 3, 5, 7, 11)
PARAMETERS = (mp.mpf("1.5"), mp.mpf("2"), mp.mpc(2, 3))
ORDERS = (2, 3, 5, 6)


def block_det_m(a, order):
    value = (1 - a) * (1 + a)
    correction = mp.mpc(0)
    for power in range(1, order):
        correction += (a**power + (-a) ** power) / power
    return value * mp.e**correction


block_formula_ok = True
only_order_two_counterterm_free = True
higher_orders_differ_from_euler = True
max_block_error = mp.mpf(0)

for p in PRIMES:
    for s in PARAMETERS:
        q = mp.power(p, -s)
        a = mp.power(p, -s / 2)
        for order in ORDERS:
            cutoff = (order - 1) // 2
            counterterm = mp.fsum(q**j / j for j in range(1, cutoff + 1))
            expected = (1 - q) * mp.e**counterterm
            actual = block_det_m(a, order)
            error = abs(actual - expected)
            max_block_error = max(max_block_error, error)
            block_formula_ok &= error < mp.mpf("1e-50")
            if order == 2:
                only_order_two_counterterm_free &= abs(actual - (1 - q)) < mp.mpf("1e-50")
            else:
                higher_orders_differ_from_euler &= abs(actual - (1 - q)) > mp.mpf("1e-8")


# Finite global identity for m=5.
finite_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
global_formula_ok = True
for s in PARAMETERS:
    direct = mp.mpc(1)
    euler_inverse = mp.mpc(1)
    p1 = mp.mpc(0)
    p2 = mp.mpc(0)
    for p in finite_primes:
        q = mp.power(p, -s)
        direct *= block_det_m(mp.power(p, -s / 2), 5)
        euler_inverse *= 1 - q
        p1 += q
        p2 += q**2
    predicted = euler_inverse * mp.e ** (p1 + p2 / 2)
    global_formula_ok &= abs(direct - predicted) < mp.mpf("1e-45")


# At sigma=1/2, S_4 asks for sum 1/p (divergent), whereas S_5 asks
# for sum p^{-5/4} (convergent).
sigma = mp.mpf("0.5")
critical_order_four_exponent = 4 * sigma / 2
critical_order_five_exponent = 5 * sigma / 2
critical_threshold_ok = (
    critical_order_four_exponent == 1
    and critical_order_five_exponent > 1
)

verdict = all(
    [
        block_formula_ok,
        only_order_two_counterterm_free,
        higher_orders_differ_from_euler,
        global_formula_ok,
        critical_threshold_ok,
    ]
)

print(f"SCHATTEN_ORDERS_TESTED: {len(ORDERS)}")
print(f"MAX_PAIRED_BLOCK_FORMULA_ERROR: {mp.nstr(max_block_error, 8)}")
print(f"PAIRED_COUNTERTERM_FORMULA: {'YES' if block_formula_ok else 'NO'}")
print(f"ONLY_DET2_COUNTERTERM_FREE: {'YES' if only_order_two_counterterm_free else 'NO'}")
print(f"HIGHER_DETERMINANTS_DIFFER_FROM_EULER: {'YES' if higher_orders_differ_from_euler else 'NO'}")
print(f"FINITE_GLOBAL_PRIME_ZETA_FORMULA: {'YES' if global_formula_ok else 'NO'}")
print(f"CRITICAL_LINE_MINIMUM_SCHATTEN_ORDER: {5 if critical_threshold_ok else 'UNRESOLVED'}")
print("UNCORRECTED_HIGHER_SCHATTEN_CONTINUATION: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: DERIVED_GLOBAL_COUNTERTERM")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
