# Phase 212 — Complete reading annex: files of phase 211, block 8

Source: `../phase-211-sign-sandbox/`, `*.md` files in alphabetical order (`ls *.md | sort`), from `ROUND_016_B.md`
to `TOOL_001_GALERKIN_MP.md` inclusive: 25 files, read completely. Notation of
`../phase-211-sign-sandbox/STATEMENT_001.md`: (★) is λ_A(T) ≥ 0 for all T. Labels as recorded by each
file. Abbreviations: 𝒯 Poisson tail map; Ψ_f = 𝒯(ℱf) the tail of Ef on (−∞, −T); Φ_f(x) = e^{x/2}Σ_{n≥1}f(ne^x);
𝒲 tail form; 𝒜_∞ archimedean form; λ = e^T, N = e^{2T}; d_k = 1 − χ_k (prolates ψ_k of [−λ, λ]).

## 1. Entries by file

### 1.1 ROUND_016_B.md — direct tails of the high block, chirp matrix, first Poisson cell
- Object: chirps F_N(x) = 1_{x<−T}e^{−x/2}u(Ne^{−x}), u = ε_kℱ(ψ_k1)|_{|ξ|>λ}; matrix B_{NN′} = (1/π)∫_0^∞ m Re(F̂_NF̂̄_{N′})
  − (log N + log N′)⟨F_N, F_{N′}⟩; gauge quotient metric ℓ_g = 2 dist²(ℱf|_{(λ,∞)}, tails of the gauge |y| < 1/λ).
- Lemma 2.1 (dilation form) PROVED: F_N = N^{−1/2}τ_{log N}F₁, 𝒯u = 𝔇F₁, ‖F₁‖² = ½‖u‖²; the tail form is
  independent of T in F₁ («universal» framework of DOSSIER §7.1, used, not claimed).
- Lemma 2.2 (first Poisson cell) PROVED: u supported on λ < |ξ| < 2λ ⇒ no comb, 𝒲[𝒯u] = 𝒜_∞[F₁] at length log 2.
- Lemma 2.3 (complete tail form W_T(Ef) = 𝒲[Ψ_f] + 2A(Ψ_f)B(Ψ_f)) CITED + NUMERICAL (5 digits on one probe).
- Observation 2.4 (jump part, formula J²(1/2π)∫m/(β²+τ²)) PROVED; choice of β ARGUED.
- NUMERICAL: three methods agree (Galerkin unit D = λ·a_T(Ef)/‖f‖²); the drift is 100 % B₁₁ = 𝒜_∞[F₁]
  (comb weight 2 log 1 = 0); it is not the jump, nor the nonresonant pairs (≤ 5 %, X_eff ≈ 1), nor the resonant comb.
- ARGUED: the high block degenerates in D units (leak toward an infinite-dimensional gauge); (HR) must be stated in ℓ_g:
  (HR_g) 𝒢[b] ≥ κ_T·ℓ_g^S[b] on the high block, κ_T independent of K — OPEN (values ≥ 0.80, still decreasing).
- Unsigned remainder: the floor of (HR_g). Falsifiers: everything proved is Λ-blind (no sign step).
- Recorded failures: «the drift is the jump», «it is nonresonant MV», uniform floor in D units; omitting 2AB in the
  limit problem (negative from R = 3: must not be omitted again).
- Result: PIVOT. Next step: first-cell bound 𝒜_∞[F] ≥ μ‖F‖² under the transported functionals, and ℓ_g with
  the gauge resolved. Taken up: the first part by ROUND_017_C (Theorems 3.1, 3.3); the resolved ℓ_g was not taken up in the block.

### 1.2 ROUND_017_A.md — coupling vector of the survivor, Schur correction and falsifiers
- Object: survivor f_* = 0.1037ψ_0 − 0.7340ψ_4 + 0.6712ψ_8 (kernel of f(0), ℱf(0), A(Ef), B(Ef)); F = Ef_*/‖Ef_*‖,
  H = P_T ⊖ F, b(G) = a_T(F, G), ρ = a_T(F), C = a_T|_H.
- Prop. 1.1 (Schur/secular form) PROVED: (★) at T ⟺ C ⪰ 0 and ρ ≥ sup_{G∈H} b(G)²/a_T(G).
- Prop. 1.2 PROVED for admissible f with f(λ) = 0, ARGUED for the survivor: b(G) = ∫_0^∞ h_G dν,
  h_G(u) = ⟨Ψ, G(·+u)⟩, ν = ½K du + Σ_{n≥2}Λ(n)n^{−1/2}δ_{log n} (uncollapsed comb), b_Tate ≡ 0 on P_T; on E images,
  b(Eg) = 𝒲(Ψ_f, Ψ_g) (second-level radical identity (1.3), comb collapsed to log N).
- Prop. 1.3 PROVED: the odd part of Ef, f ∈ span{ψ_0, ψ_4, ψ_8}, is −½E(u1_{(λ,∞)}) + O(d), Λ-free.
- Prop. 3.1 PROVED: under cΛ, a_P, finite e, b changes by the radical defect X_w = 𝒞_{Λ−w}(Φ_{f*}, ·), O(1).
- NUMERICAL (T = 0.8, 1): ρ/λ_A = 1.58/1.49; Schur part 0.366/0.329; arch and comb parts 10²–10³⁸ times the correction
  and they cancel; ≈ half is Λ-free parity defect, the rest tail–tail coupling to the even rungs.
  Threshold c > 1: λ_A/Π_T(F) (5·10⁻²² at T = 1); c < 1: size of the next rung (corrects the 1.5·10⁻⁴ of ROUND_015_B).
- Failures: hypothesis of 015_B §3.5 («comb-dependent cross terms»); five-prolate block model.
- OPEN: Schur balance of the exact survivor (exact 𝒲[Ψ_*] not computed); whether the tail–tail inequality survives
  c·log N (if it survives, (R) is robust to the comb and is not a sign step).
- Result: PIVOT. Next step: tail Gram on (Ψ_*, Ψ_g) in dilation coordinates, Schur 2×2 and 3×3, repeat
  with c·log N. Not taken up in this block (STATE_001/002 summarize it; no later file of the range computes it).

### 1.3 ROUND_017_B.md — band margins at full range T = 2.5–4, closed matrix-free form
- Object: A_τ^{(η)} compression of A_τ to span{e_1..e_K}, e_k = sin(a_k(x+T))/√T, a_k = kπ/2T; margin
  μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}).
- Prop. 1.1 PROVED: A_τ^{(η)} = ½(𝔈 + 𝔈ᵀ), 2T𝔈 = CS − ESCE + ESHE + HS + Dd, C Toeplitz (a_j − a_k)^{−1}, H Hankel
  (a_j + a_k)^{−1}; the comb enters only through s_k = Σ c_n sin(a_kℓ_n), d_k = Σ c_n(2T − ℓ_n)cos(a_kℓ_n), c_n = v_n cos(τℓ_n).
- NUMERICAL: min μ_⅛ = 0.2566 (T = 2.5, full range [1.1, 3]·2πN), 0.1140 (T = 3, full), ≤ 0.1343 (T = 3.25),
  ≤ 0.0782 (T = 3.5), ≤ 0.1341 (T = 4) (partial ranges); direct W_T = margin to 10⁻⁶; no negative value; no
  certificate. The zero extrapolated at T ≈ 3.3 does not appear; the minimum is set by isolated alignment cells.
- Falsifier: cΛ fails (HB_η) in the cell at T = 3.5 for c > 1.0111 (decreasing budget c*(T)).
- Failures/«do not reuse as a shortcut»: screens g_T (flat-window tone), dense block k ≤ 96, diagonal — valid
  Rayleigh bounds but 0.2–0.9 above; Lanczos with pure warm start (fails at 6 % of points).
- Next step: cover [1.2, 3]·2πN at T = 3.5 and [1.11, 3]·2πN at T = 4; locator of alignment cells by phases
  τ log p mod 2π, p ≤ 13; certify only if a smaller cell appears. Not taken up in the block.

### 1.4 ROUND_017_C.md — first-cell coercivity of the archimedean form at length log 2
- Object: 𝒬[F] = (1/2π)∫m|F̂|² = (C_0 + ∫_L^∞K)‖F‖² + ½∫_0^L K(u)∫|F(x+u) − F(x)|² dx du, L = log 2,
  C_0 + ∫_L^∞K = −2.3784…; hyperplane H₀ = {∫_I F e^{−y/2} = 0}; four transported functionals f(0), f(λ), A, B.
- Lemma 2.1 (monotone symbol) PROVED; Lemma 2.2 (truncation of the symbol, 𝒬 ≥ M‖F‖² − ⟨GF, F⟩) PROVED; Lemma 2.3
  (polynomial compression with HS tail ≤ L(τ*/π)(M − C_0)(τ*L/2)^n/n!) PROVED; Lemma 2.4 (lower bound with constraints and
  leak) PROVED.
- Theorem 3.1 PROVED (computer-assisted, ball arithmetic, independent of T): on every window of length log 2,
  ∫F e^{−y/2} = 0 ⇒ (1/2π)∫m|F̂|² ≥ μ₀‖F‖², μ₀ = 0.069611…; true value in [0.0696, 0.0720].
- Corollary 3.2 PROVED: at length log 2 the complete form 2AB + (1/2π)∫m|F̂|² ≥ μ₀‖F‖² on {B(F) = 0}.
- Theorem 3.3 PROVED (assisted, pointwise in T): with the four transported functionals, μ₄(0.8) ≥ 0.527631,
  μ₄(1.0) ≥ 0.549417.
- §4(i) CONDITIONAL on the transport of 016_B §3.1: κ_T ≥ (λ/2)μ₄ on first-cell data.
- OPEN: transport defect; data on R ≥ 3 cells (multicell analogue of Lemma 2.4 with the gauge closure as W;
  the comb enters via 𝔇); first cell–rest cross terms.
- Falsifiers: everything holds under cΛ, a_P, Beurling, finite modifications ⇒ not a sign step.
- Next step: multicell version (R = 3, 4) of Lemma 2.4 with the transported gauge as W; quantify the transport
  defect. Not taken up in the block.

