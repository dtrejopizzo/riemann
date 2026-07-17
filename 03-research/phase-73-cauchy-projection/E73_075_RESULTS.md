# E73.075 results - exact pair divisibility verifier

## 1. Purpose

E73.075 proves the exact identity

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

The verifier checks the identity in the finite harness.

## 2. Output

```text
E73.075 exact pair divisibility verifier
Checks Pair_z^infty(w)=A H0(w)+B H0(-w).
 lam     L   zIm    wIm       absErr      relErr
  16   5.545  14.13    3.70   6.059e-16   7.561e-15
  16   5.545  14.13   14.13   1.313e-15   1.356e-01
  16   5.545  14.13   21.02   1.233e-15   1.577e+00
  20   5.991  14.13    3.70   7.836e-15   9.300e-13
  20   5.991  17.30   28.40   8.898e-16   1.238e-09
  24   6.356  14.13    3.70   4.030e-16   1.040e-14
  24   6.356  17.30   28.40   1.444e-16   1.626e-12
```

The relative error is large only when both sides are at the `1e-15` scale.  The absolute error is the
relevant check.

## 3. Result

The identity is verified at absolute error

```text
<= 2e-14
```

in the tested cases.

## 4. Status

```text
proved algebraically: complete-mesh Pair_z^infty is divisible by H_0(w),H_0(-w);
verified numerically: finite harness matches the identity to roundoff;
open: prove the analogous bound for the finite mesh tail Pair_z^tail.
```
