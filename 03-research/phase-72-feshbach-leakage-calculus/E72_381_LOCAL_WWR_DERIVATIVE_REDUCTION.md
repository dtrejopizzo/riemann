# E72.381 - Local WWR derivative reduction

## 1. Purpose

E72.379 defines the local weighted modulus

```text
Omega_delta(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2)
  sup_{|t-log n|<=delta}|B_z^M(t)-B_z^M(log n)|.
```

This note removes the pointwise supremum and rewrites it as a finite weighted derivative estimate for
the actual packet.  The result is a concrete analytic target involving `B'_z`, not an abstract modulus.

## 2. Prime-window weight

For `0<delta<1`, define

```text
W_{L,delta}(r)
:=sum_{n<=e^L} Lambda(n)n^(-1/2)
  1_{|r-log n|<=delta},        0<=r<=L.                (1)
```

This is finite and depends only on the von Mangoldt list up to `e^L`.

## 3. Derivative domination

For every `n` and every `t` with `|t-log n|<=delta`,

```text
B_z^M(t)-B_z^M(log n)=int_{log n}^{t} (B_z^M)'(r)dr.
```

Therefore

```text
sup_{|t-log n|<=delta}|B_z^M(t)-B_z^M(log n)|
<=int_{|r-log n|<=delta}|(B_z^M)'(r)|dr.
```

Multiplying by `Lambda(n)n^(-1/2)` and summing gives

```text
Omega_delta(z)
<=int_0^L |(B_z^M)'(r)| W_{L,delta}(r)dr.             (2)
```

This is the local WWR derivative reduction.

## 4. Actual packet derivative

By E72.337,

```text
B_z^M(y)
=1/L int_0^(L-y)
 [ A_z(t+y) conjugate(X(t)) + A_z^#(t+y)X(t) ]dt,
```

where

```text
A_z(r)=sum_m a_m(z)e^(id_mr),
X(r)=sum_n xi_n e^(id_nr).
```

Using

```text
A_z'(r)= -zA_z(r)-i(1-e^(zL))D_M(r),
(A_z^#)'(r)= zA_z^#(r)+i(1-e^(zL))D_M(r),
```

one obtains

```text
(B_z^M)'(y)
=1/L int_0^(L-y)
 [ (-zA_z(t+y)-iE_zD_M(t+y))conjugate(X(t))
   +( zA_z^#(t+y)+iE_zD_M(t+y))X(t) ]dt
 -Boundary_z(y),                                      (3)
```

with

```text
E_z:=1-e^(zL),
Boundary_z(y)=1/L[A_z(L)conjugate(X(L-y))+A_z^#(L)X(L-y)].
```

Equations (2)--(3) reduce the local half of `WWR` to finite harmonic analysis.

## 5. Proof-facing local gate

The local WWR gate is:

```text
LWWR:
int_0^L |(B_z^M)'(r)| W_{L,delta}(r)dr
 + delta sum_{n<=e^L} Lambda(n)n^(-1/2)|B_z^M(log n)|
<= C_K L^B.                                           (4)
```

If `LWWR` holds, then the near part of `WWR` holds by E72.379.

## 6. Why this is sharper

The old bad estimate was a global wall variation:

```text
Var(e^(ct)B_z^M).
```

E72.381 replaces it locally by:

```text
int |B'_z(r)| W_{L,delta}(r)dr,
```

where the wall gauge has already cancelled against the prime weight.  This keeps the arithmetic
sampling geometry and avoids the global `e^(cL)` ceiling.

## 7. Status

```text
proved: Omega_delta is dominated by the prime-windowed derivative integral (2);
proved: B'_z has the exact Dirichlet-Cauchy packet form (3);
reduced: local WWR to LWWR;
open: prove LWWR uniformly for the actual Feshbach packet.
```
