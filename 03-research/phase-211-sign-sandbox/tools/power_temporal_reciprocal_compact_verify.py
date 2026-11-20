"""Fixed Arb certificate for the temporal reciprocal q(u)=sqrt(u)/p(sqrt(u)).

No parameter search: 512 bits, 16 modes, origin degree 40 / 256 panels,
rest 8192 panels. Full theta tails and Taylor remainders are included.
"""
from flint import arb, arb_series, ctx
from fractions import Fraction as F
from math import factorial
from hashlib import sha256
from pathlib import Path

BITS, MODES, DEGREE, OPANELS, RPANELS = 512, 16, 40, 256, 8192
ctx.prec = BITS
ctx.cap = 2 * DEGREE + 3
def ball(q):
    q = F(q)
    return arb(q.numerator) / q.denominator
def interval(lo, hi):
    return arb(ball((lo + hi) / 2), ball((hi - lo) / 2).upper())
def err(q):
    return arb(0, ball(q).upper())

# The complex origin bound is 089 section 2: |Phi(z)|<1000 on |z|<=1/4.
# Mode tail <=304*17^4/4^289 on this disk (ratio <1/2).
EPS_O = F(304 * 17**4, 4**289)
assert F(18, 17)**4 / 4**35 < F(1, 2)
# For real centers r in [1/8,1], on |z-r|<=1/64:
# Re exp(2z)>1; |exp(2z)|<9, |exp(5z/2)|<16.
# Hence |Phi_m(z)|<4800*m^4*8^(-m^2), using exp(3)>8.
assert (1 + F(7, 32)) * (1 - F(1, 2048)) > 1
assert sum(F(3)**k / factorial(k) for k in range(5)) > 8
assert F(16,8**3) < F(1,2)
assert F(18, 17)**4 / 8**35 < F(1, 2)
EPS_R = F(9600 * 17**4, 8**289)
pi = arb.pi()
assert pi > 3 and pi < 4
assert ball(F(65, 32)).exp() < 9
assert ball(F(325, 128)).exp() < 16

def theta(t, cap):
    y = pi * (2*t).exp()
    out = arb_series([0], prec=cap)
    for m in range(1, MODES+1):
        out += m*m * (2*m*m*y-3) * (-m*m*y).exp()
    return pi * (5*t/2).exp() * out

# Extract the even coefficients of the FULL even function, not of its prefix.
cap = 2*DEGREE+3
raw = theta(arb_series([0, 1], prec=cap), cap)
full = [raw[j] + err(EPS_O * 4**j) for j in range(cap)]
assert all(full[j].contains(0) for j in range(1, cap, 2))
coeff = [full[2*k] for k in range(DEGREE+1)]

def deriv_poly(j, u):
    out = arb(0)
    for k in range(DEGREE, j-1, -1):
        out = out*u + coeff[k] * (factorial(k)//factorial(k-j))
    # Cauchy |[u^k]f|<=1000*16^k, radius 1/16.
    # For k>=41 and j<=3 the successive positive tail ratio is <1/2
    # throughout u<=1/64. Include twice its first term.
    k = DEGREE+1
    assert F(k+1, k+1-j) * F(1, 4) < F(1, 2)
    rem = 2000 * F(factorial(k), factorial(k-j)) * 16**k * F(1,64)**(k-j)
    return out + err(rem)

min_origin = None
for j in range(OPANELS):
    u = interval(F(j,64*OPANELS), F(j+1,64*OPANELS))
    f, d1, d2, d3 = [deriv_poly(k,u) for k in range(4)]
    assert f > 0 and d1 < 0, ('origin a positivity',j,f,d1)
    # a''=-2(log f)'''<0: avoid dividing the near-origin temporal jets.
    L3 = d3*f*f - 3*d2*d1*f + 2*d1**3
    assert L3 > 0, ('origin a second derivative',j,L3)
    if min_origin is None or L3.lower() < min_origin:
        min_origin = L3.lower()
print('PASS origin: a>0 and a_second<0, u=[0,1/64], panels=256', flush=True)
print('origin log-third numerator lower:', min_origin, flush=True)

RDEGREE, RCAP = 24, 28
ctx.cap = RCAP
# |Phi|<10000 on every radius-1/64 disk centered in [1/8,1].
assert 2*F(4800,8) < 10000
# On the smaller radius-1/128 disks, derivatives j<=3 satisfy Pj.
P = [10000*factorial(j)*128**j for j in range(4)]
B = 4*(P[1]**2*P[2]+2*P[0]*P[2]**2+P[0]*P[1]*P[3])
B += 2*(P[1]**3+P[0]*P[1]*P[2])+P[0]*P[1]**2
assert B < 10**24
halfwidth = F(7,16*RPANELS)
ratio = 128*halfwidth
REM_R = 10**24*ratio**(RDEGREE+1)/(1-ratio)
assert REM_R < F(1,10**30)
min_n = None
for j in range(RPANELS):
    lo = F(1,8) + F(7*j,8*RPANELS)
    hi = F(1,8) + F(7*(j+1),8*RPANELS)
    r = arb_series([ball((lo+hi)/2),1],prec=RCAP)
    raw = theta(r,RCAP)
    f = arb_series([raw[k]+err(EPS_R*64**k) for k in range(RCAP)],prec=RCAP)
    d1 = f.derivative()
    d2 = d1.derivative()
    d3 = d2.derivative()
    # T = N*Phi^3, an entire polynomial; no reciprocals near the origin.
    T = -r*r*d1*d1*d2+2*r*r*f*d2*d2-r*r*f*d1*d3
    T += r*d1**3-r*f*d1*d2-f*d1*d1
    loss = sum((T[k].abs_upper()*ball(halfwidth)**k
                for k in range(1,RDEGREE+1)),arb(0))+ball(REM_R)
    lower = T[0]-loss
    assert lower > 0, ('reciprocal polynomial',j,lo,hi,lower)
    if min_n is None or lower.lower() < min_n:
        min_n = lower.lower()
print('PASS rest: N*Phi^3>0, r=[1/8,1], panels=8192, Taylor degree=24',flush=True)
print('rest N*Phi^3 lower:', min_n,flush=True)
print('rest Taylor remainder exact:',REM_R,flush=True)
print('EPS_ORIGIN exact:',EPS_O)
print('EPS_REST exact:',EPS_R)
print('FULL PASS temporal reciprocal compact; no floating-point tests')
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest())
