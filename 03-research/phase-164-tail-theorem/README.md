# Phase 164 — The tail theorem

**Purpose.** Attack the single point remaining to close row D: R163_401 §4.8's compensation inequality
(★_cell) at the first-contact witness, written as a statement about the tail 𝒯_X(x)=Σ_{n≥X}Λ(n)n^{−1/2+ix},
X=e^{2T_c}, of −ζ′/ζ:
**(TC)** C_{T_c}−iG²𝒯_X has no poles with Im x∈(−½,0). (TC) at the witness is RH (Rem 4.8a); the phase only
maintains that its hypothesis (Euler product over p≥X against a witness built with p<X) is the only one not
excluded (R163_901 f_t, R163_1001 f_χ/W3′, Bombieri–Hejhal).

## Index
- [R164_000_PROPOSAL.md](R164_000_PROPOSAL.md) — diagnosis P1–P4, (TC), lines L1 (hybrid Euler–Hadamard cutoff), L2 (BF_θ^disc, θ≤1/3), L3, round plan.
- [R164_301_INTEGRATION_LOG.md](R164_301_INTEGRATION_LOG.md) — editor (L3): grid merge (parts 12–13; part 14 in §6, part 15 in §9), Paper 48, R163_401 v7/v8/v9, citation verification, Thm R literature note (§7).
- [R164_101_HYBRID_KZ.md](R164_101_HYBRID_KZ.md) — L1a, hybrid Euler–Hadamard cutoff: (KZ) is E1, DEAD (round 1).
- [R164_102_POSITIVE_TAIL.md](R164_102_POSITIVE_TAIL.md) — L1b, positive tail measure: Thm A, Thm L, Thm H (round 1).
- [R164_201_BEURLING_BELOW_THIRD.md](R164_201_BEURLING_BELOW_THIRD.md) — L2, Beurling frontier below 1/3: Theorem L (round 1, repaired).
- [R164_190_AUDIT.md](R164_190_AUDIT.md) — audit, rounds 1–2; synthesis: identification theorem.
- [R164_291_AUDIT_201.md](R164_291_AUDIT_201.md) — audit of R164_201: Theorem L PROVED after R1/R2; scope downgraded (R4).
- [R164_401_O164_101_CONSTRUCTION.md](R164_401_O164_101_CONSTRUCTION.md) — O164.101, construction side: Thm R (positive rigidity off ℕ), O164.101 ⟺ ¬RH (round 2).
- [R164_402_O164_101_OBSTRUCTION.md](R164_402_O164_101_OBSTRUCTION.md) — O164.101, obstruction side: Props P/S/F/B, superseded by Thm R (round 2).
- [R164_501_ZERO_SIDE_SINC.md](R164_501_ZERO_SIDE_SINC.md) — sinc on the zero side: Thm SA, Cor SA.1, Prop 4; route DEAD (E1, no room) (round 3).
- [R164_502_DETERMINANT_MOMENTS.md](R164_502_DETERMINANT_MOMENTS.md) — determinant / Szegő / spectral moments: L0–L8; DEAD (window data) (round 3).
- [R164_503_OFF_LATTICE_BEURLING.md](R164_503_OFF_LATTICE_BEURLING.md) — Beurling off the lattice below 1/3: Goal B ≥ RH + quadratic GRH; Goal A OPEN; O164.503a–d (round 3).
- [R164_491_AUDIT_401_501.md](R164_491_AUDIT_401_501.md) — audit of Thm R and R164_501 (F1–F6): accepted, fixes applied (round 4).
- [R164_601_UNCERTAINTY_OBSTRUCTION.md](R164_601_UNCERTAINTY_OBSTRUCTION.md) — O164.501.1 closed (dlVP test over G²), discarded-term principle (Thm 3.1), W2/M; residual O164.601.1 (round 4).

## Status
**Phase closed in rounds 1–4; (★_cell) OPEN.** (TC), row D: OPEN. No record label changed in this phase.

## Round 1 (construction, audit in R164_190)
- R164_101 (L1a): (KZ) is E1, DEAD (Thm E1 PROVED). New: Prop D (deletion has exactly ζ's Z_X and opposite sign: the sign lives in the window × tail coupling).
- R164_102 (L1b): positive tail / Bernstein DEAD (Thm A PROVED: off-line zero in any cone with ζ's window and a positive tail, paid for with a double pole). New: Thm H (within the witness's class, every member with an off-line zero moves infinitely many zeros), Thm L (Landau: positivity blind to zeros, sensitive to poles).
- R164_201 (L2): L2a closed negatively within the Witt class 𝒦_θ (Theorem L PROVED: error ≫ x^{θ+δ} for θ<1/3, the threshold is real); L2b stops at Lemma D (blind to zeros). Problem 6 below 1/3 OPEN; countermodels only off the lattice (O164.201a).
- R164_301 (editor): grid 975 routes ■10 ◩20 ◧34; Paper 48 25 pp with f_χ, W3′, Thm O; R163_401 v7.
- **Convergence: a single question, O164.101** (positive Beurling system with ζ's window+Γ+FE+pole and an off-line zero in a cone). Round 2 attacks it by construction and by obstruction.

## Round 2
- R164_401: **Thm R (PROVED, audited):** integer measure ≥ 0 off ℕ + gap (1,X) + ζ's FE with its poles ⇒ f = ζ. Hamburger with positivity instead of integer support. Cor: O164.101 ⟺ ¬RH; L1 dies by identification.
- R164_402: Poisson form of the FE (Prop P), forced sign change (Prop S), infinite erased mass (Prop F); superseded by Thm R (Q0 answered: 𝒞 = {ζ}).
- R164_291: audit of Theorem L: PROVED after R1/R2; scope downgraded (no x^{1/3} floor); fixes applied.
- **Synthesis: identification theorem** (R164_190 §Round 2): every global property separating ζ from the falsifiers identifies it. (★_cell) can only be proved using ζ individually. Row D remains OPEN.

## Rounds 3–4
- R164_501: **Thm SA (PROVED)**: every ≥0 test annihilated by the kernel equation is a kernel square ĤĤ^#; critical node density, no room for Thm R's sinc (E1). **Prop 4 (PROVED)**: Λ's tail with a sign at real height (identity, off-line weight y/γ_q²).
- R164_502: L1: every spectral invariant of A_T is window data; determinant, heat trace, moments, Szegő–Widom DEAD; tools L4, L5, L6.
- R164_503: Goal B ≥ RH + quadratic GRH (rejected as a route); prime-ceiling rounding at x^{1/2} (ARGUED); Goal A OPEN; O164.503a–d.
- R164_491 (audit): Thm R PROVED after F3 (ζ's explicit residues) and F1; novelty: "not found in this form," possibly folklore.
- R164_601: O164.501.1 CLOSED (the test exists: dlVP over G²); the uncertainty reading is refuted; **discarded-term principle** (Thm 3.1) + W2/M: route DEAD; residual O164.601.1 = (★_cell) weighted by K.
- Editor (R164_301 §9): grid part 15 (989 routes, ■10 ◩20 ◧34), Paper 48 (thm:R with F3, rounds 3–4 paragraph), R163_401 v9.
- **Closure:** every route from R164_000 closed with proof; identification theorem + Thm R; **every route returns to (★_cell)** (RH at the witness).
-, phase 165 closed (R165_190): bracket 0.8047 < T_c ≤ min_ρ τ(ρ) PROVED (Det+), Det− DEAD, critical interlacing refuted, sign variable ω(E); see 03-research/phase-165-critical-interlacing/README.md.
