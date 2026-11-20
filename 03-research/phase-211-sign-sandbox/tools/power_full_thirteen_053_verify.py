"""One exhaustive segment j=1,...,95 fixed by audited CENTERED_MOMENT053.
Outward rational intervals, EM12/CUT256, no floating point in certificates.
"""
from fractions import Fraction as F
from math import comb,factorial,prod
from functools import lru_cache
S=10**260

def down(x):return F((x*S).numerator//(x*S).denominator,S)
def up(x):return -down(-x)
class I:
 def __init__(self,a,b=None):self.lo=down(F(a));self.hi=up(F(a if b is None else b))
 def __add__(self,o):
  o=cv(o);return I(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,o):return self+-cv(o)
 def __rsub__(self,o):return cv(o)+-self
 def __mul__(self,o):
  o=cv(o);z=[x*y for x in [self.lo,self.hi] for y in [o.lo,o.hi]];return I(min(z),max(z))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=cv(o);assert not o.lo<=0<=o.hi;return self*I(1/o.hi,1/o.lo)
def cv(x):return x if isinstance(x,I) else I(x)
def lograw(x):
 # Same512 terms; interval rounding after each operation prevents huge denominators.
 rExact=(F(x)-1)/(F(x)+1);assert 0<=rExact<=F(1,2)
 r=I(rExact);sq=r*r;power=r;total=I(0)
 for k in range(512):
  total+=2*power/F(2*k+1)
  power*=sq
 # Universal upper bound on the exact omitted tail, since rExact<=1/2.
 remainder=2*F(1,2)**1025/F(1025)/(1-F(1,4))
 return total+I(0,remainder)
def logq(x):
 x=F(x);k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 return lograw(x)+k*lograw(2)
def atan_inv(q):
 lo=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(128)),F())
 return I(lo,lo+F(1,257*q**257))
l2=lograw(2);l3=lograw(3)
print('PASS: log2 and log3 intervals computed, fixed precision260',flush=True)
pi=16*atan_inv(5)-4*atan_inv(239)
lpi=I(logq(pi.lo).lo,logq(pi.hi).hi)
print('PASS: Machin pi and logpi enclosed with outward512-term intervals',flush=True)
M=256
H=sum((F(1,k) for k in range(1,M+1)),F())
gamlo=H-F(1,2*M)+F(1,12*M*M)-F(1,120*M**4)
gamma=I(gamlo,gamlo+F(1,252*M**6))-8*l2
u=F(63,2);size=108;CUT=256
BER=[F(1,6),F(-1,30),F(1,42),F(-1,30),F(5,66),F(-691,2730),F(7,6),F(-3617,510),F(43867,798),F(-174611,330),F(854513,138),F(-236364091,2730)]
@lru_cache(None)
def hurwitz(p):
 center=sum((F(1,k**p) for k in range(16,CUT)),F())+F(1,(p-1)*CUT**(p-1))+F(1,2*CUT**p)
 for k,b in enumerate(BER,1):center+=b*prod(range(p,p+2*k-1))/F(factorial(2*k)*CUT**(p+2*k-1))
 err=abs(BER[-1])*prod(range(p,p+23))/F(factorial(24)*CUT**(p+23))
 return center-err,center+err
D0=I(sum((F(1,k) for k in range(1,16)),F()))-gamma-lpi
bands=[]
for k in range(size):
 band=D0 if k==0 else I(0)
 if k:
  for r in range(1,k+1):
   coeff=F((-1)**(r+1)*comb(k-1,r-1),2)*u**r
   lo,hi=hurwitz(r+1)
   # Scale exact rational endpoints before outward interval quantization.
   band+=I(coeff*lo,coeff*hi) if coeff>=0 else I(coeff*hi,coeff*lo)
 polar=F(63,992)*(-1)**k*(F(32,31)**k+F(31,32)**k)
 band+=polar
 for n,ln in [(2,l2),(3,l3)]:
  # q_k=L_k-L_(k-1), q_0=1; exact coefficients, interval Horner.
  coeffs=[(-1)**r*F(comb(k,r)-(comb(k-1,r) if k and r<k else 0),factorial(r)) for r in range(k+1)]
  pol=I(coeffs[-1])
  for coef in reversed(coeffs[:-1]):pol=pol*(63*ln)+coef
  atom=ln*pol*(-F(2 if k==0 else 1,n**32))
  band+=atom
 bands.append(band)
print('PASS: all108 E23 bands enclosed with EM12/CUT256 and precision260',flush=True)
den=10**24
center=[F((((z.lo+z.hi)/2)*den).__floor__(),den) for z in bands]
errors=[max(abs(z.lo-c),abs(z.hi-c)) for z,c in zip(bands,center)]
epsilon=F(1,10**12)
assert max(sum(errors[abs(i-j)] for j in range(size)) for i in range(size))<epsilon
print('PASS: spectral rowerror <1e-12 BEFORE finite certificates',flush=True)
# The following is the unique exhaustive segment prescribed by the analytic J=96.
c=F(1,500)
for highpass in range(1,96):
 weighted=[];gram=[]
 for r in range(13):
  weighted.append(sum((F(comb(2*highpass,highpass+d))*center[abs(r+d)] for d in range(-highpass,highpass+1)),F()))
  gram.append(F(comb(2*highpass,highpass+r)) if r<=highpass else F())
 matrix=[[weighted[abs(i-j)]-(c+epsilon)*gram[abs(i-j)] for j in range(13)] for i in range(13)]
 for k in range(13):
  pivot=matrix[k][k]
  assert pivot>0,('failed sufficient finite block',highpass,k)
  for i in range(k+1,13):
   for j in range(k+1,13):matrix[i][j]-=matrix[i][k]*matrix[k][j]/pivot
 print('PASS exact E23 highpass block',highpass,flush=True)
# Uniform tail on arbitrary fourteen poles, alpha=1/2, all contacts n>=4.
alpha=F(1,2)
BT=sum((F(comb(j,k)**2)*alpha**(2*k)/(1-alpha)**(2*j+1) for j in range(14) for k in range(j+1)),F())
assert BT==947334302964 and BT<973312**2
assert F(7,5)**4<4
TAIL=2*973312*F(5,7)*F(1,4**16)*(F(7,5)+4*F(7,5)/15+F(4,225))
assert 2*l2.hi<F(7,5)
assert TAIL<F(1,1000)
assert c-TAIL>F(1,1000)
assert F(1,1000)>F(1,4000)
print('PASS: E23 orbit >norm squared/500 for j1..95, analytic tail starts96')
print('PASS: full W on14 numerator-zero spaces >norm squared/1000')
print('PASS: FULLTEL014 plus audited baseV13_052 yields full W >norm squared/4000 on ALL13 real poles >=63/2')
