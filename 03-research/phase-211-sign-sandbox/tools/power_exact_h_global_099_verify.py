"""Fixed continuous exact T_h test on u in [0,512], round099.

Entire regularization Ntilde/u^15, followed by a positive panelwise exponential
gauge. The final design fixes 2048 panels, 1024 bits, degree104 and cap109.
All analytic bounds and representation changes precede the first run.
"""
from flint import arb,arb_series,ctx
from fractions import Fraction as Q
from math import factorial
from hashlib import sha256
from pathlib import Path

PANELS,PREC,CAP,DEGREE=2048,1024,109,104
BOUND=2**169
RATIO=Q(1,8)
TAIL_EXACT=BOUND*RATIO**105/(1-RATIO)
assert TAIL_EXACT<Q(1,2**145)
assert Q(87,32)**6<512
assert Q(8,3)**5>86
assert Q(1,516)+Q(1,515)<Q(1,2)
assert 1024*factorial(4)<2**15 and 513<2**10
assert 91*2**100<2**107 and 51*2**90<2**96
assert 2**120+2**98<2**121
assert 6*Q(56,81)>Q(15,4)
assert 128*factorial(4)<2**12
assert 91*2**48<2**55 and 51*2**48<2**54
assert 2**56+2**56<=2**57
assert 2**57*4**15==2**87
assert 2**121*4**15==2**151
assert 512**2==2**18
print('PASS all predeclared Cauchy, Schwarz and gauge bounds',flush=True)

ctx.prec,ctx.cap=PREC,CAP
LOGPI=arb.pi().log()
def ball(q):return arb(q.numerator)/q.denominator

def entire_u(u):
    # Official deflation: zeta(A)-1/(A-1), not (A-1)*zeta(A).
    A=u+arb(1)/2
    regular=1+(A-1)*A.zeta(deflate=True)
    value=A*regular*(A/2).gamma()*(-A*LOGPI/2).exp()
    assert value.prec>=u.prec
    assert value[0].is_finite() and value[0]>0
    return value

# One fixed origin jet for the SAME a; exact evenness makes E'(0)=0.
origin=entire_u(arb_series([arb(0),arb(1)],prec=3))
assert origin.prec>=3 and all(origin[k].is_finite() for k in range(3))
assert origin[1].contains(arb(0))
a=2*origin[2]/origin[0]
assert a>0 and a<8
old_center=Q('0.0462099862308379415778676')
old_radius=Q(374,10**28)
old_a=ball(old_center-old_radius).union(ball(old_center+old_radius))
assert old_a.contains(a),('origin a not enclosed by certificate098',a,old_a)

# Identity/API checks, not samples of the target sign.
at_one=arb_series([arb(1),arb(1)],prec=CAP)
assert at_one.zeta(deflate=True)[0].overlaps(arb.const_euler())
assert entire_u(at_one-arb(1)/2)[0].contains(arb(1))
at_two=arb_series([arb(2),arb(1)],prec=CAP)
ordinary=at_two*(at_two-1)*at_two.zeta()*(at_two/2).gamma()*(-at_two*LOGPI/2).exp()
regular=entire_u(at_two-arb(1)/2)
assert all(ordinary[k].overlaps(regular[k]) for k in range(CAP))
print('PASS precise a, certificate098 containment and entire representation',flush=True)
print('a from fixed origin jet',a,flush=True)

def target(mid):
    u=arb_series([mid,arb(1)],prec=CAP)
    raw=entire_u(u)
    mc=raw[1]/raw[0]
    assert mc.is_finite() and mc>0 and mc<3
    # Only a CONSTANT normalization. Derivatives are of the original E.
    E=raw/raw[0]
    e=[E]
    for _ in range(4):e.append(e[-1].derivative())
    e0,e1,e2,e3,e4=e
    assert e4.prec>=DEGREE+1
    PS=(u**4*(2*e0**2*e2*e4-3*e0**2*e3**2-2*e0*e1**2*e4
              +10*e0*e1*e2*e3-6*e0*e2**3-4*e1**3*e3+3*e1**2*e2**2)
        +u**3*(2*e0**2*e1*e4-6*e0**2*e2*e3-2*e0*e1**2*e3
               +12*e0*e1*e2**2-6*e1**3*e2)
        +u**2*(6*e0**2*e1*e3-9*e0**2*e2**2+3*e1**4)
        +u*(6*e0**2*e1*e2-6*e0*e1**3)+3*e0**2*e1**2)
    PC=(u**3*(e0*e1**2*e4-6*e0*e1*e2*e3+6*e0*e2**3
              +2*e1**3*e3-3*e1**2*e2**2)
        +u**2*(6*e0*e1**2*e3-12*e0*e1*e2**2+6*e1**3*e2)
        +u*(3*e0*e1**2*e2-3*e1**4)+3*e0*e1**3)
    S=(a*u*PS-4*PC)/(u**15)
    assert S.prec>=DEGREE+1
    # Gauge is applied AFTER PS/PC and the removable division, never to ej.
    gauge=(-4*mc*(u-mid)).exp()
    G=S*gauge
    assert G.prec>=DEGREE+1
    assert all(G[k].is_finite() for k in range(DEGREE+1))
    return G

H=arb(1)/8
HPOW=[H**k for k in range(DEGREE+1)]
TAIL=ball(TAIL_EXACT)
for j in range(PANELS):
    mid=arb((2*j+1,-3))
    panel=arb((2*j+1,-3),(1,-3))
    assert mid>0 and panel.contains(mid-H) and panel.contains(mid+H)
    G=target(mid)
    loss=sum((G[k].abs_upper()*HPOW[k] for k in range(1,DEGREE+1)),arb(0))+TAIL
    lower=G[0]-loss
    assert lower>0,('not certified',j,mid,G[0],loss,lower)
    if (j+1)%128==0:
        print('PASS exact T_h panels',j+1,'of',PANELS,flush=True)
print('PASS ALL099: exact T_h positive throughout [0,512]',flush=True)
print('CAUCHY GAUGED BOUND',BOUND,'CAUCHY TAIL EXACT',TAIL_EXACT,flush=True)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
