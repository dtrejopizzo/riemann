# Point 09 - Arithmetic discriminant

## Role

The discriminant is the part of the proof that must distinguish the zeta
Euler--Gamma data from an admissible off-line control. It cannot be a
coordinate change that is true for both builds and then imports positivity at
the last step.

## Minimal formulation after A0

Let \({\cal C}_{\rm EG}\) be a class of completed Euler--Gamma data with:

- the same Gamma symmetry type;
- a Dirichlet-series logarithmic derivative in a right half-plane;
- a paired prime-side continuation to the Li coefficients;
- a functional equation allowing the Li criterion to be stated.

A discriminant theorem sufficient for point 09 is:
\[
  D_{\zeta}(n):=
  -n+\int_1^{e^{T_n}}E_\zeta(y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_{n,\zeta}^{\rm arch}
  \ge0
  \qquad(n\ge8),
\]
while for a typed off-line perturbation \(F\in{\cal C}_{\rm EG}\) with a zero
\(\rho\) satisfying \(|1-1/\rho|>1\), the analogous inequality fails for
some index.

## What this buys

The theorem is not an auxiliary aesthetic test. It is exactly the arithmetic
content required to prove A1 for zeta while preventing a build-neutral proof
from proving a false statement for an off-line model.

## Status

Open. A0 does not supply the discriminant. The discriminant is now identified
with the compact signed core inequality, not with GAP-Z or another purely
convergence statement.
