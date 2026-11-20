"""Darboux bounds for the central signed density; all arithmetic is exact."""
from fractions import Fraction
from math import factorial
from flint import fmpz_poly


def density_bound(upper, order):
    # Mesh 1/1000. The real upper prime cutoff lies between .560 and .565.
    end = 565 if upper else 560
    scale = 10**8
    masses = [0] * end
    for j in range(160, end):
        masses[j] = (scale + j - 1) // j if upper else scale // (j + 1)
    first = fmpz_poly(masses) ** (order - 1)
    total = 0
    for j, count in enumerate(first.coeffs()):
        low = 995 - j - (order - 1)
        high = 1005 - j
        if upper and high >= 160 and low <= end:
            total += int(count) * ((1000 * scale + max(160, low) - 1) // max(160, low))
        elif not upper and low >= 160 and high <= end:
            total += int(count) * (1000 * scale // high)
    return Fraction(total, scale**order * factorial(order))


lower = upper = Fraction(0)
for k in range(2, 7):
    lo, hi = density_bound(False, k), density_bound(True, k)
    lower += lo if k % 2 == 0 else -hi
    upper += hi if k % 2 == 0 else -lo
assert -1 < lower <= upper < Fraction(-1, 10)
print("PASS: -1 < signed density < -1/10 throughout [.995, 1.005]")
