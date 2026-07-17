# P76.040 - Hard Euler trace autopsy

The proposed identity

```text
core Schur trace
 ?=arch_gamma(s)-2 sum_{n<=lambda^2}Lambda(n)n^(-s)+o(1)
```

is false at finite scale and is not a valid starting identity.

At `lambda=6` (`lambda^2=36`) the comparison is:

```text
sigma   2 Xi'/Xi       hard truncated Euler target
0.60    0.05542         14.08965
0.75    0.06925          3.36871
1.00    0.09227          0.77244
1.50    0.13813          0.19588
2.00    0.18367          0.19020
```

The finite Schur trace is of order `0.1--0.3`, not `14`, in the same range.
Thus the nonlinear Schur quotient cannot be replaced by the hard truncated
Dirichlet series with a small finite-section error.

## What remains true

P76.039 correctly proves that the hard prime tail converges locally uniformly
on every fixed compact in `Re(s)>1` as `L -> infinity`.  What fails is the
asserted finite identity linking that hard truncation to `T_+'/T_+`.

The CCM cells couple the archimedean and prime terms before the Schur solve.
The solve performs a signed rational/Padé-type regularization; separating it
afterward into a raw Gamma term and a raw prime sum destroys that coupling.

## Route closure

The formula `(RTS-3)` in P76.036 and `(ET-3)` in P76.039 are withdrawn as
proof targets.  The valid endpoint remains `CORE-SR-LOG`, but its finite
comparison object must be derived exactly from the cell transform.  It may
not be postulated to be the hard Euler truncation.

## Next finite object

Define the exact cell-smoothed trace symbol

```text
J_{L,N}(sigma)
=L coth(sigma L/2)+2 Re[iT_+'(i sigma)/T_+(i sigma)]
 -B_ext,L,N(sigma).                              (HA-1)
```

The next task is to express `J_{L,N}` before inversion using the rank-two
displacement generators `(u,v,s,1)` and identify its signed continuum limit.
Only after that exact formula is obtained may its Gamma-prime pieces be
compared with `2 Xi'/Xi`.
