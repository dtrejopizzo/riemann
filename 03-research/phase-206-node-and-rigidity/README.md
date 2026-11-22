# Phase 206 — The node (step 4) and the rigidity family E∧F

(A) pour the effort into building the node of the mechanism's skeleton, independently of D;
(B) in parallel, look for objects where Euler and the functional equation coexist in a nonlinear way by nature
(reciprocal theorems Hamburger/Hecke/Weil, Rankin–Selberg, theta with Euler product) and ask whether a quadratic
version of that rigidity produces a sign.

## Mechanism skeleton (even sector) — status
1. **Reduction (PROVED, P46 prop:H + cor:H1minus).** W^ev_T ⪰ 0 ∀T ⟺ n₋(𝔄_ev(T)) = 1 ∀T (𝔄_ev = archimedean + comb, without pole).
2. **Finite coordinates (PROVED, P46 lem:combsine; RFIN_TRACT_001 RF.1).** On E_N^ev = span{sin(πk(x+T)/2T), k odd ≤ N}, N ≈ 4T:
   𝔄_N = (𝔪 + 𝔢)_N − 2ccᵀ + Φ_N,
   𝔪 = gamma factor of conductor 1 (symbol m), 𝔢 = pole kernel (symbol 1/(¼+τ²)), c = coefficients of the polar
   direction χ_ev (c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²))), Φ_N = compressed fluctuation form −𝓕_T: Σ_{n≤e^{2T}} (Λ(n) − 1)·(2/√n)·𝓕_F(log n)
   [CORRECTED by NODE_001/AUDIT_206: Φ_N = Stieltjes integral of 𝓕_F against d(ψ(t) − t), not Σ(Λ−1)+boundary; exact statement in NODE_001 (N)].
3. **Budget (PROVED, lem:archcount + A∞(t₀′) + Weyl).** n₋((𝔪+𝔢)_N) = N′ ≈ 1.95T (even sector). n₋(𝔄_N) = 1 requires (NECESSARY condition, not equivalent)
   n₊(Φ_N) ≥ N′ − 1 on the orthogonal complement of c: exact cancellation in the count, not a perturbation.
4. **THE NODE (OPEN).** For every F ∈ E_N^ev with ⟨F, c⟩ = 0:   Φ_N(F) ≥ −(𝔪 + 𝔢)(F).
   ("the fluctuation of the primes dominates the gamma deficit in every direction except the polar one").
   Forced properties (PROVED in phases 200–205): (i) it uses that Λ comes from the Euler product over ℕ (a_P the false one; mechanism B_P
   PROVED, TOOLS_204U); (ii) [CORRECTED AUDIT_207] 𝔪 fixed at conductor 1; quartets and f_t have the SAME node (lem:shape-quartet: their negativity
   lives in −kβ_z, outside 𝔄_N) ⇒ at the node the coordinate F has no falsifier; Epstein/DH give another spectrahedron, not a point of the same one;
   (iii) [CORRECTED AUDIT_207] for the node, Φ200′ loses half of F: the requirement "E ∧ F" becomes "E with 𝔪 fixed" (O2 of CLASS_001);
   (iv) not reducible by H1PLUS (1.4) to zero data;
   (v) it is not h*, nor tests with ζ coefficients, nor Möbius inversion, nor pairing with R_Λ (AUDIT_205_SKELETON).
5. **Dead mechanisms for the node:** SOS (thm:sos: every certificate = explicit formula on flat-top tests); size bound
   |Φ_N| ≤ 𝔪 (false pointwise, SKELETON_002; dlVP without sign, M1); Hamburger linear rigidity (BARRIER_D1 Thm 4: every
   analytic/C^{2m} defect with zero only at Λ is blind to w_T; residue R1 closed); bilinear in Λ via h* (Theorem X); Szegő/Widom
   (critical sampling, RFIN_TRACT RF.2); continuation in T (𝒦_W, L2_INTERLACE); Perron–Frobenius/Markov (H1_TRACT).

## Index restrictions for track (B)
- Front A (phase 193): Petersson/Maass–Selberg/Rankin–Selberg blind to the comb; comb-generic Hecke multiplicativity (PROVED).
- SYNTHESIS §4: sign of RS (|a_p|² ≥ 0) and FE rigidity share the blind spot of Kronecker parity; weight gap: every
  built-in positivity reads the primes at weight ≤ n^{−1}; the cell "weight n^{−1/2} + global FE + built-in
  positivity" is EMPTY in the literature (the only cell not dead).
- BARRIER_D1 (quantitative Hamburger with sign): NO-GO in the analytic class; INV_A (rigidity 𝔐 = {ζ}): retried without a reason.
- Required new reason: the object must lie in the empty cell and the sign step cannot be an analytic defect of the FE.

Memos: NODE_*.md (track A), RIGID_*.md (track B), AUDIT_206_*.md (audit).

## Corrections (NODE_001)
- Φ_N is NOT Σ(Λ(n)−1)·(2/√n)𝓕_F(log n): it is the Stieltjes integral of 𝓕_F against d(ψ(t) − t) (Euler–Maclaurin leaves a
  nonzero term; n = 1 alone already contributes +2‖F‖²). Exact statement in NODE_001 (N).
- Step 3: the count n₊(Φ_N|_{c^⊥}) ≥ N′ − 1 is a NECESSARY CONSEQUENCE of the node, not an equivalence.
- ½log3 is not a model case (even block of dimension 1, empty node). First case with content: T = ½log5, block {e₁,e₃}, N′ = 2
  (NUMERICAL): margin 0.00185 (= sum of zeros); the prime 2 is paid for by phase resonance ω₃·log 2 ≈ 1.29π; a_P falsifies it (−0.477);
  cΛ fails for c < 0.9924. No arithmetic identity makes it positive.
- Track B (RIGID_001): 12 objects, none evades the index; Lemma N: quadratic rigidity = ‖generic norm‖² + identity F.

## Status after AUDIT_206_001
- Node PROVED for T ≤ ½log5 (corollary of P46 thm:log5W); OPEN in general. The 2×2 margin at ½log5 is a truncation artifact
  (with 3 modes: 1e−6–1e−7). Resonance of 2: coincidence. N5-uniform withdrawn. No sign step in either track A or B.

## Other files in this folder

- `INTEGRATION_206_ZCERT_001.md` — Integration of rem:zcert into Paper 46 (phase 206).
- `ZCERT_001.md` — Certificate of the node from the zero side (phase 206).
- `ZCERT_001_data/` — numerical data for `ZCERT_001` (9 files).
