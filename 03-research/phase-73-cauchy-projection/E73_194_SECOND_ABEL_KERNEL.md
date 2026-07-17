# E73.194 - Second Abel kernel for balanced packets

Date: 2026-07-14.

## 1. Purpose

E73.193 reduced the transverse matching theorem to balanced packets satisfying

```text
B(0)=0,      B'(0)=0,      B(L)=0.
```

This note derives the exact second-Abel identity for the model-prime
functional

```text
F_L[B]=A_L[B]-P_L[B].
```

The goal is to move the proof from endpoint estimates to a finite kernel
identity involving `B''`.

## 2. Dirichlet measure

For `B(0)=0`, the archimedean part is

```text
A_L[B]=int_0^L W_L(y)B(y)dy,
```

where

```text
W_L(y)=e^(y/2)+e^(-y/2)-e^(y/2)/(2sinh y).
```

The removable value at zero is interpreted after multiplication by `B(y)`.
The prime part is

```text
P_L[B]=sum_{p^k<=e^L} (log p)p^(-k/2) B(klog p).
```

Thus

```text
F_L[B]=int_[0,L] B(y)dmu_L(y),
```

with signed finite measure

```text
dmu_L(y)=W_L(y)dy
 - sum_{p^k<=e^L}(log p)p^(-k/2) delta_{klog p}(y).
```

## 3. Second Abel kernel

Define the second right-tail primitive

```text
K_L(t)=int_[t,L] (y-t)dmu_L(y)
```

or explicitly

```text
K_L(t)=int_t^L (y-t)W_L(y)dy
 - sum_{p^k: klog p>=t} (log p)p^(-k/2)(klog p-t).
```

Then, distributionally,

```text
K_L''=mu_L,       K_L(L)=0,       K_L'(L)=0.
```

## 4. Exact identity

If `B` is `C^2` between the prime-power nodes and satisfies

```text
B(0)=0,      B'(0)=0,      B(L)=0,
```

then

```text
F_L[B]=int_0^L K_L(t)B''(t)dt.                    (1)
```

Proof:

```text
int_0^L K_L B''
= [K_LB']_0^L - [K_L'B]_0^L + int_[0,L] B dmu_L.
```

The endpoint terms vanish because

```text
K_L(L)=K_L'(L)=0,      B(0)=B'(0)=0.
```

This gives (1).

## 5. New endpoint

For the balanced transverse packet,

```text
B=B_a^bal,
```

`BAL-DOUBLE-ZERO` is equivalent to

```text
SECOND-ABEL:
int_0^L K_L(t)(B_a^bal)''(t)dt = O_R(L^-R).       (2)
```

This is a finite zero-free identity.  The kernel `K_L` contains exactly the
model-prime discrepancy; the packet contains exactly the Cauchy-Schur
transverse geometry.

## 6. Why this is sharper than the old PNT route

E72.49 showed that classical PNT plus finite bandwidth still loses a
half-power.  The second-Abel identity does not estimate the prime discrepancy
by an external PNT error.  It keeps the exact finite kernel `K_L` and asks for
orthogonality against the specific balanced packet curvature.

Thus the next theorem is not a generic bound on `K_L`.  It is the signed
orthogonality

```text
<K_L,(B_a^bal)''>=O_R(L^-R)
```

for the Cauchy-balanced transverse packets.

## 7. Status

```text
proved: exact second-Abel identity for double-zero packets;
reduced: BAL-DOUBLE-ZERO to SECOND-ABEL;
open: prove the curvature orthogonality analytically.
```
