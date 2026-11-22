# Phase 197 — Barrier theorem (tool, not an ending)

- `BARRIER_001_TRICHOTOMY_AND_ADMISSIBLE_CLASS.md`: methods = (premise class S, conclusion Ψ). Conjunction lemma (Lemma 2)
  over the atom catalogue 𝒜 (A1–A9, pinning atoms P); Theorem 3 trichotomy (comb-generic / dual certificate ≤ λ_P /
  REF-D) for T≥0.60; Prop 4 minimality of the falsifier family; Theorem 5 half-space localisation (PROVED, from lem:degen
  + margin); §6 admissible class: (D1) non-pinning FE-defect atoms inside H_T, (D2) signed stability inequality
  λ_A(T;a) ≥ −C_T Δ_T(a) (quantitative signed Hamburger). Status: memo, no audit. Row D OPEN.
- `REVIEW_BARRIER_EST_001.md`: review. Lemma 3/Thm 4 PROVED but 𝓔 is near-tautological and excludes any exact
  support axiom; Paper 46's estimate notion is integer-indexed (𝓔^ℕ), so lem:shape-est(iv) stays ARGUED quantitatively;
  Prop 6 normalisation fixed (relative slack); κ̂ ≥ m_T−λ_A−η; CIRC upgrades only #15, #16 (#25 conditional); #2, #14, #23, #26 need 𝓔^ℕ.
- `AUDIT_197_HOSTILE.md`: Lemma 2(a) false as stated (prefix/support atoms); Ξ_Q kills ARGUED (O10 primitive); Thm 3 ARGUED/CONDITIONAL, "at least one"; Prop 4: 0 ≡ a_P on the window, minimality false; Thm 5 = supporting half-space of convex K_T (PROVED), localisation CONDITIONAL on w_T≠0; D1.a false; D2 OPEN, ill-posed, near-retry INV_P/INV_Q. Row D OPEN.
- `BARRIER_D1_001_QUANTITATIVE_HAMBURGER_TANGENT_NO_GO.md`: door D1. Tangent of conductor-1 FE locus at ζ = {0} (Hamburger linear, CITED→PROVED); exact Bohr FE defect on Euler deformations Δ=½(∏(1+(α_p−1)²/(p−α_p²))−1) (PROVED, place-wise by Kronecker); NO-GO for analytic/symmetric FE-defect premises (w-blind at leading order ⇒ REF-D⁺). Memo, no audit.
- `BARRIER_D2_001_DEFECT_STABILITY_SPLITTING_AND_CONTINUATION_NO_GO.md`: door (D2). Family 𝓔𝓟 (real-exponent Euler products
  ∏(1−p^{−s})^{−θ_p}), defect Δ_T = |log ξ_a(s)/ξ_a(1−s)| on σ=¾. Thm 1 (PROVED): for every Δ with Δ(Λ)=0, λ_A ≥ −CΔ ⟺
  WP_T(Λ) ∧ sign-free rigidity of Δ. Thm 2 (PROVED): continuation from a positive reference comb transfers only
  λ_A(a_0) − d_v(a_0,Λ); barrier bites only at Λ. Thm 3: (I_T) PROVED on 𝓔𝓟_Q for T≤½log5; tails OPEN (sign-free). NO-GO 𝒦_D2.
