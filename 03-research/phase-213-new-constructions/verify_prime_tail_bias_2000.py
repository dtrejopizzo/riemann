"""Certify the dual prime-tail upper bound for p <= 2000 using Arb balls."""
from math import isqrt
from flint import arb, ctx

ctx.prec = 96
limit = 3_000_000
sieve = bytearray([1]) * (limit + 1)
sieve[:2] = bytes(2)
for d in range(2, isqrt(limit) + 1):
    if sieve[d]:
        sieve[d*d::d] = bytes((limit-d*d)//d + 1)

# Upper B tail by the integral of log(t)/t^(5/2); D needs only a lower bound.
x = arb(limit)
b_upper = (x.log() + arb(2)/3) * 2 / (3*x*x.sqrt())
d_lower = arb(0)
constant = arb(2)/3 * (arb(5)/2)**(arb(3)/5)
count = 0
for n in range(limit, 1, -1):
    if not sieve[n]:
        continue
    if n <= 2000:
        assert n*n*(constant*d_lower**(arb(3)/5)-b_upper) > arb('0.03'), n
        count += 1
    p = arb(n)
    term = p.log()/(p*p*p.sqrt())
    b_upper += term
    d_lower += term/p
print(f"PASS: {count} primes, p²(g(D_p)−B_p)>0.03")
