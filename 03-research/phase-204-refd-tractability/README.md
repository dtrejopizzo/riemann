# Phase 204 — Discarded reformulations: does any of them resolve independently of D?

## Mandate (verbatim)
«Thoroughly review every discarded reformulation (REF-D): if they have their own proof path, with applicable
general theorems, even if they are stronger than D, solve them — something independent of D that is then used as
input. One by one, with audit, so none is lost; it is likely that some of them can.»

## Protocol (each reformulation goes through the 4 steps)
1. **Inventory**: TRACT_001 (13 structural), TRACT_D_README (82 from the README), TRACT_E_PHASES (~250 from phases
   100–189 + residues). TRAT column = YES / TRANSFER / NO, unifying duplicates; each YES with a general theorem,
   missing hypothesis (other than the sign), first lemma, input for D.
2. **Re-verification of the inventory**: an audit rereads every TRAT verdict (especially the NOs and TRANSFERs) and
   can raise it to YES or lower it; nothing is left out by omission.
3. **Construction one by one**: for each YES (in ranking order), the first lemma is attempted with its own
   path; label PROVED/CONDITIONAL/OPEN/NO-GO; declares the trait of Λ (lem:transfer: every proof must fail on
   DH T≥9/5 and Epstein T≥1.59).
4. **Audit of each construction** before recording; index immediately; if PROVED, verification
   against the definitions of Paper 46 and integration as an independent result (input).

## Rules
never D⟺RH (reformulations written via RH are rewritten D-only); honest labels; a result
independent of D is valid even if it does not close D.

## Status
- In progress: TRACT_D, TRACT_E (step 1); L2_INTERLACE (step 3, route (L2) of TRACT_001); P1_BBSTAR (step 3, gap P1
  of BARRIER_SOUND: quadratic operator on Λ PSD via BB*, Weil-curves form).
- Done: TRACT_001 (PARTIAL: 3 routes with their own path), BARRIER_SOUND (3 layer closures reclassified ARGUED).
- Queue (step 3): polar capacity g_±(T) (T6.1/T6.2); Lemma F half-line (T10.1/T10.2); P2 (exact Schur coupling
  archimedean + Lemma R + gap); P4 (contact sign pattern); + all the YESes of TRACT_D/E after step 2.

## Status (night) — closing the batch
- Complete inventory (4 parts + 3 audits): 43 distinct reformulations, 0 YES / 22 TRANSFER / 21 NO.
- Closed constructions (all audited): L2 interlacing, P1 BB*, polar capacity, Lemma F, P2 Schur, damped K12,
  P4 sign pattern, G16.0, WT halves, (C★), H1⁺. No amplification (Prop S; AUDIT_W1; CALIB_R4).
- **Corrected map:** Φ200 is not a class barrier (O1 REFUTED); Φ200′: every proof uses ≥ 2 channels (E Dirichlet
  series over ℕ, F conductor 1) in the SAME sign step (composition, not chaining); no route in the corpus composed them.
- **Closed without touching D (in P46):** H1⁻ (cor:H1minus), Theorem A∞ (lem:archcount), prop:WT, rem:conjunctions,
  rem:inertiatower, rem:sosatoms, PC-2. New reading: the even sign is the exact cancellation by the comb of all but
  one of ≍ 4T negative archimedean directions (count, not bound); the inertia of 𝔄_ev = pole + hyperbolic pairs.
- OPEN closable without D: Lemma LCB; PRED-aP; upper bound of A∞. No sign. L′♯ OPEN.

## Other files in this folder

- `AUDIT_204_CLOSURES_001.md` — Audit, step 4 of phase 204: is any of the five closures wrong?
- `AUDIT_204_CSTAR_001.md` — Audit of (C★) "Hamburger inequality with defect" (COMPOSE_EF_001 §5).
- `AUDIT_204_H1MINUS_001.md` — working memo
- `AUDIT_204_TRACT_D_001.md` — Audit of the tractability inventory, part D (TRACT_D_README_001).
- `AUDIT_204_TRACT_E_001.md` — Audit of the tractability inventory, part E (phase 204, step 2).
- `AUDIT_204_TRACT_F_001.md` — Audit of TRACT_F_PHASES000_001 (phase 204, step 2, phases 0–99).
- `AUDIT_204_W1_001.md` — Audit of Lemma W1 and Cor W1′ (WEAKEN_001 §K11, phase 204o).
- `COMPOSE_EF_001.md` — First attempt at a genuine composition (E, F): the FE as a symmetry of h_par (phase 204q).
- `FINAL_204_001.md` — Final synthesis of phase 204: did any discarded reformulation have its own path to resolution?
- `G16_GATE_001.md` — Gate G16.0: the «gauge-existential Lemma F» (phase 204m).
- `H1PLUS_001.md` — (phase 204t): H1⁺ = n₋(𝔄_ev(T)) ≤ 1 ∀T, EXACT inertia accounting via the comb structure.
- `H1_TRACT_001.md` — Tractability audit (phase 204r): (A) H1⁺ = n₋(𝔄_ev(T)) ≤ 1 ∀T; (B) 𝔄_odd(T) ≻ 0 ∀T.
- `INTEGRATION_204_001.md` — Integration into Paper 46 of the phase-204 inputs.
- `INTEGRATION_O1_001.md` — Integration of O1 into Paper 46 (phase 204p).
- `K12_DAMPED_001.md` — (Ω_{t₀}): the damped comb is the chord toward ρ_κ, not the line cΛ; Lemma E.2 resolved (limsup form empty, liminf form ⟺ (E_γ)); K12 → TRANSFER on packets (phase 204j).
- `LEMMA_AINF_001.md` — Lemma A∞ with explicit constants (phase 204s).
- `LEMMA_F_HALFLINE_001.md` — Lemma F on the half-line as a statement in its own right (phase 204g, route 3 of TRACT_001).
- `O1_COMPOSITION_001.md` — Branch composition rule of Φ200 (phase 204p).
- `P2_SCHUR_001.md` — Exact Schur complement «Euler ⊕ gap» (gap P2, phase 204i).
- `P4_SIGNPATTERN_001.md` — The sign pattern of c_{g*} at the contacts (gap P4, phase 204k).
- `POLAR_CAP_001.md` — Route 2 of TRACT_001 (R6): the polar capacity 𝔊_T = diag(𝔤_ev, 𝔤_odd) as an object in its own right.
- `TOOLS_204U_001.md` — Three tools closable without D (phase 204u): Lemma LCB, PRED-aP, upper bound of A∞.
- `TRACT_F_PHASES000_001.md` — Phase 204, part F: the «CIRCULAR»/REF-D entries from phases 0–99, one by one.
- `WEAKEN_001.md` — Phase 204o: can the hypothesis consumed by the 22 TRANSFER entries be weakened to something PROVED?
- `WT_HALVES_001.md` — The two halves of Lemma WT (prop:WT of Paper 46) as independent statements.
- `LEMMA_AINF_001_data/` — numerical data for `LEMMA_AINF_001` (2 files).
- `LEMMA_F_HALFLINE_001_data/` — numerical data for `LEMMA_F_HALFLINE_001` (6 files).
- `TOOLS_204U_001_data/` — numerical data for `TOOLS_204U_001` (7 files).
