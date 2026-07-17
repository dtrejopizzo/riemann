# E72.374 - Right-wall trace compression

## 1. Purpose

E72.373 writes the paired zero pressure as

```text
PAIR-Z_R(z)=1/(4pi i) int_{Gamma_R} H_z(w) Z'(w)/Z(w) dw,
```

where `Gamma_R` is symmetric under `w -> -w`, `Z(w)=xi(1/2+w)` is even, and `H_z(w)` is even.

This note compresses the symmetric contour to the right wall.  On that wall

```text
Re(1/2+w)>1,
```

so the prime current enters through the absolutely convergent Dirichlet series for `zeta'/zeta`.

## 2. Parity

Since

```text
Z(-w)=Z(w),
```

we have

```text
L_Z(w):=Z'(w)/Z(w),       L_Z(-w)=-L_Z(w).              (1)
```

By E72.373,

```text
H_z(-w)=H_z(w).                                        (2)
```

Thus

```text
F_z(w):=H_z(w)L_Z(w)
```

is odd:

```text
F_z(-w)=-F_z(w).                                       (3)
```

## 3. Rectangle compression

Let `Gamma_{c,T}` be the counterclockwise rectangle with vertices

```text
c-iT, c+iT, -c+iT, -c-iT,
```

where `c>1/2` and the boundary avoids zeros of `Z`.  Write the right, top, left, and bottom pieces as
`R_{c,T}`, `Top`, `L_{c,T}`, and `Bot`.

The left side is parametrized downward:

```text
int_{L_{c,T}} F_z(w)dw = int_T^{-T} F_z(-c+it)i dt.
```

Using oddness,

```text
F_z(-c+it)=F_z(-(c-it))=-F_z(c-it).
```

Therefore

```text
int_{L_{c,T}} F_z(w)dw
= int_T^{-T} -F_z(c-it)i dt
= int_{-T}^{T} F_z(c+iu)i du
= int_{R_{c,T}} F_z(w)dw.                              (4)
```

The top and bottom pieces satisfy the same relation after reflection:

```text
int_Top F_z(w)dw + int_Bot F_z(w)dw = Horiz_{c,T}(z),   (5)
```

where `Horiz_{c,T}` is explicit and must be shown small or polynomial in the final contour limit.

Combining (4)--(5),

```text
int_{Gamma_{c,T}} F_z(w)dw
=2 int_{-T}^{T} H_z(c+it)L_Z(c+it)i dt
 + Horiz_{c,T}(z).                                     (6)
```

Consequently,

```text
PAIR-Z_{c,T}(z)
=1/(2pi) int_{-T}^{T} H_z(c+it)L_Z(c+it) dt
 + 1/(4pi i)Horiz_{c,T}(z).                            (7)
```

This is the right-wall compression.

## 4. Explicit right-wall integrand

Put

```text
s=1/2+w.
```

For `Re s>1`,

```text
L_Z(w)
= xi'(s)/xi(s)
= 1/s + 1/(s-1)
   -1/2 log(pi)
   +1/2 psi(s/2)
   + zeta'(s)/zeta(s),                                (8)
```

and

```text
zeta'(s)/zeta(s)
= -sum_{n>=1} Lambda(n)n^{-s}.                         (9)
```

Thus on the right wall `w=c+it`, `c>1/2`,

```text
L_Z(c+it)
= A_c(t) - sum_{n>=1} Lambda(n)n^(-1/2-c-it),          (10)
```

where

```text
A_c(t)
=1/(1/2+c+it)+1/(-1/2+c+it)
 -1/2 log(pi)+1/2 psi((1/2+c+it)/2).                   (11)
```

Substituting (10) into (7) gives the explicit compressed identity

```text
PAIR-Z_{c,T}(z)
= ArchPolar_{c,T}(z)-PrimeWall_{c,T}(z)
 + 1/(4pi i)Horiz_{c,T}(z),                            (12)
```

with

```text
ArchPolar_{c,T}(z)
=1/(2pi) int_{-T}^{T} H_z(c+it)A_c(t)dt,
```

and

```text
PrimeWall_{c,T}(z)
=1/(2pi) sum_{n>=1} Lambda(n)n^(-1/2-c)
  int_{-T}^{T} H_z(c+it)e^(-it log n)dt.               (13)
```

The series and integral may be interchanged for finite `T` because the Dirichlet series is absolutely
convergent on `Re s=1/2+c>1`.

## 5. Finite identity form

For a finite cutoff `N`,

```text
PrimeWall_{c,T}^{<=N}(z)
=1/(2pi) sum_{n<=N} Lambda(n)n^(-1/2-c)
  int_{-T}^{T} H_z(c+it)e^(-it log n)dt.
```

The tail has the explicit bound

```text
|PrimeWall_{c,T}^{>N}(z)|
<= [1/(2pi) int_{-T}^{T}|H_z(c+it)|dt]
   sum_{n>N} Lambda(n)n^(-1/2-c).                      (14)
```

Since `1/2+c>1`, the last sum tends to zero as `N -> infinity`.  Therefore (12) is the requested
finite explicit identity up to:

```text
finite prime cutoff tail,
horizontal contour term,
finite Fourier tail from E72.319.
```

Each of these is now separately explicit.

## 6. Proof status

```text
proved: symmetric contour equals twice the right wall plus horizontal term;
proved: right-wall logarithmic derivative has explicit arch/polar/prime form;
proved: finite prime cutoff identity with explicit absolute tail;
open: prove the polynomial bound for the right-wall finite identity plus horizontal and finite-mesh tails.
```

The important point is that the remaining target is no longer a zero-sum estimate.  It is a right-wall
Fourier transform estimate for the explicit kernel `H_z(c+it)`, with the arithmetic appearing only
through the absolutely convergent prime series on `Re s>1`.
