# 112.00 -- Plan for requirement d5 (the effective cone)

## 0. What d5 is, in the language already built

Row (d) of Weil's four ingredients needs, for the classical Hodge-index
argument to run, an **effective cone**: a subset $\mathrm{Eff}$ of the
divisor group such that

* $D \in \mathrm{Eff}$, $D\ne 0$, and $H$ a polarization $\implies D\cdot H>0$;
* $\mathrm{Eff}$ is not merely posited to have this property -- it must be
  *the same* cone that classically means "$D$ is the divisor of an actual
  global section," i.e. $D$ effective $\iff h^0(D)>0$.

107_241 built the pairing $I_\partial$, computed its signature, and identified
the polar block $H_{\mathrm{ruling}}$ with $H=F_v+F_h$, $H^2=2>0$ -- so the
polarization (row analogue) already exists. 107_237 built the divisor
assignment $f\mapsto D_f$ from the DC potential $U_f$ on the square, with
$u_f''(r)=f(r)/r$, and showed $D_f = \int f(\lambda)[\Psi_\lambda]\,d^\times\lambda$
is a *bona fide integral combination of the prime correspondence divisors*
$[\Psi_\lambda]$ (its equation (2.4)). Nothing in either file defines,
or attempts to define, an effective cone. That is the gap this phase closes
or forecloses.

## 1. Pre-registration: what would refute the candidate cone $\{f\ge 0\}$

This section is written **before** any computation below. It commits, in
advance, to falsifiable outcomes, so that a positive result cannot be
manufactured by relaxing the target after seeing the numbers.

The candidate is $\mathrm{Eff} := \{f \in \mathcal A : f\ge 0 \text{ a.e.},\
f\not\equiv 0\}$ (and $D\in\mathrm{Eff}$ iff $D=D_f$ for some such $f$; this
is well posed because $f\mapsto D_f$ is injective, 107_237 §5).

**Task 1 refutation criterion.** The claim is: $f\ge0,\ f\not\equiv 0
\implies I_\partial(D_f,H)>0$. This is refuted if the direct computation of
$I_\partial(D_f,H)$ in evaluation coordinates produces an expression that is
*not* sign-definite under $f\ge0$ -- e.g. if a term with indefinite sign
under $f\ge 0$ appears. (Forecast: it will not be refuted, because $H$ has
no zero-coordinates and the two polar coordinates of $D_f$ are literal
integrals of $f$ against positive weights -- but this must be checked, not
assumed, and the convergence hypotheses on $f$ must be stated candidly.)

**Task 2(ii) refutation criterion.** The claim is that $\{f\ge0\}$ is a
salient convex cone closed under the operations a divisor semigroup needs
(addition, positive scaling). This is refuted if $\{f\ge0\}$ fails closure
under addition (it cannot; sums of nonnegative functions are nonnegative --
this sub-check exists only to be stated, not to manufacture drama) or if it
fails salience, i.e. if there exists $f\not\equiv0$ with $f\ge0$ and
$-f\ge0$ simultaneously (impossible unless $f\equiv 0$ by definition of
$\ge$; again this is a real check, run mechanically, not skipped because
the answer is "obviously" yes).

**Task 2(iii) refutation criterion -- the substantive, falsifiable test.**
The claim under test: for all $f,g\in\mathcal A$ with $f,g\ge0$,
$f,g\not\equiv0$,
$$
I_\partial(D_f,D_g)\ \ge\ 0 .
$$
**This is refuted outright if a single numerical example, computed from
actual nontrivial zeros of $\zeta$ (via `mp.zetazero`, with convergence of
the truncated zero-sum verified by comparing partial sums at increasing
truncation), produces $I_\partial(D_f,D_g)<0$ for some $f,g\ge0$.** No
after-the-fact redefinition of "effective" is permitted to rescue a
negative outcome. A negative outcome is a complete, decisive refutation of
the candidate cone as an intersection-theoretic effective cone (per the
classical fact that effective divisors meet nonnegatively), independent of
whatever Task 1 and Task 2(i)/(ii) find. The search is required to include
configurations designed adversarially to fail: $f,g$ narrow and separated
in scale (their supports far apart on the $r=\lambda$ axis), $f,g$
overlapping, $f=g$, and $f,g$ with comparable but unequal polar mass, at
several widths, run at two truncation depths to confirm the reported sign
is not a truncation artifact.

**Task 2(i) refutation criterion.** The claim under test: $f\ge0$
corresponds to a structurally meaningful "has sections" reading, not merely
to positivity of two integrals. This is refuted -- i.e. demoted from
verdict (a) to (b) -- if the only available correspondence is: (I) the
formal fact that $D_f$ is by definition of $D_f=\int f(\lambda)[\Psi_\lambda]
\,d^\times\lambda$ (107_237 (2.4)) a nonnegative-density combination of the
prime divisors $[\Psi_\lambda]$ when $f\ge0$ -- which is a correct and
non-circular transcription of the classical definition of effective divisor
as a nonnegative combination of primes, but (II) no cohomology functor
$H^0$, no sheaf of sections, and no Riemann-Roch statement has been built
for $\mathcal K_{\mathrm{DC}}/\mathrm{CorrCur}$ on this object -- 107_237 §5
says so explicitly ("does not yet provide ... an $H^1$ theory or RR
existence theorem"). If (I) holds and (II) is confirmed still missing, the
verdict is capped at (b): the cone is right in the *sense available*, but
the *classical* sense ($h^0>0$) is not constructible here yet, so it is a
formal/structural cone, not a cohomological one. This outcome must be
stated as such and not inflated.

**What would make this test worthless.** If every conceivable outcome of
2(iii) were compatible with "the cone is correct" -- e.g. if a negative
sign were explainable away as "well, that's fine, effective divisors are
allowed to meet negatively here" -- the test would carry no information.
It does not: the classical fact that two effective divisors on a surface
meet with $D\cdot D'\ge 0$ (indeed $>0$ unless they share no common
support and behave like disjoint effective classes off the polarization)
is a hard consequence of what "effective" means classically, and failure of
this property for $\{f\ge0\}$ under $I_\partial$ is unambiguous evidence
that $\{f\ge0\}$ is not that classical notion transplanted correctly, i.e.
a genuine refutation, forcing verdict (c) or a sharply qualified (b).

## 2. What is explicitly out of scope

RH is not addressed and is not moved by any outcome here. d5 does not
depend on the other open requirements of the programme (row (a)'s
missing global geometrization, in particular) and this phase does not
attempt to supply them; it only asks whether $\{f\ge0\}$ is a legitimate
effective cone for the pairing and divisor group already built.

## 3. Deliverable map

* `112_01_THE_CANDIDATE_CONE.md`/`.py` -- Task 1.
* `112_02_IS_IT_THE_RIGHT_CONE.md`/`.py` -- Task 2, all three angles.
* `112_03_VERDICT.md`/`.py` -- Task 3.
* `112_99_PHASE_112_SUMMARY.md` + verifier -- roll-up.
