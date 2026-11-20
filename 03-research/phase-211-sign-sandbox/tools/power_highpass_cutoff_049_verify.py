from fractions import Fraction as F
j=F(32)
assert (2*j-F(3,2))**2-88*(j+11)==F(489,4)
assert (2*j-F(1,2))**2-80*(j+12)==F(2049,4)
assert 4*(2*j-F(3,2))-88>0
assert 4*(2*j-F(1,2))-80>0
assert F(8,3969)<F(1,400)
r=F(12,23)
loglower=2*sum((r**(2*k+1)/F(2*k+1) for k in range(12)),F())
assert loglower>F(921,800)
assert F(31,19)<2
assert F(63,992)*3<F(1,5)
assert 3*F(9,62)**32<F(1,1000)
assert F(11,10)-1-F(1,1000)==F(99,1000)
print('PASS: J=32; all numerator inverse moment <1/400; E2 highpass tail >.099 norm squared')
