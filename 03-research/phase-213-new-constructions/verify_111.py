"""Check every prime centre up to one million in the criterion of round 110."""
from bisect import bisect_right
from math import isqrt
from flint import arb, ctx

ctx.prec = 128
limit = 10**6
h = arb(11) / 25
r = h.exp()


def certified_floor(value):
    return int(value.floor().unique_fmpz())


bound = certified_floor(limit * r)
sieve = bytearray([1]) * (bound + 1)
sieve[:2] = bytes(2)
for p in range(2, isqrt(bound) + 1):
    if sieve[p]:
        sieve[p*p::p] = bytes((bound - p*p) // p + 1)
primes = [n for n, flag in enumerate(sieve) if flag]
mass, reciprocals = [arb(0)], [arb(0)]
for p in primes:
    weight = arb(p).log()
    mass.append(mass[-1] + weight)
    reciprocals.append(reciprocals[-1] + weight / p)

counts = {}
last = {}
original_failures = []
for i, q in enumerate(primes):
    if q > limit:
        break
    lo = bisect_right(primes, certified_floor(q/r))
    hi = bisect_right(primes, certified_floor(q*r))
    d = arb(q).log()
    balance = mass[hi] - mass[i+1] - r*(mass[i] - mass[lo])
    left = reciprocals[i] - reciprocals[lo] - h
    right = reciprocals[hi] - reciprocals[i] - h
    excess = r*right - left
    assert all(v < 0 or v > 0 for v in (left, right, excess))
    # From 110, 2 sqrt(r) E(q) = q*excess - (balance+d).
    original = q*excess - (balance + d)
    assert original < 0 or original > 0
    if original > 0:
        original_failures.append(q)
    if balance < -d or balance > r*d:
        continue
    assert balance >= -d and balance <= r*d
    key = tuple('+' if v > 0 else '-' for v in (left, right, excess))
    counts[key] = counts.get(key, 0) + 1
    last[key] = q
print('centres, selected:', bisect_right(primes, limit), sum(counts.values()))
for key in sorted(counts):
    print(''.join(key), counts[key], last[key])
print('positive original discrepancies at all centres:', len(original_failures), original_failures[-1:] )
