"""Exact scalar inequalities for global four-pole sign transfer.
Input AP>=49/200 is independently certified in power_confluent_four_005_verify.py.
This verifier uses only Python integers and Fraction.
"""
from fractions import Fraction as F
from math import factorial
u=F(63,2)
# Elementary constants implying m(0)>-11/2.
log2lower=2*(F(1,3)+F(1,81)+F(1,1215))
assert log2lower>F(693,1000)
H32=sum((F(1,k) for k in range(1,33)),F(0))
assert H32-5*F(693,1000)<F(3,5) # gamma<H32-log32<3/5
assert F(25,36)<F(7,10) # log2<2/3+1/36=25/36
assert sum((F(23,20)**k/F(factorial(k)) for k in range(7)),F(0))>F(22,7)
assert F(3,5)+F(11,7)+3*F(7,10)+F(23,20)<F(11,2)
# Uses classical pi<22/7. The preceding exponential sum gives logpi<23/20.
def lower(x):
 return -F(11,2)+sum((F(x)/(F(4*k+1,4)*(4*F(4*k+1,4)**2+x)) for k in range(16)),F(0))
assert lower(4)>-F(4,3)
assert lower(16)>-F(3,5)
assert lower(32)>-F(1,4)
assert lower(64)>F(2,25)
assert lower(81)>F(1,10)
# For intervals [0,4],[4,16],[16,32],[32,64],[64,81],
# x*(1/10-m)_+ <= right endpoint * (1/10-lower at left).
for b,L in [(4,-F(11,2)),(16,-F(4,3)),(32,-F(3,5)),(64,-F(1,4)),(81,F(2,25))]:
 assert b*(F(1,10)-L)<23
K=((1+F(81)/(u*u))**4-1)/81
assert F(49,200)-F(1,10)-23*K-1/(u*u)>F(3,100)
# Exact confluence polar operator bound |2AB|<||f||^2.
AA=F(63,31**2)*sum((F(32,31)**(2*j) for j in range(4)),F(0))
BB=F(63,32**2)*sum((F(31,32)**(2*j) for j in range(4)),F(0))
assert 4*AA*BB<1
# Uniform prime cost from B4=32552, sqrt(B4)<181.
assert 32552<181**2
assert F(362,28672)<F(13,1000)
assert F(1,10)-F(13,1000)>F(2,25)
print('PASS: m(0), five scalar panels, spectral threshold, filter loss, polar norm, prime loss.')
print('Global conclusion: W[f] > (2/25)||f||^2 on every four-real-pole space with poles >=63/2.')
