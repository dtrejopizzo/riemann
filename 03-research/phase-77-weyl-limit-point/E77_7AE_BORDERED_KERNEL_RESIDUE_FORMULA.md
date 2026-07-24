# E77.7ae - Bordered kernel residue formula

**Run:** 2026-07-18.

## 1. Purpose

E77.7ad isolated the correct singular finite-section target:

```text
KERNEL-ANCHOR-RESIDUE-FORMULA.
```

This note proves it exactly for the fixed finite section at its moving
spectral point `mu`.

## 2. Setup

Let

```text
A = H_inner - mu I
```

be the shifted inner block of one finite section, where `mu` is the lowest
eigenvalue of the full section.  Let

```text
M(z0) =
[ A      g ]
[ r(z0)  c0 ]
```

be the shifted bordered matrix from E77.7ac.

Assume the zero eigenvalue of `A` is simple, and let `v0` be a normalized
kernel vector:

```text
Av0 = 0,
v0^* v0 = 1.                                          (AE-1)
```

Write the remaining eigenvalues of `A` as `lambda_1,...,lambda_{m-1}` and
define

```text
p'_A(0) = product_{j=1}^{m-1} (-lambda_j).            (AE-2)
```

## 3. Determinant expansion

Expand `det M(z0)` along the last row / column, equivalently by the Schur
complement formula for a bordered matrix:

```text
det M(z0) = c0 det A - r(z0) adj(A) g.                (AE-3)
```

Since `A` has a zero eigenvalue,

```text
det A = 0,                                            (AE-4)
```

so only the adjugate term remains:

```text
det M(z0) = - r(z0) adj(A) g.                         (AE-5)
```

## 4. Adjugate at a simple zero mode

Because `A` is Hermitian and `0` is a simple eigenvalue, its spectral
decomposition is

```text
A = sum_{j=1}^{m-1} lambda_j v_j v_j^*,
```

with `v0` spanning the zero eigenspace.  Therefore

```text
adj(A) = p'_A(0) v0 v0^*.                             (AE-6)
```

Indeed, in a diagonal basis the adjugate is

```text
diag(p'_A(0), 0, ..., 0),
```

and conjugating back by the unitary eigenbasis replaces the first diagonal
projector by `v0 v0^*`.

Substituting `(AE-6)` into `(AE-5)` gives the exact factorization

```text
det M(z0)
= -p'_A(0) r(z0) v0 v0^* g
= -p'_A(0) (v0^* g)(r(z0)v0).                         (AE-7)
```

This is exactly the residue-level formula predicted in E77.7ad.

## 5. Consequence

Equation `(AE-7)` proves that tiny bordered determinants in the singular
finite sections come from two independent factors:

```text
1. the characteristic derivative p'_A(0), carrying the collapse of the
   almost-singular inner block;
2. the directional kernel-anchor scalar (v0^* g)(r(z0)v0).
```

So determinant smallness and kernel blindness are different phenomena.

In particular:

```text
(v0^* g)(r(z0)v0) != 0
=> det M(z0) != 0                                     (AE-8)
```

and, by E77.7ab,

```text
(v0^* g)(r(z0)v0) != 0
=> FIXED-SECTION-KERNEL-ANCHOR-THEOREM.               (AE-9)
```

## 6. Relation to the singular projective bridge

Combining E77.7ab, E77.7z, and `(AE-7)` gives the honest chain

```text
KERNEL-DOUBLE-COUPLING
=> FIXED-SECTION-KERNEL-ANCHOR-THEOREM
=> INTRINSIC-SCHUR-ETA-LIMIT at fixed section
=> singular-section clause for PROJECTIVE-MU-TRANSFER.   (AE-10)
```

The stronger target from E77.7ac,

```text
uniform bordered-anchor invertibility,
```

is not needed and was rightly autopsied in E77.7ad.

## 7. Compatibility with the probe

The audit E77.7ad computed

```text
det M(z0) / (p'_A(0) scalar),
scalar = (v0^* g)(r(z0)v0),
```

and found it numerically close to `-1` in both builds by the end of the
tested ladder:

```text
zeta N=14:  -0.98958 - 0.03662 i,
plant N=14: -1.00561 + 0.00076 i.
```

This is exactly the finite-precision shadow of `(AE-7)`.

## 8. Status

```text
proved:    exact bordered determinant factorization
           det M(z0) = -p'_A(0) (v0^* g)(r(z0)v0)
           for simple zero mode of the finite shifted inner block;
proved:    determinant collapse can occur without loss of kernel-anchor
           coupling;
closed:    KERNEL-ANCHOR-RESIDUE-FORMULA;
next:      lift the fixed-section kernel-anchor nonvanishing from audit
           to theorem, or isolate the exact remaining obstruction if the
           finite proof still needs one more border identity.
```
