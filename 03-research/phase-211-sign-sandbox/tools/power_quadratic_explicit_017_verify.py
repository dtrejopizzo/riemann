"""Elementary rational constants for the analytic eta=15 quadratic-cone proof."""
from fractions import Fraction as F
from math import factorial
u=F(63,2);eta=F(15);C=10000
a=4*eta**2/u**2
assert a==F(400,441)
assert a*F(101,100)/(2*(1-a))==F(202,41)<5
assert a*F(101,100)/2==F(202,441)<F(1,2)
assert F(5120,C)==F(64,125)
assert 1/(1-F(64,125))==F(125,61)
assert F(1,16)/(1-F(1,C))==F(625,9999)
A=u**2/(u**2-eta**2);r=2*eta**2/(u**2-eta**2)
assert A==F(441,341)<2
assert r==F(200,341)<F(3,5)
assert 2*eta/u==F(20,21)<1
assert sum((F(6)**j/F(factorial(j)) for j in range(7)),F())>200
assert sum((F(5)**j/F(factorial(j)) for j in range(7)),F())>100
assert F(1,100)+2*(F(125,61)+F(625,9999))<5
assert F(10,2**14)*(1+F(2,13))<F(1,1000)
assert u*100/8>3**5
assert F(1,2*C*2**2)<F(1,100)
assert F(99,100)-F(2,1000)>F(49,50)
print('PASS: all rational constants in eta15 explicit P=1 cone k>=10000N^2, N>=2')
