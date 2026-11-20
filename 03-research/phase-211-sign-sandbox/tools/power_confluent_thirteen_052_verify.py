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

n=13; u=F(63,2); M=256
l2=logb(F(1,3))
pi=add(scale(16,atanb(F(1,5))),scale(-4,atanb(F(1,239))))
lp=(logb((pi[0]-1)/(pi[0]+1))[0],logb((pi[1]-1)/(pi[1]+1))[1])
gam0=add(point(H(M)-F(1,2*M)+F(1,12*M*M)-F(1,120*M**4)),scale(-8,l2))
gamma=(gam0[0],gam0[1]+F(1,252*M**6))
d=add(add(point(H(15)),scale(-1,gamma)),scale(-1,lp))
sums={}
for p in range(2,14):
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

# Keep the actual components for the Schur minimizing direction.
E2bands=bands[:]
P2=[]; AP=[]; P3=[]; E23=[]
l3=logb(F(1,2))
for k in range(n):
    polys=[]
    for logn in [l2,l3]:
        poly=point(0)
        for ell,coef in enumerate(q[k]):
            poly=add(poly,scale(coef*63**ell,(logn[0]**ell,logn[1]**ell)))
        polys.append(poly)
    p2=scale(-F(2 if k==0 else 1,2**32),mul(l2,polys[0]))
    p3=scale(-F(2 if k==0 else 1,3**32),mul(l3,polys[1]))
    P2.append(p2); P3.append(p3)
    AP.append(add(E2bands[k],scale(-1,p2)))
    E23.append(add(E2bands[k],p3))

def centered(bb):
    den=10**15
    ctr=[F(((lo+hi)*den/2).__floor__(),den) for lo,hi in bb]
    err=[max(abs(lo-c),abs(hi-c)) for (lo,hi),c in zip(bb,ctr)]
    assert max(sum(err[abs(i-j)] for j in range(n)) for i in range(n))<F(1,10**10)
    return [[ctr[abs(i-j)] for j in range(n)] for i in range(n)]
T2=centered(E2bands); T23=centered(E23)
epsilon=F(1,10**10)

def ldl(A, rhs=None):
    size=len(A); A=[row[:] for row in A]
    LL=[[F(i==j) for j in range(size)] for i in range(size)]
    dd=[]
    for k in range(size):
        pivot=A[k][k]
        assert pivot>0,('pivot',k)
        dd.append(pivot)
        for i in range(k+1,size): LL[i][k]=A[i][k]/pivot
        for i in range(k+1,size):
            for j in range(k+1,size): A[i][j]-=LL[i][k]*LL[j][k]*pivot
    if rhs is None:return
    yy=[]
    for i in range(size):yy.append(rhs[i]-sum((LL[i][k]*yy[k] for k in range(i)),F()))
    xx=[F()]*size
    for i in range(size-1,-1,-1):xx[i]=yy[i]/dd[i]-sum((LL[k][i]*xx[k] for k in range(i+1,size)),F())
    return xx

def shifted(T,c):return [[T[i][j]-(c if i==j else 0) for j in range(n)] for i in range(n)]
ldl(shifted(T2,F(3,10000)+epsilon))
ldl(shifted(T23,F(7,25000)+epsilon))

# Complement h=ell (norm squared13), C spans ell.perp exactly.
h=[F((-1)**i) for i in range(n)]
C=[[F((1 if a==i else 0)-((-1)**i if a==12 else 0)) for i in range(12)] for a in range(n)]
def schur(T,offset=F()):
    M=shifted(T,offset)
    A=[[sum((C[a][i]*M[a][b]*C[b][j] for a in range(n) for b in range(n)),F()) for j in range(12)] for i in range(12)]
    g=[sum((C[a][i]*M[a][b]*h[b] for a in range(n) for b in range(n)),F()) for i in range(12)]
    diagonal=sum((h[a]*M[a][b]*h[b] for a in range(n) for b in range(n)),F())
    sol=ldl(A,g)
    correction=sum((g[i]*sol[i] for i in range(12)),F())
    x=[h[a]-sum((C[a][i]*sol[i] for i in range(12)),F()) for a in range(n)]
    return (diagonal-correction)/13,diagonal/13,correction/13,x
s2,d2,c2,x=schur(T2)
s23,d23,c23,_=schur(T23)
assert F(4054,10**7)<schur(T2,epsilon)[0]
assert schur(T2,-epsilon)[0]<F(4055,10**7)
assert F(3834,10**7)<schur(T23,epsilon)[0]
assert schur(T23,-epsilon)[0]<F(3836,10**7)
assert F(12337,10**5)<d2<F(12338,10**5)
assert F(12296,10**5)<c2<F(12298,10**5)

def quadratic(bb,x):
    result=point(0)
    for i in range(n):
        for j in range(n):result=add(result,scale(x[i]*x[j]/13,bb[abs(i-j)]))
    return result
ap=quadratic(AP,x);p2=quadratic(P2,x);p3=quadratic(P3,x)
assert F(1839,10**5)<ap[0]<ap[1]<F(1841,10**5)
assert -F(1800,10**5)<p2[0]<p2[1]<-F(1798,10**5)
assert p3[1]<0

# Complete tail n>=4: shifted Laguerre coefficients retain cancellation.
a=F(7,5);c0=F(40,63);tails=[]
assert 2*l2[0]>F(4,3)
assert 2*l2[1]<F(7,5)
assert 1/F(4,3)+63*12/(63*F(4,3)-40)<32
for k in range(n):
    shiftedq=[sum((q[k][ell]*comb(ell,j)*40**(ell-j) for ell in range(j,k+1)),F()) for j in range(k+1)]
    assert all((-1)**k*z>=0 for z in shiftedq)
    total=F()
    for j,coef in enumerate(shiftedq):
        integ=F()
        for r in range(j+2):
            z=63**j*((a*comb(j,r)*(a-c0)**(j-r) if r<=j else 0)+(comb(j,r-1)*(a-c0)**(j-r+1) if r>=1 else 0))
            integ+=z*F(factorial(r),31**(r+1))
        bound=F(1,4**32)*a*(63*a-40)**j+F(1,4**31)*integ
        total+=abs(coef)*bound*(2 if k==0 else 1)
    tails.append(total)
tailrow=max(sum(tails[abs(i-j)] for j in range(n)) for i in range(n))
assert tailrow<F(1,100000)
assert F(7,25000)-F(1,100000)>F(1,4000)
# Monotonicity of the Schur minimum under an operator bound controls its full-W value.
assert schur(T23,epsilon+F(1,100000))[0]>F(3,10000)
assert schur(T23,-epsilon-F(1,100000))[0]<F(1,2000)
print('PASS: E2_V13 >.0003 norm squared; E23_V13 >.00028 norm squared')
print('PASS: all remaining contacts n>=4 norm <.00001; W_V13 >norm squared/4000')
print('PASS: E2 Schur pivot in(.0004054,.0004055); E23 pivot in(.0003834,.0003836)')
print('PASS: real Schur direction AP positive(.01839,.01841), contact2 adverse(-.018,-.01798), contact3 adverse')
print('PASS: full-W Schur pivot in(.0003,.0005); no claim on arbitrary thirteen poles')
