# E72.382 - Local weight scale audit

## 1. Purpose

E72.381 reduces the local WWR term to

```text
int_0^L |(B_z^M)'(r)|W_{L,delta}(r)dr,
```

where

```text
W_{L,delta}(r)
=sum_{n<=e^L} Lambda(n)n^(-1/2)1_{|r-log n|<=delta}.
```

This note audits the scale of `W_{L,delta}`.  The goal is to avoid hiding an exponential ceiling inside
the local derivative estimate.

## 2. Total mass

Integrating (1) gives the exact identity

```text
int_0^L W_{L,delta}(r)dr
=sum_{n<=e^L} Lambda(n)n^(-1/2)
  |[log n-delta,log n+delta] cap [0,L]|.               (1)
```

Away from the endpoints this is approximately

```text
2delta sum_{n<=e^L} Lambda(n)n^(-1/2).
```

By partial summation and the elementary scale of `psi(x)`,

```text
sum_{n<=e^L} Lambda(n)n^(-1/2) ~ 2e^(L/2).             (2)
```

Thus the natural local mass is

```text
int W_{L,delta} ~ 4delta e^(L/2).                      (3)
```

## 3. Consequence for finite wall height

With the default Dirichlet choice

```text
delta=T^(-1/2),
```

the mass scale is

```text
e^(L/2)/sqrt(T).                                      (4)
```

Therefore a purely positive local estimate cannot be polynomial in `L` unless either:

```text
T >= e^L / L^A
```

for some `A`, or the actual packet derivative contributes additional cancellation/decay near the
prime-weighted region.

This is not a contradiction.  It says that `LWWR` with absolute local modulus is still not the final
mechanism unless the height is allowed to be exponential or a sharper signed estimate is used.

## 4. The two viable routes

### Route A: Exponential wall height with horizontal control

Choose

```text
T(L) ~= e^L L^A,
delta ~= e^(-L/2)L^(-A/2).
```

Then the local mass (4) is polynomial or smaller.  The required new work is to prove that the
horizontal contour and finite-mesh tail remain polynomial at that height.

### Route B: Signed local quadrature

Do not dominate the local defect by a positive window `W_{L,delta}`.  Keep the signed Dirichlet kernel
and the prime weights:

```text
sum_{n<=e^L} Lambda(n)n^(-1/2-c)
  int [g_z(t)-g_z(log n)]D_T(t-log n)dt.               (5)
```

This is the `FarWall + NearWall` signed quadrature from E72.379.  It may remain polynomial even when
the positive local mass is exponential, because oscillation is retained.

## 5. Status

```text
proved: local positive prime-window mass has scale delta e^(L/2);
warning: LWWR with positive local modulus is too strong unless T is exponential or packet decay enters;
reduced: final WWR proof must choose Route A or Route B explicitly.
```

This audit prevents a false closure by a positive local derivative bound.
