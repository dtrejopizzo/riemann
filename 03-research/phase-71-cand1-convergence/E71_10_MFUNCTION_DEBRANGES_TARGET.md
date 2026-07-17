# E71.10 -- Weyl m-function / de Branges target for the CCM determinant

**Date:** 2026-07-07.
**Role:** correct the determinant target after E71.8-E71.9 and avoid a false matrix-determinant turn.

## The important correction

The finite CCM zeros in Phase 71 are not the eigenvalues of the matrix `QW` itself.

The matrix `QW` is used to produce the ground vector `xi`. The finite spectral roots are the zeros of
the rational Weyl function

```text
m_N(s) = sum_k xi_k/(s-d_k),
d_k = 2*pi*k/L.
```

Equivalently, writing

```text
m_N(s) = P_N(s) / Q_N(s),
Q_N(s) = product_k (s-d_k),
```

the CCM roots are the zeros of the numerator `P_N`.

Therefore the determinant object is not

```text
det(QW - z),
```

and not a naive determinant of the operator pair `(QW_zeta,QW_arch)`. Those determinants live in the
wrong spectral variable.

## Correct object

The correct object is the Weyl/de Branges m-function:

```text
m_N(s) = <(s-D_N)^(-1) 1, xi_N>,
```

where `D_N=diag(d_k)` and `xi_N` is the CCM ground vector.

The numerator `P_N` is a finite real-rooted polynomial when the CCM self-adjoint realization applies.
The de Branges entire function should be built from the pair

```text
E_N(s) = A_N(s) - i B_N(s),
```

whose ratio or phase recovers `m_N`, rather than from an arbitrary spectral product.

This is the right replacement for E71.6-E71.9:

```text
raw sine-comb numerator      -> too much background;
all-root product             -> background roots contaminate;
arch/free spectral quotient  -> wrong background;
Weyl m-function/de Branges   -> correct finite spectral carrier.
```

## Why this avoids the Phase 53 trap

Phase 53 killed:

```text
choose boundary/scattering phase so that the spectrum is zeta.
```

The m-function route is allowed only if `m_N` is computed from finite CCM data:

```text
QW_N -> xi_N -> m_N.
```

No zeta zero locations may be used to choose boundary conditions.

The final theorem must then prove:

```text
normalized de Branges functions E_N converge locally uniformly
to a de Branges/Hermite-Biehler representative of Xi.
```

If the normalization is fitted from `Xi`, this collapses into Phase 53 boundary fitting.

## Candidate convergence statement

The non-circular theorem should be stated at the level of logarithmic derivatives:

```text
m_N(s) - background_N(s)  ->  Xi'(s)/Xi(s)
```

locally uniformly away from the limiting divisor, with residues converging to zero multiplicities.

Equivalently, after integration with a canonical basepoint,

```text
E_N^{rel}(s) -> Xi(s)/Xi(0).
```

This is a de Branges/Hurwitz statement:

1. finite `E_N^{rel}` has real spectral divisor by CCM self-adjointness;
2. local uniform convergence gives the `Xi` divisor;
3. Hurwitz forces the divisor of `Xi` to be real.

## What to test next

Build `P_N` explicitly from the rational function:

```text
P_N(s) = sum_k xi_k product_{l != k}(s-d_l),
```

then compare three normalizations:

1. monic polynomial `P_N/P_N(0)`;
2. de-pole normalized function `sin(sL/2)m_N(s)`;
3. logarithmic derivative `P_N'/P_N - background_N'/background_N`.

E71.6 already tested item 2 and found it fails. E71.8 effectively tested item 1 as a product and
found background roots. Therefore the next nontrivial test is item 3: **log-derivative with a
canonical background subtraction**.

## Status

E71.10 is a correction, not a closure.

It prevents the next false move:

```text
do not take determinants of QW;
take the Weyl m-function / de Branges numerator determined by xi_N.
```

The remaining obstacle is now sharply named:

```text
find the canonical background_N for the CCM Weyl m-function.
```

That is the next mathematical object to construct.
