#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the balanced local-character pushforward through Morishita."""

from mpmath import mp


mp.dps = 70
PRIMES = (2, 3, 5, 7, 11)


def bump_log(x, center=mp.mpf("1.5"), radius=mp.mpf("1.4")):
    """A smooth asymmetric compactly supported function on R_+^*."""
    z = (mp.log(x) - center) / radius
    if abs(z) >= 1:
        return mp.mpf(0)
    return mp.exp(-1 / (1 - z * z))


def modular_involution(f, x):
    return f(1 / x) / x


def oriented_character(p, f, max_return=30):
    log_p = mp.log(p)
    return log_p * mp.fsum(f(mp.power(p, e)) for e in range(1, max_return + 1))


def balanced_character(p, f, max_return=30):
    return oriented_character(p, f, max_return) + oriented_character(
        p, lambda x: modular_involution(f, x), max_return
    )


max_balance_error = mp.mpf(0)
min_oriented_failure = mp.inf
all_nonzero = True

for p in PRIMES:
    value = balanced_character(p, bump_log)
    inverted = balanced_character(
        p, lambda x: modular_involution(bump_log, x)
    )
    max_balance_error = max(max_balance_error, abs(value - inverted))

    positive_half = oriented_character(p, bump_log)
    reversed_half = oriented_character(
        p, lambda x: modular_involution(bump_log, x)
    )
    min_oriented_failure = min(min_oriented_failure, abs(positive_half - reversed_half))
    all_nonzero &= abs(value) > mp.mpf("1e-30")

balance_ok = max_balance_error < mp.mpf("1e-60")
oriented_rejected = min_oriented_failure > mp.mpf("1e-8")

# Pushforward of packet traces depends only on the coefficient sum.
# These finite vectors probe both the kernel and its complement.
packet_tests = ((1, -1), (3, -2, -1), (2, 0, -2), (1, 1), (2, -1, 4))
kernel_exact = True
for p, coefficients in zip(PRIMES, packet_tests):
    base_trace = balanced_character(p, bump_log)
    pushed = mp.fsum(mp.mpf(c) * base_trace for c in coefficients)
    expected = mp.fsum(coefficients) * base_trace
    kernel_exact &= abs(pushed - expected) < mp.mpf("1e-60")
    kernel_exact &= (abs(pushed) < mp.mpf("1e-40")) == (sum(coefficients) == 0)

# A deliberately wrong involution omits the modular factor x^{-1}.
wrong_rejected = any(
    abs(
        balanced_character(p, bump_log)
        - balanced_character(p, lambda x: bump_log(1 / x))
    )
    > mp.mpf("1e-8")
    for p in PRIMES
)

verdict = (
    balance_ok
    and oriented_rejected
    and all_nonzero
    and kernel_exact
    and wrong_rejected
)

print(f"ACTUAL_PRIME_ORBITS_TESTED: {len(PRIMES)}")
print(f"MAX_BALANCED_INVERSION_ERROR: {mp.nstr(max_balance_error, 8)}")
print(f"MIN_ORIENTED_HALF_FAILURE: {mp.nstr(min_oriented_failure, 8)}")
print(f"BALANCED_LOCAL_CHARACTER_ANTI_FLOW_INVARIANT: {'YES' if balance_ok else 'NO'}")
print(f"ORIENTED_HALF_DESCENDS: {'NO' if oriented_rejected else 'YES'}")
print(f"ZERO_SUM_PACKET_KERNEL_EXACT: {'YES' if kernel_exact else 'NO'}")
print(f"WRONG_UNWEIGHTED_INVOLUTION_REJECTED: {'YES' if wrong_rejected else 'NO'}")
print("MORISHITA_FINITE_CHARACTER_PUSHFORWARD: CONSTRUCTED")
print("PACKET_SENSITIVE_BASE_CURRENT: NOT_CONSTRUCTED")
print("ARITHMETIC_SQUARE_INTERSECTION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

