from fractions import Fraction as F

def J(r):
    return 2*sum((r**(2*k+1)/F(2*k+1) for k in range(24)),F())
def E(r):
    return 2*r**49/(49*(1-r*r))
def H(n):
    return sum((F(1,k) for k in range(1,n+1)),F())

u=F(63,2)
dlo=H(15)-H(256)+8*J(F(1,3))-J(F(15,29))-E(F(15,29))
dhi=H(15)-H(256)+8*(J(F(1,3))+E(F(1,3)))+F(1,256)-J(F(76,147))
tails={}
for p in (2,3,4):
    total=sum((F(1,k**p) for k in range(16,256)),F())
    tails[p]=(total+F(1,(p-1)*256**(p-1)),total+F(1,(p-1)*255**(p-1)))
s2,s3,s4=[tails[p] for p in (2,3,4)]
blo,bhi=u*s2[0]/2,u*s2[1]/2
clo,chi=blo-u*u*s3[1]/2,bhi-u*u*s3[0]/2
elo,ehi=blo-u*u*s3[1]+u**3*s4[0]/2,bhi-u*u*s3[0]+u**3*s4[1]/2
intervals=[(dlo,dhi),(blo,bhi),(clo,chi),(elo,ehi)]
r=[F(1596,1000),F(1016,1000),-F(16,1000),F(349,1000)]
errors=[max(abs(lo-q),abs(hi-q)) for (lo,hi),q in zip(intervals,r)]
assert max(sum(errors[abs(i-j)] for j in range(4)) for i in range(4))<F(1,200)
A=[F((-32)**j,31**(j+1)) for j in range(4)]
B=[F((-31)**j,32**(j+1)) for j in range(4)]
M=[[r[abs(i-j)]+63*(A[i]*B[j]+B[i]*A[j])-(F(1,4) if i==j else 0)
    for j in range(4)] for i in range(4)]
a,b,c,e=[M[0][j] for j in range(4)]
for x,y,z in ((a+e,b+c,a+b),(a-e,b-c,a-b)):
    assert x>0 and x*z-y*y>0
for k in range(4):
    pivot=M[k][k]
    assert pivot>0
    for i in range(k+1,4):
        for j in range(k+1,4):
            M[i][j]-=M[i][k]*M[k][j]/pivot
assert dhi-F(3,2)*blo+chi-elo/2<-F(1,10)
assert 4*32552<362**2
assert F(362,28672)<F(13,1000)
assert F(49,200)-F(13,1000)>F(1,5)
print('PASS: rational confluence-four certificate, prime bound, and ARCH countervector')
