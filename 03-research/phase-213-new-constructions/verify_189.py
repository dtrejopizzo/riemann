"""Two applications of the compressed prime operator, T=129/50."""
from bisect import bisect_right
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from flint import arb, ctx

ctx.prec = 192
one = arb(1)
T = arb(129)/50
radius = Fraction(14)
R, k, m, H = 128000000, 20, 1070000000, 400000000000
G, N = 3*10**12, 10**10
def check(label, verdict):
    if not verdict:
        raise ArithmeticError(label)
    print("PASS", label)

limit = int(radius**2)
powers = {}
for p in range(2, limit+1):
    if all(p % j for j in range(2, isqrt(p)+1)):
        q = p
        while q <= limit:
            powers[q] = arb(p).log()
            q *= p
ordered = sorted(powers)
mass = [arb(0)]
weighted = [arb(0)]
for q in ordered:
    mass.append(mass[-1] + powers[q])
    weighted.append(weighted[-1] + powers[q]/q)

@lru_cache(maxsize=None)
def first_row(x):
    i = bisect_right(ordered, radius*x)
    j = bisect_right(ordered, radius/x)
    y = arb(x.numerator)/x.denominator
    return y*weighted[i] + mass[i] + weighted[j] + y*mass[j]

inner = {b for q in ordered for b in (q/radius, radius/q)
         if 1/radius <= b <= radius}
points = {Fraction(1), radius} | {b for b in inner if b >= 1}
for b in inner:
    for q in ordered:
        points.update(x for x in (b*q, b/q) if 1 <= x <= radius)

bound = arb(1672)/100
for x in sorted(points):
    row = sum(powers[q]*first_row(x/q) for q in ordered if q <= radius*x)
    row += sum(powers[q]*first_row(x*q)/q for q in ordered if q <= radius/x)
    y = arb(x.numerator)/x.denominator
    if not row < bound**2*(1+y):
        raise ArithmeticError(f"second Schur row at {x}")
print("PASS second Schur rows", len(points))
U = arb(14).log()
check("support", T+arb(k*m)/H < U and 2*U < arb(11)/2)
arch = (R/(2*arb.pi())).log()-one/R-one/(2*R**2)-bound
check("archimedean margin", arch > one/10)
a = arb(k*R**2)/(3*H**2)
v = arb(2*R)/H
check("mask band edge", 1-(v.sin()/v)**(2*k) > arb(7)/2*a and 1-one/2**(2*k)>arb(7)/2*a)
# log(1+(1+T*omega)*exp(2*T*omega+2)) <= log(2*(1+T*omega))+2*T*omega+2
omega = 2*R
loss = (2*(1+T*omega)).log()+2*T*omega+2
check("escape versus suppression", m*(arb(7)/2).log()-loss > 10)
check("norm floor", m*a.log() > -20000000000)
check("polar", arb(k)/H**2 < a/2 and 4*T.exp() < 2**20)
check("low correction", arb(10**9).log()+arb(3+G).log().log()-N*arb(100).log() < -20000000002)
high = m*(2*arb(H)/G)**(2*k)
check("high correction", high < one/2 and high*10**9*arb(3+G).log() < one/1000)
check("reserved density", one/(80*arb.pi()) > one/1000)
