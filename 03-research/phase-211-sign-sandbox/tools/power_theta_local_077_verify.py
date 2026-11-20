"""Fixed compact certificate for the local R-monotonicity criterion, round077."""
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
 # x in [0,2048]; Taylor at x/2048, then eleven squarings.
 x=I(x);assert 0<=x.l<=x.h<=2048*S
 v=x/2048;t=I(1);r=t
 for k in range(1,129):t=t*v/k;r=r+t
 # v<=1: sum_{k>=129}v^k/k! <=2/129!.
 r=r+I(0,F(2,factorial(129)))
 for _ in range(11):r=r*r
 return r

Q=[[F(-3),F(2)]]
for r in range(8):
 p=Q[-1];out=[F(0)]*(len(p)+1)
 for k,c in enumerate(p):
  out[k+1]-=2*c
  if k:out[k]+=2*k*c
 Q.append(out)
def poly(p,x):
 r=I(0)
 for c in reversed(p):r=r*x+c
 return r
CBOUND=max(sum(abs(c) for c in p) for p in Q)
assert CBOUND<10**12
# y>=3m^2>=147>9 and e^3>16, tail m>=7, all derivatives through8.
assert sum(F(3)**k/F(factorial(k)) for k in range(8))>16
assert F(8,7)**20/F(2)**60<F(1,2)
TAIL=2*CBOUND*3**9*F(7)**20/F(2)**196

def derivatives(t,n):
 x=PI*expi(2*t);v=[I(-TAIL,TAIL) for _ in range(n+1)]
 for m in range(1,7):
  y=m*m*x;e=I(1)/expi(y)
  for r in range(n+1):v[r]=v[r]+m*m*poly(Q[r],y)*e
 assert v[0].l>0
 log=[I(0)]
 for r in range(1,n+1):
  log.append((v[r]-sum((comb(r-1,k-1)*log[k]*v[r-k] for k in range(1,r)),I(0)))/v[0])
 V=[I(0),-log[1]-F(5,2)]+[-log[r] for r in range(2,n+1)]
 return V

def add(a,b):return [a[i]+b[i] for i in range(4)]
def neg(a):return [-v for v in a]
def mul(a,b):return [sum((comb(i,k)*a[k]*b[i-k] for k in range(i+1)),I(0)) for i in range(4)]
def scale(a,k):return [k*v for v in a]
def coeff(t,v):
 x=[t,I(1),I(0),I(0)];p=v[1:5];q=v[2:6];r=v[3:7]
 C=add(add(mul(mul(p,p),p),mul(mul(mul(x,p),p),q)),add(neg(mul(p,q)),add(neg(mul(mul(x,p),r)),mul(x,mul(q,q)))))
 return C
v0=derivatives(I(0),6);a=v0[2];b=v0[4]
assert a.l>0 and b.l>0
assert (2*a*a-b).l>0
ORIGIN=1024
for z in range(ORIGIN):
 lo=F(z,16*ORIGIN);hi=F(z+1,16*ORIGIN);mid=(lo+hi)/2;rad=(hi-lo)/2
 vc=derivatives(I(mid),8);vv=derivatives(I(lo,hi),8)
 # Second-order Taylor enclosure of V6; its degree2 coefficient uses V8.
 whole=vc[6]+I(-rad,rad)*vc[7]+I(0,rad*rad/2)*vv[8]
 assert whole.h<0,('origin V6',z,F(whole.h,S))
print('PASS origin: V6<0 on [0,1/16], b<2a^2',flush=True)
REST=8192
for z in range(REST):
 lo=F(1,16)+F(15*z,16*REST);hi=lo+F(15,16*REST);mid=(lo+hi)/2;rad=(hi-lo)/2
 vv=derivatives(I(lo,hi),6);cc=coeff(I(lo,hi),vv)
 vc=derivatives(I(mid),6);ct=coeff(I(mid),vc)
 x=I(mid);p,q,r,ss=vc[1:5]
 N=(x*q-p)*ct[1]-x*r*ct[0]
 Np=(x*q-p)*ct[2]-(r+x*ss)*ct[0]
 x=I(lo,hi);p,q,r,ss,tt=vv[1:6]
 Npp=x*r*cc[2]+(x*q-p)*cc[3]-(2*ss+x*tt)*cc[0]-(r+x*ss)*cc[1]
 Nwhole=N+I(-rad,rad)*Np+I(0,rad*rad/2)*Npp
 Cwhole=ct[0]+I(-rad,rad)*ct[1]+I(0,rad*rad/2)*cc[2]
 assert Cwhole.l>0,('C',z,F(Cwhole.l,S))
 assert Nwhole.l>0,('L derivative',z,F(Nwhole.l,S))
print('PASS rest: C>0 and Lprime<0 on [1/16,1], fixed 8192 panels',flush=True)
print('TAIL all m>=7:',TAIL)
