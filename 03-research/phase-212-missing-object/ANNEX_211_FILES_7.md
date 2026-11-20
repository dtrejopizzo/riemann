# Annex 211 — files ROUND_007_C to ROUND_016_A (complete reading)

Source: `../phase-211-sign-sandbox/`, files `*.md` in alphabetical order (`ls *.md | sort`) from `ROUND_007_C.md`
to `ROUND_016_A.md` inclusive: 22 files (ROUND_008_B, ROUND_010_B and ROUND_014_B do not exist). Notation of
`STATEMENT_001.md`: a_T = Arch − Π on P_T, λ_A(T), v_n = 2Λ(n)/√n, N = e^{2T}, λ = e^T, c = 2πN, m(τ) =
Re ψ(¼+iτ/2) − log π, K the Lévy kernel, C_0 = m(0). Goal (★): λ_A(T) ≥ 0 for all T. Also: W_T complete
form, E summation map Ef(x) = e^{x/2}Σ_{n≥1}f(ne^x), ψ_k even prolates of [−λ, λ] with parameter c, χ_k
concentrations, d_k = 1 − χ_k, ε_k = i^k, 𝒯 tail map, 𝒲 complete form on the line. Falsifiers of rule 4:
(a) cΛ, (b) a_P / a_3 (prime 2 deleted), (c) Beurling systems (shift 3 → 3.2), (d) finite modification.
Labels as they appear in the files. «Taken» indicates whether a later file in the range carried out the step.

---------------------------------------------------------------------------------------------------

## Entries by file

### 1. ROUND_007_C.md — certified falsifiers (a_3, 3 → 3.2, 1.1Λ)
- Object: a_T^w(F) = C_0‖F‖² + Lev(c_F) − Σ_x w_x c_F(x) for finite combs w; witnesses F = Σ a_k sin(kπ(t+T)/2T)
  in P_T with enclosure in ball arithmetic.
- Lemma 1 (witness bound): PROVED. Lemma 2 (extension by zero: a_{T′}(F̃) = a_T(F), witness holds for all T′ ≥ T): PROVED.
- Lemma 3 (Lévy form on Dirichlet sines: closed formula for c_F, tail ∫_{2T}^∞K = −log tanh(T/2) + π − 2arctan e^T,
  bound on [0, δ] by ‖F′‖²(δ²/4 + δ³/12)): PROVED.
- Thm 1: λ_A(½log5 + 10⁻⁴; a_3) ≤ −0.50528: PROVED. Thm 2: λ_A(½log5 + 10⁻⁴; 3 → 3.2) ≤ −0.23448: PROVED.
  Thm 3: λ_A(1; 1.1Λ) ≤ −0.078244: PROVED (all for every larger T′).
- Record: NO-GO (PROVED) of sign mechanisms based only on identities valid for a_3 or 3 → 3.2 (Λ∗1 = log,
  Selberg identities, Euler factor bounds, Lévy kernel identity) at T ≥ ½log5 + 10⁻⁴.
- Open remainder: Θ_T(w) < 0 for a_3 and 3 → 3.2 (two-witness criterion in μ stated, not carried out): OPEN;
  λ_A(T; 1.1Λ) < 0 for T < 1: NUMERICAL; non-rejection of the Krylov family at c = 1.1: NUMERICAL.
- Reusable positives: Lemmas 1–3 (every finite comb); three certificates with ≤ 5 rational coefficients.
- Next step: certify Θ_T < 0 by covering in μ and 1.1Λ at T = 0.9. Taken: no.

### 2. ROUND_007_D.md — lower half of a two-sided law for λ_A
- Object: law λ_A(T) = L(T)(1 + o(1)); comparison with λ_W (complete form) and with cΛ, a_3; unrestricted
  eigenvalues μ_k of a_T in L²_ev(I_T), Tate moments τ_k.
- Prop 4.1 (λ_W^par ≤ λ_A^par ≤ λ_{W,2}^par): PROVED. Cor 4.3 (floors λ_A ≥ 2^{−1518} for T ≤ ½log12, ≥ 2^{−2904} for
  T ≤ ½log15): transfer PROVED from CITED inputs.
- Prop 4.2 (capacity correction; «λ_A ≥ λ_W − 𝔤/‖h‖²» REFUTED in general by a 2×2 model): PROVED.
- Prop 4.4 (a law for λ_W only transfers a floor; −log λ_A ≤ 4πe^{2T} − 9T + O(1)): CONDITIONAL (band κ OPEN).
- Lemma 4.6 (λ_A^ev ≥ L ⟺ τ₀²/(|μ₀|+L) ≥ Σ_{k≥1}τ_k²/(μ_k − L)): PROVED. Cor 4.7 (with n₋ = 1: μ₁ ≥ L and τ₁² ≤ ηL·D(L)
  ⟹ λ_A^ev ≥ (1−η)L; converse λ_A ≥ L ⟹ μ₁ ≥ L): PROVED reduction.
- NUMERICAL: λ_A to 40–80 digits at T = 1.0–1.4; rate-2 law: −ln λ_A = c₁e^{2T} + c₂T + c₃, c₁ → 4π from above
  (12.99 → 12.59); simply exponential family NO-GO as a law (fails by 14 orders at T = 1.4); no jumps at
  contacts ½log7, ½log8 (≥ 0.03 digits); falsifiers cross zero at T ≈ 0.48–0.67 with size O(10⁻²), then −|1−c|g(T).
- Remainder: (N1′) μ₁(T) ≥ L(T) ≈ exp(−4πe^{2T}) — not weaker than (★), with margin; no mechanism of the phase gives a
  positive floor for μ₁. PIVOT.
- Reusable positives: Prop 4.1 (sandwich), Cor 4.3 (floors up to ½log15), Lemma 4.6, Cor 4.7.
- Next step: lower bound of μ₁ with Hellmann–Feynman sensitivity dμ₁/dc = Π_T(e₁). Taken: no.

### 3. ROUND_007_E.md — family of comb responses E_T in multiprecision (T = 1.0, 1.2, 1.4)
- Object: E_T = N′ ⊕ P_𝒞Π(𝒩_η + 𝒯) (negative Nyquist block with gauge + Π responses), exact Schur complement.
- Everything NUMERICAL; nothing PROVED. PIVOT.
- Findings: E_T captures the bottom of the cluster at angle 10⁻⁸–10⁻¹⁵, coercive complement (λ_min(C) ∈ [0.9, 2.5]),
  but λ_min(a_T|E_T) exceeds λ_A by 6/13/31 orders (T = 1.0/1.2/1.4): the sign lives in the Schur coupling.
  Necessary condition fails for 0.99Λ, 1.01Λ, 1.1Λ, a_3, v_2 + 0.1 (confounded by saturation). dim E_T ≈ 7× cluster.
- Remainder: R3(i) (capture at precision λ_A) not met; R1 (growth vs saturation) OPEN; run T = 1.4 with q_cap = 120
  degenerate.
- Next step: coupling B C⁻¹ Bᵀ with N ≥ 200, truncation of the block to a fixed fraction of N. Taken: yes, ROUND_008_D.

### 4. ROUND_008_A.md — exact band Schur complement and Neumann expansion in the comb
- Object: spectral band B_t = span{u_l : α_l ≤ t} of Arch, complement C_t; Arch block-diagonal, coupled
  only by the comb; S_T = D_b − Π_bb − Π_bc C⁻¹ Π_cb, C = Arch_c − Π_cc.
- Thm 2.1 (exact band reduction for t_c > π_+; (★)_T ⟺ S_T ⪰ 0; quantitative bounds with κ = ‖C⁻¹Π_cb‖): PROVED.
- Thm 3.1 (C = Arch_c^{1/2}(1−X)Arch_c^{1/2}; Neumann series converges iff r = ‖X‖ < 1, sufficient ‖Π‖ < t_c; term
  k homogeneous of degree k+2 in v with only archimedean coefficients; two-sided tail ε_K; K odd ⟹ S_T ⪯ S_T^{(K)}): PROVED.
