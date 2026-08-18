# 106.112 — Analytic Bochner multiplier and the heat-order gate

## 1. Purpose and conclusion

Document 106.110 reduces the signed source of a heat row to

\[
 \int_0^\infty \mathcal J_u[\Gamma]\,d\sigma(u)
 =-2C_\Gamma(0)\,
   \ell_\sigma(\Phi_\Gamma-\chi_K).
 \tag{1}
\]

This note computes the Fourier-side object represented by
\(\ell_\sigma\) after the canonical radical subtraction.  The answer is
not, in general, a real scalar cost against the Bochner probability
measure.  It is the analytic zero-sampling functional

\[
 \boxed{
 \widehat{\ell_\sigma}^{\,\mathrm{an}}
 =-\frac12\sum_{s\in\mathcal Z}m_s\,\delta_s^{\mathrm{an}},}
 \qquad
 \delta_s^{\mathrm{an}}(H)=H(s),
 \tag{2}
\]

where \(\rho=\frac12+is\) runs over the nontrivial zero divisor in the
centered coordinate.  Thus the literal von Mangoldt, Gamma and polar
terms have already combined into one analytic multiplier.

If all \(s\) are real, (2) is a negative point-sampling measure on the
real frequency axis and the desired sign is immediate.  An off-line
orbit moves two sampling points off the real axis and changes the
corresponding square into one positive and one negative real channel.
Consequently the missing sign cannot be obtained from a standard
monotone or convex order of the real Bochner measures.

Two further exact tests reinforce this conclusion.

1.  The complete Riemann radical contains normalized Bochner measures
    with variance both above and below that of \(\beta_K\), while every
    one of them gives equality in (1).  Hence neither orientation of
    convex order relative to \(\beta_K\) is compatible with the equality
    family.
2.  The normalized Bochner measure of a pure eigenmode is stationary
    under the physical heat flow.  In particular, heat evolution would
    leave the forbidden Bochner measure of a hypothetical subthreshold
    eigenmode unchanged.

The outcome is an exact gate, not the physical-surplus theorem.  Any
successful Bochner argument must control the off-real analytic samples
using the joint arithmetic source; ordinary order of probability
measures on \(\mathbb R\) does not see them.

No zero location is assumed in the unconditional identities below.

## 2. Canonically subtracted autocorrelations

Use the centered zero coordinate

\[
 \rho=\frac12+is,
 \qquad
 \mathcal Z=\{s:\Xi(s)=0\},
 \tag{3}
\]

with multiplicities \(m_s\).  Let \(f\) be a real even Weil-admissible
row, let

\[
 F(z)=\widehat f(z),
 \qquad
 C_f(u)=\int_{\mathbb R}f(x)f(x-u)\,dx,
 \tag{4}
\]

and put

\[
 C_f^\circ(u)
 =C_f(u)-\frac{\|f\|_2^2}{\|K\|_2^2}C_K(u).
 \tag{5}
\]

With the Fourier convention used throughout Phase 106,

\[
 \widehat{C_f}(z)=F(z)F(-z)=F(z)^2,
 \tag{6}
\]

because \(F\) is even.  Since \(\widehat K=\Xi\),

\[
 \widehat{C_f^\circ}(z)
 =F(z)^2-\frac{\|f\|_2^2}{\|K\|_2^2}\Xi(z)^2.
 \tag{7}
\]

The subtraction in (5) is essential on the physical side: it gives the
two vanishing endpoint jets needed to pair the prime, Gamma and polar
channels jointly.  Equation (7) shows that it does not alter a single
zero sample.

For a positive finite-rank state

\[
 \Gamma=\sum_{j=1}^N\gamma_j|r_j\rangle\langle r_j|,
 \qquad
 f_j=Kr_j,
 \qquad \gamma_j>0,
 \tag{8}
\]

write \(F_j=\widehat f_j\) and

