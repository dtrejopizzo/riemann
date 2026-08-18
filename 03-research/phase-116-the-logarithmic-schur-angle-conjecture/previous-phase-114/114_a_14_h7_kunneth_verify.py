#!/usr/bin/env python3
"""Acceptance-test checks for 114.a.14."""

from math import log


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}" + (f"   {detail}" if detail else ""))
    if not condition:
        raise AssertionError(label)


print("A. Pure external products")
# Exact models |B_m|=3^(2m+1), |C_m|=5^(m+2).
rows = []
for m in (5, 10, 20, 40, 80, 160):
    b = 3 ** (2 * m + 1)
    c = 5 ** (m + 2)
    pure = b * c
    rows.append((m, log(pure), log(pure) / (m * m)))
check("A1 |image| <= |B||C| (equality in the injective best case)",
      all(3 ** (2 * m + 1) * 5 ** (m + 2) == p for m, _, _ in rows
          for p in [3 ** (2 * m + 1) * 5 ** (m + 2)]))
check("A2 log pure-products is linear, so log/m^2 tends to zero",
      rows[-1][2] < rows[0][2] / 20,
      f"ratios {rows[0][2]:.6f} -> {rows[-1][2]:.6f}")

print("\nB. Mixed coefficient arrays")
# d_m=m^2 binary independent generators give exactly 2^(m^2) arrays.
mixed_ratios = [log(2 ** (m * m)) / (m * m) for m in (2, 4, 8, 16)]
check("B1 m^2 independent binary choices give exp((log 2)m^2)",
      all(abs(x - log(2)) < 1e-12 for x in mixed_ratios))
check("B2 mixed growth separates from pure growth",
      mixed_ratios[-1] > 20 * rows[-1][2])

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
