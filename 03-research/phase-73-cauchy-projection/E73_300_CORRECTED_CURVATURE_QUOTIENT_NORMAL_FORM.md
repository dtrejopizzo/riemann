# E73.300 - Corrected curvature quotient normal form

Date: 2026-07-16.

## 1. Purpose

E73.299 fixes the constant part of the balanced curvature sign.  E73.301
upgrades it to the full neutral ramp of E73.193:

```text
(B^bal)''(t)=q[Q_t''+alpha_L(t)J]eta,
alpha_L(t)=(2/L)[-2/L+c_L(2-6t/L)].
```

This note propagates that correction into the quotient language of E73.271.
It also records what the correction does, and does not, buy.

## 2. Canonical corrected row

Let

```text
H_L=F_L[Q_t],       H_Lxi_L=mu_Lxi_L,
Q=Q_w,             R=I-Q^*(QQ^*)^(-1)Q,
eta=Rxi_L.
```

For each Cauchy row `q`, the endpoint scalar is

```text
S=qH_Leta=F_L[t -> qQ_teta].
```

The balanced packet is

```text
B(t)=qQ_teta,
B^bal(t)=B(t)-B'(0)r_*(t),
r_*(t)=t(1-t/L)+c_Lt^2(1-t/L).
```

Since `F_L[r_*]=0`, one has `F_L[B^bal]=F_L[B]`.  Applying the second
Abel identity to `B^bal` gives the corrected curvature row:

```text
S
=int_0^L K_L(t) q[Q_t''+alpha_L(t)J]eta dt.    (CQN)
```

## 3. Relation to the adjoint-source collapse

E73.276 proved that the coefficient/curvature adjoint source collapses to

```text
qH_L.
```

The corrected curvature operator does not evade that collapse.  It only gives
the correct local representative of the same row after the neutral ramp has
been absorbed.

Thus the corrected quotient theorem is not:

```text
find a new adjoint source.
```

It is:

```text
prove that the specific row
q int_0^L K_L(t)[Q_t''+alpha_L(t)J]dt R
pairs rapidly with the Gamma-prime eigenline xi_L.
```

## 4. Corrected quotient statement

Let `M_L^sym={Y^*E_L}` be any fixed symbolic left-coborder module, chosen
without using `xi_L` as a smallness input.  Define

```text
rho_q=qH_LR,
Delta_q=rho_q-Pi_{M_L^sym}rho_q.
```

Then

```text
rho_qxi_L=Delta_qxi_L.
```

Using `(CQN)`, the same `Delta_q` may be represented in curvature coordinates
by reducing the corrected row

```text
q int_0^L K_L(t)[Q_t''+alpha_L(t)J]dt R
```

modulo the same left-coborder module.  This is only a coordinate change unless
one proves an estimate for the quotient pairing.

## 5. The remaining theorem

The non-circular theorem is now precisely:

```text
Corrected Curvature Quotient Divisibility.
For every admissible q,w and every M,

Delta_qxi_L = O_M(L^(-M)),
```

where `Delta_q` is obtained from the corrected curvature row using a fixed
symbolic quotient construction.

Invalid proof branches remain:

```text
1. use Q_wxi_L as small;
2. choose the quotient projection by fitting xi_L;
3. estimate Q_t'' and J separately in absolute value;
4. invoke low-rank or low-moment compression.
```

## 6. Consequence

The current Phase 73 endpoint is unchanged, but its proof-facing curvature
normal form is now:

```text
CURV-ABEL-corrected:
int_0^L K_L(t) q[Q_t''+alpha_L(t)J]R_wxi_L dt
=O_M(L^(-M)).
```

This is equivalent to `FINAL-ETA-ADJ`, `CELL-CTM`, and the Schur-commutator
form.  It is the version that should be used in any subsequent analytic
attack.
