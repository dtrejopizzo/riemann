"""Exact rational breakpoints and Arb interval checks for T=5/2."""
from fractions import Fraction
from math import isqrt
from flint import arb, ctx

ctx.prec = 192
one = arb(1)
T = arb(5)/2
radius = Fraction(25, 2)
R, k, m, H = 55000000, 20, 500000000, 400000000000
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
points = {Fraction(1), radius}
for q in powers:
    points.update(x for x in (q/radius, radius/q) if 1 <= x <= radius)
for x in sorted(points):
    y = arb(x.numerator)/x.denominator
    row = sum(w*(y/q+1) for q,w in powers.items() if q <= radius*x)
    row += sum(w*(one/q+y) for q,w in powers.items() if q <= radius/x)
    check(f"Schur endpoint {x}", row/(1+y) < arb(79)/5)

U = (arb(25)/2).log()
check("support", T+arb(k*m)/H < U and 2*U < arb(11)/2)
arch = (R/(2*arb.pi())).log()-one/R-one/(2*R**2)-arb(79)/5
check("archimedean margin", arch > one/10)
a = arb(k*R**2)/(3*H**2)
v = arb(2*R)/H
check("mask band edge", 1-(v.sin()/v)**(2*k) > arb(7)/2*a and 1-one/2**(2*k)>arb(7)/2*a)
# log(1+(1+T*omega)*exp(2*T*omega+2)) <= log(2*(1+T*omega))+2*T*omega+2
omega = 2*R
loss = (2*(1+T*omega)).log()+2*T*omega+2
check("escape versus suppression", m*(arb(7)/2).log()-loss > 10)
check("norm floor", m*a.log() > -9000000000)
check("polar", arb(k)/H**2 < a/2 and 4*T.exp() < 2**20)
check("low correction", arb(10**9).log()+arb(3+G).log().log()-N*arb(100).log() < -9000000002)
high = m*(2*arb(H)/G)**(2*k)
check("high correction", high < one/2 and high*10**9*arb(3+G).log() < one/1000)
check("reserved density", one/(80*arb.pi()) > one/1000)
