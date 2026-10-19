# 104_56B — Background audit of the relaxed density criterion

## Executive verdict

The decomposition into dominant exterior modes and the conclusion
"if RH fails, there are exponentially negative Li coefficients infinitely
often" **are not new**. They are in Bombieri–Lagarias and appear in
explicit trigonometric form, for \(\tau\)-Li coefficients, in Bucur–Ernvall-
Hytönen–Odžak–Smajlović.

In the directed search described below I did not find in a primary
source the exact strengthenings

\[
 \neg\mathrm{RH}\Longrightarrow
 \{n:\lambda_n<0\}\text{ contains a syndetic set of positive density},
\tag{1}
\]

nor the equivalent criteria

\[
\begin{aligned}
 \mathrm{RH}
 &\Longleftrightarrow
 4\lambda_n>A_n\text{ outside an exception of zero logarithmic density},
 \tag{2}\\
 \mathrm{RH}
 &\Longleftrightarrow
 \text{there exist consecutive blocks of unbounded length where }
 4\lambda_n>A_n.
 \tag{3}
\end{aligned}
\]

The correct novelty level is therefore:

> **apparently unrecorded strengthening of a known proof**, obtained by
> adding uniform recurrence/equidistribution on the compact orbit closure
> to the dominant term of Bombieri–Lagarias; it is not a new analytic bound
> for the zeros nor a proof of A1.

"Not found" is not equivalent to a priority proof. Before claiming
editorial novelty a broader professional bibliographic search and
consultation with specialists would be needed.

---

## 1. Exact primary background

### 1.1 Bombieri–Lagarias (1999)

E. Bombieri and J. C. Lagarias, *Complements to Li's criterion for the
Riemann hypothesis*, J. Number Theory **77** (1999), 274--287,
[DOI 10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392).

Their Theorem 1 gives, for the abstract admissible multiset, the equivalence
between the localization \(\Re\rho\le1/2\), the positivity of all oriented Li
sums, and a subexponential lower bound for all degrees. The proof isolates
the transformed points of maximal exterior modulus and uses simultaneous
Diophantine approximation. If the localization fails, it obtains negative
values of exponential size **infinitely often**. The paper does not state
in its theorem a natural/logarithmic density of those degrees, nor
syndeticity.

### 1.2 Voros (2006)