- Cor 3.2 (what a truncation certifies; necessary degree K+1 ≳ log(‖Y*Y‖/((1−r)λ_min S_T))/log(1/r)): PROVED.
- Obs. 3.3: S^{(K)}(cv) is not homogeneous (not blind to c like the word families).
- The file ends at Obs. 3.3: the announced numerical §4 and the Result / Next step sections do not appear in the
  file read (ROUND_008_D cites from it K* ≈ 150 with certified tail, ≈ 25–40 in practice, and K ≈ 7 for 1.01Λ).
- Reusable positives: Thm 2.1, Thm 3.1, Cor 3.2 (valid for every Galerkin compression and every comb).
- Next step: not recorded. Taken: the degree question is taken up by ROUND_008_D.

### 5. ROUND_008_C.md — one-sided variation of λ_A in T, two brackets and Grönwall in the window variable
- Object: dilation U_rF; virial 𝒱^♯ = 𝒱_∞ − Σ v_n log n·c_F′(log n) + τ(F) (Tate moments × multipliers),
  entry fold φ; boundary-strip budget 𝔈_h.
- Lemma 1.2 (m′ ≥ 0 on [0, ∞); 0 ≤ 𝒱_∞ ≤ M₁‖F‖²): PROVED.
- Thm 1 (λ_A(T+h) ≤ λ_A(T) − (h/T)𝒱^♯(F) − h⁺φ(F) + o(h) on the bottom eigenspace): PROVED under (R_E); Danskin
  equality CONDITIONAL on (U). Cor 2.2 (𝒱^♯ ≥ 0 on E_T; fold: cost in the even sector, payment in the odd one): PROVED under (R_E).
- Prop 2.3 (three frames: extension by zero, dilation, truncation): PROVED.
- Prop 3 (decrement ≤ boundary-strip energy: (λ_A(T) − λ_A(T+h))‖G♯‖² ≤ 𝔈_h): PROVED for minimizers bounded
  near ±T; ARGUED in general. Cor 3.1 (derivative between virial and boundary budget): PROVED under hypotheses.
- Prop 4 (discrete Grönwall on increments, continuity only): PROVED. Prop 5 (D ≤ Cλ, (EB_C), (VE_C) with unspecified
  C = (★) + Lipschitz; every falsifier fails automatically at its first zero by its own sign):
  PROVED; uniform version = (★) at the next Euler step: ARGUED. Prop 6 (D/λ via the minimizer): PROVED under (R_E).
- NO-GO (reformulation): Grönwall in T, class 𝒦_H; the constant demanded by the data C ≈ 8πe^{2T} − 21 is the Slepian
  constant 2 in c. NUMERICAL: Hellmann–Feynman reproduces the derivative to 11–22 digits; virial ≈ 1.003 cancels to relative
  precision C·T·λ (3.4·10⁻²¹ at T = 1).
- Remainder: (EB_C) with C(T) = 8πe^{2T}(1+o(1)) for T ≥ ½log5: OPEN; Hadamard form 𝔈_h ≍ (θ₊² + θ₋²)h: ARGUED.
- Reusable positives: Thm 1, Cor 2.2, Prop 2.3, Prop 3, Prop 4 (for every comb).
- Next step: measure 𝔈_h/h with a basis that resolves the boundary and the traces θ_±; do not retry Grönwall with another
  denominator. Taken: no.

### 6. ROUND_008_D.md — Schur coupling of E_T: rank, Neumann and truncation degree
- Object: S_E = a_EE − a_EC a_CC⁻¹ a_CE with E = E_T, C = E_T^c; X = Arch_CC^{−1/2}Π_CC Arch_CC^{−1/2}.
- Prop 1 (a_CE = Arch_CE − Π_CE P_V; a_EC = Arch_EC only on N′): PROVED.
- Thm 2 (Neumann on E_T^c, tail, structure of degrees k, k+1, k+2): PROVED under (H₋); (H₋) NUMERICAL, without proof
  (proved π_− exceeds λ_min(Arch_CC) 2.4×). Cor 3 (necessary degree ∝ log(1/λ_A)/log(1/r)): PROVED under (H₋).
- Prop 4 (explicit finite sufficient polynomial inequality at T = 1, N fixed, V and C frozen): PROVED conditional on (H₋).
- NUMERICAL: coupling O(1) and of nearly full rank; r ≈ 0.54 (T = 1), 0.65–0.67 (T = 1.2); low even truncations
  with the wrong sign; K* ≈ 25–30 / 105–125, certified tail K ≈ 80–84 / 205–220; falsifiers rejected at K = 0–7.
- NO-GO (class: finite-degree Neumann truncation of the Schur coupling on E_T with tail by spectral radius):
  same wall as the archimedean band of ROUND_008_A; unsigned terms, relative cancellation 10⁻⁹ per order.
- Remainder: version uniform in N; degree bound independent of λ_A: OPEN.
- Next step: Chebyshev/minimax polynomial of 1/(1−x) (still ∝ log(1/λ_A)); close the class except for signed
  resummation. Taken: no.

### 7. ROUND_008_E.md — margin law of λ_A against the prolate defect 1 − χ_k(2πN)
- Object: R(T) = λ_A/(1 − χ_0(2πN)); images Eψ_k; space 𝒜⁺_T (f even, C², f(λ) = f′(λ) = 0, f(0) = ℱf(0) = 0);
  out-of-band energies L₁, L₂.
- Thm 3.1 (W_T(Ef) ≤ Kλ^{−2}(L₁² + L₂²) on 𝒜⁺_T): PROVED given thm:ext-half. Cor 3.2 (λ_A ≤ 4K(L₁²+L₂²)/‖f|‖²): PROVED.
- Prop 3.3 (index count: 5 dimensions for λ_A — four functionals f(0), ℱf(0), A(Ef), B(Ef) —, 3 for λ_W): PROVED.
- Lemma 3.4 (weighted leakage of tapered prolates): ARGUED; Cor 3.5 (upper half index 8): CONDITIONAL (superseded by
  ROUND_009_A; the comparison with 1 − χ_0 via the Fuchs quotient was withdrawn).
- Conj 4.1 (λ_A ≥ κ₋N^a(1 − χ_0), sharp form κ₋(1 − χ_8)): OPEN. Prop 4.2 (under prob:ext-L, λ_A ≥ (κ/4)N^{−A_0−1}(1−χ_0)):
  transfer PROVED, CONDITIONAL. Lemma 4.3 (leakage floor on a restricted subspace d_q/(1 + ‖C^{−1}‖²‖C‖²)): PROVED;
  application (index 6) CONDITIONAL on polynomial κ_C (OPEN).
- Prop 5.1 and identity (5.1) W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]; law with zero robustness (survives cΛ only with
  |1−c||Π_T(F★)| ≤ λ_A): PROVED.
- NUMERICAL: R ≈ e^{17.1}N^{9.6}; κ₈ = λ_A/(1 − χ_8) ∈ [0.74, 1.62] over 37 windows; the minimizer lies in
  P_T ∩ span{Eψ_0, …, Eψ_8} at angle 10⁻⁴; only ψ_0, ψ_4, ψ_8 enter the even sector; gap λ_A/λ_W = index change 4 → 8.
- NO-GO (NUMERICAL): upper half with the single test function PEψ_0 (quotient 0.12–0.26, angle 63–75°).
- Remainder: lower half; intermediate range 10 ≲ k ≲ 4N not touched by any coercivity; low block–rest coupling.
- Reusable positives: Thm 3.1, Cor 3.2, Prop 3.3, Lemma 4.3, (5.1)/Prop 5.1.
- Next step: prove Lemma 3.4; prove prob:ext-L in prolate form by sectors. Taken: yes, ROUND_009_A and ROUND_009_B.

### 8. ROUND_009_A.md — leakage bound for mollified prolates (Lemma 3.4′); upper bound only
- Object: V_d = {f_a = (Σ_{k∈K_d}a_kφ_k(x/a)1_{[−a,a]}) ∗ ρ_ε}, a = λ − ε, b = λ²/a (c = 2πN exact), ε = θλ^{−3},
  θ = 1/(48π²), ρ(u) = (35/32)(1 − u²)³₊, d ∈ {3, 5}.
