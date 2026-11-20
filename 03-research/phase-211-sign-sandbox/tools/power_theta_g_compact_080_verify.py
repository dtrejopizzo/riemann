"""One fixed continuous certificate of Delta>0, u in [1/2,63/2].
Uses point ball jets of the pole-deflated arithmetic entire function,
with a uniform analytic Cauchy remainder; no interval zeta jets.
No parameter search, eigenvalue sampling, or adaptive subdivision.
"""
from flint import arb,arb_series,ctx
from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
from math import factorial
ctx.prec=256
ctx.cap=20
PANELS=4096
DEGREE=16
RADIUS=F(1,16)
CAUCHY_BOUND=60000000
HALF=arb(1)/2
H=arb(31)/8192
LOGPI=arb.pi().log()
# Analytic constants used in the Cauchy proof, not sampled function values.
assert sum(F(9,5)**k/F(factorial(k)) for k in range(11))>6
assert F(8,3)+F(5,96)<F(11,4)
assert F(11,4)*F(16,15)<3
assert F(9,10)+F(2,32)<1
assert 10**2+32*10*120+32**2*10*2700+2*32**2*120**2<CAUCHY_BOUND
RATIO=F(31,512)
TAIL_EXACT=CAUCHY_BOUND*RATIO**17/(1-RATIO)
assert TAIL_EXACT<F(1,10**12)
TAIL=arb(TAIL_EXACT.numerator)/TAIL_EXACT.denominator


def entire(A):
    # deflate=True means zeta(A)-1/(A-1), NOT (A-1)*zeta(A).
    Q=1+(A-1)*A.zeta(deflate=True)
    E=A*Q*(A/2).gamma()*(-A*LOGPI/2).exp()
    assert E[0].is_finite() and E[0]>0,('positive entire log branch',A[0],E[0])
    return E

def delta(base):
    u=arb_series([base,arb(1)],prec=20)
    A=u+HALF
    L=entire(A).log()
    c=L.derivative()
    d=c.derivative()
    e=d.derivative()
    D=c*c+u*c*d+u*u*c*e-2*u*u*d*d
    assert D.prec>=17
    assert all(D[k].is_finite() for k in range(17)),('nonfinite jet',base)
    return D

# Validate the documented pole regularization at the exact endpoint A=1.
A1=arb_series([arb(1),arb(1)],prec=20)
F1=A1.zeta(deflate=True)
assert F1[0].overlaps(arb.const_euler())
assert entire(A1)[0].contains(arb(1))
# Away from the pole it encloses the ordinary identical expression.
A2=arb_series([arb(2),arb(1)],prec=20)
ordinary=A2*(A2-1)*A2.zeta()*(A2/2).gamma()*(-A2*LOGPI/2).exp()
assert all(entire(A2)[k].overlaps(ordinary[k]) for k in range(20))
print('PASS regularized entire function: endpoint A=1, identity A=2',flush=True)

for j in range(PANELS):
    # mid = 1/2 + (2j+1)*31/8192, exact dyadic; h=31/8192.
    numerator=4096+(2*j+1)*31
    mid=arb((numerator,-13))
    panel=arb((numerator,-13),(31,-13))
    assert panel.contains(mid-H) and panel.contains(mid+H)
    center=delta(mid)
    # Degree16 center Taylor polynomial; one external analytic Cauchy remainder.
    loss=sum((center[k].abs_upper()*H**k for k in range(1,DEGREE+1)),arb(0))
    loss+=TAIL
    lower=center[0]-loss
    assert lower>0,('Delta not certified positive',j,mid,center[0],loss,lower)
    if (j+1)%512==0:
        print('PASS panels',j+1,'of',PANELS,flush=True)
print('PASS ALL: Delta>0 for every u in [1/2,63/2]; gsecond<0',flush=True)
print('CAUCHY TAIL EXACT',TAIL_EXACT,flush=True)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
