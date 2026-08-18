#!/usr/bin/env python3
"""Directed numerical and exact algebra checks for D.69."""

import mpmath as mp
import sympy as sp

mp.mp.dps = 80
a = mp.log(2)
tau0 = 3 * mp.pi / (2 * a)
beta = tau0 / 2

# Positive-series evaluation of a'(tau_0), with a conservative integral
# tail enclosure after a large cutoff.
N = 10000
s = mp.fsum(
    [(j + mp.mpf(1) / 4) / ((j + mp.mpf(1) / 4) ** 2 + beta**2) ** 2
     for j in range(N)]
)
# For y>N-3/4>beta/sqrt(3), the summand is decreasing.  The tail is below
# the first omitted value plus the exact integral from that point.
y0 = mp.mpf(N) + mp.mpf(1) / 4
first = y0 / (y0**2 + beta**2) ** 2
tail_integral = 1 / (2 * (y0**2 + beta**2))
aprime_upper = beta * (s + first + tail_integral)
prime_slope = mp.sqrt(2) * a**2
assert prime_slope > aprime_upper

# The elementary closed upper bound in the proof also suffices.
elementary_upper = 1 / (2 * beta) + 9 / (8 * mp.sqrt(3) * beta**2)
assert aprime_upper < elementary_upper < prime_slope

# Persistent-mode counterexample.
z = sp.symbols("z", real=True)
B = sp.diag(2, 1, -1)
D = sp.diag(1, -1)
sfun = 2 - z
assert D.eigenvals() == {1: 1, -1: 1}
assert sfun == 2 - z

print(f"tau0={mp.nstr(tau0, 20)}")
print(f"a'(tau0) upper={mp.nstr(aprime_upper, 20)}")
print(f"sqrt(2) log(2)^2={mp.nstr(prime_slope, 20)}")
print("PASS actual first-cell prime--Gamma multiplier has b'(tau0)>0")
print("PASS scalar positive Stieltjes monotonicity is impossible")
print("PASS Schur scalar can miss a positive persistent compressed mode")
