# E72.226 - Hermitian cubic moment

## Purpose

E72.225 suggested a real spectral mechanism for the high-block odd sign. This probe checks whether the
aggregated plus-current has a nontrivial skew-Hermitian part or whether the problem is already a real
symmetric matrix inequality.

For one block:

```text
A_j = sum_{n in S_j} A_n^+,
H_j=(A_j+A_j^*)/2,
S_j=(A_j-A_j^*)/(2i).
```

## Diagnostic

Script:

```text
E72_226_plus_current_hermitian_probe.py
```

Output:

```text
E72.226 plus-current Hermitian/normality probe
A=sum plus cells; H=(A+A*)/2, S=(A-A*)/(2i)
lam block ReTrA3 TrH3 ratio minH maxH posH negH ||S||F/||H||F ||[A,A*]||F/||A||F^2
 12     0 +1.799732e-02 +1.799732e-02 +1.000 -1.966e-01 +2.194e-01   13   19 5.132e-16 2.592e-16
 12     1 -9.452352e-03 -9.452352e-03 +1.000 -2.226e-01 +1.197e-01   13   14 5.690e-16 4.450e-16
 16     0 +1.175549e-02 +1.175549e-02 +1.000 -1.765e-01 +1.997e-01   15   25 2.529e-15 1.849e-15
 16     1 -9.305587e-03 -9.305587e-03 +1.000 -2.187e-01 +1.093e-01   17   18 3.112e-15 3.592e-15
 20     0 +8.960922e-03 +8.960922e-03 +1.000 -1.696e-01 +1.782e-01   20   28 6.095e-16 2.677e-16
 20     1 -1.076469e-02 -1.076469e-02 +1.000 -2.243e-01 +9.118e-02   21   21 6.552e-16 4.866e-16
 24     0 +7.875274e-03 +7.875274e-03 +1.000 -1.595e-01 +1.745e-01   21   35 5.971e-16 2.328e-16
 24     1 -1.568847e-02 -1.568847e-02 +1.000 -2.542e-01 +9.623e-02   24   24 5.740e-16 3.334e-16
 28     0 +8.818289e-03 +8.818289e-03 +1.000 -1.142e-01 +1.729e-01   25   39 1.116e-15 4.429e-16
 28     1 -1.331685e-02 -1.331685e-02 +1.000 -2.409e-01 +9.368e-02   26   27 1.734e-15 8.525e-16
 32     0 +2.329573e-03 +2.329573e-03 +1.000 -1.500e-01 +1.122e-01   28   44 6.492e-16 2.249e-16
 32     1 -2.110545e-03 -2.110545e-03 +1.000 -1.368e-01 +8.375e-02   29   30 7.806e-16 3.524e-16
```

## Structural identity

The skew-Hermitian part is zero to roundoff:

```text
||S_j||_F/||H_j||_F = O(10^-15),
||[A_j,A_j^*]||_F/||A_j||_F^2 = O(10^-15).
```

This is not caused by an explicit symmetrization in `plus_sum`. The raw one-sided kernel `U_y` is not
Hermitian, but the compressed relative cell

```text
C_model^{-1/2} B^T U_y B C_model^{-1/2}
```

is Hermitian to roundoff on the tested windows. The next exact algebraic sublemma is therefore:

```text
(C_model^{-1/2} B^T U_y B C_model^{-1/2})^*
= C_model^{-1/2} B^T U_y B C_model^{-1/2}.        (CUH)
```

This is a structural identity of the even compressed Green channel, not a post-hoc replacement of
`A_j` by `(A_j+A_j^*)/2`.

Thus E72.224 becomes the exact real identity:

```text
K_j = A_j + A_j^* = 2A_j,
Tr(K_j^3)=8 Tr(A_j^3).
```

## No Loewner shortcut

The high block is not negative semidefinite:

```text
min eig(A_1)<0<max eig(A_1).
```

So the proof cannot be:

```text
A_1 <= 0.
```

The correct finite statement is a third-moment domination:

```text
sum_{\lambda_r(A_1)>0} lambda_r(A_1)^3
<=
sum_{\lambda_r(A_1)<0} |lambda_r(A_1)|^3.          (HOC3)
```

Equivalently:

```text
Tr(A_1^3) <= 0.
```

## New exact target

The high-block odd channel is now reduced to a real Hermitian matrix moment inequality:

```text
HOC3(lambda):
  Tr( (sum_{0.60L < log n <= L} A_n^+)^3 ) <= 0.
```

No zero information is used in its formulation. It is a finite algebraic inequality in the model
Green-whitened prime-power cells.

The next proof attempt should expand `Tr(A_1^3)` in the displacement variables

```text
u_n = log n / L
```

and prove that the high-window kernel has negative cubic moment on `u_n in (0.60,1]`, with the
von Mangoldt weights entering only through the positive coefficients `(Lambda(n)/sqrt(n))`.
