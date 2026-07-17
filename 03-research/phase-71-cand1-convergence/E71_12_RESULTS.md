# E71.12 -- finite-section persistence filter results

**Date:** 2026-07-07.
**Script:** `E71_12_persistence_filter.py`.

## Zeta true

Clustering used only CCM roots across finite sections. Known zeta zeros were used only afterward as an
audit label.

With `lambda=5`, `N in {14,18,20,24,30,36,40}`, radius `1e-3`, the persistent clusters were:

```text
 center        count spread       Ns                  nearest zeta zero
 14.134725      6  5.453e-13  [14,18,20,24,30,40]  gamma1 err=1.417e-07
 21.022040      6  1.315e-13  [14,18,20,24,36,40]  gamma2 err=3.612e-07
 25.010858      6  1.794e-12  [14,18,20,24,36,40]  gamma3 err=4.199e-07
 30.424876      5  1.105e-12  [18,20,30,36,40]     gamma4 err=1.259e-07
 32.935062      5  1.430e-11  [18,24,30,36,40]     gamma5 err=4.123e-07
 37.586178      5  2.180e-09  [20,24,30,36,40]     gamma6 err=1.593e-07
 40.918719      4  3.638e-12  [24,30,36,40]        gamma7 err=1.215e-08
 43.327073      4  5.371e-11  [24,30,36,40]        gamma8 err=2.809e-07
 48.005151      3  2.132e-13  [30,36,40]           gamma9 err=1.188e-07
 49.773832      3  1.798e-12  [30,36,40]           gamma10 err=4.777e-07
```

There is one additional persistent cluster at `52.970321`, outside the listed ten-zero audit range.

## Planted off-line control

For the planted off-line perturbation `(g0=25,b=0.30,c=5.0)`, the same clustering finds essentially
one persistent cluster:

```text
 center        count spread       Ns                  nearest zeta zero
 25.001074      6  8.621e-05  [18,20,24,30,36,40]  gamma3 err=9.784e-03
```

The rest of the spectrum drifts with `N`.

## Reading

Persistence is the first zero-independent diagnostic that cleanly separates physical-looking roots
from finite-section background roots.

For true zeta, persistent clusters reconstruct the low zeta divisor.

For the planted control, persistence does **not** reconstruct the true zeta divisor; it extracts a
stable displaced cluster near the planted height and loses the coherent full sequence. This is exactly
what an RH detector should do.

## Consequence

The relative determinant should not be built by static subtraction. It should be built from the stable
finite-section spectral subspace:

```text
D_N^{phys}(t) = product over persistent/Riesz-stable roots.
```

As a proof object this cannot be an algorithmic post-selection. It must arise from a canonical compact
projection or Fredholm decomposition of the CCM m-function.

This becomes the next target:

```text
construct the stable Riesz/Fredholm projection intrinsically.
```
