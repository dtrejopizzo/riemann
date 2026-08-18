# D.240 — Dual Euler conservation and its localized norm defect

## Verdict

The semilocal Euler and inverse-Euler embeddings satisfy an exact
source-defined conservation law.  Differentiating it produces the local
scores of D.239 with opposite signs.  This is the first completed
prime-state identity in the current route which is both lossless and
specific to the adelic/Sonin construction.

Let \(S\) be a finite set of primes and, for real \(\sigma>0\), put

\[
 E_{S,\sigma}^{\pm}(\tau)
 =\prod_{p\in S}L_p(\sigma\pm i\tau).               \tag{0.1}
\]

On a common dense Schwartz core define

\[
 \eta_{S,\sigma}f=E_{S,\sigma}^{-}f,
 \qquad
 \theta_{S,\sigma}f=(E_{S,\sigma}^{+})^{-1}f.      \tag{0.2}
\]

Then, with the complex Hilbert pairing linear in the first variable,

\[
 \boxed{
 \langle\theta_{S,\sigma}f,
        \eta_{S,\sigma}g\rangle_{L^2(d\tau)}
 =\langle f,g\rangle_{L^2(d\tau)}.
 }                                                     \tag{0.3}
\]

The identity is pointwise: for real \(\tau\),
(overline{E_{S,\sigma}^{-}(\tau)}=E_{S,\sigma}^{+}(\tau)).
It is the finite-place multiplier form of the pairing theorem for the
maps \(\theta_S,\eta_S\) in the semilocal adelic construction.

Differentiating (0.3) gives the exact conservation law

\[
 \boxed{
 \langle\dot\theta_{S,\sigma}f,eta_{S,\sigma}g\rangle
 +\langle\theta_{S,\sigma}f,dot\eta_{S,\sigma}g\rangle=0.
 }                                                     \tag{0.4}
\]

At \(\sigma=1/2\), the logarithmic derivatives in (0.4) are exactly the
prime-tower score operators of D.239, containing all (p^k) with weights
((\log p)p^{-k/2}).

This conservation law does not yet prove row D.  It preserves a **dual
pairing**, not the two positive Hilbert norms separately.  The semilocal
maps are bounded isomorphisms but are not asserted to be contractions.
After support cutoff, the failure of the cutoff projection to intertwine
\(\eta\) and \(\theta\) is a Hankel/Poisson boundary block.  Identifying its
positive norm defect with the D.190 born budget is the remaining theorem.

## 1. Exact differentiation

The Euler logarithmic derivatives are

\[
 \begin{aligned}
 \partial_\sigma\log E_{S,\sigma}^{-}(\tau)
 &=-\sum_{p\in S}(\log p)
 {p^{-\sigma+i\tau}\over1-p^{-\sigma+i\tau}},\\
 \partial_\sigma\log (E_{S,\sigma}^{+}(\tau))^{-1}
 &=+\sum_{p\in S}(\log p)
 {p^{-\sigma-i\tau}\over1-p^{-\sigma-i\tau}}.
 \end{aligned}                                      \tag{1.1}
\]

Hence

\[
 \dot\eta_{S,\sigma}=M_{a_{S,\sigma}^{-}}\eta_{S,\sigma},
 \qquad
 \dot\theta_{S,\sigma}=M_{a_{S,\sigma}^{+}}\theta_{S,\sigma},
                                                               \tag{1.2}
\]

where the multipliers in (1.1) are conjugate with opposite signs.  This
proves (0.4) directly.  Taking the real part of either logarithmic norm
derivative recovers

\[
 -\partial_\sigma\log|E_{S,\sigma}^{-}|^2
 =\sum_{p\in S}(\log p)
  \sum_{k\ge1}p^{-k\sigma}
  (e^{ik\tau\log p}+e^{-ik\tau\log p}).             \tag{1.3}
\]

At \(\sigma=1/2\), inverse Fourier transformation of (1.3) is the complete
finite-place contact operator of A--B--C.

## 2. Relation with the one-state factors

For one prime, the inverse-Euler multiplier in \(\theta\) is

\[
 1-p^{-1/2-i\tau},                                  \tag{2.1}
\]

which is exactly the stable numerator appearing in the semilocal Sonin
embedding.  The Euler multiplier in \(\eta\) is its resolvent.  D.237's
filters

\[
 (I-p^{-1/2}S_{\log p})^{-1}(I-s_pS_{\log p})       \tag{2.2}
\]

are therefore finite-energy combinations of the same dual Euler states.
The special antisymmetric numerator \(I-S_{\log p}\) records the difference
channel, while the denominator is the Euler state of \(\eta\).

Thus D.237 is not an unrelated spectral factorization: it is a positive
feature realization inside the dual pair (0.2).

## 3. Support projections and the exact anomaly

Before introducing the support projection, the archimedean factor closes
the score identity exactly.  Put

\[
 L_\infty(s)=\pi^{-s/2}\Gamma(s/2),
 \qquad
 E_{S,\sigma}(\tau)=L_\infty(\sigma+i\tau)
       \prod_{p\in S}L_p(\sigma+i\tau).              \tag{3.1}
\]

Then

\[
 -\left.\partial_\sigma\log|L_\infty(\sigma+i\tau)|^2
 \right|_{\sigma=1/2}
 =\log\pi-\operatorname {Re}\psi
       (\tfrac14+\tfrac{i\tau}{2})
 =m_\infty(\tau).                                   \tag{3.2}
\]

