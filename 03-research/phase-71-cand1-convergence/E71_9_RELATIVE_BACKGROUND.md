# E71.9 -- relative determinant with archimedean/free background

**Date:** 2026-07-07.
**Script:** `E71_9_relative_arch_background_probe.py`.
**Role:** test the first zero-independent candidate for the background determinant `B_N`.

## Motivation

E71.8 showed that the all-root product

```text
D_N^{all}(t) = product_{r in sp_+(H_N)} (1 - t^2/r^2)
```

is contaminated by background roots below the first zeta zero.

The first natural background is the same CCM finite construction with the arithmetic prime-power term
removed:

```text
H_N^{arch/free}.
```

This gives a zero-independent determinant

```text
B_N^{arch}(t) = product_{r in sp_+(H_N^{arch})} (1 - t^2/r^2).
```

Then test

```text
D_N^{rel}(t) = D_N^{all}(t) / B_N^{arch}(t).
```

## Why this is allowed

The arch/free background uses:

- the same pole mesh `d_k`;
- the same Fejer/CCM window;
- the same Gamma/polar terms;
- no zeta zeros;
- no positivity assumption.

Thus it does not violate the Phase 53 or NO-GO audit.

## What would count as progress

If `D_N^{all}/B_N^{arch}` is much closer to `Xi/Xi(0)` than `D_N^{all}`, then the determinant problem
has a concrete shape:

```text
Xi = limit of a relative Euler-vs-arch CCM determinant.
```

If it fails, the background is not purely archimedean/window. The required cancellation is subtler and
may involve a de Branges or Fredholm determinant normalization.

## Result

The arch/free quotient fails badly. Results are recorded in `E71_9_RESULTS.md`.

The failure means the background roots of the zeta finite section are not the spectrum of the
arch/free finite section. A naive quotient of two spectral products introduces poles/near-poles rather
than cancelling the finite-section background.

The next candidate is a finite-dimensional perturbation determinant

```text
det(I - (QW_zeta - QW_arch)(QW_arch - z)^(-1)),
```

which compares the operator pair directly.

## Status

The script is a diagnostic. A proof would require:

1. a canonical definition of the relative determinant;
2. normal-family estimates;
3. local uniform convergence to `Xi`.

Then E71.5 applies.
