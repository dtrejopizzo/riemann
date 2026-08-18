# Phase 94 closure - Inverse-free cofactor anchor

## 1. Closed mathematics

The global bordered determinant has the exact cofactor form

```text
N(z)=det M-h_z^Tadj(M)b.                              (1.1)
```

For the raw boundary column, the displacement law gives

```text
Delta A=-(2/L)(C U+T V),                             (1.2)
```

where

```text
Delta=det M,
y=adj(M)b,
C=Delta-1^Ty,
T=s^Ty-Delta S_b,
A=(D-d_bI)y,
U=adj(M)s,
V=adj(M)1.                                           (1.3)
```

Thus the projective numerator is

```text
P(z)
 =Delta C+(2/L)[C U_z+T V_z],                        (1.4)
```

and its logarithmic derivative is a coupled quotient of cofactor Cauchy
transforms.  No inner inverse remains.

## 2. Exact remaining scalar

After restoring the explicit mesh factor, the sole direct defect is

```text
D_(L,N)(s)
 =partial_s log C_(L,N)(s)-H_L(s).                   (2.1)
```

E94.004 expresses (2.1) entirely through the cofactors in (1.3)--(1.4).

## 3. Decision

The rank-two displacement identity closes the algebraic part of the direct
bordered program, including singular sections.  It does not produce a
termwise Euler identity.  Differentiated cofactor pieces must remain coupled.

## 4. Closure grade

```text
closed:
  global cofactor current;
  inverse-free boundary displacement polynomial;
  polynomial two-generator numerator;
  exact bordered Euler defect;
  inverse-free deformation identity;
  finite certification through relative residuals below 1e-96;

open and transferred:
  COFACTOR-CELL-ANCHOR;
  determinant-level Gamma--Euler cancellation;
  DIRECT-BORDERED-ANCHOR and Omega7.
```
