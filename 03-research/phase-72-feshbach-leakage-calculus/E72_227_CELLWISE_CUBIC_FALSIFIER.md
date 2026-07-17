# E72.227 - Cellwise cubic falsifier

## Purpose

E72.226 reduced the high-block odd channel to:

```text
Tr(A_1^3) <= 0,
A_1=sum_{n in S_1} A_n.
```

This note tests whether the sign is already true cell by cell.

Write the Hermitian compressed one-sided cell before the von Mangoldt sign as `M_n`, so that:

```text
A_n = - (Lambda(n)/sqrt(n)) M_n.
```

For a high cell, `Tr(A_n^3)<=0` is equivalent to `Tr(M_n^3)>=0`.

## Diagnostic

Script:

```text
E72_227_cellwise_cubic_probe.py
```

Output:

```text
E72.227 cellwise cubic sign probe
M_n=relative compressed U_logn cell before the -Lambda(n)/sqrt(n) sign
For A_n=-beta M_n, high block wants Tr(A_n^3)<=0, i.e. Tr(M_n^3)>=0
lam block cells minTrM3 maxTrM3 badCells sumCellTrA3 sumAggTrA3 crossFrac worstN
 12     0    12 -5.388e-04 +1.590e-04        2 +2.956923e-04 +1.799732e-02 +9.836e-01 5
 12     1    35 -1.188e-04 +9.253e-05       21 +1.443829e-04 -9.452352e-03 -1.015e+00 23
 16     0    15 -2.165e-04 +8.327e-06        1 +1.960173e-04 +1.175549e-02 +9.833e-01 16
 16     1    55 -3.210e-05 +2.876e-05       33 +5.575514e-05 -9.305587e-03 -1.006e+00 31
 20     0    18 -1.108e-04 +9.023e-06        2 +1.065865e-04 +8.960922e-03 +9.881e-01 29
 20     1    79 -1.251e-05 +1.116e-05       39 +3.294641e-06 -1.076469e-02 -1.000e+00 41
 24     0    21 -8.741e-05 +2.275e-05        3 +4.777571e-05 +7.875274e-03 +9.939e-01 2
 24     1   105 -8.519e-06 +1.223e-05       59 +9.951158e-06 -1.568847e-02 -1.001e+00 61
 28     0    24 -5.093e-05 +1.477e-05        9 +3.799609e-05 +8.818289e-03 +9.957e-01 11
 28     1   136 -7.442e-06 +5.571e-06       74 +7.203894e-06 -1.331685e-02 -1.001e+00 61
 32     0    27 -2.151e-05 +8.912e-06       12 +1.071821e-05 +2.329573e-03 +9.954e-01 2
 32     1   171 -3.476e-06 +2.451e-06       94 +7.824178e-07 -2.110545e-03 -1.000e+00 271
```

## Reading

The cellwise route fails.

The sum of individual cubic traces is tiny and often has the wrong sign for the high block:

```text
sum_n Tr(A_n^3) > 0,
Tr((sum_n A_n)^3) < 0.
```

The useful sign comes almost entirely from cross terms:

```text
Tr((sum_n A_n)^3) - sum_n Tr(A_n^3).
```

For the high block, `crossFrac` is essentially `-1`. This means the proof of HOC3 cannot be a local
cell positivity theorem. It must be a coherent triple-kernel theorem.

## Consequence

The correct kernel is:

```text
T(u,v,w)=Tr(M_u M_v M_w).
```

HOC3 is equivalent to:

```text
sum_{n_a,n_b,n_c in S_1}
  beta_a beta_b beta_c T(u_a,u_b,u_c) >= 0,

beta_n = Lambda(n)/sqrt(n),  u_n=log n/L.
```

This is a signed coherent average of `T`, not a pointwise sign statement.
