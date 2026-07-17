# E72.225 - Plus-current spectral phase

## Purpose

E72.224 reduced the high-block odd sign to the aggregated plus-current:

```text
A_j = sum_{n in S_j} A_n^+,
Tr(K_j^3)=8 Re Tr(A_j^3).
```

This probe asks whether the sign is visible as a simple spectral phase of `A_j`.

## Diagnostic

Script:

```text
E72_225_plus_current_spectral_probe.py
```

Output:

```text
E72.225 plus-current spectral phase probe
A=sum plus cells; reports trace powers and leading eigenvalue phases
lam block ReTrA2 ImTrA2 ReTrA3 ImTrA3 ||A||2 ||A||HS topEigAbs topEigArg
 12     0 +3.205311e-01 +7.615466e-18 +1.799732e-02 +2.479883e-18 2.194e-01 5.662e-01 2.194e-01 -0.000
 12     1 +1.169855e-01 -1.750341e-17 -9.452352e-03 +2.941429e-18 2.226e-01 3.420e-01 2.226e-01 +3.142
 16     0 +2.603867e-01 +1.100291e-16 +1.175549e-02 +3.024996e-17 1.997e-01 5.103e-01 1.997e-01 +0.000
 16     1 +1.174954e-01 +7.269331e-17 -9.305587e-03 -2.053862e-17 2.187e-01 3.428e-01 2.187e-01 -3.142
 20     0 +2.304208e-01 +9.754894e-19 +8.960922e-03 -2.049782e-18 1.782e-01 4.800e-01 1.782e-01 -0.000
 20     1 +1.100463e-01 +6.192668e-18 -1.076469e-02 -2.532049e-18 2.243e-01 3.317e-01 2.243e-01 -3.142
 24     0 +2.124248e-01 -1.081728e-17 +7.875274e-03 -1.177092e-18 1.745e-01 4.609e-01 1.745e-01 -0.000
 24     1 +1.166779e-01 -3.438594e-18 -1.568847e-02 +2.311460e-18 2.542e-01 3.416e-01 2.542e-01 +3.142
 28     0 +1.834644e-01 +1.728339e-17 +8.818289e-03 -1.988300e-18 1.729e-01 4.283e-01 1.729e-01 -0.000
 28     1 +1.089138e-01 -6.982646e-18 -1.331685e-02 +1.190719e-18 2.409e-01 3.300e-01 2.409e-01 +3.142
 32     0 +1.682350e-01 +7.378753e-18 +2.329573e-03 +5.521561e-20 1.500e-01 4.102e-01 1.500e-01 -3.142
 32     1 +6.442615e-02 -4.730512e-19 -2.110545e-03 -2.891888e-19 1.368e-01 2.538e-01 1.368e-01 -3.142
```

## Reading

The robust sign is:

```text
block 0: Re Tr(A_0^3)>0,
block 1: Re Tr(A_1^3)<0.
```

For the high block, the leading spectral phase lies on the negative real axis in every tested stable
window. This is the first usable explanation of the odd sign: it is a spectral skew toward negative
eigenvalues in the aggregated high plus-current.

The low block at `lambda=32` warns against using only the leading eigenvalue phase. The sign of
`Tr(A_j^3)` is a full third spectral moment statement, not a one-eigenvalue statement.

## Consequence

Replace the complex phase target by the real moment target:

```text
HOC:  Tr(A_1^3) <= 0.
```

The next question is whether `A_j` is actually Hermitian and whether `HOC` is a Loewner-order
statement or a genuine third-moment domination.
