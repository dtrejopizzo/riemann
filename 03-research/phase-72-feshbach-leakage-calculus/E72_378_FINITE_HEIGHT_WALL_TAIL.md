# E72.378 - Finite-height wall tail

## 1. Purpose

E72.377 proves the infinite-height wall inversion.  The remaining finite-wall issue is the error

```text
WallTail_T(z;u)
= I_{c,T}(z;u)-e^(cu)f_z(u),
f_z(u)=B_z^M(|u|)1_{|u|<=L}.
```

This note gives a quantitative Dirichlet-kernel bound and records the scale obstruction that prevents
a crude absolute proof from closing Phase 72.

## 2. Dirichlet-kernel representation

Let

```text
g(t):=e^(ct)f_z(t).
```

Then

```text
I_{c,T}(z;u)
=int_{-L}^{L} g(t)D_T(t-u)dt,
D_T(x)=sin(Tx)/(pi x).                                (1)
```

Assume `u` is an interior point and set

```text
d(u):=dist(u,{-L,L}).
```

For any `0<delta<d(u)`,

```text
WallTail_T(z;u)
= Near_delta + Far_delta + Endpoint_delta,
```

where the near part integrates over `|t-u|<=delta`, the far part over
`delta<|t-u|<=L`, and the endpoint term accounts for truncating the Dirichlet integral to `[-L,L]`.

## 3. Quantitative lemma

Let

```text
omega_g(delta;u):=sup_{|t-u|<=delta}|g(t)-g(u)|,
V_g:=Var_{[-L,L]}(g).
```

Then

```text
|WallTail_T(z;u)|
<= C omega_g(delta;u) log(2+Tdelta)
 + C V_g/(Tdelta)
 + C |g(u)|/(T d(u)),                                  (2)
```

for an absolute constant `C`.

### Proof

Write

```text
WallTail_T(z;u)
=int_{-L}^{L} [g(t)-g(u)]D_T(t-u)dt
 + g(u)[int_{-L}^{L}D_T(t-u)dt-1].                    (3)
```

On `|t-u|<=delta`,

```text
int |D_T(t-u)|dt <= C log(2+Tdelta),
```

giving the first term.

On the far region, integrate by parts in the Stieltjes sense against `g`.  Since

```text
|D_T(x)|<=1/(pi|x|),
```

and the oscillatory primitive of `D_T` on intervals avoiding zero is `O(1/(Tdelta))`, the far term is
bounded by `C V_g/(Tdelta)`.  Finally,

```text
int_{-L}^{L}D_T(t-u)dt-1
```

is the missing tail of the full-line Dirichlet inversion.  Since the nearest missing endpoint is at
distance `d(u)`, a single integration by parts gives `O(1/(T d(u)))`. `QED`

## 4. Summed prime-wall tail

For `u_n=log n`, the finite-height prime error satisfies

```text
ErrWallPrime_T(z)
<= sum_{n<=e^L} Lambda(n)n^(-1/2-c)
   |WallTail_T(z;u_n)|.                                (4)
```

Using (2),

```text
ErrWallPrime_T(z)
<= C log(2+Tdelta) S_omega
 + C V_g/(Tdelta) S_c
 + C/T S_end,                                         (5)
```

where

```text
S_omega=sum_{n<=e^L} Lambda(n)n^(-1/2-c)omega_g(delta;log n),
S_c=sum_{n<=e^L} Lambda(n)n^(-1/2-c),
S_end=sum_{n<=e^L} Lambda(n)n^(-1/2-c)|g(log n)|/d(log n).
```

This is a fully finite bound.

## 5. Scale warning

The bound is only useful if `g(t)=e^(ct)f_z(t)` has controlled variation/modulus in the weighted
right-wall gauge.  A crude estimate gives

```text
V_g <= e^(cL)(c||f_z||_1+Var(f_z)),
```

which is exponential in `L`.  Taking `T` exponentially large would formally suppress this term, but
the horizontal contour and finite-mesh tail must then be controlled at the same height.  Therefore the
crude BV route is not a proof of Phase 72.

The required improvement is a coupled packet estimate:

```text
WeightedWallRegularity:
S_omega, V_g S_c, S_end are polynomial in L after the prime weights and Feshbach coupling are kept.
```

This is the right quantitative replacement for the old false `PACK-SMOOTH`.

## 6. Status

```text
proved: explicit finite-height Dirichlet tail bound;
proved: summed prime-wall tail reduces to finite weighted regularity quantities;
warning: crude absolute BV gives an exponential e^(cL) ceiling;
open: prove WeightedWallRegularity for the actual Feshbach packet.
```
