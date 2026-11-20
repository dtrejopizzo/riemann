"""One fixed particular-origin sign: three complete theta moments, round093.

All parameters and analytic errors were fixed and independently audited in
POWER_PARTICULAR_ORIGIN_DESIGN_093.md before this implementation.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from hashlib import sha256
import runpy
from flint import arb, arb_series, ctx

PANELS, DEGREE, CAP, PREC, MODES = 128, 64, 65, 512, 16
EPS = Q(2**25*17**4, 8**289)
REM = 2*10**8*Q(1,4)**65/(1-Q(1,4))
TEMPORAL_TAIL = Q(1,2**140)
assert Q(87,32)<3
assert 3*Q(15,16)*Q(511,512)>Q(5,2)
assert 3**5<256 and 3**6<1024
assert 4*1024*2051<2**24
assert 16*Q(1,8)**3<Q(1,2)
assert 9*2**22<10**8
assert Q(18,17)**4/Q(8)**35<Q(1,2)
assert REM<Q(1,10**28)
assert sum(Q(4)**k/Q(factorial(k)) for k in range(20))>54
assert 64*3**9<2**22
assert Q(9,2)-6*54<-300 and Q(4,298)<1
assert sum(Q(2)**k/Q(factorial(k)) for k in range(6))>7
assert 7*Q(3,2)>8
print('PASS predeclared analytic bounds', flush=True)

# Reuse the unchanged single-point rational certificate087, never its mesh.
data = runpy.run_path(str(Path(__file__).resolve().parent /
                         'power_theta_density_origin_087_verify.py'))
ctx.prec, ctx.cap = PREC, CAP

def ball(q):
    return arb(q.numerator)/q.denominator

def from087(z):
    lo=arb(z.l)/data['S']
    hi=arb(z.h)/data['S']
    return lo.union(hi)

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
totals=[arb(0),arb(0),arb(0)]
for j in range(PANELS):
    mid=arb((2*j+1,-7))
    t=arb_series([mid,arb(1)],prec=CAP)
    phi=theta16(t)
    functions=[phi,t*phi,t*t*phi]
    for r,g in enumerate(functions):
        assert g.prec>=CAP
        assert all(g[k].is_finite() for k in range(CAP))
        totals[r]+=sum((2*g[k]*h**(k+1)/(k+1)
                       for k in range(0,DEGREE+1,2)),arb(0))
    if (j+1)%32==0:
        print('PASS complete moment panels',j+1,'of',PANELS,flush=True)

quadrature_error=arb(0,ball(REM).upper())
tail=arb(0).union(ball(TEMPORAL_TAIL))
moments=[z+quadrature_error+tail for z in totals]
assert all(z.is_finite() and z>0 for z in moments)
I0,I1,I2=moments
Phi0=from087(data['Phi'][0])
assert Phi0>0
a1,a2,a3,a4=[from087(z) for z in data['a'][1:5]]
P=192*(6*a1*a3*a4-8*a2*a2*a4+3*a2*a3*a3)
Qc=ball(Q(16,35))*(126*a1**3*a4-51*a1*a1*a2*a3+10*a1*a2**3
       -588*a1*a2*a4+210*a1*a3*a3+30*a2*a2*a3+420*a3*a4)
R=-ball(Q(192,35))*(28*a1*a1*a2*a4-20*a1*a1*a3*a3+2*a1*a2*a2*a3
       -70*a1*a3*a4+56*a2*a2*a4-15*a2*a3*a3)
NUM=Qc*Phi0*I0+P*I1*I0+(R-P)*Phi0*I2
assert NUM.is_finite()
assert NUM>0 or NUM<0,('INCONCLUSIVE fixed particular-origin sign',NUM)
Dpart=NUM/(Phi0*I2)
print('PASS093: particular-origin determinant sign',
      'POSITIVE' if NUM>0 else 'NEGATIVE',flush=True)
for name,z in [('I0',I0),('I1',I1),('I2',I2),('a',I2/I0),
               ('tau0',I1/Phi0),('NUM',NUM),('Dpart',Dpart)]:
    print(name,z,flush=True)
print('EPS exact',EPS,'REM exact',REM,'TEMPORAL_TAIL exact',TEMPORAL_TAIL)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
