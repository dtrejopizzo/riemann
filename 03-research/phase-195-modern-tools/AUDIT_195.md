# AUDIT_195 — audit of INV_L_001 (phase 194) and INV_M/N/O/P_001 (phase 195)

Audit. Checked against Paper 46 main.tex: eq:symbol/eq:form
(s_T = m − Σ_{N_T} v_n cos, v_n = 2Λ(n)/√n), eq:W, eq:m (C_0 = −5.3721834), λ_A/λ_W (l.129), thm:band (l.7489), thm:C/sec:cert, thm:O, eq:nuw.

## (a) INV_L_001 — L3 Green identity: VERIFIED, one correction
- 2∂_σu_S(½+iτ) = m(τ) − Σ_{p∈S,k} v_{p^k}cos(τ k log p); atoms with log n ≥ 2T are invisible against |F̂|² ⇒ LHS = 𝔞_T(F) for S ⊇ S_N. OK.
- Sources: Γ_R(1−s̄) pole at w=0 ⇒ s=1 (next s=3 ∉ Ω); (1−p^{−w})^{−1} poles at w = 2πik/log p ⇒ s = 1+2πik/log p. log|·| near a pole
  has Δ = −2πδ, so Δd_S = +2πδ. The k=0 source of each p coincides with s=1 ⇒ coefficient (1+|S|)|Φ_F(1)|². OK.
- Green's second identity on Ω: left edge d_S = 0 and outward normal −∂_σ gives ∫G∂_σd_S; right edge gives B₂; ΔG = 4|Φ′|². Signs OK.
- Smoothness: needs |Φ_F|,|Φ_F′| = o(|τ|^{−1}/log|τ|) uniformly in ½≤σ≤2; C_c^∞ is more than enough; the check's F=(1−x²)⁴ (C³) also qualifies.
- Re-run: LHS −0.4794314, RHS −0.4794303 (reproduced; residual consistent with truncation |k| ≤ 60).
- **Error in (b):** Σ_k|Φ_F(1+2πik/log p)|² = (log p)·∫_0^{log p}|Σ_j g(t+j log p)|²dt, g = F e^{·/2}; the stated factor 2π/log p is wrong
  (numerical check T=0.6, p=2: both sides 0.2623662). Qualitative content unaffected.
- L2 "⟺ S⊇S_N": forward direction PROVED; converse only ARGUED.
- Corpus check incomplete: G7A-120 (zero-residual Green identity) and G4A-122 (two-prime finite Green complex) not cited. Object differs
  (zero-free d_S, sources at local reflected poles) ⇒ not a retry, but must be cited. (Π_L) = REF-D: label correct. No sign.

## (b) INV_P_001 — P2 overclaimed
1. L2 constant is not uniform: Σ_{n≥N} e^{−πn²/y} ≤ (1 + y/(2πN))e^{−πN²/y}, factor ≍ N/T at y=Y. Also |y^{−s/2}−y^{−(1−s)/2}| ≤ 2
   gives ∫ dy/y ≍ log Y, not Y. Correct bound: ε_T ≪ (N/T)·log Y·e^{−2πT} = O(T^0 e^{(2−2π)T}). Conclusion (exponentially small) survives.
2. Domain: P1 needs 0<σ<1; the tail ∫_Y^∞ e_S(y) y^{−(1−s)/2}dy/y has e_S ≍ ψ_S(1/y) ≍ (log y)^{|S|} and diverges for σ ≥ 1. L3's Ω = (½,2)
   contains the sources (σ=1) and B₂ (σ=2). So the "edge-band" reading is PROVED only on ½<σ<1, OPEN on Ω. Downgrade.
3. Falsifier a_P (2 ∉ S′): removing 2 removes all even n, so the deficit in e_{S′} is ≍ √y, not ≍1; and with |y^{(s−1)/2}| = y^{−1/8} at
   σ=¾ the displayed integral is O(1), not ≍Y^{1/8}. Internally inconsistent; separation plausibly holds (stronger), stays ARGUED.
4. "First non-comb-generic statement": inherited from L2 = support identification 𝒞_1 (R163_1001), indexed. Not a new handle.
5. P3 PROVED; P4 (i),(iii) PROVED; P4 (iv) (failure of a sampling constant) is ARGUED, not PROVED.

## (c) INV_N_001 — gap ceiling: CONFIRMED (narrow class)
- Re-ran INV_N_001_be_check.py: m(0) = −5.372183, W_T(0) = −2.080998, ess inf W_T = −2.534483 at |s| = 0.143918⁺ (one-sided at the atom
  jump), R(t) = 2.108375, Ritz P₁–P₆ g_T ≤ 1.941379 ⇒ g_T + ess inf W_T ≤ −0.593. δ_T²/2T = 1.246e−4. All match.
- Logic: any bound λ_A ≥ K·(1−δ²/2T) + inf_{𝒫_T}⟨W_T F,F⟩/‖F‖² is ≤ g_T + ess inf W_T, since K ≤ g_T (CD ⇒ Poincaré, Lichnerowicz) and
  the multiplication form's infimum on a codim-2 subspace equals ess inf W (bumps). Correct. W_T formula consistent with eq:m and v_2.
- Caveat: the class 𝒦_BE is "sum of separately minimised pieces"; the NO-GO is near-tautological given λ_A(½log3) ≈ 9.4e−4.
  Constants NUMÉRICO (float mpmath, no interval arithmetic). Labels honest.

## (d) INV_M_001 — CONFIRMED
- M0: the thm:band subspace span{V_{∓D/2}F₀} lies in 𝒫_T, so λ_A(T) > 0 gives a PD 2×2. Zhu certifies the complete form (λ_W ≤ λ_A, so it
  transfers); a cleaner citation is P46's own certified λ_A ≥ 2.5e−12 on T ≤ ½log5. Face {1,3} at T = log 2 needs T₀ ≤ 0.144.
- M1/M2 correct (Brändén 2007 Rayleigh criterion for multi-affine; specialisation at real 0 preserves stability). NO-GO is narrow:
  a PD Gram symbol is never real stable. Labels OK.

## (e) INV_O_001 — confirmed except §3 label
- (X) and O1 (|cos| ≤ 1, valid for all F ∈ 𝒟_T) PROVED; O2 (HKS functionals = dual certificates of def:W/eq:nuw ⇒ REF-D) PROVED.
- §3 "Mazáč = magic functions, CITED": Hartman–Mazáč–Rastelli relate Cohn–Elkies functionals to the spinless modular bootstrap; no cited
  theorem identifies Mazáč functionals transposed to (X) with interpolation bases at {±log n}. Downgrade to ARGUED. Closure survives via O2.

## Net
No sign anywhere; no retries found; no circularity beyond the declared REF-D residues. Corrections applied in ROUTES-TRIED-INDEX
([AUDIT_3]), grid part19 (AUDIT_195), crossword addendum. Row D: OPEN.
