# R129.002 — auditor report, round 1 (on the builder's first rebuild of Paper 43)

Date: 2026-09-12.  Auditor: hostile referee agent.  Target: Paper 43 after R129.001.

## Headline
The rebuild is a large honest improvement — the withdrawals are correct, Lemma 8.2
and Theorem 8.8 are right, the normalization dictionary is right, and the Theorem 9.5
computation is right.  But A.5 is NOT proved: its restriction half rests on a chart
map that does not exist (F1), its determinant half is the gate P123.014's status
declares open (F7), and `Tr_A` is not yet a function of an object (F4).  A.1 is not
proved as written (F11).

## Findings
- **F1 (FATAL for A.5's restriction clause).** Thm 8A.5's `J_{ST}` does not exist:
  extension-by-one is refuted by P123.018 §2; projection does not descend modulo the
  unit groups (P123.018 §2 verbatim: "Projection ... also does not automatically descend
  ... reversing the arrow without a construction is not a repair"); the displayed
  formula is not `Γ_T`-invariant (take `γ=3`).  Fix: construct the chart transition as
  a span/induction with coherence, or declare the restriction half OPEN, obstacle (O-A5-2).
- **F2 (SERIOUS).** Thm 8.7 (`T=Σ_v W_v` exactly) contradicts Thm 8.9 (differs by `c·F(1)`
  from P123.046 (4.1)); P123.046 (4.1) has no archimedean term.  Fix: write
  `T=Σ_v W_v + c·F(1)` with `c` open, or compute `c`.
- **F3 (SERIOUS).** Import `C` (semilocal trace formula) is not "audited in P123.004":
  P123.004 §4 is schematic and its normalization audit says the archimedean coefficient
  cannot be imported unreconciled; P123.035 §6 forbids citing it with these constants.
  Add obstacle (O-A5-3).
- **F4 (SERIOUS).** `s(K)` is defined on a presentation, not an object; `Tr_A` not well
  defined on `Corr_A^tr`.
- **F5 (SERIOUS).** Thm 8A.8's proof evaluates `s` in the Karoubi envelope where it is undefined.
- **F6 (SERIOUS).** `Corr_A^tr ⊆ G` is a type error (`E_F` is not an object of `C_tw(U)`);
  closure of the chart-unit section class under `⋆` needs the splitting
  `φ(x)=∏_p p^{v_p(x_p)}`, `A_S^× = Γ_S × ker φ`, not stated (P123.014 §5).
- **F7 (SERIOUS, unlisted obstacle).** Thm 8A.7 determinant compatibility is exactly the
  gate P123.014's status and P123.012 §7 declare open.  Add (O-A5-1)/(O-A8-4).
- **F8 (SERIOUS, label).** Thm 9.5 proves `N_A ≠ 0` and that `T` separates two sections of
  equal radial push-forward — not a "nonzero completed mixed sector" (needs O-A6-1/2).
- **F9 (MINOR).** Three proof defects in Thm 9.5 (archimedean slice statement false but
  harmless; unstated hypotheses for `μ>0`; `T|_𝓝=0` needs citing).
- **F10 (MINOR).** Thm 8.9 needs `T'` continuous of finite order.
- **F11 (SERIOUS).** A.1 declared PROVED after rewriting the clause; restriction and descent
  are open/refuted.  Verdict PARTIAL.
- **F12 (MINOR).** Thm 6.1: `†` antilinear vs `D_h` linear; comparison is on a surrogate
  `G_Λ`; twist bookkeeping asserted; `Perf^{gr}` undefined.  A.9 "passed for the formalism".
- **F13 (SERIOUS).** Effectivity never defined for smeared objects; Thm 10.3 vacuous until
  `E_F` effective iff `F≥0` is proved to extend Def 10.1.
- **F14–F19 (MINOR/PRESENTATION).** Garbled †-chain in Thm 9.4; (O-A6-1) second formulation
  ill-posed (no spectral measure defined) — record WHY it is hard: `T` is supported on the
  null slices `j_v(Q_v^×)` while `λ_±` are Haar integrals over `C_S`; two `vol(Z_p^×)`
  conventions in §7.2; two objects called `Tr_A`; P123.064/082 proved for a different
  algebra than `U`; Thm 8.7 finiteness paragraph vacuous.

## Verified correct
§8.1, Lemma 8.2, Remark 8.3, Lemma 8.4; the normalization dictionary; Theorem 8.8;
Theorem 9.1 (P123.014 §6 is PROVED-IN-REPOSITORY and untouched by the P123.018 override);
Theorem 9.3; the Theorem 9.5 computation `T(F)−T(F')=μ(log p)(p^j−p^{j'})`; Appendix A–E
corrections; §11bis; §11; import count three.

## Clause verdicts (auditor)
A.1 PARTIAL · A.2 PARTIAL · A.3 PROVED on G · A.4 PROVED on G · A.5 PARTIAL ·
A.6 OPEN · A.7 PARTIAL · A.8 OPEN · A.9 PASSED for the formalism · A.10 PROVED.

## Required next (in order)
1 fix/withdraw Thm 8A.5 · 2 reconcile 8.7/8.9 · 3 downgrade import C, add (O-A5-3) ·
4 make `s` an invariant, repair 8A.8 · 5 rebuild Def 3.1/8A.1 with the splitting φ ·
6 add (O-A5-1)/(O-A8-4) · 7 rebill Thm 9.5, fix F9 · 8 define effectivity for smeared
objects · 9 downgrade A.1, A.9 · 10 housekeeping F10, F14–F19.
