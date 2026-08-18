# 106.116 — PNT heat quadrature and the no-matching-scale gate

## 1. Purpose

The cofinal heat criterion of 106.102 asks for

\[
 \int_0^\infty J_t(u)\,d\sigma(u)\geq-o(Z(t))
 \tag{1}
\]

along an unbounded sequence of heat times.  The special source profile
\(J_t\) is nonnegative, starts quadratically at the origin, and is built
from the literal prime, Gamma and polar gradients.  This suggests a
sampling argument: use the prime number theorem on the slowly varying part
of \(J_t\), and use the Gamma small-jump energy on the rapidly varying
part.

This note carries out the reduction exactly.  It produces two useful
results.

1.  The complete source is an exact PNT quadrature error plus one positive
    archimedean remainder.  No source term is estimated before the PNT main
    measure has cancelled the growing polar branch.
2.  Heat time supplies no scale separation in the displacement variable.
    On a pure eigenrow the normalized profile is exactly stationary, and
    on an isolated bottom eigenspace it is asymptotically stationary.  The
    canonical Gamma translation seminorm penalizes frequency \(\xi\) only
    by \(\frac12\log |\xi|+O(1)\).  Consequently a low/high-frequency split
    has no regime in which the PNT quadrature loss and the unresolved high
    frequency part both become \(o(Z(t))\).

The second statement is a gate for this particular proof architecture.  It
does not refute a globally signed prime--Gamma transfer.  It proves that
such a transfer must retain correlations with the actual PNT discrepancy;
pointwise PNT plus Gamma regularity cannot supply (1).

### Relation to earlier project results

The algebra in (5) is the heat-profile specialization of the exact PNT
compensation in 106.18, not a second independent cancellation identity.
Document 106.22 already excludes generic translation-metric quadrature,
and the old Paley--Wiener phases already show that band limitation alone
does not create prime slack.  Documents 106.102 and 106.112 already prove,
respectively, the cofinal heat criterion and stationarity of the normalized
Bochner law on an eigenrow.  The new content here is the combination needed
for the proposed attack: the exact multiplier (17), the fixed-carrier
observation (9), the quantitative envelope deficit (13), and the resulting
no-matching-scale theorem for a PNT-envelope/Gamma-frequency split.  No
novelty is claimed for the standard digamma summation used to evaluate
(17).

## 2. Exact quadrature identity

Put

\[
 E(u)=\psi(e^u)-e^u,
 \qquad
 p(u)=\frac{e^{-5u/2}}{1-e^{-2u}}.
 \tag{2}
\]

The compensated source measure of 106.102 is

\[
 d\sigma(u)=
 \sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}\,
       \delta_{\log n}(du)
 +\left\{\frac{e^{-u/2}}{1-e^{-2u}}
          -2\cosh(u/2)\right\}du.
 \tag{3}
\]

Since

\[
 e^{-u/2}\,dE(u)
 =\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
       \delta_{\log n}(du)-e^{u/2}\,du,
 \tag{4}
\]

one has the exact joint identity

\[
 \boxed{d\sigma(u)=e^{-u/2}\,dE(u)+p(u)\,du.}
 \tag{5}
\]

The remainder in (5) is positive.  It is precisely what remains after the
PNT main measure, both polar branches and Gamma have been assembled.

### Theorem 1 — Heat-profile PNT quadrature

Let \(J\) be a translation-smooth hybrid profile satisfying

\[
 J(0)=J'(0)=0,
 \qquad
 e^{-u/2}J(u)E(u)\longrightarrow0
 \quad(u\to\infty).
 \tag{6}
\]

Then

\[
 \boxed{
 \int_0^\infty J(u)\,d\sigma(u)
 =-\int_0^\infty E(u)
       \bigl(e^{-u/2}J(u)\bigr)'\,du
  +\int_0^\infty p(u)J(u)\,du.}
 \tag{7}
\]

The same formula holds on a heat row by common source cutoff and closed
form approximation.

#### Proof

Pair (5) with \(J\).  Stieltjes integration by parts gives

\[
 \int_0^\infty e^{-u/2}J(u)\,dE(u)
 =\left[e^{-u/2}J(u)E(u)\right]_{0}^{\infty}
  -\int_0^\infty E(u)
       \bigl(e^{-u/2}J(u)\bigr)'\,du.
 \tag{8}
\]

Both boundary values vanish by (6).  Adding the positive term in (5)
proves (7).  For a general heat row, first use a common finite prime cutoff,
a Gamma cutoff and a spatial mollifier.  Equation (7) holds there.  The
unsplit left side converges in the closed source form, and the right side is
defined by that same joint limit.  \(\square\)

The centering factor in (7) is load-bearing:

