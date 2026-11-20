# Auxiliary diagnostics of the second round

2026-10-18. **NUMERICAL, exploratory, not certified.** Not used in any
proof of ANTICORRELATION_003 or CONSTRUCTOR_004.

Gaussian moments were evaluated with cutoff n²πy≤45 to guide the proof
of concavity of log(θ−1)(e^x). The observed sign was negative; note 003
replaces it by a uniform analytic proof. Small samples of laws with one
prime excluded were also tested: they showed no robust violation of the
punctured anticorrelation. This does NOT prove inheritance or specificity.

A tempting extension of the cross sign to matrix order was checked:

    D_y(d,e)=y^(-1/2)(gcd(d,e)-1)/(de)-τ(y)C_y(d,e).

With indices {2,3,5,7}, y=0.001, diagonalisation in double precision gave a
minimum close to -0.04752. Hence the sample does not support D_y PSD. That
domination is neither formulated nor used as a lemma; the test is not a certified NO-GO.
Do not confuse positivity of the coprime entries of -τC with positivity of the form.

Reproduction of the matrix diagnostic, with Python3/numpy:

```python
import math
import numpy as np
indices=[2,3,5,7]
y=0.001
nmax=int(math.sqrt(45/(math.pi*y)))+1
def tau(k):
    return 2*sum(math.exp(-math.pi*y*k*k*n*n)
                 for n in range(1,nmax+1))
z=tau(1)
a={d:tau(d) for d in indices}
D=np.array([[(math.gcd(d,e)-1)/(d*e*math.sqrt(y))
             -tau(math.lcm(d,e))+a[d]*a[e]/z
             for e in indices] for d in indices])
print(np.linalg.eigvalsh(D))
```

These tests only prevent extrapolating the scalar proofs to an unproved
operator inequality. They do not alter the status of O1.
