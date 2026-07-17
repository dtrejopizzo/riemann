# E72.376 - Finite wall bound gate

## 1. Purpose

E72.373--E72.375 replace the paired zero pressure by the finite right-wall identity

```text
Lambda_L G_x(z)
= ArchPolar_{c,T}(z)
 - PrimeWall_{c,T}^{<=N}(z)
 + Horiz_{c,T}(z)/(4pi i)
 + ErrPrime_{c,T}^{>N}(z)
 - Lcal(B_z^tail).                                     (1)
```

This note states the exact analytic gate left by that reduction and proves that it implies the
transformed Phase 72 endpoint.

## 2. The finite wall bound

Fix a compact shifted strip `K` for `z`, and choose `c>1/2`.  The finite wall bound is:

```text
FWB(K,c):
there exist B,C and choices T=T(L), N=N(L) with T,N -> infinity such that
for all z in K,

|ArchPolar_{c,T}(z)-PrimeWall_{c,T}^{<=N}(z)|
+ |Horiz_{c,T}(z)|
+ M_{c,T}(z)R_c(N)
+ |Lcal(B_z^tail)|
<= C L^B.                                             (2)
```

Here

```text
M_{c,T}(z)=1/(2pi) int_{-T}^{T}|H_z(c+it)|dt,
R_c(N)=sum_{n>N} Lambda(n)n^(-1/2-c),
```

and all terms are those of E72.375.

This is not a positivity statement and not a zero-location statement.  It is a finite explicit
right-wall Fourier estimate.

## 3. Theorem

### Theorem 72.376

Assume:

```text
LCOEF: |Lambda_L| >= c_0 L^a,
FWB(K,c).
```

Then

```text
PW-Cauchy(K): sup_{z in K}|G_x(z)| <= C_K L^{B-a}.
```

Consequently, by E72.329 and the already recorded transport/source gates of Phase 72, the transformed
Mellin spectral divisibility endpoint follows for the compact-root channel.

### Proof

Start from (1).  By (2), the right side has size `O_K(L^B)`.  Divide by `Lambda_L`; `LCOEF` gives

```text
|G_x(z)| <= C_K L^B / (c_0 L^a)=C'_K L^{B-a}.
```

This is exactly `PW-Cauchy(K)`.  The implication from `PW-Cauchy` to the compact-root Mellin spectral
divisibility endpoint is Theorem 72.329.  `QED`

## 4. What remains genuinely open

The whole remaining mathematical content is now (2).  Written without names:

```text
| 1/(2pi) int_{-T}^{T} H_z(c+it)A_c(t)dt
 - sum_{n<=N} Lambda(n)n^(-1/2-c)
   1/(2pi) int_{-T}^{T} H_z(c+it)e^(-it log n)dt |

+ horizontal + prime-tail + finite-mesh-tail
<= C_K L^B.                                            (3)
```

Everything in (3) is finite and computable.  The zero divisor is no longer an input.

## 5. Why this is the correct next inequality

Earlier gates tried to control zero sums, Cauchy denominators, or matrix energies directly.  E72.372
removed the Cauchy denominator by a hyperbolic divided difference.  E72.373 converted divisor sampling
to a residue trace.  E72.374 compressed the trace to the right wall.  E72.375 cut the right-wall prime
series to a finite von Mangoldt sum.

Thus (3) is the first formulation in this branch with all four required properties:

```text
finite;
explicit;
zero-free at proof level;
still coupled to the actual prime current.
```

## 6. Status

```text
proved: FWB + LCOEF implies PW-Cauchy;
proved: PW-Cauchy feeds the E72.329 transformed endpoint;
open: prove FWB itself.
```
