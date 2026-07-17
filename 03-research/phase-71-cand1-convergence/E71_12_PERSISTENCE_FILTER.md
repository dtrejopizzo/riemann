# E71.12 -- finite-section persistence filter

**Date:** 2026-07-07.
**Script:** `E71_12_persistence_filter.py`.
**Role:** test a zero-independent dynamic background principle after static backgrounds failed.

## Motivation

E71.8-E71.11 show that the finite CCM divisor contains two kinds of roots:

```text
physical roots:    lock near zeta zeros;
background roots:  finite-section artifacts.
```

Static backgrounds failed:

- all-root product;
- pole mesh;
- sine comb;
- arch/free quotient.

So the next possible zero-independent rule is dynamic:

```text
physical divisor = roots persistent under refinement in N;
background       = roots drifting with N.
```

## Diagnostic

For several values of `N`, compute the positive roots of

```text
m_N(s)=sum_k xi_k/(s-d_k).
```

Cluster roots across `N` using only a numerical radius, without using known zeta zeros. After
clustering, compare the persistent centers to known zeros only as an audit label.

## Why this is allowed

The clustering uses only finite CCM spectra. It does not use:

- zeta zero locations to define clusters;
- positivity;
- Stone/unitarity;
- KMS or partition normalization.

It is still not a proof: a persistence filter is an algorithmic detector, not a normal-family theorem.

## What would count as progress

For true zeta:

```text
persistent clusters should align with the first zeta zeros.
```

For the planted off-line control:

```text
persistent clusters should either drift away from zeta zeros or reveal a displaced stable floor.
```

This would support the idea that the relative determinant must quotient drifting roots and retain the
stable divisor.

## Closure interpretation

A proof cannot define the determinant by "keep persistent roots" as an algorithm unless that rule is
shown to arise from a canonical compactness/Fredholm construction.

But persistence can identify the mathematical object to seek:

```text
stable spectral subspace / Riesz projection limit of the CCM m-function.
```

This is exactly the operator-theoretic version of the Hurwitz theorem in E71.5.

## Result

The persistence filter works sharply as a diagnostic. Results are recorded in `E71_12_RESULTS.md`.

For true zeta, persistent clusters recover the first low zeros without using zero locations as input.
For the planted off-line control, only a displaced cluster near the planted height persists and the
full coherent zeta divisor is lost.

The next step is to replace algorithmic persistence by an intrinsic stable Riesz/Fredholm projection.
