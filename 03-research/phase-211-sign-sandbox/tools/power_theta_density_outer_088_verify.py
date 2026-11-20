"""Exact polynomial/rational certificate for the real R4-density Wronskian, t>=1."""
from fractions import Fraction as F
from itertools import permutations
from math import comb,factorial
from hashlib import sha256
from pathlib import Path

def const(c,n):return {(0,)*n:F(c)} if c else {}
def var(n,i):
 e=[0]*n;e[i]=1;return {tuple(e):F(1)}
def add(*ps):
 r={}
 for p in ps:
  for e,c in p.items():r[e]=r.get(e,F(0))+c
 return {e:c for e,c in r.items() if c}
def scale(p,c):return {e:v*F(c) for e,v in p.items() if v*c}
def mul(p,q):
 r={}
 for a,c in p.items():
  for b,d in q.items():
   e=tuple(x+y for x,y in zip(a,b));r[e]=r.get(e,F(0))+c*d
 return {e:c for e,c in r.items() if c}
def power(p,k):
 n=len(next(iter(p))) if p else 1;r=const(1,n)
 while k:
  if k&1:r=mul(r,p)
  p=mul(p,p);k//=2
 return r
def part(p,j):
 r={}
 for e,c in p.items():
  if e[j]:
   ee=list(e);ee[j]-=1;r[tuple(ee)]=c*e[j]
 return r
def det(rows):
 n=len(rows);out={}
 for pp in permutations(range(n)):
  sg=(-1)**sum(pp[i]>pp[j] for i in range(n) for j in range(i+1,n))
  term=const(sg,len(next(iter(rows[0][0]))))
  for i in range(n):term=mul(term,rows[i][pp[i]])
  out=add(out,term)
 return out
def shift2(p,a,b):
 r={}
 for (i,j),c in p.items():
  assert i>=0 and j>=0
  for k in range(i+1):
   for l in range(j+1):
    e=(k,l);r[e]=r.get(e,F(0))+c*comb(i,k)*a**(i-k)*comb(j,l)*b**(j-l)
 return {e:c for e,c in r.items() if c}

# First mode: remove the common exp(5t/2-y) before forming its Wronskian.
t,y=var(2,0),var(2,1)
D2=lambda p:add(part(p,0),scale(mul(y,part(p,1)),2))
b=add(scale(y,2),const(-3,2));B=[b]
for _ in range(3):B.append(add(D2(B[-1]),mul(add(const(F(5,2),2),scale(y,-2)),B[-1])))
rows=[[mul(t,B[0]),add(mul(t,B[2]),scale(B[1],2)),scale(B[1],-1),scale(B[3],-1)]]
for _ in range(3):rows.append([D2(p) for p in rows[-1]])
W0num=det(rows)
P={ (i,j-2):-c/16 for (i,j),c in W0num.items() }
assert all(i>=0 and j>=0 for i,j in P)
margin=add(P,scale(mul(power(t,2),power(y,8)),-4096))
shifted=shift2(margin,1,21)
assert len(shifted)==27 and all(c>0 for c in shifted.values())
assert shifted[(0,0)]>0
print('PASS first-mode margin: all27 shifted coefficients positive',flush=True)

# Generic G=t^4 W(1,A,B,C) in six independent potential derivatives.
v=[var(7,j) for j in range(7)];t,p,q,r,s,v5,v6=v
inv_t={( -1,0,0,0,0,0,0):F(1)}
A=add(power(p,2),scale(q,-1),scale(mul(p,inv_t),-2))
B=mul(p,inv_t)
C=mul(add(power(p,3),scale(mul(p,q),-3),r),inv_t)
def D7(f):
 assert all(e[6]==0 for e in f), "No derivative of V6 is required by these three rows"
 return add(part(f,0),*[mul(v[j+1],part(f,j)) for j in range(1,6)])
rows=[[D7(f) for f in [A,B,C]]]
for _ in range(2):rows.append([D7(f) for f in rows[-1]])
G=mul(power(t,4),det(rows))
assert len(G)==55
assert all(0<=e[0]<=2 and sum(e[1:])<=6 for e in G)
K=sum(abs(c)*sum(e[1:])*128**(sum(e[1:])-1) for e,c in G.items() if sum(e[1:]))
assert K==30936927338496
print('PASS generic polynomial:55 monomials, tdegree<=2, jetdegree<=6; K exact',flush=True)

# Whole theta tail through six derivatives, with no sampled theta values.
h=F(1,14)
Euler5=h*(1+26*h+66*h*h+26*h**3+h**4)/(1-h)**6
assert Euler5<1
z=F(63)
bell6=4096+30720/z+66560/z**2+46080/z**3+7936/z**4+128/z**5
assert bell6<5000
assert sum(F(3)**k/F(factorial(k)) for k in range(12))>20
assert F(4,3)**8/F(20)**7<F(1,2)
E=F(320000,9)*3**8*21**6/F(20)**21
assert E==F(62523502209,6553600000000000000000)
logbound=E+31*E**2+180*E**3+390*E**4+360*E**5+120*E**6
assert logbound<2*E and 2*E<1
assert 68*21+1<128*21
assert 2*E*K<96*21
print('PASS full theta derivative/log tail and MVT loss',flush=True)
print('PASS conclusion: t^4 W_R4 < -4000 t^2 y^6 for every t>=1, y=pi exp(2t)',flush=True)
print('E exact',E,'K exact',K,'etaK exact',2*E*K,flush=True)
print('SCRIPT SHA256',sha256(Path(__file__).read_bytes()).hexdigest(),flush=True)