A. Voros, *Sharpenings of Li's criterion for the Riemann Hypothesis*,
Math. Phys. Anal. Geom. **9** (2006), 53--63,
[arXiv:math/0506326](https://arxiv.org/abs/math/0506326),
[DOI 10.1007/s11040-005-9002-8](https://doi.org/10.1007/s11040-005-9002-8).

The abstract and the asymptotics distinguish the growth
\(n(A\log n+B)\) under RH from the non-tempered oscillatory behavior if RH
is false. This anticipates the "exponential exterior mode" diagnosis, but it
does not formulate (1)--(3).

### 1.3 Bucur–Ernvall-Hytönen–Odžak–Smajlović (2016)

A. Bucur, A.-M. Ernvall-Hytönen, A. Odžak and L. Smajlović,
*On a Li-type criterion for zero-free regions of certain Dirichlet series
with real coefficients*, LMS J. Comput. Math. **19** (2016), 259--280,
[Cambridge PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9D6498CFDB802707E1A0EDFFE5B81C34/S1461157016000115a.pdf/on-a-li-type-criterion-for-zero-free-regions-of-certain-dirichlet-series-with-real-coefficients.pdf),
[DOI 10.1112/S1461157016000115](https://doi.org/10.1112/S1461157016000115).

This is the closest piece of background. Its equation (3.9), p. 266, exhibits for
the maximal-modulus modes a term of the form

\[
 -2(1+m)^n\sum_{j=1}^k\cos(n\phi_j)
\tag{4}
\]

plus terms of strictly smaller radius and a polynomial error. Immediately
afterward they apply simultaneous Diophantine approximation and conclude that the
coefficient is negative, with exponential amplitude, infinitely often. In the
discussion on pp. 278--279 they describe the same mechanism again. The text
does not contain the terms *density* or *positive proportion* for the set
of degrees, and does not state syndeticity or (2)--(3).

### 1.4 Lagarias (2007), for the direction under RH

J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst.
Fourier **57** (2007), 1689--1740,
[Centre Mersenne PDF](https://aif.centre-mersenne.org/item/10.5802/aif.2311.pdf),
[DOI 10.5802/aif.2311](https://doi.org/10.5802/aif.2311).

Under RH it obtains the asymptotic

\[
 \lambda_n=A_n+O(\sqrt n\log n)
\tag{5}
\]

in the zeta normalization used by Phase 104. Since
\(A_n\sim\frac12n\log n\), (5) gives \(4\lambda_n>A_n\) for every
sufficiently large degree. This is the direction RH \(\Rightarrow\) (2),(3);
the label **conditional on RH** must be kept explicit.

---

## 2. What 104_56 exactly adds

The published input has the form

\[
 \lambda_n=-R^n F(n\alpha)
 +O\!\left(n^2R_1^n+n^2\right),
 \qquad 1<R_1<R,
\tag{6}
\]

where \(F(x)=\sum_{j=1}^K\cos x_j\), after absorbing the harmless constant
terms into the error. Let

\[
 H=\overline{\{n\alpha:n\in\mathbb Z\}}\subset\mathbb T^K.
\tag{7}
\]

Translation by \(\alpha\) is minimal and uniquely ergodic on the
compact monothetic group \(H\). For a regular level
\(K/2<\eta<K\), the open set

\[
 U_\eta=\{x\in H:F(x)>\eta\}
\tag{8}
\]

contains the origin and has boundary of zero Haar measure. Hence its
return times

\[
 D_\eta=\{n:n\alpha\in U_\eta\}
\tag{9}
\]

have natural density \(\mu_H(U_\eta)>0\). Minimality plus compactness
further gives that \(D_\eta\) is syndetic. On \(D_\eta\), (6) is negative and
of size \(\gg R^n\) past a prefix.

Thus the jump from "infinitely often" to "positive density and syndetic
set" uses no new information about \(\zeta\). It uses a stronger
topological-dynamical consequence of the same finite trigonometric sum.

The absence of a universal density \(\delta_0>0\) is also important:
the family of Fejér kernels of 104_56 shows that, within the abstract
Bombieri–Lagarias class, the measure of the returns forcing a negative sign
can tend to zero. For fixed zeta there is some
\(d_\zeta>0\) under \(\neg\mathrm{RH}\), but no universal numerical
constant comes out of those axioms.

---

## 3. Internal repository audit

The essential algebra was already present internally:

* `phase-102/.../136_FINITE_EXTERIOR_SHELL_DOMINANCE.md` uses the orbit
  closure on a torus and obtains a negative geometric subsequence;
* `phase-102/.../138_ZETA_EXTERIOR_RADIUS_MAXIMUM.md` proves that a zero of
  zeta off the line produces a finite maximal exterior shell;
* `phase-102/.../139_ZERO_SIDE_LI_CRITERION_CLOSURE.md` assembles that
  zero-side discrimination.

These documents say "infinite subsequence," not positive density nor
syndeticity. So the new internal part of 104_56 is the strengthening of
the quantifier and its logical corollaries, not the exterior shell.

This should be read together with:

* `257_AVERAGED_SLACK_POINTWISE_NO_GO.md`;
* `278_COFINAL_SUBSEQUENCE_CERTIFICATE_NO_GO.md`.

Both remain correct for the literal obligation
"A1 at every coordinate." A density-one theorem does not prove the omitted
indices of A1. What is new is that it can **avoid that internal obligation**
and close RH directly via (1). It must not be claimed simultaneously that
A1 has been proved for all \(n\).

---

## 4. Two technical precautions

1. The dominant orientation must be fixed as
   \(u_\rho=\rho/(\rho-1)\) when using \(\lambda_{-n}=\lambda_n\).
   Mixing it with \((\rho-1)/\rho\) flips which half of the quadruple is
   exterior.
2. Criteria (2)--(3) only need the full coefficient
   \(\lambda_n\). The additional formula of 104_56 for
   \(\lambda_n(\sqrt n)\) was not located as a published statement in this
   audit and must keep its own proof; it is not needed for
   syndeticity nor for the relaxed criteria.

---

## 5. Search scope

I explicitly searched, up to the 26th, combinations of
*Li/Keiper coefficients* with *syndetic*, *positive density*, *natural
density*, *logarithmic density*, *density one* and *arbitrarily long blocks*
on arXiv, publisher pages and public mathematical repositories. After
building `104_61` the search was repeated with *Fermi–Dirac*, *logistic
partition*, *bounded nonlinear detector* and *degree partition*. The
earlier primary texts and the nearby references that appeared in that
search were reviewed. No blogs or manuscripts claiming RH were used as
mathematical background.

**Final classification:**

| Claim | Bibliographic status |
|---|---|
| Maximal exterior shell and exponential trigonometric term | known |
| Infinitely-often exponential negativity if RH fails | known |
| Negativity on a set of positive natural density | not found explicitly; short corollary |
| Syndeticity of the forcing set | not found explicitly; short corollary |
| Criterion with a zero-logarithmic-density exception | not found explicitly |
| Criterion via good blocks of unbounded length | not found explicitly |
| Bounded Fermi detector equivalent to RH | not found; functional corollary of syndeticity |
| Regulated prime–Laguerre lift of the Fermi detector | not found |
| Universal positive-density constant | not valid in the abstract BL class |
