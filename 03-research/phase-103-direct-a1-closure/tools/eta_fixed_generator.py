#!/usr/bin/env python3
"""Fixed-point Euler/Hasse generator, with the k,j sums interchanged.

The finite eta coefficients use W_j exactly; all transcendental logs are
outward rational intervals before their fixed-point quantization.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import runpy

P=500; S=10**P
em=runpy.run_path(str(Path(__file__).with_name('stieltjes_em_interval_pilot.py')))
I=em['I']
def fl(q): return q.numerator*S//q.denominator
def ce(q): return -((-q.numerator*S)//q.denominator)
class F:
 def __init__(s,l,h=None):s.l=int(l);s.h=int(l if h is None else h)
 def __add__(a,b):b=X(b);return F(a.l+b.l,a.h+b.h)
 def __sub__(a,b):b=X(b);return F(a.l-b.h,a.h-b.l)
 def __mul__(a,b):
  b=X(b)
  if a.l>=0 and b.l>=0:
   return F((a.l*b.l)//S,-((-(a.h*b.h))//S))
  if a.h<=0 and b.h<=0:
   return F((a.h*b.h)//S,-((-(a.l*b.l))//S))
  v=(a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h)
  return F(min(v)//S,-((-max(v))//S))
 def mul_int(a,n):
  """Exact multiplication by an integer (no fixed-point rescaling)."""
  return F(a.l*n,a.h*n) if n>=0 else F(a.h*n,a.l*n)
 def div(a,d):return F(a.l//d,-((-a.h)//d))
 def divF(a,b):
  if b.l<=0: raise ZeroDivisionError
  num=(a.l*S,a.l*S,a.h*S,a.h*S); den=(b.l,b.h,b.l,b.h)
  lo=min(q//d for q,d in zip(num,den)); hi=max(-((-q)//d) for q,d in zip(num,den))
  return F(lo,hi)
def X(a):return a if isinstance(a,F) else F(a*S)
def qf(a):return F(fl(a.lo),ce(a.hi))

_L2=None
def _ratF(num,den): return F((num*S)//den,-((-(num*S))//den))
def log_integer_fixed(q,T):
 """Outward fixed-point artanh log; no Fraction series or gcd in the loop."""
 global _L2
 if q==1:return F(0)
 e=q.bit_length()-1; two=1<<e
 y=_ratF(q-two,q+two)
 p=y; total=F(0)
 for r in range(T):
  total=total+p.div(2*r+1); p=p*y*y
 # p is y^(2T+1); tail <= 2p/((2T+1)(1-y^2))
 den=F(S)-y*y
 tail=(p*2).div(2*T+1).divF(den)
 ans=total*2 + F(-tail.h,tail.h)
 if e:
  if _L2 is None:
   yy=_ratF(1,3); pp=yy; ss=F(0)
   for r in range(T): ss=ss+pp.div(2*r+1); pp=pp*yy*yy
   dd=F(S)-yy*yy; tt=(pp*2).div(2*T+1).divF(dd)
   _L2=ss*2+F(-tt.h,tt.h)
  ans=ans+_L2*e
 return ans

def weights(K):
 """W_j=(-1)^j A_j/2^K, A_j integer, exact O(K^2) precomputation."""
 A=[0]*K
 for j in range(K):
  A[j]=sum(comb(k,j)<<(K-k-1) for k in range(j,K))
  if j&1:A[j]=-A[j]
 return A,1<<K

def eta_coeffs(K,M,terms=800):
 A,D=weights(K); out=[F(0) for _ in range(M+1)]
 for j in range(K):
  L=log_integer_fixed(j+1,terms); p=F(S)
  for m in range(M+1):
   out[m]=out[m]+p.mul_int(A[j]).div(D*(j+1)*factorial(m))
   p=p*L
 # coefficient of exp(-t log) includes (-1)^m
 for m in range(1,M+1,2):out[m]=F(-out[m].h,-out[m].l)
 return out

def q_coeffs(K=32,M=20,terms=None):
 """Outward coefficients q[0..M] of q(t)=t*zeta(1+t).

 The proved 103_44 Hasse-tail error is added at the normalized coefficient
 level, before any multiplication by a factorial.
 """
 if terms is None: terms=120 if K<=32 else 800
 eta=eta_coeffs(K,M,terms)
 a=log_integer_fixed(2,terms)
 # d_r=(-1)^r a^(r+1)/(r+1)!; solve d*c=eta
 d=[];p=a
 for r in range(M+1):
  d.append(p.div(factorial(r+1)))
  p=p*a; p=F(-p.h,-p.l)
 c=[F(0) for _ in range(M+1)]
 # First solve q_K=eta_K/d exactly at the interval level.  The tail theorem
 # controls q-q_K as a whole; do not alter q_K,0 inside this recurrence.
 for n in range(M+1):
  v=eta[n]
  for r in range(1,n+1):v=v-d[r]*c[n-r]
  c[n]=v.divF(d[0])
 # q(0)=1 exactly.  Replacing only the returned constant coefficient is
 # valid; for n>=1 add the coefficient-tail enclosure around q_K,n.
 c[0]=F(S)
 # (27+9 log(K+1))*2^(n-K)/(K+1) from 103_44.
 LK=log_integer_fixed(K+1,terms).h
 for n in range(1,M+1):
  e=(27*S+9*LK)//(2**(K-n)*(K+1)) + 1
  c[n]=F(c[n].l-e,c[n].h+e)
 return c

def gamma_pilot(K=32,M=20,terms=None):
 c=q_coeffs(K,M,terms)
 out=[]
 for n in range(M):
  g=c[n+1].mul_int(((-1) if n%2 else 1)*factorial(n))
  out.append(g)
 return out

if __name__=='__main__':
 A,D=weights(32);print('weights-denominator-bits',D.bit_length(),'W0',A[0])