### 1.5 ROUND_018_A.md — transport defect on the measured vectors and complete form on R cells against ℓ_g
- Object: Q_R[F] = 𝒲[𝔇_RF] + 2A(𝔇_RF)B(𝔇_RF), 𝔇_RF = Σ_{N<R}N^{−1/2}F(· − log N)1_{I_R}, 𝒲 = 𝒬 − cΠ,
  Π[H] = Σ_{2≤m<R}2Λ(m)m^{−1/2}⟨τ_{log m}H, H⟩; V_R = four transported functionals on all F;
  κ_R(T) = inf_{V_R} Q_R/ℓ_g.
- NUMERICAL: in-band mass < 10⁻⁴; value defect always ≥ 0 (the first cell is a lower model); constraint defect
  δ = 0.03–0.16 (oscillating f(λ), A, B do not transport; f(0) does, cosine ≤ 0.007).
- Lemma 1.1 (transfer of a codimension-k bound to almost-constrained data, via the seminorm of 𝒬 + β) PROVED;
  positive only if δ < δ* = 0.0752.
- Prop. 3.1 (R = 2 in ℓ_g from 17C) PROVED; Lemma 3.2 (piecewise compression with exact 𝔇₃ and comb) PROVED; Lemma 3.3
  (three-cell bound against a finite gauge family with all leak terms) PROVED.
- Theorem 3.4 PROVED (assisted, T ∈ {0.8, 1.0}): Q₃[F] ≥ 0.70·ℓ_g[F] on V₃ (only m = 2 acts at length log 3).
- Theorem 4.1: (i) PROVED for idealized data R = 2, 3; (ii) CONDITIONAL for the high block (fails by δ);
  (iii) NUMERICAL negative: κ_R collapses for R ≥ 5 (T = 0.8), R ≥ 4 (T = 1.0): 0.11–0.17, 0.10, 10⁻⁴, 10⁻¹¹ (R = 5…8).
- NO-GO NUMERICAL (class: idealized R-cell problem with transported constraints, R ≳ 4): «wrong limit»;
  the band limitation (exponential type 2πλ of ℱf) is missing as a family of constraints, OPEN.
- Falsifier: Theorem 3.4 survives c = 0.9 and fails c = 1.1 (γ < 0); at R = 4 both c = 0.9 and 1.1 fail. First
  certified bound of the phase destroyed by cΛ, c = 1.1 — not claimed as a sign step (a_P with P = 3 raises it).
- Next step: add the band limitation (e.g. the high prolate span transported cell by cell) and remeasure κ_R,
  R = 5…8; run (b)–(d) on Theorem 3.4. Not taken up in the block (STATE_002 cites it as open).

### 1.6 ROUND_018_B.md — exact ledger of the survivor, tail Grams on the first rungs, c·log N test
- Object: 𝒲̂ = 𝒜_∞ − 𝒞 + 𝒯 on tails, 𝒯(F, G) = A(F)B(G) + B(F)A(G); pair (Ψ_*, Ψ_g), g admissible rungs in
  E(span{ψ_0 … ψ_20}) (and up to ψ_40).
- Lemma 1.1 PROVED: replacing log N by c log N in the tails is 𝒲̂^c = 𝒜_∞ − c𝒞 + 𝒯; it differs from a^c_T by the radical defect
  (1 − c)𝒞(Φ_f, ·) = O(1).
- Lemma 1.2 PROVED: (4.1) of 17A on span{Ef_*, Eg} ⟺ det of the 2×2 Gram of 𝒲̂ ≥ 0; rung part s_g = 1 − det/(ρa_T(G)).
- NUMERICAL: ρ = 𝒲̂[Ψ_*] = 8.23·10⁻¹² (T = 0.8), 2.17·10⁻²³ (T = 1); 𝒜_∞ : 𝒞 : 𝒯 ≈ 3.2 : 0.77 : 0; Schur part on
  E images 8–13 % (rungs 2–10 %); the rest (≈ 0.16–0.26 ρ, parity) does not live in E images of prolates ψ_0…ψ_40.
- NO-GO (class: «the rung piece (R) of the Schur inequality as the sign carrier — 2×2 positivity of the complete
  tail Gram on {Ψ_*, Ψ_g} with collapsed weight log N»): survives c ∈ [0, 3.5] (det vanishes at c ≈ 3.6–4.2);
  generic in the comb. Falsifier: cΛ (a) suffices; (b)–(d) not run.
- Recorded reading: all the c-sensitivity of (★) on E images is in the identity a_T(Ef) = 𝒲̂[Ψ_f] (radicality of
  Φ_f), none in the tail Gram (the window dies at |1 − c| ≈ 5·10⁻²², the tail tolerates |1 − c| ≈ 3).
- Observation 4.1 (m_eff against κ_w; frequency statement, blind to arithmetic).
- Next step: Schur coupling of the survivor with the parity piece (P) in E-preimage form (Möbius inversion
  on [e^{−T}, λ]) to decide whether (P) is also robust to the comb in tail form. Not taken up in the block.

### 1.7 ROUND_019_A.md — band limitation of the tail as a family of constraints on R-cell data
- Object: E_λ = {ℱf : f ∈ L²(−λ, λ) even}; 𝔅_R; projection P_λ with kernel k_λ(ξ, η) = sin2πλ(ξ−η)/(π(ξ−η)) +
  sin2πλ(ξ+η)/(π(ξ+η)); band defect β[F] = ‖(1 − P_λ)u‖²; concentration operator B_R = 1_{J_R}P_λ1_{J_R};
  families S_θ (spectral) and cone {β ≤ ε‖F‖²}; penalized quotient κ_R(μ) = inf_{V_R}(Q_R + μβ)/ℓ_g^{fam}.
- Prop. 1.1 PROVED + NO-GO (qualitative formulation): 𝔅_R ∩ V_R is dense in the form norm of Q_R; imposing «u is the
  restriction of a function of type 2πλ» does not change κ_R.
- Lemma 2.1 PROVED: β[u]^{1/2} ≤ ‖g‖_{L²(0,λ)} + ‖g‖_{L²(Rλ,∞)}.
- NUMERICAL: the collapse directions are almost band-limited (β/‖F‖² ≤ 10⁻⁷…10⁻¹³) but β/ℓ_g ≈ 0.8–1.7; with μ ≥ 10² the quotient
  returns to 0.45–0.71; with μ = 10⁶ ≥ 0.627 at R = 3…8; no uniformity in R is seen at fixed μ.
- Theorem 4.1 CONDITIONAL (H_band(μ, κ) and H_lim): complete tail form ≥ κℓ_g − μ‖ℱf‖²_{L²(0,λ)}; moves the deficit to the in-band
  mass (low block). H_band(10⁶, 0.62) NUMERICAL for R ≤ 8; H_lim ARGUED; transport fails (18A §1).
- §5.1 PROVED: every statement at fixed R is invariant under (c), (d) beyond cell R ⇒ a coercivity piece, never
  a sign step; the sign could only live in the uniformity in R.
- Certificates (arb): Q₃ ≥ 0.60ℓ_g with c₂ = 0 (a_3) at T = 0.8, 1.0; Q₃ ≥ 0.20ℓ_g with c₂ = 1.01 (T = 0.8). Threshold
  c₂* ≈ 1.016 (T = 0.8), 1.008 (T = 1.0): the true weight lies 0.8–1.6 % below the threshold.
- NUMERICAL: at R = 4 the falsifier (a) fails on both sides (c = 0.9 and 1.1), first bilateral failure of the phase.
- OPEN: (1) H_band certificate at R ≥ 4; (2) mechanism uniform in R (cell R+1 only creates almost-null directions with
  β/ℓ_g ≳ 1); (3) low-block bound (LB_μ).
- Result: PIVOT. Next step: measure the in-band side (LB_μ) for μ = 10², 10⁴, 10⁶ and certify H_band at R = 4
  (five pieces). Not taken up in the block (ROUND_019_B pivots to the tail reduction; STATE_002 lists it as open).

### 1.8 ROUND_019_B.md — tail reduction (i)+(ii): density of the E image; the comb-robust margin is an effect of the representative
- Object: admissible f (even, support [−λ, λ], C², f(0) = ℱf(0) = f(λ) = 0); gauge 𝒢_T = {φ admissible, support ⊂ [−1/λ, 1/λ]};
  𝒲̂^c = 𝒜_∞ − c𝒞 + 𝒯, 𝒜𝒫 = 𝒜_∞ + 𝒯; gauge radicals Φ_φ with Φ̃_φ(s) = ζ(s)Mφ(s).
- Prop. 1.1 PROVED (≈ CITED, lem:ext-mob): E(admissibles) ⊇ C_c^∞(I_T) ∩ P_T by Möbius inversion, fibre f_0 + 𝒢_T.
- Cor. 1.2 PROVED: (★) at T ⟺ 𝒲̂[Ψ_f] ≥ 0 for every admissible f with Ef ∈ P_T ∩ C_c^∞(I_T) — reformulation (REF-D), equal to
  eq:ext-starstar with κ = 0; prob:ext-L is the version with margin, strictly stronger.
- Theorem 2.1 PROVED: there exist φ_R ∈ 𝒢_T with B(Φ_φ) = 0 and 𝒜𝒫[Φ_{φ_R}] → m(0)ζ(½)²‖η‖² ≈ −11.457‖η‖² and others with
  → m(10)|ζ(½+10i)|²‖η‖² ≈ +1.114‖η‖² (without using zeros; only ζ(0) = −½ and two point values).
- Cor. 2.2 PROVED: for every admissible f and every c ≠ 1, inf_{φ∈𝒢_T}𝒲̂^c[Ψ_{f+φ}] = −∞ (Prop 1.5 of ROUND_001_B, now PROVED
  with both signs).
- Cor. 2.3 PROVED / NO-GO (class: comb-robust or weighted bounds «archimedean coercivity beats the overlapping
  comb» for (ii) on the whole class of admissible tails): 𝒜_∞ + 𝒯 − c𝒞 ≥ 0 on admissible tails is false for every
  c ≠ 1. The margin c ∈ [0, 3.5] of 18B is a property of the representative, not of the class.
- OPEN: (ii_s) 𝒲̂^c[Ψ_{f_G}] ≥ 0 for a fixed gauge section G ↦ f_G and c ∈ [0, c₁], c₁ > 1; ARGUED that it is prob:ext-L in
  another gauge (density of the gauge tails ARGUED).
- Falsifiers: (a) (i) fails; (b)–(d) (i) fails; analogue of Cor 2.2 for (d) ARGUED.
- Next step: fix the gauge by the representative minimizing the leak and measure 𝒲̂^c, c ∈ [0.5, 2], with gauge rank
  ≥ 30. Not taken up in the block (ROUND_020_A changes object).

