from fractions import Fraction as F
from math import comb, factorial

def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def mul(a,b):
    z=[x*y for x in a for y in b]
    return min(z),max(z)
def point(x): return (F(x),F(x))
def logb(r,N=64):
    a=2*sum((r**(2*k+1)/F(2*k+1) for k in range(N)),F())
    return a,a+2*r**(2*N+1)/(F(2*N+1)*(1-r*r))
def atanb(x,N=30):
    a=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(N)),F())
    b=a+(-1)**N*x**(2*N+1)/F(2*N+1)
    return min(a,b),max(a,b)
def H(n): return sum((F(1,k) for k in range(1,n+1)),F())

n=14; u=F(63,2); M=256
l2=logb(F(1,3))
pi=add(scale(16,atanb(F(1,5))),scale(-4,atanb(F(1,239))))
lp=(logb((pi[0]-1)/(pi[0]+1))[0],logb((pi[1]-1)/(pi[1]+1))[1])
gam0=add(point(H(M)-F(1,2*M)+F(1,12*M*M)-F(1,120*M**4)),scale(-8,l2))
gamma=(gam0[0],gam0[1]+F(1,252*M**6))
d=add(add(point(H(15)),scale(-1,gamma)),scale(-1,lp))
sums={}
for p in range(2,15):
    s=sum((F(1,k**p) for k in range(16,M)),F())
    upper=s+F(1,(p-1)*M**(p-1))+F(1,2*M**p)+F(p,12*M**(p+1))
    lower=upper-F(p*(p+1)*(p+2),720*M**(p+3))
    sums[p]=(lower,upper)
bands=[d]
for k in range(1,n):
    b=point(0)
    for r in range(1,k+1):
        b=add(b,scale(F((-1)**(r+1)*comb(k-1,r-1),2)*u**r,sums[r+1]))
    bands.append(b)
q=[]
for k in range(n):
    q.append([(-1)**j*F(comb(k,j)-(comb(k-1,j) if k and j<k else 0),factorial(j))
              for j in range(k+1)])
for k in range(n):
    polar=F(63,992)*(-1)**k*(F(32,31)**k+F(31,32)**k)
    bands[k]=add(bands[k],point(polar))
    poly=point(0)
    for j,c in enumerate(q[k]):
        poly=add(poly,scale(c*63**j,(l2[0]**j,l2[1]**j)))
    atom=scale(-F(2 if k==0 else 1,2**32),mul(l2,poly))
    bands[k]=add(bands[k],atom)

den=10**15
center=[F(((lo+hi)*den/2).__floor__(),den) for lo,hi in bands]
errors=[max(abs(lo-z),abs(hi-z)) for (lo,hi),z in zip(bands,center)]
assert max(sum(errors[abs(i-j)] for j in range(n)) for i in range(n))<F(1,10**10)
C=[[F(a==i or a==i+1) for i in range(13)] for a in range(14)]
T=[[center[abs(i-j)]-(F(1,125)+F(1,10**10) if i==j else 0) for j in range(14)] for i in range(14)]
M=[[sum((C[a][i]*T[a][b]*C[b][j] for a in range(14) for b in range(14)),F()) for j in range(13)] for i in range(13)]
for k in range(13):
    pivot=M[k][k]
    assert pivot>0
    for i in range(k+1,13):
        for j in range(k+1,13): M[i][j]-=M[i][k]*M[k][j]/pivot
alpha=F(1,2)
BT=sum((F(comb(j,k)**2)*alpha**(2*k)/(1-alpha)**(2*j+1) for j in range(14) for k in range(j+1)),F())
assert BT==947334302964
assert 973311**2<BT<973312**2
TAIL3=2*973312*F(10,13)*F(1,3**16)*(F(11,10)+3*F(11,10)/15+F(3,225))
assert TAIL3>F(1,125)
# Even the single n=3 term of this Cauchy majorant is already too large;
# retaining exact Lambda on n>=4 cannot fix that particular estimate.
first3lower=2*973311*F(3,4)*F(16,15)*F(1,3**16)
assert first3lower>F(1,125)
TAIL4=2*973312*F(5,7)*F(1,4**16)*(F(7,5)+4*F(7,5)/15+F(4,225))
assert TAIL4<F(1,1000)
print('PASS: E2[Q V13] >norm squared/125; BT14 exact',BT)
print('PASS: tail>=3 Cauchy majorant',float(TAIL3),'singlecontact3 majorant lower',float(first3lower))
print('PASS: tail>=4 Cauchy majorant',float(TAIL4),'<.001')
