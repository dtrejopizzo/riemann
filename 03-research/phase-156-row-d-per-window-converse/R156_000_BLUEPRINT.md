# R156_000 — Blueprint, phase 156: the per-window converse and the residuals

Opened on the decision to scope: close 155 + phase 156. Ceiling stated in advance, as in `R155_056`:
**row D complete = RH** (Paper 47 §9.1 reduction chain; after round 8 the only arithmetic content is uniformity in
`T`, `R155_053` Prop 1.3). This phase cannot and does not aim at the sign; it closes the open per-window equivalence and the
residuals of the frame, so that the final reduced statement of D can be written.

## Corpus check (done)
* 156a (rank-one Schur reduction at log 2) — already done in substance (D.56; Prop 3c.1/Thm 3c.3; P47 `subsec:schur`); the
  only new input, (H1) at log 2, is now P47 `thm:index`/`cor:H1`. **Not a round.**
* 156b (r(T)≈4T finite compression, interlacing in T) — blocked by `thm:arena`/N5 unless W > 0 on the positive subspace of
  A_∞; D.55 is the correct finite core (doubly exponential); D.53: no monotone spectral flow. **Dropped.**
* 156c (per-window converse `λ_min(A_T|P_T) ≥ 0 ⟹ λ^W_T ≥ 0`) — never attempted, labelled OPEN (`R155_053` §(v) l.255–274,
  `R155_058`, `R155_060`, P47 §10.6 OPEN paragraph). Tools on record: D.47 Thm 2.1 constrained Haynsworth
  `In(A|_K) = In(A) − In(G)` with the 2×2 boundary Green matrix (`03-research/phase-116-the-logarithmic-schur-angle-conjecture/
  previous-phase-114/114_d_47_TWO_JET_PONTRYAGIN_SCHUR_GATE.md`), D.49 (1.4), D.50 rank-one parity channels; the Tate-collar
  range condition `ρ ∈ Ran L_T^{1/2}` (`03-research/phase-124-direct-first-contact/P124_011_SCHUR_COLLAR_REDUCTION.md:240-330`);
  P47 `lem:polar` (polar term has exactly one negative square on every interval), `thm:KEP2`.
* 156d — residual R1 (truncation lemma for the Gaussian witness `F₀`, `R155_054:52-56`, `R155_057:59-67,261-266`, P46 §19.6
  l.6203–6220, Thm 19.25 l.6332): one paragraph, never written. O-150.1 (Diamond–Montgomery–Vorhauer 2006): source not in
  `00-references/` — **blocked until the PDF is supplied.** Fixed-M lossiness / optimised lattice Θ(1/M): OPEN, optional.

## Round 1 (parallel reports, files of record)
| file | task |
|---|---|
| `R156_001_CONVERSE.md` | 156c: exact inertia relation between the primitive form (on `P_T`) and the complete Weil form (on `L²(I_T)`) at a fixed window through the 2×2 boundary Green matrix `G_T`; theorem `λ_min(A_T|P_T) ≥ 0 ⟹ (λ^W_T ≥ 0 ⟺ explicit sign/range condition on G_T)`; decide the condition where the primitive sign is known (T ≤ ½log3 via Thm C, T ≤ log 2); outcome either a proof of the converse or a proved counter-mechanism (a model form satisfying all window hypotheses where it fails). |
| `R156_002_R1_TRUNCATION.md` | 156d: the truncation lemma R1 for the Gaussian witness of P46 Thm 19.25 onto `C_c^∞ ⊕ ℝK`, so that Thm 12.3/19.25 apply on the small domain; closes residual R1 of `R155_057`. |
Rules unchanged: pure mathematics; scripts ≤ 60 s, one at a time; corpus grep before novelty; audit per report;
integration into any paper only after audit and check against the paper's own definitions. No sign for ζ beyond `T ≤ log 2`.
