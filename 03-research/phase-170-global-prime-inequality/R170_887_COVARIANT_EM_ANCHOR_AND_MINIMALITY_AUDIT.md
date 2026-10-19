# R170_887 — Covariant EM anchor and minimality audit

## 0. Result

R170_885--886 correctly compute the antidiagonal jet with `P,h,F`
frozen. A comparison with the first-contact spectral branch must
add the motion of these three objects.

Let a `C1` family be

\[
 e_s:=Q_sS_{N,s}^*h_s-C_{N,s}^*h_s,
 \qquad Q_s=I-P_s,                                       \tag{0.1}
\]

and let `F_s` be a normalized branch. At `s=0`,

\[
\boxed{
 {d e_s\over ds}=\dot e_{\rm fr}+\chi_e,}                \tag{0.2}
\]

where

\[
 \dot e_{\rm fr}=Q\dot S_N^*h-\dot C_N^*h,              \tag{0.3}
\]

\[
\boxed{
 \chi_e=-\dot P S_N^*h+(QS_N^*-C_N^*)\dot h.}           \tag{0.4}
\]

Consequently, the covariant Wronskian of the branch is

\[
\boxed{
 \mathfrak W_{\rm cov}(F)
 =W_{\rm fr}(e_{\rm EM},A_MF)
  +(\chi_e,A_MF)-(e_{\rm EM},A_M\dot F).}                \tag{0.5}
\]

The first term is exactly R170_886(0.2). The other two are the
missing connection needed to compare with minimality. They have no sign fixed
by the eigenvalue slope.

Equivalently, using `dot F=Pi dot F+dot Pi F`, the last correction
of (0.5) splits as

\[
 -(e_{\rm EM},A_M\Pi\dot F)
 -(e_{\rm EM},A_M(\dot P-\dot R_T)F).                    \tag{0.6}
\]

In the fixed ambient trivialization (`Gamma=0`), (0.5)--(0.6) are the
correct formulas with ordinary derivatives. Under a moving trivialization,
the ordinary Wronskian is not invariant: the metric covariant derivative
of §2.1 must be used.

## 1. Exact derivative of the anchor

Differentiating (0.1) and using `dot Q=-dot P` gives

\[
\begin{aligned}
 {d e_s\over ds}\bigg|_0={}&
 -\dot P S_N^*h+Q\dot S_N^*h+QS_N^*\dot h\\
 &-\dot C_N^*h-C_N^*\dot h,
\end{aligned}                                             \tag{1.1}
\]

which is (0.2)--(0.4). This formula keeps `S_N`; replacing it with `S`
would again lose the exterior tail `U_N`.

The causal dual satisfies

\[
 B_sh_s=b_s,\qquad B_s=P_sS_{N,s}^*P_s,\qquad P_sh_s=h_s.\tag{1.2}
\]

Its derivative is determined by

\[
\boxed{
 P\dot h=B^{-1}P(\dot b-\dot B\,h),
 \qquad Q\dot h=\dot P\,h,}                            \tag{1.3}
\]

\[
 \dot B=\dot P S_N^*P+P\dot S_N^*P+PS_N^*\dot P.         \tag{1.4}
\]

Hence `chi_e` is not a free term: it is fixed by the motion of
the window, the finite comb, and the Tate column.

## 2. Proof of the covariant Wronskian

The total derivative of the second argument is

\[
 {d\over ds}(A_{M,s}F_s)|_0=\dot A_MF+A_M\dot F.          \tag{2.1}
\]

Inserting (0.2) and (2.1) into

\[
 \left({de_s\over ds},A_MF\right)
 -\left(e_{\rm EM},{d\over ds}(A_{M,s}F_s)\right)         \tag{2.2}
\]

separates the frozen jet

\[
 (\dot e_{\rm fr},A_MF)-(e_{\rm EM},\dot A_MF)           \tag{2.3}
\]

from the two connection terms of (0.5). This proves the formula without
choosing a gauge for `dot F`.

### 2.1. Gauge correction

Let

\[
 \nabla_s=\partial_s+\Gamma_s,
 \qquad \Gamma_s^*=-\Gamma_s.                            \tag{2.4}
\]