### 1.9 ROUND_020_A.md — tail inequality with fixed gauge: representatives, null quadric of the comb, canonical sections
- Object: V_T = {Ψ_f : f admissible, Ef ∈ P_T}, R_T = {Φ_φ : φ ∈ 𝒢_T}; fibres Ψ_f + R_T; quadric {𝒞 = 0}; Rep(I) =
  representatives with 𝒲̂^c ≥ 0 for c ∈ I; Λ-free sections (none, ell = min ℓ, f2 = min ∫_0^{1/λ}f², tail = min ‖Ψ‖²).
- Lemma 1.1 PROVED: 𝒞[Ψ + Φ] = 𝒞[Ψ] + 2𝒜𝒫(Ψ, Φ) + 𝒜𝒫[Φ]. Lemma 1.2 PROVED: every fibre meets {𝒞 = 0}.
- Theorem 1.3 PROVED: for isolated c ≠ 1 there is always a good representative; for every interval I ∋ 1, Rep(I) ≠ ∅ ⟺ 𝒲̂ ≥ 0.
- Cor. 1.4 PROVED: (★) ⟺ 𝒜𝒫 ≥ 0 on V_T ∩ {𝒞 = 0} (reformulation invariant under scaling of the weight; Λ-specific only via (A)).
- Theorem 1.5 PROVED on finite-dimensional sections (ARGUED in general; Finsler S-lemma CITED): the multiplier is
  forced to μ = 1 by the gauge radicals of both signs.
- NO-GO PROVED (class: existential version «choose the representative with comb-robust positivity» = (★)).
- NUMERICAL: canonical sections without uniform margin: ell δ = 0.027 → 0.0035; f2 0.73 → 0.24; tail 1.29 → 0.37 under refinement.
  Mechanism ARGUED: L²-type minimizers are not attained if the gauge is dense.
- OPEN: (B_δ, s) 𝒜𝒫[Ψ] − c𝒞[Ψ] ≥ 0 on Ran s, c ∈ [1 − δ, 1 + δ], s a Λ-free linear section; ARGUED not weaker than prob:ext-L.
- Falsifiers: (A) fails for (a), (b), (d); (c) without Poisson. (B) by itself is robust to the comb and carries no sign.
- Result: NO-GO (existential) + PIVOT (sections). Next step: w = 0.025, 0.018 and fit δ(w); if δ → 0 record the
  closure of the fixed-gauge tail line; if it stabilizes, H¹-type tail norm. Not taken up in the block.

### 1.10 ROUND_021_A.md — positivity window J_R(T) of the complete R-cell form
- Object: Q_R^{(w)}[F] = 𝒜[𝔇_RF] − Π_w[𝔇_RF] + 2A(𝔇_RF)B(𝔇_RF), Π_w = Σ w_nΠ_n; J_R = {c : Q_R^{(c·1)} ≥ 0 on V_R}; windows
  per prime and per atom; truncated Dirichlet algebra Φ_R(α) = Σ_{n<R}α_n n^{−1/2}τ^I_{log n}.
- Lemma 1.1 PROVED: each window is a closed interval. §2.1 PROVED: the Galerkin windows are outer bounds.
- §3.1 PROVED: Φ_R is a homomorphism (Dirichlet convolution → compressed shifts), kernel {α_n = 0, n < R};
  [M_x, Φ_R(α)] = Φ_R(α·log).
- Prop. 3.2 PROVED: P_w𝔇_R = [M_x, 𝔇_R] ⟺ w ≡ 1 on prime powers < R; Q_R^{(c)} = Q₀ − c𝒦_R,
  𝒦_R[F] = 2⟨𝔇_RF, [M_x, 𝔇_R]F⟩ = 2Σ_{m,n<R}(log n)(mn)^{−1/2}⟨τ_{log m}F, τ_{log n}F⟩; Λ disappears.
- Lemma 3.3 PROVED (sandwich): λ₀/‖𝒦‖ ≤ c_+ − 1 ≤ λ₀/K₀ and analogues for c_−.
- NUMERICAL: J_R → {1} bilaterally and superexponentially (δ_+ = 1.7·10⁻², 5·10⁻⁵, 6.7·10⁻⁸, 1.3·10⁻¹¹, 7.4·10⁻¹⁶,
  6.9·10⁻¹⁹, R = 3…8); a_P fails by O(1) from R = 4; per-prime windows shrink likewise.
- NO-GO (class: positivity windows in the comb weight on idealized R-cell data, uniform or per prime):
  the shrinking is equivalent to λ₀(R) → 0 (Lemma 3.3), with no lower bound; the mechanism (Prop. 3.2) survives the
  falsifier (c) Beurling (structural PROVED, numerical ARGUED). NO-GO NUMERICAL of κ_R uniform in R (already in P211-18A).
- Unsigned remainder: Q₀ − 𝒦_R ≥ 0 on V_R (Λ-free), floor ~ exp(−2.9R log R) (fit).
- Next step: almost-null direction of Q₀ − 𝒦_R and test whether it is the 𝔇_R-preimage (𝔇_R^{−1} = Φ_R(μ)) of the floor of 𝒜 − Π
  on the window. Not taken up in the block (ROUND_021_B studies the native window, not that comparison).

### 1.11 ROUND_021_B.md — band margins on alignment cells of small primes, T = 3.5–4.5
- Object: band margin μ_η(τ) = m(τ) − λ_max(A_τ^{(η)}); locators h₄(τ) = Σ_{p∈{2,3,5,7}}(1 − cos(τ log p)),
  δ(τ) = max_p‖τ log p/2π‖, and g_T (flat-window tone); r = τ/2πN.
- All NUMERICAL (counterexample watch; there is no sign step nor applicable falsifier).
- Results: no negative margin nor < 0.02; minimum found 0.0631 (T = 4.2, τ = 30775.05574, r = 1.10); upper
  bounds per T: 0.114 (3.0), ≤ 0.134 (3.25), ≤ 0.078 (3.5), ≤ 0.106 (3.75), ≤ 0.084 (4.0), ≤ 0.071 (4.1), ≤ 0.063
  (4.2), ≤ 0.084 (4.25), ≤ 0.083 (4.5).
- Correction to ROUND_017_B: τ = 7713.88 is not a simultaneous alignment (p = 3 at a quarter cycle); the minimum at T = 3.25 is
  anti-aligned. Alignment is neither necessary nor sufficient; the position r ≈ 1.1 predicts the depth; in a fixed cell the margin
  decreases monotonically in T.
- Failures: locators h₄ and g_T do not locate minima; polishing window ±0.1 too narrow in some cells.
- Result: PIVOT. Next step: complete Lanczos sweep of the strip r ∈ [1.1, 1.3] at T = 4.0, 4.25, 4.5 and
  tracking in T. Not taken up in the block.

### 1.12 ROUND_022_A.md — the R-cell form on generalized integer systems
- Object: system 𝒩 (multiplicative closure of generators g > 1), Λ_𝒩 by Σ_{de=x}Λ_𝒩(d) = log x;
  𝔇^𝒩 = Σ_{x∈𝒩,x<R}x^{−1/2}τ^I_{log x}, Π^𝒩, Q^𝒩 = Q₀^𝒩 − 𝒦_R^𝒩; λ₀(R; 𝒩); summation set S of the A/B constraints.
- Lemma 3.1 PROVED: the homomorphism Φ_R^𝒩 and [M_x, Φ^𝒩(α)] = Φ^𝒩(α log) hold for every multiplicatively closed system.
- Prop. 3.2 PROVED (perturbation CITED Rellich–Kato): ∂_{η_i}𝔇 = −G_i𝔇(½ + ∂), ∂_{η_i}P = G_i − η_iG_i^{(1)}(½ + ∂);
  exponent direction ∂_t𝔇 = −[M_x, 𝔇](½ + ∂) = −P𝔇(½ + ∂), ∂_tP = P − Φ(Λ log)(½ + ∂); Hellmann–Feynman slopes.
- Prop. 3.3 PROVED (structural part: ℕ^{1+t} ≅ ℕ as ordered monoids, Λ scaled by 1 + t; ℕ the unique additively
  closed one) + NUMERICAL (sign): positive for t ∈ [−10⁻³, 0], negative for t > 0 (10⁻⁶…10⁻³); the R-cell sign is not
  a monoid invariant; ℕ at the tip of a thin wedge along ℕ^{1−ε}.
- NUMERICAL: generic perturbations (2 → 2 ± δ, 3 → 3 ± δ, extra prime 2.5, free system on {2, 3}, √p, ℕ ∪ √2ℕ)
  negative from the first R at which they differ; the summation set of the constraints does not influence the sign.
- Falsifier (c): R-cell positivity SURVIVES on the Beurling ray ℕ^{1−ε} for ε ≤ ε₀(R) ≈ 0.1, 0.05, 0.02,
  0.005 (R = 5…8); no statement at fixed R is a sign step; a mechanism must produce ε₀(R) → 0.
- OPEN: sign of ∂_tQ on the almost-null cluster (δ_tQ[u_k] < 0, NUMERICAL, no proof).
- Failures: «perturbed negative ⇒ ℕ-specific sign» (false on ℕ^{1−ε}); «integer spacing via Poisson in the
  constraints is responsible» (no effect).
- Next step: prove or refute ∂_tQ[u] < 0 on the almost-null vectors; measure ε₀(R), R = 9, 10; isolate near-coincidences
  with a system preserving the log-gaps up to a size and breaking a relation m = kn. Partially taken up: ROUND_022_B
  studies ∂_tQ on the almost-null cluster.

### 1.13 ROUND_022_B.md — complete Lanczos sweep of the strip r ∈ [1.1, 1.3], T ≥ 4
- Object: the band margin μ_⅛(τ) of 017_B/021_B; grid τ ∈ w₀ + δℤ, δ = h/m, h = π/2T, with S(w), D(w) tabulated
  (tool strip_scan.py).
- All NUMERICAL; nothing proved. Coverage: T = 4.0 r ∈ [1.100, 1.158] (min 0.07979, τ = 20948.73412); T = 4.5 only
  r ∈ [1.1000, 1.1008] (0.1377); T = 5.0 only r ∈ [1.10000, 1.10005] (0.1226 on the grid, unpolished).
