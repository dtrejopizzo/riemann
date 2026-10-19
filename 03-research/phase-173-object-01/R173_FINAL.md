# R173 FINAL — Construction of the object (0.1)

**Verdict: NO-GO.** After rounds 0–3 no Hermitian form was built that
simultaneously satisfies (Q1)–(Q4). The following theorems close the
concrete families examined. They do not prove the impossibility of any
future construction in (a), (b), or (c); hence the additional mandate to
close them "forever" remains **NO-GO**.

## Round 0 — corpus (PROVED)

In the space of adele classes, positive norms prior to the spectrum omit
the non-critical zeros, while the compatible form that sees all the zeros
is Weil/E1. Prop. H excludes polarizations of finite exponential type and
N-a requires positivity prior to the spectrum
([R158_005](../phase-158-row-d-mw5-object/R158_005_CLOSING_DECISION.md),
[R158_006](../phase-158-row-d-mw5-object/R158_006_O0_MEYER_K.md)).
T6 and Rankin–Selberg close the magnitude positivities that only recover
the density frontier ([R151_005](../phase-151-row-d-the-bridge/R151_005_CLOSING_DECISION.md);
phases 139, 146, and 168). The weight-\(1/2\) theta with \(T_{p^2}\) had not
been tried exactly. No windows, ledgers, or D reductions were repeated.

## (a) Adelic Schwartz–Bruhat — NO-GO

**Maximal theorem (PROVED).** In
\(L^2(\mathbb R_+^\times,d^\times x)\), let

\[
 E_X=\sum_{n\le X}{\Lambda(n)\over\sqrt n}\,U_n,
 \qquad (U_nf)(x)=f(x/n).
\]

Its Mellin multiplier satisfies, by PNT and partial summation,

\[
 \sum_{n\le X}{\Lambda(n)\over n^{1/2+it}}
 ={X^{1/2-it}\over1/2-it}+o_t(X^{1/2}).
\]

Thus \(E_Xf\) converges strongly only for \(f=0\), and
\(\liminf_X\|E_Xf\|=\infty\) for \(f\ne0\). If a bounded Euler operator
\(A\) has dense range and \(q\) is a continuous Hermitian form, then
\(q(Af)\ge0\) for every \(f\) implies \(q\ge0\) by density: Euler remains
inert on the sign. Finally, \(q_A(f)=\|Af\|^2\), also for closable singular
\(A\), is positive for a formal reason independent of Euler and Poisson, and
fails (Q3). This excludes the raw Euler sums, the dense-range continuous
insertions, and the norms/GNS constructions examined; it does not exclude every
renormalized adelic crossed form.

## (b) Jacobi theta and \(T_{p^2}\) — NO-GO

**Maximal theorem (PROVED).** Let
\(\mathcal M=W^*(T_{p^2}:p\ {\rm prime})\). The joint spectral
decomposition reduces norms, traces, and positive functional calculus of
\(\mathcal M\) fiber by fiber. The Jacobi theta is a joint eigenvector;
hence

\[
 Q_B(\theta)=|\chi_\theta(B)|^2\,\|\theta\|^2
 \qquad (B\in\mathcal M).
\]

On the full automorphic space, the positivity reason is universal and
does not fail when changing fiber; the defects of \(P_{171}\) and
Davenport–Heilbronn occur when trying to simultaneously realize Poisson and
the Hecke character, not in the sign proof. Hence it fails (Q3). On the
theta block, the sign is the scalar positivity of the character and
produces no zero bound: it fails (Q4). This excludes functional calculus, norms, and
positive traces within \(\mathcal M\); it does not exclude a polarization mixing
blocks outside that algebra.

## (c) Weil–Connes — NO-GO

**Maximal theorem (PROVED).** The standard realizations form a
trichotomy. (i) \(L^2_\delta\) is positive prior to the spectrum, but the
proof of the sign does not use the Euler–Poisson coupling and the space
only realizes critical zeros. (ii) The nuclear \(H^1\) of Meyer–CCM contains
all the zeros and its character couples Euler with Poisson, but the
positivity of the Rosati–trace form is Weil's criterion, equivalent to RH.
(iii) Connes's compressions are positive, but they use forbidden cutoffs
and transferring their sign to the global distribution is equivalent to RH.

\(P_{171}\) fails on the additive lattice
\(\mathbb Q\subset\mathbb A_{\mathbb Q}\) and on an adelic Poisson
compatible with its Euler product; Davenport–Heilbronn fails on the local
Tate/Meyer factors. The abstract norms remain positive, so they do not
pass (Q3). The trichotomy closes the standard models, not every future
polarization on \(L^2(\mathbb A_{\mathbb Q}/\mathbb Q^\times)\).

## Audit and stop

The audit verified (PROVED) that no candidate satisfies (Q1)–(Q4) and
that the three NO-GOs have the indicated scope. It further confirmed that no
proof quantifies over all admissible Hermitian forms. The stop is
activated after round 3 with a NO-GO result. Claiming that (a), (b), and
(c) were closed forever would exceed the theorems proved.

The strongest available source confirms this limit: R158_002,
Theorem 158.2-G, proves its clauses on the adelic space \(X\), but
explicitly labels **exhaustivity** as unproved; R158_005 records the
residue OT-5′ as an unconstructed object. Hence a classification
theorem for all admissible prespectral polarizations is missing. That is
exactly the remaining requirement of the goal, not a fourth construction
round.
