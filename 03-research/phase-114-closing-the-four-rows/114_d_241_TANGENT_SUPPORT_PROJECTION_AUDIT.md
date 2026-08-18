# D.241 — Tangent support projection and the wrong second-order budget

## Verdict

D.240 permits a precise enlargement in which the D.190 commutator is the
tangent block of an actual orthogonal projection.  This partially realizes
the two-projection idea, but the exact projection identity pays a
second-order angle budget, not the first-order born budget in the sharp
Douglas inequality.  Therefore it does not close row D by itself.

Let \(G_\sigma>0\) be a differentiable metric and fix
\(\sigma_0\).  Trivialize so that \(G_{\sigma_0}=I\), and put

\[
 H=G_{\sigma_0}^{-1/2}\dot G_{\sigma_0}
   G_{\sigma_0}^{-1/2}=\dot G_{\sigma_0}.            \tag{0.1}
\]

For a fixed support projection \(P\), let \(\mathsf P_\sigma\) be the
ordinary orthogonal projection onto

\[
 G_\sigma^{1/2}P\mathcal H.                          \tag{0.2}
\]

Then

\[
 \boxed{
 (I-P)\dot{\mathsf P}_{\sigma_0}P
 ={1\over2}(I-P)HP,
 \qquad
 P\dot{\mathsf P}_{\sigma_0}(I-P)
 ={1\over2}PH(I-P).
 }                                                     \tag{0.3}
\]

For the semilocal metric of D.240, \(H=Q_T\) after support and Tate
compression.  Hence the D.190 raw boundary block is twice a subblock of
the tangent support projection:

\[
 \boxed{
 P_OQ_TP_E
 =2P_O\dot{\mathsf P}_{\sigma_0}P_E,
 \qquad P_E\le I-P_O.
 }                                                     \tag{0.4}
\]

Thus \(Q_T\) is not a projection, but its support commutator has an exact
projection dilation at the infinitesimal level.

The obstruction is equally exact.  The two-projection identity for
\((P,\mathsf P_{\sigma_0+h})\) gives, to second order,

\[
 \boxed{
 P\mathsf P_{\sigma_0+h}(I-P)
 \mathsf P_{\sigma_0+h}P
 ={h^2\over4}PH(I-P)HP+O(h^3).
 }                                                     \tag{0.5}
\]

The matching diagonal defect is

\[
 P\mathsf P_{\sigma_0+h}P-
 (P\mathsf P_{\sigma_0+h}P)^2
 ={h^2\over4}PH(I-P)HP+O(h^3).                      \tag{0.6}
\]

Equations (0.5)--(0.6) pay the Fisher/angle Gram of the boundary coupling.
D.190 instead requires

\[
 (P_OQ_TP_E)^*A_O^\dagger(P_OQ_TP_E)\le B_E,        \tag{0.7}
\]

where \(A_O=P_OQ_TP_O\) and \(B_E=P_EQ_TP_E\) are
**first derivatives** of the semilocal metric.  No identity between the
second-order angle defect (0.6) and the first-order forms \(A_O,B_E\)
follows from \(G_\sigma>0\).

The exact remaining residual is therefore the difference between the
first-order born score and the old-score Green of the tangent angle:

\[
 \boxed{
 \mathscr R_E
 =B_E-(P_OHP_E)^*(P_OHP_O)^\dagger(P_OHP_E).
 }                                                     \tag{0.8}
\]

This is precisely the D.190 Schur residual.  The projection dilation
reconstructs its cross Gram but supplies no sign for (0.8).

## 1. Derivative of the metric support projection

Write

\[
 G_{\sigma_0+h}^{1/2}=I+{h\over2}H+O(h^2)           \tag{1.1}
\]

in operator norm on a finite-energy regularization; the closed-form
statement follows on the common form core.  The range (0.2) is the graph
over \(P\mathcal H\) of

\[
 K_h={h\over2}(I-P)HP+O(h^2).                       \tag{1.2}
\]

The orthogonal projection onto the graph of \(K_h\) is

\[
 \begin{pmatrix}
 (I+K_h^*K_h)^{-1}&(I+K_h^*K_h)^{-1}K_h^*\\
 K_h(I+K_h^*K_h)^{-1}&K_h(I+K_h^*K_h)^{-1}K_h^*
 \end{pmatrix}.                                     \tag{1.3}
\]

Differentiating (1.3) at \(h=0\) proves (0.3).  Multiplying its
off-diagonal blocks and retaining order \(h^2\) proves (0.5).  The exact
two-projection identity

\[
 P\mathsf P(I-P)\mathsf PP
 =P\mathsf PP-(P\mathsf PP)^2                       \tag{1.4}
\]

then proves (0.6).

## 2. A scalar counterexample to the missing implication

The mismatch is not a domain technicality.  On
\(\mathbb C\oplus\mathbb C\), take

\[
 H=\begin{pmatrix}a&c\\\bar c&b\end{pmatrix}.        \tag{2.1}
\]

For sufficiently small \(|h|\), \(G_h=I+hH\) is positive regardless of
the sign of \(ab-|c|^2\).  The tangent projection identities
(0.3)--(0.6) therefore hold for every \(a,b,c\).  But the sharp Douglas
residual is

\[
 b-|c|^2/a                                          \tag{2.2}
\]

when \(a>0\), and can have either sign.  Hence positivity of the ambient
metric path and the exact two-projection conservation law do not imply the
first-derivative Schur sign.

The source-specific theorem must impose additional curvature or
monotonicity on the semilocal metric path.  In the notation of D.240, that
additional assertion is exactly positivity of the localized logarithmic
metric derivative on the primitive space.

## 3. What remains viable

The projection enlargement is still useful because it identifies the
coupling geometrically and fixes its normalization.  A successful theorem
could proceed in either of two ways:

1. prove a semilocal curvature identity expressing (0.8) as a square of a
   second fundamental form plus a nonnegative Sonin term; or
2. prove monotonicity of the weighted support projection in the
   \(\sigma\)-direction after removing the two Tate characters.

Either theorem must use the self-Fourier adelic vectors and must fail for
the Beurling surrogate.  Generic positivity of \(G_\sigma\), the
two-projection identity, or differentiability alone is insufficient.

## 4. Classification

* Semilocal logarithmic metric representation of \(Q_T\): **PROVED** in
  D.240.
* Tangent projection formula (0.3)--(0.4): **PROVED**.
* Second-order two-projection identity (0.5)--(0.6): **PROVED**.
* Equality of the second-order angle budget with the D.190 first-order
  born budget: **FALSE IN GENERAL**, with counterexample (2.1)--(2.2).
* Exact unpaid residual (0.8): **IDENTICAL TO THE SHARP DOUGLAS GATE**.
* Source-specific semilocal curvature/monotonicity theorem: **OPEN**.
* Row D: **OPEN**.
