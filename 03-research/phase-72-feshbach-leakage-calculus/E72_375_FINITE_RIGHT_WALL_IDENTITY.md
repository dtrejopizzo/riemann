# E72.375 - Finite right-wall identity

## 1. Purpose

E72.374 gives

```text
PAIR-Z_{c,T}(z)
= ArchPolar_{c,T}(z)-PrimeWall_{c,T}(z)
 + 1/(4pi i)Horiz_{c,T}(z),
```

where

```text
PrimeWall_{c,T}(z)
=1/(2pi) sum_{n>=1} Lambda(n)n^(-1/2-c)
  int_{-T}^{T} H_z(c+it)e^(-it log n)dt.
```

This note records the finite identity obtained by cutting the absolutely convergent prime series.

## 2. Right-wall Fourier coefficients

For `c>1/2`, `T>0`, define

```text
I_{c,T}(z;u):=1/(2pi) int_{-T}^{T} H_z(c+it)e^(-itu)dt.        (1)
```

Then

```text
PrimeWall_{c,T}(z)
=sum_{n>=1} Lambda(n)n^(-1/2-c) I_{c,T}(z;log n).              (2)
```

For every finite `N`,

```text
PrimeWall_{c,T}^{<=N}(z)
=sum_{n<=N} Lambda(n)n^(-1/2-c) I_{c,T}(z;log n).              (3)
```

and

```text
PrimeWall_{c,T}(z)-PrimeWall_{c,T}^{<=N}(z)
=sum_{n>N} Lambda(n)n^(-1/2-c) I_{c,T}(z;log n).               (4)
```

This is an identity, not an estimate.

## 3. Explicit tail certificate

Let

```text
M_{c,T}(z):=1/(2pi) int_{-T}^{T}|H_z(c+it)|dt.
```

Then from (4),

```text
|PrimeWall_{c,T}(z)-PrimeWall_{c,T}^{<=N}(z)|
<=M_{c,T}(z) R_c(N),                                    (5)
```

where

```text
R_c(N):=sum_{n>N} Lambda(n)n^(-1/2-c).                  (6)
```

Since `1/2+c>1`, `R_c(N)->0`.  No zero information is used.

For explicit computation one may bound `R_c(N)` by a dyadic PNT-free crude estimate using
`Lambda(n)<=log n`:

```text
R_c(N)
<= sum_{n>N} (log n)n^(-1/2-c)
<= int_N^infty (log(t+1))(t-1)^(-1/2-c)dt,              (7)
```

valid for `N>=2`.  This bound is weak but unconditional and sufficient to make the finite identity
auditable.

## 4. Full finite compressed formula

Combining E72.374 with (3)--(5), for all `N>=2`,

```text
PAIR-Z_{c,T}(z)
= ArchPolar_{c,T}(z)
 - PrimeWall_{c,T}^{<=N}(z)
 + Horiz_{c,T}(z)/(4pi i)
 + ErrPrime_{c,T}^{>N}(z),                              (8)
```

with

```text
|ErrPrime_{c,T}^{>N}(z)| <= M_{c,T}(z)R_c(N).           (9)
```

Every term in (8) is finite and explicitly computable from:

```text
H_z(c+it),
A_c(t),
Lambda(n) for n<=N,
the four sides of the finite rectangle.
```

## 5. Finite identity for the transformed packet equation

Substituting (8) into E72.319/E72.321 gives

```text
Lambda_L G_x(z)
= ArchPolar_{c,T}(z)
 - PrimeWall_{c,T}^{<=N}(z)
 + Horiz_{c,T}(z)/(4pi i)
 + ErrPrime_{c,T}^{>N}(z)
 - Lcal(B_z^tail).                                     (10)
```

Thus the transformed route is reduced to proving the uniform polynomial bound for the right side of
(10).  The proof can no longer hide behind zero positions: the only arithmetic input is the finite
von Mangoldt list up to `N` plus the explicit tail (9).

## 6. Status

```text
proved: finite right-wall identity (8);
proved: explicit prime-tail certificate (9);
reduced: CTRACE to a finite Fourier-coefficient identity plus horizontal and finite-mesh tails;
open: prove uniform polynomial bounds for the finite identity as L,T,N vary in the Phase 72 order of limits.
```
