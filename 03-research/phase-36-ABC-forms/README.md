# Phase 36 — Forms A/B/C

This phase executes three concrete analytic/algebraic tests proposed in paper P41/P42 for propagating positivity from unconditional edge theorems to RH: Form A (a joint De Bruijn–Newman time / Euler-approximant trace $\mathcal T(t,x)$ and whether a parabolic inequality propagates positivity to the corner), Form B (an "amplifier functor" $\boxtimes$ realizing a Deligne-style integer invariant on the Weil–Connes Pontryagin space), and Form C (effective quantitative degeneration as a dichotomy parameter $d\to0$), followed by an attempted sieve-to-index bridge.

## Results
- Form C (effective $SR_d$, Problem 8.1 of P41): the posed dichotomy (exponential vs. polynomial degeneration) is shown to be false as stated; the actual behavior is finer than either branch. (NO-GO for the dichotomy as posed; refined finding reported)
- Form A, first test on the 2-prime approximant: the only definition of $\mathcal T(t,x)$ making both edges already-proved theorems forces $\mathcal T\equiv0$ in the whole interior (by de Bruijn's forward-time reality inheritance), so every parabolic inequality is vacuous and nothing propagates to the corner $(t,x)=(0,\infty)$. (NO-GO)
- Form B (amplifier functor $\boxtimes$, Problem 7.2 of P41): systematic search over five candidate constructions on $(\mathcal K,Q)$ or the CCM-triple category; all collapse (sterility lemma). (NO-GO)
- Execution of Problem 5.4 (two-variable Weil formula with a thickened diagonal multiplicative kernel $h(x_1,x_2)=g(x_1x_2)\varphi(x_1/x_2)$): tested as a candidate analytic realization of the tensor square needed for Form B; result documented against the missing-lemma obstruction MW-7. (OPEN / partial NO-GO)
- Sieve→index bridge (Missing Lemma 6.1 of P42): the distance between the available sieve bound and what the bridge needs is identified precisely as the step from "on average over windows" to "uniform over windows" — which is RH re-encoded. (NO-GO, "BRIDGE DEAD")

## Documents
- `104-effective-quantitative-degeneration.md`: Form C, resolution of the degeneration dichotomy.
- `105-coupling-first-test-of-form.md`: Form A, the 2-prime approximant test and the interior-degeneration theorem.
- `106-amplifier-functor-systematic-search.md`: Form B, systematic search and collapse of the five amplifier candidates.
- `107-execution-of-problem-5-4-the-weil.md`: two-variable Weil formula with diagonal multiplicative kernel, test of Missing Lemma 5.2.
- `108-sieve-index-bridge-formulation-unconditional-inventory.md`: sieve→index bridge, formulation and verdict (bridge dead).

## Relation to other phases
Executes concrete test problems posed in papers P41/P42 (referenced throughout), building on Phase 32–35 machinery (Jacobi trace, CCM triples, toy models). The negative verdicts here (Forms A, B, and the sieve bridge) are audited further in Phase 38.