- Tracking of five cells in T: they decrease monotonically and almost linearly in log r (convex, flattening at the lower
  end); values at r = 1.1: 0.0631, 0.0713, 0.0773, 0.0789, 0.0849; linear extrapolation of the zero at r ≈ 0.29–0.39 (outside
  the window). Minimum seen 0.0589 at r = 0.997 (outside the window).
- No negative value, none < 0.02; stopping rule not triggered. The pure warm start fails again.
- Failure: complete sweep infeasible due to eigensolver cost (K = 6.6·10³ … 6·10⁴).
- Next step: (a) finish T = 4.0 on r ∈ (1.158, 1.3] and stop; or (b) certified locator via a Lipschitz bound of
  λ_max(A_τ) in τ (dλ/dτ = ⟨∂_τA x, x⟩). Not taken up in the block.

### 1.14 ROUND_023_A.md — the exponent ray ℕ^{1+t}: edges of the positive segment and first variation at t = 0
- Object: family ℕ^{1+t}, variants powfix (fixed cell set), sig (weights n^{−(1+t)/2}), pos (positions
  (1+t)log n), lam (comb (1+t)Λ); D = ½ + ∂; U_s(F)(y) = s^{1/2}F(sy).
- Lemma 2.1 PROVED: Φ(Λ·log) = [M, P] = 𝔇⁻¹[M,[M,𝔇]] − P², 𝔇⁻¹ = Φ(μ) (Selberg identity Λ·log + Λ∗Λ = μ∗log² in
  operator form, CITED).
- Prop. 2.2 PROVED: ∂_t = δ_lam + δ_sig + δ_pos; δ_lamλ_k = −𝒦_R[u_k] (Hellmann–Feynman CITED).
- Prop. 2.3 PROVED (dilation image): ℕ^{1+t} on window log R is unitarily the R^{1/s}-cell form of ℕ with comb
  ×s, weight exponent s/2, archimedean data and constraints dilated.
- Prop. 2.4 PROVED (virial identity): δ_posλ_k = −ℓ∂_ℓλ_k + δ_∞λ_k + δ_Cλ_k; δ_∞ is the form of (uk_∞(u))′ on 𝔇u, indefinite.
- Lemma 4.1 PROVED (first-order edge bounds) and 2×2 coupling formula of the cluster (PROVED, elementary).
- NUMERICAL: λ₀(9) = 1.33·10⁻²², λ₀(10) = 1.06·10⁻²⁴ (T = 0.8); almost-null slopes in [−3.4, −0.9], ≈ 90 % δ_pos; right
  edge t₊ ≈ 1.05λ₀; left edge |t₋| ≈ λ₀^{0.10…0.13}; the entering prime cell extends the segment.
- ARGUED: the uniqueness of ℕ on the ray = [positivity on ℕ] + [generic corollary of the collapse]; it is not a characterization that
  isolates the sum; ℕ is the point of minimal margin of the segment: there is no variational lever; even proved, ∂_tλ₀ < 0 does not give
  λ₀(0) ≥ 0. Declared: «the exponent ray should not be continued as a route to (★)».
- OPEN: sign of ∂_tQ on the cluster; whether ∂_tλ₀ → −1 is exact (structural curiosity).
- Falsifiers: (a) the same uniqueness at c = 1; (b), (d) fail O(1); (c) ℕ^{1−ε} finally rejected by the generic
  mechanism.
- Result: PIVOT. Next step: evaluate δ_∞, δ_C, ℓ∂_ℓ at u₀ for R = 4…10 (curiosity only). Not taken up.

### 1.15 ROUND_024_A.md — three sign-carrying designs on the bandwidth axis; contact entry lemma
- Object: continuous axis N, contacts entering at T_n = ½ log n (Λ(n) ≠ 0); design A (entry ledger), design B
  (Chebyshev floor relation Σ ε_k⌊y/k⌋ ∈ [0, 1], ε = (1, −1, −1, −1, 1) at k = 1, 2, 3, 5, 30, at the exact truncation
  log n < 2T), design C (prolate extremality with index-8 constraint count).
- Prop. 2.1 PROVED / NO-GO (class: finitely many strict floor relations, any precision): the set of weights satisfying them
  with slack is open in c around Λ on every bounded range; without slack it is R10 (Λ ∗ 1 = log).
- Lemma 4.1 PROVED: |c_F(2T − δ)| ≤ ‖F‖_{L²(T−δ,T)}‖F‖_{L²(−T,−T+δ)}. Lemma 4.2 PROVED: c_F(2T − δ) = δF(T⁻)conj F(−T⁺) + o(δ)
  (O(δ^{3/2}) in H¹).
- Prop. 4.3 PROVED: at an entry, −v_n Re c_F(log n) = −2hv_nF(T⁻)² + o(h) < 0 for real even F; > 0 for real odd F.
- Cor. 4.4: (i) PROVED |a_T − a_T^{∖n}| ≤ v_n × edge-strip product; (ii) CONDITIONAL on (R_edge) (simple floor,
  continuity at the edge): jump of the right derivative of λ_A at T_n equal to −2v_nF*(T_n)².
- NO-GO (class: positivity propagated through contact entries along N): entry law of definite sign
  and generic in the weight (survives (a) c > 0, (b), (c), (d)); every propagation reduces to the rate bound (EB_C)
  of P211-8C, OPEN (reformulation class).
- Design C: retry of L′/L′♯, dies in the gauge directions (ARGUED, not pursued).
- ARGUED: by the Slepian identity the entry jump ≈ (2v_nc/(Tκ₈))·λ_A: a jump in the logarithmic derivative, not an
  additive impulse; explains the invisibility of contacts in log λ_A.
- Next step: prove (R_edge) and test the entry law numerically at n = 7, 8, 9 (logarithmic derivatives at T_n ± 10⁻⁴) and
  record the residue of (EB_C) as the only piece on the bandwidth axis. Not taken up in the block.

### 1.16 ROUND_025_B.md — the prime-free statement as a kernel on a function: coprime ratio, local factors, Schur product test
- Object: 𝒬[F] = 𝒜𝒫[Ψ] − 𝒞[Ψ] = ∫∫F(y)F(y′)K_ℕ(y, y′), K_ℕ = Σ_{N,N′}(NN′)^{−1/2}{k(y − y′ + log(N/N′))1[N < ξ/λ]1[N′ < ξ′/λ]
  − log(NN′)δ(y − y′ + log(N/N′))1[N < ξ/λ]} + α⊗β + β⊗α, α = e^{y/2}⌊ξ/λ⌋, β = e^{−y/2}H(⌊ξ/λ⌋), ξ = e^{−y}.
- Theorem 1.1 PROVED (under the summability hypothesis (H)): exact prime-free kernel. Theorem 2.1 PROVED (= Thm E.1′ of phase 199
  in the tail variable): decomposition by coprime ratio with weights (ab)^{−1/2}H(min(M_a, M_b)) and
  (ab)^{−1/2}[2L(M) + log(ab)H(M)], M_a(y) = ⌊ξ/(λa)⌋.
- Prop. 3.1 PROVED: w(a/b) = (ab)^{−1/2} = Π_p p^{−|v_p|/2} is positive definite on ℚ^×_{>0} (product of Poisson kernels);
  D_σ(τ) = |ζ(½ + σ + iτ)|²/ζ(1 + 2σ) > 0, σ > ½.
- Theorem 3.2 PROVED (σ > ½; limit CITED): in the dilation model without cutoff the cofactor is m + 2Re(ζ′/ζ)(½ + σ + iτ),
  which at σ = 0 vanishes identically (symbol identity, phase 199 Thm F.1).
- NO-GO PROVED (class: Schur/Hadamard products of a multiplicative PD local weight on ℚ^×_{>0} with an archimedean kernel
  independent of q): with m it is not ⪰ 0; with m + 2Re ζ′/ζ it is zero; the sign lives in the cutoff/polar part, which is not of product type.
- NUMERICAL: each coprime class indefinite; every truncation by height or by prime support negative by O(1); positivity
  appears only with the complete set of classes and the polar term is essential.
- Unsigned remainder: K_cut := Σ_{(a,b)=1}(ab)^{−1/2}{k(z)[H(min M) − regularized value] − δ(z)[2(L(M) − ½log²M − γ₁) +
  log(ab)(H(M) − log M − γ)]} + polar (sawtooth form F.2 in the tail variable).
- Next step: attack K_cut + polar directly (do not retry «the sawtooth decides the sign in the transition region»,
  F.2/J.3). Not taken up in the block.

### 1.17 ROUND_026_A.md — computer-assisted lower certificate for λ_A beyond ½log5
- Object: certificate of P47 prop:lowercert (frequency-truncated symbol, Legendre block, Haynsworth inertia),
  with floor s_∞ certified by an interval sweep of s_T on [τ_N, τ_B], g = (s_∞ − s_T)1_{|τ|<τ_N}, 𝒢 = Q_Tg(D)Q_T,
  a_T(F) ≥ s_∞‖F‖² − ⟨𝒢F, F⟩, 0 ≤ 𝒢_± ≤ ω_±S_c, c = Tτ_N; positivity by Gershgorin of XSXᵀ with X ≈ L⁻¹ exact.
- §1.1–1.4 PROVED (lower form, Bernstein-ellipse quadrature bounds, Bessel enclosures, positivity criterion).
- §1.5 NUMERICAL: reproduces thm:log5A (even 2.5·10⁻¹², odd 3.0·10⁻¹⁰).
- Theorem 26A.1 PROVED (assisted): λ_A(1) ≥ 1.0·10⁻²³, hence λ_A(T) ≥ 1.0·10⁻²³ on 0 < T ≤ 1 (contacts {2,3,4,5,7}).
- Theorem 26A.2 PROVED (assisted): λ_A(207/200) ≥ 2·10⁻²⁶, hence on 0 < T ≤ 1.035 (last window before contact 8).
- §3.1 PROVED (two forced sizes): τ_N ≥ τ_0(T; s_∞) and dim E ≥ #{λ_j(S_c) > ½} ≈ (2/π)Tτ_0 (Ky Fan, Landau–Widom CITED).
- §3.3 NO-GO for this machine, not in principle (NUMERICAL): at ½log15 + 0.01 one needs dim E ≥ 1.1·10⁵; τ_0 grows doubly
  exponentially in T. What would change the class: a bound of the complement without a positive floor of the symbol at every frequency
  beyond τ_N (average of s_T over windows of width ≈ π/T; Q12 of STATE_002), not attempted.