- (F1) 0 ≤ ϑ_k ≤ k(k+1) + c²; (F2) ϑ_k ≥ c/8; (F3) m_k = ∫_1^∞φ_k² = (1−χ_k)/(2χ_k): PROVED.
- Lemma 2.1 (boundary sheet of width 1/(12c²)): PROVED. Lemma 2.2 (φ_k(1)² ≤ 27c²m_k, ∫_1^∞φ_k′² ≤ 60c⁴m_k): PROVED.
  Lemma 2.3 (∫_0^hφ_k² ≤ 12h√c, Sonin function): PROVED.
- Lemma 3.4′ ((L₁² + L₂²)/‖f|‖² ≤ C_dN⁹(1 − χ_{2d−2}), C_5 = 1.3·10¹⁶, N ≥ 1.6·10⁶; existence for 3 ≤ N < N₀): PROVED
  (Landau and Titchmarsh CITED).
- Cor 4.1 (λ_A ≤ 4KC_5N⁹(1 − χ_8), λ_W ≤ 4KC_3N⁹(1 − χ_4)): PROVED given thm:ext-half. §7: K = 141 admissible (PROVED);
  Cor 7.1 (λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πe^{2T}} for N ≥ 1.6·10⁶): PROVED given thm:ext-half and a CITED non-asymptotic bound
  (arXiv:1804.01257, Thm 3.2).
- Failed: explicit constant for N < N₀; exponent b = 9 not sharp; comparison 1 − χ_8 vs 1 − χ_0 not re-proved.
- Reusable positives: Lemmas 2.1–2.3, Lemma 3.4′, Cor 4.1, Cor 7.1 (explicit doubly exponential upper bound).
- Next step: lower N₀ (sup|φ_k| ≤ C(k)c^{1/4}) and b (exact 1/s decay of Φ_a′). Taken: no.

### 9. ROUND_009_B.md — Fourier class selection rule and lower half in the self-dual sector
- Object: prolate index classes ε_k = i^k; h_k = P_+Π_TEψ_k; pair (M, D) with D = Σd_ka_k²; blocks L = {0, 4, 8},
  middle 12 ≤ k ≤ 4N, high k > 4N.
- Thm 1.1 (exact parity defect P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf)): PROVED. Thm 1.2 (‖ℱf − εf‖² = Σ2(1 − εε_k√χ_k)a_k²):
  PROVED given CITED facts. Lemma 1.3 (‖Eh‖² ≤ ζ(2s)λ^{2s}∫u^{2s}|h|²): PROVED. Cor 1.4: PROVED for C¹ data.
- Thm 1.5 + Lemma 1.6 (decoupling of classes in the even sector; cross terms ≲ poly(N)√(d_jd_k)): PROVED.
- §1.7 (the near-null class of the even sector is the ℱ-eigenvalue +1): PROVED (reading). Lemma 2.1, Prop 2.2 (two- and three-level
  Schur): PROVED. Bound (2.1) λ_A ≥ κ(1 − χ_8)N^{−b} on the subspace: PROVED as an implication, CONDITIONAL on three
  constants (later measured in ROUND_010_A: factor 10⁻⁶; «not to be read as a bound on λ_A»).
- §2.4(iii) (decay of α_HI through near-gauge vectors): ARGUED — WITHDRAWN in ROUND_010_A.
- NUMERICAL: even spectrum λ_j^ev ≈ (0.85–2.0)(1 − χ_{4j+8}); three-level Schur closes up to 1.4–2.0·4N.
- Falsifiers: the class–parity rule is Λ-free (not a sign step); the near-nullity of the +1 class is destroyed
  by 𝒫_{Λ−w}; the map adapted to a_P does not intertwine ℱ with R (PROVED).
- Remainder: (HR) high-range estimate: (a) inf a_T/ℓ_HI ≥ κ_HN^{−b}; (b) Γ′² ≤ (1−η)κ_LMκ_HN^{−b}: OPEN.
- Reusable positives: Thm 1.1, Thm 1.2, Lemma 1.3, Thm 1.5, Lemma 1.6, Lemma 2.1, Prop 2.2.
- Next step: prove (HR)(a) with gauge-minimized D on the high block; measure κ_C and ‖Gram‖. Taken: yes, ROUND_010_A.

### 10. ROUND_010_A.md — (HR) with consistent gauge quotient; scale of the generic tools in the comb
- Object: consistent pair (M(a) = W_T(Ef_a), D_g = D − DJH^{−1}JᵀD) on 𝒜_K (five conditions: f(λ) = f(0) = ∫f =
  A(Ef) = B(Ef) = 0).
- Obs. 1.1 (the pair of 9B differs in three identified points): PROVED. (3.1) W_T(g) = (1/2π)∫(m − P_T)|ĝ|² + 2A(g)B(g),
  P_T(τ) = Σ_{n<N}v_n cos(τ log n): PROVED.
- Lemma 3.1 (L² Markov, (K+2)²/L): PROVED. Prop 3.2 (lem:ext-hf is empty on degree-K data unless K is superpolynomial
  in N): PROVED.
- Prop 3.3 NO-GO (class 𝒦_S: estimates that see the comb only through its total mass Σw_n ≤ S): there exist w ∈ 𝒦_S and g ∈ P_T
  with spectrum in Ω₀ ≤ |τ| ≤ 2Ω₀ and W^w_T(g) < 0 for log(2 + 3Ω₀) ≤ S − C₀: PROVED; transfer to the high block ARGUED.
- Prop 4.1 (cross overlaps of prolates ≡ 0; all the coupling is the symbolic pairing (4.1)): PROVED.
- NUMERICAL: α_HI = O(1) in the consistent pair (no collapse), decreases ≈ 4N/K; Γ′ grows; assembled Schur bound
  θ_K = 0.86 → 0.025; falsifiers rejected only on the low block (≈ −10²⁰ d_8).
- Corrections: 9B §2.4(iii) WITHDRAWN; constant of (2.1) measured (≈ 3–4·10⁻⁶).
- Remainder: (HR)(a) uniform in K, (HR)(b), (HR-Π) on the plunge (m×m, m = O(log N log(1/ε))): OPEN; the
  super-plunge range up to e^{cλ} does not reduce to finite dimension.
- Reusable positives: (3.1), Lemma 3.1, Prop 3.2, Prop 4.1.
- Next step: mean-value/large-value tool for P_T on the high block; raise Nb. Taken: yes, ROUND_011_A
  (theory) and ROUND_011_B (numerics).

### 11. ROUND_011_A.md — (HR)(a) via large values of P_T; uncertainty; exact open range
- Object: packets g₀ = β(x/T)cos(τ₀x); P^ρ_T(τ) = Σ_{n<N}v_nρ(log n/T)cos(τ log n), ρ normalized autocorrelation of β;
  Σ₀ = Σ_{n<N}v_n, S₂ = Σ_p a_p².
- Lemma 1.1 (packet calculus): PROVED. Prop 1.2 (necessity: every coercive (HR)(a) ⟹ P^ρ_T(τ₀) ≤ m(τ₀) − κ + O(1/(τ₀T))
  for all τ₀ ≥ 2Ω_lo): PROVED.
- Lemma 2.1 (local energy at scale 1/T): PROVED. Prop 2.2 (thickness of {P_T ≤ ϑm} + Kovrijkine CITED gives only the pointwise
  condition (2.1), stronger than (1.2)): PROVED.
- Thm 3.1 (P^ρ_T < ϑm on [Ω, 2Ω] if (3.1); log Ω_B = (64/(eϑ²))Te^{2T}(1+o(1))): PROVED given Mertens/PNT CITED.
  Cor 3.2 ((HR)(a) with θ → 0 for data above Ω_B, coercivity ≍ TN): PROVED.
- Prop 4.1 (sup_{[Ω,2Ω]}P^ρ_T ≥ c₁T for Ω ≥ N²; hence (1.2) fails for cΛ with c ≥ c* absolute): PROVED.
- NO-GO (class: large-value measure + Logvinenko–Sereda/Kovrijkine): collapses to the pointwise bound. NO-GO (class:
  order-k moments with integer-spacing error): does not certify below log τ ≈ (64/e)TN; without spacing error, not
  below log τ ≈ 8T² (ARGUED, torus model).
