"""Interval enclosures for ordered semiprime discrepancies in the moving band."""
from mpmath import iv

iv.dps = 30


def enclose(lower, upper, primes, cells=512):
    x = iv.mpf([lower, upper]) / 100
    a = iv.log(x) / 3
    cumulative = iv.mpf(0)
    continuous, errors = [], []
    for j in range(cells):
        u = 1 + iv.mpf([j, j + 1]) / cells
        t = iv.exp(a * u)
        increment = t / u / cells
        mass = iv.mpf([cumulative.a, (cumulative + increment).b])
        count = iv.mpf([sum(t.a >= p for p in primes),
                        sum(t.b >= p for p in primes)])
        continuous.append(mass)
        errors.append(count - mass)
        cumulative += increment

    quadratic = a * sum(e * f for e, f in zip(errors, reversed(errors))) / cells
    linear = 2 * a * sum(e * c for e, c in zip(errors, reversed(continuous))) / cells
    return quadratic, linear, quadratic + linear


for lower, upper, primes in [(2499, 2501, (3, 5, 7)), (2701, 2703, (5, 7))]:
    quadratic, linear, total = enclose(lower, upper, primes)
    print(lower, upper, quadratic, linear, total)
    if lower == 2499:
        assert quadratic.a > -iv.mpf(8)/100 and quadratic.b < -iv.mpf(5)/100
        assert total.a > 0
    else:
        assert total.b < 0
