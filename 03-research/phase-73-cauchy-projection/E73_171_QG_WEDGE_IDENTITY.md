# E73.171 - QG wedge identity

Date: 2026-07-14.

## 1. Purpose

E73.170 reduces the current endpoint to the sufficient norm theorem:

```text
QUOT-NORM:
e^(alpha L)||P_Q,L Pi_A|| ||P_Q,L G_K|| <= L^B.
```

The geometric side is:

```text
QPI:
e^(alpha L)||P_Q,L Pi_A|| <= L^B.
```

The spectral side is:

```text
QG:
||P_Q,L G_K|| <= L^B e^(-alpha L).
```

This note rewrites `QG` without an opaque projector.  The result is an exact
finite wedge/determinant identity.

## 2. Stable Cauchy form of the dual vector

Let the natural mesh be

```text
d_m = 2 pi m / L.
```

For a critical node `k=i gamma`,

```text
DD_L(-gamma,d_m)
= [e^(-i d_m L)-e^(i gamma L)]/(-gamma-d_m).
```

Since `e^(-i d_m L)=1` on the natural mesh, the proof-facing form is:

```text
G_L(gamma)
= (1-e^(i gamma L)) sum_m xi_L(m)/(-gamma-d_m).
```

This is the same bilinear convention used in E73.003 and E72.396:

```text
sum_m xi_L(m) DD_L(-gamma,d_m),
```

not the Hermitian `vdot` convention.  Numerically, the direct `DD` formula
can lose relative accuracy when the value is tiny, because `e^(-i d_m L)-1`
is only zero up to floating-point error.  Therefore the stable Cauchy form is
the definition used for certification.

For the first five critical nodes, write:

```text
G_L = (G_L(gamma_1),...,G_L(gamma_5)) in C^5.
```

## 3. The quotient space

E73.167 identifies:

```text
C_L = span of the five cauchy0 critical atoms,
M_L = principal image of the finite rational local action,
I_L = C_L cap M_L,
Q_L = C_L / I_L.
```

In the trusted windows:

```text
dim C_L = 5,
dim I_L = 2,
dim Q_L = 3.
```

Let `U_L` be any `5 x 2` matrix whose columns form a basis of `I_L` in
`cauchy0` coordinates.  Let `P_Q,L` be the orthogonal projector onto
`I_L^\perp` inside `C_L`.

## 4. Wedge identity

For every vector `G in C_L`,

```text
||P_Q,L G||^2
= det Gram(U_L,G) / det Gram(U_L),
```

where

```text
Gram(U_L)   = U_L^* U_L,
Gram(U_L,G) = [U_L G]^* [U_L G].
```

Equivalently,

```text
||P_Q,L G|| = ||u_1 wedge u_2 wedge G|| / ||u_1 wedge u_2||.
```

### Proof

The identity is the standard volume formula for distance to a subspace.
Let `I=span(U_L)` and let `G=G_I+G_Q` be the orthogonal decomposition with
`G_I in I` and `G_Q in I^\perp`.  Replacing the last column `G` by
`G_I+G_Q` does not change the wedge except for the `G_Q` component, because
`u_1 wedge u_2 wedge G_I=0`.  Hence

```text
||u_1 wedge u_2 wedge G||^2
= ||u_1 wedge u_2||^2 ||G_Q||^2.
```

The squared wedge norms are the corresponding Gram determinants.  Since
`G_Q=P_Q,L G`, division by `det Gram(U_L)` gives the formula.

## 5. Finite determinant form of QG

Thus `QG` is equivalent to:

```text
det Gram(U_L,G_L) <= L^(2B) e^(-2 alpha L) det Gram(U_L).
```

This is the current proof-facing scalar statement.  It involves:

1. the two generated intersection directions `I_L` coming from the finite
   CCM/Feshbach rational local action;
2. the stable Cauchy transform of the finite eigenline `xi_L`;
3. only a `3 x 3` Gram determinant over five critical samples.

## 6. Why this is new relative to earlier failures

This does not return to the Phase 72 Green-cycle/RFBD majorant problem.
Those estimates work in the large Feshbach complement and suffered from
majorant, dimension, and mixed-cycle bookkeeping.

Here the obstruction is already quotiented down to:

```text
five critical Cauchy samples modulo two generated local-action directions.
```

The remaining theorem is not positivity of a large operator.  It is a finite
spectral Cauchy determinant smallness statement for the actual finite
CCM/Feshbach eigenline.

## 7. Status

```text
proved:   QG has an exact wedge/determinant form;
verified: determinant formula equals ||P_Q G|| numerically;
open:     prove the determinant smallness uniformly from the finite
          CCM/Feshbach equation.
```