- Remainder: (1.2) in 2T ≲ log τ < log Ω_B: OPEN; the plunge plays no special role.
- Reusable positives: Prop 1.2, Lemma 2.1, Prop 2.2, Thm 3.1, Cor 3.2, Prop 4.1.
- Next step: (1) numerical scan of m − P^ρ_T; (2) large sieve via multiplicative energy of k-fold products.
  Taken: (1) yes, ROUND_011_C; (2) no.

### 12. ROUND_011_B.md — is the high gauge quotient uniform in K? (decision test)
- Object: α_HI(K), Γ′(K), θ_K of the consistent pair with Nb ≈ 2.5K; everything NUMERICAL, nothing PROVED.
- Findings: resolution cap k_* ≈ 0.32–0.35·Nb (not 0.4·Nb); α_HI converges from below in Nb (products of 10A biased
  downwards); α_HI ≳ 3·4N/K fits everything; positive floor ≤ 0.2 (T = 0.8), not seen at T = 1.0; +1 class alone flat
  (≈ 1.9, ≈ 2.9); the decay is the mixing of classes.
- NO-GO (class: two-block Schur assembly LM/HI with block-diagonal ℓ_g normalization, NUMERICAL): θ_K → 0
  at K ≈ 4.5·4N (T = 0.8), 3.3·4N (T = 1.0) while the form stays positive (Ritz 1.3–1.5 λ_A). Uniform (HR)(a) not supported.
- Falsifiers: the high block does not see 1.01Λ (Δ < 0.1 %); a_3 rejected only on the low block.
- Next step: three-block assembly separating the class on the high block; (HR)(a) with normalization c·4N/K.
  Taken: yes, ROUND_012_B (first part).

### 13. ROUND_011_C.md — packet margin m − P^ρ_T: finite reduction, minima and direct values
- Lemma 1.1 (m strictly increasing; P^ρ_T ≤ Σ^ρ_T; (1.2)_κ holds for τ ≥ τ*_κ, log τ*_κ ≤ Σ₀ + κ + 2 ≍ 4e^T): PROVED.
- NUMERICAL: inf(m − P^ρ_T) > 0 over the whole high range for T = 0.8–2.5 (three profiles) and T = 3 (cos², bump); minimum
  0.341 (T = 2, mollified indicator); the worst centre lies just above the plunge (1.1–1.6·2πN); direct values
  W_T(f)/‖f‖² agree with m − P^ρ_T to ≤ 2.4·10⁻³; danger zone of the torus model empty for T ≲ 6.5 (the cap Σ^ρ_T
  dominates); budget in cΛ ≈ 9 % at T = 2.
- Remainder: lower bound of the margin uniform in T: not decided; T = 3 ind on [2·10⁶, 3.4·10⁸] not scanned.
- Reusable positives: Lemma 1.1 (holds for every comb v_n ≥ 0 and |ρ| ≤ 1).
- Next step: prove (1.2) on the first cells above the plunge uniformly in T. Taken: partially,
  ROUND_012_A (certified ranges and NO-GOs for a uniform proof).

### 14. ROUND_012_A.md — (1.2) above the plunge: certified range, operator form for every profile, three NO-GOs
- Lemma 1.1 (|ρ_β| ≤ 1, ≤ ½ for |u| ≥ 1, 0 for |u| ≥ 2): PROVED. Lemma 1.2 (ρ explicit and non-increasing for cos²): PROVED.
- Thm 2.1 ((1.2) for every profile, T ≤ log 2, κ = 0.069): PROVED. Thm 2.2 (profile cos², T ≤ 2.64, κ = 0.0486): PROVED
  computer-assisted (intervals).
- Prop 3.1 (sup_β P^{ρ_β}_T(τ) = λ_max(A_τ), A_τ f = ½Σv_n cos(τ log n)[f(x+log n) + f(x−log n)]1_{[−T,T]}): PROVED as a
  statement; its reading as a condition for (HR)(a) was invalidated in ROUND_015_C.
- NO-GO 4.1 (trivial bound with fixed profile: Σ^ρ_T grows exponentially): PROVED. NO-GO 4.2 (short packets of length
  o(T)): PROVED as a logical statement. NO-GO 4.3 (mean value + Sobolev/Gallagher: loss e^T√T; closed family).
  4.4 Gaussian extreme-value heuristic: ARGUED and contradicted (NUMERICAL: ind margin flat ≈ 0.355, T = 3–4.5).
- Remainder (U): there exists κ > 0 with λ_max(A_τ) ≤ m(τ) − κ for T > log 2 and 2πN(1+δ) ≤ τ ≤ 2π·exp(Σv_n + κ): OPEN (later
  reformulated with a band in ROUND_016_A). Every proof must be additively exact to O(1) on a quantity ≍ 2T.
- Reusable positives: Lemmas 1.1–1.2, Thm 2.1, Thm 2.2.
- Next step: explain the blocking sup P ≈ log(τ/2π) − 0.35 via process B/Vaughan; compute λ_max(A_τ). Taken:
  yes, ROUND_013_A and ROUND_013_B.

### 15. ROUND_012_B.md — three-block assembly LM/H₊/H₋; class structure of the coupling
- Thm 1.1 (sign conjugation: W_T(Ef, Eg) = Σa_jb_kε_jε_k𝒢_{jk}, 𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k), M = ZᵀS𝒢SZ): PROVED given (S)
  Slepian equation on the whole line CITED and (T) ROUND_001_B.
- Cor 1.2 (H₊–H₋ coupling = −Z₊ᵀ𝒢_{+−}Z₋, without a small factor): PROVED → NO-GO of every proof of smallness of that
  coupling by the selection rule or by class symmetry. Cor 1.3 (M(a₊ + a₋) = 𝒢[a₊ − a₋]): PROVED.
- Prop 1.4 (low–high coupling: form PROVED, constants ARGUED, leakage comparison CONDITIONAL).
- NO-GO (class: three-block Schur LM/H₊/H₋ with block-diagonal ℓ_g normalization, NUMERICAL): θ₃ < 0 from
  K ≈ 3·4N / 2.4·4N, worse than two blocks; cut by index range also negative (T = 1.0, K ≈ 3.2·4N).
  α₊, α₋ flat; G_{+−} grows; the form stays positive.
- Falsifiers: Thm 1.1 uses Λ (radical relation) but carries no sign; the high block does not distinguish Λ from 1.01Λ, a_3.
- Reusable positives: Thm 1.1, Cor 1.2, Cor 1.3; rule: decompose in the class-blind variable b = Sa along
  the index axis.
- Next step: band sweep of 𝒢 in b = Sa; express 𝒢_{jk} via the packet symbol. Taken: yes, ROUND_014_A.

### 16. ROUND_013_A.md — peak blocking under process B: dual Type I, complete dual = conjugate polynomial
- Object: D_w(s) = Σ Λ(n)n^{−s}w(n), w(x) = ρ(|log x|/T), P^ρ_T = 2Re D_w(½+iτ); Λ = μ∗log.
- Lemma 1.1 (above 2πN(1+δ) each Type I sum is its Poisson dual with frequencies j ≥ m(1+δ); the term j = 0 is
  O(τ^{−K})): PROVED (second order CITED); NUMERICAL check 3.5 %.
- Prop 2.1 / (2.2) (P^ρ_T(τ) = 𝒜_w(½+iτ) + R_w(½+iτ) exact via Mellin and the functional equation of ζ′/ζ; dual = conjugate
  polynomial by parity of the profile): PROVED. Lemma 2.2 (𝒜_w = m(τ) + O(T^{−2}τ^{−2}); polar part O(e^T(Tτ)^{−k})): PROVED.
- Reading: (U) for a profile ⟺ R_w(½+iτ) ≤ −κ + O(τ^{−2}) (reformulation); the blocking 0.355 = inf R_w.
- Prop 3.1 NO-GO (class 𝒱: Vaughan/Heath-Brown/μ∗log + Poisson/van der Corput process B for P^ρ_T at τ ≍ 2πN):
  structure PROVED, size ARGUED: either it reproduces (U) literally or it loses more than the budget ≈ 0.35/(2T).
