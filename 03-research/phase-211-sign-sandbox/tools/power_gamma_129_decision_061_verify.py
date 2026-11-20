"""Decide ONLY the previously unresolved gamma atom N129,k0,u31.5.
Exact rational ARCH0_032, all prime powers <=512, complete adverse tail.
"""
from fractions import Fraction as F
from math import comb,factorial,isqrt,prod
from functools import lru_cache
import power_fixed_grid_003 as C
N=129;d=N-1;u=F(63,2);M=512
norm=F(comb(2*d,d),63**(2*d+1))
# a_r=r!*[t^r]rho_N(t), with rho_N=e^-ut P_N(t), rho_N(0)=1.
a=[F(1)]
for r in range(1,N):a.append(a[-1]*2*u*F(d-r+1,2*d-r+1))
BER=C.B[:8];CUT=32
@lru_cache(None)
def hurwitz(p):
 center=sum((F(1,k**p) for k in range(16,CUT)),F())+F(1,(p-1)*CUT**(p-1))+F(1,2*CUT**p)
 for k,b in enumerate(BER,1):center+=b*prod(range(p,p+2*k-1))/F(factorial(2*k)*CUT**(p+2*k-1))
 err=abs(BER[-1])*prod(range(p,p+15))/F(factorial(16)*CUT**(p+15))
 return center-err,center+err
ARCH=sum((F(1,k) for k in range(1,16)),F())-C.gamma-C.logpi
for r in range(1,N):
 lo,hi=hurwitz(r+1);b=a[r]/2**r
 ARCH-=C.I(b*lo,b*hi)
assert ARCH.hi-ARCH.lo<F(1,10**18)
POLAR=F(2,(u*u-F(1,4))**N)/norm

def polynomial(t):
 v=C.I(a[-1])
 for r in range(d-1,-1,-1):v=a[r]+t*v/F(r+1)
 return v
powers=[]
for p in range(2,M+1):
 if all(p%q for q in range(2,isqrt(p)+1)):
  power=p
  while power<=M:powers.append((power,p));power*=p
powers.sort()
PRIME=C.I(0)
for power,p in powers:
 v=polynomial(C.logq(power))
 PRIME+=2*C.logq(p)*C.I(v.lo/power**32,v.hi/power**32)
assert PRIME.hi-PRIME.lo<F(1,10**40)
# For t>=log512>6, ROOT026 gives q_N(t)>16 and q_N is increasing.
assert C.log2.lo>F(2,3)
assert u*u>16**2+F(2*d*16,6)
LM=C.logq(M);vM=polynomial(LM)
wMhi=vM.hi/M**32 # exact positive normalized weight x^-1/2 rho(logx)
TAIL=2*M*wMhi*(F(2,31)*LM.hi+F(4,961))
assert 0<TAIL<F(1,10**24)
W=C.I(ARCH.lo+POLAR-PRIME.hi-TAIL,ARCH.hi+POLAR-PRIME.lo)
assert F(134,10**12)<W.lo<W.hi<F(135,10**12)
# Resolvent and sharp decomposition: same original normalization throughout.
RESOLVENT=2*sum((a[r]/32**(r+1) for r in range(N)),F())
SHARP=ARCH+RESOLVENT
ERR=C.I(PRIME.lo-POLAR+RESOLVENT,PRIME.hi+TAIL-POLAR+RESOLVENT)
assert -F(10422,10000)<SHARP.lo<SHARP.hi<-F(10421,10000)
assert -F(10422,10000)<ERR.lo<ERR.hi<-F(10421,10000)
# The guaranteed .66 from025 is not added: the actual ERR is independently enclosed.
# Using old audited .33<S129(2)<1/3, quantify all other cell contributions.
RESTLO=-ERR.hi-F(2,3);RESTHI=-ERR.lo-F(33,50)
assert RESTLO>F(3755,10000)
assert RESTHI<F(3822,10000)
def output(name,z):
 if isinstance(z,C.I):
  s=10**20
  print(name,'[',(z.lo*s).__floor__(),',',(z.hi*s).__ceil__(),']/10^20')
 else:print(name,float(z))
output('ARCH normalized',ARCH);output('POLAR normalized',C.I(POLAR))
output('PRIME through512 normalized',PRIME);output('complete prime tail upper',TAIL)
output('W normalized',W);output('ARCH sharp normalized',SHARP);output('ERR complete normalized',ERR)
print('PASS: unique historical atom N129,k0 has 1.34e-10 < W/norm squared <1.35e-10')
print('PASS: full cells n>=3 contribute between .3755 and .3822 to -ERR, without double counting first cell')
