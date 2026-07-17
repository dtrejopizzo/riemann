# E72.3 -- Reduced Feshbach leakage: the correct norm

**Date:** 2026-07-08.
**Role:** strengthen E72.1 by replacing the too-strong raw leakage estimate with the reduced-resolvent
leakage estimate that actually controls the ground vector.

## 0. Correction to E72.1

E72.1 used the sufficient condition

```text
||b_x|| / g_x -> 0,
```

where

```text
b_x = Q_x R_x k_x,
C_x = Q_x(H_x - mu_x^0 - a_x)Q_x >= c g_x Q_x.
```

That condition is clean, but still too strong. It penalizes leakage into very high complement modes even
when that leakage is killed by the inverse complement operator. Eigenvector perturbation does not see
`b_x` directly. It sees

```text
C_x^{-1} b_x.
```

This matters because the old Sonin/prolate failures repeatedly showed high-mode contamination in full
Rayleigh or full operator norms. Feshbach does not ask whether high modes are excited; it asks whether
the excited high modes feed back into the ground line after the complement is inverted.

So the right Phase 72 target is:

```text
reduced leakage, not raw leakage.
```

## 1. Abstract theorem

Let `H = C k plus QH`, `||k||=1`, and let a self-adjoint operator `T` have block form

```text
T =
  [ 0    b^* ]
  [ b     C  ],
```

with

```text
C >= g Q,        g>0.
```

Define the reduced leakage vector

```text
eta := C^{-1} b
```

and the Feshbach energy drop

```text
s := <b, C^{-1} b> = <eta, C eta> >= 0.
```

### Theorem 72.3 -- reduced leakage controls the ground vector

Assume

```text
||C^{-1}b|| -> 0.
```

Then `T` has a unique eigenvalue `delta<=0` at the bottom of the spectrum. If `b!=0`, then `delta<0`;
if `b=0`, then `delta=0` and the eigenvector is exactly `k`. For `b!=0`, the corresponding normalized
eigenvector can be written as

```text
theta = alpha k + u,       alpha>0,
```

with

```text
u = -alpha (C-delta)^(-1)b
```

and

```text
||theta-k|| <= 2 ||C^{-1}b|| + o(||C^{-1}b||).
```

Moreover

```text
-s <= delta <= 0,
```

and, if additionally `s/g -> 0`, the eigenvalue lies in the original E72.1 spectral island near `0`.

### Proof

For `delta<0`, the complement operator `C-delta` is invertible and

```text
||(C-delta)^(-1)|| <= ||C^{-1}|| <= 1/g.
```

The eigenvalue equation for `theta=alpha k+u` is equivalent to

```text
b^*u = delta alpha,
alpha b + C u = delta u.
```

If `alpha != 0`, the second equation gives

```text
u = -alpha (C-delta)^(-1)b,
```

and substitution in the first equation gives the scalar Feshbach equation

```text
delta = - b^*(C-delta)^(-1)b.          (F)
```

For `delta in [-s,0]`,

```text
0 <= b^*(C-delta)^(-1)b <= b^*C^{-1}b = s,
```

so the right side of (F) maps `[-s,0]` into itself. Its derivative has absolute value

```text
b^*(C-delta)^(-2)b <= ||C^{-1}b||^2.
```

For large `x`, this is `<1`; hence (F) has a unique fixed point `delta in [-s,0]`.

The complement component satisfies

```text
||u|| <= |alpha| ||(C-delta)^(-1)b|| <= |alpha| ||C^{-1}b||.
```

After normalization, `alpha=(1+||u||^2)^(-1/2)`, so `alpha -> 1` and

```text
||theta-k|| <= |1-alpha| + ||u|| <= 2||C^{-1}b|| + o(||C^{-1}b||).
```

If `b=0`, the conclusion is immediate: `delta=0`, `theta=k`, and the complement is bounded below by
`g`. If `b!=0`, the uniqueness of the negative eigenvalue follows from the Schur complement/inertia
formula: since
`C>0`, the negative index of `T` equals the negative index of

```text
0 - b^*C^{-1}b = -s,
```

which is one. This proves the theorem. `QED`

## 2. Why this is strictly better than E72.1

E72.1 follows immediately from Theorem 72.3 because

```text
||C^{-1}b|| <= ||b||/g.
```

But the converse is false. The reduced condition allows `||b||` to be large if the leakage lies in high
complement modes.

In complement eigen-coordinates

```text
C e_j = lambda_j e_j,      lambda_j >= g,
b = sum_j b_j e_j,
```

the raw E72.1 condition is

```text
sum_j |b_j|^2 = o(g^2).
```

The reduced E72.3 condition is instead

```text
sum_j |b_j|^2 / lambda_j^2 -> 0.
```

This is exactly the Feshbach/Schur correction that Phase 60 was missing when full Rayleigh norms were
contaminated by high modes.

## 3. The new arithmetic target

The CCM route no longer needs to prove

```text
||Q_x(H_x-H_x^0)k_x|| = o(g_x).
```

It is enough to prove

```text
||C_x^{-1} Q_x(H_x-H_x^0)k_x|| -> 0,
```

where

```text
C_x = Q_x(H_x - mu_x^0 - a_x)Q_x.
```

Equivalently, one may prove a projected coboundary identity:

```text
Q_x(H_x-H_x^0)k_x = C_x u_x + r_x,
```

with

```text
||u_x|| -> 0,
||C_x^{-1}r_x|| -> 0.
```

This is the right place for the Sonin/Feshbach integration-by-parts formula. It may produce a large
raw vector `C_x u_x`; that is harmless if `u_x` itself is small.

## 4. What the desired identity should look like

The previous target in E72.1 was

```text
<e_{x,j}, R_x k_x> = Boundary_{x,j} + Tail_{x,j},
sum_j |Tail_{x,j}|^2 = o(g_x^2).
```

The corrected target is weighted by the complement inverse:

```text
<e_{x,j}, R_x k_x>
  = lambda_{x,j} u_{x,j} + r_{x,j},
```

with

```text
sum_j |u_{x,j}|^2 -> 0,
sum_j |r_{x,j}|^2/lambda_{x,j}^2 -> 0.
```

Thus the proof may tolerate large high-frequency boundary terms, provided they are exact `C_x`-coboundary
terms with small primitive `u_x`.

This avoids the old Sonin failures:

- no pointwise localization of Christoffel kernels;
- no false `1/log gamma` scale;
- no absolute prime ceiling;
- no additive Green-resolvent claim;
- no global strong-resolvent convergence.

## 5. Falsifier

For Davenport--Heilbronn or a planted off-line deformation, the same reduced leakage should fail in one
of two ways:

```text
liminf ||C_x^{-1}Q_x(H_x-H_x^0)k_x|| > 0,
```

or

```text
C_x >= c g_x Q_x
```

fails after pole-relative shorting.

This is stronger and cleaner than the raw leakage falsifier, because it ignores harmless high-mode
excitation and measures only the part capable of moving the finite CCM ground vector.

## 6. Status

```text
proved:   reduced Feshbach leakage theorem;
new:      the correct arithmetic norm is ||C_x^{-1}Q_x R_x k_x||, not ||Q_x R_x k_x||/g_x;
open:     prove the projected coboundary identity for actual CCM/Sonin data.
```

The next mathematical object to build is therefore not a norm bound on `R_x`, and not a local kernel
asymptotic. It is a **pole-relative Feshbach coboundary formula**

```text
Q_x(H_x-H_x^0)k_x = C_x u_x + r_x
```

with `u_x -> 0` and `C_x^{-1}r_x -> 0`.
