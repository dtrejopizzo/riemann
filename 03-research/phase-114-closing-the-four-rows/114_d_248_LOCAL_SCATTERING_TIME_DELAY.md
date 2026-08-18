# D.248 — Euler scores as relative Wigner--Smith time delays

## Verdict

The local tangent score of D.245 is the relative time delay of a canonical
inner scattering factor.  For every prime, the normalized Euler factor
extends to a scalar Blaschke function, whose Wigner--Smith delay is the
positive Poisson kernel.  The arithmetic score is that positive delay
minus the free unit delay.

The scalar degree/contact channels in the conservative identity D.247 are
exactly the source channels needed to retain this subtraction without a
lossy estimate.  At infinity, the local Tate scattering ratio has the
analogous boundary phase derivative equal to the complete Gamma score.

This supplies a genuine Hardy/scattering candidate for the D.190
colligation.  What is not yet proved is that the support-compressed
derivative of the product scattering colligation has the D.190 Schur
residual with positive defect.

## 1. Prime Blaschke factor

Let \(U=e^{i\theta}\), \(0<r=p^{-1/2}<1\), and

\[
 b_p(U)={U-r\over1-rU}
       =U\,{1-rU^*\over1-rU}.                      \tag{1.1}
\]

This is a scalar inner function on the disk.  On the unit circle,
\(|b_p(U)|=1\).  Direct differentiation gives

\[
 \begin{aligned}
 -i\,\partial_\theta\log
   {1-rU^*\over1-rU}
 &=P_r(U)-I,\\
 -i\,\partial_\theta\log U&=1,
 \end{aligned}                                      \tag{1.2}
\]

where

\[
 P_r(U)={1-r^2\over|1-rU|^2}.
\]

Therefore

\[
 \boxed{
 -i\,\partial_\theta\log b_p(U)=P_r(U)\ge0.
 }                                                   \tag{1.3}
\]

Since \(\theta=\tau\log p\),

\[
 \boxed{
 (\log p)(P_r-I)
 =-i\,\partial_\tau\log b_p-\log p.
 }                                                   \tag{1.4}
\]

The left side is the complete prime-power score of D.245.  The first term
on the right is a positive Wigner--Smith delay; the second is the free
translation delay.

## 2. Canonical unitary colligation

The Blaschke factor (1.1) is the transfer function of the two-dimensional
Julia colligation

\[
 \mathcal J_r=
 \begin{pmatrix}
 r&\sqrt{1-r^2}\\
 \sqrt{1-r^2}&-r
 \end{pmatrix},
 \qquad \mathcal J_r^*\mathcal J_r=I,               \tag{2.1}
\]

up to the harmless standard input/output sign convention.  Its
observability kernel is

\[
 (1-r^2)(I-rU^*)^{-1}(I-rU)^{-1}=P_r(U),            \tag{2.2}
\]

which is exactly the one-state Euler--Poisson feature of D.236.

Thus the positive kernel, the rational feature, the local Fourier tangent,
and the time-delay scattering factor all arise from the same unitary
colligation:

\[
 \text{Julia colligation}
 \Longrightarrow b_p
 \Longrightarrow P_r
 \Longrightarrow (\log p)(P_r-I).
                                                               \tag{2.3}
\]

No sign of the global Weil form is used.

## 3. Contact and free delay

Equation (1.4) explains the exact diagonal cancellation in D.238.  On a
new shell, the Poisson delay and the free delay have the same diagonal
compression, so

\[
 P_E(\log p)(I-P_r)P_E=0.
\]

They cannot be estimated separately.  The conservative colligation of
D.247 retains them as two ports:

* the scalar/global degree port carries the coherent free delay;
* the diagonal torsion-contact port carries the local Poisson delay.

On the primitive degree kernel, their difference is the positive defect of
the prime-tangent contraction.

## 4. Archimedean scattering phase

Put \(s=\frac12+i\tau\) and define the boundary-unitary local Tate ratio

\[
 b_\infty(\tau)
 ={L_\infty(s)\over L_\infty(\bar s)}.              \tag{4.1}
\]

It has modulus one.  Differentiating and using
\(\overline{L_\infty'(s)/L_\infty(s)}
=L_\infty'(\bar s)/L_\infty(\bar s)\) gives

\[
 \boxed{
 -i\,\partial_\tau\log b_\infty(\tau)
 =2\mathrm{Re}{L_\infty'(s)\over L_\infty(s)}.
 }                                                   \tag{4.2}
\]

This is exactly the Gamma score of D.246.  Formula (4.2) is a boundary
unitary identity.  Calling \(b_\infty\) an inner function in a chosen
half-plane additionally requires the standard pole/outer-factor
normalization; that analytic assertion is not assumed here.

## 5. Product scattering target

For a finite active set \(S\), form the tensor/cascade of the prime Julia
colligations and the normalized archimedean scattering system.  On the
boundary its logarithmic time delay is additive:

\[
 -i\,\partial_\tau\log
 \left(b_\infty\prod_{p\in S}b_p\right)
 =
 \text{Gamma score}
 +\sum_{p\in S}(\log p)P_{p^{-1/2}}.                \tag{5.1}
\]

Subtracting the free-delay/contact ports gives the complete semilocal score
of D.240.

The next theorem must not merely note boundary unitarity.  It must prove:

> After the position/Fourier support compression and two-Tate shorting, the
> differentiated transfer-defect identity of the source cascade equals
> \[
> B_E-X_{OE}^*A_O^\dagger X_{OE}.
> \]

If the cascade has the required causal/Hardy realization from its local
factors, the standard unitary-colligation defect identity is a candidate
source for positivity.  D.234 forbids assuming causality of the completed
global zeta quotient; it must be proved here for the finite semilocal
source cascade and shown compatible with passage through the active
windows.

## 6. Classification

* Prime Blaschke/time-delay identities (1.1)--(1.4): **PROVED**.
* Julia colligation and Poisson observability (2.1)--(2.3): **PROVED**.
* Identification of free-delay/contact cancellation: **PROVED**, using
  D.238.
* Archimedean boundary phase identity (4.2): **PROVED**.
* Boundary unitarity of the finite product: **PROVED**.
* Causal/Hardy transfer realization of the complete finite semilocal
  Gamma-normalized cascade: **OPEN**.
* Differentiated support-defect equality with D.190: **OPEN**.
* Row D: **OPEN**.
