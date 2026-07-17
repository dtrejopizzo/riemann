# E73.189 - Cauchy-Dirichlet transverse packet

Date: 2026-07-14.

## 1. Purpose

E73.188 identifies the anti-circular target:

```text
TRANS-CELL:
Q_wH_model,L eta_w = Q_wPrime_L eta_w + O_R(L^-R),
eta_w=(I-P_w)xi_L,
Q_w eta_w=0.
```

This note extracts the first analytic consequence of `Q_w eta_w=0`: the
transverse packet has two endpoint zeros.  This removes the dangerous boundary
terms from the explicit formula cell.

## 2. Packet

For a Cauchy row `q_j in {q_w,q_-w}` define

```text
B_j^perp(y)=q_j Q_L(y) eta_w.
```

The kernel used throughout Phase 72--73 satisfies

```text
Q_L(0)=2I,
Q_L(L)=0.
```

Therefore:

```text
B_j^perp(0)=2 q_j eta_w=0,              (1)
B_j^perp(L)=0.                          (2)
```

Equation (1) uses the Cauchy annihilation; equation (2) is the finite
Dirichlet wall of the triangular Weyl kernel.

## 3. Simplified archimedean cell

For a general packet `B`, E73.181 used

```text
A_L[B] =
 int_0^L B(y)(e^(y/2)+e^(-y/2))dy
 - 1/2(log(4pi)+gamma)B(0)
 - int_0^L [e^(y/2)B(y)-B(0)]/[2sinh(y)]dy
 - 1/2 log(tanh(L/2))B(0).
```

For the transverse Cauchy-Dirichlet packet, `B(0)=0`, so this becomes

```text
A_L[B_j^perp]
= int_0^L B(y)(e^(y/2)+e^(-y/2))dy
 - int_0^L e^(y/2)B(y)/(2sinh y) dy.       (3)
```

The apparent singularity at `0` is removable because `B(y)=B'(0)y+O(y^2)` and

```text
e^(y/2)B(y)/(2sinh y) = B'(0)/2 + O(y).
```

Equivalently,

```text
A_L[B]
= int_0^L B(y) e^(-y/2) dy
 + int_0^L B(y)e^(y/2)(1-1/(2sinh y))dy.  (4)
```

The second weight is regular at `0` after multiplication by `B(y)`.

## 4. What this buys

The old principal packet had nonzero `B(0)` and therefore carried:

```text
Gamma constant term,
log(tanh(L/2)) boundary term,
WR subtraction by B(0).
```

Those terms are exactly gone in the transverse packet.  Thus `TRANS-CELL` is
not a generic explicit-formula residual.  It is a Dirichlet packet residual:

```text
A_L[B^perp]-P_L[B^perp],
B^perp(0)=B^perp(L)=0.
```

This is the first place where the Cauchy projection produces an analytic gain
instead of merely reorganizing the same scalar obstruction.

## 5. Next proof target

The next theorem should use (1)--(2) to prove a finite quadrature identity:

```text
Dirichlet explicit-formula matching:
A_L[B^perp_{j,w}]
-
sum_{p^k<=e^L} (log p)p^(-k/2) B^perp_{j,w}(k log p)
= O_R(L^-R).
```

The packet is not arbitrary: it is a finite Weyl packet with two Cauchy
moments zero.  The proof should exploit both:

```text
endpoint Dirichlet: B(0)=B(L)=0,
Cauchy divisibility: sum_n eta_n/(w+id_n)=sum_n eta_n/(-w+id_n)=0.
```

## 6. Status

```text
proved: Qeta=0 and Q_L(0)=2I imply B^perp(0)=0;
proved: Q_L(L)=0 implies B^perp(L)=0;
reduced: TRANS-CELL to a Dirichlet explicit-formula matching problem;
open: prove the matching from finite Weyl packet structure and prime sampling.
```

## 7. Prior-route audit

Phase 72 already had a `Cauchy-Dirichlet packet` in E72.337.  That object came
from the one-parameter multiplier

```text
a_m(z)=(1-e^(zL))/(iz-d_m)
```

and was used for `BULK-SMOOTH`.  The useful lesson from E72.337 is the
differential identity

```text
A_z'(r)=-zA_z(r)-i(1-e^(zL))D_M(r),
```

which avoids exposing uncontrolled powers of `d_m`.

The E73.189 object is not just a reprise of that route:

```text
E72.337: one-parameter transformed packet, Dirichlet endpoint, norm bounds;
E73.189: two-row Cauchy transverse packet, Dirichlet endpoints, and
         Q_w eta=0 for both rows.
```

The no-go lesson is also imported: endpoint Dirichlet control alone is not
enough.  The next theorem must use the two Cauchy moment constraints together
with the model-prime explicit formula; otherwise it collapses back to the
generic packet-bound route that Phase 72 did not close.
