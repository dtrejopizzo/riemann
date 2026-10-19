# R170_853 — Curvature of the causal graph and arithmetic exterior mismatch

## 0. Result

In the real parity sector (the complex form is obtained by
polarization), the Tate defect of R170_852 can be split into a part
determined by the integer comb and a part that carries all the
exterior information of the Weil operator.

Let

\[
 C_{N,T}:=PS_N^*P,
 \qquad
 \mathcal D_{N,T}:=QS_N^*P\,C_{N,T}^{-1}.                    \tag{0.1}
\]

`C_N,T` is invertible because its adjoint is `PS_NP`, whose finite
inverse was built in R170_849. For the Tate datum `b_epsilon`, define

\[
 h_\epsilon=C_{N,T}^{-1}b_\epsilon,
 \qquad
 q_\epsilon=\mathcal D_{N,T}b_\epsilon=QS_N^*Ph_\epsilon.    \tag{0.2}
\]

If

\[
 PA_MF=\rho_Fb_\epsilon,
 \qquad \ell_F=QA_MF,
\]

the exterior mismatch is

\[
 \boxed{z_F:=\ell_F-\rho_Fq_\epsilon.}                       \tag{0.3}
\]

The quantity `z_F` is the component of the arithmetic exterior not
predicted by the causal extension of the Tate forcing. Vanishing
`z_F=0` is not assumed; it would be a strong exterior reciprocity law.

## 1. The causal graph is explicit

The pair

\[
 (b,\mathcal D_{N,T}b)
\]

is the interior/exterior trace of `S_N^*Ph`, where
`h=C_N,T^{-1}b`. Indeed,

\[
 S_N^*Ph=b+\mathcal D_{N,T}b.                               \tag{1.1}
\]

Thus `Graph(D_N,T)` is not a postulated graph: it is the exact
exterior extension produced by the integer comb and the finite causal
inverse. For `N>=e^(2T)` it depends only on the geometry of the
integers visible in the window.

The derivative holding `h_epsilon` fixed is

\[
 \dot q_\epsilon^{\,0}:=Q\dot S_N^*Ph_\epsilon.              \tag{1.2}
\]

The corresponding interior connection is the scalar

\[
 \kappa_{N,T}^\epsilon
 ={\langle P\dot S_N^*Ph_\epsilon,b_\epsilon\rangle
    \over q_\epsilon^{\rm Gram}},
 \qquad q_\epsilon^{\rm Gram}=\|b_\epsilon\|^2.             \tag{1.3}
\]

These are exactly the two components of
`dot S_N^*Ph_epsilon` under `I=P+Q`.

## 2. Substitution into the Tate defect

R170_852 gives

\[
\begin{aligned}
 q_\epsilon^{\rm Gram}\Delta^{\rm Tate}(F)
={}&(\kappa^\epsilon-1)\rho_Fq_\epsilon^{\rm Gram}\\
 &+\langle\dot q_\epsilon^{\,0},\ell_F\rangle
  -\langle q_\epsilon,Q\dot A_MF\rangle.                    \tag{2.1}
\end{aligned}

Inserting `ell_F=rho_F q_epsilon+z_F`,

\[
\boxed{
\begin{aligned}
 q_\epsilon^{\rm Gram}\Delta^{\rm Tate}(F)
={}&\rho_F\mathfrak K_{N,T}^\epsilon(F)\\
 &+\langle\dot q_\epsilon^{\,0},z_F\rangle
  -\langle q_\epsilon,\dot z_F^{\,0}\rangle,
\end{aligned}}                                               \tag{2.2}
\]

where

\[
 \mathfrak K_{N,T}^\epsilon(F)
 :=(\kappa^\epsilon-1)q_\epsilon^{\rm Gram}
   +\langle\dot q_\epsilon^{\,0},q_\epsilon\rangle
   -\langle q_\epsilon,\dot q_\epsilon^{\,0}\rangle.       \tag{2.3}
\]

The last difference in (2.2) is the exterior velocity that does not
follow the causal graph. If one defines, in the core,

\[
 \dot z_F^{\,0}:=Q\dot A_MF-\rho_F\dot q_\epsilon^{\,0},     \tag{2.4}
\]

then the last two terms are the exterior Wronskian

\[
 \langle\dot q_\epsilon^{\,0},z_F\rangle
 -\langle q_\epsilon,\dot z_F^{\,0}\rangle.                 \tag{2.5}

No derivative of `rho_F` was included: (2.4) is the velocity with the
forcing coefficient frozen, which is the one appearing in the
antidiagonal derivative of R170_847--848. A different gauge must add
its term explicitly.

## 3. Audit of the purely causal part

The quantity `mathfrak K` of (2.3) depends only on `S_N`, the window
and the Tate basis. It can be computed at finite cutoff using
`B=PMP`. It contains no `Lambda`, no Gamma term, and no minimality.
Hence it cannot, by itself, be the law that distinguishes zeta from
the falsifiers.

A universal cancellation of `mathfrak K` with the polar derivative is
possible as a geometric normalization identity. Even if proved, (2.5)
remains, and it does contain `z_F` and `Q dot A_MF`. The irreducible
arithmetic datum therefore lies in the Wronskian between the integer
causal extension and the exterior mismatch of the Weil operator.

## 4. Collision with the earlier exterior reciprocity

R161_022--023 builds the canonical causal pullback of the product
port and proves that pairing it linearly with `AF` recombines in
PC-ren; it does not force its vanishing. R161_064 formulates the
correct concomitant as a mixed power of support.

The vector `z_F` of (0.3) is another coordinate of that same
discrepancy:

* `rho_F q_epsilon` is the exterior predicted from the Tate datum via
  the integer comb;
* `ell_F=Q A_MF` is the physical exterior;
* their difference is exactly the exterior reciprocity not determined
  by the interior radical equation.

Hence imposing `z_F=0`, or imposing that (2.5) vanish without deriving
it from the two-scale PC identity, would repeat L161.6. The novelty
of (2.2) is that it identifies the exact **antidiagonal jet** that
would need to be controlled, not that it already controls it.

## 5. Remaining law in minimal form

After cancelling the causal curvature `mathfrak K` against the
normalized polar term, Tate closure requires

\[
 \boxed{
 \operatorname{Re}\bigl(
  \langle\dot q_\epsilon^{\,0},z_F\rangle
  -\langle q_\epsilon,\dot z_F^{\,0}\rangle
 \bigr)=0}                                                   \tag{5.1}
\]

or a compatible sign that can be absorbed into the Wronskian energy.
Equation (5.1) must come out of the differentiated right-hand side of
PC (4.5) of R170_847, preserving `H_M,N`, `K_N(r,q)` and `C_N`; it
does not come from radicality alone.

## 6. Status

```text
causal extension operator D_N,T                                DEFINED
exterior mismatch z_F                                           DEFINED
exact decomposition of the Tate defect, equation (2.2)          PROVED
isolation of the purely causal curvature K                      PROVED
identification of the residue as exterior Wronskian             PROVED
vanishing z_F=0 by direct pullback                               FORBIDDEN / TAUTOLOGICAL
exterior Wronskian law (5.1) from two-scale PC                   OPEN
VIR--LB / D                                                      OPEN
```