- No falsifiers (it is a window certificate). No explicit «next step» at the end. Within the cited range.

### 1.18 ROUND_027_A.md — is the comb weight vector the global maximizer of μ_T?
- Object: μ_T(v) = floor of Arch − Σ_n v_nΠ_n on P_T, v ∈ ℝ^{N_T}, concave (P47 lem:degen), μ_T(v_T(Λ)) = λ_A(T); hypotheses
  (A) v_T(Λ) = argmax μ_T and (B) there exists an explicit v̂ with μ_T(v̂) ≥ 0.
- NUMERICAL: simple floor at T = 0.8, 1.0, 1.2, gradient g = (c_{F*}(log n))_n ≠ 0, hence 0 ∉ ∂μ_T(v_T(Λ));
  M_{0.8} = 0.04735, maximizer v* = (0.0843, −0.858, −1.820)·v_T(Λ); M_{1.0} = 0.02968 with sixfold floor.
- NO-GO NUMERICAL (with mechanism PROVED by lem:degen; class: global concave maximization of the floor over weight vectors
  at the positions log 𝒩_T). μ_T does not depend on the comb; v* does not separate the comb from the falsifiers.
- Nothing new proved. Next step: none; a restricted variant (v ≥ 0, or a set separating falsifiers)
  would need its own reason.

### 1.19 SQUARE_COMPLETENESS_AUDIT.md — audit of partial completeness on perfect powers
- Object: literal audit of SQUARE_COMPLETENESS_OBSTRUCTION §§1–11 (family F_p = (1 + c_pz)/(1 − z²), 0 ≤ c_p ≤ 1;
  fixed exponent F_m = ζ(1 − 2^{−s})/(1 − 2^{−ms}); simultaneous member with local factor at 2 (1 − z/2 + z²/2)/(1 − z);
  repair of the residue with P_δ = 1 + δz − δz²).
- Approves (without new execution): N(n²) = 1, logarithmic coefficients ≥ 0, primitive witness of ROUND_007_C with
  W_{a3}/‖F‖² ≤ −0.50528; W_new = W_{a3} − 2log2·C_F(log 4) < 0; exact residue 1 within the ansatz forces c_p = 1;
  exponent m ≥ 3 gives W_m = W_{a3} < 0; simultaneous member with W_new < −0.00528‖F‖²; integer identification §10 correct;
  repair of the residue §11 correct (N(2) = ½ not an integer, N(p) > 1 at compensating primes).
- Recorded scope: falsifier of the DECLARED class (completeness on squares / on all powers with the declared
  requirements), not a global exclusion of every use of squares; not a sign proof for Λ. The endpoint 2 → 4 already appeared in
  R163_102 Cor F / R163_191.
- No next step; «no pending audits remain».

### 1.20 SQUARE_COMPLETENESS_OBSTRUCTION.md — completeness on squares and perfect powers: sufficiency falsifiers
- Object: primitive form with fixed archimedean floor with weights v_n = 2ℓ(n)/√n (ROUND_007_C/P47); Euler families
  F_p(z) = (1 + c_pz)/(1 − z²) (§2), F_square = ζ(s)/(1 + 2^{−s}) (§3), F_m = ζ(s)(1 − 2^{−s})/(1 − 2^{−ms}) (§8),
  F_all = ζ(s)[1 − 2^{−s}/2 + 2^{−2s}/2] (§9), F_norm = ζ(s)R(s) with high factors (1 + δz − δz²)/(1 − z) (§11).
- §2 PROVED: N_c(n²) = 1 for all n, 0 ≤ N_c ≤ 1, ℓ_c(p^k)/log p = c_p^k (k odd), 2 − c_p^k (k even), ℓ_c ≥ 0.
- §5 PROVED (analytic): C_F(log 4) > 0 on the certified witness of ROUND_007_C (T₀ = ½log5 + 10⁻⁴, x > 1).
- §6 PROVED (transfer of the certificate CERT007 ≤ −0.50528): a^{ℓ_square}_{T₀}(F) < −0.50528‖F‖²; falsifier of the sufficiency
  of {ℓ ≥ 0, support on prime powers, N multiplicative, 0 ≤ N ≤ 1, N(n²) = 1, simple pole with positive residue not
  imposed to be 1}; negative for every T ≥ T₀.
- §7 PROVED: within THIS ansatz, exact residue 1 forces c_p = 1 for all p (identification, not sign).
- §8 PROVED: for each fixed m ≥ 2, N(n^m) = 1 is not enough (m ≥ 3: W_m = W_{a3} ≤ −0.50528‖F‖²; residue 1/[2(1 − 2^{−m})]).
- §9 PROVED: simultaneous ALL-POWERS with N(2) = ½ not an integer, ℓ ≥ 0 (roots r_± = (1 ± i√7)/4): a < −0.00528‖F‖²; residue 7/8.
- §10 PROVED (identification, not NO-GO): N multiplicative, N(n^m) = 1 ∀m ≥ 2, N(p) integer ≥ 0, ℓ ≥ 0 ⇒ N ≡ 1, ℓ = Λ.
- §11 PROVED: exact residue 1, count x + O(1), N ≥ 0 multiplicative bounded by C, ALL-POWERS, ℓ ≥ 0 are not enough either
  (compensating primes ≥ 7 invisible to the witness; N(p) > 1 at them, N(2) = ½).
- NO-GO (declared class: partial completeness on squares / fixed powers / all powers, with the written
  positive hypotheses, without integrality nor N ≤ 1 nor functional equation): explicit falsifiers. Does not exclude every use of
  partial completeness; does not touch Λ.
- Implicit reopening: an additional hypothesis excluding ℓ_square/ℓ_all/ℓ_norm (integrality, N ≤ 1, functional
  compatibility) specified and proved separately; with integrality + ALL-POWERS + ℓ ≥ 0 the datum is identified (§10).
- No «next step» (closing memo).

### 1.21 STATE_001.md — status of the phase after rounds 1–3 (with round-4 annex)
- Object: synthesis. Reduced forms of (★): (L2) S_{T,k} ⪰ 0; (S) 𝔸_M = Arch_M − Div_M − Near_M ⪰ 0; (B) B positive definite
  and smoothed Chebyshev form; 2×2 band |B(d)| ≤ B(0) (necessary); (L2′) with shift α and gauge c (dim 11 at
  ½log5 + ε, 41 at T = 1, NUMERICAL); Candidate-I split (★) ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; cone 𝒦_T; Schur suppression t*_M = 0.
- PROVED (table P1–P35, with review verdicts): P1 m = 2θ′ and sign of the comb as a truncation of +2Re ζ′/ζ; P2–P5
  (Lemma 1, Thm 1 of ROUND_001_A); P7 radical lemma and zero-free half-line identity (σ₂ ∈ (−½, 0)); P8 defect
  𝒲^w = 𝒲 + 𝒫_{Λ−w}; P9 no common radical vector for c ≠ 1; P10 (last step ARGUED); P11 cell positivity for w ≤ Λ;
  P12; P14–P15 (L2′); P16 the sign is not a function of the block samples; P17 germ of B at 0 comb-free; P18 Lemma P;
  P19 Thm F (coercivity floor); P20 Prop S/L; P21 Prop M (deep sample ⇒ near-coincidence n′^{q_n} ≈ n^{q_{n′}});
  P22–P23 coherent part of the comb monotone and PSD; P24 Thm 1 of ROUND_002_D; P25; P26; P28 (ROUND_003_B, reduced
  scope); P32–P35 (ROUND_003_A, unreviewed); P29 arithmetic squares on (½log2, ½log3) ⟺ λ^{∞,P}_min(T) ≥ √2log2;
  P30; P31. CONDITIONAL: P6, P13, P27; DOWNGRADES recorded (Q_M ARGUED, Prop 2.3 ARGUED, etc.).
- NO-GO (§3): C1 smooth family s_w (ARGUED); cell positivity as a complete step; fused reading (ARGUED); slice edges
  (empty residue); C5 moment-only criteria (germ of B) PROVED; C3 floor-only Schur inequalities (NUMERICAL);
  C2 dependence of the comb in the prolate sector (ARGUED, asymptotic); C9 two concrete Schur prescriptions (split,
  Div/Near) PROVED with reduced scope; C10 dominated by C8; Candidate I as a universal step PIVOT.
- Round-4 annex: NO-GO (Prop B PROVED): no condition on a fixed Λ-free finite subspace with positive margin can
  carry the sign (it survives small changes and cΛ); the next object must have dimension growing with T.
- Corrections to P47 (12 items; apply only at closure): eq:coer-sandwich, normalization of F_0, prop:H, §ext-constraints,
  rem:directbound, thm:nyq-schur(ii), labels, thm:ext-half, sign of the comb, range of σ₂, term K3, reading of ROUND_001_C §4.
- Open (§5.5): (a) Θ_T(Λ) ≥ 0 (Lévy form ≥ 0 on the null quadric of the comb); (b) 1 ∈ J_T; (c) mechanism producing
  the almost-degenerate pair; (P1) second even eigenvalue almost null; (P2) Π indefinite on the even pair.
- §6 candidates with a first lemma (see §D): C11/C8, C3, exterior form at low Mellin frequency, C6, C4, C7, P6.
- Verdict: nothing changes the status of (★).

### 1.22 STATE_002.md — status of the phase after rounds 5–20 (verdicts of REVIEW_004–010)
- Object: synthesis. Reformulations R1–R16: E_T (Nyquist block + comb responses) R1 PROVED; sign budget
  a_T = σ_T‖F‖² + κ − ℛ (σ_T > 0 only for T < 0.0520) R2; (L2′) with two parameters R3; band reduction (HR)(a) R4
  (necessity PROVED); closed matrix-free form R5; Weyl counts R6; margin and index law R7; index-8 prolate law
  R8; Fourier selection rule R9; radical/half-line identity R10 («the only Λ-specific input of every route»);
  tail form R11; tail reduction R12; null formulation of the comb R13; split (A) + (B_δ, s) R14; Neumann/Schur
  R15 (CONDITIONAL on (H₋)); Schur functional of the survivor R16.
- PROVED Q1–Q27 (with scope): Q1 certified falsifiers (a_3 and Beurling 3 → 3.2 negative at ½log5 + 10⁻⁴ and every larger
  T; 1.1Λ negative at T = 1); Q2 upper bound λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πN} (N ≥ 1.6·10⁶, given thm:ext-half);
  Q3 first cell; Q4 three cells; Q5–Q27 according to the table (Q7, Q8 CONDITIONAL; Q11 value lowered; Q13 reformulation).
