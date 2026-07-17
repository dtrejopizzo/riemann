# E74.4 - Harmonic row equals the CCM operator row

Date: 2026-07-16.

## Purpose

E74.3 rewrote the final scalar as

```text
<r_beta, M_U eta> + <r_beta, M_W(A+M_{H_beta})eta>.
```

This note identifies the corresponding row with the actual finite CCM row
`r_beta H_L`, modulo the harmless Cauchy gauge already isolated in E73.291.

## Statement

Define the harmonic-symbol row

```text
K_HS
= r_beta M_U + r_beta M_W A + r_beta M_W M_{H_beta}.
```

Then

```text
K_HS = r_beta H_L + alpha q_w + beta q_-w.          (HS-ROW)
```

Consequently, for

```text
eta=(I-P_w)xi_L,        Q_w eta=0,
```

one has

```text
K_HS eta = r_beta H_L eta.                          (HS-PAIR)
```

Since `Q_w eta=0`, the Cauchy gauge is invisible in the scalar.

## Relation to the eigenline equation

Let

```text
E_L=H_L-mu_L I,        H_L xi_L=mu_L xi_L.
```

Because `r_beta eta=0`,

```text
r_beta H_L eta = r_beta E_L eta.
```

Since `eta=(I-P_w)xi_L` and `E_L xi_L=0`,

```text
r_beta E_L eta = -r_beta E_L P_w xi_L
               = -r_beta[H_L,P_w]xi_L.
```

Thus E74 does not create a separate proof branch.  It gives a sharper finite
coordinate form for the same load-bearing theorem:

```text
Harmonic-symbol eigenline cancellation
<=> Schur-commutator eigenline cancellation
<=> structured left-coborder for r_beta E_L(I-P_w).
```

## The next theorem

The proof-facing target is now:

```text
HSEC-COB.
There exists an explicit primitive row Y_{beta,w,L}, built only from the
finite mesh, H_beta, the Cauchy rows, and the CCM cell algebra, such that

K_HS = Y_{beta,w,L} E_L + alpha q_w + beta q_-w + R_L,

with <R_L,xi_L>=O_M(L^(-M)).
```

This is the non-tautological way to use the eigenline equation.  Choosing
`Y` by a pseudoinverse of `E_L`, or from the final scalar, is forbidden.

## Status

```text
proved: algebraic reduction HS-PAIR -> Schur commutator;
verified: HS-ROW modulo Cauchy gauge numerically;
open: construct the explicit primitive Y_{beta,w,L}.
```
