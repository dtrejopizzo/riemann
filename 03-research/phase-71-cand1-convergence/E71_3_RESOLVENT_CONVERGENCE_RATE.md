# E71.3 -- convergence rate and the PNT horizon for CAND-1

**Date:** 2026-07-07.
**Script:** `E71_3_convergence_rate_pnt.py`.
**Role:** sharpen the CAND-1 proof target after E71.1-E71.2.

## Starting point

E71.1 and E71.2 changed the shape of the remaining problem:

```text
not:    prove a Weil-positive form;
but:    prove convergence of explicit self-adjoint CCM operators.
```

The spectrum is real by the CCM construction tested in E71.1. Therefore an off-line zero is not seen as
a complex eigenvalue; it is seen as failure of convergence.

E71.2 verified this numerically:

```text
zeta true:       eigenvalue errors -> 0 in the tested window;
planted off-line: errors stall at a stable nonzero floor.
```

Thus CAND-1 is a live detector. E71.3 asks whether the rate can be bounded using only the finite Euler
product / PNT side.

## Three convergence layers

The phrase

```text
sp(H_x) -> zeta zeros
```

contains three different limits.

### 1. Finite-section convergence at fixed `lambda`

For fixed `lambda`, the CCM matrix is truncated to Fourier modes `|k|<=N`. Increasing `N` is a
finite-section approximation to the fixed-`lambda` operator.

This layer is not expected to be monotone. The poles

```text
d_k = 2*pi*k / L,       L = 2 log lambda,
```

move only through the cutoff `N`, and roots of the rational function can alias between nearby gaps.
So the relevant statement is not monotone error decrease, but saturation:

```text
H_{lambda,N} -> H_lambda      in norm/strong resolvent sense.
```

### 2. The `lambda -> infinity` CCM horizon

The zeta zeros are reached only after the fixed-`lambda` operator itself converges:

```text
H_lambda -> H_zeta.
```

Equivalently, the resolved zero horizon

```text
H(lambda; eps) = largest height up to which consecutive zeros are eps-close
```

must satisfy

```text
H(lambda; eps) -> infinity.
```

This is the real analogue of the Phase-60 E6 horizon.

### 3. Resolvent stability

Even if matrix entries converge, roots/eigenvalues converge only when the relevant resolvent is stable.
The theorem needed is a bound of the form

```text
dist(sp(H_lambda), zeros up to height T) <= C(T) * R(lambda),
R(lambda) -> 0.
```

The constant `C(T)` is a spectral conditioning/resolvent constant. If it is allowed to encode the
zeros, the proof is circular. If it is bounded from the CCM algebra itself, this becomes a genuine
CAND-1 closure route.

## What PNT can and cannot do

The finite Euler product in the CCM matrix uses prime powers

```text
p^m <= lambda^2.
```

PNT controls the size and density of this input:

```text
sum_{n<=lambda^2} Lambda(n) ~ lambda^2.
```

That is enough to control crude matrix-entry growth and to justify that the arithmetic input becomes
denser as `lambda` grows.

But PNT alone does **not** control the oscillatory error needed for the zeta-zero limit. If it did, it
would already imply a zero-location theorem much stronger than PNT. Therefore:

```text
PNT may bound the finite Euler product size;
PNT cannot by itself prove sp(H_lambda)->zeta zeros.
```

The missing ingredient is resolvent rigidity: the CCM rational function must convert the exact finite
Euler data into stable zeros without requiring a Weil-positivity estimate.

## E71.3 diagnostic

The script keeps the E71.2 engine and reports:

1. fixed-`lambda` finite-section errors for true zeta;
2. the same scan with a planted off-line zero;
3. a small `lambda` horizon scan with `N` chosen to cover the first five zeros.

The discriminant is:

```text
true zeta improves/saturates toward zero;
planted off-line retains a nonzero floor;
lambda horizon improves as lambda grows.
```

The output should not be read as a theorem. It is a rate probe for the next theorem.

## The exact theorem now needed

### CCM Resolvent Convergence Theorem

Let `H_{lambda,N}` be the finite CCM operator and `H_lambda` its finite-section limit. There exist
zero-independent constants `C(T)` and an arithmetic error function `R(lambda,T)->0`, obtained from the
explicit Euler/Gamma construction and not from the zeros, such that

```text
||(H_lambda-z)^(-1) - R_zeta(z)|| <= C(T) R(lambda,T)
```

uniformly for `z` in contours isolating the first zeros up to height `T`.

Then the Riesz projections converge, hence

```text
sp(H_lambda) -> {gamma_rho}
```

on every bounded height window.

Since each `H_lambda` is self-adjoint, the limiting zeros in that window are real. Therefore the theorem
implies RH.

## Honest status

E71.3 does **not** close RH. It narrows CAND-1 to the one non-circular theorem that would close it:

```text
prove zero-independent CCM resolvent convergence.
```

This is materially different from Phases 67-70. The missing statement is not positivity of the Weil
form; it is compactness/rigidity of an explicit self-adjoint approximation scheme.

## Important correction to keep the route honest

The slogan "real rational function with real simple poles has all real roots" is false for arbitrary
residues. The E71.1 numerics show that the CCM ground vector produces all-real roots in the tested
cases even with mixed signs, but the theorem must use the actual CCM structure of `xi`, not a generic
rational-function claim.

So the safe statement is:

```text
CCM self-adjointness supplies real finite spectra;
generic rational functions do not.
```

This correction strengthens the audit: CAND-1 remains off MW-1, but the proof must cite the CCM
self-adjoint operator construction rather than a false generic interlacing lemma.