- Reusable positives: Lemma 1.1, Prop 2.1, Lemma 2.2.
- Next step: leave the summation methods; compute λ_max(A_τ) and look for a positivity structure of m(τ)I − A_τ as a
  cell operator. Taken: the computation yes (ROUND_013_B); the positivity structure no.

### 17. ROUND_013_B.md — direct computation of λ_max(A_τ)
- Everything NUMERICAL; nothing PROVED; reusable tool: exact closed matrix elements of Sh(s) in the sine basis.
- Reported: margin m − λ_max = 0.668, 0.311, −0.504, 0.273, 0.255, 0.114 at T = 0.8, 1.0, 1.5, 2.0, 2.5, 3.0 (Nb = 400);
  cΛ budget: crossing at c ∈ (1.05, 1.10) at T = 2, (1.00, 1.05) at T = 3. Nodal discretization with interpolation
  discarded (diverges by aliasing).
- Later correction (ROUND_015_C): the positive values at T ≥ 2 were basis truncation artefacts
  (Nb·π/2T < τ); with Nb = 800, T = 2 gives −1.71.
- Next step: fine mesh in T ∈ [1.2, 1.8]; falsifiers (b), (d) at T = 1.5. Taken: the mesh in T yes (ROUND_015_C,
  [1.40, 1.60]); the falsifiers no.

### 18. ROUND_014_A.md — class-blind tail Gram on the high block; sweep along the index axis
- §1.0 (u_k = ε_kψ_k(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}); 𝒢 entry by entry is not defined on raw prolates; domain
  S{f(λ) = 0}): PROVED.
- Thm 1.1 (M ⪰ 0 on 𝒜 ⟺ 𝒢 ⪰ 0 on S𝒜; generalized minima with D and ℓ_g^S = Sℓ_gS): PROVED. Prop 1.2 (S𝒜 ≠ 𝒜; principal
  cosines up to 0.135): PROVED in form, NUMERICAL in size. Cor 1.3 (one-sided transfer): PROVED.
- Thm 3.1 (Toeplitz/band sweep bound with explicit error): PROVED (linear algebra).
- Prop 3.2 NO-GO (class: lower bounds by symbol on the prolate index axis + band/Toeplitz error in
  D normalization; NUMERICAL): D bottom on S𝒜 → 0 with K (0.98 → 0.015), near-null direction = gauge (blind to the comb),
  band without decay (0.3–0.55 at shifts 8–16), Gershgorin −5.7/−8.4. The tails above the plunge are chirps,
  not packets (ARGUED).
- Falsifiers: D collapse and gauge alignment survive 1.01Λ and a_3: they carry no arithmetic.
- Reusable positives: §1.0, Thm 1.1, Cor 1.3, Thm 3.1.
- Next step: exact quotient by the gauge before sweeping; test whether the long-range band is the correction of the
  radical; mollified data. Taken: yes, ROUND_015_A.

### 19. ROUND_015_A.md — high block in the gauge quotient; mollified tail Gram; chirp ledger of the comb
- Lemma 1.0 (two forms agreeing in codim r differ by rank ≤ 2r): PROVED. Prop 1.1 (tail Gram entry by
  entry on mollified data; SM^ρS − 𝒢^ρ of rank ≤ 8, invisible on the compatible subspace): PROVED given (S), (T).
- Thm 3.1 (comb on Poisson tails = 2⟨𝒯_log u, 𝒯u⟩, Λ ∗ 1 = log; = prime collapse already recorded): PROVED
  (used, not claimed). Domain remark: raw obstruction = Σ log N/N = ∞: PROVED.
- Cor 3.2 (exact ledger: diagonal B_{NN} = (⟨m⟩_N − 2log N)‖F_N‖²; the comb is resonant, it does not average out): PROVED.
- Thm 3.3 (non-resonant pairs via the generalized Hilbert inequality of Montgomery–Vaughan in the
  dilation model, explicit constants): PROVED. Cor 3.4 (criterion (C): ⟨m⟩_G − log X ≥ κ with long sweep relative to the number
  of chirps): PROVED in the model. §3.5 WKB margin ≈ 2T + 1/(p−1): ARGUED.
- Hypothesis FALSIFIED (NUMERICAL): «the constant-sign long-range band is the finite correction of the radical».
- NUMERICAL: bottom of the gauge quotient does not stabilize (2.64 → 1.63; 3.08 → 2.27); collapse beyond K ≈ 0.3·Nb is
  an artefact; diagonal Ĝ_kk − m(k) nearly independent of k; boundary kernel explains only the low part of the band.
- Falsifiers: criterion (C) survives c < 1, a_P, small (d): it is not a sign step; the high block rejects c > 1
  only asymptotically (k ≈ e^{290} for c = 1.01).
- Remainder: transfer from the dilation model to truncated tails (G_N depends on N); WKB localization; passage from single
  profiles to oscillating combinations of neighbours: OPEN. PIVOT.
- Reusable positives: Lemma 1.0, Prop 1.1, Thm 3.1, Cor 3.2, Thm 3.3, Cor 3.4.
- Next step: build tails via the spherical Legendre–Bessel formula, chirp matrix B_{NN′} of the bottom vector,
  separate diagonal / non-resonant / jump at x = −T; layered version of Thm 3.3. Taken: no.

### 20. ROUND_015_B.md — low block: what the half-line identity leaves, nested cancellations, where the falsifiers die
- §1.1 (the identity leaves the complete form with the complete comb; on tails the comb collapses to log N): PROVED
  (assembled). (1.2) entries 𝒢_{jk} of the low block: PROVED; case f(λ) ≠ 0 as a mollified limit: ARGUED.
- (1.3)–(1.4) Langer/WKB principal form, κ₈ ≈ ½[D(N) + R_{88}]a_8²/‖Ef_*‖²: ARGUED. The bottom carries f(λ) ≠ 0 (boundary
  channel at leading order): ARGUED.
- §2.1: the low block sees neither near-coincidences nor atoms log n > T; it sees divisor sums of the first cells and resonant
  pairs (1, n): structure PROVED, sizes ARGUED. §2.2 harmonic constant (f(λ)²/(12λ))(2T + 0.430): ARGUED.
- §3.1 identity (3.1) Π_T(Ef) = 𝒜_∞(Ef) + 2A(Ef)B(Ef) − 𝒲[Ψ_f] (first cancellation O(1) → O(d_8)): PROVED.
- Lemma 3.1 (𝔴_N(ω) ≥ 2T·H(ω) ≥ 2T; ≥ 2T + log 2 on the caustic layer): PROVED.
- §3.3 first uncancelled term positive for T ≥ log 2: ARGUED. §3.4 that term is positive for all c < 1 and
  c − 1 ≲ T, survives a_P and small (d): PROVED (algebra) → not a sign step.
- §3.5 the sign at order d_8 is decided by the Schur competition «ledger (+, robust) minus coupling 𝒲(Ψ_{f*}, ·)»
  (removes 33–40 %): NUMERICAL + ARGUED. §4.2 two-threshold law at T = 1: c > 1 dies at first order (≈ 7·10⁻²²),
  c < 1 at second order (≈ 1.5·10⁻⁴): NUMERICAL; fails at T = 1.2.
- PIVOT: there is no sign step in the low block alone.
- Reusable positives: §1.1, (1.2), (3.1), Lemma 3.1, §4.1 (under cΛ the defect is (1−c)Π_T(Ef) in the window).
- Next step: isolate the coupling 𝒲(Ψ_{f*}, ·) at T = 1 (archimedean, collapsed comb, Tate parts) and look for
  an identity of type (3.1) for the pair (f_*, g) with falsifiers c = 1 ± 10⁻⁴, a_3. Taken: no (outside the range).

### 21. ROUND_015_C.md — the violation at T = 1.5 of λ_max(A_τ) ≤ m(τ): real for the operator, artefact for the form
- Everything NUMERICAL; nothing PROVED.
- Findings: −0.504 real for the operator (≤ −0.511 at Nb = 1000), negative on all T ∈ [1.40, 1.60] and at T = 2.0
  (−1.71 with Nb = 800); the positive values of 013B at T ≥ 2 were artefacts. The maximizer oscillates at frequency τ
  (99.95 % of ‖f̂‖² above τ/2): outside the validity of the packet reduction. Direct W_T on the projected function:
  +0.79 (T = 1.5), +1.05 (T = 2.0). Restricted to envelopes with band |ξ| ≤ τ/4: margin +0.46 to +0.72.
