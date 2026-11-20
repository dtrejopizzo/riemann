"""Compact frequency filter with hyperbolic cosine, T=68/25."""
from math import isqrt
from flint import arb, ctx

ctx.prec = 192
one = arb(1)
T = arb(68)/25
U = arb(2749)/1000
R, b, m, H = 315000000, 29, 1390000000, 1500000000000
G, N = 3*10**12, 10**10
def check(label, verdict):
    if not verdict:
        raise ArithmeticError(label)
    print("PASS", label)

# Upper bounds for positive shifts on cells. The negative shifts follow
# by reflection because the test weights are constructed symmetrically.
cells = 2048
scale = 10**8
limit = 250
check("prime enumeration range", (2*U).exp() < limit)
jumps = []
for p in range(2, limit+1):
    if any(p % j == 0 for j in range(2, isqrt(p)+1)):
        continue
    q = p
    while q <= limit:
        position = arb(q).log()*cells/(2*U)
        offset = int(position.floor().unique_fmpz())
        if offset < cells:
            weight = int((scale*arb(p).log()/arb(q).sqrt()).ceil().unique_fmpz())
            jumps.append((offset, weight))
        q *= p

def row_upper(weights):
    neighbors = [max(a,b) for a,b in zip(weights, weights[1:] + [0])]
    upward = [0]*cells
    for offset, coefficient in jumps:
        for i in range(cells-offset):
            upward[i] += coefficient*neighbors[i+offset]
    return [a+b for a,b in zip(upward, reversed(upward))]

weights = [10**7]*cells
for _ in range(32):
    row = row_upper(weights)
    trial = [18*scale*w + v for w,v in zip(weights,row)]
    top = max(trial)
    weights = [1 + v*10**7//top for v in trial]
check("positive symmetric weights", min(weights)>0 and weights == weights[::-1])
row = row_upper(weights)
bound = arb(1762)/100
check("all continuous Schur rows", all(100*v < 1762*scale*w for v,w in zip(row,weights)))
check("support", T+arb((b+1)*m)/H < U and 2*U < arb(11)/2)
arch = (R/(2*arb.pi())).log()-one/R-one/(2*R**2)-bound
check("archimedean margin", arch > one/10)
r = arb(R)/H
a = r**2*(one/3 + 2*b/(1+(1-r**2).sqrt()))
v = 2*r
edge = 1-(v.sin()/v*((1-v**2).sqrt()*b).cosh()/arb(b).cosh())**2
check("mask band edge", v < 1 and edge > arb(7)/2*a and 1-one/arb(b).cosh()**2 > arb(7)/2*a)
# log(1+(1+T*omega)*exp(2*T*omega+2)) <= log(2*(1+T*omega))+2*T*omega+2
omega = 2*R
loss = (2*(1+T*omega)).log()+2*T*omega+2
# Relative to the inverse square of the Chebyshev denominator.
polar_log = m*(1+arb(b+2)/(H**2*a)).acosh() + (4*T.exp()).log()
gain_log = m*arb(6).acosh() - loss - arb(80).log()
check("polar and signed low band versus gain",
      polar_log > 0 and gain_log > polar_log + 10 and gain_log > 10)
check("denominator floor", m*(2/a-1).acosh() < 22000000000)
check("derivative bound", a < one/2)
check("low correction", arb(10**9).log()+arb(3+G).log().log()-N*arb(100).log() < -22000000002)
high = 2*m/arb(b).cosh()**2
check("high correction", high < one/2 and high*10**9*arb(3+G).log() < one/1000)
check("reserved density", one/(80*arb.pi()) > one/1000)
