# 115.10 — State of the literature on the prime-free window, and three independent confirmations of the no-go

A survey of 2020 → August 2026 was run against the question raised by `115_08`
Corollary 7: has anyone closed the gap between the archimedean positivity and
the finite contact term?  The answer is no, and the way in which it is no
corroborates the no-go from three independent directions.

Items marked **[verified here]** were checked directly against local sources;
the rest are from the survey and carry its provenance.

## 1. The window has not moved in six years

Connes–Consani arXiv:2006.13771 (June 2020), Theorem 1, requires
\(\mathrm{supp}\,g\subset[2^{-1/2},2^{1/2}]\).  Nothing in the subsequent
Connes / Consani / Moscovici output — 2008.10974, 2106.01715, 2112.08820,
2205.01391, 2207.10419, 2208.08339, 2306.00456, 2307.06748, 2310.18423,
2401.08401, 2403.01247, 2501.06560, 2511.22755, 2511.23257, 2602.15941,
2606.06604 — extends it.

**[verified here]** The decisive evidence is Connes' own survey
*"The Riemann Hypothesis: Past, Present and a Letter Through Time"*,
arXiv:2602.04022 (February 2026), local copy
`00-references/papers-ref-phase-60/arXiv-2602.04022v1.tex`.  Two sentences,
quoted exactly:

> line 1298: *"the compression of the scaling \(\vartheta(f)\) to Sonin's space
> was shown to be the root of Weil's positivity at the archimedean place **on
> test functions with support in the interval \([2^{-1/2},2^{1/2}]\)**"*

> line 1196: *"The key ingredient is the semilocal trace formula, which in our
> paper was used **in the simple case when no primes are involved**."*

The second sentence is Proposition 5 of `115_08` in Connes' own words: the
support window *is* the condition that no primes enter.  Our characterisation
is therefore not a reinterpretation — it is the author's own reading.  And the
first sentence shows the hypothesis unchanged six years on, in a survey written
this year.

## 2. Three independent confirmations of Corollary 7

Corollary 7 says: a functional carrying no arithmetic input cannot dominate
\(K\), because the inequality producing it costs exactly the missing amount.
Three separate lines of work stop at precisely that point.

**(a) Connes–Consani's own counterexample.**  Remark 3.9(ii) of 2006.13771
constructs an explicit positive-definite \(f\) supported in
\([-\log2,\log2]\) with \(D_+(Q_+f)>0\), i.e. **\(D\circ Q\) is not negative on
\([2^{-1},2]\)**.  Their positivity results reach only \(u=1.10246\)
(Corollary 3.8) and, with Boas–Kac, \(u=1.15077\) (Remark 3.9(i)).

This is stronger than `115_08` Corollary 3 on the \(-D\) route.  Corollary 3
said the route is a strengthening of row (d); Remark 3.9(ii) says the
strengthened statement is **outright false** past a small interval.  The
\(-D\ge K\) route is therefore closed by counterexample, not merely by slack.

**(b) Suzuki's unconditional programme stops at the same place.**
arXiv:2606.09096 (June 2026), *"Weil's quadratic form via the screw function"*,
proves genuinely unconditional results — Theorem 1.5, that all zeros of
\(W(a,\theta;z)\) are real, without assuming RH, improving on CCM which needs
simplicity of \(\lambda_a\) and evenness of its eigenfunction.  But Suzuki
states that the proof *"relies essentially only on the fact that the prime
contribution to \(Q_W^a\) involves only finitely many primes for fixed \(a\)"*,
and that control of the arithmetic prime terms *"lies beyond the arguments
used"*.

That is Corollary 7 restated from an entirely different formalism: the
unconditional machinery works precisely because it does not engage the prime
terms.

**(c) Connes–van Suijlekom's hypotheses are the unknown part.**
arXiv:2511.23257 (November 2025) proves that all zeros of \(\widehat\xi(z)\) are
real **given** that the spectral minimum of \(A\) is a simple isolated
eigenvalue with even eigenfunction.  The paper's own framing: *"the key
difficulty in this context becomes the verification that zero is indeed the
(simple) minimal eigenvalue."*  The conditional part is exactly what would have
to be supplied by arithmetic.

## 3. What does exist on the semi-local side

Connes–Consani–Moscovici, arXiv:2310.18423v2, *"Zeta zeros and prolate wave
operators — semilocal adelic operators"* (Oct 2023, v2 May 2024).  Local copy
`00-references/papers-ref-2/arXiv-2310.18423v2/`.

* **Theorem 4.6.**  For \(S\ni\infty\) finite and \(\lambda>0\), the map
  \(\theta_S\) is a Hilbertian isomorphism of Sonin spaces
  \(\mathfrak S_\lambda(\mathbb R,e_\infty)\to\mathfrak S_\lambda(X_S,\alpha)\).
* Constructs a semilocal analogue of the prolate wave operator, related to the
  metaplectic representation of the double cover of \(SL(2,\mathbb R)\).

**This is the object hypothesised in `115_09` §1, and it already exists.**  The
semi-local Sonin space is constructed and shown stable under enlarging \(S\).
What does *not* exist is the positivity: the paper's own statement is that they
*"expect"* these tools *"open a way"* to handle Weil positivity, and that the
operator-theoretic aspect *"provides a more precise strategy"* — a strategy,
explicitly not a theorem.

So `115_09`'s hypothesis (H) is not an invention, and it is not available
either.  The gap is exactly: from \(\theta_S\) being an isomorphism, to a
semilocal analogue of Theorem 3 with a controllable \(E_S\).

Also relevant: arXiv:2008.10974, *"Quasi-inner functions and local factors"*
(Aug 2020), where the kernels of \(u(F)_{22}\) form an inductive system equal to
the semi-local Sonin spaces — the same object again, no positivity statement.

And arXiv:2511.22755, *"Zeta Spectral Triples"* (Nov 2025): rank-one
perturbations whose spectra match low zeta zeros numerically, with the authors'
own note that *"a rigorous proof of this convergence would establish the
Riemann Hypothesis"* — i.e. conjectural.

## 4. Reading

The three confirmations in §2 come from three formalisms — Sonin compression,
screw functions, spectral-action truncations — that share no technical
machinery.  All three produce unconditional results up to the point where the
prime terms must be engaged, and stop there.  That convergence is the strongest
available evidence that `115_08` Corollary 7 identifies a real obstruction
rather than an artefact of our formulation.

It also fixes the standard this programme has to meet.  Row (d) is not blocked
by a missing lemma inside an otherwise complete construction; it is blocked at
the point where every existing approach is blocked, and closing it means
supplying what none of them supplies.

## 5. Consequences for phase 115

* The \(-D\ge K\) route: **closed by counterexample** (CC Remark 3.9(ii)), a
  strictly stronger refutation than `115_08` Corollary 3.
* The \(\mathcal S\ge K\) route: **closed** by `115_08` Corollary 3.
* The semi-local route of `115_09`: the *space* exists (CCM Theorem 4.6); the
  *positivity* does not, and is described by its authors as a strategy.
  Hypothesis (H) remains unproved, and no one has proved it.
* Row (d): **OPEN**.

## 6. Sources worth pulling that are not local

2008.10974 (Quasi-inner functions), 2206.03682 and 2308.11860 (Suzuki),
2607.02828 and 2605.20224 (Groskin).  Already local:
`papers-nuevos/extension-clase-test/` holds 2006.13771, 2310.18423, 2511.22755,
2606.09096; `papers-ref-phase-60/` holds 2602.04022, 2511.23257, 2511.22755.
