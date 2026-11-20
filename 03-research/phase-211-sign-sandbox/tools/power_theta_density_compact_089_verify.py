"""Two fixed continuous R4-density certificates, with complete complex theta tails.
Origin uses the even lambda jet, rest the raw temporal Wronskian.
Parameters and mathematical remainder bounds are fixed in the source089 design.
"""
from flint import arb,arb_series,ctx
from fractions import Fraction as Q
from math import factorial
from itertools import combinations
from pathlib import Path
from hashlib import sha256
MODES=16
# Constants proved before either run.
assert Q(87,32)<Q(25,9)
assert Q(3,5)*Q(7,8)>Q(1,2)
assert Q(5,3)*Q(8,7)<2
assert sum(Q(3)**k/Q(factorial(k)) for k in range(12))>16
assert Q(16,4**3)<Q(1,2)
assert 2*Q(152,4)<1000
assert Q(18,17)**4/Q(4)**35<Q(1,2)
assert 3*Q(56,81)>Q(33,16)
assert 4*Q(56,81)>Q(165,64)
assert 3*(1-Q(1,16)**2/2)>Q(5,2)
assert sum(Q(2)**k/Q(factorial(k)) for k in range(6))>7
assert 7*Q(3,2)>8
assert Q(16,8**3)<Q(1,2)
assert 2*Q(4288,8)<10000
assert Q(18,17)**4/Q(8)**35<Q(1,2)

ORIGIN_PANELS,ORIGIN_CAP,ORIGIN_DEGREE=1024,23,16
REST_PANELS,REST_CAP,REST_DEGREE=8192,47,40
EPS_ORIGIN=Q(304*17**4,4**289)
EPS_REST=Q(8576*17**4,8**289)
REM_ORIGIN=10**48*Q(1,8192)**17/(1-Q(1,8192))
REM_REST=10**60*Q(15,4096)**41/(1-Q(15,4096))
assert REM_ORIGIN<Q(1,10**18) and REM_REST<Q(1,10**39)
P=lambda k:1000*factorial(k)*32**k
OC=[max(P(j) for j in range(4)),
    max((6+4*j)*P(j+1)+Q(1,8)*P(j+2) for j in range(4)),
    max(2*P(j+1) for j in range(4)),
    max((12+8*j)*P(j+2)+Q(1,4)*P(j+3) for j in range(4))]
assert OC==[196608000,956301312000,50331648000,338228674560000]
prod=24
for x in OC:prod*=x
assert prod<10**48
P=lambda k:10000*factorial(k)*64**k
RC=[2*P(3)+3*P(2),2*P(5)+5*P(4),P(4),P(6)]
prod=24
for x in RC:prod*=x
assert prod<10**60
print('PASS all predeclared analytic bounds and exact remainders',flush=True)

def ball(q):return arb(q.numerator)/q.denominator

def theta16(t,cap,pi):
    assert t.prec>=cap
    y=pi*(2*t).exp()
    acc=arb_series([arb(0)],prec=cap)
    for m in range(1,MODES+1):
        acc+=m*m*(2*m*m*y-3)*(-m*m*y).exp()
    value=pi*(5*t/2).exp()*acc
    assert value.prec>=cap
    assert all(value[k].is_finite() for k in range(cap))
    return value

def coefficient_errors(eps,cap):
    e=ball(eps)
    return [arb(0,(e*32**k).upper()) for k in range(cap)]

def with_tail(value,errors,cap):
    assert value.prec>=cap
    result=arb_series([value[k]+errors[k] for k in range(cap)],prec=cap)
    assert result.prec>=cap
    assert all(result[k].is_finite() for k in range(cap))
    return result

def det4(rows,cap):
    # Laplace along the first two rows: six products of 2x2 minors, no divisions.
    out=arb_series([arb(0)],prec=cap)
    for i,j in combinations(range(4),2):
        k,l=[x for x in range(4) if x not in (i,j)]
        top=rows[0][i]*rows[1][j]-rows[0][j]*rows[1][i]
        bottom=rows[2][k]*rows[3][l]-rows[2][l]*rows[3][k]
        out+=(-1)**(i+j+1)*top*bottom
    return out

def wronskian(cols,cap,degree):
    rows=[cols]
    for _ in range(3):rows.append([f.derivative() for f in rows[-1]])
    W=det4(rows,cap)
    assert W.prec>=degree+1
    assert all(W[k].is_finite() for k in range(degree+1))
    return W

def certify_negative(W,h,rem,degree,label,j,mid):
    loss=sum((W[k].abs_upper()*h**k for k in range(1,degree+1)),arb(0))+rem
    upper=W[0]+loss
    assert upper<0,(label,'not certified',j,mid,W[0],loss,upper)

# ORIGIN: all lambda centers are positive; the average is analytically even.
ctx.prec=1024;ctx.cap=ORIGIN_CAP
pi=arb.pi();errors=coefficient_errors(EPS_ORIGIN,ORIGIN_CAP)
h=arb(1)/524288;rem=ball(REM_ORIGIN)
for j in range(ORIGIN_PANELS):
    n=2*j+1;mid=arb((n,-19));panel=arb((n,-19),(1,-19))
    assert mid>0 and panel.contains(mid-h) and panel.contains(mid+h)
    lam=arb_series([mid,arb(1)],prec=ORIGIN_CAP)
    t=lam.sqrt()
    even=(theta16(t,ORIGIN_CAP,pi)+theta16(-t,ORIGIN_CAP,pi))/2
    phi=with_tail(even,errors,ORIGIN_CAP)
    p1=phi.derivative();p2=p1.derivative();p3=p2.derivative()
    cols=[phi,6*p1+4*lam*p2,-2*p1,-12*p2-8*lam*p3]
    W=wronskian(cols,ORIGIN_CAP,ORIGIN_DEGREE)
    certify_negative(W,h,rem,ORIGIN_DEGREE,'ORIGIN',j,mid)
    if (j+1)%128==0:print('PASS origin lambda panels',j+1,'of',ORIGIN_PANELS,flush=True)
print('PASS ORIGIN: W_lambda(Psi)<0 everywhere on [0,1/256]',flush=True)

# REST: raw density Wronskian; no division by Phi or t.
ctx.prec=512;ctx.cap=REST_CAP
pi=arb.pi();errors=coefficient_errors(EPS_REST,REST_CAP)
h=arb(15)/262144;rem=ball(REM_REST)
for j in range(REST_PANELS):
    n=16384+(2*j+1)*15;mid=arb((n,-18));panel=arb((n,-18),(15,-18))
    assert panel.contains(mid-h) and panel.contains(mid+h)
    t=arb_series([mid,arb(1)],prec=REST_CAP)
    phi=with_tail(theta16(t,REST_CAP,pi),errors,REST_CAP)
    p1=phi.derivative();p2=p1.derivative();p3=p2.derivative()
    tphi=t*phi
    cols=[tphi,tphi.derivative().derivative(),-p1,-p3]
    W=wronskian(cols,REST_CAP,REST_DEGREE)
    certify_negative(W,h,rem,REST_DEGREE,'REST',j,mid)
    if (j+1)%512==0:print('PASS rest t panels',j+1,'of',REST_PANELS,flush=True)
print('PASS REST: raw W_t(rho4)<0 everywhere on [1/16,1]',flush=True)
print('PASS ALL: R4 density Wronskian negative on the entire missing compact',flush=True)
print('EPS ORIGIN',EPS_ORIGIN,'EPS REST',EPS_REST,flush=True)
print('REM ORIGIN',REM_ORIGIN,'REM REST',REM_REST,flush=True)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
