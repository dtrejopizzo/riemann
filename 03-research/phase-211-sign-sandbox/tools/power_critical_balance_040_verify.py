"""Uniform Laurent/curvature constants; no evaluated W or N campaign."""
from fractions import Fraction as F
from math import factorial
import power_fixed_grid_003 as C
u=F(63,2);a=F(992)
assert 1-F(17,64)>0
assert 2+F(17,8)**2/(1-F(17,64))<9
assert F(2,16**2)<F(1,8**2)
assert 18*16==288 and 18*500000==9000000
assert 92+100+46000+62500<110000
assert C.gamma.lo>F(57,100) and C.gamma.hi<F(3,5)
assert 2/(u*u-1)<F(1,400)
assert F(200,3)>50
assert 1/(u*u)<F(1,900)<F(4,7)
assert 4*a+2==3970
N0=2**80;rootN=2**40
scaled_error=F(288,N0**5)+F(9000000,rootN)+F(110000*factorial(6)*10**36,2**200)
assert scaled_error<F(1,10000)
coef=-1+1/(u*u)+F(2,N0)+F(3,5)*(1+F(3970,N0))+F(6,5*N0**2)
assert coef<-F(39,100)
assert F(1,N0)-F(39,100)*50+F(1,10000)<-1
assert F(7,100)*50-F(1,N0**3)-F(1,10000)>1
print('PASS: Laurent cubic remainder and uniform actual-gamma derivative constants.')
print('PASS: full h/H < -1/N and full K/G > 1/N at delta=N^-2, ALL N>=2^80; no W sign claim.')

# Uniform delta interval [2000/N,1000/sqrt(N)]: no parameter scan.
assert F(1000,rootN)<F(1,1000)
assert F(288*10**6,N0)<F(1,1000)
assert F(9000000,rootN)<F(1,10000)
assert F(55*factorial(6)*10**36,2**280)<F(1,10000)
assert F(998,1000)*2000-u*u-F(1,5000)>0
assert F(2000*1986,1)/(992*(u*u-1))<5
print('PASS: full h and K positive for ALL log(x)>=(N-1)/992+5, N>=2^80, using theorem039.')
