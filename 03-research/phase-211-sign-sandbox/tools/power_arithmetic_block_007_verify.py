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

n=12; u=F(63,2); M=256
l2=logb(F(1,3))
pi=add(scale(16,atanb(F(1,5))),scale(-4,atanb(F(1,239))))
lp=(logb((pi[0]-1)/(pi[0]+1))[0],logb((pi[1]-1)/(pi[1]+1))[1])
gam0=add(point(H(M)-F(1,2*M)+F(1,12*M*M)-F(1,120*M**4)),scale(-8,l2))
gamma=(gam0[0],gam0[1]+F(1,252*M**6))
d=add(add(point(H(15)),scale(-1,gamma)),scale(-1,lp))
sums={}
for p in range(2,13):
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
den=10**12
center=[F(((lo+hi)*den/2).__floor__(),den) for lo,hi in bands]
errors=[max(abs(lo-c),abs(hi-c)) for (lo,hi),c in zip(bands,center)]
rowerror=max(sum(errors[abs(i-j)] for j in range(n)) for i in range(n))
assert rowerror<F(1,10**8)
mat=[[center[abs(i-j)]-(F(1,1250) if i==j else 0) for j in range(n)] for i in range(n)]
for k in range(n):
    pivot=mat[k][k]
    assert pivot>0
    for i in range(k+1,n):
        for j in range(k+1,n):
            mat[i][j]-=mat[i][k]*mat[k][j]/pivot

# Retain cancellations by shifting every Laguerre polynomial by 40.
a=F(11,10); c0=F(40,63)
assert logb(F(1,2))[0]>1
assert logb(F(1,2))[1]<a
tails=[]
for k in range(n):
    shifted=[sum((q[k][ell]*comb(ell,j)*40**(ell-j) for ell in range(j,k+1)),F())
             for j in range(k+1)]
    assert all((-1)**k*z>=0 for z in shifted)
    total=F()
    for j,coef in enumerate(shifted):
        integ=F()
        for r in range(j+2):
            z=63**j*((a*comb(j,r)*(a-c0)**(j-r) if r<=j else 0)
                    +(comb(j,r-1)*(a-c0)**(j-r+1) if r>=1 else 0))
            integ+=z*F(factorial(r),31**(r+1))
        bound=F(1,3**32)*a*(63*a-40)**j+F(1,3**31)*integ
        total+=abs(coef)*bound*(2 if k==0 else 1)
    tails.append(total)
tailrow=max(sum(tails[abs(i-j)] for j in range(n)) for i in range(n))
assert tailrow<F(3,5000)
assert F(1,1250)-F(1,10**8)-F(3,5000)>F(1,10000)
print('PASS: AP+atom2 > .0008 minus 1e-8; prime tail norm < .0006; full Laguerre12 block > 1/10000')
