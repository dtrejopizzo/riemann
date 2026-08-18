#!/usr/bin/env python3
"""Directed primitive V200-complement gap at T=log(6)/2."""
import math
from flint import arb,ctx
ctx.dps=1100;N=200;T=arb(6).log()/2;k=T/2

def endpoint_derivative(n,r):
 return math.factorial(n+r)//(2**r*math.factorial(r)*math.factorial(n-r))
def g_bound(n):
 df=arb(1)
 for j in range(n+1):df*=2*j+1
 ib=k**n/df*(k*k/(2*(2*n+3))).exp()
 return (2*T*(2*n+1)).sqrt()*ib
gb=[g_bound(n) for n in range(N)];D=[]
for r in range(N):
 total=arb(0)
 for n in range(r,N):
  total+=gb[n]*(arb(2*n+1)/(2*T)).sqrt()*T**(-r)*endpoint_derivative(n,r)
 D.append(total)
L=2*T;c=2+2*T-arb(2).log()/2;logL=L.log()
h1=(L*(c*c-c*(logL-1)+(logL*logL-2*logL+2)/4)).sqrt()
boundary=2*D[0]*h1;interior=arb(0);root=(2*T).sqrt();quarter=arb(1)/4
for r in range(1,N):
 H0=arb(r+1).zeta(quarter)/arb(2)**(r+1)
 boundary+=2*root*D[r]*H0
 if r>=2 and r%2==0:interior+=2*root*D[r]*H0
gamma_bound=boundary+interior
m0=arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
weights=sum((arb(lam).log()/arb(nn).sqrt() for nn,lam in ((2,2),(3,3),(4,2),(5,5))),arb(0))
unorm=(2*T.sinh()).sqrt();base=gamma_bound+(m0+2*weights)*unorm
gN=g_bound(N);ratio=k/(2*N+3)*(arb(2*N+3)/(2*N+1)).sqrt();tail=gN*gN/(1-ratio*ratio)
gq=2*tail;lowgram=2*(T.sinh()-T)-gq
C=arb(2).sqrt()*base/lowgram.sqrt();eta=(gq/lowgram).sqrt()

# Uniform band-concentration estimate, worst at the right endpoint T6.
Rband=arb(150);cc=T*Rband
b=arb.pi().sqrt()*cc**N/(arb(2)**(N+1)*arb.gamma(arb(N)+arb('1.5')))
term=(2*N+1)*b*b;rr=cc*cc/(arb(2*N+1)*arb(2*N+3))
trace=2*cc/arb.pi()*term/(1-rr)
qgap=arb('.22')-(arb('.22')+arb('8.315'))*trace
gap=(qgap-2*C*eta-arb('8.315')*eta*eta)/(1+eta*eta)
print('T6 V200 concentration trace upper =',trace)
print('T6 Tate graph eta upper =',eta)
print('T6 primitive complement gap lower =',gap)
assert trace<arb('3e-17') and eta<arb('1e-500') and gap>arb('.219')
print('D185 T6 COMPLETE PRIMITIVE COMPLEMENT: PASS')
