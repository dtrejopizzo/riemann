# D.243 — The dual-Euler oblique projection and the first-order coupling

## Verdict

The dual Euler conservation law produces a canonical **oblique**
projection whose tangent recovers the D.190 boundary coupling at first
order.  This is better typed than the orthogonal support projection of
D.241, whose conservation law begins at second order.

However, idempotence of the oblique projection imposes no Hilbert-norm
contractivity.  It reconstructs the complete coupling but does not prove
the sharp Douglas sign.  The remaining positive input must therefore be a
source-specific metric property of the adelic oblique projection, not
idempotence alone.

## 1. Canonical transported idempotent

Let \(\eta_\sigma\) and \(\theta_\sigma\) be the dual Euler maps on a
common Hilbert realization, so that

\[
 \theta_\sigma^*\eta_\sigma=I.                     \tag{1.1}
\]

On their common boundedly invertible core this says
\(\theta_\sigma^*=\eta_\sigma^{-1}\).  For an orthogonal support projection
\(P\), define

\[
 \mathsf E_\sigma
 :=\eta_\sigma P\theta_\sigma^*
 =\eta_\sigma P\eta_\sigma^{-1}.                   \tag{1.2}
\]

Then

\[
 \boxed{\mathsf E_\sigma^2=\mathsf E_\sigma}       \tag{1.3}
\]

exactly.  Its range is \(\eta_\sigma(P\mathcal H)\); it is generally not
the orthogonal projection onto that range.

Fix \(\sigma_0\), trivialize by \(\eta_{\sigma_0}\), and put

\[
 K=\dot\eta_{\sigma_0}\eta_{\sigma_0}^{-1}.
\]

Thus \(\eta_{\sigma_0}=I\), \(\mathsf E_{\sigma_0}=P\), and

\[
 \boxed{\dot{\mathsf E}_{\sigma_0}=[K,P].}          \tag{1.4}
\]

Differentiating (1.3) also gives

\[
 P\dot{\mathsf E}P=0,\qquad
 (I-P)\dot{\mathsf E}(I-P)=0,                      \tag{1.5}
\]

so the tangent is exactly off diagonal.

## 2. Recovery of the metric score

The Hilbert metric transported by \(\eta_\sigma\) is

\[
 G_\sigma=\eta_\sigma^*\eta_\sigma.
\]

At the normalized point,

\[
 H:=\dot G_{\sigma_0}=K^*+K.                       \tag{2.1}
\]

Using (1.4),

\[
 \begin{aligned}
 P\dot{\mathsf E}(I-P)&=-PK(I-P),\\
 P\dot{\mathsf E}^{\,*}(I-P)&=PK^*(I-P).
 \end{aligned}
\]

Consequently

\[
 \boxed{
 PH(I-P)
 =P\bigl(\dot{\mathsf E}^{\,*}-\dot{\mathsf E}\bigr)(I-P).
 }                                                   \tag{2.2}
\]

For the semilocal metric of D.240, after support and Tate compression,
\(H=Q_T\).  If \(P_O\le P\) and \(P_E\le I-P\), (2.2) gives

\[
 \boxed{
 P_OQ_TP_E
 =P_O(\dot{\mathsf E}^{\,*}-\dot{\mathsf E})P_E.
 }                                                   \tag{2.3}
\]

Equation (2.3) includes Gamma and all prime powers through the complete
metric derivative.  D.242 identifies the finite-prime failure of the
Fourier-compatible part of this tangent explicitly.

## 3. Why idempotence does not pay the Douglas budget

The first derivative of an idempotent is off diagonal, but its two
off-diagonal blocks are independent.  On
\(\mathbb C\oplus\mathbb C\), take

\[
 K=\begin{pmatrix}\alpha&u\\v&\delta\end{pmatrix}.
\]

Then

\[
 \dot{\mathsf E}
 =\begin{pmatrix}0&-u\\v&0\end{pmatrix},\qquad
 PH(I-P)=u+\bar v.                                  \tag{3.1}
\]

The value \(u+\bar v\) is arbitrary.  Moreover the diagonal score blocks
are

\[
 PHP=2\operatorname{Re}\alpha,\qquad
 (I-P)H(I-P)=2\operatorname{Re}\delta,              \tag{3.2}
\]

and are independent of \(u,v\).  Thus the Schur residual

\[
 2\operatorname{Re}\delta
 -{|u+\bar v|^2\over2\operatorname{Re}\alpha}       \tag{3.3}
\]

can have either sign even though (1.3)--(1.5) hold exactly.

This is the first-order analogue of the counterexample in D.241.  The
oblique projection solves the typing problem but not the positivity
problem.

## 4. The smaller source question

The tangent now has two independent source pieces:

1. its Fourier-compatible component, containing the central self-dual
   vector and the archimedean channel;
2. the anti-self-dual anomaly of D.242,
   \[
   -\sum_{p\in S}{\log p\over p}\,
      \sigma_{S\setminus\{p\}}\otimes w_p .
   \]

The next exact calculation is to decompose
\(\dot{\mathsf E}\) into these two pieces after adelic quotient and support
compression.  The target is an identity of the form

\[
 B_E-X_{OE}^*A_O^\dagger X_{OE}
 =\mathcal Z_{\rm anom}^*\mathcal Z_{\rm anom}
  +\mathcal R_{\Gamma,\rm Sonin},                  \tag{4.1}
\]

with the first term correctly tangent/Fisher normalized.  If
\(\mathcal R_{\Gamma,\rm Sonin}\) is not manifestly positive, its exact
formula is the next residual.  Neither term may be defined using the
left-hand pseudoinverse.

## 5. Classification

* Dual transported idempotent (1.2)--(1.3): **PROVED IDENTITY**.
* Tangent commutator (1.4)--(1.5): **PROVED**.
* First-order recovery of the complete D.190 coupling (2.2)--(2.3):
  **PROVED IDENTITY**.
* Sharp Douglas sign from idempotence alone: **FALSE IN GENERAL**, by
  (3.1)--(3.3).
* Source-specific decomposition (4.1): **OPEN**.
* Row D: **OPEN**.
