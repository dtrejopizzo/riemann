import sys
from math import gcd
limit=int(sys.argv[1])
m=2*limit
spf=list(range(m+1))
for p in range(2,int(m**.5)+1):
    if spf[p]==p:
        for j in range(p*p,m+1,p):
            if spf[j]==j: spf[j]=p
mu=[1]*(m+1)
for j in range(2,m+1):
    k=j//spf[j]
    mu[j]= -mu[k] if k%spf[j] else 0
def allowed(k):
    return mu[k] if gcd(k,6)==1 else 0
partial=[0]*(m+1)
def update(k,sign):
    v=sign*allowed(k)
    if not v: return 0
    ds=[1]
    while k>1:
        p=spf[k]
        ds += [p*d for d in ds]
        k//=p
    delta=0
    for d in ds:
        delta+=mu[d]*(2*v*partial[d]+1)
        partial[d]+=v
    return delta
c=0
a=0
first={}
hi=(0,1)
lo=(0,1)
for n in range(1,limit+1):
    if n>1:
        c+=update(n,-1)
        c+=update(2*n-1,1)
    c+=update(2*n,1)
    a+=c
    if n<=85:
        direct=sum(allowed(k)*allowed(l) for k in range(n+1,2*n+1) for l in range(n+1,2*n+1) if gcd(k,l)==1)
        assert direct==c
    for flag in ('c+' if c>0 else 'c-' if c<0 else '', 'a+' if a>0 else 'a-' if a<0 else ''):
        if flag and flag not in first:first[flag]=(n,c,a)
    if a*hi[1]**2>hi[0]*n*n:hi=a,n
    if a*lo[1]**2<lo[0]*n*n:lo=a,n
    if n in (100,1000,10000,100000,limit):print(n,c,a)
print(first,hi,lo)
