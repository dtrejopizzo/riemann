# 106.59 — The exact localized Birman--Schwinger gate

## Purpose

Document 106.47 proves two facts about the ordinary-prime--Gamma generator
after exact radical shorting: local compactness and the essential spectral
floor \(1/2\). This note asks whether those facts can be turned into a
Birman--Schwinger estimate which excludes the remaining isolated
eigenvalues in \((0,1/2)\).

There is an exact construction. For every spectral parameter
\(\lambda<1/2\), a compactly supported positive boost produces a compact
Birman--Schwinger operator \(\mathcal K_{\lambda,R,M}\). Its eigenvalue \(1\)
detects a subthreshold eigenvalue of the complete generator, with no finite
Euler product and no discarded Gamma or prime-power term.

The construction also gives a decisive gate: the sharp norm estimate
\(\|\mathcal K_{\lambda,R,M}\|\leq1\) is algebraically identical to the
spectral-floor inequality at \(\lambda\). Localization proves compactness,
not the sign. Thus this is a rigorous Fredholm coordinate for the remaining
problem, but not a proof of the missing floor.

## 1. Semantic comparison with the Phase-64 construction

Phase 64 already introduced a Birman--Schwinger operator. Its object was a
Dirichlet Schrödinger model on a finite geometric window,

\[
 G_{\rm Dir}^{1/2}(W_\lambda^{\rm prime}-p_\lambda)^-
 G_{\rm Dir}^{1/2},
\]

and the unproved estimate was that its top eigenvalue does not exceed one.
That route used a pointwise effective potential and the proposed
Dirichlet-window reduction. Its own Section 7 correctly records that the
top-eigenvalue estimate is the original sign problem and that the trace
bound is too lossy at the marginal value one.

The operator below is not identical to that model. It is constructed directly from the
closed nonlocal form of 106.41, after exact infinite-dimensional radical
shorting, and uses the proven PNT tail floor rather than a postulated
Schrödinger potential. All ordinary von Mangoldt atoms and the continuous
Gamma channel remain in its resolvent. This is a standard localized
Birman--Schwinger construction applied in a more faithful coordinate; no
novelty is claimed for the abstract construction. Its logical endpoint is
exactly the Phase-64 wall: both constructions require the same sharp norm
bound.

## 2. The shorted generator and a central boost

Put

\[
 \mathcal H_\perp=(\mathbf1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathcal H_\perp},
\]

and denote its closed form by

\[
 \mathfrak a[f]=\langle f,Af\rangle=\mathscr E_K(f).
\]

Thus, literally,

\[
\begin{aligned}
 \mathfrak a[f]
 ={}&\mathscr E_\Gamma(f)
 +\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \int_{\mathbb R}K(x)K(x-\log n)
   |f(x)-f(x-\log n)|^2\,dx .             \tag{1}
\end{aligned}
\]

No term in (1) is truncated.

Fix

\[
 0<\lambda<a<\frac12.                                  \tag{2}
\]

By Theorem 3 of 106.47, choose \(R\) so that every form-domain function
supported outside \([-R,R]\) satisfies

\[
 \mathfrak a[f]\ge a\|f\|^2.                           \tag{3}
\]

Choose \(v_R\in C_c^\infty(\mathbb R)\), \(0\le v_R\le1\), which is
strictly positive on a neighbourhood of \([-R,R]\). Let \(Q\) be the
orthogonal projection onto \(\mathcal H_\perp\), and on
\(\mathcal H_\perp\) define the bounded positive form

\[
 V_{R,M}=M Q M_{v_R}Q,
 \qquad
 \langle f,V_{R,M}f\rangle
 =M\int v_R|f|^2\,d\mu_K .                             \tag{4}
\]

### Lemma 1 — A finite central boost makes the reference operator coercive

For every pair \((\lambda,a)\) satisfying (2), \(R\) and \(v_R\) can be
chosen as above and then there is a finite \(M>0\) for which

