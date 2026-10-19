# First campaign: viability of the carrier and of the contact

Status: **execution started after author approval**.

Progress and limits: [first-campaign record](../../03-research/phase-123-weil-strength-abc/P123_024_FIRST_CAMPAIGN_LEDGER.md). The following sections keep the original criteria; not all of them are closed.

Objective: decide whether the phase-123 candidate can be repaired into a category that hosts the arithmetic contact. Do not attempt to close RR or RH in this block.

## 1. Fix the local contract

Work first with `S={infinity,2,3}` and then with chart inclusions. State explicitly whether Gamma_S includes signs or only positive units, and how it compares with the sources that use all units.

Keep distinct the fast ideal K_S, its unitization, its multiplier algebra, the control C* representation and the smooth test kernel. Write down where U_gamma, the diagonal and each bimodule live.

Proposed deliverable: `P123_019_REPAIRED_LOCAL_BIMODULE_CONTRACT.md`.

Acceptance: every formula has domain/codomain; it does not use `1 in K_S` nor `U_gamma in K_S+C1` for gamma different from 1.

## 2. Prove the lift change in the chosen category

For each automorphism beta_a, build the corresponding essential bimodule. Prove that the multiplier U_gamma induces a valid intertwiner between the lifts a and gamma*a.

Prove composition and coherence of three lift changes. In the non-unital model, prove the identification of the balanced tensor using the tool actually available — approximate unit, essentiality or correspondence theorem — and verify its hypotheses in the fast kernel.

If only the C* theorem is obtained, label it as such. The nuclear/fast version remains open until the comparison is proved.

**First opportunity for success:** a local lift-independence theorem that repairs a currently ill-typed formula.

## 3. Build a genuine chart transition

Use as an exact regression the pair of representatives `(1,1)` and `(2,2)` in `S={infinity,2}`. The corrected transition must recognize their equivalence once place 3 is incorporated, without naively sending both to extensions by one.

Propose a span/induction compatible with the coefficient inclusion, or define the global object and derive its restrictions. Write the action on objects and arrows and check `S -> S' -> S''`.

Proposed deliverable: `P123_020_TRUE_CHART_TRANSITIONS.md`.

Acceptance: coherence diagram proved, explicit connection with the coefficient sheaf, and declared topological scope. A choice of canonical representative, if used, needs its own multiplicative coherence; it is not equivalent to a map induced by extension by one.

## 4. Prove that the test kernel is stable

The action on coefficients C_0 is continuous; determine its subspace of smooth vectors and the appropriate locally constant levels. Check the product of two sections and the dagger within that subspace.

Prove the local estimates that will later support LF continuity. Do not declare full completion at this stage by analogy with scalar functions.

## 5. Control the classical category and effectivity

Redo P123.011 in a zero-dimensional case and a simple curve:

- permutation of three points: effective graph versus matrix positivity;
- diagonal and rulings;
- graph of a finite endomorphism and its transpose;
- Frobenius: convention and difference between transposition and inverse;
- intersection of cycles versus the character of the perfect kernel, with any necessary RR correction.

Proposed deliverable: `P123_021_CLASSICAL_COMPARISON_AND_CONE_TEST.md`.

Acceptance: precise relation between the two theories, even if the conclusion is that the category must be enlarged. Do not claim cone equivalence just because both admit sums.

## 6. Decisive test B: 2, 4, 3 and 6

Build the objects before assigning them a degree. Compute their compositions and derived contacts. Expected values only as an external test:

| n | Phi_n(1) | Expected arithmetic contact |
|---|---:|---|
| 2 | 2 | `[Z --2--> Z]` |
| 4 | 2 | `[Z --2--> Z]` |
| 3 | 3 | `[Z --3--> Z]` |
| 6 | 1 | acyclic complex |

Require `Gamma_2 star Gamma_2 ~= Gamma_4` and `Gamma_2 star Gamma_3 ~= Gamma_6`. The contact need not be multiplicative: precisely what must be deduced is how a non-trivial product can have acyclic contact.

Compare the construction with the linear contact `1-u^(-1)` and with the Deninger/Haran Witt realization. Identify the morphism or excess that produces Phi_n(1); if it does not appear, the simple-graph model still does not pass the test.

Proposed deliverable: `P123_022_MINIMAL_ARITHMETIC_CONTACT_TEST.md`.

Acceptance: complexes and derived maps, not numerical labels nor a product category that carries an added complex.

## 7. Keep a concrete question about D alive during the campaign

Read P122.028 and P122.029 as existing computations. Formulate a candidate global boundary relation that could prove zero flow or transmission in a defined source space before imposing the sign.

Note separately:

1. the source identity that can be proved;
2. the comparison with the physical channels;
3. the estimate or condition still pending;
4. a counter-model that decides whether what is proved is enough.

It is not a requirement to close D in order to accept the local block. It is mandatory, however, to check that A keeps the data that future law would need: places, orientations, Gamma and Tate before scalarizing.

## 8. Decision at the end

| Outcome | Continuation |
|---|---|
| Bimodules and transitions pass; derived contact passes | Complete A: trace, numerical topology, effectivity and RR; generalize B. |
| Only the C* model passes | Keep it as an analytic control; build the integral/smooth bridge before promoting it. |
| Linear contact does not produce the cyclotomic one | Examine extension to finite correspondences/Witt; do not keep completing the graphs alone. |
| Semilocal transitions fail for the candidate | Study the global variant with an explicit chart-recovery theorem. |
| Only identities of the D defect appear | Keep them as diagnosis; the sign theorem remains open. |

No outcome is accepted because of the file's size or a matrix PASS. Each output must change a concrete obligation and update the master plan without erasing the history of the failures.
