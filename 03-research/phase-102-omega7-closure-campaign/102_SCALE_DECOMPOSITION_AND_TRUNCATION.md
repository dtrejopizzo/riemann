# 102 scale decomposition and truncation

## Purpose

The direct Li route must cover all `n>=8` without hiding a dependence on `n`
inside a constant.  The natural variable is

[
  u=\log y.
]

In this variable the tail part of the paired integral is

[
  \int_T^\infty
  E(e^u)e^{-u}
  \left[
    -L_{n-1}^{(1)}(u)+{d\over du}L_{n-1}^{(1)}(u)
  \right]du
]

at `epsilon=0`.

## Scale partition

For proof discovery, the kernel has four visible regions:

[
  0\le u\ll n,\qquad
  u\asymp n,\qquad
  n\ll u\lesssim4n,\qquad
  u\gtrsim4n.
]

This partition is diagnostic only.  A final proof may avoid it, but any
localized proof must state how the constants combine across all four regions.

## What A0 closes

The uniform tail theorem closes the region

[
  u\ge T(n),
]

where `T(n)` is chosen after `n` and satisfies the explicit PNT domination
condition.  The closure is absolute and therefore does not use the signed
problem.

This is allowed because it is applied only after the finite core has been
kept intact.  It does not attempt to prove Omega7 by bounding the whole prime
side in absolute value.

## What A0 does not close

A0 does not control the core

[
  0\le u\le T(n).
]

For the core, absolute estimates destroy the target.  The expression

[
  -n+\int_1^{e^{T(n)}}E(y)f'_{n,0}(y)\,dy
]

must be estimated as one signed object.  Splitting it into prime powers,
Laguerre lobes, short intervals, or shells is admissible only if the splitting
comes with an exact compensation law whose sum is made before absolute values
enter.

## Truncation rule

Every truncation in phase 102 must have one of the following forms:

- an absolute tail after the signed core has been isolated;
- a signed finite decomposition whose omitted part has a one-sided remainder;
- an exact identity with no omitted part.

The following form is not admissible:

[
  \left|
  \int_{\hbox{core}}E(y)f'_{n,0}(y)\,dy
  \right|
  \le
  \int_{\hbox{core}}|E(y)||f'_{n,0}(y)|\,dy.
]

That estimate is true but loses the only cancellation that can close A1.

## Status

Point 7 and point 14 are reduced to A0 plus A1.  The scale and truncation
bookkeeping is closed; the signed core remains open.
