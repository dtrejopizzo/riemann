# 106.38 — The full theta-remainder decomposition

## Purpose

The absorption target of 106.37 cannot be proved by estimating its
off-line evaluation channel directly: an off-line orbit can be isolated by
Paley--Wiener interpolation.  The proof must therefore be constructed on
the ordinary-prime side.

Document 106.32 used Riemann's theta dilation to obtain a lower bound for
each prime-power jump.  That lower bound discarded two positive pieces:

1. the theta indices not divisible by the prime power; and
2. the central crossing interval between the two reflected theta tails.

The exact radical family shows that those pieces cannot be discarded in a
sharp proof.  This note retains them and gives an exact three-channel
decomposition of every jump.  It produces the first source-side gradient
which contains all the information required by the absorption inequality.
The remaining obligation is a norm-one global contraction from the polar
variance gradient to this complete theta gradient.

No zero location is used below.

## 1. Continuous theta atoms

For \(y>0\) and \(x\geq0\), write

\[
 k_y(x)=\pi y^2e^{5x/2}
 \bigl(2\pi y^2e^{2x}-3\bigr)e^{-\pi y^2e^{2x}},
 \tag{1}
\]

with the same harmless common normalization as in 106.32.  Then

\[
 K(x)=\sum_{m\geq1}k_m(x)
 \qquad(x\geq0).
 \tag{2}
\]

For the integer atoms appearing in (2), all terms are positive for
\(x\geq0\), since \(2\pi m^2e^{2x}-3>0\).  Direct substitution gives the
continuous scaling law

\[
 \boxed{k_{ny}(x-\log n)=n^{-1/2}k_y(x)}
 \qquad(n\geq2,\ x\geq\log n).
 \tag{3}
\]

Consequently,

\[
 \begin{aligned}
 K(x-\log n)
 &=n^{-1/2}\sum_{j\geq1}k_{j/n}(x)\\
 &=n^{-1/2}K(x)+R_n(x),
 \end{aligned}
 \tag{4}
\]

where

\[
 \boxed{
 R_n(x)=n^{-1/2}
 \sum_{\substack{j\geq1\\n\nmid j}}k_{j/n}(x)>0}
 \qquad(x\geq\log n).
 \tag{5}
\]

In (5), \(j/n\) can be smaller than one; positivity nevertheless follows
from the first expression in (4), because it is the difference between
the full sum and precisely its divisible subsum.  Equivalently, each term
in (5) equals \(k_j(x-\log n)>0\) before applying (3).

## 2. Exact reflection splitting of one jump

For an even multiplier \(r\), recall

\[
 \mathcal J_a(r)=\int_{\mathbb R}K(x)K(x-a)
 |r(x)-r(x-a)|^2\,dx.
 \tag{6}
\]

### Theorem 1 — Three-channel theta decomposition

Let \(n\geq2\) and \(a=\log n\).  Then

\[
 \boxed{
 \begin{aligned}
 \mathcal J_a(r)
 ={}&2n^{-1/2}\int_a^\infty K(x)^2
             |r(x)-r(x-a)|^2\,dx\\
 &+2\int_a^\infty K(x)R_n(x)
             |r(x)-r(x-a)|^2\,dx\\
 &+\int_0^aK(x)K(a-x)
             |r(x)-r(a-x)|^2\,dx .
 \end{aligned}}
 \tag{7}
\]

Every term on the right of (7) is nonnegative, and (7) is an identity,
not a lower estimate.

#### Proof

Split (6) into \(( -\infty,0]\), \([0,a]\), and \([a,\infty)\).
In the first integral put \(y=a-x\).  Evenness of \(K\) and \(r\)
turns it exactly into the integral over \([a,\infty)\).  On the central
interval, evenness changes \(K(x-a)\) and \(r(x-a)\) into
\(K(a-x)\) and \(r(a-x)\).  Therefore

\[
 \mathcal J_a(r)
 =2\int_a^\infty K(x)K(x-a)|\Delta_ar(x)|^2\,dx
  +\int_0^aK(x)K(a-x)|r(x)-r(a-x)|^2\,dx.
 \tag{8}
\]

Insert (4) in the first integral.  This gives the first two lines of
(7), while the central term is unchanged. \(\square\)

## 3. Exact decomposition of the full prime energy

Define the divisor channel already present in 106.32 by

\[
 \widetilde{\mathscr E}_p(r)
 =2\sum_{n\geq2}\frac{\Lambda(n)}n
 \int_{\log n}^\infty K(x)^2
 |r(x)-r(x-\log n)|^2\,dx.
 \tag{9}
\]

Define the fractional-theta and central-crossing channels by

