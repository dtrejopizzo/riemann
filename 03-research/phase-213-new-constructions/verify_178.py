"""Interval certificate for the complete Weil form at T=21/10."""
from fractions import Fraction
from math import isqrt
from flint import arb, ctx

ctx.prec = 192
one = arb(1)
pi = arb.pi()
T = arb(21)/10
R = 1500000
G = 3*10**12
k = 16
m = 1200000000
H = 240000000000
N = 10**10
omega = 2*R
n = 63000000
a = arb(k*R**2)/(3*H**2)

def check(label, result):
    if not result:
        raise ArithmeticError(label)
    print("PASS", label)

def ball(x):
    return arb(x.numerator)/x.denominator

weights = {}
for p in range(2, 82):
    if any(p % j == 0 for j in range(2, isqrt(p)+1)):
        continue
    q = p
    while q <= 81:
        weights[q] = arb(p).log()
        q *= p

points = {Fraction(1), Fraction(9)}
for q in weights:
    for x in (Fraction(q, 9), Fraction(9, q)):
        if 1 <= x <= 9:
            points.add(x)

def psi_and_L(y):
    psi = arb(0)
    harmonic = arb(0)
    for q, weight in weights.items():
        if q <= y:
            psi += weight
            harmonic += weight/q
    return psi, harmonic

for x in sorted(points):
    p_plus, l_plus = psi_and_L(9*x)
    p_minus, l_minus = psi_and_L(9/x)
    X = ball(x)
    check(f"Schur endpoint {x}", (X*l_plus+p_plus+l_minus+X*p_minus)/(X+1) < 12)

check("expanded support", T+arb(k*m)/H < arb(9).log())
check("spectral guard", 2*arb(9).log() < arb(11)/2)
arch_floor = (R/(2*pi)).log()-one/R-one/(2*R**2)-12
check("archimedean floor", arch_floor > one/3)
check("interpolation remainder", (omega/pi).log()/2+n*(3*one.exp()*omega*T/n).log() < -(4*T.sqrt()).log())
loss = 230*T*R
check("escape fraction", 2*n*arb(256).log()+arb(64).log() < loss)
check("mask", (1-one/400)**(k-1) > arb(4)/5 and 2*arb(R)/H < one/10)
check("margin", m*arb(2).log()-loss > 10 and a.log()*m > -32000000000)
# sinh(v)/v <= exp(v^2) at |v|<=1 by its power series.
check("polar attenuation", arb(k)/H**2 < a/2 and arb(4)*T.exp() < 2**20)
check("correction kernel", 2*14*(arb(17)/4).exp()*25/(2*pi) < 10**5)
check("low tail", arb(10**9).log()+arb(3+G).log().log()-N*arb(100).log() < -32000000002)
high_phi = m*(arb(2*H)/G)**(2*k)
check("high tail", high_phi < one/2 and high_phi*10**9*arb(3+G).log() < one/1000)
check("high reserve with Plancherel", one/(24*pi) > one/1000)