- NO-GO: the unrestricted operator form «λ_max(A_τ) ≤ m(τ)» of 012A Prop 3.1 is false and is not a valid condition
  for (HR)(a). λ_A(1.5) to 30 digits: not resolved.
- Next step: restate Prop 3.1 with band restriction |ξ| ≤ ητ, η < ½, and recompute. Taken: yes, ROUND_016_A.

### 22. ROUND_016_A.md — band-restricted packet reduction; envelope margins T = 1–3; λ_A(1.5) to 150 digits
- Object: V_η(τ) = span{e_k : a_k ≤ ητ}, A_τ^{(η)} = Π_ηA_τΠ_η; free form Q_T on L²[−T, T].
- Thm 1.1 (exact identity: Q_T(β cos τx) = ½[m(τ)‖β‖² − ⟨A_τβ, β⟩] + ½[D_τ + X_τ − R_τ]): PROVED.
- Lemma 1.2 (ê_k closed; leakage |β̂(ξ)|² ≤ (8/π)η³τ³‖β‖²/(ξ² − η²τ²)²; L(η, θ)): PROVED. Lemma 1.3 (i) m even and increasing:
  PROVED; (ii) Stirling: CITED + NUMERICAL; (iii) |m(s)| ≤ 5.38 + log(1+s): CITED + NUMERICAL.
- Prop 1.4 (curvature D_τ ≥ −‖β‖²d(η, θ, τ)): PROVED given 1.3(ii). Prop 1.5 (|X_τ| ≤ √(2L₁)(5.72 + log τ)‖β‖²,
  |R_τ| ≤ 2√L₁Σv_n‖β‖²): PROVED. Thm 1.6 (Q_T(f) ≥ ½‖β‖²[m(τ) − ⟨A_τ^{(η)}β, β⟩/‖β‖² − E]; condition (HB_η)
  λ_max(A_τ^{(η)}) ≤ m(τ) − κ − E): PROVED. Transfer from Q_T to W_T in P_T: norm correction PROVED, form correction ARGUED.
- Failed: E is not small (2√L₁Σv_n ≍ e^T; at T = 2, η = ⅛: E ≥ 1.55 against margin 0.28): Thm 1.6 does not certify (HB_η).
  Cause: Cauchy–Schwarz loads each comb term with the whole leakage of the boundary layer.
- NUMERICAL: band margin 0.888 / 0.544 / 0.280 / ≤ 0.256 / ≤ 0.114 (η = ⅛, T = 1, 1.5, 2, 2.5, 3), decreasing,
  linear extrapolation crosses zero near T ≈ 3.3 (warning, not a result); c* → 1 (1.072 at T = 2, ≤ 1.022 at T = 3);
  direct W_T agrees to ≤ 0.002. λ_A(1.5): all Galerkin values positive, ≤ 5.1·10⁻⁸³ (N = 160), not converged.
- Remainder: sharp cross-term lemma; complete range at T = 2.5, 3, and T = 3.5: OPEN.
- Reusable positives: Thm 1.1, Lemma 1.2, Lemma 1.3(i), Prop 1.4, Prop 1.5, Thm 1.6 (every real comb; with signed
  weights, Σ|v_n|).
- Next step: (i) sharp lemma for R_τ by integration by parts against the phase 2τ, or class β = χ·γ with smooth cutoff;
  (ii) complete τ at T = 2.5, 3 and T = 3.5 with a matrix-free routine; (iii) λ_A(1.5) with N = 200–240. Taken: outside the range.

---------------------------------------------------------------------------------------------------

## A. Deduplicated «do not retry» (with reopening condition) and cross-check with RULES_AVOID.md

Key: [ABSENT] not in RULES_AVOID.md; [INACCURATE] present with a statement that does not match; [PRESENT] present correctly.

A1. Sign mechanisms based only on identities that also hold for a_3 or the system 3 → 3.2 (Λ∗1 = log,
    Selberg, Euler factors, Lévy identity), at T ≥ ½log5 + 10⁻⁴ — NO-GO PROVED (007C). Reopening: an argument that
    fails on a_3 and on 3 → 3.2. [PRESENT in essence: B1/§E; the PROVED certificate is not mentioned.]
A2. Simply exponential laws cT^a e^{−bT} for λ_A (007D) — NO-GO NUMERICAL. [PRESENT via B8 «law on a bounded
    range».]
A3. Lower half of the two-sided law λ_A ≥ L(T)(1 − o(1)): equivalent to (N1′) μ₁ ≥ L with margin exp(−4πe^{2T}); it is not
    weaker than (★); transfer from λ_W only gives floors 10⁵–10⁷ weaker (007D). Reopening: a positive floor for μ₁ with
    sensitivity to relative perturbations of size L(T). [INACCURATE] RULES_AVOID §F: «Two-sided laws λ_A = L(T)(1+o(1))
    on unbounded ranges (P47 rem:bar-fam)» appears as non-excluded ground, without warning that its lower half is (★) plus
    a margin (007D Lemma 4.6/Cor 4.7; 008E Conj 4.1).
A4. «λ_A ≥ λ_W − capacity» as a transfer tool — REFUTED (007D Prop 4.2, 2×2 model). [ABSENT]
A5. Sign capture on the family of comb responses E_T alone (Rayleigh on E_T) — PIVOT/NO-GO NUMERICAL (007E): fails
    by 13–31 orders. Reopening: control of the Schur coupling. [ABSENT] (D17 cites «Λ-free planes E_k», a different object.)
A6. Finite-degree Neumann truncation of the Schur coupling (archimedean band B_t of 008A or family E_T of 008D),
    with tail by spectral radius — NO-GO (008D): degree ∝ log(1/λ_A)/log(1/r); unsigned terms, low even truncations
    with the wrong sign; Chebyshev only changes the constant. Reopening: signed resummation of the terms k on V.
    [ABSENT]
A7. Grönwall in the window variable T (D ≤ Cλ, (EB_C), (VE_C)) — NO-GO as a reformulation (008C Prop 5; class 𝒦_H):
    with unspecified C it is (★) + Lipschitz, every falsifier fails by its own sign; with C = 8πe^{2T} it is the lower
    half of the law. «Do not retry Grönwall with another denominator». Reopening: (EB_C) proved from the boundary traces
    θ_± with its own mechanism. [INACCURATE] RULES_AVOID C1 only names «L♯ programme (exterior form, Grönwall, …)» (frequency
    variable); the version in T, the identity of constants 8πe^{2T} = 2 in c and the discrete Grönwall do not appear.
A8. Upper half of the law with a single test function PEψ_0 — NO-GO NUMERICAL (008E). [ABSENT]
A9. Class–parity selection rule (Poisson intertwines ℱ with the reflection R) as a source of sign, and as a proof of
    smallness of the H₊–H₋ coupling — NO-GO (009B §3.1 Λ-free; 012B Cor 1.2 PROVED: coupling without a small factor).
    [PARTIAL] C1 «Sonin, prolates, semilocal as source of sign»; the impossibility of smallness by class does not appear.
A10. Reading «decay of α_HI through near-gauge vectors» — WITHDRAWN (010A); pair of 9B (P_+Π_TEψ_k against D without
    admissibility) inconsistent. [ABSENT]
A11. High-block estimates that see the comb only through its total mass (class 𝒦_S, including lem:ext-hf) — NO-GO PROVED
    (010A Prop 3.2–3.3): negative at every frequency ≤ e^{S−C}; lem:ext-hf empty at polynomial indices. Reopening:
    use the dispersion of Λ over n < N (S₂, integer spacing). [ABSENT]
A12. Large-value measure of P_T + Logvinenko–Sereda/Kovrijkine uncertainty — NO-GO (011A Prop 2.2): collapses to the
    pointwise bound. [ABSENT]
A13. Order-k moments with integer-spacing error — NO-GO: does not certify below log τ ≈ (64/e)TN; torus model blind
    below 8T² (ARGUED) (011A). Reopening: arithmetic correlations between cells (near-coincidences of k-fold products).
    [PARTIAL] B2 «large sieve and quadratic mean»; the threshold and the reopening condition do not appear.
