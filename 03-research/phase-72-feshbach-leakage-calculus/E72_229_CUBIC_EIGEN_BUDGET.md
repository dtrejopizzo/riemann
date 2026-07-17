# E72.229 - Cubic eigen-budget

## Purpose

E72.228 shows that HOC3 is an averaged triple-kernel positivity theorem, not pointwise positivity. This
probe measures the same statement spectrally:

```text
Tr(A_1^3)=sum_r lambda_r(A_1)^3 <= 0.
```

Equivalently:

```text
sum_{lambda_r>0} lambda_r^3 <= sum_{lambda_r<0} |lambda_r|^3.
```

## Diagnostic

Script:

```text
E72_229_cubic_eigen_budget_probe.py
```

Output:

```text
E72.229 cubic eigen-budget probe
A=sum plus cells; Tr(A^3)=posCube-negCube
lam block posCube negCube margin leadNegFrac leadPosFrac posCt negCt
 12     0 3.287319e-02 1.487586e-02 -1.799732e-02 0.511 0.321    13    19
 12     1 3.366945e-03 1.281930e-02 +9.452352e-03 0.861 0.509    14    14
 16     0 2.219390e-02 1.043841e-02 -1.175549e-02 0.527 0.359    15    25
 16     1 2.904490e-03 1.221008e-02 +9.305587e-03 0.856 0.449    18    18
 20     0 1.730710e-02 8.346174e-03 -8.960922e-03 0.584 0.327    20    28
 20     1 1.947962e-03 1.271266e-02 +1.076469e-02 0.888 0.389    21    21
 24     0 1.484391e-02 6.968633e-03 -7.875274e-03 0.582 0.358    21    35
 24     1 1.797834e-03 1.748630e-02 +1.568847e-02 0.940 0.496    24    24
 28     0 1.258414e-02 3.765855e-03 -8.818289e-03 0.396 0.411    25    39
 28     1 1.626326e-03 1.494318e-02 +1.331685e-02 0.936 0.506    27    27
 32     0 7.735221e-03 5.405649e-03 -2.329573e-03 0.625 0.183    28    44
 32     1 1.229703e-03 3.340248e-03 +2.110545e-03 0.767 0.478    30    31
```

Here:

```text
margin = negCube - posCube = -Tr(A^3).
```

## Reading

For the high block:

```text
negCube > posCube
```

in every tested stable window. The margin is the desired HOC3 sign.

The negative side is mostly carried by the leading negative eigenvalue:

```text
leadNegFrac ~ 0.77 to 0.94.
```

Thus HOC3 is plausibly a one-mode edge dominance plus a Schatten-3 tail estimate:

```text
|lambda_min(A_1)|^3
  - sum_{r>=2, lambda_r<0}|lambda_r|^3
  >= sum_{lambda_r>0} lambda_r^3
```

or, more usefully,

```text
|lambda_min(A_1)|^3 >= ||(A_1)_+||_{S^3}^3.       (EDGE3)
```

The tested data suggest `EDGE3` may be slightly too strong without using part of the negative tail,
but it gives the right proof architecture.

## New proof target

Prove the high-block cubic sign by min-max:

```text
1. find an explicit test vector e_L with
   -<e_L,A_1 e_L> >= alpha_L;

2. prove a positive-tail Schatten bound
   ||(A_1)_+||_{S^3}^3 <= alpha_L^3 + tail_negative_budget;

3. conclude Tr(A_1^3)<=0.
```

This is the finite Hermitian replacement for the earlier complex phase story.