\[
 C_\Gamma(0)=\sum_j\gamma_j\|f_j\|_2^2.
 \tag{9}
\]

The corresponding normalized positive-definite function is

\[
 \Phi_\Gamma(u)=\frac{C_\Gamma(u)}{C_\Gamma(0)}.
 \tag{10}
\]

All statements extend to the translation-smooth positive trace-class
heat rows by positive finite-rank approximation in the closed source
form.

## 3. The analytic Fourier multiplier

### Theorem 1 — Exact zero-sampling formula

For every state in (8),

\[
 \boxed{
 \ell_\sigma(\Phi_\Gamma-\chi_K)
 =-\frac{1}{2C_\Gamma(0)}
   \sum_{s\in\mathcal Z}m_s
   \sum_j\gamma_jF_j(s)^2.}
 \tag{11}
\]

Equivalently, on the canonically subtracted autocorrelation class the
analytic Fourier transform of \(\ell_\sigma\) is (2).

#### Proof

The zero side of the polarized completed Weil formula gives, for a real
even row,

\[
 QW(f,f)=\sum_{s\in\mathcal Z}m_sF(s)^2.
 \tag{12}
\]

On the other hand, Theorem 2 of 106.110 gives

\[
 QW(f,f)=-2\ell_\sigma(C_f^\circ).
 \tag{13}
\]

Equations (7), (12) and (13) prove the assertion for one row.  Sum with
the positive coefficients \(\gamma_j\) and divide by (9).  The common
radical subtraction contributes \(\Xi(s)^2=0\) at every sample, proving
(11).  Formula (2) is exactly the functional form of (11).  \(\square\)

The theorem is also a cutoff statement.  The three physical components

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n},
 \qquad
 \frac{e^{-u/2}}{1-e^{-2u}}\,du,
 \qquad
 -2\cosh(u/2)\,du
 \tag{14}
\]

must be paired with the same subtracted autocorrelation before the
cutoff is removed.  Formula (2) is their joint limit; it is not obtained
by Fourier transforming the three divergent pieces separately.

### Corollary 2 — Real-axis multiplier under the critical-line condition

If \(\mathcal Z\subset\mathbb R\), let

\[
 b_\Gamma(\xi)
 =\frac{\sum_j\gamma_j|F_j(\xi)|^2}
        {2\pi C_\Gamma(0)}
 \tag{15}
\]

be the density of \(\beta_\Gamma\).  Then

\[
 \boxed{
 \ell_\sigma(\Phi_\Gamma-\chi_K)
 =-\pi\sum_{\gamma\in\mathcal Z}m_\gamma
        b_\Gamma(\gamma)\le0.}
 \tag{16}
\]

Thus in this case (2) reduces to the negative real point-sampling
distribution

\[
 -\frac12\sum_{\gamma\in\mathcal Z}m_\gamma\delta_\gamma.
 \tag{17}
\]

#### Proof

For real \(\gamma\), every \(F_j(\gamma)\) is real.  Substitute (15)
in (11).  \(\square\)

This corollary is a stress test, not an unconditional step: its
hypothesis is precisely the location statement under investigation.

### Corollary 3 — Off-line orbit and the negative analytic channel

Let \(s=a+ib\), \(ab\ne0\), represent an off-line orbit and write

\[
 F_j(s)=u_j+iv_j.
 \tag{18}
\]

The orbit contributes

\[
 \boxed{
 -\frac{2m_s}{C_\Gamma(0)}
  \sum_j\gamma_j(u_j^2-v_j^2)}
 \tag{19}
\]

to the right side of (11).  In particular it has no fixed sign.

#### Proof

The orbit \(\{s,-s,\bar s,-\bar s\}\), together with reality and
evenness, contributes

\[
 4m_s\operatorname {Re}F_j(s)^2
 =4m_s(u_j^2-v_j^2)
 \tag{20}
\]

to (12).  Multiply by the factor in (11).  \(\square\)

