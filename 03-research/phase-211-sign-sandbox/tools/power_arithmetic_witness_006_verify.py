from fractions import Fraction as F
from math import comb, factorial

v=[2521,-3701,3730,-3278,2158,-793,-793,2158,-3278,3730,-3701,2521]
N=sum(x*x for x in v)
assert N==99993678
u=F(63,2)
def J(r):
    return 2*sum((r**(2*k+1)/F(2*k+1) for k in range(24)),F())
def E(r):
    return 2*r**49/(49*(1-r*r))
def H(n):
    return sum((F(1,k) for k in range(1,n+1)),F())
dlo=H(15)-H(256)+8*J(F(1,3))-J(F(15,29))-E(F(15,29))
dhi=H(15)-H(256)+8*(J(F(1,3))+E(F(1,3)))+F(1,256)-J(F(76,147))
C=[sum(v[i]*v[i+k] for i in range(12-k)) for k in range(12)]
lo,hi=N*dlo,N*dhi
for r in range(1,12):
    coeff=(-1)**(r+1)*u**r*sum(C[k]*comb(k-1,r-1) for k in range(r,12))
    total=sum((F(1,k**(r+1)) for k in range(16,256)),F())
    sl=total+F(1,r*256**r)
    sh=total+F(1,r*255**r)
    lo+=coeff*(sl if coeff>=0 else sh)
    hi+=coeff*(sh if coeff>=0 else sl)
A=sum((F(v[j]*(-32)**j,31**(j+1)) for j in range(12)),F())
B=sum((F(v[j]*(-31)**j,32**(j+1)) for j in range(12)),F())
polar=126*A*B
assert -F(2,125)*N<lo+polar<=hi+polar<-F(1,100)*N
q=[]
for j in range(12):
    q.append(sum((C[k]*((-1)**j*F(comb(k,j),factorial(j))-
        ((-1)**j*F(comb(k-1,j),factorial(j)) if k>0 and j<=k-1 else 0))
        for k in range(j,12)),F()))
expected=[F(99993678),F(49185301),F(13821792),-F(7615697,2),F(59520419,12),
          -F(128178871,60),F(39362105,72),-F(4637517,56),F(7669309,1008),
          -F(3136561,7560),F(133613,10800),-F(6355441,39916800)]
assert q==expected
shift=[sum((q[k]*comb(k,j)*40**(k-j) for k in range(j,12)),F()) for j in range(12)]
assert all(x<0 for x in shift)
Q42=sum((q[k]*42**k for k in range(12)),F())
assert -F(4,3)*F(1,2**32)*Q42/N>F(1,25)
assert F(1,25)-F(2,125)>F(1,50)
assert J(F(1,2))>1
assert J(F(1,2))+E(F(1,2))<F(11,10)
tail=F()
for k,coeff in enumerate(q):
    r=k+1
    bound=F(1,3**32)*F(11,10)**r+F(1,3**31)*sum((
        F(comb(r,j)*factorial(j),31**(j+1))*F(11,10)**(r-j)
        for j in range(r+1)),F())
    tail+=2*abs(coeff)*63**k*bound/N
assert tail<F(1,500)
assert -F(1,100)+F(1,500)==-F(1,125)
print('PASS: AP negative; n=2 alone repairs; deleting only n=2 makes the full form negative')