A14. Two-block Schur assembly LM/HI and three-block LM/H₊/H₋ (and cut by index range) with block-diagonal ℓ_g
    normalization — NO-GO NUMERICAL (011B, 012B): θ → 0 while the form stays positive. Reopening: decomposition
    in the variable b = Sa cut along the index axis with a controlled coupling. [PRESENT] D17 «two- and three-block
    assemblies» (without the range variant or the condition).
A15. (HR)(a) as a constant uniform in K — not supported (011B: α_HI ≳ 3·4N/K). Reopening: K-dependent normalization.
    [ABSENT]
A16. Trivial bound P^ρ_T ≤ Σ^ρ_T with fixed profile; short packets of length o(T); mean value + Sobolev/Gallagher for the
    pointwise bound — three NO-GOs (012A §4); every method that loses a multiplicative constant is excluded (budget
    ≈ 0.35/(2T)). [PARTIAL] B2 covers «quadratic mean»; 4.1 and 4.2 are absent.
A17. Gaussian extreme-value heuristic for P^ρ_T — contradicted by the data (012A §4.4; 011C §4(ii)). [ABSENT]
A18. Class 𝒱 (Vaughan/Heath-Brown/μ∗log + Poisson/process B) for P^ρ_T at τ ≍ 2πN — NO-GO (013A Prop 3.1): reproduces (U)
    or loses more than the budget; the constant lives in R_w. Indicated: «leave the summation methods on the polynomial».
    [PRESENT] D17 «process B / Vaughan» (without identity (2.2) or the scope).
A19. Unrestricted operator form λ_max(A_τ) ≤ m(τ) − κ (sup over every L² profile) — FALSE (015C; violated at T = 1.4–1.6
    and 2.0) and not a valid condition for (HR)(a); the positive values of 013B at T ≥ 2 were artefacts. Reopening: only
    with envelope band |ξ| ≤ ητ, η < ½ (016A). [ABSENT]
A20. Lower bounds of the high block by symbol on the prolate index axis + band/Toeplitz/Gershgorin error in
    D normalization — NO-GO NUMERICAL (014A Prop 3.2). Reopening: exact quotient by the gauge and comparison with the archimedean
    average along chirps. [ABSENT]
A21. Identification «tails above the plunge = packets» (packet symbol as index symbol) — fails, they are chirps
    (014A, ARGUED). [ABSENT]
A22. Hypothesis «the constant-sign long-range band of the tail Gram is the finite correction of the radical/polar» —
    FALSIFIED (015A §1.3). [ABSENT]
A23. «The high block is controlled by averages of the comb along chirps» — CORRECTED (015A): the comb does not average out, it
    collapses to the resonant weights log N; mean values only control the non-resonant remainder. [ABSENT]
A24. Sign from the high block (any form) — excluded by rule 4: every falsifier is rejected only on the low block
    and its coupling (010A §5, 011B, 012B §3, 014A §4, 015A §4). [ABSENT]
A25. Sign step on the low block alone (first uncancelled term, second cancellation log² against log²) — PIVOT (015B):
    positive for robust reasons (survives c < 1, a_P, small (d)). Reopening: exact inequality in the comb on the
    coupling 𝒲(Ψ_{f*}, ·). [ABSENT]
A26. Premise «the tail of the low block sees the atoms log n > T / the near-coincidences» — false (015B §2.1). [ABSENT]

Cross-check of a statement of RULES_AVOID.md against these files:
- B2 says: «For T ≥ 1 the margin is ≤ 4·10⁹Te^{−15.449T}; every bound with a remainder loses more». [OUTDATED] 009A Cor 7.1
  proves (given thm:ext-half and a cited non-asymptotic bound) λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πe^{2T}} for N ≥ 1.6·10⁶, and 007D
  §2(iii) records that the 15.449 bound is uninformative over the whole resolved range; the relevant margin is doubly
  exponential.
- B8 says «determinant or moment of the frame» and B2 «quadratic mean»; 011A §0(i) and 015A §0 specify that mean values and
  moments are legitimate for the O(1) coercivity of the high block and for the non-resonant remainder, never for the sign. The
  sentence in RULES_AVOID does not distinguish these uses.

## B. PROVED positive results (statement and scope)

B1. Lemmas 1–3 of 007C: witness bound, invariance under extension by zero (every comb), closed evaluation of the
    Lévy form on Dirichlet sines; certificates λ_A ≤ −0.505 (a_3), −0.234 (3 → 3.2) at T ≥ ½log5 + 10⁻⁴, −0.078 (1.1Λ) at T ≥ 1.
B2. Sandwich λ_W^par ≤ λ_A^par ≤ λ_{W,2}^par; floors λ_A ≥ 2^{−1518} (T ≤ ½log12), ≥ 2^{−2904} (T ≤ ½log15) with cited inputs
    (007D Prop 4.1, Cor 4.3).
B3. Exact secular form of the lower half (Lemma 4.6) and reduction to an unrestricted eigenvalue μ₁ with Tate moment
    τ₁ (Cor 4.7), even sector with n₋ = 1 (007D).
B4. Exact band reduction (★)_T ⟺ S_T ⪰ 0 with spectral band of Arch and t_c > π_+; Neumann series with homogeneous
    degrees and two-sided tail (008A Thm 2.1, 3.1, Cor 3.2); valid for every Galerkin compression.
B5. One-sided variation formula with Tate multipliers and fold; 𝒱^♯ ≥ 0; boundary-strip inequality
    (Prop 3, minimizers bounded near ±T); discrete Grönwall on increments (008C Thm 1, Cor 2.2, Prop 3, Prop 4);
    m′ ≥ 0 on [0, ∞) (Lemma 1.2).
B6. a_CE = Arch_CE − Π_CE P_V (008D Prop 1); Neumann expansion on E_T^c under (H₋) (Thm 2).
B7. Exterior upper bound W_T(Ef) ≤ Kλ^{−2}(L₁² + L₂²), K = 141, on 𝒜⁺_T; index count 5/3; identity
    W^w_T(Ef) = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef]; zero robustness of the law (008E Thm 3.1, Prop 3.3, (5.1), Prop 5.1; 009A §7.2).
B8. Prolate lemmas 2.1–2.3, Lemma 3.4′ (weighted leakage ≤ C_dN⁹(1 − χ_{2d−2}), N ≥ 1.6·10⁶), and explicit upper bound
    λ_A(T) ≤ 3.2·10²³N^{33/2}e^{−2πe^{2T}} (009A, given thm:ext-half and a cited non-asymptotic bound).
B9. Exact parity defect P_{−ε}Π_TEf = ½RΠ_TE(ℱf − εf); diagonal Fourier defect on prolates; decoupling of classes
    with cross terms ≲ poly(N)√(d_jd_k) (009B Thm 1.1, 1.2, 1.5, Lemma 1.3, 1.6, Prop 2.2). Λ-free.
B10. Symbolic form in the window W_T(g) = (1/2π)∫(m − P_T)|ĝ|² + 2AB; L² Markov; lem:ext-hf empty at polynomial degree;
    cross prolate overlaps ≡ 0 (010A).
B11. Necessity of the pointwise packet bound for every coercive (HR)(a); vacuity of P^ρ_T ≥ ϑm above Ω_B, log Ω_B =
    (64/(eϑ²))Te^{2T}(1+o(1)), and coercivity ≍ TN for data above Ω_B; sup P^ρ_T ≥ c₁T for Ω ≥ N² (011A).
B12. Finite high range: (1.2)_κ holds for τ ≥ τ*_κ, log τ*_κ ≤ Σ₀ + κ + 2 (011C Lemma 1.1, every comb v_n ≥ 0).
B13. (1.2) over the whole high range for every profile if T ≤ log 2 (κ = 0.069) and for cos² if T ≤ 2.64 (κ = 0.0486, intervals)
    (012A Thm 2.1, 2.2).
B14. Sign conjugation M = S𝒢S with 𝒢 a class-blind Gram of exterior tails; exact transfer to the subspace
    S𝒜; domain S{f(λ) = 0}; Toeplitz/band sweep lemma (012B Thm 1.1, Cor 1.2–1.3; 014A §1.0, Thm 1.1, Cor 1.3, Thm 3.1).