Together with D.239(0.2), this gives

\[
 \left.\partial_\sigma\log|E_{S,\sigma}(\tau)|^2
 \right|_{\sigma=1/2}
 =-m_\infty(\tau)
 -\sum_{p\in S}\sum_{k\ge1}{\log p\over p^{k/2}}
   (e^{ik\tau\log p}+e^{-ik\tau\log p}).             \tag{3.3}
\]

For a support window \(I_T\), terms with \(k\log p\ge2T\) vanish after
zero-extension compression.  The finite-part normalization of the first
term and the two Tate--Chebyshev identities are exactly those already
proved in D.133--D.137.  Consequently

\[
 \boxed{
 Q_T=-B_{{\rm nuc},T}^{\rm prim}
 =\Pi_TJ_T^*
 \left.\partial_\sigma\log|E_{S,\sigma}|^2
 \right|_{\sigma=1/2}
 J_T\Pi_T
 }                                                     \tag{3.4}
\]

as a closed quadratic form, whenever \(S\) contains the primes active in
the window.  Thus the complete Gamma/Tate port from the semilocal metric to
the A--B--C form is proved; no comparison remains at the scalar-form level.

Equivalently, if

\[
 G_{S,\sigma}=M_{|E_{S,\sigma}|^2},                 \tag{3.5}
\]

then the unlocalized score operator is the logarithmic metric derivative

\[
 G_{S,\sigma}^{-1/2}\dot G_{S,\sigma}
 G_{S,\sigma}^{-1/2}
 =M_{\partial_\sigma\log|E_{S,\sigma}|^2}.          \tag{3.6}
\]

Row D is therefore positivity of the support- and Tate-compressed
logarithmic derivative (3.6), not positivity of \(G_{S,\sigma}\) itself.
Every \(G_{S,\sigma}\) is positive automatically; its derivative can have
either sign.

### Support anomaly

Let \(P\) be a support projection in logarithmic coordinates.  Although
\(\theta^*\eta=I\) on the uncut core, generally

\[
 (\theta P)^*(\eta P)=P,
\]

while the cross-support block contains

\[
 P\theta^*(I-P)\eta P.                              \tag{3.7}
\]

Equivalently, the failure of support intertwining is measured by

\[
 [P,M_{E_{S,\sigma}^{-}}],
 \qquad
 [P,M_{(E_{S,\sigma}^{+})^{-1}}].                  \tag{3.8}
\]

Differentiating (3.8) at \(\sigma=1/2\) produces the same Toeplitz--Hankel
boundary type as

\[
 [P_O,Q_T]P_E                                       \tag{3.9}
\]

in D.190.  The equality of types is exact at the prime multiplier level by
(1.3), and equations (3.1)--(3.4) supply the Gamma normalization and the
two Tate corrections.

The conservation law (0.3) therefore pays the **ambient** Euler pairing.
The D.190 theorem asks for the positive norm defect after old-core
shorting.  Algebraically, the unpaid object is the localized commutator
defect remaining after (0.4) cancels the coherent interior contribution.

## 4. Semilocal Sonin input which is already proved

For the normalized additive characters, the semilocal construction proves:

1. the inverse-Euler vector
   \(\sigma_p=\epsilon_0-p^{-1}\epsilon_1\) is self-Fourier;
2. tensoring these vectors defines the map \(\theta_S\);
3. \(\theta_S\) intertwines the local Fourier transforms;
4. \(\theta_S\) is a Hilbert-space isomorphism from the archimedean Sonin
   space onto the semilocal Sonin space;
5. the dual pairing with the Euler map \(\eta_S\) is exactly preserved.

These are unconditional theorems in
[Connes--Consani--Moscovici](https://arxiv.org/abs/2310.18423), and they use
the self-duality of the additive adelic characters, an input absent from a
generic Beurling prime system.

What is not proved there is positivity of the derivative score after the
support/phase-space compression.  The paper presents this as the proposed
semilocal Weil-positivity programme.

## 5. Porting theorem still required

The admissible next theorem can now be stated without postulating
causality of the completed zeta quotient:

> **Dual-Euler boundary-defect theorem.**  The derivative at
> \(\sigma=1/2\) of the localized conservation law (0.3), already
> identified with (3.4), has a positive defect factorization.  On every
> old/born cell this factorization is D.190(0.3), with the born metric
> \(B_E\) and constant one.

The theorem must be proved from the self-Fourier local vectors, the
semilocal Sonin projection and the phase-space support geometry.  It may
not be obtained by declaring the completed Euler quotient inner or by
using the spectral zeros.

If true, it supplies the uniform birth theorem directly and avoids a
separate asymptotic estimate.  If false, its exact residual is the
structurally correct object on which the D.211 finite-Green and D.213
Carleson routes must act.

## 6. Classification

* Dual Euler pairing (0.3): **PROVED IDENTITY**.
* Differentiated conservation (0.4): **PROVED IDENTITY**.
* Recovery of every prime-power score (1.3): **PROVED**.
* Semilocal Sonin isomorphism and Fourier compatibility: **PROVED IN THE
  CITED PRIMARY SOURCE**.
* Complete Gamma/Tate identification of the localized logarithmic metric
  derivative with \(Q_T=-B_{\rm nuc,T}^{\rm prim}\): **PROVED**, using
  D.133--D.137.
* Positivity of the localized derivative defect: **OPEN**.
* Row D: **OPEN**.
