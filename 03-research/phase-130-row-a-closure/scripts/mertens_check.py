# check: sum_N Lambda(N)/N * phi(log N) -> integral phi = 1 for wide smooth bumps phi
import numpy as np
from sympy import primerange
X=int(4e7)
# Lambda via sieve of primes up to X (prime powers)
primes=np.array(list(primerange(2,X+1)))
def S(phi):
    tot=0.0
    for p in primes:
        lp=np.log(p); pk=p; j=1
        while pk<=X:
            tot+=lp/pk*phi(j*lp); pk*=p; j+=1
    return tot
def bump(c,w):  # smooth bump centered c, half-width w, normalized
    def phi(t):
        u=(t-c)/w
        return (np.exp(-1/(1-u*u)) if abs(u)<1 else 0.0)
    from scipy.integrate import quad
    Z=quad(phi,c-w,c+w)[0]
    return lambda t: phi(t)/Z
for c,w in [(8,3),(10,5),(12,5)]:
    print(f"center {c}, halfwidth {w}: sum = {S(bump(c,w)):.4f}  (need log X={np.log(X):.1f} > {c+w})")
