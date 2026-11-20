"""One compensated primitive point; complete tails, no global sign extrapolation."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
import power_inverse_interior_022_verify as V
J=C.I(0)
for m in range(1,V.M+1):
    mu=V.moebius(m)
    if not mu:continue
    z=C.I(0);t=C.logq(m)
    for coeff in reversed(V.p):z=z*t+coeff
    J+=mu*z/m**32
jtail=sum((a*b for a,b in zip(V.p,V.integrals)),F(0))
K=J+V.partial
ktail=jtail+V.tail
assert F(665,1000)<J.lo-jtail<J.hi+jtail<F(666,1000)
assert F(3,1000)<K.lo-ktail<K.hi+ktail<F(4,1000)
assert jtail<F(1,10**10) and ktail<F(1,10**10)
assert F(3,4)-C.log2.hi>0
print('PASS: COMPLETE J128(1) in(.665,.666), K128(1)=J128(1)+h128(1) in(.003,.004).')
print('Only one point; K>=0 on the entire half-line remains OPEN.')