- NO-GO N1–N26 (class and status): N1 Krylov at bounded degree; N2 floor-only Schur on enlargements; N3 identity mechanisms on
  E_T (Selberg, local Euler factors, Lévy kernel) PROVED; N4 ground-state transformation (ARGUED); N5 homogeneous families
  of words in {M, Π_P} PROVED; N6 Weyl bounds from Arch − θ; N7 budgets by minimizer; N8 finite-degree
  Neumann; N9 Grönwall in T (𝒦_H); N10 PEψ₀ alone; N11 class 𝒦_S of comb mass; N12 Logvinenko–Sereda/Kovrijkine;
  N13 two- and three-block Schur assemblies; N14 trivial fixed-profile bound, short packets, MV + Sobolev for (U);
  N15 Vaughan/Heath-Brown + process B (class 𝒱); N16 symbol on the index axis in D units; N17–N26 (rounds 18–24, see
  entries 1.5–1.15).
- NUMERICAL: table of λ_A (Galerkin) from ½log3 to 1.5; law −ln λ_A ≈ c₁e^{2T} + c₂T + c₃, c₁ → 4π from above; κ₈ law; packet
  margins; anomaly at T = 1.5 resolved; three cells at 0.8–1.6 % of the threshold; ledger of the survivor.
- Map of the obstacle (§5): every route ends in (a) a statement generic in the comb or (b) a reformulation whose
  Λ-specific content is exactly R10, always used as an identity, never as an inequality.
- Open targets in order (see §C/§D): (B_δ, s); uniformity in R with quantitative band; (HB_η) uniform in T;
  (ii_s); (H₋) and (EB_C); lower half of prob:ext-L and (HR) in ℓ_g.
- Corrections to P47 added 8–13. Verdict: status of (★) unchanged.

### 1.23 STATEMENT_001.md — record statement of the phase
- Object: a_T(F) = (1/2π)∫s_T|F̂|², s_T = m − Σ_{log n<2T}v_n cos(τ log n), P_T = {A(F) = B(F) = 0}, λ_A(T); Lévy form
  K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)), C_0 = ψ(¼) − log π = −5.3721834…; unique profile F_0 = (¼ − ∂²)G_0 and function B(d);
  matrices 𝔸_M = [B(log m − log k)] = Arch_M − Div_M − Near_M (2T_0 < log 2).
- PROVED (cited from P47): Lévy form (lem:K, thm:A); continuity and nonincreasing monotonicity of λ_A; thm:oneprofile ((★) ⟺ B
  positive definite); prop:AM ((★) ⟺ 𝔸_M ⪰ 0 ∀M); 2×2 band |B(d)| ≤ B(0) necessary (Bochner). CITED: smoothed Chebyshev
  fluctuation form B(log x) = −x^{−1/2}ΣΛ(n)φ(n/x) − Σ_{j≥1}γ_jx^{−(2j+½)}, ∫φ = ∫φ/y = 0. NUMERICAL: B(0) = 0.01492,
  |B(d)| ≤ 0.0122 on 0 < d ≤ 13 (a = 0.15, b = 1).
- Declared status: PROVED (certificate) T ≤ ½log5; CITED T ≤ ½log15 and T ≤ 17/16 (preprint); OPEN beyond.
- §4 requirements (i)–(vi) of the sign step and open clause (an object coupling (Λ(n))_{n<N} with the functional equation by
  a route different from the common factor ζ(½ + iτ)); §5 allowed internal reformulations ((L2), (N), (S), (B), Kreĭn, leak).
- Not a construction memo: no new theorems, no NO-GO, no next step.

### 1.24 SURVEY_001.md — audit of Papers 01–42 as a toolbox for a_T
- Object: reading of 42 earlier papers looking for reusable techniques on a_T, S_{T,k} and the Toeplitz matrix
  [Ξ_{F0}(log(m/k))] of (S). Labels per paper (PROVED/CITED/CONDITIONAL/NUMERICAL/ARGUED of each source).
- Recorded discards (closed families of the index, do not propose): Papers 01–06, 08, 10, 11, 13, 14, 16 (spectral side,
  excluded), 17, 18, 19 (conditional on a hypothesis without analogue), 21, 23, 25, 27, 28, 30, 31, 32, 33, 34, 37, 40, 41, 42; Paper 12
  as a lever (NO-GO: no arithmetic margin from band limitation alone).
- Top 10 never applied to the finite object (see §D): (1) P26 Weil–Toeplitz/corona algebra and symbol σ(Q); (2) P38
  coercivity of adjacent windows |H_L|² + |H_{L+1}|² ≥ ½|z|^{2L}; (3) P39 exact transport defect (two rank-one
  channels + double operator integral); (4) P07 thm:trunc η(X) ≤ A exp(−α(log X)²); (5) P22 Carleman determinacy;
  (6) P15 thm:crit (eventual positivity → uniform); (7) P24 dominance measure (analogy); (8) P09 thm:concave
  (reduction to extreme points of coefficient boxes); (9) P35 Bakry–Émery curvature bound of the prime part after
  Doob conjugation; (10) P36 thm:mirror-criterion and nodes H1–H5 (one-round cross-check).
- No theorem of its own; no falsifiers; no next step apart from the list.

### 1.25 TOOL_001_GALERKIN_MP.md — multiprecision Galerkin engine for a_T
- Object: basis of N Dirichlet sines on (−T, T), Arch via the Lévy form (three moments of K on [0, 2T] + closed tail),
  Π (true or supplied comb), A, B, projector onto P_T, floors by parity, Θ_T = max_μ λ_min(Arch − μΠ) and c*.
- All NUMERICAL (upper bounds of λ_A). Validation: ½log3 1.008·10⁻³; log 2 1.1137·10⁻⁷; ½log5 + 10⁻³ 3.088·10⁻¹²;
  0.9 6.03·10⁻¹⁷ (the double-precision value 4.5·10⁻¹⁵ was rounding). T = 1.0: 1.74·10⁻²³ (N = 120); T = 1.2, 1.4 not converged in N
  (upper bounds; 1.26·10⁻⁴¹, 5.67·10⁻⁶⁵ at 80 digits).
- Readings: floor always even; odd 10²–10³ higher; almost-null cluster 7, 14, 20–25 (T = 1.0, 1.2, 1.4); cor:margin1 without
  content for T ≤ 1.4; Θ_T with c* = 1 to 10⁻³⁰ for T ≥ 1.2 (the maximum in μ is a fold: fine tolerance mandatory; a
  run with tolerance 10⁻¹² gave a spurious Θ < 0, discarded).
- Limits: no interval arithmetic; convergence in N not reached for T ≥ 1.2. No formal next step.

## A. Deduplicated «do not retry» list from these files, with reopening condition

Mark: [ABSENT] does not appear in `RULES_AVOID.md`; [INACCURATE] appears with a statement that does not match the source
(both are quoted); [PRESENT] appears in a compatible form.

A1. Omitting the polar term 2A(Ψ)B(Ψ) in the tail form or in limit cell problems (ROUND_016_B §3.1, «recorded
    so that no later round drops it»). No reopening: it is an error, not a route. [ABSENT]
A2. Uniform floor in K of the high block in D units; symbol on the index axis with band/Toeplitz error in D
    units (ROUND_016_B §4(i); STATE_002 N16). Reopening: normalize by the complete gauge-quotient leak ℓ_g (sweeps
    normalized in ℓ_g not covered by the NO-GO). [ABSENT]
A3. Attributing the drift of the high block to the jump at x = −T, to the nonresonant chirp pairs (MV regime) or to the
    resonant comb (ROUND_016_B §1.3). No reopening (measured false). [ABSENT]
A4. Transferring the first-cell constant μ₄ by a transfer lemma to vectors with constraint defect δ ≥ 0.075
    (ROUND_018_A §1; «the fix is not a better transfer lemma but exact constraints»). Reopening: exact constraints
    on all of F₁. [ABSENT]
A5. Constant κ_R uniform in R for the complete R-cell form against ℓ_g in the idealized class with transported
    constraints (ROUND_018_A Thm 4.1(iii); ROUND_019_A; STATE_002 N17). Reopening: quantitative band limitation with
    penalty μβ and an argument that cell R+1 only creates almost-null directions with β/ℓ_g ≳ 1, plus (LB_μ) on the
    low block. [ABSENT]
A6. Qualitative band limitation («u is the restriction of a function of type 2πλ») or absolute bound β ≤ ε‖F‖² as a
    constraint on R-cell data (ROUND_019_A Prop 1.1, §3.2(c)): dense, imposes nothing. No reopening in that form.
    [ABSENT]
A7. Rung inequality (R) of the Schur inequality of the survivor as the sign carrier (2×2 tail Gram with
    collapsed weight log N) (ROUND_018_B; STATE_002 N18): survives c ∈ [0, 3.5]. No reopening except a Λ-specific mechanism
    different from R10. [ABSENT]
A8. Bounds «archimedean coercivity beats the overlapping comb» / 𝒜𝒫 − c𝒞 ≥ 0 on the whole class of admissible tails for
    c ≠ 1 (ROUND_019_B Cor 2.3; N19), including the «crude» proof (decay beyond the first cell + Schur bound
    of the comb + m_eff > κ). Reopening: only using the radical identity in the gauge directions (exact c = 1).
    [PRESENT, INACCURATE] RULES_AVOID D17: «𝒜𝒫 − c𝒞 with c ≠ 1» — the source specifies «on the class of admissible tails …
    unbounded below for c < 1 and for c > 1»; on a fixed (prolate) representative it does hold for c ∈ [0, 3.5] (18B), and
    D17 does not distinguish class from representative.
A9. Choosing «the right representative» of each gauge fibre with comb-robust positivity (existential version) and the
    S-lemma variant with multiplier ≠ 1 (ROUND_020_A Thm 1.3, Thm 1.5; N20): it is exactly (★). No reopening.
    [PRESENT partially] D8 «tails with gauge — only with a new hypothesis resolving the identified failure»: does not record
    that the existential version is a proved exact reformulation nor that the multiplier is fixed at 1.
A10. Λ-free canonical sections (min ℓ, min ∫_0^{1/λ}f², min ‖Ψ‖²) with uniform margin δ (ROUND_020_A §2; N21, PIVOT).
     Reopening: δ(w) stabilizing under refinement (w = 0.025, 0.018) or a section in an H¹-type weighted tail norm in which
     the radical is closed. [ABSENT]
