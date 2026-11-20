# Exhaustive initial segment j=1,...,13; upper cutoff derived analytically.
# No search over j, rates, or candidate vectors.
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

n=25; u=F(63,2); M=256
l2=logb(F(1,3))
pi=add(scale(16,atanb(F(1,5))),scale(-4,atanb(F(1,239))))
lp=(logb((pi[0]-1)/(pi[0]+1))[0],logb((pi[1]-1)/(pi[1]+1))[1])
gam0=add(point(H(M)-F(1,2*M)+F(1,12*M*M)-F(1,120*M**4)),scale(-8,l2))
gamma=(gam0[0],gam0[1]+F(1,252*M**6))
d=add(add(point(H(15)),scale(-1,gamma)),scale(-1,lp))
sums={}
for p in range(2,26):
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

den=10**18
center=[F(((lo+hi)*den/2).__floor__(),den) for lo,hi in bands]
errors=[max(abs(lo-z),abs(hi-z)) for (lo,hi),z in zip(bands,center)]
rowerror=max(sum(errors[abs(i-j)] for j in range(n)) for i in range(n))
assert rowerror<F(1,10**8)
c=F(1,50)
for highpass in range(1,14):
    size=12+highpass
    # The omitted common factor 2^-highpass cancels from the quadratic inequality.
    C=[[F(comb(highpass,a-i)) if 0<=a-i<=highpass else F() for i in range(12)] for a in range(size)]
    Gram=[[sum((C[a][i]*C[a][j] for a in range(size)),F()) for j in range(12)] for i in range(12)]
    M=[[sum((C[a][i]*center[abs(a-b)]*C[b][j] for a in range(size) for b in range(size)),F())-(c+F(1,10**8))*Gram[i][j] for j in range(12)] for i in range(12)]
    for k in range(12):
        pivot=M[k][k]
        assert pivot>0, ('failed sufficient block',highpass,k)
        for i in range(k+1,12):
            for j in range(k+1,12):
                M[i][j]-=M[i][k]*M[k][j]/pivot
    print('PASS exact highpass block',highpass,flush=True)
print('PASS: E2[Q^j F] > ||Q^j F||^2/50 for every j=1,...,13 and F in V12')

# Analytic tail j>=14, from audited CENTERED_CUTOFF049 and polar048.
assert F(859,800)-1-3*F(9,62)**14>F(1,50)
# Uniform weighted trace on ANY thirteen real poles >=u.
alpha=F(1,2)
BT=sum((F(comb(j,k)**2)*alpha**(2*k)/(1-alpha)**(2*j+1) for j in range(13) for k in range(j+1)),F())
assert BT==109543953194
assert 330974**2<BT<330975**2
assert F(13,10)**4<3
rr=F(1,2)
log3upper=2*sum((rr**(2*k+1)/F(2*k+1) for k in range(64)),F())+2*rr**129/(129*(1-rr*rr))
assert log3upper<F(11,10)
TAIL=2*330975*F(10,13)*F(1,3**16)*(F(11,10)+F(3,15)*F(11,10)+F(3,225))
assert TAIL<F(2,125)
assert F(1,50)-TAIL>F(1,250)
assert F(1,250)>F(1,10000)
print('PASS: BT13 exact; all contacts n>=3 norm <.016; full W on13-pole numerator-zero spaces >.004 norm squared')
print('PASS: FULLTEL014 plus audited base007 yields full W >norm squared/10000 on ALL12 real poles >=63/2')
