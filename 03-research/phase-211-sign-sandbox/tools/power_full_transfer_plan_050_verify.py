from fractions import Fraction as F
from math import comb
alpha=F(2,3)
B=sum((F(comb(j,k)**2)*alpha**(2*k)/(1-alpha)**(2*j+1) for j in range(12) for k in range(j+1)),F())
assert B==1282776893780652
b=35815875
assert (b-1)**2<B<b*b
# Log bounds from positive atanh series, with explicit positive tail.
def log_interval(x):
    r=(x-1)/(x+1)
    lo=2*sum((r**(2*k+1)/F(2*k+1) for k in range(64)),F())
    hi=lo+2*r**129/(129*(1-r*r))
    return lo,hi
for M,L,s,upper in [(3,F(11,10),F(17,10),F(5126,10**6)),(4,F(7,5),F(2),F(13763,10**9)),(5,F(17,10),F(11,5),F(146,10**9))]:
    assert log_interval(F(M))[1]<L
    assert s*s<=M
    bound=2*b/s*F(1,M**21)*(L+M*L/20+F(M,400))
    assert bound<upper
    assert (bound<F(1,2500))==(M>=4)
    print('PASS tail from',M,'bound',float(bound))
print('PASS: exact BT12, and keeping contacts2,3 suffices for this tail comparison if joint orbit has c=1/2500')
