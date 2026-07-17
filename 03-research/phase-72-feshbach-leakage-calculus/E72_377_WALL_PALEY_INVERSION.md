# E72.377 - Wall Paley inversion

## 1. Purpose

E72.375 writes the right-wall prime term as Fourier coefficients of `H_z(c+it)`:

```text
I_{c,T}(z;u)=1/(2pi) int_{-T}^{T} H_z(c+it)e^(-itu)dt.
```

This note proves the exact infinite-height inversion.  It removes the artificial infinite prime tail
from the wall formulation and recovers the natural compact cutoff `n<=e^L`.

## 2. Compact packet representation

For the finite Feshbach packet `B_z^M`, E72.339 gives

```text
F_z^M(w)=int_{-L}^{L} e^(wt)B_z^M(|t|)dt.              (1)
```

In the complete-mesh paired kernel, E72.372--E72.373 identify the same object as

```text
H_z(w)=F_z^M(w)
```

up to the finite Fourier-mesh tail already isolated in E72.319.  Therefore the wall inversion should
be applied to the finite packet form (1).  This avoids any ambiguity caused by the complete/tail split.

## 3. Inversion lemma

Let

```text
F(w)=int_{-L}^{L} e^(wt)f(t)dt
```

with `f in L^1[-L,L]` and continuous at `u`.  For any `c in R`,

```text
I_c^T(u):=1/(2pi) int_{-T}^{T} F(c+it)e^(-itu)dt.
```

Then

```text
lim_{T->infty} I_c^T(u)=e^(cu)f(u)                    (2)
```

at every continuity point `u`, with the standard half-sum convention at jump points.

### Proof

Substitute the compact representation:

```text
I_c^T(u)
=int_{-L}^{L} e^(ct)f(t)
  [1/(2pi)int_{-T}^{T} e^(it(t-u))dt]dt
=int_{-L}^{L} e^(ct)f(t) D_T(t-u)dt,                  (3)
```

where

```text
D_T(x)=sin(Tx)/(pi x)
```

is the Dirichlet approximate identity in the symmetric Fourier inversion convention.  Hence (2)
follows from the standard Fourier inversion theorem for compactly supported `L^1` functions. `QED`

## 4. Prime-wall limit

Apply (2) with

```text
f_z(t)=B_z^M(|t|)1_{|t|<=L}.
```

For `u=log n>=0`,

```text
lim_{T->infty} I_{c,T}(z;log n)
= e^(c log n)B_z^M(log n)1_{log n<=L}.                (4)
```

Therefore

```text
lim_{T->infty} PrimeWall_{c,T}(z)
= sum_{n<=e^L} Lambda(n)n^(-1/2-c)
   n^c B_z^M(log n)
= sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n).         (5)
```

This is exactly the prime term in the balanced explicit formula of E72.339--E72.340.

## 5. Consequence

The right-wall formulation is not a new independent estimate.  In the infinite-height limit it is
exactly equivalent to the compact Paley-Weil identity:

```text
RightWall(F_z^M)
= Arch_L(B_z^M)
 - sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n).
```

Thus `FWB` is the finite-height, finite-wall version of `BER-POLY/BFW-coupled`.  It is useful because
it gives a completely explicit finite approximation, but it cannot close the theorem by an absolute
Dirichlet-tail estimate alone.  The load-bearing cancellation is still the coupled Feshbach-Weil
identity of E72.340.

## 6. Quantitative finite-height form

For finite `T`,

```text
I_{c,T}(z;u)-e^(cu)f_z(u)
=int_{-L}^{L} e^(ct)[f_z(t)-f_z(u)]D_T(t-u)dt
 + e^(cu)f_z(u)
   [int_{-L}^{L} D_T(t-u)dt - 1].                     (6)
```

This gives the next genuinely analytic estimate:

```text
WallTail_T(z;u)
= I_{c,T}(z;u)-e^(cu)B_z^M(u).
```

The finite wall bound follows from a summed Dirichlet-kernel modulus estimate:

```text
sum_{n<=e^L} Lambda(n)n^(-1/2)
 |WallTail_T(z;log n)|
```

plus the corresponding archimedean wall-tail and finite Fourier-mesh tail.  This is an approximation
problem for the compact packet, not a zero-divisor problem.

## 7. Status

```text
proved: right-wall Fourier coefficients invert to the compact packet;
proved: the infinite-height prime wall has the natural finite cutoff n<=e^L;
identified: FWB is a finite-height version of BER/BFW-coupled, not a separate RH mechanism;
open: prove quantitative finite-height wall-tail bounds for the actual packet.
```
