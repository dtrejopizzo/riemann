# E74.26 - Davenport--Heilbronn nodal falsifier

Date: 2026-07-16.

## Compatible engine

`E74_026_davenport_heilbronn_nodal_falsifier.py` reuses the Phase 60 CCM
engine with:

```text
odd Gamma factor a=3/4,
conductor 5,
exact coefficients of -L'_DH/L_DH,
the same Fourier pole mesh and lowest Weyl eigenvector.
```

It evaluates the normalized finite Cauchy numerator at six on-line DH zeros
and at the shifted off-line node

```text
85.699348 + 0.308517 i.
```

## Result

For `lambda=7`, resolved meshes above height 85.7 give

```text
mu approximately -0.33 to -0.42,
critical nodal values approximately 0.003 to 0.005,
off-line nodal value approximately 0.20.
```

The values are stable when the archimedean quadrature step changes from
`0.05` to `0.025`, and the off-line value remains near `0.20` when the mesh is
expanded from `N=58` to `N=64`.

## Verdict

Davenport--Heilbronn fails the zeta nodal-lock pattern.  In particular, the
off-line node is not hidden by self-adjointness or by the real finite Weyl
divisor.  This independently confirms the planted falsifier: the live
observable is sensitive to RH violation.

The DH critical floor should not be compared numerically with the zeta
roundoff floor as a convergence rate, because the two engines use different
Gamma factors and the DH archimedean term is quadrature-based.  The robust
falsifier is the resolved off-line value and negative ground floor.