\[
 \boxed{A+V_{R,M}-\lambda\ge c_{\lambda,R,M}I>0.}      \tag{5}
\]

#### Proof

Consider the increasing family of closed forms

\[
 \mathfrak a_M[f]=\mathfrak a[f]
 +M\int v_R|f|^2\,d\mu_K.                             \tag{6}
\]

Its monotone form limit is the restriction of \(\mathfrak a\) to functions
which vanish almost everywhere on \(\{v_R>0\}\). By enlarging the positive
set of \(v_R\) slightly beyond \([-R,R]\), every function in this limiting
domain is supported in the region where (3) holds. Hence the bottom of the
limit operator is at least \(a\).

For completeness, no low-energy mass can disappear in this passage. If a
sequence with unit norm had \(\mathfrak a_M[f_M]\le a-\delta\) while
\(M\to\infty\), then its form norms would be bounded and
\(\int v_R|f_M|^2\to0\). Local compactness from 106.47 gives strong
convergence on the support of \(v_R\). The nonlocal IMS identity of
106.47 then puts all surviving mass in the exterior region, where (3)
gives energy at least \(a\), a contradiction. This is the usual monotone
Dirichlet-bracketing argument, with escape ruled out by the tail floor.

Therefore

\[
 \inf\sigma(A+V_{R,M})\uparrow
 \inf\sigma(A_\infty)\ge a .                          \tag{7}
\]

Since \(\lambda<a\), some finite \(M\) makes the left side larger than
\(\lambda\), which proves (5). \(\square\)

## 3. The exact compact Birman--Schwinger operator

For an admissible triple \((\lambda,R,M)\), write

\[
 B_{\lambda,R,M}=A+V_{R,M}-\lambda>0                  \tag{8}
\]

and define

\[
 \boxed{
 \mathcal K_{\lambda,R,M}
 =B_{\lambda,R,M}^{-1/2}V_{R,M}
  B_{\lambda,R,M}^{-1/2}.}                            \tag{9}
\]

### Theorem 2 — Compactness and exact factorization

The operator in (9) is positive and compact, and

\[
 \boxed{
 A-\lambda
 =B_{\lambda,R,M}^{1/2}
  (I-\mathcal K_{\lambda,R,M})
  B_{\lambda,R,M}^{1/2}}                              \tag{10}
\]

as an identity of closed forms.

#### Proof

Let

\[
 T=\sqrt M\,M_{v_R^{1/2}}Q
 B_{\lambda,R,M}^{-1/2}.                              \tag{11}
\]

A bounded sequence in the range of \(B^{-1/2}\) is bounded in the full
form norm. Since \(v_R\) has compact support, Lemma 1 of 106.47 makes its
image under \(M_{v_R^{1/2}}\) relatively compact in \(L^2\). Thus \(T\)
is compact. Formula (4) gives

\[
 T^*T=B^{-1/2}V_{R,M}B^{-1/2}
 =\mathcal K_{\lambda,R,M},                            \tag{12}
\]

so \(\mathcal K\) is positive and compact. Finally,

\[
 B^{1/2}(I-B^{-1/2}VB^{-1/2})B^{1/2}=B-V=A-\lambda,
\]

which is (10). \(\square\)

### Corollary 3 — Exact detection of a bound state

For every admissible triple,

\[
\begin{aligned}
 A\ge\lambda
 &\Longleftrightarrow \mathcal K_{\lambda,R,M}\le I,\tag{13}\\
 \lambda\in\sigma_{\rm p}(A)
 &\Longleftrightarrow 1\in
   \sigma_{\rm p}(\mathcal K_{\lambda,R,M}).         \tag{14}
\end{aligned}
\]

The multiplicities in (14) agree. In particular, a subthreshold
eigenvalue \(\nu\in(0,1/2)\) is detected by the eigenvalue \(1\) of
\(\mathcal K_{\nu,R,M}\).

This is the localized Fredholm alternative promised by the essential-floor
theorem.

## 4. The sharp norm calculation

