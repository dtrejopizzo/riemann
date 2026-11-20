"""Fixed rational certificate: (log Phi)''''<0 on [0,1/4]."""
from fractions import Fraction as F
from math import factorial,comb
S=10**70
class I:
 def __init__(self,a=0,b=None):
  if isinstance(a,I):self.l,self.h=a.l,a.h;return
  a=F(a);b=a if b is None else F(b)
  self.l=a.numerator*S//a.denominator; self.h=-((-b.numerator*S)//b.denominator)
 @classmethod
 def raw(cls,l,h):
  z=cls();z.l,z.h=l,h;return z
 def __add__(self,z):
  z=I(z);return I.raw(self.l+z.l,self.h+z.h)
 __radd__=__add__
 def __neg__(self):return I.raw(-self.h,-self.l)
 def __sub__(self,z):return self+-I(z)
 def __rsub__(self,z):return I(z)+-self
 def __mul__(self,z):
  z=I(z);v=[self.l*z.l,self.l*z.h,self.h*z.l,self.h*z.h];return I.raw(min(v)//S,-((-max(v))//S))
 __rmul__=__mul__
 def __truediv__(self,z):
  z=I(z);assert z.l>0;return self*I.raw(S*S//z.h,-((-S*S)//z.l))
 def __pow__(self,n):
  r=I(1);a=self
  while n:
   if n&1:r=r*a
   a=a*a;n//=2
  return r

def atan(x):
 x=F(x);z=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(128)),F(0));e=x**257/F(257)
 return I(z-e,z+e)
PI=16*atan(F(1,5))-4*atan(F(1,239))
assert PI.l>3*S and PI.h<4*S

def expi(x):
 # x in [0,128]; Taylor at x/128, then seven squarings.
 x=I(x);assert 0<=x.l<=x.h<=128*S
 v=x/128;t=I(1);r=t
 for k in range(1,129):t=t*v/k;r=r+t
 # v<=1: sum_{k>=129}v^k/k! <=2/129!.
 r=r+I(0,F(2,factorial(129)))
 for _ in range(7):r=r*r
 return r
Q=[[F(-3),F(2)]]
for r in range(4):
 p=Q[-1];out=[F(0)]*(len(p)+1)
 for k,c in enumerate(p):
  out[k+1]-=2*c
  if k:out[k]+=2*k*c
 Q.append(out)

def poly(p,x):
 r=I(0)
 for c in reversed(p):r=r*x+c
 return r
# All derivatives r<=4: |Q_r(y)|<=9600 y^5 for y>=1.
assert all(sum(abs(c) for c in p)<=9600 for p in Q)
# y^5 exp(-y) decreases y>=5; exp(3)>16.
assert sum(F(3)**k/F(factorial(k)) for k in range(8))>16
assert F(6,5)**12/F(2)**44<F(1,2)
TAIL=F(2*9600*3**5*5**12,2**100)
WORST=None
PANELS=4096
for z in range(PANELS):
 t=I(F(z,4*PANELS),F(z+1,4*PANELS));x=PI*expi(2*t)
 vals=[I(-TAIL,TAIL) for _ in range(5)]
 for m in range(1,5):
  y=m*m*x;e=I(1)/expi(y)
  for r in range(5):vals[r]=vals[r]+m*m*poly(Q[r],y)*e
 a,b,c,d,e=vals
 assert a.l>0
 # numerator of log-fourth, denominator a^4 positive.
 numer=e*a**3-4*d*b*a**2-3*c*c*a**2+12*c*b*b*a-6*b**4
 assert numer.h<0,(z,F(numer.h,S))
 upper=F(numer.h,S)/F(a.h,S)**4
 WORST=upper if WORST is None else max(WORST,upper)
print('PASS: 4096 fixed panels; log-fourth upper <',WORST)
print('Q polynomials:',Q)
print('derivative-tail bound:',TAIL)
