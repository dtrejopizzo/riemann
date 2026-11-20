"""Certify the explicit 039 trace inequality on [16, 2**20] (python-flint)."""
from math import isqrt

from flint import arb, arb_series, ctx


def prime_powers(limit):
    prime = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p*p::p] = bytes((limit - p*p) // p + 1)
    terms = []
    for p in range(2, limit + 1):
        if prime[p]:
            weight = arb(p).log()
            n = p
            while n <= limit:
                terms.append((n, weight))
                n *= p
    return sorted(terms)


def certify():
    ctx.prec = 160
    zeta = arb_series([2, 1], 2).zeta()
    s2 = -zeta[1] / zeta[0]
    euler = arb.const_euler()
    trace3 = 3 - euler - arb.pi().log() - 2*s2
    coeff = 1 - euler - (2*arb.pi()).log() - s2
    if not -16*coeff > arb(2).log() + arb(1)/2:
        raise ArithmeticError("Archimedean correction bound failed")

    denom = 32
    terms = prime_powers(2**20)
    index = 0
    mass = arb(0)
    moment = arb(0)
    previous = None
    cells = 0
    lower_margin = arb(1)/1000
    for j in range(2*denom, 32*denom + 1):
        x = (arb(j)/denom)**4
        while index < len(terms) and terms[index][0]*denom**4 <= j**4:
            n, weight = terms[index]
            mass += weight / n**2
            moment += n*weight
            index += 1
        scale = x*x.sqrt()
        error = scale*(mass-s2) - moment/scale + 3*x.sqrt()/2
        if previous is not None:
            left, left_error = previous
            interpolation = x**6*x.sqrt()*(left**-3-x**-3)**2/24
            ceiling = trace3 - interpolation - lower_margin
            if not all(ceiling > value for value in (0, left_error, error)):
                raise ArithmeticError(f"Cell ending at ({j}/{denom})^4 unresolved")
            cells += 1
        previous = x, error
    if cells != 960 or index != len(terms):
        raise ArithmeticError("Incomplete coverage")
    print(f"PASS {cells} cells, {index} prime powers, margin > 1/1000")


if __name__ == "__main__":
    certify()