An analytic evaluation at \(a+ib\) is not an order functional on a real
probability measure.  More sharply, the orbit form (20) is indefinite,
whereas integration of a squared real Fourier amplitude against a
positive real multiplier is nonnegative.  Hence no positive real
Fourier multiplier can represent the complete source in the presence of
an off-line orbit.

## 4. The radical equality family forbids a fixed convex-order direction

Let \(X\) have law \(\beta_K\), and denote

\[
 M_{2k}=\mathbb E_{\beta_K}X^{2k}.
 \tag{21}
\]

All these moments are finite, and \(X^2\) is not almost surely constant.
For every real even polynomial \(P\), the row whose transform is

\[
 F_P(\xi)=P(\xi)\Xi(\xi)
 \tag{22}
\]

lies in the complete Riemann radical.  Its Bochner probability measure is

\[
 d\beta_P(\xi)
 =\frac{P(\xi)^2}{\mathbb E_{\beta_K}P(X)^2}\,d\beta_K(\xi),
 \tag{23}
\]

and Theorem 1 gives

\[
 \ell_\sigma(\Phi_P-\chi_K)=0.
 \tag{24}
\]

### Theorem 4 — Two-sided variance motion inside the equality family

There are radical rows \(P_+\) and \(P_-\) such that

\[
 \operatorname {Var}(\beta_{P_-})
 <\operatorname {Var}(\beta_K)
 <\operatorname {Var}(\beta_{P_+}),
 \tag{25}
\]

while both rows satisfy the exact equality (24).

#### Proof

Take \(P_+(\xi)=\xi^2\).  Then

\[
 \operatorname {Var}(\beta_{P_+})=\frac{M_6}{M_4}.
 \tag{26}
\]

Strict positive association of the increasing functions \(y\) and
\(y^2\) of the nonconstant random variable \(Y=X^2\) gives

\[
 M_6-M_2M_4
 =\operatorname {Cov}(Y,Y^2)>0.
 \tag{27}
\]

Therefore \(M_6/M_4>M_2=\operatorname {Var}(\beta_K)\).

For the opposite direction take

\[
 P_c(\xi)=1-c\xi^2,
 \qquad c>0.
 \tag{28}
\]

Its variance is

\[
 V(c)=
 \frac{M_2-2cM_4+c^2M_6}
      {1-2cM_2+c^2M_4}.
 \tag{29}
\]

At \(c=0\),

\[
 V'(0)=-2(M_4-M_2^2)<0.
 \tag{30}
\]

Thus \(V(c)<M_2\) for every sufficiently small positive \(c\).  Use
\(P_-=P_c\).  Both transforms in (22) vanish on the complete zero
divisor, so (24) holds for both.  \(\square\)

All the measures in Theorem 4 are even and hence have the same mean
zero.  Since ordering in convex order forces the corresponding ordering
of second moments, (25) has the following immediate consequence.

### Corollary 5 — Convex-order gate

On any form-core class retaining the exact radical equality anchors,
neither of the universal assertions

\[
 \beta_\Gamma\preceq_{\mathrm{cx}}\beta_K,
 \qquad
 \beta_K\preceq_{\mathrm{cx}}\beta_\Gamma
 \tag{31}
\]

can hold.  In particular, the sign in (1) is not a consequence of a
fixed convex-order orientation relative to \(\beta_K\).

There is an additional quotient issue.  Adding a radical row changes the
real Bochner measure but changes no completed Weil pairing.  Therefore
\(\beta_f\) itself does not descend to the quotient by the full Riemann
radical.  Exact radical anti-shorting must occur before any proposed
frequency-order statement.

## 5. Heat evolution does not create a Bochner order

Let \(T\) be multiplication by \(K\), so \(Tr=Kr\).  For a bounded real
even frequency test \(\varphi\), define the form operator \(B_\varphi\)
by

