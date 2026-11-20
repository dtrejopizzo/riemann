"""Exact rational certificate for the signed-gain eight-pole transfer.
No floating point, optimizer, spectral mesh, or numerical special function.
"""
from fractions import Fraction as F
from math import comb,factorial
import power_fixed_grid_003 as C
u=F(63,2);n=8;M=2000;ps={}
for j in range(1,n+1):
 part=sum((C.I(F(1,k**(j+1))) for k in range(16,M+1)),C.I(0))
 tail=C.I(F(1,j*(M+1)**j),F(1,j*M**j))
 ps[j]=(-1)**(j+1)*factorial(j)*(part+tail)
arch=[sum((F(1,k) for k in range(1,16)),F(0))-C.gamma-C.logpi]
for k in range(1,n+1):
 arch.append(sum((ps[j]*F(1,2**(j+1))*(2*u)**j*F(comb(k-1,j-1),factorial(j)) for j in range(1,k+1)),C.I(0)))
r=F(32,31)
polar=[2*u/(u*u-F(1,4))*(-1)**k*(r**k+r**(-k)) for k in range(n+1)]

def ldl_positive(T):
 for k in range(len(T)):
  p=T[k][k];assert p.lo>0,(k,p)
  for i in range(k+1,len(T)):
   for j in range(i,len(T)):T[i][j]=T[j][i]=T[i][j]-T[i][k]*T[j][k]/p
# Base AP8 >7/200.
b=F(7,200)
T=[[arch[abs(i-j)]+polar[abs(i-j)]-(b if i==j else 0) for j in range(n)] for i in range(n)]
ldl_positive(T)
# Arch9 constrained to F(0)=0: Laguerre evaluation signs (-1)^j.
# Basis B_i=e_i-(-1)^i e_8, i=0,...,7, Gram I+aa^t.
gamma=F(1,4)
T=[]
for i in range(n):
 row=[]
 for j in range(n):
  ai=(-1)**i;aj=(-1)**j
  val=arch[abs(i-j)]-aj*arch[8-i]-ai*arch[8-j]+ai*aj*arch[0]
  row.append(val-gamma*((1 if i==j else 0)+ai*aj))
 T.append(row)
ldl_positive(T)
# Polar base bound p=3/2.
AA=F(63,31**2)*sum((F(32,31)**(2*j) for j in range(n)),F(0))
BB=F(63,32**2)*sum((F(31,32)**(2*j) for j in range(n)),F(0))
p=F(3,2);assert 4*AA*BB<p*p
c=F(3,100)
assert gamma>c
assert b-c-p*F(n,4)/(u*u)>F(1,1000)
# Uniform weighted trace: alpha=3/5, sigma=189/10, beta=97/5.
a=F(3,5)
BT=sum((sum((F(comb(j,k)**2)*a**(2*k) for k in range(j+1)),F(0))/(1-a)**(2*j+1) for j in range(n)),F(0))
assert 4*BT<25000**2
assert 25**5<4*19**5 # 2^(-2/5)<19/25.
assert C.log2.hi<F(7,10)
L=F(25000*19,25*2**19)*(F(7,10)+F(14,10*18)+F(2,18**2))
assert L<F(29,1000)
assert c-L>F(1,1000)
print('PASS: AP8 base>7/200; constrained Arch9>1/4; polar bound; signed margin>1/1000; trace prime loss<29/1000.')
print('Global conclusion: W[f]>(1/1000)||f||^2 on all eight-real-pole spaces with poles>=63/2.')
