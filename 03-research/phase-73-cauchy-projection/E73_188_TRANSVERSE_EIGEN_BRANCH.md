# E73.188 - Transverse eigen-branch and the anti-circular target

Date: 2026-07-14.

## 1. Purpose

E73.187 showed that the remaining residual is

```text
T(w)=Q_w(H_model,L-Prime_L)(I-P_w)xi_L
    =Q_wH_L(I-P_w)xi_L.
```

This note separates two facts:

```text
1. an exact eigen-equation identity that explains why T is small once h is small;
2. the anti-circular theorem that is still needed to prove h is small.
```

This prevents us from accidentally proving the divisor statement by feeding
the divisor statement back into itself.

## 2. Exact projection algebra

Let `Q=Q_w` be the `2 x n` matrix of Cauchy rows and let

```text
P=Q^*(QQ^*)^{-1}Q
```

be the orthogonal projection onto the row plane.  Then

```text
Q(I-P)=0.
```

For the ground vector

```text
H_L xi_L = mu_L xi_L,
h=Q xi_L,
```

we have

```text
T(w)=QH_L(I-P)xi_L
    =QH_Lxi_L-QH_LPxi_L
    =mu_L h-QH_LQ^*(QQ^*)^{-1}h.              (1)
```

If the Cauchy-plane action is represented in the orthogonal row basis by

```text
A_Q(w)=QH_LQ^*(QQ^*)^{-1},
```

then

```text
T(w)=(mu_L I-A_Q(w))h.                         (2)
```

This is the vector form of E73.179.

## 3. Why (2) is not a proof

Equation (2) shows that `T` is small if `h` is small and `A_Q` is
polynomially bounded.  But the chain needs the reverse direction:

```text
T small + CPINV => h small.
```

Thus proving `T small` by first proving `h small` is circular.  The exact
eigen-branch is useful only as a consistency check and as a guard against
tautological proofs.

## 4. Anti-circular target

The theorem must be proved in the model-prime cell form:

```text
Q_wH_model,L(I-P_w)xi_L
-
Q_wPrime_L(I-P_w)xi_L
= O_R(L^-R),                                      (3)
```

without using the smallness of

```text
h=Q_wxi_L.
```

Equivalently, since `(I-P_w)xi_L` lies exactly in `ker Q_w`, (3) says:

```text
The explicit CCM model-prime operator maps the intrinsic ground component
inside ker Q_w back into ker Q_w, up to rapidly decaying error, as seen by
the two Cauchy rows.
```

This is a finite Cauchy-Schur invariance statement on one vector, not a norm
invariance of the whole Cauchy plane.  This distinction matters because
E73.154 already showed that the Cauchy plane is not almost invariant in row
norm.

## 5. Proof-facing finite identity

The non-circular statement to attack is therefore:

```text
TRANS-CELL:
For eta_w=(I-P_w)xi_L, Q_w eta_w=0 and

Q_wH_model,L eta_w
=Q_wPrime_L eta_w + O_R(L^-R)
```

with both sides expanded by the explicit finite cells:

```text
(Q_wH_model,L eta_w)_j
  = A_L[B^perp_{j,w}],

(Q_wPrime_L eta_w)_j
  = P_L[B^perp_{j,w}],

B^perp_{j,w}(y)=q_j Q_L(y) eta_w.
```

The condition `Q_w eta_w=0` is the new structural input.  The next analytic
step is to use that annihilation to prove a divisibility or integration-by-
parts gain in the explicit formula cell

```text
A_L[B^perp]-P_L[B^perp].
```

## 6. Status

```text
proved:  exact eigen-branch T=(mu I-A_Q)h;
proved:  this branch is circular if used to prove T small;
target:  prove TRANS-CELL from the explicit formula and Q_w eta_w=0.
```
