# Phase 129 — row A rebuild

Four construction rounds and three audit rounds on
[Paper 43](../../04-papers/43-row-a-torsion-theory/main.md), followed by a final
verification by hand of Theorems 9.7, 9.8,
9.13(a), 14.1 and the restructured Definition 8.6.

| file | content |
|---|---|
| R129_001 | round 1 |
| R129_002 | audit round 1 (F1 FATAL: chart map did not exist; 19 findings) |
| R129_003 | round 2 (valuation splitting Lemma 3.3; chart invariance proved FALSE; wrongly claimed A.6 structurally blocked) |
| R129_004 | audit round 2 (refuted the A.6 blockage; gave the P123.017 route and the question `𝓝 = 0?`) |
| R129_005 | round 3 (**Theorem 9.8: `𝓝 = 0`**, import-free after round 4; (T1)–(T6)) |
| R129_006 | audit round 3 (verified `𝓝 = 0` step by step; F1 archimedean ½; F5 A.6 reading; F6 no Hodge-index shape; F14 A.8 is one theorem) |
| R129_007 | round 4 (T defined from proved local terms; Thm 9.13(a) no module splitting; Thm 14.1 signature; Prop 10.6 closes the contact-determinant route to A.8; proposed A.6 amendment) |

## Outcome

The rounds **converged**.  Both agree:

- **New, verified, import-free theorem:** the numerical radical vanishes, `𝓝 = 0`
  (Thm 9.8).  Hence `N_A = D_A`, the Tate functionals descend, the canonical
  hyperbolic boundary sequence `0 → N_A^prim → N_A → B_T → 0` exists with a nonzero
  primitive sector on which `I_A` is nondegenerate, and the completion is separated.
- **A.6** is PROVED in P123.017 §4's exact-sequence reading and REFUTED on this carrier
  in the literal "contains the ruling plane" reading (Thm 9.13(a): no `D_A`-module
  splitting exists).  **Decision still open for the specification** — proposed text in
  Paper 43 §14.2.
- **A.8** is OPEN and binding: one theorem, the geometric source functor `Φ_det`
  into the periodic Deligne ruling category plus the metric comparison with the
  already-constructed analytic target `L_tan` (A_MIXED_METRIC_WORK).  No route in the
  corpus; the one candidate (determinant of the contact complex) is closed off by
  Prop 10.6 / Cor 7.5.
- **A.5** PARTIAL: (O-A5-1b) a determinant construction beyond the unit block, which
  P123.105 §4 and P123.107 §5 disclaim; chart invariance is false; the constant `c`
  decides the signature.
- **Negative result for rows B/C/D (Thm 14.1):** `I_A(F,F) = ∫|F̂|²(T̂+c)` is indefinite
  with infinite index on both sides, `(D_A^prim)^⊥ = 0`; no Hodge-index shape on `N_A`.

**Label: `ROW A: CONSTRUCTED`.**  `WEIL-STRENGTH-COMPLETE` is not earned and cannot be
earned by further rounds of the same loop: what remains is (1) new mathematics for
A.8, (2) a specification decision for A.6, (3) a construction for A.5.

**Superseded (later the same day):** the three remaining items were closed in [phase 130](../phase-130-row-a-closure/README.md); see `R130_005` for the label decision.