- `AUDIT_197_2.md`: audit of D1/D2. Factor-2 normalisation (P46 v_n=2a(n)/√n) in BARRIER_001/D1/D2; D1 Thm 2 PROVED + NUMERICAL ✓; Thm 4 'symmetric' wrong, continuity suffices, relabel REF-D⁺ reduction (CONDITIONAL w_T≠0); D2 PROVED, Thm 2(ii) sharpness witness wrong (use max[φ−d_v]); Lipschitz = prop:wit-sens. R1 collapses (continuous ⇒ REF-D⁺, discontinuous ⇒ cone/certificate); R2 = AUDIT_193 #101 restatement. Row D OPEN.
- `BARRIER_W_001_NONCROSSING_INDEX_SIGNATURE_CODIMENSION_NO_GO.md`: track W (non-crossing). W1 PROVED: n₋(𝔞_T|P_T) nondecreasing in T,
  all crossings downward (spectral flow = n₋), so "index constant" ⟺ WP_T; W1′ positivity on (0,½log5+ε), ε non-explicit. W2 PROVED:
  residual R2 of D2 ⟺ μ_T(Λ)≥0 (concavity; one downward crossing at most). W3: vNW gives only 1-dim kernels, no extra constraint.
  All invariants hold on falsifiers; sole Λ datum = Σv_n c_{h*}(log n). NO-GO 𝒦_W. Memo, no audit. Row D OPEN.
- `BARRIER_X_001_INTEGRALITY_TANGENT_CONE_AND_KRONECKER_PARITY.md`: track X. Lattice dichotomy on integral Euler class (ε<1/2N pinning; else antipodal ±1 top-layer moves, PROVED); Kronecker parity Thm X2 (every FE ratio defect, smooth or sup/max, invariant under d(p^j)↦(−1)^j d(p^j) ⇒ antipodal on odd levels; NO-GO 𝒦_X^dist); {0,1}-vertex (b≤b(ζ)) breaks parity: one-sided finite set, survives falsifier list for ε<¼, but tangent cone = polyhedral divisor cone of its LP relaxation (sup of linear forms of the comb, not a def:PD certificate), decision = WP_T on finitely many deleted combs (REF-D⁺, non-pinning); parity lemma X4 for c_{F⋆} at top lags. Row D OPEN.
- `AUDIT_197_HOSTILE_3.md`: audit of BARRIER_X_001. X0 confirmed (+NUMERICAL), X1 confirmed, X4 lemma confirmed (use
  CONDITIONAL; U3 does not supply the no-zero hypothesis). X2 argument correct but 𝓘 is not σ-closed (R_p=1+2x ↦ 1−2x, b<0): NO-GO
  scope restricted. X3(a) one-sidedness FALSE (R_2=1−x^k+x^{k+1} gives a positive coordinate); X3(b,d) collapse to REF-D⁺. Row D OPEN.
- `BARRIER_Y_001_FARKAS_DUAL_AND_DELETION_FALSIFIERS_FOR_THE_01_CLASS.md` (+ `scripts/y001_*.py`): track Y. Exact Farkas dual of
  cone(S_ε−Λ) for the {0,1} class: c_{F⋆}(log q) ≥ 0 on admitted q, plus monotonicity of g along powers p^i<p^{i'} in 𝒬 (PROVED).
  Signs: hold at ½log3, log2, 0.75, ½log5+0.01 (even sector); undecided in double precision for T≥0.9 (parity degeneracy 1e-14).
  Moot: every admitted single deletion fails, λ_A(T;Λ−q) ≈ −0.08…−0.71 for T ∈ [log2, ½log11) (Galerkin = upper bound; mp check
  30 digits on 2 cases; NUMERICAL). Y1: non-pinning ⇒ falsified (NO-GO 𝒦_Y^{01}), not ℤ-specific. Residue (ii) closed. Row D OPEN.
- `BARRIER_Z_001_PARITY_SECTOR_SPLITTING_IS_LEVEL_SCALE.md` (+ `scripts/z001_parity_split.py`): track Z. Reflection R decouples P_T exactly
  into even/odd sectors (PROVED). mp parity-resolved Galerkin: μ_even, μ_odd both exponentially small, ratio 10²–10³, same decay rate
  (≈ −110…−116/unit T on [0.8,0.9]); the Y_001 "1e-14 degeneracy" = both levels below double precision, splitting = level scale; no
  intertwiner, nothing to test on falsifiers. T ≥ 1 unresolved at M ≤ 64 (upper bounds only). NUMERICAL. Row D OPEN.
