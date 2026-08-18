# E99.005 - Final adjugate boundary target

## 1. Canonical constrained sensitivity

Let `SRC_(t,z)` denote the bordered block source in E99.002 after the
Gamma--Euler expansion E99.004.  Put

```text
G_t=adj(H_t-mu_tI)/partial_mu chi(t,mu_t),             (1.1)

gamma_t(z)=partial_mu P(t,mu_t,z)/P(t,mu_t,z).        (1.2)
```

The constrained sensitivity commutator has two different exact components:

```text
bordered component:
  a cofactor sandwich of SRC_(t,z) by adj(B_z)/det(B_z);

characteristic component:
  -gamma_t(z)[Z,G_t].                                (1.3)
```

The first component follows from E99.003(2.1).  The second is retained as a
normalized characteristic-adjugate commutator.  No characteristic inverse or
power of `det(H_t-mu_tI)` occurs.

## 2. Trace pairing

In one Euler direction the bordered component is

```text
+Tr[adj(B_z)SRC_(t,z)adj(B_z)Z^(-1)X]
 /det(B_z)^2,                                        (2.1)
```

while the characteristic component is

```text
+gamma_t(z)Tr([Z,G_t]Z^(-1)X).                       (2.2)
```

The adjoint Euler direction is included by the formula of E97.002.  Equations
(2.1)--(2.2) are schematic block notation for the exact pullbacks to the full
finite matrix direction.

## 3. Bilateral projective combination

Let `PAIR_t(z)` be the sum of the two Euler directions in (2.1)--(2.2), and
define

```text
BPAIR_t(s;s_*)
 =PAIR_t(iu)+PAIR_t(-iu)
  -PAIR_t(iu_*)-PAIR_t(-iu_*).                       (3.1)
```

Add the Fourier shell scalar of E98.004.

## 4. Remaining theorem

The direct route is reduced to

```text
ADJUGATE-BOUNDARY-SANDWICH:
BASE_(L,N)(s;s_*)
 +integral_0^1 {
    BPAIR_t(s;s_*)
   +SHELL_(L,N,t)(s;s_*)
   -[J_L(s)-J_L(s_*)]
  }dt
 ->0.                                                (4.1)
```

## 5. Minimality and status

Every symbol in (4.1) is explicit finite Gamma--prime data, an independently
defined Euler current or an exact boundary/compression correction.  Removing
any bordered source block or the characteristic cofactor commutator changes
the finite determinant identity.

```text
closed:
  explicit construction of every bordered sandwich source and the normalized
  characteristic cofactor term;

open:
  ADJUGATE-BOUNDARY-SANDWICH.
```
