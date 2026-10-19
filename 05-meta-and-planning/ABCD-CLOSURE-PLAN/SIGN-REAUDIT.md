# Re-audit of the sign of D —

**State: D open.** Three independent reviews respectively covered
blocks 0–134, 135–161, and 162–175 via maps, closures, and selected
proofs. A full reading of the 8829 inventoried research files is not
claimed. The main audit corrected the proposals before recording them.
There is no proof of the global sign in this round, nor a claim of novelty
in the literature.

## 1. Scope of the exclusions

- R158_003, A10, already corrects "no uniform margin implies a proof by identity."
  A scale-dependent bound is not excluded by that argument.
- R170_841, §6.1, does obstruct a relative bound on the dilation derivative
  valid for all vectors: the prime derivative grows linearly with the
  frequency and changes sign. It does not contradict a bound restricted to
  special states, whose proof is still missing.
- R172 does not prove that Euler plus the functional equation implies RH by exclusion.
  That each condition alone is insufficient does not show that together they suffice.
- R175 does not prove the nonexistence of a suitable geometry. It records the absence
  of a positive form and of its exact transfer, not a universal classification.

Sources: [R158_003](../../03-research/phase-158-row-d-mw5-object/R158_003_AUDIT_SPEC.md),
[R170_841](../../03-research/phase-170-global-prime-inequality/R170_841_VIRIAL_LB.md),
[R172](../../03-research/phase-172-p171-probe/R172_FINAL.md),
[R175](../../03-research/phase-175-third-coordinate/R175_FINAL.md).

## 2. Preserved arithmetic inequality and proved limit

**PROVED.** Define, with the ordinary von Mangoldt function,

\[
\beta(n)=2\sum_{d\mid n}\Lambda(d)\log d-(\log n)^2,
\qquad B(s)=\sum_{n\ge2}\beta(n)n^{-s}.
\]

For every real \(s\ge2\),

\[
B(s)\ge\tfrac14\zeta(s)
 \sum_p\frac{(\log p)^2p^s}{(p^s-1)^2}>0.
\tag{1}
\]

Proof. All the following series converge absolutely for \(\Re s>1\),
since \(|\beta(n)|\le(\log n)^2\), a consequence of
\(\sum_{d\mid n}\Lambda(d)=\log n\). Writing

