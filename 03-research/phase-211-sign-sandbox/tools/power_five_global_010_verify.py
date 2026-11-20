from fractions import Fraction as F
from math import comb

def H(n): return sum((F(1,k) for k in range(1,n+1)),F())
def J(r): return 2*sum((r**(2*k+1)/F(2*k+1) for k in range(24)),F())
def E(r): return 2*r**49/(49*(1-r*r))
u=F(63,2)
dlo=H(15)-H(256)+8*J(F(1,3))-J(F(15,29))-E(F(15,29))
dhi=H(15)-H(256)+8*(J(F(1,3))+E(F(1,3)))+F(1,256)-J(F(76,147))
intervals=[(dlo,dhi)]
for k in range(1,5):
    lo=hi=F()
    for r in range(1,k+1):
        total=sum((F(1,j**(r+1)) for j in range(16,256)),F())
        sl=total+F(1,r*256**r)
        sh=total+F(1,r*255**r)
        coeff=F((-1)**(r+1)*comb(k-1,r-1),2)*u**r
        lo+=coeff*(sl if coeff>=0 else sh)
        hi+=coeff*(sh if coeff>=0 else sl)
    intervals.append((lo,hi))
center=[F(1596,1000),F(1016,1000),-F(16,1000),F(349,1000),-F(154,10000)]
errors=[max(abs(lo-c),abs(hi-c)) for (lo,hi),c in zip(intervals,center)]
assert max(sum(errors[abs(i-j)] for j in range(5)) for i in range(5))<F(1,200)
A=[F((-32)**j,31**(j+1)) for j in range(5)]
B=[F((-31)**j,32**(j+1)) for j in range(5)]
matrix=[[center[abs(i-j)]+63*(A[i]*B[j]+B[i]*A[j])-(F(39,200) if i==j else 0)
         for j in range(5)] for i in range(5)]
for k in range(5):
    pivot=matrix[k][k]
    assert pivot>0
    for i in range(k+1,5):
        for j in range(k+1,5):
            matrix[i][j]-=matrix[i][k]*matrix[k][j]/pivot
assert F(39,200)-F(1,200)==F(19,100)
AA=63*sum(x*x for x in A)
BB=63*sum(x*x for x in B)
assert 4*AA*BB<1

# The audited scalar negative-region bound from FOUR_GLOBAL009.
def ell(x):
    return -F(11,2)+sum((x/(F(k,1)+F(1,4))/(4*(F(k,1)+F(1,4))**2+x)
                         for k in range(16)),F())
for x,lower in [(4,-F(4,3)),(16,-F(3,5)),(32,-F(1,4)),(64,F(2,25)),(81,F(1,10))]:
    assert ell(F(x))>lower
assert max(F(112,5),F(344,15),F(112,5),F(112,5),F(81,50))<23
c=F(1,50)
K=((1+81/u**2)**5-1)/81
assert F(19,100)-c-23*K-F(5,4)/u**2>F(3,100)
B5=F(49**5-1,16)
assert B5==3*sum(F(49)**j for j in range(5))
assert 4*B5<8404**2
loss=F(8404,2**20)*F(21,19)
assert loss<F(1,100)
assert c-loss>F(1,100)
print('PASS: confluence-five AP>.19, global transport AP>.02, full W>.01 for all five real poles>=31.5')
