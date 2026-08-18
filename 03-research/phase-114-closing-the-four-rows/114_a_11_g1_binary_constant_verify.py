#!/usr/bin/env python3
"""Exact checks for 114.a.11 (no RH or zeta-zero input)."""

from itertools import product
from math import ceil, comb, exp, lgamma, log


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}" + (f"   {detail}" if detail else ""))
    if not condition:
        raise AssertionError(label)


print("A. Positive boundary")
ok = True
for r in range(2, 6):
    for n in range(1, 9):
        count = sum(1 for v in product(range(n + 1), repeat=r) if sum(v) == n)
        ok &= count == comb(n + r - 1, r - 1)
check("A1 enumeration equals stars-and-bars", ok)

ok = all(
    ceil(log(comb(n + r - 1, r - 1), 2)) >= ceil(log(n + 1, 2))
    for r in range(2, 20) for n in range(1, 40)
)
check("A2 new lower bound strengthens the old segment bound", ok)

print("\nB. Coupled squeeze")
k, a = 2, 0.7
rows = []
for m in (10, 20, 40, 80, 160):
    r = m * k + 1
    n = int(exp(m * a))
    # Product formula avoids catastrophic cancellation of lgamma(n+r)-lgamma(n).
    log_binom = sum(log(n + j) for j in range(1, r)) - lgamma(r)
    lower = log_binom / log(2) / (k * a * m * m)
    upper = r * ceil(log(n + 1, 2)) / (k * a * m * m)
    rows.append((m, lower, upper))
check("B1 lower <= upper in every tested coupled case",
      all(lo <= hi for _, lo, hi in rows))
target = 1 / log(2)
check("B2 squeeze endpoints approach 1/log(2)",
      abs(rows[-1][1] - target) < 0.09 and abs(rows[-1][2] - target) < 0.02,
      f"last=[{rows[-1][1]:.6f},{rows[-1][2]:.6f}], target={target:.6f}")
check("B3 lower endpoint is eventually increasing",
      all(rows[i][1] < rows[i + 1][1] for i in range(1, len(rows) - 1)))

print("\nC. Refined logarithmic expansion")
errors = []
for m in (20, 40, 80, 160):
    r0 = m * k
    n = int(exp(m * a))
    exact = sum(log(n + j) for j in range(1, r0 + 1)) - lgamma(r0 + 1)
    leading = r0 * log(n) - lgamma(r0 + 1)
    errors.append(abs(exact - leading) / (r0 * r0 / n))
check("C1 binomial product error is O(r^2/n)", max(errors) < 1.0,
      f"scaled errors={[round(x, 6) for x in errors]}")

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