A11. Positivity windows J_R in the comb weight (uniform, per prime, per atom) on idealized R-cell data
     as a source of sign (ROUND_021_A; N22): equivalent to λ₀(R) → 0. No reopening. [PRESENT] D17 «windows in c».
A12. «Identity + coercive remainder» on R-cell data: after Prop 3.2 there is no remainder, Q_R = Q₀ − 𝒦_R Λ-free (ROUND_021_A
     §3.4). [ABSENT]
A13. R-cell sign as a monoid invariant; additive characterization of ℕ on the ray ℕ^{1+t}; proving ∂_tλ₀ < 0 as a step
     toward (★) (ROUND_022_A, ROUND_023_A §5(iii); N23). Source: «the exponent ray should not be pursued further as a route to
     (★)». No reopening. [ABSENT]
A14. Attributing the R-cell sign to the constraints transported by Poisson over ℤ (summation set) (ROUND_022_A
     §2.3). [ABSENT]
A15. Any statement at fixed R (or fixed Λ-free finite subspace with margin) as a sign step (ROUND_019_A §5.1; STATE_001
     round-4 annex, Prop B). Reopening: dimension growing with T / uniformity in R. [PRESENT] D17 «Λ-free planes E_k»
     (only the planes, not the general invariance of §5.1).
A16. Finitely many strict Chebyshev floor relations at the exact truncation (ROUND_024_A Prop 2.1; N24, CONDITIONAL on the
     numerical width of J_T according to REVIEW_010). Reopening: none; without slack it is R10. [ABSENT]
A17. Propagating positivity through the contact entries along N (ROUND_024_A §4; N25). Reopening: a lower
     bound on the total descent rate (EB_C). [ABSENT] (RULES_AVOID C1 mentions «Grönwall» of the L♯ program; not this
     class.)
A18. Prolate extremality with index-8 count as a variational principle (ROUND_024_A design C; N26, ARGUED): retry
     of L′/L′♯. [ABSENT as such]
A19. Schur/Hadamard products of a multiplicative PD local weight on ℚ^×_{>0} with an archimedean kernel independent of q;
     sums of squares by coprime ratio classes; truncations by height or by prime support (ROUND_025_B; also phase
     199 E.5). Reopening: work on K_cut + polar directly (without «the sawtooth decides the sign in the transition
     region», F.2/J.3). [ABSENT]
A20. Global concave maximization of the floor μ_T(v) over weight vectors at the positions log 𝒩_T (ROUND_027_A).
     Reopening: a restricted variant (v ≥ 0 or a set separating falsifiers) with its own reason. [ABSENT]
A21. Partial completeness on squares, on powers of fixed order m or on all powers, with the written positive hypotheses
     (SQUARE_COMPLETENESS_OBSTRUCTION §§6, 8, 9, 11). Reopening: an additional hypothesis excluding the examples,
     specified and proved (integrality, N ≤ 1, functional compatibility); with integrality + all powers + ℓ ≥ 0 the
     datum is identified (§10), which is not a sign. [INACCURATE] RULES_AVOID D14: «integrality identifies, does not sign;
     the power falsifiers also hold without integrality». Source: the FIXED-order falsifiers (F_square, F_m)
     have N ∈ {0, 1}, i.e. they hold WITH integrality; the simultaneous all-powers one (F_all, F_norm) needs
     N(2) = ½ not an integer; the identification requires integrality + all powers + ℓ ≥ 0. Moreover §11 is missing: exact
     residue 1 and count x + O(1) are not enough either.
A22. Cheap locators of minima of the band margin: tone function g_T, dense block k ≤ 96, diagonal, alignment of
     small primes h₄ (ROUND_017_B §2.3; ROUND_021_B; «not reused as a shortcut»); Lanczos with pure warm start.
     Reopening: certified locator via a Lipschitz bound in τ (ROUND_022_B). [ABSENT] (operational, not mathematical)
A23. Lower certificates of the class of P47 prop:lowercert (constant floor of the symbol) beyond contact 8 on the
     available machine (ROUND_026_A §3.3; NO-GO of the machine, not of principle). Reopening: bound of the complement without a positive
     floor at every frequency (average of s_T on windows of width π/T). [ABSENT]
A24. From STATE_001 (rounds 1–3): C1 smooth family s_w (ARGUED) [PRESENT D8]; C5 moment-only criteria of the
     representing measure (germ of B) [PRESENT C1 «Carleman germ criteria»]; C3 floor-only Schur [PRESENT D17]; C2 monotone
     prolate sector (ARGUED, asymptotic) [ABSENT]; C9 split and Div/Near prescriptions of the Schur factorization
     (PROVED, reduced scope) [ABSENT: D8 cites «Arch − Div − Near by Poisson/divisors», a different thing]; cell positivity
     as a complete step [ABSENT].
A25. From STATE_002 (rounds 5–16, not covered above): N3 identity mechanisms on E_T (Selberg, local Euler factors,
     Lévy kernel) PROVED [INACCURATE: B1 cites «Selberg-type identities NODE_001», another source; N3 of 211 does not appear]; N4
     ground-state transformation / weighted Poincaré 𝒦_gap (ARGUED) [ABSENT]; N7 budgets by minimizer
     [ABSENT]; N8 finite-degree Neumann [ABSENT]; N9 Grönwall in T (𝒦_H) [PRESENT partially]; N10 PEψ₀ alone [ABSENT];
     N11 class 𝒦_S of comb mass [ABSENT]; N12 Logvinenko–Sereda/Kovrijkine and moments below log τ ≈ 8T² [ABSENT];
     N14 trivial fixed-profile bound, short packets, MV + Sobolev for (U) [ABSENT]; N1, N2, N5, N6, N13, N15 [PRESENT in D17].

## B. Positive results PROVED, with exact scope

B1. Lemma 2.1/2.2 of ROUND_016_B: F_N = N^{−1/2}τ_{log N}F₁, tail form independent of T in F₁; first cell without comb
    (u on (λ, 2λ) ⇒ 𝒲[𝒯u] = 𝒜_∞[F₁]). Λ-blind.
B2. ROUND_017_C Theorem 3.1 (assisted, ball arithmetic): every window of length log 2, ∫F e^{−y/2} = 0 ⇒
    (1/2π)∫m|F̂|² ≥ 0.069611‖F‖² (independent of T); Cor 3.2 complete form ≥ μ₀ on {B = 0}; Theorem 3.3 with four
    transported functionals, μ₄(0.8) ≥ 0.527631, μ₄(1.0) ≥ 0.549417 (pointwise in T). Tool: Lemmas 2.1–2.4 (monotone
    symbol, truncation, polynomial compression with HS tail, bound with constraints).
B3. ROUND_018_A: Lemma 1.1 (transfer by seminorm); Lemmas 3.2–3.3; Theorem 3.4: Q₃ ≥ 0.70·ℓ_g on V₃, T ∈ {0.8, 1.0}
    (assisted); ROUND_019_A §5.2: Q₃ ≥ 0.60ℓ_g with c₂ = 0 (T = 0.8, 1.0), ≥ 0.20ℓ_g with c₂ = 1.01 (T = 0.8). Coercivity, not sign.
B4. ROUND_019_A Prop 1.1 (density of Paley–Wiener constraints in the form norm) and Lemma 2.1 (band defect).
B5. ROUND_017_A Props 1.1–1.3, 3.1 (Schur/secular form; b = ∫h_G dν, b_Tate ≡ 0; second-level radical identity on
    E images; radical defect X_w under cΛ, a_P, e) — PROVED for data with f(λ) = 0; survivor ARGUED.
B6. ROUND_018_B Lemmas 1.1–1.2 (collapsed weight c log N = 𝒜_∞ − c𝒞 + 𝒯 on tails; 2×2 Schur = determinant).
B7. ROUND_017_B Prop 1.1: closed form A_τ^{(η)} = ½(𝔈 + 𝔈ᵀ), 2T𝔈 = CS − ESCE + ESHE + HS + Dd (any real weight).
B8. ROUND_019_B Prop 1.1/Cor 1.2 (E(admissibles) ⊇ C_c^∞(I_T) ∩ P_T; (★) ⟺ 𝒲̂ ≥ 0 on E images of the kernel); Theorem 2.1
    (gauge radicals with 𝒜𝒫 → −11.457‖η‖² and → +1.114‖η‖², without zeros); Cor 2.2 (𝒲̂^c unbounded below on each fibre,
    c ≠ 1).
B9. ROUND_020_A Lemmas 1.1–1.2, Theorem 1.3, Cor 1.4 ((★) ⟺ 𝒜𝒫 ≥ 0 on V_T ∩ {𝒞 = 0}), Theorem 1.5 (finite sections).
B10. ROUND_021_A §3.1 and Prop 3.2: Φ_R homomorphism from the truncated Dirichlet convolution to compressed shifts,
     [M_x, Φ_R(α)] = Φ_R(α log); P_w𝔇_R = [M_x, 𝔇_R] ⟺ w ≡ 1; Q_R^{(c)} = Q₀ − c𝒦_R; Lemma 1.1 (windows are intervals);
     §2.1 (Galerkin windows are outer); Lemma 3.3 (sandwich). ROUND_022_A Lemma 3.1 (every multiplicative system) and
     Prop 3.2 (first variations). ROUND_023_A Lemma 2.1 (Φ(Λ log) = [M, P] = 𝔇⁻¹[M,[M,𝔇]] − P²), Props 2.2–2.4 (2.4 must
     include the polar functionals, REVIEW_010), Lemma 4.1, 2×2 formula.
B11. ROUND_024_A Lemmas 4.1–4.2, Prop 4.3 (entry law), Cor 4.4(i); Prop 2.1 (strict floors open in c).
B12. ROUND_025_B Theorem 1.1 (prime-free kernel K_ℕ under (H)), Theorem 2.1, Prop 3.1 ((ab)^{−1/2} PD on ℚ^×_{>0}), Theorem 3.2
     (zero cofactor at σ = 0, citation of the symbol).
B13. ROUND_026_A Theorems 26A.1 and 26A.2 (assisted): λ_A(T) ≥ 1.0·10⁻²³ for T ≤ 1; λ_A(T) ≥ 2·10⁻²⁶ for T ≤ 1.035. Within the
     cited range; extends the own certified range from ½log5. §3.1 forced size bounds of the class.
