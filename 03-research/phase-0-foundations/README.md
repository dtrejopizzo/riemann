# Phase 0 — Foundations & Translation

The phase asks whether the localized Weil quadratic form Q (built from a Hermite–Gauss test-function
family at height T₀, width σ, dimension J) is already a known object under another name, and whether
the truncation lemma needed to control Q is a routine harmonic-analysis fact or hides a deep obstruction.
It does this by translating Q into four established frameworks and by tracing which known hypotheses would
or would not imply the truncation bound.

## Results
- Q written exactly in the Weil–Guinand explicit-formula language (zero side = polar + archimedean − prime side), with the archimedean density Ω(r) made explicit. CITED/translation (classical formula, one normalization point flagged for numerical cross-check).
- Q identified as a finite-dimensional compression P_J T P_J of Connes' adelic trace operator T on L²_δ(A_Q/Q^×); faithfulness of this compression (algebraic and spectral) posed as the open question, not resolved. OPEN.
- Dictionary entry relating Q to a de Branges structure function E(z), with RH-equivalence located in the ordering/chain condition on E, flagged against the Conrey–Li obstruction. OPEN, pending specialist check.
- Truncation lemma decomposed into prime-sum, archimedean, and zero-sum tails: the prime and archimedean tails are shown unconditionally benign (Gaussian decay of the test function); the zero-sum tail is isolated as the one substantive piece. First-pass verdict: the truncation lemma itself is likely TECHNICAL/unconditional, and the RH-equivalent content lives separately, in global positivity (LB). ARGUED, first pass only, flagged for numeric and expert confirmation.

## Documents
- `phase0-plan.md` — work plan for 0.A (translation into four languages) and 0.B (cartography of the truncation lemma).
- `0A1-weil-guinand-translation.md` — Q in the Riemann–Weil explicit-formula language.
- `0A2-connes-compression.md` — Q as a compression of Connes' trace operator; the faithfulness question.
- `0A3-debranges-structure-function.md` — Q and the de Branges structure function E(z).
- `0B-cartography-first-pass.md` — decomposition and first-pass classification of the truncation lemma's three tails.

## Relation to other phases
Sets up the vocabulary (Weil functional, Connes trace, de Branges chain) used throughout the later row-D phases; the truncation-lemma question raised in 0.B is picked up by subsequent phases that build the Q-engine in full.
