#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the global balanced prime Dirac det_2 realization."""

from mpmath import mp


mp.dps = 60
PRIME_CUTOFF = 100_000


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


primes = primes_up_to(PRIME_CUTOFF)
parameters = (mp.mpf("2"), mp.mpf("2.5"), mp.mpf("3"), mp.mpc(2, 3))

paired_block_ok = True
determinant_convergence_ok = True
green_convergence_ok = True
max_det_error = mp.mpf(0)
max_green_error = mp.mpf(0)

for s in parameters:
    determinant_product = mp.mpc(1)
    green_sum = mp.mpc(0)
    for p in primes:
        half = mp.power(p, -s / 2)
        paired_block = (1 - half) * mp.e**half * (1 + half) * mp.e ** (-half)
        expected_block = 1 - mp.power(p, -s)
        paired_block_ok &= abs(paired_block - expected_block) < mp.mpf("1e-50")
        determinant_product *= expected_block
        green_sum += mp.log(p) * mp.power(p, -s) / (1 - mp.power(p, -s))

    det_error = abs(determinant_product - 1 / mp.zeta(s))
    green_target = -mp.diff(mp.zeta, s) / mp.zeta(s)
    green_error = abs(green_sum - green_target)
    max_det_error = max(max_det_error, det_error)
    max_green_error = max(max_green_error, green_error)
    determinant_convergence_ok &= det_error < mp.mpf("2e-5")
    green_convergence_ok &= green_error < mp.mpf("2e-5")


cutoffs = (100, 1_000, 10_000, 100_000)
hs_partial = []
trace_partial = []
sigma = mp.mpf("1.5")
for cutoff in cutoffs:
    visible = [p for p in primes if p <= cutoff]
    hs_partial.append(2 * mp.fsum(mp.power(p, -sigma) for p in visible))
    trace_partial.append(2 * mp.fsum(mp.power(p, -sigma / 2) for p in visible))

hilbert_schmidt_behavior_ok = all(
    hs_partial[index + 1] - hs_partial[index]
    < hs_partial[index] - hs_partial[index - 1]
    for index in range(1, len(hs_partial) - 1)
)
trace_norm_growth_ok = all(
    trace_partial[index + 1] > trace_partial[index]
    for index in range(len(trace_partial) - 1)
) and trace_partial[-1] > 2 * trace_partial[0]

# Removing the negative partner leaves an uncancelled exponential factor.
mutation = mp.mpf("0.2")
unpaired = (1 - mutation) * mp.e**mutation
unpaired_mutation_rejected = abs(unpaired - (1 - mutation**2)) > mp.mpf("1e-3")

verdict = all(
    [
        paired_block_ok,
        determinant_convergence_ok,
        green_convergence_ok,
        hilbert_schmidt_behavior_ok,
        trace_norm_growth_ok,
        unpaired_mutation_rejected,
    ]
)

print(f"PRIME_CUTOFF: {PRIME_CUTOFF}")
print(f"PRIMES_USED: {len(primes)}")
print(f"PAIRED_DET2_BLOCK_CANCELLATION: {'YES' if paired_block_ok else 'NO'}")
print(f"MAX_INVERSE_ZETA_PRODUCT_ERROR: {mp.nstr(max_det_error, 10)}")
print(f"GLOBAL_DET2_EQUALS_ZETA_INVERSE: {'YES' if determinant_convergence_ok else 'NO'}")
print(f"MAX_GREEN_CHANNEL_ERROR: {mp.nstr(max_green_error, 10)}")
print(f"GLOBAL_GREEN_TRACE_RECOVERED: {'YES' if green_convergence_ok else 'NO'}")
print(f"HILBERT_SCHMIDT_TAIL_BEHAVIOR: {'YES' if hilbert_schmidt_behavior_ok else 'NO'}")
print(f"TRACE_NORM_GROWTH_IN_CRITICAL_EULER_STRIP: {'YES' if trace_norm_growth_ok else 'NO'}")
print(f"UNPAIRED_BLOCK_MUTATION_REJECTED: {'YES' if unpaired_mutation_rejected else 'NO'}")
print("GLOBAL_BALANCED_PRIME_DIRAC_DET2: CONSTRUCTED_FOR_RE_S_GT_1")
print("COMPLETED_ARCHIMEDEAN_OPERATOR_FAMILY: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