\[
 \bigl(e^{-u/2}J(u)\bigr)'
 =e^{-u/2}\{J'(u)-\tfrac12J(u)\}.
 \tag{9}
\]

Thus even a slowly varying \(J\) retains a fixed carrier derivative
\(-J/2\).  Demodulating that carrier requires analytic control in a
half-strip; ordinary real-variable smoothness does not provide it.

## 3. The strongest pointwise-PNT consequence

Define

\[
 \begin{aligned}
  \mathcal P(J)&=\int_0^\infty p(u)J(u)\,du,\\
  \mathcal V_E(J)&=
  \int_0^\infty |E(u)|e^{-u/2}
       |J'(u)-\tfrac12J(u)|\,du.
 \end{aligned}
 \tag{10}
\]

Whenever the quantities are finite, (7) gives

\[
 \boxed{
  \int J\,d\sigma\geq \mathcal P(J)-\mathcal V_E(J).}
 \tag{11}
\]

Replacing \(|E(u)|\) by any effective Vinogradov--Korobov envelope gives a
larger loss.  Therefore (11) is the sharpest lower bound obtainable after
discarding the sign correlation between \(E\) and the centered derivative
in (7).

There is a quantitative stress test.  Suppose that \(Aq=\alpha q\),
\(\|q\|=1\), and \(0<\alpha<1/2\).  Let \(J_q\) be its displacement
profile.  The exact source identity gives

\[
 \int J_q\,d\sigma=\alpha-\frac12.
 \tag{12}
\]

Combining (11) and (12) yields

\[
 \boxed{
 \mathcal V_E(J_q)-\mathcal P(J_q)
 \geq\frac12-\alpha.}
 \tag{13}
\]

Hence a pointwise-PNT proof does not merely miss a convenient constant in
the forbidden model.  It loses at least the complete subthreshold depth.
The only way to reverse (13) in the Riemann system is to use the signed
correlation suppressed in passing from (7) to (11).

## 4. What the Gamma small-jump term controls

The most favorable stationary part of a heat profile is the translation
metric of \(f=Kr\),

\[
 G_f(u)=\|f-\tau_u f\|_2^2.
 \tag{14}
\]

Let

\[
 c_\infty(u)=\frac{e^{-u/2}}{1-e^{-2u}}
 =\sum_{k=0}^\infty e^{-(2k+1/2)u}.
 \tag{15}
\]

### Theorem 2 — Exact logarithmic Gamma multiplier

For every \(f\) for which the two sides are finite,

\[
 \int_0^\infty G_f(u)c_\infty(u)\,du
 =2\int_{\mathbb R}m_\Gamma(\xi)
       |\widehat f(\xi)|^2\frac{d\xi}{2\pi},
 \tag{16}
\]

where

\[
 \begin{aligned}
 m_\Gamma(\xi)
 &=\sum_{k=0}^\infty
   \frac{\xi^2}
   {(2k+\tfrac12)((2k+\tfrac12)^2+\xi^2)}\\
 &=\frac12\mathrm{Re}
   \left\{
    \psi_0\!\left(\frac14+\frac{i\xi}{2}\right)
    -\psi_0\!\left(\frac14\right)
   \right\}.
 \end{aligned}
 \tag{17}
\]

Here \(\psi_0\) is the digamma function.  The multiplier is even and
strictly increasing in \(|\xi|\), and

\[
 \boxed{m_\Gamma(\xi)=\frac12\log|\xi|+O(1)}
 \qquad(|\xi|\to\infty).
 \tag{18}
\]

#### Proof

Plancherel gives

\[
 G_f(u)=2\int_{\mathbb R}(1-\cos(\xi u))
             |\widehat f(\xi)|^2\frac{d\xi}{2\pi}.
 \tag{19}
\]

Tonelli and (15) reduce the inner integral to

\[
 \int_0^\infty(1-\cos(\xi u))e^{-au}\,du
 =\frac{\xi^2}{a(a^2+\xi^2)}.
 \tag{20}
\]

This proves the first line of (17).  Put \(a=2(k+1/4)\) and use the
standard series definition of the digamma function to obtain the second
line.  Every summand is strictly increasing in \(|\xi|\).  Finally,
\(\psi_0(z)=\log z+O(1/z)\) in the relevant sector, which gives (18).
\(\square\)

For \(\Omega>0\), Theorem 2 implies only

\[
 \boxed{
 \int_{|\xi|>\Omega}|\widehat f(\xi)|^2\frac{d\xi}{2\pi}
 \leq
 \frac{1}{2m_\Gamma(\Omega)}
 \int_0^\infty G_f(u)c_\infty(u)\,du.}
 \tag{21}
\]

Thus the available high-frequency coercivity grows logarithmically.  Even
granting a uniform normalized bound for the right side, its tail estimate
becomes small only by sending \(\Omega\to\infty\).

## 5. Heat does not create a displacement bandwidth

### Theorem 3 — Stationarity of the normalized eigenrow profile

If \(Aq=\alpha q\), \(\|q\|=1\), and

\[
 \Gamma_t=e^{-t(A+I/2)/2}|q\rangle\langle q|
          e^{-t(A+I/2)/2},
 \tag{22}
\]

then

\[
 \Gamma_t=e^{-t(\alpha+1/2)}|q\rangle\langle q|,
 \qquad
 \boxed{
 \frac{J_t(u)}{Z(t)}=J_q(u)\quad\text{for every }t,u.}
 \tag{23}
\]

More generally, if \(\alpha\) is an isolated finite-multiplicity bottom
eigenvalue and the positive heat-core boost sees its eigenspace, then the
normalized heat state converges in trace norm to

\[
 \Gamma_\infty
 =\frac{P_\alpha V P_\alpha}
        {\mathrm{Tr}(P_\alpha V P_\alpha)},
 \tag{24}
\]

and, for every fixed displacement,

\[
 \frac{J_t(u)}{Z(t)}\longrightarrow
 \mathcal J_u[\Gamma_\infty].
 \tag{25}
\]

#### Proof

Equation (23) follows by applying the heat factors to the eigenvector.
For (24), split the spectral resolution of \(A\) at the isolated bottom
eigenspace.  After dividing by the leading exponential, every complementary
term decays by the spectral gap.  This gives trace-norm convergence.  For
fixed \(u\), the jump operator \(B_u\) is bounded: each diagonal term is at
most \(K(0)\|r\|^2\), and the cross term follows by Cauchy--Schwarz.  Hence
trace-norm convergence implies (25).  \(\square\)

Theorem 3 is the exact missing scale.  Heat time suppresses higher spectral
rows, but it does not send the surviving displacement profile to lower
bandwidth.  In the only adversarial case relevant to the proof--an isolated
subthreshold mode--the profile in (23) is independent of heat time.

## 6. No matching scale for the proposed split

Consider any low/high decomposition at displacement bandwidth \(\Omega\)
which is compatible with scalar multiplication of the heat state.  There
are two possible asymptotic choices.

* To make the Gamma-controlled high-frequency tail in (21) small, one must
  take \(\Omega\to\infty\).  Then the low-frequency part converges back to
  the complete stationary profile, and its PNT quadrature converges to the
  original unknown signed pairing.
* To make a Bernstein-type derivative bound for the low-frequency part
  small, one would take \(\Omega\to0\).  The high-frequency remainder then
  converges back to the complete stationary profile.  Moreover (9) leaves
  the fixed half-carrier even at zero bandwidth, unless one has analytic
  half-strip control capable of demodulating \(e^{-u/2}\).

Every bounded intermediate sequence of bandwidths has a subsequence
converging to a fixed \(\Omega_*\); Theorem 3 then leaves a fixed, not
vanishing, decomposition of \(J_q\).  Thus heat cofinality contributes no
small parameter to either side.

This can be summarized by the following exact stress statement.

### Corollary 4 — Fixed deficit of every triangle-envelope split

Let \(J_q=\sum_aJ_a\) be any finite decomposition for which differentiation
and integration in (7) may be performed term by term.  Suppose the PNT
piece of every component is bounded by

\[
 -\int E(u)\bigl(e^{-u/2}J_a(u)\bigr)'du
 \geq
 -\int |E(u)|\left|
       \bigl(e^{-u/2}J_a(u)\bigr)'\right|du,
 \tag{26}
\]

and every additional Gamma estimate is used only as a nonnegative lower
bound.  In a subthreshold eigenrow, the total loss in these componentwise
PNT bounds exceeds the positive remainder by at least

\[
 \boxed{\frac12-\alpha.}
 \tag{27}
\]

#### Proof

The triangle inequality gives

\[
 \sum_a\int |E|
 \left|\bigl(e^{-u/2}J_a\bigr)'\right|du
 \geq
 \int |E|\left|\bigl(e^{-u/2}J_q\bigr)'\right|du
 =\mathcal V_E(J_q).
 \tag{28}
\]

Equation (13) now proves (27).  Formula (23) makes the normalized deficit
independent of heat time.  \(\square\)

Corollary 4 is deliberately restricted to the envelope-split architecture.
A signed operator mixing distinct prime powers with Gamma before taking a
norm is not covered by it.

## 7. Surviving theorem

The quadrature attack therefore sharpens, but does not prove, the physical
surplus.  The surviving statement is not a smoothness estimate.  It is the
signed correlation bound

\[
 \boxed{
 -\int_0^\infty E(u)
       \bigl(e^{-u/2}J_{t_k}(u)\bigr)'\,du
 +\int_0^\infty p(u)J_{t_k}(u)\,du
 \geq-o(Z(t_k))}
 \tag{29}
\]

for a cofinal sequence \(t_k\).  The sign of \(E\) must be retained in
(27).  Equivalently, one must prove that the literal prime-log sampling
error is aligned with the centered derivative of the physical heat
profile.  PNT envelopes, real-variable low-pass smoothing, and Gamma
small-jump coercivity do not imply that alignment.

## 8. Status

Proved here:

* the exact PNT quadrature identity (7);
* the sharp envelope loss and its subthreshold lower bound (13);
* the exact logarithmic Gamma multiplier (16)--(18);
* the normalized stationarity of a pure heat eigenrow and trace-norm
  convergence on an isolated bottom eigenspace;
* the no-matching-scale result for the low/high envelope architecture.

Not proved here:

\[
 \int J_{t_k}\,d\sigma\geq-o(Z(t_k)).
\]

The remaining input is the signed correlation (27), with ordinary prime
locations, Gamma and the polar carrier kept jointly after exact radical
anti-shorting.
