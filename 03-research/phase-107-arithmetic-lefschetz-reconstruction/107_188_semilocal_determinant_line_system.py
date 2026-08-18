#!/home/trabajo/miniforge3/bin/python
"""Exact/high-precision falsifier for the semilocal determinant system."""

from mpmath import mp
from sage.all import prime_range


mp.dps = 60


def archimedean_section(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)


def local_section(p, s):
    return 1 / (1 - mp.power(p, -s))


def semilocal_section(prime_set, s):
    value = archimedean_section(s)
    for p in sorted(prime_set):
        value *= local_section(p, s)
    return value


def transition_factor(source, target, s):
    if not source.issubset(target):
        raise ValueError("transition requires inclusion")
    value = mp.mpc(1)
    for p in sorted(target - source):
        value *= local_section(p, s)
    return value


sets = [
    set(),
    {2, 3},
    {2, 3, 5, 7},
    {2, 3, 5, 7, 11, 13},
]
parameters = [mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3)]
tolerance = mp.mpf("1e-50")

transition_ok = True
cocycle_ok = True
for s in parameters:
    for i in range(len(sets) - 1):
        source = sets[i]
        target = sets[i + 1]
        lhs = semilocal_section(target, s)
        rhs = semilocal_section(source, s) * transition_factor(source, target, s)
        transition_ok = transition_ok and abs(lhs - rhs) < tolerance
    for i in range(len(sets) - 2):
        source, middle, target = sets[i], sets[i + 1], sets[i + 2]
        direct = transition_factor(source, target, s)
        composed = transition_factor(source, middle, s) * transition_factor(middle, target, s)
        cocycle_ok = cocycle_ok and abs(direct - composed) < tolerance

# A nonnested pair must not acquire a transition in either direction.
nonnested_rejected = True
try:
    transition_factor({2, 5}, {3, 5}, mp.mpf("2"))
    nonnested_rejected = False
except ValueError:
    pass

cutoffs = [10, 100, 1000, 10000, 100000]
all_primes = list(prime_range(2, cutoffs[-1] + 1))
target_s = mp.mpf("2")
target_xi = archimedean_section(target_s) * mp.zeta(target_s)
errors = []
for cutoff in cutoffs:
    prime_set = {int(p) for p in all_primes if p <= cutoff}
    errors.append(abs(semilocal_section(prime_set, target_s) - target_xi))
cofinal_ok = all(errors[j + 1] < errors[j] for j in range(len(errors) - 1)) and errors[-1] < mp.mpf("2e-6")

verdict = all([transition_ok, cocycle_ok, nonnested_rejected, cofinal_ok])

print(f"SEMILOCAL_TRANSITIONS_EXACT: {'YES' if transition_ok else 'NO'}")
print(f"TRIPLE_TRANSITION_COCYCLE: {'YES' if cocycle_ok else 'NO'}")
print(f"NONNESTED_TRANSITION_REJECTED: {'YES' if nonnested_rejected else 'NO'}")
print("COFINAL_ERRORS=" + ",".join(mp.nstr(error, 8) for error in errors))
print(f"COFINAL_SECTION_CONVERGES_TO_XI: {'YES' if cofinal_ok else 'NO'}")
print("SEMILOCAL_DETERMINANT_LINE_SYSTEM: CONSTRUCTED")
print("ABSOLUTE_SQUARE_SHEAF_DESCENT: NOT_PROVED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
