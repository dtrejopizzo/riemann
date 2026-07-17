# E73.175 - Boundary trace reduction

Date: 2026-07-14.

## 1. Purpose

E73.174 rewrites the quotient forms using the scalar packets:

```text
B_{r,L}(y) = a_r(L) Q_L(y) xi_L.
```

This note records the key boundary identity:

```text
B_{r,L}(0) = 2 ell_r(G_L).
```

Thus `QG` is exactly a boundary trace estimate for three scalar packets.

## 2. Proof

The finite CCM kernel satisfies:

```text
q_{mn}(0)=0,      m != n,
q_{nn}(0)=2.
```

Hence:

```text
Q_L(0)=2I.
```

Therefore:

```text
B_{r,L}(0)
= a_r Q_L(0) xi_L
= 2 a_r xi_L
= 2 ell_r(G_L).
```

No limit or asymptotic is involved.

## 3. Boundary form of QG

The theorem `QG-LF`:

```text
|ell_r(G_L)| <= L^B e^(-alpha L)
```

is equivalent to:

```text
|B_{r,L}(0)| <= 2 L^B e^(-alpha L),
r=1,2,3.
```

## 4. Boundary equation

E73.174 gives:

```text
A_L[B_r] - P_L[B_r] = mu_L ell_r(G_L).
```

Using `B_r(0)=2ell_r(G_L)`, this becomes:

```text
A_L[B_r] - P_L[B_r] = (mu_L/2) B_r(0).
```

So the current theorem is:

```text
BT-QG:
For the three quotient packets B_{r,L},

|B_{r,L}(0)| <= L^B e^(-alpha L).
```

Equivalently, because the boundary equation is exact:

```text
|A_L[B_r]-P_L[B_r]| <= |mu_L| L^B e^(-alpha L).
```

## 5. Meaning

This is sharper than the previous Cauchy wording.  The proof no longer needs
to control a general Cauchy transform.  It must prove that the three quotient
packets have exponentially small boundary trace at `y=0`.

The packets are not arbitrary.  They are produced by:

1. the finite CCM/Feshbach eigenline `xi_L`;
2. the quotient rows `a_r(L)` in the three-dimensional critical quotient;
3. the exact finite kernel `Q_L(y)`.

## 6. Relation to Phase 72

This boundary identity is not conceptually isolated.  Phase 72 already found
the analogous transformed-packet fact:

```text
B_z(0)=2G_x(z).
```

There the route continued through the transformed packet equation, symmetric
zero-pair cancellation, and the gates `PAIR-Z / UREM-POLY`.

The new feature here is the quotient:

```text
C_L -> C_L / (C_L cap M_L).
```

So E73 is not rediscovering the Phase 72 packet boundary identity.  It is
applying the same boundary mechanism after the finite local action has removed
two generated critical directions.  The remaining packets are only:

```text
B_{1,L}, B_{2,L}, B_{3,L}.
```

Thus the corresponding Phase 72-style next theorem should be a quotient
packet equation for these three packets, not the old one-parameter `B_z`
equation.

## 7. Status

```text
proved:   B_r(0)=2 ell_r(G_L);
proved:   QG is equivalent to boundary trace smallness of B_r;
open:     prove the boundary trace estimate for the three quotient packets.
```
