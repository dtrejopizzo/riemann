# D.165 — Corrected compressed moments for the primitive Weil operator

## Verdict

Let

\[
  A_T=P_T^0M_{r_T}P_T^0
\]

be the exact primitive operator of D.163.  If the columns of (S) belong
to (PW_T^0), then only the first moment can be evaluated by deleting the
Paley--Wiener projections:

\[
 S^*A_TS=S^*M_{r_T}S.                                  \tag{0.1}
\]

For (j\geq2), in general,

\[
 \boxed{S^*A_T^jS\ne S^*M_{r_T}^jS.}                  \tag{0.2}
\]

Thus the directed integrals already obtained for

\[
 {1\over2\pi}\int r_T(\tau)^j
        \widehat{s_a}(\tau)\overline{\widehat{s_b}(\tau)}\,d\tau
\]

are valid ambient multiplier moments, but are not the compressed Krylov
moments required by D.155.  They cannot be used in its Feshbach recursion.
This is a correction to the research route, not to the paper.

The exact replacement is a chain integral with one Tate-deflated
Paley--Wiener kernel between every two multipliers.  This retains all
prime powers and the complete Gamma term and supplies the correct input
for any future moment/Krylov certificate.

## 1. Algebraic correction

Let (P=P_T^0), (M=M_{r_T}), and (PS=S).  Associativity gives

\[
 S^*(PMP)^jS
 =S^*M(PMP)^{j-1}S.                                  \tag{1.1}
\]

For (j=2), this is

\[
 S^*A_T^2S=S^*MPMS,                                  \tag{1.2}
\]

whereas the ambient second moment is (S^*M^2S).  Their difference is

\[
 \boxed{
 S^*M^2S-S^*A_T^2S
 =S^*M(I-P)MS\geq0.}                                 \tag{1.3}
\]

Equality holds precisely when (MS\subseteq\mathrm{Ran}\,P).  A
nonconstant multiplier does not preserve a proper Paley--Wiener space, so
this exceptional condition is not available here.

More generally, the exact compressed moments are

\[
 \boxed{H_j^{\rm comp}=S^*M(PM)^{j-1}S,\qquad j\geq1.} \tag{1.4}
\]

No sign statement is needed for (1.4).

## 2. Exact kernel formula

Use the Fourier normalization in which

\[
 K_T^0(z,w)=K_T(z,w)-k_T(z)\mathsf G_T^{-1}k_T(w)^*
\]

is the primitive reproducing kernel from D.163.  The projection acts by

\[
 (P_T^0G)(\tau)={1\over2\pi}\int_{\mathbb R}
                  K_T^0(\tau,\sigma)G(\sigma)\,d\sigma,              \tag{2.1}
\]

with the harmless normalization factor adjusted together with the chosen
kernel convention.  Consequently

\[
\begin{aligned}
 (H_j^{\rm comp})_{ab}
  ={}&{1\over(2\pi)^j}\int_{\mathbb R^j}
  \overline{\widehat{s_a}(\tau_0)}r_T(\tau_0)
  \prod_{q=0}^{j-2}
   \left[K_T^0(\tau_q,\tau_{q+1})r_T(\tau_{q+1})\right]
  \widehat{s_b}(\tau_{j-1})
  \,d\tau_0\cdots d\tau_{j-1}.                     \tag{2.2}
\end{aligned}
\]

Equivalently, (2.2) may be evaluated recursively by applying the integral
operator (P_T^0M_{r_T}) between directed endpoint-flat columns.  Formula
(2.2) contains the exact multiplier

\[
 r_T(\tau)=\mathrm{Re}\,\psi(1/4+i\tau/2)-\log\pi
 -2\sum_{p^k\le e^{2T}}{\log p\over p^{k/2}}
                      \cos(k\tau\log p),             \tag{2.3}
\]

so neither Gamma nor any Frobenius depth is separated before the
compression.

## 3. Diagnostic supplied by the directed ambient moments

At (T=\frac12\log5), the five-column directed enclosures of D.160--D.164
give a positive first moment, but inserting their ambient (H_2,H_3,H_4)
into the compressed block-path identities produces a matrix called

\[
 M_1=H_3-B^3-BM_0-M_0B
\]

with a negative central eigenvalue (approximately (-7.8\times10^{-3})).
This is not evidence against positivity.  It is the expected failure of
substituting ambient moments into identities derived for (A_T^j).

The ancillary `114_d_165_compressed_moment_verify.py` checks (1.2)--(1.4)
on exact rational finite matrices and exhibits strict inequality in
(1.3).  The failed ambient substitution is therefore removed from the D
route.  The weighted-prolate operator of D.163 and the annular capacity
route remain correctly typed because they use (P_T^0M_{r_T}P_T^0)
itself, not ambient powers.
