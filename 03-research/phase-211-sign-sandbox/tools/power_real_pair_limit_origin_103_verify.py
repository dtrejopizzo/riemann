"""One fixed real-pair double-limit origin test, round103.

The analytic limit proof and fixed moment design precede execution. All seven
moments include the complete theta and temporal tails. Either sign is accepted.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from hashlib import sha256
from flint import arb,arb_series,ctx

PANELS,DEGREE,CAP,PREC,MODES=128,64,65,512,16
ORDERS=tuple(range(7))
EPS=Q(2**25*17**4,8**289)
REM=2*10**12*Q(1,4)**65/(1-Q(1,4))
TEMPORAL_TAIL=Q(1,2**138)
assert Q(87,32)<3
assert 3*Q(15,16)*Q(511,512)>Q(5,2)
assert 3**5<256 and 3**6<1024
assert 4*1024*2051<2**24
assert 16*Q(1,8)**3<Q(1,2)
assert 3**6*2**22<10**12
assert Q(18,17)**4/Q(8)**35<Q(1,2)
assert REM<Q(1,10**24)
assert sum(Q(4)**k/Q(factorial(k)) for k in range(20))>54
assert 64*3**9<2**22
assert Q(9,2)-6*54<-300 and Q(1024,295)<4
assert sum(Q(2)**k/Q(factorial(k)) for k in range(6))>7
assert 7*Q(3,2)>8
print('PASS predeclared complete seven-moment bounds',flush=True)

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
    for r in ORDERS:
        g=t**r*phi
        assert g.prec>=CAP
        assert all(g[k].is_finite() for k in range(CAP))
        totals[r]+=sum((2*g[k]*h**(k+1)/(k+1)
                        for k in range(0,DEGREE+1,2)),arb(0))
    if (j+1)%32==0:
        print('PASS complete seven-moment panels',j+1,'of',PANELS,flush=True)

quadrature_error=arb(0,ball(REM).upper())
tail=arb(0).union(ball(TEMPORAL_TAIL))
moments=[z+quadrature_error+tail for z in totals]
assert all(z.is_finite() and z>0 for z in moments)
I0,I1,I2,I3,I4,I5,I6=moments

# Cleared polynomial; no nearly equal ratio subtraction decides the sign.
P=(-3*I0**2*I3*I6+5*I0**2*I4*I5
   +6*I0*I1*I2*I6-20*I0*I1*I4**2
   -15*I0*I2**2*I5+25*I0*I2*I3*I4
   +30*I1*I2**2*I4-30*I2**3*I3)
assert P.is_finite()
assert P>0 or P<0,('INCONCLUSIVE fixed double-limit origin test',P)

# Analytically positive denominators are checked before auxiliary readings.
Kmass_num=3*I2**2-I0*I4
Hmass_num=15*I2**2*I4-10*I0*I4**2+3*I0*I2*I6
assert Kmass_num>0 and Hmass_num>0
Kmass=Kmass_num/(6*I0)
Hmass=Hmass_num/(360*I0*I2)
a=I2/I0
b0=Kmass/I2
K0=a*I1-I3/2
H0=(b0/2-a/6)*I3+I5/24
Ulim0=P/(720*I0**2*Hmass)
print('PASS103: real-pair double-limit origin sign',
      'POSITIVE' if P>0 else 'NEGATIVE',flush=True)
for r,z in enumerate(moments):print('I'+str(r),z,flush=True)
for name,z in [('a',a),('b0',b0),('K0',K0),('Kmass',Kmass),
               ('H0',H0),('Hmass',Hmass),('P',P),('Ulim0',Ulim0)]:
    print(name,z,flush=True)
print('EPS exact',EPS,'REM exact',REM,'TEMPORAL_TAIL exact',TEMPORAL_TAIL)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