\[
 \begin{aligned}
 \mathscr X_{\rm frac}(r)
 &:=2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
 \int_{\log n}^\infty K(x)R_n(x)
 |r(x)-r(x-\log n)|^2\,dx,\\
 \mathscr X_{\rm ctr}(r)
 &:=\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
 \int_0^{\log n}K(x)K(\log n-x)
 |r(x)-r(\log n-x)|^2\,dx.
 \end{aligned}
 \tag{10}
\]

### Corollary 2 — No theta information is lost

On the full-kernel form domain,

\[
 \boxed{
 \mathscr E_p(r)
 =\widetilde{\mathscr E}_p(r)
  +\mathscr X_{\rm frac}(r)
  +\mathscr X_{\rm ctr}(r).}
 \tag{11}
\]

#### Proof

Multiply (7) by \(\Lambda(n)/\sqrt n\), sum over \(n\), and use
monotone convergence.  Each integrand is nonnegative.  Double-exponential
decay of \(K\) gives finiteness on the smooth compact multiplier core and
then closure gives the stated domain. \(\square\)

Equation (11) corrects the lossy step of 106.32.  That document retained
only the first term on the right.  The discarded amount is now the explicit
positive form

\[
 \mathscr X_{\rm frac}+\mathscr X_{\rm ctr}.
 \tag{12}
\]

## 4. The exact absorption target in the new coordinate

Combining (11) with the full-kernel identity of 106.31 gives

\[
 \boxed{
 QW(Kr,Kr)
 =\mathscr E_\Gamma(r)
  +\widetilde{\mathscr E}_p(r)
  +\mathscr X_{\rm frac}(r)
  +\mathscr X_{\rm ctr}(r)
  -\frac12\mathrm{Var}_{\mu_K}(r).}
 \tag{13}
\]

Thus the ordinary-prime absorption inequality is equivalent to

\[
 \boxed{
 \frac12\mathrm{Var}_{\mu_K}(r)
 \leq
 \mathscr E_\Gamma(r)
 +\widetilde{\mathscr E}_p(r)
 +\mathscr X_{\rm frac}(r)
 +\mathscr X_{\rm ctr}(r).}
 \tag{FTC}
\]

The difference from the previous canonical-path target is substantive:
FTC keeps the nondivisible rational theta indices and the entire central
crossing region.  It is therefore compatible with equality on every exact
Riemann-radical multiplier.

Indeed, for

\[
 r_j=K^{(2j)}/K,
 \tag{14}
\]

106.31 gives equality in FTC.  Consequently any proof of FTC must use all
four channels without leaving a strictly positive local remainder on an
\(r_j\).

## 5. Gradient formulation

Let \(D_\mu r(x,y)=2^{-1}(r(x)-r(y))\) in
\(L^2(\mu_K\otimes\mu_K)\), restricted to the centered subspace.  Let
\(G_\Gamma,G_{\rm div},G_{\rm frac},G_{\rm ctr}\) be the four weighted
difference maps whose squared norms are the four terms on the right of
FTC, and put

\[
 \mathcal G r
 =G_\Gamma r\oplus G_{\rm div}r
  \oplus G_{\rm frac}r\oplus G_{\rm ctr}r.
 \tag{15}
\]

Then FTC is

\[
 \|D_\mu r\|\leq\|\mathcal G r\|.
 \tag{16}
\]

By the Douglas factorization lemma, (16) is equivalent to the existence of
a contraction \(C\), defined on the closure of the complete theta-gradient
range, such that

\[
 \boxed{D_\mu=C\mathcal G,\qquad\|C\|\leq1.}
 \tag{17}
\]

Unlike the formal contraction obtained by defining
\(C=D_\mu\mathcal G^\dagger\), a closing construction must give \(C\)
directly from the theta/divisor geometry and prove its norm before invoking
FTC.  Formulae (5), (10) and (15) specify every source fiber on which such
a construction must act.

## 6. Nonduplication and present status

The following candidates were checked before selecting (17).

* Birman--Schwinger and Feshbach reductions were already exhausted in
  Phases 64 and 72--90 and reproduce the unknown top eigenvalue.
* Stein--Mecke, the divisor Markov selector and the full finite additive
  cumulant hierarchy were exhausted in Phase 104.
* The expander/canonical-path proof of 106.36 and the reduced theta bound
  of 106.32 discard exactly the two channels restored in (10)--(12).

The new proved content here is the exact, non-lossy decomposition (7) and
(11), including its fractional-theta realization (5).  The remaining
force-bearing statement is the explicit construction of the contraction
(17).  It has not yet been proved.  Establishing it would prove FTC, the
absorption inequality of 106.37, the semilocal complement floor, and RH.