If `v'=U_sv`, the connection transforms as

\[
 \Gamma'=U\Gamma U^*-\dot U U^*,                         \tag{2.5}
\]

so that `nabla'(Uv)=U nabla v`. The invariant quantity is

\[
\boxed{
 W_\nabla(e,A_MF)
 :=(\nabla e,A_MF)-(e,\nabla(A_MF)).}                     \tag{2.6}
\]

For operators, `nabla A=dot A+[Gamma,A]`, and likewise for the
projections. Formulas (0.2)--(1.4) correspond to `Gamma=0`; they are
covariantized by consistently replacing all derivatives.

## 3. Exact minimality equation

Let `Pi_s` be the projection onto the primitive fiber, and assume REG/C1:

\[
 \Pi_sA_s\Pi_sF_s=\lambda_sF_s,\qquad
 \Pi_sF_s=F_s,\qquad \|F_s\|=1.                          \tag{3.1}
\]

At first contact `lambda_0=0`, and the Hellmann--Feynman derivative
with a moving subspace is

\[
\boxed{
 \nu:=\dot\lambda_0
 =\operatorname{Re}(F,\dot A F)
  +2\operatorname{Re}(AF,\dot\Pi F)\le0.}                \tag{3.2}
\]

Since `Pi=P-R_T`, the connection is

\[
 \dot\Pi=\dot P-\dot R_T.                                \tag{3.3}
\]

In a dilation gauge with fixed window, `dot P` is absorbed into
`dot A` and into the boundary atoms, but the Tate term
`-2 Re(AF,dot R_T F)` remains. Omitting it changes the physical derivative.

Equations (0.2)--(3.3) require REG/C1 and fixed cutoffs `M,N` within
a chamber, i.e. away from a threshold `e^(2T)=p^k`. At a threshold the
collar's birth term must be kept; it cannot be hidden
in `dot A`.

Normalization only gives `Re(F,dot F)=0`. The Kato equation fixes the
transversal part of `dot F` via the reduced resolvent and leaves a
rotation within a multiple radical, exactly as in R170_857.

## 4. Parity no-go

The quantity `nu` of (3.2) is quadratic:

\[
 \nu(-F)=\nu(F).                                         \tag{4.1}
\]

By contrast, both the frozen Wronskian and its full covariant completion
are linear when the branch `F_s` is jointly changed to `-F_s`:

\[
 \mathfrak W_{\rm cov}(-F)=-\mathfrak W_{\rm cov}(F).    \tag{4.2}
\]

Hence minimality cannot identify
`mathfrak W_cov(F)` with `nu(F)` nor assign it a one-sided sign. Such an
identification is only possible after proving
`mathfrak W_cov(F)=0`, which is exactly the missing law.

## 5. Consequence for the construction

The frozen range equation of R170_886 must be replaced, when using
minimality, by a covariant law that simultaneously annihilates

\[
\boxed{
 (\omega_{\rm EM},F)
 +(\chi_e,A_MF)-(e_{\rm EM},A_M\dot F).}                 \tag{5.1}
\]

The first part contains the exact discrete--continuous incidence; the
other two connect that incidence to the moving geometry of first
contact. Linear PC computes the first, and Kato computes `dot F`, but
neither identity alone annihilates their sum.

The next law must act on (5.1) as a covariant cocycle. A
factorization of `omega_EM` by `H_T` alone would omit precisely the
connection that can link the odd arithmetic to the selected branch.

## 6. Status

```text
total derivative of the EM anchor                           PROVED
equation for dot h                                            PROVED
total Wronskian (0.5) in fixed ambient gauge                   PROVED ON THE CORE
gauge-invariant Wronskian W_nabla, (2.6)                       PROVED
minimal derivative with dotPi/dotR_T                            PROVED UNDER REG/C1
minimality assigns a sign to the linear functional             REFUTED BY PARITY
frozen range equation suffices for a moving branch               FALSE WITHOUT CONNECTION
covariant vanishing law (5.1)                                    OPEN
differential version at thresholds without a birth term           NOT AUTHORIZED
VIR--LB / D                                                       OPEN
```
