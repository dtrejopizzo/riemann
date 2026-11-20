"""One fixed exact T_h-origin test from six complete even theta moments.

Design098 fixes all parameters and analytic errors before execution. No grid
of signs, moment-order search, or imported earlier numerical run is used.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from hashlib import sha256
from flint import arb, arb_series, ctx

PANELS, DEGREE, CAP, PREC, MODES = 128, 64, 65, 512, 16
ORDERS = (0,2,4,6,8,10)
EPS = Q(2**25*17**4, 8**289)
REM = 2*10**12*Q(1,4)**65/(1-Q(1,4))
TEMPORAL_TAIL = Q(1,2**138)
assert Q(87,32)<3
assert 3*Q(15,16)*Q(511,512)>Q(5,2)
assert 3**5<256 and 3**6<1024
assert 4*1024*2051<2**24
assert 16*Q(1,8)**3<Q(1,2)
assert 3**10*2**22<10**12
assert Q(18,17)**4/Q(8)**35<Q(1,2)
assert REM<Q(1,10**24)
assert sum(Q(4)**k/Q(factorial(k)) for k in range(20))>54
assert 64*3**9<2**22
assert Q(9,2)-6*54<-300 and Q(1024,295)<4
assert sum(Q(2)**k/Q(factorial(k)) for k in range(6))>7
assert 7*Q(3,2)>8
print('PASS predeclared analytic bounds for all six even moments',flush=True)

ctx.prec,ctx.cap=PREC,CAP
def ball(q):return arb(q.numerator)/q.denominator
pi=arb.pi()
errors=[arb(0,(ball(EPS)*32**k).upper()) for k in range(CAP)]

def theta16(t):
    assert t.prec>=CAP
    y=pi*(2*t).exp()
    acc=arb_series([arb(0)],prec=CAP)
    for m in range(1,MODES+1):
        acc+=m*m*(2*m*m*y-3)*(-m*m*y).exp()
    value=pi*(5*t/2).exp()*acc
    assert value.prec>=CAP
    assert all(value[k].is_finite() for k in range(CAP))
    full=arb_series([value[k]+errors[k] for k in range(CAP)],prec=CAP)
    assert full.prec>=CAP
    return full

h=arb(1)/128
totals=[arb(0) for _ in ORDERS]
for j in range(PANELS):
    t=arb_series([arb((2*j+1,-7)),arb(1)],prec=CAP)
    phi=theta16(t)
    for r,order in enumerate(ORDERS):
        g=t**order*phi
        assert g.prec>=CAP
        assert all(g[k].is_finite() for k in range(CAP))
        totals[r]+=sum((2*g[k]*h**(k+1)/(k+1)
                        for k in range(0,DEGREE+1,2)),arb(0))
    if (j+1)%32==0:
        print('PASS complete six-moment panels',j+1,'of',PANELS,flush=True)

quadrature_error=arb(0,ball(REM).upper())
tail=arb(0).union(ball(TEMPORAL_TAIL))
moments=[z+quadrature_error+tail for z in totals]
assert all(z.is_finite() and z>0 for z in moments)

# Z/Z0 is known only through degree10. Do not fill unknown higher terms.
coeffs=[arb(0) for _ in range(11)]
coeffs[0]=arb(1)
for r in range(1,6):
    coeffs[2*r]=moments[r]/(moments[0]*factorial(2*r))
Z=arb_series(coeffs,prec=11)
assert Z.prec>=11 and all(Z[k].is_finite() for k in range(11))
logZ=Z.log()
assert logZ.prec>=11
M=logZ.derivative()
assert M.prec>=10 and all(M[k].is_finite() for k in range(10))
a,b,c,d,e=[M[k] for k in (1,3,5,7,9)]
assert a>0 and b<0
H3=a*c*e-a*d*d-b*b*e+2*b*c*d-c**3
assert H3.is_finite()
assert H3>0 or H3<0,('INCONCLUSIVE fixed exact T_h-origin test',H3)
Th0=12*a*H3/(b**4)
print('PASS098: exact T_h(0) sign',
      'POSITIVE' if H3>0 else 'NEGATIVE',flush=True)
for order,z in zip(ORDERS,moments):print('I'+str(order),z,flush=True)
for name,z in [('a',a),('b',b),('c',c),('d',d),('e',e),('H3',H3),('Th0',Th0)]:
    print(name,z,flush=True)
print('EPS exact',EPS,'REM exact',REM,'TEMPORAL_TAIL exact',TEMPORAL_TAIL)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
