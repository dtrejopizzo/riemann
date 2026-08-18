# D.222 — Directed finite Green capacity on the orthogonal band \(200{:}260\)

## Verdict

At \(T=\frac12\log6\), let \(S\) be the \(196\)-dimensional old safe
space of D.220--D.221 and let

\[
 W=(V_{260}^{\rm prim})\ominus(V_{200}^{\rm prim}).
\]

The complete Gamma/contact operator, both Tate equations and the
orthogonality defining \(W\) have been rebuilt in Arb.  If

\[
 B=S^*A_TS,\qquad E=W^*A_TW,\qquad C=S^*A_TW,
\]

then the finite Galerkin Green satisfies

\[
 \boxed{CE^{-1}C^*\le0.09\,B.}                       \tag{0.1}
\]

Equation (0.1) is **CERTIFIED BY INTERVALS**.  The scalar-gap replacement
on the same band gives a diagnostic constant about \(1.4486\), whereas the
exact finite Green has centre constant about \(0.08424\).  Thus retaining
the operator-valued Green is not merely a formal refinement: it pays almost
all of the apparent raw band load.

Combining (0.1) with D.210--D.211 reduces the remaining safe-capacity target
\(\rho_6\le0.7\) to the corrected residual inequality

\[
 \boxed{R_W^*R_W\le0.134139\,B,}                     \tag{0.2}
\]

where

\[
 0.134139=(0.7-0.09)\,0.2199.
\]

The residual in (0.2) is the Galerkin-corrected residual, not the raw
safe-to-tail coupling.  Equation (0.2) remains **OPEN**.

## 1. Orthogonal primitive trial space

Write \(M_{200}\) for the two Tate moments restricted to \(V_{200}\).
The orthogonal complement of \(\ker M_{200}\) inside \(V_{200}\) is

\[
 \operatorname{Ran}M_{200}^*
 =\operatorname{span}\{g_+,g_-\},
\]

where \(g_\pm\) are the two finite Tate representers.  For each high
Legendre vector \(e_n\), \(200\le n<260\), solve

\[
 \begin{pmatrix}
 \langle g_+,g_+\rangle&\langle g_+,g_-\rangle\\
 \langle g_-,g_+\rangle&\langle g_-,g_-\rangle
 \end{pmatrix}
 \binom{a_n}{b_n}
 =
 -\binom{M_+(e_n)}{M_-(e_n)}
                                                        \tag{1.1}
\]

and put

\[
 w_n=e_n+a_ng_++b_ng_- .                              \tag{1.2}
\]

Then \(M_\pm(w_n)=0\), and \(w_n\) is orthogonal to every vector in
\(V_{200}^{\rm prim}\).  The sixty vectors (1.2) therefore span precisely

\[
 W=(V_{260}^{\rm prim})\ominus(V_{200}^{\rm prim}).
\]

The Arb construction verifies simultaneously

\[
 M_\pm W=0,\qquad (V_{200}^{\rm prim})^*W=0
\]

as interval inclusions containing the zero matrices.  This corrects the
oblique high-mode frame that was sufficient for earlier diagnostics but
was not correctly typed for the D.210 orthogonal Green decomposition.

## 2. Directed block construction

The old frame is selected from the centre eigensystem and its two Tate
equations are then solved again in Arb.  Its last \(196\) columns give
\(S\).  The complete \(260\times260\) operator is loaded from the native
Gamma and contact balls and includes:

* the full archimedean Gamma block;
* the scalar \(m_0\);
* the contacts \(2,3,4,5\), with the contact at \(4\) weighted by
  \(\Lambda(4)/2\);
* the exact two-Tate primitive constraints.

The three directed matrices \(B,E,C\) are then formed without binary64
operator entries.  Frozen midpoint Cholesky factors are used only as
congruences.  Arb Gershgorin proves:

\[
 B>0,\qquad E>0,
\]

with whitened lower margins respectively

\[
 0.9999999999999996517\ldots,\qquad
 0.9999999999999991808\ldots .
\]

Finally, a third frozen congruence applied to

\[
 0.09B-CE^{-1}C^*
\]

has directed Gershgorin lower margin

\[
 1-5.07\,10^{-15}>0.
\]

This proves (0.1).  No sampled spectrum or pseudoinverse is used in the
certificate.

## 3. Exact residual reduction

Let \(Q=(V_{200}^{\rm prim})^\perp\) and decompose \(Q=W\oplus Z\).  In
the notation of D.210, the exact Green identity is

\[
 C_SA_{QQ}^{-1}C_S^*
 =CE^{-1}C^*+R_W^*\Sigma_W^{-1}R_W.                 \tag{3.1}
\]

D.185 gives

\[
 A_{QQ}\ge0.2199I.
\]

The gap-preservation theorem of D.211 therefore gives

\[
 \Sigma_W\ge0.2199I_Z.                               \tag{3.2}
\]

Using (0.1)--(3.2),

\[
 C_SA_{QQ}^{-1}C_S^*
 \le0.09B+0.2199^{-1}R_W^*R_W.                     \tag{3.3}
\]

Consequently (0.2) implies

\[
 C_SA_{QQ}^{-1}C_S^*\le(0.09+0.61)B=0.7B,
\]

which is exactly the missing hypothesis of D.221.  Thus the remaining
endpoint work is no longer a \(196\)-dimensional Green inversion.  It is a
source estimate for the corrected residual \(R_W\).

## 4. Reproduction

    PYTHONPATH=/tmp/rowd-flint D222_DPS=120 \
    python3 114_d_222_t6_finite_green_capacity_arb.py

The run exits with code zero and prints

    D222 DIRECTED FINITE GREEN CAPACITY rho<=0.09: PASS

The generated artifact is

    /tmp/t6_finite_green_capacity_rho009_arb.npz

and has SHA-256

    8aca29f74432b3945b7ba9ca3a6de96f28cd7c35a37df40923aff6e828a00b53

## 5. Classification

* construction of the orthogonal primitive band \(W\): **PROVED**;
* positivity of \(B\) and \(E\): **CERTIFIED BY INTERVALS**;
* finite Green bound (0.1): **CERTIFIED BY INTERVALS**;
* exact residual identity (3.1): **PROVED OPERATOR IDENTITY** in D.210;
* preservation of the \(0.2199\) gap in (3.2): **PROVED** in D.211;
* reduction to (0.2): **PROVED**;
* corrected residual bound (0.2): **OPEN**;
* full endpoint and global row D: **OPEN**.
