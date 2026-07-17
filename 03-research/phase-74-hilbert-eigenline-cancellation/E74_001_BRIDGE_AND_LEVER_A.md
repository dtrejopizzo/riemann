# E74.1-E74.3 - Bridge identity and Lever A first audit

Date: 2026-07-16.

## Purpose

Phase 74 starts from the exact Hilbert product rule

```text
HPR(r,eta)=
  sum_j eta_j r_j U^even_j
+ sum_j W^odd_j r_j (A eta)_j
+ sum_j W^odd_j eta_j (A r)_j.
```

The proposed lever is that the Cauchy row `r` should be a quasi-eigenvector of
the mesh Hilbert matrix `A`.  This note performs the first audit:

1. re-check the algebraic bridge `HPR = diagonal + commutator`;
2. measure the finite-mesh relation `A r = c r + rho`;
3. test whether substituting this relation actually collapses the endpoint to a
   one-sided symbol.

## Exact bridge

With

```text
A_jb = 1/(2 i pi (n_b-n_j)), j != b,       A_jj=0,
M=M_{W^odd},
```

one has, bilinearly,

```text
sum_j W_j r_j (A eta)_j + sum_j W_j eta_j (A r)_j
= r^T M A eta - r^T A M eta
= r^T [M,A] eta.
```

The off-diagonal entries of `[M,A]` are

```text
([M,A])_jb = (W_j-W_b)/(2 i pi (n_b-n_j)).
```

This is exactly the off-diagonal closed spectral distribution from E73.304 and
the Hilbert product rule from E73.305.  The probe re-verifies the bridge to
roundoff.

## Lever A audit

The finite mesh is not the continuous Hilbert transform.  Therefore the first
quantity to measure is not the formal constant `+-i/2`, but the actual
bilinear projection

```text
c_bil = (sum_j r_j (A r)_j)/(sum_j r_j^2),
rho   = A r - c_bil r.
```

This is the coefficient relevant to the bilinear HPR pairing.  The probe also
prints the Hermitian least-squares coefficient as a diagnostic.

## One-sided substitution

Substituting `A r=c r+rho` controls only the third HPR term:

```text
sum_j W_j eta_j (A r)_j
= c sum_j W_j eta_j r_j + sum_j W_j eta_j rho_j.
```

It does **not** remove the second term

```text
sum_j W_j r_j (A eta)_j.
```

Thus Lever A alone proves a one-sided collapse only if this remaining term is
already negligible or is killed by an additional eigenline identity.  The probe
therefore reports:

```text
total        = full HPR scalar;
oneSide      = diagonal + c <r,W eta> + <rho,W eta>;
oneSideErr   = total - oneSide = r^T M A eta, up to roundoff.
```

## Status

```text
proved: bridge identity HPR = diagonal + commutator;
audited: finite-mesh quasi-eigenvector projection of Cauchy rows;
warning: Lever A alone does not algebraically collapse HPR-DIV;
open: find a second relation controlling r^T M_W A eta or prove a symmetric
      eigenline/Hilbert relation for eta.
```
