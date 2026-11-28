# Scope of the Lean records

**Verdict (c): this review does not certify the complete formalisation nor the correspondence between it and the papers.** The local records are documentary evidence of a reported compilation, not a compilation repeated during this audit.

`06-alpoge-verification/README.md`, `scripts/AxiomCheck.lean`, `source-metadata/Statements.lean`, `source-metadata/MainTheorems.lean` and `results/axioms.log` were read. The file `README-mio.md`, which appeared untracked by Git at the start, was neither modified nor used.

The log contains `riemannHypothesis : RiemannHypothesis` and reports only `propext`, `Classical.choice` and `Quot.sound` for five main theorems. The checking script does indeed ask for `#print axioms` on those names. `Statements.lean` expresses zeros of zeta excluding negative even integers, a zero-free half-plane for Dirichlet characters except for the pole, and zeros of L in the open strip. Those formulas have the scope that their names suggest at the level of the visible expressions.

This does not yet establish:

1. That the transitive definitions of zeta, L and `RiemannHypothesis` of the compiled environment are exactly those expected; `Statements.lean` imports Mathlib and does not contain that whole environment.
2. That the log corresponds to the totality of the source tree and to the binaries whose chain of trust is to be verified.
3. That each human statement of 49–56 is a faithful translation of a formal declaration, with the same constants and hypotheses.
4. That a formal proof of the final result automatically validates a different prose proof of the same result.

The README describes an archive of approximately 175,000 modules and a large-scale compilation. That archive was not downloaded or rebuilt in this task. Nor were `lake build` or an independent kernel run. For that reason "Lean verified" is not reported as a result of this work.

The next useful check would be a bidirectional map between the central statements of each paper and exact Lean declarations, including their definitions and the transitive tree of dependencies. This task is different from reviewing the logs and different from auditing the human proofs, which was the main assignment.
