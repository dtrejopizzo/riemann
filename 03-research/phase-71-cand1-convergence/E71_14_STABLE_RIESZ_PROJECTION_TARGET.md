# E71.14 -- stable Riesz/Fredholm projection target

**Date:** 2026-07-07.
**Role:** convert the successful persistence diagnostic into a precise theorem target.

## What E71.12-E71.13 found

Static backgrounds failed. Dynamic persistence succeeded:

```text
true zeta:        persistent clusters reconstruct the low zeta divisor;
planted control:  persistence collapses to a displaced/falsifying cluster.
```

The persistent product improved the determinant shape without using zero locations.

But numerical clustering is not a mathematical object. The next step is to replace it by an intrinsic
projection.

## Desired intrinsic object

Let

```text
m_N(s) = sum_k xi_{N,k}/(s-d_{N,k})
```

be the CCM Weyl function.

We need a canonical decomposition

```text
m_N = m_N^{phys} + m_N^{bg}
```

or equivalently a factorization of the numerator

```text
P_N = P_N^{phys} P_N^{bg},
```

such that:

1. `P_N^{phys}` contains exactly the Riesz-stable divisor;
2. `P_N^{bg}` contains the drifting finite-section background;
3. the construction uses only finite CCM data, not zero locations;
4. `P_N^{phys}` forms a normal family;
5. after canonical normalization,

```text
P_N^{phys}(s) -> Xi(s)/Xi(0)
```

locally uniformly.

## Stable Riesz Projection Theorem

The theorem needed is:

### Theorem Target

There exists a sequence of finite-rank projections

```text
Pi_N^{phys}
```

defined functorially from the CCM Weyl data `(D_N,xi_N)` such that the determinant

```text
D_N^{phys}(s) = det(1 - s^2 (Pi_N^{phys} H_N Pi_N^{phys})^{-2})
```

is well-defined, has only real zeros, and satisfies

```text
D_N^{phys}(s) -> Xi(s)/Xi(0)
```

locally uniformly on `C`.

Then RH follows by E71.5.

## What "functorially" must forbid

`Pi_N^{phys}` may not be defined by:

- proximity to known zeta zeros;
- positivity of the Weil form;
- sign of the ground energy `epsilon_0`;
- KMS/zeta partition weights;
- a boundary phase fitted from `zeta`;
- spectral factorization of a known nonnegative limit.

It may use:

- the pole mesh `D_N`;
- the CCM ground vector `xi_N`;
- finite-section comparison maps `N -> N'`;
- Riesz stability under those maps;
- compactness/Fredholm data intrinsic to the finite construction.

## Why this is not Phase 53

Phase 53 killed global Stone/Hilbert-Polya:

```text
choose a Hilbert metric or boundary condition so the zeta spectrum is real.
```

E71.14 asks instead:

```text
finite real spectra are already given;
construct the stable finite-section divisor and prove normal convergence.
```

The missing work is compactness/convergence, not positivity or unitarity.

## Current status

E71.14 is the sharpest CAND-1 endpoint reached in Phase 71:

```text
closed experimentally: stable divisor exists and separates planted controls;
open mathematically:   intrinsic construction of Pi_N^{phys} and proof of normal convergence.
```

This is not a proof of RH. It is a precise theorem target outside the previously catalogued walls,
provided the projection is built without the forbidden inputs above.
