# E73.174 - QG quadrature form

Date: 2026-07-14.

## 1. Purpose

E73.173 identifies the active matching theorem:

```text
Arch_r(L) - Prime_r(L) = mu_L ell_r(G_L),       r=1,2,3.
```

This note rewrites `Arch_r` and `Prime_r` from a single scalar packet:

```text
B_{r,L}(y) = a_r(L) Q_L(y) xi_L.
```

Here `Q_L(y)` is the finite matrix with entries `q_{mn}(y)` from the CCM/Weil
operator.

## 2. Scalar packet

For a quotient row `a_r`, define:

```text
B_r(y) := a_r Q_L(y) xi_L,       0 <= y <= L.
```

This is now the only object entering both sides of the arch/prime matching.

## 3. Prime side

The prime transform is exactly:

```text
Prime_r(L)
= sum_{p^k <= exp(L)}
   (log p) p^(-k/2) B_r(k log p).
```

This follows directly from the arithmetic part of the finite CCM matrix:

```text
P_prime,L(m,n)
= sum_{p^k <= exp(L)} (log p) p^(-k/2) q_{mn}(k log p).
```

## 4. Archimedean side

Let:

```text
B_0 = B_r(0).
```

The archimedean finite functional is:

```text
Arch_r(L)
= int_0^L B_r(y)(e^(y/2)+e^(-y/2)) dy
 - 1/2(log(4pi)+gamma) B_0
 - int_0^L [e^(y/2)B_r(y)-B_0]/[2sinh(y)] dy
 - 1/2 log(tanh(L/2)) B_0.
```

At `y=0`, the regularized integrand is interpreted by the finite limit:

```text
[B_r'(0)+B_0/2]/2.
```

Thus the matching theorem can be written entirely as:

```text
QG-QUAD:
| A_L[B_r] - P_L[B_r] |
<= |mu_L| L^B e^(-alpha L),
```

where:

```text
A_L[B] = the archimedean functional above,
P_L[B] = sum_{p^k <= exp(L)} (log p)p^(-k/2)B(k log p).
```

## 5. Why this matters

The proof problem no longer contains a hidden matrix operation.  It is a
finite explicit formula comparison on three scalar packets:

```text
B_{1,L}, B_{2,L}, B_{3,L}.
```

The catch is important: `A_L[B_r]` and `P_L[B_r]` are individually much larger
than their difference.  Therefore numerical subtraction of quadratures is not
proof-facing.  The proof must use the structure of `B_r` and the finite
eigenline equation to show symbolic cancellation.

## 6. Relation to previous endpoints

This is sharper than the Phase 72 packet estimates.  Those tried to bound
large packets or their Green-cycle energies.  Here the packet is not arbitrary:
it is one of three quotient rows after the finite local action has removed
the generated two-dimensional obstruction.

The theorem is still not proved.  But it is now an explicit scalar
arch/prime quadrature identity for three packets.

## 7. Status

```text
proved:   Arch_r and Prime_r have exact scalar packet formulas;
verified: the formulas reconstruct matrix Arch_r and Prime_r individually;
open:     prove the cancellation A_L[B_r]-P_L[B_r] at the mu_L*QG scale.
```
