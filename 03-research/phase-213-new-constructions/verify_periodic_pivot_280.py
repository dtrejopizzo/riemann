"""Endpoint-corrected filter through T=14011/5000 with a movable spectral cutoff."""
from math import isqrt
from flint import arb, ctx

ctx.prec = 192
one = arb(1)
T = arb(14011)/5000
U = arb(57)/20
R, b, m, H = 2014985964, 13, 9115062736, 2673507086718
G, N = 3*10**12, 120122483651
def check(label, verdict):
    if not verdict:
        raise ArithmeticError(label)
    print("PASS", label)

# Upper bounds for positive shifts on cells. The negative shifts follow
# by reflection because the test weights are constructed symmetrically.
cells = 2048
scale = 10**8
limit = 300
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
for _ in range(70):
    row = row_upper(weights)
    trial = [18*scale*w + v for w,v in zip(weights,row)]
    top = max(trial)
    weights = [1 + v*10**7//top for v in trial]
check("positive symmetric weights", min(weights)>0 and weights == weights[::-1])
row = row_upper(weights)
bound = arb(19486)/1000
check("all continuous Schur rows", all(1000*v < 19486*scale*w for v,w in zip(row,weights)))
check("support", T+arb((b+1)*(m+48))/H < U and 2*U < arb(13)/2)
arch = (R/(2*arb.pi())).log()-one/R-one/(2*R**2)-bound
check("archimedean margin", arch > one/10)
check("global low floor", (arb(1)/4).digamma()-arb.pi().log()-bound > -26)
check("spectral regions", G <= 2*H and H < G and 2*R < H)
r = arb(R)/H
a = r**2*(one/3 + 2*b/(1+(1-r**2).sqrt()))
v = 2*r
edge = 1-(v.sin()/v*((1-v**2).sqrt()*b).cosh()/arb(b).cosh())**2
check("mask band edge", v < 1 and edge > arb(7)/2*a and 1-one/arb(b).cosh()**2 > arb(7)/2*a)
# log(1+(1+T*omega)*exp(2*T*omega+2)) <= log(2*(1+T*omega))+2*T*omega+2
omega = 2*R
loss = (2*(1+T*omega)).log()+2*T*omega+2
# Relative to the inverse square of the Chebyshev denominator.
inflation = arb(25).log()+24*arb(2*m).log()
polar_log = 2*inflation + m*(1+arb(b+2)/(H**2*a)).acosh() + (4*T.exp()).log()
gain_log = m*arb(6).acosh() - loss - arb(80).log()
check("polar and signed low band versus gain",
      polar_log > 0 and gain_log > polar_log + 10 and gain_log > 2*inflation+10)
check("denominator floor", m*(2/a-1).acosh() < 120110026806)
check("low mask positive", a < one/2 and m*(2/a-1).acosh() - arb(4).log() > 2*inflation)
check("cutoff prefactor", 2*16*(arb(19)/4).exp()*25/(2*arb.pi()) < 10**5)
check("cutoff tail ratio", H + N*arb(2718)/1000 < G)
check("low correction", arb(10**9).log()+arb(3+G).log().log()-N*(arb(2718)/1000).log() < -120110026808)
z = m/arb(b).cosh()**2
check("series converges", z < 1)
high = 2*z**25/(1-z)
check("high correction", high < one/2 and high*10**9*arb(3+G).log() < one/1000)
check("reserved density", one/(80*arb.pi()) > one/1000)
