# R170_894 — Polar moment residual and the moving face

## 0. Doubly audited result

The polar scalar law of R170_893 can be fully expanded. Its
interior terms are elementary moments; the remaining information lies in
two truncated exterior moments and in the moving face `t+log N`.

Suppose `N>=e^(2T)`. For `f` supported on `I=[-T,T]`, define

\[
 \alpha(f)=\int_I e^{u/2}f(u)du,\qquad
 \beta(f)=\int_I u e^{u/2}f(u)du,                         \tag{0.1}
\]

and for `h`

\[
 H_0=\int_I e^{-t/2}h(t)dt,\qquad
 H_1=\int_I t e^{-t/2}h(t)dt.                            \tag{0.2}
\]

Then

\[
 (h,PC_Nf)=H_0\alpha(f),                                 \tag{0.3}
\]

\[
 (h,P\dot C_Nf)
 =(H_0-H_1/2)\alpha(f)+(H_0/2)\beta(f).                  \tag{0.4}
\]

## 1. Proof of the interior moments

On the window, the hypothesis on `N` gives

\[
 C_Nf(t)=e^{-t/2}\alpha(f).                              \tag{1.1}
\]

The exact formula R170_856(9.3) reduces to

\[
 \dot C_Nf(t)=e^{-t/2}\left[
 (1-t/2)\alpha(f)+\beta(f)/2\right],                     \tag{1.2}
\]

because the face `f(t+log N)` falls outside the support except for a
measure-zero trace at the threshold. Pairing (1.1)--(1.2) with `h` proves
(0.3)--(0.4).

## 2. Exterior moments

For an exterior vector `v`, set

\[
 J_0[v](t)=\int_{-\infty}^{t+\log N}e^{u/2}v(u)du,
\qquad
 J_1[v](t)=\int_{-\infty}^{t+\log N}u e^{u/2}v(u)du.     \tag{2.1}
\]

Define

\[
 \mathsf X_N(v)=\int_I h(t)e^{-t/2}J_0[v](t)dt,           \tag{2.2}
\]

\[
\boxed{
\begin{aligned}
 \mathsf D_N(v)=\int_I h(t)e^{-t/2}\big[&
 (1-t/2)J_0[v](t)+J_1[v](t)/2\\
 &-(\log N)\sqrt N\,v(t+\log N)\big]dt.
\end{aligned}}                                           \tag{2.3}
\]

Hence

\[
 (h,PC_Nv)=\mathsf X_N(v),\qquad
 (h,P\dot C_Nv)=\mathsf D_N(v).                          \tag{2.4}
\]

The last line of (2.3) is the moving face. It cannot be discarded by
a support estimate.

## 3. Minimal polar residue

Write

\[
 u=P\dot A_MF,\qquad v=Q\dot A_MF,\qquad
 \ell=QA_MF,\qquad PA_MF=\rho b.                         \tag{3.1}
\]

R170_893(0.5) is exactly equivalent to

\[
\boxed{
\begin{aligned}
 \mathfrak R_{\rm pol}(F):={}&
 H_0\alpha(u)+\mathsf X_N(v)\\
 &-\rho\big[(H_0-H_1/2)\alpha(b)+(H_0/2)\beta(b)\big]\\
 &-\mathsf D_N(\ell)
 -\rho\big[(P\dot S_N^*Ph,b)-\|b\|^2\big]=0.
\end{aligned}}                                           \tag{3.2}
\]

In one parity some interior moments can be simplified using
reflection. However,

\[
 \mathsf X_N(Q\dot A_MF),\qquad
 \mathsf D_N(QA_MF)                                    \tag{3.3}
\]

remain. These are the two exterior data that the interior equation
`PA_MF=rho b` does not determine.

## 4. Abstract independence and scope

Keep `b,h,S_N,dot S_N,rho` and the interior datum
`PA_MF=rho b` fixed. In an abstract decomposition `P+Q=I`, the exterior
block `Q dot A F` can be varied in a direction `v` with
`X_N(v) ne 0`, preserving the interior datum. The discrete side of (3.2)
does not change, and the polar side does.

This proves that first contact and the projections, in isolation, do not imply
(3.2). It is not a counterexample to the zeta operator: a valid proof must
use an additional PC relation that simultaneously ties the two moments
of (3.3) to the exact discrete normalization.

The PC expansion can rewrite those moments, but doing so linearly
reproduces the ledger; the new law must act on the moving face and the
exterior routes before recombining them.

## 5. Status

```text
interior moments of C_N and dot C_N                         PROVED
exterior moments X_N and D_N                                 PROVED
minimal polar residue (3.2)                                  PROVED
interior first contact implies R_pol=0                        REFUTED IN THE ABSTRACT
arithmetic identity for the moving face in (3.3)               OPEN
polar normalization / covariant vanishing                      OPEN
VIR--LB / D                                                     OPEN
```
