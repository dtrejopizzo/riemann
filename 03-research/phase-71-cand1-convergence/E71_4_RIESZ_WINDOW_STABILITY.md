# E71.4 -- Riesz-window stability for the CAND-1 convergence front

**Date:** 2026-07-07.
**Script:** `E71_4_riesz_window_stability.py`.
**Role:** replace nearest-root matching by the finite-dimensional Riesz projection criterion.

## Why E71.4 is needed

E71.3 showed that nearest-root error is a noisy convergence statistic. At fixed `lambda`, increasing
`N` can add roots and shift the nearest match, producing aliasing. That is not the right language for
operator convergence.

For self-adjoint operators, the natural statement is Riesz projection stability. A first coarse
attempt is to choose, around each target zero `gamma_j`, an isolating window

```text
I_j = ((gamma_{j-1}+gamma_j)/2, (gamma_j+gamma_{j+1})/2),
```

with the first interval closed on the left by a harmless lower cutoff. Then the finite spectral
projection rank is

```text
rank P_j(H) = # { eigenvalues of H in I_j }.
```

Equivalently,

```text
P_j(H) = (1/2*pi*i) integral_{Gamma_j} (z-H)^(-1) dz.
```

For finite real spectra, the contour integral is exactly the root count inside the window.

## Correct convergence criterion

The CAND-1 convergence statement up to height `T` should be:

1. each window `I_j`, `gamma_j<=T`, has rank one;
2. the unique eigenvalue in `I_j` converges to `gamma_j`;
3. the distance of that eigenvalue to the boundary of `I_j` stays positive enough to control the
   resolvent contour.

This avoids the nearest-root aliasing of E71.3 only if the window contains no extra finite-section
roots. The E71.4 diagnostic shows that full zero-gap windows are too coarse for the CCM finite spectra:
they can contain several extra roots even when a root is extremely close to the target zero.

Therefore the correct finite diagnostic is a **micro Riesz contour**

```text
|z - gamma_j| = r
```

with `r` much smaller than the zero gap and larger than the expected local convergence error.

## What would prove RH

If one proves, from the CCM Euler/Gamma construction and without zero-location input, that for every
fixed `T` the windows up to `T` eventually have stable rank one and the unique eigenvalue converges to
the zeta zero in that window, then:

```text
finite CCM spectra are real
stable Riesz convergence reaches every zeta zero
=> all zeta zeros are real heights
=> RH.
```

The theorem still requires knowing which windows isolate the zeta zeros. In a final proof this must be
phrased as convergence of the entire divisor/counting measure or as contour convergence for the
completed zeta function, not as an input list of zeros. The numerical diagnostic can use known zeros
because it is only testing the mechanism.

## The exact non-circular theorem

### CCM Riesz Stability Theorem

For every bounded height window `0<t<T`, there is a finite union of zero-independent contours
`Gamma_T` and an error `R(lambda,T)->0`, obtained from the CCM finite Euler/Gamma construction, such
that

```text
||(1/2*pi*i) integral_{Gamma_T}
    ((z-H_lambda)^(-1) - R_zeta(z)) dz|| <= R(lambda,T).
```

Then spectral projections converge. Since `H_lambda` is self-adjoint, the limiting spectral divisor is
real.

## Status

E71.4 is not a proof of RH. It identifies the right finite-dimensional measurement for the theorem
E71.3 identified:

```text
nearest-root convergence      -> too noisy;
wide zero-gap Riesz windows   -> too coarse;
micro Riesz contours          -> correct local operator language.
```

The next audit point is whether the zeta case has stable local rank-one contours while the planted
off-line case loses those local locks or keeps a persistent displacement floor. That separates true
convergence from mere root counting.