B15. P^ρ_T(τ) = 𝒜_w + R_w exact with 𝒜_w = m(τ) + O(T^{−2}τ^{−2}); Type I sums above the plunge are purely dual (013A).
B16. Tail Gram entry by entry on mollified data (rank ≤ 8 correction); collapse of the comb on Poisson
    tails to log N; exact diagonal ledger (⟨m⟩_N − 2log N)‖F_N‖²; Montgomery–Vaughan control of non-resonant pairs with
    constants; criterion (C) in the dilation model (015A).
B17. Identity (3.1) Π_T(Ef) = 𝒜_∞(Ef) + 2A(Ef)B(Ef) − 𝒲[Ψ_f] on admissible data; 𝔴_N ≥ 2T·H ≥ 2T (Lemma 3.1);
    under cΛ the defect is (1−c)Π_T(Ef) in the window (015B).
B18. Exact packet identity Q_T(β cos τx) = ½[m(τ)‖β‖² − ⟨A_τβ, β⟩] + ½[D_τ + X_τ − R_τ]; leakage of V_η;
    curvature ≥ −η²/(2(1−θ²)) − …; band reduction (HB_η) (016A Thm 1.1, Lemma 1.2, Prop 1.4–1.5, Thm 1.6; every real comb).

## C. Open obligations (mathematical statement and what was attempted)

C1. (N1′) μ₁(T) ≥ L(T), L ≈ exp(−4πe^{2T}), μ₁ second even eigenvalue of a_T without restriction, with τ₁² ≤ ηL·D(L). Attempted:
    sandwich with λ_W, cluster, polar capacity (007D). OPEN.
C2. (EB_C): 𝔈_h(F*_{T+h}) ≤ C(T)hλ_A(T+h)(1 + o(1)), C(T) = 8πe^{2T}(1+o(1)), T ≥ ½log5. Attempted: Danskin, virial,
    Hellmann–Feynman (008C). OPEN; Hadamard form via boundary traces ARGUED.
C3. Signed resummation of the series Σ_k W*X^kW on V_T, or a degree bound independent of λ_A; (H₋): Arch_CC + Π_CC ≻ 0 on C
    (008D). OPEN.
C4. Conj 4.1 (008E): λ_A(T) ≥ κ₋(1 − χ_8(2πN)); via prob:ext-L (Prop 4.2) or polynomial conditioning κ_C(T) (Lemma 4.3). OPEN.
C5. (HR)(a)/(HR)(b) in the consistent pair: inf_{HI} W_T/ℓ_g ≥ κ_H·(normalization, e.g. 4N/K) and Γ′² ≤ (1−η)κ_LMα_HI.
    Attempted: Schur with 2 and 3 blocks, range, index sweep, gauge quotient (009B–015A). OPEN.
C6. (HR-Π): M|_{𝒜(Π_ε)} ≥ κ_Π·D_g|_{𝒜(Π_ε)} on the plunge (dimension O(log N·log(1/ε))) (010A §3.4(iii)). Stated, neither
    proved nor computed.
C7. Pointwise bound (1.2)/(U): P^ρ_T(τ) ≤ m(τ) − κ on 2πN(1+δ) ≤ τ ≤ τ*_κ uniformly in T (with band: (HB_η)). Attempted:
    trivial bound, large values, Kovrijkine, moments, MV+Sobolev, process B/Vaughan, operator without band (011A–016A).
    OPEN; certified only for T ≤ log 2 (every profile) and T ≤ 2.64 (cos²).
C8. Sharp cross-term lemma: |R_τ(β)| ≤ C(η)Σv_n/τ^{1/2} + (small boundary-layer term) for β ∈ V_η, or a
    class of envelopes with o(1) leakage (016A). OPEN.
C9. Transfer of Thm 3.3 / criterion (C) from the dilation model to truncated tails (G_N = G1_{(−∞,−T−log N)}); WKB
    localization; passage to oscillating combinations of neighbours that realize the bottom in X (015A §3.6). OPEN.
C10. Coupling of the survivor: sup_G |W_T(Ef_*, G)|²/(‖Ef_*‖²a_T(G)) bounded by (1 − η)·ledger, through an
    exact identity in the comb of type (3.1) for pairs (f_*, g) (015B §3.5). OPEN; this is where c < 1 is rejected and where
    a sign step must act.
C11. Convergence of the mollified limit for f(λ) ≠ 0: uniform bound on Σ_{N>X} log N⟨F_N, 𝒯u⟩ (015B §1.2). OPEN.
C12. Θ_T(w) < 0 certified for a_3 and 3 → 3.2 by covering in μ (007C §3.2). OPEN, not attempted.
C13. Transfer Q_T → W_T in P_T for β ∈ V_η at the level of the form (016A). ARGUED.

## D. Objects, steps or ideas named and not taken up

D1. Certification of Θ_T(w) < 0 by two witnesses F_± (007C).
D2. Bound on μ₁ with Hellmann–Feynman sensitivity dμ₁/dc = Π_T(e₁) and the test of the sign of Π_T(e₁) − Arch(e₁) (007D).
D3. Measurement of 𝔈_h/h with a basis that resolves the boundary ((log 1/(T∓t))^{−1/2} or Jacobi weights) and the law λ_A ≍ θ²e^{−2T}/(8π)
    on two numbers per window (008C).
D4. Chebyshev/minimax resummation of 1/(1−x) on [−r_−, r_+] (008D).
D5. The numerical §4 of 008A (degree in v that rejects 1.01Λ) does not appear in the file read.
D6. Lower N₀ and b in Lemma 3.4′: sup|φ_k| ≤ C(k)c^{1/4} via Sonin function and Airy scale; exact 1/s decay of Φ_a′ (009A).
D7. Measure κ_C and ‖Gram(h)‖ to make (2.1) explicit — measured in 010A but the route was replaced by μ; the form
    (HR-Π) of the plunge was never computed (010A).
D8. Large sieve for P^k on [Ω, 2Ω] counting near-coincidences of k-fold products via multiplicative energy (011A step 2).
D9. Scan of T = 3 (ind) on [2·10⁶, 3.4·10⁸] (011C).
D10. Positivity structure of m(τ)I − A_τ as a cell operator (Toeplitz symbol of the comb tail at
    Dirichlet frequencies) (013A).
D11. Falsifiers (b) a_P, (c) Beurling, (d) finite modification on λ_max(A_τ) and on (HB_η) (013B, 016A).
D12. Construction of tails via the spherical Legendre–Bessel formula, chirp matrix B_{NN′} of the bottom vector, separation
    diagonal / non-resonant / jump at x = −T; layered version of Thm 3.3 (015A).
D13. Isolate 𝒲(Ψ_{f*}, ·) at T = 1 by parts (archimedean, collapsed comb, Tate) and look for an identity of type (3.1) for pairs (015B).
D14. Validate the two-threshold law of falsifiers outside T = 1 (fails at T = 1.2, cause not verified) (015B).
D15. Matrix-free routine for λ_max(A_τ^{(η)}) at T = 3.5 (K ≈ 2000) and decision on the margin crossing near T ≈ 3.3;
    λ_A(1.5) with N = 200–240 (016A).
D16. Measurement of the bound of Lemma 1.3(iii)/(HB_η) with τ-dependent η; envelopes β = χ·γ with smooth cutoff (016A).

## E. Coverage

Files in the range ROUND_007_C.md … ROUND_016_A.md according to `ls *.md | sort`: 22. Read completely: 22 (ROUND_007_C, 007_D,
007_E, 008_A, 008_C, 008_D, 008_E, 009_A, 009_B, 010_A, 011_A, 011_B, 011_C, 012_A, 012_B, 013_A, 013_B, 014_A, 015_A, 015_B,
015_C, 016_A). No file or stretch left unread. Remark: ROUND_008_A.md ends at Obs. 3.3 (127 lines) without a numerical §4
or Result / Next step sections, although ROUND_008_D cites numerical results from it; what was read is everything the file
contains. In addition, RULES_AVOID.md, OBJECT_SPEC.md and STATEMENT_001.md were read as reference.
