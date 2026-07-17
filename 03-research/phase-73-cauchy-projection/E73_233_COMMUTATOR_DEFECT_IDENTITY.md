# E73.233 - Canonical commutator defect identity for U4

Date: 2026-07-14.

## 1. Purpose

E73.232 isolates the remaining uniform arithmetic center cancellation:

```text
U4: |C_a^0(L,N,w)| <= A L^(-M).
```

E73.162 also warns that arbitrary rowspace or pseudoinverse decompositions of
`H_L-mu_L I` are tautological.  This note records a fixed, canonical defect
identity for the TRANS-CELL center.  It uses only:

```text
H_L xi_L = mu_L xi_L,
P_w = Q_w^*(Q_wQ_w^*)^(-1)Q_w,
eta_w=(I-P_w)xi_L,
```

and the prescribed Cauchy row `q_a`.  No choice of spectral projection,
least-squares inverse, or smallness of `h=Q_w xi_L` is used.

## 2. Exact identity

Let `Q=Q_w` be the two-row Cauchy matrix and let

```text
P=Q^*(QQ^*)^(-1)Q
```

be the orthogonal projection onto the Cauchy row plane.  For a fixed row
`q=q_a`, the TRANS-CELL center in matrix form is

```text
C_q = q H_L (I-P) xi_L.                         (1)
```

Define the canonical source and canonical primitive

```text
S_q=(I-P)H_L q^*,
Y_q=(I-P)q^*.
```

Then, since `H_L` and `P` are self-adjoint,

```text
C_q=<S_q,xi_L>.
```

Subtract the fixed image vector `(H_L-mu_L I)Y_q`.  The pairing with `xi_L`
vanishes by the eigen-equation, so

```text
C_q=<D_q,xi_L>,                                  (2)
```

where

```text
D_q
= S_q-(H_L-mu_L I)Y_q
= (I-P)H_Lq^* - H_L(I-P)q^* + mu_L(I-P)q^*
= [I-P,H_L]q^* + mu_L(I-P)q^*.                  (3)
```

This is the canonical commutator defect.

## 3. Why this is not the old tautology

The forbidden move is:

```text
S_q=(H_L-mu_L I)Y + residual
```

with `Y` chosen by free projection onto `xi_L^perp`.  That residual is just the
original scalar obstruction in disguise.

Here `Y_q` is fixed before seeing `xi_L`:

```text
Y_q=(I-P)q^*.
```

Thus the defect is not a fitted projection residual.  It is the explicit
commutator between the CCM/Feshbach operator and the Cauchy projection, plus
the small eigenvalue term:

```text
D_q=[I-P,H_L]q^* + mu_L(I-P)q^*.
```

The remaining proof problem is therefore not generic image membership.  It is
an explicit Cauchy-projection commutator estimate evaluated on the intrinsic
ground vector.

## 4. Sufficient analytic theorem

For every target `M`, it is enough to prove the uniform bound

```text
|<[I-P_w,H_L]q_a^*,xi_L>
 + mu_L <(I-P_w)q_a^*,xi_L>|
<= A_M L^(-M)                                      (CD-U4)
```

for all admissible windows and Cauchy rows.

Then (2) gives U4, and E73.232 gives the finite-frequency TRANS-CELL
certificate once U1--U3 are supplied.

An even stronger, purely operator-style sufficient condition is

```text
||[I-P_w,H_L]q_a^*|| + |mu_L| ||(I-P_w)q_a^*|| <= A_M L^(-M).
```

But this stronger norm form is not required.  The load-bearing statement is
the paired commutator estimate `(CD-U4)`.

## 5. Relation with prior no-go results

This differs from:

```text
E73.065 / E73.162: free rowspace distance       -> tautological if projected;
E73.179 / E73.188: Cauchy-plane eigen branch    -> circular if it uses h small;
E72.283: crude compact-root commutator probe    -> diagnostic scale only.
```

The current identity fixes the primitive `Y_q` algebraically and exposes the
only possible new cancellation channel:

```text
the Cauchy projection nearly commutes with H_L on q_a^*, after pairing with
the CCM ground vector.
```

If `(CD-U4)` cannot be proved without reusing the smallness of `Q_w xi_L`, then
the Phase 73 route has not escaped the old Cauchy-divisor wall.  If it can be
proved from the explicit Gamma/prime cell formula for `[I-P_w,H_L]`, it is a
genuine analytic route to U4.

## 6. Status

```text
proved: exact identity C_q=<D_q,xi_L>;
new target: paired commutator defect estimate CD-U4;
open: prove CD-U4 uniformly from the explicit CCM/Feshbach cell formula.
```