\[
f(s)=\sum_p\frac{\log p}{p^s-1}=-\frac{\zeta'}{\zeta}(s),\qquad
g(s)=\sum_p\frac{(\log p)^2p^s}{(p^s-1)^2},
\]

the Dirichlet convolution gives

\[
B=\zeta''-2\frac{(\zeta')^2}{\zeta}=\zeta(g-f^2).
\]

Cauchy–Schwarz, applied with factors
\((\log p)p^{s/2}/(p^s-1)\) and \(p^{-s/2}\), gives
\(f^2\le g\sum_p p^{-s}\). Finally,

\[
\sum_p p^{-s}\le\sum_{n=2}^{\infty}n^{-2}
\le\frac14+\int_2^\infty x^{-2}\,dx=\frac34.
\]

This proves (1). For every positive, finite, nonzero measure \(\nu\)
on \([2,\infty)\), one also obtains

\[
\sum_{n\ge2}\beta(n)\psi(\log n)>0,
\qquad \psi(x)=\int_{[2,\infty)}e^{-sx}\,d\nu(s).
\tag{2}
\]

The interchange of integral and series uses
\(\sum(\log n)^2n^{-2}<\infty\), not positivity of the coefficients.

**PROVED: (1) does not survive arbitrary modulations.** Fix
\(t_0=\pi/\log2\). Then

\[
\lim_{s\to+\infty}2^s\Re B(s+it_0)=-(\log2)^2<0.
\tag{3}
\]

Indeed, \(\beta(2)=(\log2)^2\), and its phase is \(-1\).
The remainder tends to zero by dominated convergence, since for \(s\ge2\)
\(|\beta(n)|(2/n)^s\le4(\log n)^2/n^2\). So a positive exponential
weight does orient this channel, but multiplying it by the oscillation
\(\cos(t_0\log n)\) destroys the sign even in absolute convergence.

Moreover, every \(\psi\) from (2) is strictly positive at every \(x>0\).
So no nonzero compactly supported weight literally belongs
to that cone. A representation of the full physical test via (2)
would need an additional theorem about its outer terms, Gamma, and
poles. That theorem was not proved.

**NO-GO for this round's proposal:** presenting (1) or (2) as the
sign of D omits the modulations and the archimedean coupling. The lemma
is correct; the transfer is not proved. It also does not by itself separate
the Beurling falsifiers. The review's claim about
all decreasing weights is withdrawn: a localized bump is not a counterexample
within that class.

## 3. Direct proof against the proposed relative propagation

The abstract Grönwall lemma is correct: on a common domain, if
\(q_r(F)\) is locally absolutely continuous,
\(q'_r(F)\ge-C(r)q_r(F)\), \(C\in L^1_{\rm loc}\), and
\(q_{r_0}(F)\ge0\), then \(q_r(F)\ge0\) for \(r\ge r_0\).
What fails is the hypothesis proposed for the physical form over the whole domain.

**PROVED, for unrestricted dilation transport.** Let
\(\tfrac12\log2<T<\tfrac12\log3\),
\(U_rF(t)=r^{-1/2}F(t/r)\), and \(q_r(F)=W(U_rF)\).
There is no finite constant \(C\) such that
\(q'_1(F)\ge-Cq_1(F)\) for every \(F\in C_c^\infty(-T,T)\).

Proof. Choose \(\phi\) real, smooth, and nonnegative, with support in
\((-T,T)\), unit norm and \(a(\log2)>0\), where
\(a(u)=\int\phi(t)\phi(t-u)dt\). Set
\(F_\xi(t)=\phi(t)e^{i\xi t}\). Then
\(c_{F_\xi}(u)=a(u)e^{i\xi u}\).
In a neighborhood of \(r=1\) only the prime 2 is involved. Its contribution to
\(q'_1\), using \(c_{U_rF}(u)=c_F(u/r)\), is

\[
\frac{2(\log2)^2}{\sqrt2}
 \left[a'(\log2)\cos(\xi\log2)
       -\xi a(\log2)\sin(\xi\log2)\right].
\]

The archimedean contribution to \(q_1\) is
\(\log\xi+O(1)\); its derivative is bounded because
\(\tau m'(\tau)\) is bounded. These are the Gamma-kernel estimates
used in R170_841 §6.1. The polar terms and their derivatives decay
faster than any power by integration by parts.
For \(\xi_j\log2=\pi/2+2\pi j\), it follows that

\[
q_1(F_{\xi_j})=\log\xi_j+O(1),\qquad
q'_1(F_{\xi_j})=-c\xi_j+O(1),\quad c>0.
\]

This contradicts the bound for any finite \(C\). The same argument
applies at every nearby scale, after transporting the test; this is not
an isolated exception that could be omitted from an almost-everywhere statement.
The extension to primitive sectors requires the Tate frame; R170_841 §6.1
handles that correction. No arbitrary connection to simple transport is
identified here, nor is every possible relative estimate excluded.

The repair restricted to low-energy states still needs a proof.
It is not enough for the restriction to remove the counterexample: an
evolution law must be proved within that restriction, and the coupling with
its complement must be controlled.

## 4. Other withdrawn proposals

The bispectrum over prime powers only relates powers of the same
base; its positivity for positive coefficients transports to free
semigroups. The fourth moment is a universal norm. Neither provides the
mixed sign required.

The independence of rational translates is correct, but universal:
for any \(G\ne0\) in \(L^2(\mathbb R)\), the translates by
distinct \(\log(m/n)\) are linearly independent. A finite relation,
Fourier-transformed, would annihilate an exponential polynomial on a
set of positive measure; its analyticity forces all its
coefficients to be zero. For coprime pairs \(1\le m,n\le M\) there are
\(2\sum_{k\le M}\varphi(k)-1\) directions. This proves neither effectivity,
a Hodge index, a lower Gram bound, nor separation of falsifiers.
It is not recorded as progress toward the sign.

## 5. Outcome of the round

Inequality (1) is proved, with its exact domain. Proof (3)
prevents extrapolating it to the oscillatory problem; the proposed propagation
over the whole domain is refuted. No proposal produced an
inequality for the full mixed term. **The requested solution
was not obtained, nor a closure of D.** The papers are not modified, and no
new phase is opened on the basis of these auxiliary results.
