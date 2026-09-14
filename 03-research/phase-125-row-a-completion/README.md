# Phase 125 — row A completion campaign

Opened 2026-09-12.  Status after A125.015:

```text
ROW A:  WEIL-STRENGTH-COMPLETE  on the graph sector G with its Fell
        completion, the full cyclic shadow and the torsion invariant T,
        with one cited theorem, Wodzicki excision (Paper 43 §12 and appendix) as its only inputs
        beyond the repository.
```

The decisive step is [A125.014](A125_014_THE_TORSION_THEORY.md) as corrected
by A125.016: distinct classes can have **isomorphic** full shadows, so **no
additive numerical invariant can be Weil-strength**; the invariant that
separates them is the half-density-normalized analytic relative trace, whose
difference on two unit classes is `(v_p(1−u)−v_p(1−u'))log p` exactly, with no
regularization, and which is nonzero on the arithmetic family `Γ_n`.

See [PLAN.md](PLAN.md) for the entry state and the note order.

## Notes

* [A125.001](A125_001_DUALIZING_BIMODULE_AND_SHIFTED_DAGGER.md) — **A.4**.
  The recorded obstruction `Hom_{U-bimod}(U,N)=0` forbids self-duality of the
  localized ideals, not `Δ^†≅Δ`.  The dagger is built from two objects that
  already exist: the half-density `h=|·|_S^{-1/2}` with `h²=` the module,
  canonical by the product formula, and the degree-one dualizing object
  `Ω_dR=(S→S dt)` with its orientation trace.  The two rival routes were
  already refuted in the corpus; this is the surviving one.  Theorem 3.1
  computes the dual of a localized ideal as a boundary-profile object.
* [A125.002](A125_002_TWO_SIDED_EXCISION.md) — **A.3**.  Resolves the open
  item of P123.125 §4.  The obstruction to two-sided excision is one object,
  `B_O ⊗ M ⊗ I_O ⊗ N ⊗ B_O`, and it vanishes on the ideal-generated sector.
  It is not known to vanish on the profile objects, which is a genuine
  tension between A.3 and A.4.
* [A125.003](A125_003_TRACE_CLASS_DOMAIN_AND_DETERMINANT_TARGET.md) — **A.5**.
  First definition of `Corr_A^tr` in the corpus: objects perfect after the de
  Rham twist.  The twist repairs the recorded perfect-kernel counterexample
  and puts the diagonal in the domain.
* [A125.004](A125_004_NUMERICAL_EQUIVALENCE_AND_QUOTIENT.md) — **A.6**.
  Numerical radical proved closed, a two-sided ideal and `†`-stable; `N_A`
  Hausdorff with descending operations.  Graph classes lie in the trace-class
  domain.
* [A125.005](A125_005_CORRECTION_DETERMINANT_TARGET_MUST_RETAIN_THE_TWIST.md)
  — **correction**.  Proves the boundary determinant is trivial on every graph
  class, hence cannot be the numerical target: no isomorphism-class invariant
  of bundles on `B_q` separates a graph from the diagonal.  Specifies the
  corrected target.

* [A125.006](A125_006_FIXED_POINT_DICHOTOMY_AND_THE_MIXED_SECTOR.md) —
  **A.6, the turning point**.  Two notes written for other purposes combine
  into a dichotomy: a freely acting class has acyclic shadow, the identity has
  shadow of rank `r>0`.  No function of `|w|` alone can do both, so the graph
  classes leave the ruling span and the mixed sector is nonzero.  The graph
  sector is also `†`-closed by itself, which dissolves the A.3/A.4 tension:
  the localized ideals were the wrong generators.
* [A125.007](A125_007_EFFECTIVITY_AND_PROPERNESS.md) — **A.7**.  The recorded
  refutation `C1` kills the sum-of-squares identification, which the clause
  forbids anyway.  The cone is coefficient nonnegativity; it descends and is
  **proper**, closing an item P123.010 left open.
* [A125.008](A125_008_MIXED_RIEMANN_ROCH.md) — **A.8**.  The composition
  anomaly is not a defect: a determinant composing up to a cocycle is a
  biextension, which is what the clause asks for.  The Riemann–Roch equality
  `deg λ_RR = χ(Tr_A)` is forced by the dichotomy in both of its cases.
