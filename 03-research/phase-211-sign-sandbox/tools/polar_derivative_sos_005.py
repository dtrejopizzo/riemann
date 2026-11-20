"""Exact rational verifier of one explicit four-variable quartic SOS.
No numerical optimizer, floating point, or numerical special function is used.
"""
from fractions import Fraction as F
from math import comb, factorial
import power_fixed_grid_003 as C
u=F(63,2)
# psi^(j)(16), 1<=j<=4, bounded by integral tails.
ps={}
M=2000
for j in range(1,5):
 p=j+1
 part=sum((C.I(F(1,k**p)) for k in range(16,M+1)),C.I(0))
 tail=C.I(F(1,j*(M+1)**j),F(1,j*M**j))
 ps[j]=(-1)**(j+1)*factorial(j)*(part+tail)
r=F(32,31)
mk=[]
for k in range(1,5):
 arch=sum((ps[j]*F(1,2**(j+1))*(2*u)**j*F(comb(k-1,j-1),factorial(j)) for j in range(1,k+1)),C.I(0))
 pol=2*u/(u*u-F(1,4))*(-1)**k*(r**k+r**(-k))
 mk.append(arch+pol)
a=[F(q,10000) for q in (8887,1116,2213,1126)]
for k in range(4):
 assert a[k]-F(1,10000)<mk[k].lo<=mk[k].hi<a[k]+F(1,10000)
# Quadratic monomials x0²,x0x1,x0x2,x0x3,x1²,x1x2,x1x3,x2²,x2x3,x3².
Z=[]
for i in range(4):
 for j in range(i,4):
  e=[0]*4;e[i]+=1;e[j]+=1;Z.append(tuple(e))
Qraw=[
[8087,558,5550,1121,-5250,-358,-1663,1687,558,937],
[558,8900,-200,5000,558,-4324,1005,-1358,-2787,558],
[5550,-200,12800,0,-7900,800,-7200,5550,1005,-1663],
[1121,5000,0,14300,-1000,-10000,0,-1000,5000,1121],
[-5250,558,-7900,-1000,8087,558,5550,-5450,-1358,1687],
[-358,-4324,800,-10000,558,9300,800,558,-4324,-358],
[-1663,1005,-7200,0,5550,800,12800,-7900,-200,5550],
[1687,-1358,5550,-1000,-5450,558,-7900,8087,558,-5250],
[558,-2787,1005,5000,-1358,-4324,-200,558,8900,558],
[937,558,-1663,1121,1687,-358,5550,-5250,558,8087]]
Q=[[F(t,10000) for t in row] for row in Qraw]
def add(p,q):
 o=p.copy()
 for k,v in q.items():o[k]=o.get(k,F(0))+v
 return {k:v for k,v in o.items() if v}
def scale(p,s):return {k:v*s for k,v in p.items() if v*s}
def mul(p,q):
 o={}
 for k,v in p.items():
  for t,w in q.items():
   e=tuple(a+b for a,b in zip(k,t));o[e]=o.get(e,F(0))+v*w
 return {k:v for k,v in o.items() if v}
N={tuple(2 if j==i else 0 for j in range(4)):F(1) for i in range(4)}
cs=[]
for k in range(1,4):
 p={}
 for j in range(4-k):
  e=[0]*4;e[j]+=1;e[j+k]+=1;p[tuple(e)]=F(1)
 cs.append(p)
c1,c2,c3=cs
D=scale(mul(N,N),a[0]-F(2,25))
for coeff,p in [(a[1],c1),(a[0]+a[2],c2),(a[1]+a[3],c3)]:D=add(D,scale(mul(p,N),coeff))
inside=add(add(scale(c1,a[0]),scale(c2,a[1])),scale(c3,a[2]))
D=add(D,scale(mul(c1,inside),-2))
gram={}
for i in range(10):
 for j in range(10):
  e=tuple(t+w for t,w in zip(Z[i],Z[j]));gram[e]=gram.get(e,F(0))+Q[i][j]
gram={k:v for k,v in gram.items() if v}
assert D==gram
# LDL exact: all ten pivots even exceed 1/5.
T=[row[:] for row in Q]
for k in range(10):
 pivot=T[k][k];assert pivot>F(1,5)
 for i in range(k+1,10):
  for j in range(i,10):T[i][j]=T[j][i]=T[i][j]-T[i][k]*T[j][k]/pivot
assert F(2,25)-F(12,10000)>F(3,40)
print('PASS: four coefficient intervals, exact Gram identity, ten LDL pivots >1/5.')
print('Conclusion: u * normalized archimedean-plus-polar derivative > 3/40 for every nonzero numerator.')