The useful feature of (9) is also the obstruction. If
\(u=B^{1/2}f\ne0\), then

\[
 \boxed{
 \frac{\langle u,\mathcal Ku\rangle}{\|u\|^2}
 =\frac{M\int v_R|f|^2\,d\mu_K}
 {\mathfrak a[f]+M\int v_R|f|^2\,d\mu_K
       -\lambda\|f\|^2}.}                            \tag{15}
\]

Consequently

\[
\begin{aligned}
 1-\frac{\langle u,\mathcal Ku\rangle}{\|u\|^2}
 =\frac{\mathfrak a[f]-\lambda\|f\|^2}
 {\mathfrak a[f]+M\int v_R|f|^2\,d\mu_K
       -\lambda\|f\|^2}.                             \tag{16}
\end{aligned}
\]

Thus

\[
 \boxed{
 \|\mathcal K_{\lambda,R,M}\|\le1
 \quad\Longleftrightarrow\quad
 \mathfrak a[f]\ge\lambda\|f\|^2
 \quad(f\in\mathcal H_\perp).}                      \tag{17}
\]

The localization term cancels exactly. Substituting (1) into the right
side of (17) recovers the complete ordinary-prime--Gamma inequality, with
the same radical constraint as before. In particular,

\[
 \boxed{
 A\ge\frac12
 \Longleftrightarrow
 \|\mathcal K_{\lambda,R,M}\|<1
 \text{ for every }0<\lambda<\frac12.}               \tag{18}
\]

In the forward direction one even has, because \(0\le v_R\le1\),

\[
 \|\mathcal K_{\lambda,R,M}\|
 \le\frac{M}{M+1/2-\lambda}<1.                       \tag{19}
\]

But (19) uses the desired floor. It cannot be run in reverse from PNT or
from local compactness.

## 5. Why the tail floor cannot supply the missing norm bound

The analytic inputs of 106.47 determine the essential spectrum but do not
exclude a central bound state. This is not peculiar to the arithmetic
operator. On \(L^2(\mathbb R)\), start with

\[
 H_0=-\partial_x^2+\frac12
\]

and perturb it by a compactly supported attractive rank-one form

\[
 H_\tau=H_0-\tau|\phi\rangle\langle\phi|,
 \qquad \phi\in C_c^\infty(\mathbb R).               \tag{20}
\]

For suitable \(\tau>0\), \(H_\tau\) has an eigenvalue in \((0,1/2)\), while
its local embedding is compact and every function supported away from
\(\mathrm{supp}\,\phi\) still obeys the exact tail floor \(1/2\).
The localized Birman--Schwinger operator then has eigenvalue one at that
bound-state energy. Hence local compactness plus a \(1/2\) tail floor can
never prove the strict norm bound.

For the literal operator, the additional data are precisely the central
arrangement of the weights \(\Lambda(n)\), the Gamma channel, the theta
kernel and polar centering. Formula (15) shows that any estimate of their
Birman--Schwinger norm at one is already an estimate of their original
joint form. No Schur test follows merely from \(\Lambda(n)\ge0\): after the
projection \(Q\), neither the compressed resolvent nor its kernel is
positivity preserving, and the cancellation required at the threshold is
not atomwise.

## 6. Verdict and usable output

The localized Birman--Schwinger route supplies three rigorous facts:

1. every possible violation of the complementary floor is encoded by an
   eigenvalue of a **compact** operator, so the remaining obstruction is a
   genuine Fredholm bound state rather than essential spectrum;
2. the compact operator is built from the complete literal
   von-Mangoldt--Gamma generator, not from a finite Euler product or an
   assumed local potential; and
3. its sharp norm inequality is exactly (17), so a proof cannot be obtained
   from IMS localization or the PNT tail floor alone.

Accordingly, this route does not yield a QED. A closing estimate still has
to use a new central arithmetic identity which controls the joint form in
(1), or equivalently the projection-constrained three-point current of
106.48. The Birman--Schwinger construction is a valid compact coordinate
for that estimate, but it does not weaken it.
