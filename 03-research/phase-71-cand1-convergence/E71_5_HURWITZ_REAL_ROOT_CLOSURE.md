# E71.5 -- Hurwitz real-root closure theorem for CAND-1

**Date:** 2026-07-07.
**Role:** remove the circular use of pre-known zero centers in E71.4 and state the clean complex
analytic closure theorem.

## Why this is the right upgrade

E71.4 used micro-contours centered at known zeros `gamma_j`. That is fine for diagnostics, but it is
not the final proof language: a proof of RH cannot assume the zero centers it wants to prove are on the
critical line.

The non-circular replacement is not to choose contours around known zeros. It is to prove convergence
of the whole characteristic function/divisor.

## Finite real-rooted approximants

For each CCM finite operator `H_{lambda,N}`, define a normalized characteristic function

```text
Phi_{lambda,N}(z)
```

whose zeros are exactly the finite spectrum of `H_{lambda,N}` in the height variable.

Because `H_{lambda,N}` is self-adjoint, every zero of `Phi_{lambda,N}` is real:

```text
Zeros(Phi_{lambda,N}) subset R.
```

This is the CAND-1 advantage. It is not a positivity theorem about `Xi`; it is finite
self-adjointness.

## Hurwitz closure

### Theorem

Assume there is a cofinal path `(lambda_j,N_j)` such that

```text
Phi_{lambda_j,N_j}(z) -> Xi(z)
```

locally uniformly on `C`, after a nonzero normalization.

Then all zeros of `Xi` are real. Hence RH holds.

### Proof

Let `rho` be a zero of `Xi`. Choose a small disk `D(rho,r)` whose boundary contains no zero of `Xi`.
By local uniform convergence and Hurwitz/Rouche, for all sufficiently large `j`, the function
`Phi_{lambda_j,N_j}` has the same number of zeros in `D(rho,r)` as `Xi`, counted with multiplicity.

But all zeros of `Phi_{lambda_j,N_j}` are real. If `Im rho != 0`, choose `r < |Im rho|/2`. Then
`D(rho,r)` contains no real point, so `Phi_{lambda_j,N_j}` has no zeros in the disk, contradiction.

Therefore `Im rho = 0`. Since `rho` was arbitrary, every zero of `Xi` is real.

## Equivalence to the Riesz language

E71.4's micro-contours are the finite-dimensional shadow of this theorem. A local contour around a
zero is stable exactly when the characteristic functions converge uniformly on that contour.

Thus the clean hierarchy is:

```text
locally uniform characteristic convergence
  => Riesz projection convergence on every zero contour
  => spectral convergence to the zeta divisor
  => RH, because finite CCM spectra are real.
```

## Why this is off MW-1

No Weil positivity is used in the implication above. The proof only uses:

1. finite self-adjointness of `H_{lambda,N}`;
2. local uniform convergence of the normalized characteristic functions to `Xi`;
3. Hurwitz/Rouche.

The entire burden is now the convergence theorem:

```text
Phi_{lambda,N} -> Xi locally uniformly.
```

This is precisely the CAND-1 operator-convergence frontier.

## What remains open

The theorem above is conditional. It does not prove the required convergence.

The remaining work is to construct `Phi_{lambda,N}` canonically from the CCM data and prove local
uniform convergence to `Xi` with estimates obtained from the Euler/Gamma construction, not from known
zero locations.

This is the sharpened CAND-1 closure target:

### CCM-Hurwitz Convergence Theorem

There exists a normalization `c_{lambda,N}` and a cofinal path `(lambda,N(lambda))` such that

```text
c_{lambda,N} Phi_{lambda,N}(z) -> Xi(z)
```

locally uniformly on `C`.

If this theorem is proved, `Omega_7` is closed.

## Diagnostic meaning of E71.2-E71.4

The planted off-line experiment now has a clean interpretation. A planted off-line zero cannot appear
as a non-real finite eigenvalue, because finite spectra are real. Instead it prevents local uniform
convergence: micro-contours around the planted/target divisor fail to stabilize.

So E71.2-E71.4 are not proof, but they are exactly the finite symptoms predicted by the Hurwitz
closure theorem.
