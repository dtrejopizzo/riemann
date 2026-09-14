# R132.007 — Lead final audit of Paper 45 (rounds 1–3) and the closure decision

Author: session lead (Fable 5.1), adversarial audit of record. Date: 2026-09-12.

## 1. Grep verification of round 3 (run by the lead on the final files)

| item | result |
|---|---|
| R1 | `grep "equivalence with Weil's criterion"` → none; no "unique c for which I_∂ ≤ 0 is Weil's criterion" survives; Cor 9.6a(iii) is identity-level uniqueness only ✓ |
| withdrawn name | `^{mer}` absent from `main.md` (outside W45.15) and from the script ✓ |
| stale `9bis.2` | only the section title, display tag (9bis.2) and historical notes remain; every theorem reference is `9bis.2′` ✓ |
| r7 | (1.5) reads `I_∞(Γ_F,Γ_F) = T_∞(Γ_{F⋆F^†})` with the (C1) clause ✓ |
| r8 | Paper 44: every "both `CLASSICAL`" sentence carries the `[phase 132]` clause (explicit-formula half `PROVED-IN-REPOSITORY`, Paper 45 Thm 9.4; Weil's criterion `CLASSICAL`) ✓; 8 marks |
| r9 | Paper 43 Def 8A.7d preamble no longer says "none of them is a derivation"; 9 `[phase 132]` marks, all records ✓ |
| old carrier | Fell completion, `E_u`, zero-count filtration, `χ_A`, `G_rad` occur only in the banner's description of the previous version, D128 dispositions and the §13 ledger ✓ |
| script | `verify_132_explicit_formula.py`: 26/26 ✓; lead's own `lead_explicit_formula_check.py`: explicit formula to 20 digits, `A(s)+A(1−s)` to 25 digits ✓ |

## 2. What the lead re-derived (record)

R132.003 (round 1: Lemmas 9.1–9.3, Thm 9.4 (a)–(c), Thm 9.6 signs, Thm 9.6′,
§9bis, Thm 7.5, Thm 8.1/Rem 8.2, Thm 12.2, Thm 10.4 with `106_11` (2),(20),(21)
traced) and this session (round 2: Cor 9.6a both routes, Lemma 5.1a both legs,
Thm 9bis.2′ at both Tate points). The blueprint's §2.2 mechanism (Mertens
cancelling an archimedean growth) was refuted by the builder with a correct
counterexample and is withdrawn; the lead's supplement (`A(s)+A(1−s) ≡ 0`) is
proved and, on the auditor's finding M3, correctly demoted to a remark in
favour of the positive residue statement Thm 9bis.2′.

## 3. Renaming / definition test (D128 C3's failure mode)

