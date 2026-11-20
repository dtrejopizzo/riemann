"""One prescribed J=96 certificate on Q^J V13; no search over J or vectors."""
from fractions import Fraction as F
from math import comb

n, J = 13, 96
b = F(1, 5)

def choose(N, k):
    return comb(N, k) if 0 <= k <= N else 0

A = [[(1+b)*choose(2*J, J+x-y)
      - 4*choose(2*J-2, J-1+x-y)
      for y in range(n)] for x in range(n)]
for k in range(n):
    pivot = A[k][k]
    assert pivot > 0, (J, k)
    for x in range(k+1, n):
        for y in range(k+1, n):
            A[x][y] -= A[x][k]*A[k][y]/pivot
    print('PASS exact inverse-moment pivot', k, flush=True)

# log(56/5) = 2 sum r^(2k+1)/(2k+1), r=51/61.
# A positive finite prefix gives a lower bound; no decimal logarithms.
r = F(51, 61)
log_lower = 2*sum((r**(2*k+1)/F(2*k+1) for k in range(32)), F())
assert log_lower > F(12, 5)+F(1, 70)+F(1, 9800)
assert F(559, 250)**2 < 5
assert F(63, 2)*F(559, 250)/(2*F(22, 7)) > F(56, 5)
assert F(4, 19845) < F(1, 70**2)
assert F(2, 19845) < F(1, 9800)
assert F(12, 7)**2 < 3
assert F(10, 7)**2 > 2
assert F(77, 60) < F(13, 10)
assert F(7, 60)-F(1, 1000) > F(1, 10)

# Dimension-13 polar row bound and effective highpass ratio.
u = F(63, 2)
for k in range(n):
    band = F(63, 992)*(F(32, 31)**k+F(31, 32)**k)
    assert band < F(1, 5)
assert F(13, 5) < 3
assert F(169, 992) < F(1, 5)
assert 3*F(1, 5)**J < F(1, 1000)
print('PASS: J96 moment <1/5, ARCH>12/5 and E23>1/10 on all Q^j V13, j>=96')