B14. SQUARE_COMPLETENESS_OBSTRUCTION §§2, 5–11: algebraic identities of the families, analytic C_F(log 4) > 0, falsifiers
     PROVED for the declared classes; §10 identification by integrality + all powers + ℓ ≥ 0.
B15. Inherited in STATE_001/STATE_002 (rounds 1–16, already recorded in earlier annexes): P1–P35, Q1–Q27; in particular Q1
     (certified falsifiers a_3, Beurling 3 → 3.2, 1.1Λ) and Q2 (doubly exponential upper bound given thm:ext-half).

## C. Open obligations (precise mathematical statement and what was attempted)

C1. (HR_g): there exists κ_T > 0 independent of K with 𝒢[b] ≥ κ_Tℓ_g^S[b] for all b ∈ S𝒜 on high indices (ROUND_016_B §4).
    Attempted: first cell (17C), three cells (18A), idealized R cells (collapse R ≥ 5), band (19A).
C2. H_band(μ, κ): for every R ≥ 2 and F ∈ V_R, Q_R[F] + μβ[F] ≥ κℓ_g[F]; together with H_lim and (LB_μ): the in-band part of the complete
    form dominates μ‖ℱf‖²_{L²(0,λ)} on admissibles modulo gauge (ROUND_019_A Thm 4.1, §4). Attempted: numerical R ≤ 8; certified
    only R = 2, 3 with μ = 0.
C3. (ii_s) / (B_δ, s): for a Λ-free linear section s, 𝒲̂ ≥ δ|𝒞| on Ran s (ROUND_019_B, ROUND_020_A §3). Attempted: three
    sections, δ decreasing with resolution.
C4. Schur balance of the exact survivor and parity piece (P): decide whether (P) has a comb-robust tail form
    (ROUND_017_A, ROUND_018_B next step). Attempted: rungs (robust), E images of prolates ψ_0…ψ_40 (do not reach (P)).
C5. Q₀ − 𝒦_R ≥ 0 on V_R for every R (Λ-free R-cell form, ROUND_021_A §3.4(iii)), with λ₀(R) ~ exp(−2.9R log R)
    numerically; and whether the almost-null direction is the 𝔇_R-preimage of the floor of 𝒜 − Π on the window.
C6. Sign of ∂_tQ on the almost-null cluster and whether ∂_tλ₀ → −1 (ROUND_022_A, 023_A) — declared useless for (★).
C7. (EB_C): lower bound on the total descent rate of λ_A along N (≤ 8πe^{2T}hλ_A in P211-8C); (R_edge) (simple
    floor, continuity at the edge) for Cor 4.4(ii) (ROUND_024_A).
C8. K_cut + polar ⪰ 0 (sawtooth cutoff remainder of Thm 2.1 of ROUND_025_B in the tail variable).
C9. (HB_η) uniform in T with a cross-term lemma; coverage of the band margin on [1.2, 3]·2πN (T = 3.5), [1.11, 3]·2πN
    (T = 4), strip r ∈ [1.1, 1.3] (T ≥ 4) (ROUND_017_B, 021_B, 022_B). Generic piece for c < 1.
C10. Bound of the complement in lower certificates without a positive symbol floor (average of s_T over windows π/T; Q12
     proved only for T ≤ log 2) (ROUND_026_A §3.3).
C11. From STATE_001 §5.5: Θ_T(Λ) ≥ 0 (Lévy form ≥ 0 on the quadric {F ∈ P_T : Σv_n Re c_F(log n) = 0}); 1 ∈ J_T; (P1) second
     even eigenvalue almost null and (P2) Π indefinite on the even pair, from the exact Λ(n); simplicity of the floor.
C12. From STATE_002 §5: (H₋) for the Neumann expansion; lower half of prob:ext-L (intermediate prolate range 10 ≲ k ≲ 4N);
     (HR) in complete ℓ_g normalization.
C13. P6 (STATE_001): o(M) bound of the remainder for the necessary condition 𝒜(w) ≥ 0 outside P_{T′}.

## D. Objects, next steps or ideas named and never taken up

Next steps of memos not taken up by any file of the range: ROUND_016_B (ℓ_g with gauge resolved MIN ≥ 30, Nb ≥ 370);
ROUND_017_A (partly taken up by 18B); ROUND_017_B (coverage and locator by phases p ≤ 13); ROUND_017_C/018_A (multicell R = 4
with penalty μ(1 − B_R), five pieces, shifts log 2, log 3; falsifiers (b)–(d) on Thm 3.4: (b) done in 19A);
ROUND_018_B (parity (P) by Möbius preimage); ROUND_019_A ((LB_μ) for μ = 10², 10⁴, 10⁶; H_band certificate at R = 4);
ROUND_019_B (section minimizing the leak, c ∈ [0.5, 2], rank ≥ 30); ROUND_020_A (δ(w) at w = 0.025, 0.018); ROUND_021_A
(preimage 𝔇_R^{−1} = Φ_R(μ) of the floor of 𝒜 − Π); ROUND_021_B/022_B (complete strip; locator by Lipschitz bound of
λ_max(A_τ)); ROUND_022_A (system preserving log-gaps up to a size and breaking a single relation m = kn: isolate
near-coincidences — idea named, never executed); ROUND_024_A (proof of (R_edge) at n = 7, 8, 9); ROUND_025_B (K_cut + polar).

STATE_001 §6, candidates with a first lemma:
D1. C11/C8 almost-null pair and tangency: test whether Π is indefinite on the Λ-free plane E_T of the two lowest eigenvectors of
    Arch on P_T^ev and compute the 2×2 Schur of a_T on it (if it captures the pin, a non-circular 2×2 inequality in the Λ(n)). (ROUND_004_A
    treated planes E_k; Prop B closes fixed planes with margin.)
D2. C3 continued: A_𝒞𝒞 ⪰ R ⊕ c_floor(1 − Π) with Π a projection onto span{P_𝒞Ae_k : k ∈ 𝒩} ∪ modes of W_{t_1}; requires a
    certified version of the 11-mode block.
D3. Exterior form at low Mellin frequency: write ℬ_n in a basis of low-frequency admissible tails and decide whether
    Σ log n·ℬ_n has a sign pattern that fails for W = c log and W_{a_P}.
D4. C6 transport defect M → M+1 (Paper 39) / coercivity of adjacent windows (Paper 38). NOT STARTED. First lemma:
    exact formula of 𝔸_{M+1} ⪰ 0 given 𝔸_M ≻ 0 as a scalar Schur complement on the new row B(log((M+1)/k)).
D5. C4 corona/symbol lens (Paper 26) on M ↦ 𝔸_M. NOT STARTED. First lemma: identify the limit symbol of the field and whether
    𝔸_M − (limit) is compact with an exact formula.
D6. C7 route N of phase 160 (finite-window Carathéodory–Fejér). NOT STARTED. First lemma: answer the objection «dies in the
    limit» with a statement at fixed T.
D7. P6: o(M) bound of the remainder (O(M^{−7/3+ε}) suffices); necessary condition only.
SURVEY_001 (tools never aimed at the finite objects; no first lemma unless indicated):
D8. Paper 26: Weil–Toeplitz algebra, ideal J ≅ c₀, corona W/J, symbol σ(Q), Cesàro states versus norm, on
    [Ξ_{F0}(log(m/k))] (= D5).
D9. Paper 38: coercivity of adjacent windows |H_L|² + |H_{L+1}|² ≥ ½|z|^{2L} for the pair (S_{T,k}, S_{T,k+1}) (= D4).
D10. Paper 39: exact transport defect (two rank-one channels of opposite parity + double operator integral
     correction) and trace of the second resolvent for S_{T,k} → S_{T,k+1} (= D4).
D11. Paper 07 thm:trunc: η(X) ≤ A exp(−α(log X)²) as an estimate of the margin between contacts. (Caveat: falls into B2 of RULES_AVOID
     if used as a bound with remainder.)
D12. Paper 22: Carleman determinacy on the measure of s_T|F̂|² or of Near_M. (Caveat: C5 of STATE_001 and «Carleman germ
     criteria» of RULES_AVOID C1 close moment-only use.)
D13. Paper 15 thm:crit: eventual positivity → uniform for the tower S_{T,k} (bounded threshold / finite type). Never applied.
D14. Paper 24: dominance measure as an analogy for Arch_M − Div_M − Near_M.
D15. Paper 09 thm:concave: reduction to extreme points of boxes of admissible Λ(n) (related to, not identical with, ROUND_027_A).
D16. Paper 35: Bakry–Émery curvature bound of the prime part after Doob conjugation on S_{T,k}. (Caveat: Bakry–Émery
     Γ₂ appears closed, INV_N_001, cited in ROUND_024_A §0.)
D17. Paper 36: one-round cross-check of thm:mirror-criterion and nodes H1–H5 with S_{T,k}.
STATE_002 §5 (open targets in order): 1 (B_δ, s) — see C3; 2 uniformity in R with quantitative band — C2; 3 (HB_η) — C9;
4 (ii_s) — C3; 5 (H₋), (EB_C) — C7, C12; 6 lower prob:ext-L and (HR) in ℓ_g — C12. None taken up in the range except (EB_C),
which ROUND_024_A identifies as the residue and does not attack.

## E. Coverage

Range: `ls *.md | sort` in `../phase-211-sign-sandbox/`, from `ROUND_016_B.md` to `TOOL_001_GALERKIN_MP.md` inclusive:
25 files (ROUND_016_B, ROUND_017_A, ROUND_017_B, ROUND_017_C, ROUND_018_A, ROUND_018_B, ROUND_019_A, ROUND_019_B,
ROUND_020_A, ROUND_021_A, ROUND_021_B, ROUND_022_A, ROUND_022_B, ROUND_023_A, ROUND_024_A, ROUND_025_B, ROUND_026_A,
ROUND_027_A, SQUARE_COMPLETENESS_AUDIT, SQUARE_COMPLETENESS_OBSTRUCTION, STATE_001, STATE_002, STATEMENT_001, SURVEY_001,
TOOL_001_GALERKIN_MP). Read completely: 25 of 25. No file or stretch left unread. Order: that of `sort` in the system
locale (STATEMENT_001 after STATE_002). The summaries in STATE_001/STATE_002 of rounds prior to
ROUND_016_B are recorded as given by those files, without rereading the source rounds (covered by other annexes).