Each clause is discharged by a theorem about row A's declared objects, cited by
number: C.1 by Paper 44 Def 3bis.6/Lemma 3bis.6a; C.2 by Thm 8.1, Paper 43
9.14a–c′; C.3 by Paper 43 Thm 8.8 + Lemma 5.1a, with place-additivity
**disclosed as definitional** (row A's declared trace) and not claimed as a
localization; C.4 by Thm 5.1, Thms 7.2–7.5, Thm 9bis.2′ (a residue
computation); C.5 by §9.6; C.6 by Thm 9.6 (with Cor 9.6a) and Thm 10.4; C.7 by
Rem 9.7 (no sign proved anywhere); C.8 in the strong form by Thm 9.4 (the
explicit formula proved, imports (E1)–(E8), (R1) named with their clauses);
C.9 by §14.3 (each handed item used or declined with a reason). No clause is
satisfied by a definition alone **except as disclosed**: C.3 rests on row A's
declared trace (place-additivity definitional, said so in §5.1), and the first
half of C.6 is the explicit formula transported across that definition — the
review panel (PANEL_3 §6) is right to qualify the lead's earlier sentence, and
this file records the qualification. **Pass, with that disclosure.**

## 4. Decision

Contract (Paper 45 §2, PLAN §7; closure rule as for rows A and B): every clause
`PROVED` on the declared carrier, and the audit of record finds no clause
discharged by renaming or definition. The hostile auditor of record graded the
label **GRANTED** conditional on R1 and the sweep r1–r10 (R132.005 §8.2), all
verified above.

    ROW C: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier
           (a fixed finite chart with its chart system and colimit as
           declared structure), as a theorem about row A's declared trace
           with c = 0, the explicit formula PROVED in the repository
           (Paper 45 Thm 9.4). Granted by the lead as audit of record,
           2026-09-12, after three builder rounds and two hostile audits
           (R132.002, R132.005).

Recorded beside the label (mandatory; R132.005 §8.3 adopted verbatim in
substance):

1. **The normalization is load-bearing and pinned.** Every theorem of §§9,
   9bis, 10, 12 and §14.4's "row D's target implies RH" is about row A's
   trace with `c := 0`; by Cor 9.6a that constant is the unique one for which
   `I_∞^{(c)} = B_nuc` (identity-level uniqueness, not a statement about the
   sign condition). D128 C9 closed. Paper 43's `c_cut` is a different, open
   quantity, never conflated.
2. **Declined, not proved.** Row C does not prove that `Σ_vW_v` is the relative
   character of a localization (D128 C2, C3); place-additivity is
   definitional and said so. `𝓝_∞^W = 0` and Paper 43 Thm 8A.7b declined.
3. **Quantifiers.** The comparison theorem is a colimit statement ((C1)), exact
   at a chart inside the window `R(Γ_h) < \log ℓ_{next}(S)`, false outside it;
   `𝓝_∩ = 0` is fixed-chart; (C1) does not govern the continued Euler-product
   symbol `A`.
4. **The poles.** Thm 9bis.2′: chart residues `|S_f|+1` at `s=0` and `0` at
   `s=1`; continuation residues exactly `1` at both; the pair is the polar
   packet `2Φ_F(0)Φ_F(1) = β_T(M,M)`; Mertens (E8) used in Thm 9bis.4(ii),(iii)
   only, quarantined, serving no part of C.4's discharge; `Ξ ≡ 0` is a remark.
5. **Imports.** (E1), (E2) (incl. "no real nontrivial zeros"), (E3a)–(E3d),
   (E4)–(E8), (R1) `106_11`; no Meyer, no spectral realization, no cutoff
   theorem.
6. **No sign.** Nothing about the location of any zero outside §9.5 and the
   contrapositive argument of §10.
7. **Row D inherits** `I_∂ ≤ 0` on primitive radial classes of `D_A^∞`, on the
   trace with `c = 0` (now a theorem of row C), plus the two standing
   negatives Paper 43 Thm 14.1 and Paper 44 Thm 8bis.4a; the chain
   "row D's target ⟹ RH" is complete with the explicit formula proved.
8. **Cross-paper record.** `[phase 132]` edits: Paper 43 (Def 8A.7d reason
   (iv) characterized by Cor 9.6a; §14.0 rows `𝓝_∞^W`, `c_cut`; §14.1a what
   row C used) and Paper 44 (Thm 8bis.4(ii) explicit-formula half relabelled
   `PROVED-IN-REPOSITORY`; five consistency sentences). No theorem, proof or
   row label of A or B changed.
9. **Honesty about Weil's proof** (as for A and B). Rows A–C construct the
   objects and prove the comparison; the section theory with nonnegative
   dimension that makes Riemann–Roch an inequality is the content of RH and
   is row D's, where by Thm 14.1 and Thm 8bis.4a no naive Hodge-index shape is
   available.

## 5. The programme after phase 132

Rows A, B, C carry `WEIL-STRENGTH-COMPLETE` on the declared carrier, each by
the same protocol. Next: the 3-agent review panel of A, B, C (owner's
standing instruction), then row D.
