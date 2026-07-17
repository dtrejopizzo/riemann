# E72.379 - Weighted wall quadrature

## 1. Purpose

E72.378 bounded each wall coefficient separately.  That loses the cancellation between the wall gauge
`e^(ct)` and the prime weight `n^(-c)`.

This note sums first.  The result is an exact weighted quadrature identity for the prime wall error.
It is the correct finite object for proving `WeightedWallRegularity`.

## 2. Prime wall error after summing first

Let

```text
g_z(t):=e^(ct)B_z^M(|t|)1_{|t|<=L}.
```

For `u_n=log n`, E72.377 gives

```text
I_{c,T}(z;u_n)
=int_{-L}^{L} g_z(t)D_T(t-u_n)dt.
```

The finite-height prime wall is

```text
PrimeWall_{c,T}^{<=e^L}(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c)I_{c,T}(z;log n).
```

Interchanging the finite sum and the integral:

```text
PrimeWall_{c,T}^{<=e^L}(z)
=int_{-L}^{L} g_z(t)K_{L,c,T}(t)dt,                   (1)
```

where the finite weighted wall kernel is

```text
K_{L,c,T}(t)
:=sum_{n<=e^L} Lambda(n)n^(-1/2-c)D_T(t-log n).       (2)
```

The infinite-height target prime term is

```text
PrimeWall_{c,infty}(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n).          (3)
```

Since

```text
n^(-1/2-c)e^(c log n)=n^(-1/2),
```

(3) is exactly the weighted sampling of `g_z`:

```text
PrimeWall_{c,infty}(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c)g_z(log n).           (4)
```

Therefore the finite-height prime error is the quadrature defect

```text
ErrWallPrime_T(z)
=int_{-L}^{L} g_z(t)K_{L,c,T}(t)dt
 - sum_{n<=e^L} Lambda(n)n^(-1/2-c)g_z(log n).         (5)
```

Equation (5) is finite and exact.

## 3. Local cancellation of the right-wall gauge

Write the defect as

```text
ErrWallPrime_T(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c)
  int_{-L}^{L} [g_z(t)-g_z(log n)]D_T(t-log n)dt
 + Endpoint_T(z).                                     (6)
```

Near `t=log n`,

```text
g_z(t)-g_z(log n)
=e^(c log n)[ B_z^M(t)-B_z^M(log n)
              + O_c(|t-log n| sup_near |B_z^M|) ].
```

Multiplying by `n^(-1/2-c)` cancels the wall gauge:

```text
n^(-1/2-c)e^(c log n)=n^(-1/2).                       (7)
```

Thus the local part of the summed wall error is controlled by the natural critical weight
`Lambda(n)n^(-1/2)`, not by an exponentially larger `e^(cL)` wall norm.

## 4. Correct proof-facing bound

Define the local weighted modulus

```text
Omega_{L,T,delta}(z)
:=sum_{n<=e^L} Lambda(n)n^(-1/2)
  sup_{|t-log n|<=delta}
  |B_z^M(t)-B_z^M(log n)|,
```

and the local mass

```text
Mass_{L}(z)
:=sum_{n<=e^L} Lambda(n)n^(-1/2)|B_z^M(log n)|.
```

The near part of (6) is bounded by

```text
C log(2+Tdelta) [Omega_{L,T,delta}(z)+c delta Mass_L(z)].   (8)
```

The far part is not to be bounded by global `Var(e^(ct)B)`.  The correct finite target is the
oscillatory kernel estimate

```text
FarWall_{L,c,T,delta}(z)
:=sum_{n<=e^L} Lambda(n)n^(-1/2-c)
  int_{|t-log n|>delta}
  [g_z(t)-g_z(log n)]D_T(t-log n)dt.                  (9)
```

The finite weighted wall regularity gate is:

```text
WWR:
Omega_{L,T,delta}(z)+delta Mass_L(z)
+ |FarWall_{L,c,T,delta}(z)|
+ |Endpoint_T(z)|
<= C_K L^B
```

after choosing `delta=delta(L,T)` and `T=T(L)`.

## 5. Why this improves E72.378

E72.378 had the crude factor

```text
V(e^(ct)B_z^M).
```

That can be exponential in `L`.  E72.379 replaces it by weighted local prime sums and one signed far
oscillatory object.  The wall gauge cancels against `n^(-c)` before absolute values are taken locally.

This is the exact analogue of the earlier Feshbach lesson: sum coupled objects first, then estimate.

## 6. Status

```text
proved: finite-height prime wall error equals weighted quadrature defect (5);
proved: local wall gauge cancels against the prime weight;
reduced: WeightedWallRegularity to WWR, a finite weighted quadrature estimate;
open: prove WWR for the actual Feshbach packet B_z^M.
```
