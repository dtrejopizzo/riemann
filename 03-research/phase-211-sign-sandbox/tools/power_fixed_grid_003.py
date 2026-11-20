"""Exact rational enclosures; no floating point or numerical special functions."""
from fractions import Fraction as F
from math import comb
S=10**60

def down(x): return F((x*S).numerator//(x*S).denominator,S)
def up(x): return -down(-x)
class I:
 def __init__(self,a,b=None): self.lo=down(F(a)); self.hi=up(F(a if b is None else b))
 def __add__(self,o):
  o=cv(o); return I(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self): return I(-self.hi,-self.lo)
 def __sub__(self,o): return self+-cv(o)
 def __rsub__(self,o): return cv(o)+-self
 def __mul__(self,o):
  o=cv(o); v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=cv(o); assert not o.lo<=0<=o.hi; return self*I(1/o.hi,1/o.lo)
 def __repr__(self):
  return '['+str(float(self.lo))+','+str(float(self.hi))+']'
def cv(o):return o if isinstance(o,I) else I(o)
def log_unit(x):
 # x in [1,2]; atanh series with geometric tail.
 t=(F(x)-1)/(F(x)+1); v=sum((t**(2*j+1)/F(2*j+1) for j in range(120)),F(0))*2
 err=2*t**241/F(241)/(1-t*t)
 return I(v,v+err)
log2=log_unit(2)
def logq(x):
 x=F(x); k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 return log_unit(x)+k*log2

def atan_inv(q):
 v=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(100)),F(0))
 # 100 terms ends with negative term, next term positive.
 return I(v,v+F(1,201*q**201))
pi=16*atan_inv(5)-4*atan_inv(239)
logpi=I(logq(pi.lo).lo,logq(pi.hi).hi)
# Euler--Maclaurin gamma, remainder bounded by next term.
B=[F(1,6),F(-1,30),F(1,42),F(-1,30),F(5,66),F(-691,2730),F(7,6),F(-3617,510),F(43867,798),F(-174611,330),F(854513,138),F(-236364091,2730)]
N=1000
base=sum((F(1,j) for j in range(1,N+1)),F(0))-F(1,2*N)+sum((b/F(2*k*N**(2*k)) for k,b in enumerate(B,1)),F(0))
err=F(8553103,6)/F(26*N**26)
gamma=I(base-err,base+err)-logq(N)

def L(a):
 assert a>=32
 if a%2==0: psi=-gamma+sum((F(1,k) for k in range(1,a//2)),F(0))
 else: psi=-gamma-2*log2+2*sum((F(1,2*k-1) for k in range(1,(a-1)//2+1)),F(0))
 z=I(1); dz=I(0); M=50
 for k in range(2,M+1):
  z+=F(1,k**a); dz-=logq(k)/k**a
 tail=F(M,1)**(1-a)/F(a-1)
 dtail=F(M,1)**(1-a)*(logq(M)/F(a-1)+F(1,(a-1)**2))
 z+=I(0,tail);dz+=I(-dtail.hi,0)
 return F(1,a)+F(1,a-1)-logpi/2+psi/2+dz/z

def certificate(n):
 vals=[L(32+j) for j in range(n)]
 K=[[(vals[i]+vals[j])/F(63+i+j) for j in range(n)] for i in range(n)]
 piv=[]
 for k in range(n):
  p=K[k][k];assert p.lo>0,(k,p);piv.append(p)
  for i in range(k+1,n):
   for j in range(i,n):K[i][j]=K[j][i]=K[i][j]-K[i][k]*K[j][k]/p
 return vals,piv

def schur_parameters(vals):
 n=len(vals);x=[F(j,63+j) for j in range(n)]
 q=[(a-vals[0])/(a+vals[0]) for a in vals];q[0]=I(0)
 out=[]
 for r in range(n):
  assert -1<q[r].lo<=q[r].hi<1
  out.append(q[r])
  for j in range(r+1,n):
   q[j]=(q[j]-q[r])/(1-q[j]*q[r])/((x[j]-x[r])/(1-x[j]*x[r]))
 return out

if __name__=='__main__':
 vals,piv=certificate(6)
 for j,p in enumerate(piv):
  # Print certified decimal intervals by outward integer rounding.
  scale=10**30
  lo=(p.lo*scale).__floor__();hi=(p.hi*scale).__ceil__()
  print('pivot',j,'[',str(lo)+'/10^30,',str(hi)+'/10^30 ]')
 for j,p in enumerate(schur_parameters(vals)):
  scale=10**20
  lo=(p.lo*scale).__floor__();hi=(p.hi*scale).__ceil__()
  print('Schur',j,'[',str(lo)+'/10^20,',str(hi)+'/10^20 ]')
