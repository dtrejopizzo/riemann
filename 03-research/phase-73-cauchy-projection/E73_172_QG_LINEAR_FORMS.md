# E73.172 - QG scalar linear forms

Date: 2026-07-14.

## 1. Purpose

E73.171 rewrites `QG` as a wedge determinant:

```text
||P_Q,L G_L||^2
= det Gram(I_L,G_L) / det Gram(I_L).
```

This note expands the same condition into three scalar linear forms.

## 2. Construction

Let

```text
I_L = C_L cap M_L
```

be the two-dimensional generated intersection inside the five-dimensional
critical `cauchy0` space.  Choose an orthonormal basis

```text
q_1(L), q_2(L), q_3(L)
```

of `I_L^perp` in `C_L`.

Then

```text
||P_Q,L G_L||^2 = sum_{r=1}^3 |ell_{r,L}(G_L)|^2,
```

where

```text
ell_{r,L}(G_L)
  = sum_{j=1}^5 conjugate(q_r(L)_j) G_L(gamma_j),
```

and

```text
G_L(gamma_j)
  = (1-e^(i gamma_j L)) sum_m xi_L(m)/(-gamma_j-d_m).
```

Thus `QG` is implied by the three scalar estimates:

```text
|ell_{r,L}(G_L)| <= L^B e^(-alpha L),  r=1,2,3.
```

## 3. No hidden condition loss

The coefficient operator from `G_L` to the form vector is an orthogonal
projection:

```text
G_L -> (ell_{1,L}(G_L), ell_{2,L}(G_L), ell_{3,L}(G_L)).
```

Therefore its operator norm is exactly `1`.

This matters: the scalarization does not introduce a Cauchy-condition-number
loss, a Vandermonde loss, or a hidden exponential coefficient.

## 4. Current proof-facing theorem

The current load-bearing statement can now be written as:

```text
QG-LF:
There exist B,L0 such that for all L>=L0 and r=1,2,3,

| sum_{j=1}^5 conjugate(q_r(L)_j)
    (1-e^(i gamma_j L)) sum_m xi_L(m)/(-gamma_j-d_m) |
<= L^B e^(-alpha L).
```

Together with `QPI`, this implies `QUOT-NORM`, hence `QUOT-PAIR`, hence
`DATA-HERM/NAT-SRC`, hence scalar WRL.

## 5. Relation to prior routes

This is not the Phase 72 RFBD/LM8/XNEG majorant route.  The old route tried
to control the negative part of a large relative Feshbach operator through
Green cycles.  Here the finite CCM/Feshbach local action has already removed
two of the five critical directions, leaving only three scalar Cauchy forms.

The theorem still contains the arithmetic difficulty, but it is now a
small-dimensional spectral Cauchy cancellation statement rather than a
large-dimensional positivity or cycle estimate.

## 6. Status

```text
proved:   QG equals the l2 norm of three explicit scalar forms;
verified: the form map has operator norm 1 in the finite harness;
open:     prove QG-LF from the finite CCM/Feshbach eigenline equation.
```
