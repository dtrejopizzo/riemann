# E71.16 -- Connes Fact 6.4 bridge for Stable Divisor Identification

**Date:** 2026-07-07.
**Role:** audit the sources suggested by the user and import the strongest available Connes result
into the E71.15 proof attempt.

## Sources checked

Primary source:

```text
Alain Connes,
The Riemann Hypothesis: Past, Present and a Letter Through Time,
arXiv:2602.04022.
```

Relevant sections:

- §6.1: finite real-zero theorem for Fourier transforms of minimal eigenvectors;
- §6.2: `Xi` as Fourier transform of `k=E(h)`;
- §6.4: construction of `k_lambda=E(h_lambda)` from prolate functions;
- §6.5: convergence `hat k_lambda -> Xi`;
- §6.6: remaining steps.

Also checked:

```text
Connes--Consani, On the metaphysics of F1, Rend. Lincei Mat. Appl. 35 (2024).
```

That paper provides the global F1/arithmetic-site and counting-distribution background, but not the
specific finite CCM stable-divisor theorem needed here.

## What Connes already proves

The decisive result is Fact 6.4 in `arXiv:2602.04022`:

```text
The Fourier transform of k_lambda converges, as lambda -> infinity,
towards Riemann's Xi function uniformly on closed substrips of |Im z| < 1/2.
```

This is exactly the kind of locally uniform convergence E71.5 needs.

But it is for the **constructed prolate model vector**

```text
k_lambda = E(h_lambda),
```

where `h_lambda` is the localized/prolate analogue of the Hermite combination `h` from §6.2.

It is not, by itself, the convergence of the actual finite CCM minimal eigenvectors / Weyl
`m_N` ground-vector data:

```text
xi_N  or  theta_x.
```

## What remains open in Connes's own statement

Connes §6.6 says the remaining steps are:

1. show that the smallest eigenvalue of the Weil quadratic form `QW_lambda` is simple with even
   eigenvector;
2. show that `k_lambda` is a sufficiently good approximation of the actual finite/minimal vector
   `theta_x`, with `lambda=sqrt(x)`.

This is precisely our missing Proposition 15.2 in E71.15, translated into Connes's notation.

## Translation to Phase 71 notation

Phase 71 uses finite CCM Weyl data:

```text
(D_N, xi_N),
m_N(s)=sum_k xi_{N,k}/(s-d_{N,k}).
```

Connes's analytic chain is:

```text
h_lambda  ->  k_lambda=E(h_lambda)  ->  hat k_lambda  ->  Xi.
```

The bridge needed is:

```text
xi_N / theta_x  ->  k_lambda
```

in a topology strong enough that Fourier transforms and zeros converge.

Thus the stable divisor identification becomes:

### Connes--CCM Eigenvector Approximation Lemma

After the correct recentering and normalization, the finite CCM minimal eigenvector `theta_x`
converges to Connes's prolate model vector `k_lambda` as `x=lambda^2 -> infinity`, with an error small
enough to preserve local uniform convergence of Fourier transforms:

```text
hat theta_x - hat k_lambda -> 0
```

on compact subsets of `|Im z|<1/2`.

Combined with Fact 6.4:

```text
hat k_lambda -> Xi,
```

this gives:

```text
hat theta_x -> Xi.
```

Then Theorem 6.1 / E71.5 Hurwitz yields RH.

## What this closes

This source audit closes a conceptual uncertainty:

```text
the correct target is not an unknown arbitrary determinant;
it is the convergence of the finite CCM minimal eigenvector to the prolate model k_lambda.
```

E71.12 persistence is now interpretable as the finite spectral symptom of this vector convergence.

## What it does not close

It does **not** prove the Eigenvector Approximation Lemma.

The open step is now sharper than in E71.15:

```text
Prove theta_x - k_lambda -> 0 in a Fourier-controlling norm.
```

This is not a static divisor problem anymore. It is an eigenvector perturbation problem between:

1. the true finite Weil operator `QW_lambda`;
2. the prolate/Sonin model operator generating `k_lambda`.

## Why this avoids the old walls

This bridge avoids:

- Stone/global Hilbert-Polya: finite real-rootedness comes from Theorem 6.1, not from a limiting
  self-adjoint zeta operator;
- KMS/zeta partition: `k_lambda` is built from prolate/Hermite and the summation map `E`, not from a
  Gibbs state;
- static Weil positivity: the remaining problem is approximation of eigenvectors, not proving
  `QW_lambda >= 0`.

But it may still hit MW-2 if the eigenvector approximation requires arithmetic propagation beyond the
finite Euler input.

## New exact theorem target

Replace E71.14's abstract projection theorem by the sharper source-backed statement:

### E71.16 Target -- Prolate-CCM Ground-State Convergence

Let `theta_x` be the recentered finite CCM minimal eigenvector associated with the finite Weil form
with prime cutoff `x=lambda^2`. Let

```text
k_lambda = E(h_lambda)
```

be Connes's prolate model vector. Prove, with a canonical normalization, that

```text
||hat theta_x - hat k_lambda||_{K} -> 0
```

for every compact `K` in the strip `|Im z|<1/2`.

Then by Connes Fact 6.4:

```text
hat theta_x -> Xi
```

locally uniformly in that strip. Since Theorem 6.1 gives real zeros for every `hat theta_x`, Hurwitz
forces the zeros of `Xi` in the strip to be real. This is RH.

## Status

```text
proved in source:    hat k_lambda -> Xi;
open here/source:    theta_x -> k_lambda;
consequence:         theta_x -> Xi -> RH by Hurwitz.
```

So the source does not give the missing theorem outright, but it reduces it to the exact eigenvector
approximation lemma that Connes himself lists as a remaining step.
