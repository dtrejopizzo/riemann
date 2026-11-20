"""Check the prime endpoints for the quadratic weight using integer bounds."""
from decimal import Decimal, localcontext
from math import isqrt
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--limit", type=int, default=100_000)
limit = parser.parse_args().limit
if limit < 3:
    parser.error("--limit must be at least 3")
sieve = bytearray([1]) * (limit + 1)
for p in range(2, isqrt(limit) + 1):
    if sieve[p]:
        sieve[p*p::p] = bytes((limit - p*p) // p + 1)

lower = [0, 0, 0]
upper = [0, 0, 0]
count = 0
with localcontext() as ctx:
    ctx.prec = 45
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        # Decimal.ln is correctly rounded. Enlarging by one integer on
        # either side covers its rounding error after scaling by 10**20.
        value = int(Decimal(p).ln().scaleb(20))
        for j in range(3):
            lower[j] += (value - 1) * p**j
            upper[j] += (value + 2) * p**j
        if p > 2:
            bound = -p*p*upper[0] + 4*p*lower[1] - 3*upper[2]
            if bound <= 0:
                raise ArithmeticError(f"unresolved endpoint {p}")
            count += 1
            last = p
print(f"PASS {count} strict endpoints from 3 through {last}")
