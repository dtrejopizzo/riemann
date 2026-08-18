#!/usr/bin/env python3
"""Fixed-point outward propagation of the 217 strong margin (pilot n<=20)."""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import runpy

P = 70; S = 10**P
root = Path(__file__).resolve().parent
em = runpy.run_path(str(root / "stieltjes_em_interval_pilot.py"))
old = em["ns"]

def fl(q): return q.numerator*S // q.denominator
def ce(q): return -((-q.numerator*S)//q.denominator)
class F:
 def __init__(self,l,h=None): self.l=int(l); self.h=int(l if h is None else h)
 def __add__(a,b): b=x(b); return F(a.l+b.l,a.h+b.h)
 def __sub__(a,b): b=x(b); return F(a.l-b.h,a.h-b.l)
 def __neg__(a): return F(-a.h,-a.l)
 def __mul__(a,b):
  b=x(b); v=(a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h)
  return F(min(v)//S, -((-max(v))//S))
 def divint(a,d):
  if d<0: return (-a).divint(-d)
  return F(a.l//d, -((-a.h)//d))
def x(a): return a if isinstance(a,F) else F(a*S)
def qfix(a): return F(fl(a.lo),ce(a.hi))
def powf(a,n):
 r=F(S)
 while n:
  if n&1:r=r*a
  a=a*a;n//=2
 return r

def run(top=20):
 # exact source intervals, quantized outward once
 g=[qfix(v) for v in old["gamma"]]
 ctx=em["EMContext"](max_j=top)
 for j in range(8,top+1): g.append(qfix(em["gamma_interval"](j,ctx=ctx)))
 z={k:qfix(v) for k,v in old["zeta"].items()}
 for k in range(9,top+1): z[k]=qfix(em["zeta_interval"](k))
 log4=qfix(old["log4pi"])
 def prime(n):
  q=[F(0) for _ in range(n+1)];q[0]=F(S)
  for j in range(n): q[j+1]=(g[j]*(-1 if j%2 else 1)).divint(factorial(j))
  u=q[:];u[0]=u[0]-F(S); p=[F(0) for _ in range(n+1)];pw=[F(S)]+[F(0)]*n
  for m in range(1,n+1):
   nw=[F(0)]*(n+1)
   for i in range(n+1):
    for j in range(n+1-i): nw[i+j]=nw[i+j]+pw[i]*u[j]
   pw=nw; c=1 if m%2 else -1
   for k in range(n+1):p[k]=p[k]+pw[k].divint(m)*c
  return sum((p[k]*(n*comb(n-1,k-1)) for k in range(1,n+1)),F(0))
 def arch(n):
  a=F(S)-(g[0]+log4).divint(2)*n
  for k in range(2,n+1):a=a+(z[k]*((-1 if k%2 else 1)*comb(n,k)*(2**k-1))).divint(2**k)
  return a
 out=[]
 for n in range(9,top+1):
  A=arch(n); M=prime(n)+A.divint(2); out.append((n,M))
 return out
if __name__=='__main__':
 for n,m in run(): print(n, m.l>0, m.l//10**(P-12), m.h//10**(P-12))
