"""Universal comparison constants, no individual N evaluation or scan."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
arch=C.logq(F(15,2))-2*C.log2-C.logpi+1-C.gamma/2-F(4,25)
assert arch.lo>F(7,200)
polar0=F(24,25)*F(225,224)
assert polar0==F(27,28)
polar1=polar0*F(3,337)
assert polar1<F(9,1000)
assert F(7,200)-F(9,1000)>F(1,40)
u=F(63,2)
assert 4*u*u/225==F(441,25) # 17.64, hence all integer N<=17.
assert F(46,225)*u>F(1,3)
# All higher columns use stronger ARCH and an absolute full-prime estimate.
arch2=arch+F(1,3)+F(8,75)
assert arch2.lo>F(19,40)
assert F(63,2)**2>720
assert F(7,150)*720==F(168,5)
assert F(9,10)-F(64,75)==F(7,150)
assert F(9,10)<C.logq(F(5,2)).lo
U=F(5,7*16)*(F(5,3)*C.log2+F(2,9))
assert U.hi<F(31,500)
assert F(19,40)-5*F(31,500)-F(9,1000)>F(3,20)
assert F(3,337)<1
print('PASS: ALL N>=3,k>=1,u>=31.5,u^2>=225N/4: FULL W>norm^2/40; k>=2 gives >3norm^2/20.')
print('k1 normalized comparator B+S_K>1/40 for every odd K; no individual N evaluation.')
