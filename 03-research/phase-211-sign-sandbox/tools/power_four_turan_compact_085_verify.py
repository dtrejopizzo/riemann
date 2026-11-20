"""Fixed continuous NR>0, NS>0 certificate for all u in [1/2,255/2].
Point-only rigorous entire arithmetic jets, with one uniform analytic Cauchy tail.
No sampled eigenvalues, adaptive panels, or parameter search.
"""
from flint import arb,arb_series,ctx
from fractions import Fraction as Q
from math import factorial
from hashlib import sha256
from pathlib import Path
ctx.prec=512
ctx.cap=45
PANELS=16384
DEGREE=40
H=arb(127)/32768
LOGPI=arb.pi().log()
CAUCHY_BOUND=10**20
RATIO=Q(127,1024)
TAIL_EXACT=CAUCHY_BOUND*RATIO**41/(1-RATIO)
assert TAIL_EXACT<Q(1,10**16)
TAIL=arb(TAIL_EXACT.numerator)/TAIL_EXACT.denominator
# Exact analytical constant checks for the Cauchy proof.
assert sum(Q(11,10)**k/Q(factorial(k)) for k in range(11))>3
assert Q(33,20)+Q(2,129)<2
assert 3*2*(Q(1,3)+Q(1,3)**3/3)>Q(33,16)
a1,a2,a3,a4=32,64,192,768
assert a2+a1*a1<1100
assert a3+3*a1*a2+2*a1**3<72000
assert a4+4*a1*a3+3*a2*a2+12*a1*a1*a2+6*a1**4<8*10**6
C,D,E,F=32,128*1100,128**2*72000,128**3*8*10**6
BOUND=3*C*C+C*(6*D+6*E+2*F)+9*D*D+6*D*E+2*D*F+3*E*E
assert BOUND<CAUCHY_BOUND

def entire(A):
    # Official deflate: zeta(A)-1/(A-1), finite at A=1.
    reg=1+(A-1)*A.zeta(deflate=True)
    Z=A*reg*(A/2).gamma()*(-A*LOGPI/2).exp()
    assert Z[0].is_finite() and Z[0]>0,('real entire log branch',A[0],Z[0])
    return Z

def numerators(base):
    u=arb_series([base,arb(1)],prec=45)
    L=entire(u+arb(1)/2).log()
    c=L.derivative();d=c.derivative();e=d.derivative();f=e.derivative()
    D=u*d;E=u*u*e;F=u*u*u*f
    NR=3*c*c+c*(-6*D-6*E-2*F)+3*D*D+6*D*E+2*D*F-3*E*E
    NS=3*c*c+c*(6*D+6*E+2*F)-9*D*D-6*D*E+2*D*F-3*E*E
    for name,N in [('NR',NR),('NS',NS)]:
        assert N.prec>=41,(name,N.prec)
        assert all(N[k].is_finite() for k in range(41)),(name,'nonfinite',base)
    return NR,NS

# Endpoint/identity tests of the documented representation, not sign samples.
A1=arb_series([arb(1),arb(1)],prec=45)
assert A1.zeta(deflate=True)[0].overlaps(arb.const_euler())
assert entire(A1)[0].contains(arb(1))
A2=arb_series([arb(2),arb(1)],prec=45)
ordinary=A2*(A2-1)*A2.zeta()*(A2/2).gamma()*(-A2*LOGPI/2).exp()
regular=entire(A2)
assert all(regular[k].overlaps(ordinary[k]) for k in range(45))
print('PASS analytical constants and entire representation',flush=True)

for j in range(PANELS):
    n=16384+(2*j+1)*127
    mid=arb((n,-15))
    panel=arb((n,-15),(127,-15))
    assert panel.contains(mid-H) and panel.contains(mid+H)
    NR,NS=numerators(mid)
    for name,N in [('NR',NR),('NS',NS)]:
        loss=sum((N[k].abs_upper()*H**k for k in range(1,41)),arb(0))+TAIL
        lower=N[0]-loss
        assert lower>0,(name,'not certified',j,mid,N[0],loss,lower)
    if (j+1)%1024==0:
        print('PASS NR+NS panels',j+1,'of',PANELS,flush=True)
print('PASS ALL: NR>0 and NS>0 for every u in [1/2,255/2]',flush=True)
print('CAUCHY BOUND INTEGER',BOUND,flush=True)
print('CAUCHY TAIL EXACT',TAIL_EXACT,flush=True)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