\[
 \langle r,B_\varphi r\rangle
 =\int_{\mathbb R}\varphi(\xi)
   |\widehat{Kr}(\xi)|^2\frac{d\xi}{2\pi}.
 \tag{32}
\]

Then \(B_1=T^*T\), and for a positive heat state \(\Gamma_t\),

\[
 \mathbb E_{\beta_{\Gamma_t}}\varphi
 =\frac{\operatorname {Tr}(B_\varphi\Gamma_t)}
        {\operatorname {Tr}(B_1\Gamma_t)}.
 \tag{33}
\]

Recall

\[
 \Gamma_t'=-\frac12(S\Gamma_t+\Gamma_tS),
 \qquad S=A+\frac12I.
 \tag{34}
\]

### Theorem 6 — Exact heat derivative of a Bochner observable

Put \(m_\varphi(t)=\mathbb E_{\beta_{\Gamma_t}}\varphi\) and
\(D(t)=\operatorname {Tr}(B_1\Gamma_t)\).  On every common heat-form
core,

\[
 \boxed{
 m_\varphi'(t)
 =-\frac{1}{2D(t)}
   \operatorname {Tr}\!\left(
    \Gamma_t\{S,B_\varphi-m_\varphi(t)B_1\}
   \right).}
 \tag{35}
\]

The right side has no sign forced by positivity of \(S\), \(B_1\), or
\(\Gamma_t\).

#### Proof

Differentiate the numerator and denominator in (33), use (34), and use
trace cyclicity on the common core:

\[
 \frac{d}{dt}\operatorname {Tr}(B_\varphi\Gamma_t)
 =-\frac12\operatorname {Tr}
   \bigl(\Gamma_t\{S,B_\varphi\}\bigr).
 \tag{36}
\]

The quotient rule gives (35).  The anticommutator of two positive
operators need not be positive, so no sign follows without a further
joint arithmetic inequality.  \(\square\)

### Corollary 7 — Eigenmode stationarity and the subthreshold test

If \(Aq=\alpha q\) and the initial state is
\(\Gamma_0=|q\rangle\langle q|\), then

\[
 \Gamma_t=e^{-t(\alpha+1/2)}|q\rangle\langle q|
 \tag{37}
\]

and consequently

\[
 \boxed{\beta_{\Gamma_t}=\beta_q\quad\text{for every }t\ge0.}
 \tag{38}
\]

For a threshold radical mode, (11) is exactly zero for every heat time.
For a hypothetical subthreshold mode \(0<\alpha<1/2\),

\[
 \ell_\sigma(\Phi_q-\chi_K)
 =\frac{1/2-\alpha}{2\|Kq\|_2^2}>0
 \tag{39}
\]

for every heat time.  Thus heat smoothing cannot move the forbidden
measure into a favorable real-frequency order.

## 6. Result and surviving theorem

The following statements are now exact.

* The joint ordinary-prime--Gamma--polar Fourier multiplier on the
  canonically subtracted autocorrelation class is the analytic zero comb
  (2).
* On a critical-line divisor it becomes the negative real point sampler
  (16).
* An off-line orbit is precisely an indefinite analytic evaluation
  channel (19), which cannot be represented by a positive real
  multiplier.
* The Riemann radical equality family moves the real Bochner variance in
  both directions around \(\beta_K\), ruling out either fixed convex-order
  orientation.
* The exact heat derivative of a Bochner observable is the unsigned
  anticommutator covariance (35), and a pure eigenmode has stationary
  normalized Bochner law.

The physical surplus is not proved.  The remaining theorem cannot be a
generic monotone/convex placement statement for \(\beta_{\Gamma_t}\).
It must instead bound the negative analytic evaluation channels in (19)
using a joint property of the literal source (14), after exact radical
anti-shorting and before the character amplitudes are squared.  In the
source-covariance language of 106.110, this is the same missing comparison
between the signed first source and the integrated second-source
dissipation.
