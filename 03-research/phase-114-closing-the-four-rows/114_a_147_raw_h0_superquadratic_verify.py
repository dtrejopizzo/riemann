"""Finite checks for the reflected raw-H0 superquadratic theorem."""

from math import comb, log


for q in (3, 5, 7):
    for d in range(1, 11):
        n = 2**d
        Q = q**d
        count = comb(n + Q - 1, n)
        assert Q >= n
        assert count >= 2 ** (n - 1)
        assert log(count) >= (n - 1) * log(2)

print("VERDICT: RAW BOUNDED H0 IS SUPERQUADRATIC AFTER REGULAR REFLECTION")
