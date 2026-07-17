# P76.044 - Consecutive Sturm-chain autopsy

The right core numerators have degrees `2N-1`.  A necessary two-step
interlacing condition was tested from `N=5` through `N=9`.

For zeta the numbers of violations were

```text
N=5->6: 1
N=6->7: 0
N=7->8: 0
N=8->9: 1.
```

The violations occur at extreme roots (`O(10^3)`) that cross through the
projective point at infinity as the leading coefficient changes.  Thus the
finite core polynomials do not form an ordinary global Sturm chain.

For the planted off-line model the corresponding counts were

```text
1, 0, 0, 0.
```

Therefore even a projectively repaired/local interlacing theorem would not
provide arithmetic identification: the planted falsifier largely shares
the behavior.

## Decision

Consecutive interlacing is closed as a route to `Omega7`.  It may explain
finite-section stability on compact windows, but it cannot identify the
limit with zeta and is not a substitute for the safe-axis arithmetic
identity.

The endpoint remains the convergence of the core safe logarithmic
derivative.  Any next route must discriminate the planted model at the
function level, not merely prove real-rootedness or interlacing inherited
from finite positivity.
