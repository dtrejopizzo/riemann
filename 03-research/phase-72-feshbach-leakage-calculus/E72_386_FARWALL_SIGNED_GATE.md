# E72.386 - FarWall signed gate

## 1. Purpose

E72.385 closes the horizontal `BV-K` part of the natural-height wall route.  This note audits the
remaining far Dirichlet-quadrature term from E72.379:

```text
FarWall_{L,c,T,delta}(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c)
  int_{|t-log n|>delta}
  [g_z(t)-g_z(log n)]D_T(t-log n)dt.
```

The conclusion is important: FarWall must remain signed.  An absolute BV estimate is still too strong
unless an impossible wall inequality holds.

## 2. Why the absolute far estimate fails

For one node `u=log n`, the far Dirichlet primitive gives the generic bound

```text
|Far_u| <= C Var(g_z)/(T delta).
```

Summing with the absolutely convergent wall weights gives

```text
sum_{n<=e^L} Lambda(n)n^(-1/2-c)|Far_u|
<= C_c Var(g_z)/(T delta).                            (1)
```

At natural height

```text
T=e^L L^A,        delta=T^(-1/2),
```

we have

```text
T delta = e^(L/2)L^(A/2).
```

By E72.383--E72.385,

```text
Var(g_z) <= C_K e^((c+sigma_K)L)L^B.
```

Substituting in (1) gives

```text
absolute FarWall <= C_K e^((c+sigma_K-1/2)L)L^(B-A/2). (2)
```

For the right wall one needs `c>1/2`, and for an off-line shifted compact one has `sigma_K>0`.
Therefore

```text
c+sigma_K-1/2>0.
```

The absolute far estimate is exponential.  It cannot close Phase 72.

## 3. Correct signed form

The far term must be kept as the signed quadrature defect:

```text
FarWall(z)
=int_{-L}^{L} g_z(t)K_{L,c,T}^{far}(t)dt
 - signed local counterterms,
```

where

```text
K_{L,c,T}(t)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c)D_T(t-log n).
```

Equivalently, using the finite measure

```text
dmu_{L,c}(u)=sum_{n<=e^L} Lambda(n)n^(-1/2-c)delta_{log n}(u),
```

the full wall error is

```text
ErrWall(z)=<g_z, D_T*dmu_{L,c}-dmu_{L,c}>.             (3)
```

Thus the true FarWall theorem is a signed band-limiting statement:

```text
SignedFar:
|<g_z, D_T*dmu_{L,c}-dmu_{L,c}> - NearWall(z)|
<= C_K L^B.
```

The prime current is coupled before absolute values.  This is exactly the same structural rule that
survived every earlier wall audit.

## 4. Frequency interpretation

Let

```text
G_z(t)=g_z(t)1_{[-L,L]}(t).
```

Formally, `D_T*dmu` keeps only frequencies `|tau|<=T`.  Therefore

```text
ErrWall(z)
=1/(2pi) int_{|tau|>T} \widehat{G_z}(-tau)
   [sum_{n<=e^L} Lambda(n)n^(-1/2-c-itau)] dtau.       (4)
```

This is the right analytic form: the tail is a high-frequency interaction between the compact
Feshbach packet and a finite Dirichlet polynomial.  It is not a positive local-mass estimate.

## 5. Status

```text
proved: absolute FarWall has exponential scale at natural height;
identified: FarWall must be proved as a signed band-limiting/quadrature defect;
open: prove SignedFar for the actual Feshbach packet and finite von Mangoldt measure.
```
