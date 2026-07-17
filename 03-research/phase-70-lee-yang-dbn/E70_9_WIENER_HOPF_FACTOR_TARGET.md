# E70.9 — Wiener-Hopf factorization target for AHM

**Date:** 2026-07-07.
**Role:** formulate the strongest possible operator proof shape after local and Abel routes reduce to
the boundary problem.

## Operator target

In the additive Hardy model, the terminal form is

```text
< (A - T_Lambda) f, f > >= 0,
```

where

```text
T_Lambda = sum_{n>=2} Lambda(n)n^{-1/2}(S_log n + S_log n^*)
```

and `A` is the exact Gamma/polar archimedean form.

The desired theorem is:

```text
A - T_Lambda >= 0.
```

## Factorization route

The strongest possible non-spectral proof would exhibit an operator `D` such that

```text
A - T_Lambda = D^* D.
```

This is the Wiener-Hopf / Fejer-Riesz form of the proof.

If such a factorization is constructed from Euler/Gamma data without zero locations, then `Omega_7`
is closed.

## Symbol obstruction

For a true Toeplitz/Wiener-Hopf operator, a factorization follows from nonnegativity of the boundary
symbol:

```text
sigma_A(xi) - sigma_P(xi) >= 0.
```

But in the critical boundary,

```text
sigma_A - sigma_P
```

is exactly the boundary value of the Nevanlinna/Weil form. A sign change is exactly an off-line zero.
Therefore:

```text
existence of a boundary Fejer-Riesz factor
  <=> AHM
  <=> Omega_7.
```

The factorization is not easier unless the factor `D` is constructed independently.

## What an independent factor must look like

It cannot be:

- Cholesky of `A-T_Lambda`;
- spectral factorization of the already-known nonnegative symbol;
- KMS/Gibbs square root whose partition function is `zeta`;
- a per-prime product of local positive factors;
- a heat-flow factor at `lambda>0` continued without controlling boundary loss.

It would have to be a canonical Euler-Gamma factor:

```text
D = D_Gamma  +  D_Euler
```

with cross terms reproducing exactly

```text
-T_Lambda
```

and diagonal terms reproducing the archimedean drag.

In formula shape:

```text
D^*D
 = D_Gamma^*D_Gamma
   + D_Euler^*D_Euler
   + D_Gamma^*D_Euler
   + D_Euler^*D_Gamma
 = A - T_Lambda.
```

The negative prime-shift term must appear as a **cross term**, not as a positive Euler square. This is
the only way to keep the phase cancellation that all positive/Haar mechanisms lost.

## Cross-term identity

Thus the factorization route reduces to a single identity:

```text
D_Gamma^*D_Euler + D_Euler^*D_Gamma = -T_Lambda
```

with

```text
D_Gamma^*D_Gamma + D_Euler^*D_Euler = A.
```

This is a genuine possible shape for new mathematics: RH would follow from a hidden Euler-Gamma
supersymmetric square.

## Current obstruction

No canonical candidate for `D_Euler` is known. If one sets

```text
D_Euler ~ zeta^{-1/2}
```

or uses an Euler product square root directly, the construction is either outside the critical domain or
falls into KMS/zeta-partition circularity.

If one constructs `D` by spectral factorization of `A-T_Lambda`, one has assumed AHM.

## Status

The factorization route is the only remaining plausible proof architecture that is not merely an
estimate:

```text
find a canonical Euler-Gamma cross-term square
  => A-T_Lambda = D^*D
  => AHM
  => Omega_7.
```

The current program does not yet contain such a `D`. The target is now explicit.

