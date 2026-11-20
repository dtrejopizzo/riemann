"""One fixed origin Wronskian certificate for four theta densities, round087."""
from fractions import Fraction as F
from math import factorial,comb
from itertools import permutations
from hashlib import sha256
from pathlib import Path
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


# ONE prescribed point t=0. No interval/range search.
Q=[[F(-3),F(2)]]
for r in range(10):
 p=Q[-1];out=[F(0)]*(len(p)+1)
 for k,c in enumerate(p):
  out[k+1]-=2*c
  if k:out[k]+=2*k*c
 Q.append(out)
B=max(sum(abs(c) for c in p) for p in Q)
assert F(10,9)**24/F(2)**76<F(1,2)
assert sum(F(3)**k/F(factorial(k)) for k in range(8))>16
TAIL=2*B*3**11*F(9)**24/F(2)**324

def poly(p,x):
 r=I(0)
 for c in reversed(p):r=r*x+c
 return r
Sder=[I(-TAIL,TAIL) for r in range(11)]
for m in range(1,9):
 y=m*m*PI;em=I(1)/expi(y)
 for r in range(11):Sder[r]=Sder[r]+m*m*poly(Q[r],y)*em
# Phi(t)=pi*exp(5t/2)*S(t); retain the prefactor in ALL derivatives.
Phi=[PI*sum((comb(n,r)*F(5,2)**(n-r)*Sder[r] for r in range(n+1)),I(0)) for n in range(11)]
assert Phi[0].l>0
for n in range(1,11,2):
 assert Phi[n].l<=0<=Phi[n].h,('parity check',n)
a=[I(1)]+[Phi[2*j]/(factorial(2*j)*Phi[0]) for j in range(1,6)]
H=[]
for k in range(4):
 H.append([factorial(k)*a[k],factorial(k)*(2*k+3)*(2*k+2)*a[k+1],
           -factorial(k)*(2*k+2)*a[k+1],
           -factorial(k)*(2*k+4)*(2*k+3)*(2*k+2)*a[k+2]])
W=I(0)
for pp in permutations(range(4)):
 sign=(-1)**sum(pp[i]>pp[j] for i in range(4) for j in range(i+1,4))
 term=I(sign)
 for i in range(4):term=term*H[i][pp[i]]
 W=W+term
assert W.l>0 or W.h<0,('inconclusive',F(W.l,S),F(W.h,S))
print('CERTIFIED origin Wronskian sign:', 'POSITIVE' if W.l>0 else 'NEGATIVE')
print('Wronskian lower exact:',F(W.l,S))
print('Wronskian upper exact:',F(W.h,S))
print('TAIL each Sder exact:',TAIL)
print('Q coefficient bound exact:',B)
print('Parity checks Phi1,3,5,7,9: PASS')
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest())
