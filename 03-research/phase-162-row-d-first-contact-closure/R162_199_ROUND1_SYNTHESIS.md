# R162_199 — Round 1 synthesis

## Gate 0 — CLOSED
R162_001: T ↦ λ_A(T) is continuous (dilation + rank-two Tate correction). check R162_190:
CORRECT WITH FIXES, fixes applied. Integrated into Paper 46 as lem:contA; lem:firstcontact is now
unconditional (rem:contA removed).

## Gate 1 — OPEN; three NO-GOs
- B1 (R162_101, minimality / window variation): NO-GO. Shrinking the window has exactly zero first
  variation (a(γ)=a(γ−F)); minimality is exhausted by H_{T_*}≥0, N_{T_*}≠0; every Hadamard-type
  inequality also holds for positive eigenvectors (fails F1), and uses neither comb sign nor Λ*1=log.
  Surviving need: a two-sided arithmetic input at T_* (lower bound on λ_A just right of T_* in terms
  of R_LF, or a signed birth-collar law at a prime power e^{2T_*}).
- B2 (R162_102, Gamma-residue uniqueness): NO-GO. W^0≡0 ⟺ R_LF=0 ⟺ F=0 for every F (trivial);
  interior homogeneous uniqueness is FALSE for Davenport–Heilbronn (genuine nonzero mode), OPEN for ζ.
  All steps use only the functional equation and Γ-factor; Λ*1=log enters only via thm:PCfinite in the
  unproved passage (PC)→scattering. New falsifier: DH interior mode.
- B3 (R162_103, first chamber 0.8<T_*<½log5): NO-GO. Finite-modification models a^κ (same zeros and
  pole) satisfy all six chamber-local ingredients and have genuine first contacts with R_LF_0≠0; the
  2,3,4 collar is too short (<0.0095) to trigger gap enlargement. Chamber exclusion ⟺ λ_A≥0 up to
  ½log5=0.8047 (certified numerics, not Gate 1). The only discriminator is the global typed Sonin
  identity g_+ + C_log R g_- = 0, i.e. R161_011 (4.2), which remains OPEN.

## State
Gate 1 reduces, after round 1, to the global Sonin range-intersection lemma R161_011 (4.2) with the
Euler product (not only the functional equation) used at the vanishing step. No closure of row D.
