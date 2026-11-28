# Phase 215 — Private mathematical certification of the GRH/RH chain, with supplements

**Status: CLOSED.** The record contains a favourable private mathematical verdict on the chain as reconstructed with the explicit supplements. The exact object and scope are in [FINAL-MEMO.md](FINAL-MEMO.md); they do not extend automatically to later versions of the manuscripts.

## Question

Review the proofs of Papers 43–46 and 49–56, check their junctions and their propagation in Paper 58, identify errors and obligations, and determine whether the reconstructed chain yields GRH for Dirichlet L-functions and RH. Papers 47–48 were outside the review.

## What was done

- The review was organised by speciality: analysis, theta and Hecke, spanning and multiplicities, covolumes, Selmer and integral Hodge theory.
- The inputs Short Forms, Spanning and Covolume were reconstructed, and the assembly leading to the main inequality and to the one-sided criterion.
- Hypotheses, ranges, characters, constants, indices and quantifiers of the applications between papers were checked, distinguishing textual coincidence from mathematical validity.
- The author's corrections were checked and the finite bookkeeping of the coefficient lemma of Paper 53 was recomputed. The earlier objection about a residual character, and its consequences downstream, was withdrawn.
- Further repairs and their proofs were documented: the definition of the character ν♭ in Paper 54, the auxiliary level in Paper 55, the sufficient properties of the phase in Paper 49, and precisions of normalisation and topology.
- Conceptual connections, antecedents and autonomous projects were identified for phase 216.

## Results

| Result | Status in the record |
|---|---|
| Reconstructed chain SF + Sp + Cv → main inequality → GRH for Dirichlet L-functions → RH | Favourable private verdict by mathematical review, with the supplements identified |
| Literal approval of the audited sources without those supplements | Not given: the inventory keeps the incorrect lines and the repairs needed |
| Earlier global objection to the exchange of Paper 53 | Withdrawn after review of the specialised application and its characters |
| Strong formula for the phase in Paper 49 | Not certified in the review; the two consequences sufficient for the chain were supplied |
| Bibliographic priority and new generalisations | Absolute priority not established; research programme formulated |

The certification recorded here refers to the sources identified by their hashes, together with the supplement and the linked proofs. It is a private mathematical review; it is not a formal Lean certificate and not an endorsement by external specialists. The phase itself did not modify the manuscripts. The repairs of the supplement were incorporated into Papers 49, 53–56 and 58 afterwards (Paper 49 now proves the strong formula for the phase, Lemma 7.21); those later versions are not covered by the verdict of this phase.

## Files

1. [FINAL-MEMO.md](FINAL-MEMO.md): closing statement, scope and handover.
2. [00-verdict.md](00-verdict.md): short conclusion.
3. [FINAL-REPORT.md](FINAL-REPORT.md): results by block and junctions.
4. [Mathematical supplement](review-v2/MATHEMATICAL-SUPPLEMENT.md): the substitutions and proofs required.
5. [Inventory V2](review-v2/INVENTORY-V2.md) and [closure map](review-v2/CLOSURE-MAP.md): obligations and dependencies.
6. [Global assembly](review-v2/GLOBAL-ASSEMBLY.md): the final deduction, with its [cross-review](review-v2/GLOBAL-CROSS-REVIEW.md).
7. [Audited sources](review-v2/sources-v2.json): identity of the manuscripts considered.
8. [New connections and programme](NEW-CONNECTIONS-AND-PROGRAMME.md): antecedents, attribution, questions and success criteria.

`deep-review/` holds the mathematical notes by speciality; `evidence/`, scripts, outputs and data; `review-v2/`, the supplements and controls of the second review; `history/`, earlier versions kept for the record. The V2 verdicts prevail over the historical objections that were withdrawn.

## Relation to other phases

[Phase 214](../phase-214-explicit-bounds-and-reconstruction/README.md) keeps conditional bounds and reconstruction antecedents. Phase 215 closes the research line of phases 0–215. [Phase 216](../phase-216-new-arithmetic-connections/README.md) starts the new line: integral compatibility between twists for one and two lifts; kernels realisable by three levels of CM weights, and their costs; and an autonomous extraction of the cup-product exponents of Paper 56, their optimality and applications to congruences.
