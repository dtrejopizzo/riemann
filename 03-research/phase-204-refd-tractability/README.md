# Phase 204 — Discarded reformulations: does any of them resolve independently of D?

## Mandate (verbatim)
«Thoroughly review every discarded reformulation (REF-D): if they have their own proof path, with applicable
general theorems, even if they are stronger than D, solve them — something independent of D that is then used as
input. One by one, with audit, so none is lost; it is likely that some of them can.»

## Protocol (each reformulation goes through the 4 steps; ≤5 simultaneous agents)
1. **Inventory**: TRACT_001 (13 structural), TRACT_D_README (82 from the README), TRACT_E_PHASES (~250 from phases
   100–189 + residues). TRAT column = YES / TRANSFER / NO, unifying duplicates; each YES with a general theorem,
   missing hypothesis (other than the sign), first lemma, input for D.
2. **Re-verification of the inventory**: an audit rereads every TRAT verdict (especially the NOs and TRANSFERs) and
   can raise it to YES or lower it; nothing is left out by omission.
3. **Construction one by one**: for each YES (in ranking order), the first lemma is attempted with its own
   path; label PROVED/CONDITIONAL/OPEN/NO-GO; declares the trait of Λ (lem:transfer: every proof must fail on
   DH T≥9/5 and Epstein T≥1.59).
4. **Audit of each construction** before recording; index in the same session; if PROVED, verification
   against the definitions of Paper 47 and integration as an independent result (input).

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
- **Closed without touching D (in P47):** H1⁻ (cor:H1minus), Theorem A∞ (lem:archcount), prop:WT, rem:conjunctions,
  rem:inertiatower, rem:sosatoms, PC-2. New reading: the even sign is the exact cancellation by the comb of all but
  one of ≍ 4T negative archimedean directions (count, not bound); the inertia of 𝔄_ev = pole + hyperbolic pairs.
- OPEN closable without D: Lemma LCB; PRED-aP; upper bound of A∞. No sign. L′♯ OPEN.
