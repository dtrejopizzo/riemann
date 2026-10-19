# R170_885 — Exact Euler--Maclaurin Wronskian port

## 0. Main identity

Define

\[
 W(u,v):=(\dot u,v)-(u,\dot v),\qquad
 h=(PS_N^*P)^{-1}b,
\]

\[
 q_N=QS_N^*h,quad \ell=QA_MF,quad r=PA_MF,quad
 p=C_N^*h,quad Z_N=S_N-C_N.                              \tag{0.1}
\]

On the common core, the sum of the exterior Wronskian and the polar
port satisfies the exact identity

\[
\boxed{
 \mathfrak W_{\rm ext}+(h,P\mathcal P_{C,A_M}F)
 =W(QZ_N^*h,\ell)-W(PC_N^*h,r).}                          \tag{0.2}
\]

The projection is not commuted with a synthesis operator. The formula is
obtained before separating the arithmetic coefficients.

## 1. Algebraic proof

The ledger of R170_853 gives `W_ext=W(q_N,ell)`; the `rho` terms
cancel in the alternating form. By R170_884,

\[
 (h,P\mathcal P_{C,A_M}F)
 =(p,\dot A_MF)-(\dot p,A_MF)=-W(p,A_MF).                 \tag{1.1}
\]

Since `A_MF=r+ell` and `P,Q` are fixed orthogonal projections,

\[
 W(p,A_MF)=W(Pp,r)+W(Qp,\ell).                            \tag{1.2}
\]

Subtracting (1.2) from `W(q_N,ell)` and using
`q_N-Qp=Q(S_N^*-C_N^*)h=QZ_N^*h` proves (0.2).

## 2. Discrete--continuous disintegration

Let

\[
 m_N^d(k,t)=\sum_{\substack{n\mid k\\n\le N\\
                  |t-\log n|\le T}}\mu(k/n),             \tag{2.1}
\]

\[
 c_N(y,t)=\sum_{\substack{m\ge1\\y/m\le N\\
                  |t-\log(y/m)|\le T}}{\mu(m)\over m}.   \tag{2.2}
\]

Then

\[
\boxed{
\begin{aligned}
 QZ_N^*h=Q\bigg[&\sum_k {b(t-\log k)\over\sqrt k}m_N^d(k,t)\\
 &-\int_0^\infty {b(t-\log y)\over\sqrt y}c_N(y,t)\,dy
 \bigg].
\end{aligned}}                                           \tag{2.3}
\]

For the logarithmic incidences

\[
 l_N^d(k,t)=\sum_{\substack{n\mid k\\n\le N\\
                  |t-\log n|\le T}}\mu(k/n)\log n,       \tag{2.4}
\]

\[
 l_N^c(y,t)=\sum_{\substack{m\ge1\\y/m\le N\\
                  |t-\log(y/m)|\le T}}
                  {\mu(m)\over m}\log(y/m),              \tag{2.5}
\]

the frozen derivative is

\[
\boxed{
 \dot{(QZ_N^*h)}=Q\partial_t\bigg[
 \sum_k {b(t-\log k)\over\sqrt k}l_N^d(k,t)
 -\int_0^\infty {b(t-\log y)\over\sqrt y}l_N^c(y,t)dy
 \bigg].}                                                \tag{2.6}
\]

All derivatives are distributional for the extensions by zero.

## 3. Exact separation of the prime channel

Set

\[
 (\mathcal E_{N,T}b)(t)=
 \sum_k {b(t-\log k)\over\sqrt k}\mathfrak e_{N;T,t}(k),
\]

\[
 (\mathcal L^{\rm cont}_{N,T}b)(t)=
 \int_0^\infty {b(t-\log y)\over\sqrt y}l_N^c(y,t)dy.
\]

Since `l_N^d=Lambda+e_(N;T)` and `L^*=L_M^*+R_M^*`, (2.6) becomes

\[
\boxed{
 \dot{(QZ_N^*h)}=Q\partial_t\left[
 L_M^*b+R_M^*b+\mathcal E_{N,T}b
 -\mathcal L^{\rm cont}_{N,T}b\right].}                  \tag{3.1}
\]

This is the exact discrete--continuous Euler--Maclaurin law. The comb
tail `U_N` is encoded in `e_(N;T)` and the prime tail `R_M` appears
separately.

## 4. Falsifier of the algebraic closure

The defect `Z_N` has atoms at the integers `n<=N` and an
absolutely continuous part. It cannot be the zero measure: the atom `n=1`
has no atomic counterpart. In the Mellin variable, its model multiplier

\[
 \sum_{n\le N}n^{-s}-{N^{1-s}\over1-s}                   \tag{4.1}
\]

is not identically zero. After Möbius, the discrete part uses
`mu(k/n)` over `n|k`, while the continuous part uses `mu(m)/m` over `y`.
Hence (0.2) cannot be closed by coefficient-by-coefficient
cancellation nor by setting `Z_N=0`.

There is an even more direct spatial falsifier. On the left exterior
`t<-T`, the causal comb gives `QS_N^*h(t)=0`, while, for `N>=1`,

\[
 C_N^*h(t)=e^{t/2}\int_{-T}^{T}e^{-u/2}h(u)\,du,           \tag{4.2}
\]

which generally does not vanish. Hence `QZ_N^*h=-QC_N^*h` in that region.

## 5. New minimal door

What remains after identifying the channel `L_M^*` is the
Wronskian of the Euler--Maclaurin renormalized predictor, together with

\[
 -W(PC_N^*h,r),                                          \tag{5.1}
\]

the contributions of `R_M` inside `ell` and its velocity. The next
theorem must orient this form **on the first-contact vector**.
Euler--Maclaurin and linear PC alone do not do this; sending `N` to
infinity without using minimality reproduces the exterior tautology
already audited in phase 161.

More explicitly, defining `D_EM^0 b` as the bracket of (2.3), the
residue after extracting the main channel contains exactly

\[
\begin{aligned}
 \mathfrak R_{\rm EM}(F)={}&
 \left(Q\partial_t[R_M^*b+\mathcal E_{N,T}b
       -\mathcal L^{\rm cont}_{N,T}b],\ell\right)\\
 &-\left(Q\mathcal D_{\rm EM}^0b,\dot\ell\right)
 -W(PC_N^*h,r),                                          \tag{5.2}
\end{aligned}
\]

with

\[
 \ell=\ell_\infty+Q(R_M+R_M^*)F,
 \qquad
 \dot\ell=\dot\ell_\infty+Q(\dot R_M+\dot R_M^*)F.     \tag{5.3}
\]

Equations (5.2)--(5.3) are the object that minimality must sign;
no such sign is declared here.

## 6. Status

```text
polar coupling before disintegration                        PROVED
S_N-C_N as Euler--Maclaurin predictor                        PROVED
discrete--continuous disintegration                           PROVED
separation Lambda + e_N + R_M - continuum                      PROVED
algebraic vanishing of the renormalized predictor              REFUTED
sign of (0.2) via first-contact minimality                     OPEN
VIR--LB / D                                                     OPEN
```