* [A125.009](A125_009_CLASSICAL_CONTROL.md) — **A.9**.  Composition,
  transpose, unit and diagonal intersection all match.  The decisive point is
  that the dichotomy reproduces the classical Lefschetz vanishing
  `Γ_f·Δ = #Fix(f)`, which was not put in.
* [A125.010](A125_010_JOINT_AUDIT_A1_TO_A10.md) — A.1, A.2, A.10 and a
  first joint audit, superseded in §§4–5 by A125.013.
* [A125.011](A125_011_DISCHARGING_THE_CONDITIONAL_ON_G.md) — removes the
  conditional `(*)`: on `G` the dagger, the trace-class domain and the
  determinant are built from the graph realization alone.
* [A125.012](A125_012_THE_WEIL_STRENGTH_GATE.md) — the arithmetic family
  `Γ_n=E_{a_S(n)}` already lies in `G` (P123.038); the boundary shadow
  vanishes on it, which is the exact content of P123.082's objection and
  corrects its prescription.  States the single gate theorem `(F)` and proves
  `(F) ⇒ WEIL-STRENGTH-COMPLETE`.
* [A125.013](A125_013_FINAL_AUDIT_AND_LABEL.md) — audit including P123.082;
  label withheld pending `(F)`.  Superseded by A125.014–015.
* [A125.014](A125_014_THE_TORSION_THEORY.md) — **the torsion theory.**
  Decomposition of the full shadow over labels, deck Koszul and places;
  acyclicity off the diagonal; the tangential complex identified as HKR, so
  the old conditional `(*)` was never a hypothesis; the torsion invariant,
  its regularization well defined modulo the ruling plane; the exact mixed
  computation `T(E_u)-T(E_{u'})=(v_p(1-u)-v_p(1-u'))\log p`; properness;
  A.5–A.8.
* [A125.015](A125_015_WEIL_STRENGTH_LABEL.md) — the label, the adversarial
  audit, the imports, and the first theorem row B must prove.
* [A125.016](A125_016_CORRECTION_SHADOWS_ARE_NOT_ACYCLIC.md) — **correction**
  to A125.014: the full shadow is not acyclic (the finite-place origin is a
  twist-independent rank-one fixed class, P123.084); replaced by the
  isomorphic-shadows theorem; the invariant is the analytic relative trace,
  with the smooth-model torsion identification of P123.060 §4.  The exact
  mixed computation and the label stand.  Consolidated in
  [Paper 43](../../04-papers/43-row-a-torsion-theory/main.md).

## The crux, and how it was resolved

Three open items — excision on the dagger closure, a nontrivial joint A.3/A.5
domain, and the mixed sector — turned out to be one.  A125.005 located it in a
determinant cocycle; A125.006 then showed the right invariant is not a
determinant at all but the Euler characteristic of the cyclic shadow, where
the fixed-point dichotomy settles it outright.  The anomaly cocycle returned
in A125.008, where it is the biextension of Riemann–Roch, which is its correct
role.

## What row B inherits

A composition-closed, `†`-closed, trace-class sector with a nondegenerate
pairing, a proper effective cone and a Riemann–Roch equality; one conditional
input `(*)`; and one structural question that must be answered before B
starts, namely whether the non-invertible arithmetic correspondences B needs
lie in `G` or force an enlargement on which A.2–A.8 must be re-proved.

## Discipline

One conditional input is shared by A125.001, A125.003 and A125.004 and is
stated in each: the source pushforward must be proved to be computed by the
relative tangential complex, with its dualizing normalization and determinant
matching the arithmetic category.  It is not counted more than once and is not
hidden inside a clause.
* [A125.017](A125_017_CORRECTION_UNIT_TWISTS_AND_IMPORTS_DISCHARGED.md) —
  **second correction and imports discharged**: unit twists have
  infinite-rank twisted shadow (orbit spaces `Z_p^×/(1+p^kZ_p)` per shell),
  so the isomorphic-shadows theorem is withdrawn and Cor. 7.5 reproved;
  I-2 and I-1 proved in Paper 43's appendix, I-3 shown unnecessary; one
  citation remains (Wodzicki excision).
