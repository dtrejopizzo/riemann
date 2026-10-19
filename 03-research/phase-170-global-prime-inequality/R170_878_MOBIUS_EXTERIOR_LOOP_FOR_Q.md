# R170_878 — The causal Tate predictor is a Möbius exterior loop

> **Truncation correction.** `L=MK` holds for the full combs.
> In PC one uses `L_M`; although `M>=e^(2T)` stabilizes the interior
> block, the tail `L-L_M` still acts on `Q`. The corrected formulas of §3
> keep that tail. The loop identity (0.4) does not change.

> **Finite comb correction (R170_884).** In R170_853 the predictor
> uses `S_N`, not the full comb `S`. The interior compression is
> stabilized for `N>=e^(2T)`, but the exterior port is not. Hence (0.4)
> must include the tail `U_N=S-S_N`, as in (0.4c) below. The successor
> pointwise formulas must restrict the intermediate divisor to `n<=N`.

## 0. Result

The exterior vector

\[
 q_N=QS_N^*Ph,\qquad h=(PS_N^*P)^{-1}b,                  \tag{0.1}
\]

of R170_853 admits a purely arithmetic representation. Let

\[
 M=\sum_{n\ge1}{\mu(n)\over\sqrt n}\tau_{\log n},
 \qquad MS=SM=I.                                          \tag{0.2}
\]

For `N>=e^(2T)`, R170_850 and adjunction give

\[
 (PS_N^*P)^{-1}=PM^*P.                                    \tag{0.3}
\]

The direct formula is

\[
 \boxed{q_N=QS_N^*PM^*Pb.}                               \tag{0.4a}
\]

Set `U_N=S-S_N`. From `S^*M^*=I` one obtains

\[
\boxed{
 q_N=-QS_N^*QM^*Pb-QU_N^*M^*Pb.}                         \tag{0.4b}
\]

Thus the causal predictor does not contain an assumed exterior
reciprocity: it is the loop that leaves the window through the Möbius
comb and is observed with the finite comb, with its tail `U_N` kept
separately.

## 1. Proof

By (0.3),

\[
 h=PM^*Pb.                                                 \tag{1.1}
\]

Since `b` is in the window, `Pb=b`. Applying `Q` to
`S^*M^*Pb=Pb`, and writing `S=S_N+U_N`, gives

\[
 0=Q(S_N^*+U_N^*)M^*Pb
   =q_N+QS_N^*QM^*Pb+QU_N^*M^*Pb.                         \tag{1.2}
\]

Solving for `q_N` proves (0.4b).
`P` was not moved across `S` or `M` and no exterior route was discarded.

## 2. Frozen derivative

The convention of R170_853 keeps `P,h,b` fixed when differentiating the scale
of `S`. Hence

\[
 \boxed{\dot q_N^{\,0}=Q\dot S_N^*PM^*Pb.}                \tag{2.1}
\]

One must not differentiate (0.4) as if `M`, `h`, and the compressed
inverse also moved. Doing so would produce a different connection. If
that full connection is wanted, the identity

\[
 \dot S^*M^*+S^*\dot M^*=0                               \tag{2.2}
\]

must be added explicitly.

With the frozen convention, the Wronskian of R170_853 becomes

\[
\boxed{
 \mathfrak W_{\rm ext}(F)
 =(Q\dot S_N^*PM^*Pb,z_F)
 -(q_N,\dot z_F^{\,0}).}                                  \tag{2.3}
\]

All products are real, or one takes their real part.

## 3. Inserting unique factorization

The Dirichlet identity

\[
 \Lambda=\mu*\log                                        \tag{3.1}
\]

gives, for the full causally oriented combs,

\[
 L=MK,\qquad
 K=\sum_{n\ge1}{\log n\over\sqrt n}\tau_{\log n}.         \tag{3.2}
\]

Define the exact tail of the Euler cutoff

\[
 R_M:=L-L_M
 =\sum_{n>M}{\Lambda(n)\over\sqrt n}\tau_{\log n}.         \tag{3.3}
\]

Hence the physical exterior

\[
 \ell_F=QA_M F
 =Q\bigl(\mathcal M-L_M-L_M^*\bigr)F                     \tag{3.4}
\]

can be written as

\[
 \boxed{
 \ell_F=Q\mathcal MF-QMKF-QK^*M^*F
        +Q(R_M+R_M^*)F.}                                  \tag{3.5}
\]

Together with (0.4),

\[
\boxed{
 z_F=Q\mathcal MF-QMKF-QK^*M^*F+Q(R_M+R_M^*)F
      +\rho_FQS^*QM^*Pb.}                                  \tag{3.6}
\]

Equations (2.3) and (3.6) express the open law entirely in terms of
the Gamma operator, the comb of all integers, its Möbius inverse, and
the column `log`, together with the explicit tail `R_M`. The values of
`Lambda` were not replaced by a qualitative property: they enter via
the exact equality (3.1).

## 4. What it reduces and what it does not

The formula eliminates two apparent freedoms:

1. `q` is not an arbitrary exterior lift; it is the loop (0.4);
2. the prime part of `z_F` is not independent of `S`; it is tied to its
   inverse via (3.2), without discarding the tail `R_M`.

However, (2.3) is still an alternating form between two different
exterior vectors. Möbius factorization gives it no sign. In
particular, separating the terms of (3.6) and estimating them would lose
the doubly exponentially small cancellations required by Theorem M.

The next admissible identity must act on the full expression
(2.3)--(3.6), together with the polar term of R170_856. One concrete
candidate is to prove that the vector of (3.6) belongs to the closed range
of the same loop `QS^*QM^*P` with a preimage controlled by the
first-contact equation. That membership is not proved and must not be
assumed.

## 5. Status

```text
adjoint inverse (PS*P)^-1 = PM*P                          PROVED
finite representation q_N=QS_N*PM*Pb                      PROVED
loop decomposition with tail U_N                          PROVED
frozen derivative dot q                                   PROVED
exterior Wronskian in Q/Möbius blocks                     PROVED
L=MK via Lambda=mu*log                                    PROVED
fully arithmetic formula for z_F                          PROVED
exterior tail R_M                                         KEPT
sign or vanishing of (2.3)                                OPEN
VIR--LB / D                                               OPEN
```
