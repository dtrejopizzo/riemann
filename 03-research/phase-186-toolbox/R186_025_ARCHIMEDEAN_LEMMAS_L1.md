# R186_025 — Archimedean lemmas for (L1): low-pass leakage on 𝒱_k (PROVED), single window (PROVED), coupling = π (PROVED); the operator-norm route is NO-GO and is rewritten

Phase 186. Sources: R186_024 (decomposition 𝒱_k ⊕ E_k, pieces (P1)/(P2)), R186_104 (audit: ‖𝒦₁‖ = π, prime bound 1.674), R186_019, R155_026, Paper 46 (thm:A eq:Aform, lem:K, thm:S(iii), lem:mbounds). Standalone scripts: `r025_p1_lowpass.py` (imports `r024_schur.py`), `r025_coupling_norm.py`.
Notation: I_T = (−T,T), equal blocks B_1,…,B_k of half-length τ = T/k; 𝒱_k = ⊕_B {F_B ∈ L²(B): ∫_B F_B e^{±x/2} = 0}; 𝔞_∞(F) = C₀‖F‖² + ∫₀^∞(‖F‖² − 𝒞F(u))K(u)du = (1/2π)∫ m|F̂|², m(s) = Re ψ(¼+is/2) − log π, K = 2e^{−u/2}/(1−e^{−2u}), C₀ = ψ(¼) − log π = −5.3722 (lem:K, thm:A). c_∞(τ) = inf 𝔞_∞ over the single window 𝒫_τ. It is stated explicitly whenever something is NUMERICAL.

## 0. Verdict

1. **(P2) is false and is now closed: ‖𝒦₁‖_{𝒱_k} ≥ π for every k ≥ 2 and every T (PROVED, §3, argument + explicit Weyl sequence; an adjacent pair gives exactly π).** This independently confirms R186_104 §3 5b. The 0.74 of R186_024 is what degree-<10 polynomials see: Legendre Galerkin on an adjacent pair gives 0.98/1.33/1.70/1.98/2.19 for N = 6/10/20/40/80, with no saturation (NUMERICAL, `r025_coupling_norm.py`).
2. **(P1) PROVED with an explicit constant** (§1, Theorem A): c_∞(τ) ≥ log(1/τ) − C_A(τ), C_A(τ) ≤ 1.29 for τ ≤ 0.1 (1.20 at τ = 0.02, 1.24 at 0.0619). The true value is log(1/τ) − 0.510 (NUMERICAL, five points; Galerkin N = 14 and 20 agree to 4 digits). Slack 0.7, entirely in the double Poincaré inequality of the proof.
3. **The rewrite that saves (L1) is not a relative bound on the coupling but a direct bound on 𝒱_k that does not separate diagonal from coupling** (§2, Theorem B, PROVED): for every F ∈ 𝒱_k,
 𝔞_∞(F) ≥ (log(1/τ) − C_B(τ))‖F‖², C_B(τ) ≤ 1.74 for τ ≤ 0.1 (1.66 at τ = 0.02, 1.70 at 0.0619).
 Mechanism: 𝒱_k is high-pass (two Tate moments per block of length 2τ ⟹ Fourier mass at |s| ≤ θ/τ is at most cosh²τ (θ²+τ²/4)²/6) and m is increasing with m ≥ C₀ finite. This is exactly what R186_104 §3 row 6 calls "trivially coercive high-pass", now with a constant. The requested relative bound (𝒦₁ ≤ θ·diag as forms) exists numerically with θ ≈ 0.22 (NUMERICAL, slowly increasing in N: 0.206/0.218/0.222 for N = 8/12/16, §3.3) but **is not needed**: Theorem B surpasses it because the Weyl sequence giving π has diagonal energy ~ M²/2 per mass M.
4. **(L1) is now PROVED in the form** c(T,k) := min 𝔞_T|𝒱_k ≥ log(k/T) − C_B(T/k) − ‖P|𝒱_k‖, with ‖P|𝒱_k‖ ≤ 𝒜_T (Cauchy–Schwarz, PROVED) and ≤ 𝒜_T/2 for T ≤ log 2 (R186_104 3a/3b); with the bound 1.674 from R186_104 for T ∈ (log 2, ½log5] (CITED from 104, not re-verified here): positive with k ≥ 12 for T ≤ 0.69 and k ≥ 25 at ½log5 (k = 26: margin 0.13; k = 30: 0.27). With the trivial bound 𝒜_T = 2.94 at ½log5, k ≥ 85 is needed. All of this is PROVED but it is high-pass coercivity, and **what remains OPEN for D is entirely (L2)**: S_T ≻ 0 in dimension 2k − 2 (≈ 50 at ½log5), which, as R186_104 notes, is W ≥ 0 rewritten in the basis of piecewise Tate exponentials and inherits the full thm:margin decay. No sign claim. **Route "(L1) via operator norms" (c_∞ − ‖𝒦₁‖ − ‖P‖): explicit NO-GO** (it would require c_∞ > π + 1.674, k ≈ 160); replaced by Theorem B.

## 1. Theorem A — single window (PROVED)

**Lemma 1.1 (K ≥ 1/u on (0, 1.5]).** K(u) − 1/u = (u − 2sinh(u/2))/(2u sinh(u/2)) + 1/(2cosh(u/2)). Since 2sinh(u/2) ≤ u cosh(u/2) (tanh x ≤ x) and sinh(u/2) ≥ u/2, the first term is ≥ −u cosh(u/2)/8, and K − 1/u ≥ 1/(2cosh(u/2)) − u cosh(u/2)/8 ≥ 0 if u cosh²(u/2) ≤ 4, which holds on (0, 1.5] (cosh²(0.75) = 1.68). ∎

**Lemma 1.2 (tail).** ∫_{2τ}^∞ K = log coth(τ/2) + π − 2arctan e^τ ≥ log(2/τ) + π/2 − τ (thm:S iii; coth x ≥ 1/x; d/dτ(π − 2arctan e^τ) = −1/cosh τ ≥ −1). ∎

**Lemma 1.3 (w).** w(s) := ∫₀²(1 − cos sv)/v dv = log(2|s|) + γ − Ci(2|s|). w is increasing in |s| (w′(s) = (1−cos 2s)/s ≥ 0) and w(s)/s² = ∫₀² [(1−cos sv)/(sv)²] v dv is decreasing on 0 < s ≤ π (because (1−cos x)/x² = ½(sin(x/2)/(x/2))² decreases on 0 < x < 2π and sv ≤ 2π). Hence for 0 < R ≤ π: **w(s) ≥ w(R)·min(1, s²/R²)** for all s. ∎

**Lemma 1.4 (double Poincaré).** If h ∈ L²(ℝ), supp h ⊂ [−1,1], h″ ∈ L²(ℝ), then h ∈ H²₀(−1,1) and ‖h″‖² ≥ π²‖h′‖² ≥ (π⁴/4)‖h‖². (h′ ∈ H¹₀ with ∫h′ = 0 ⟹ Rayleigh quotient ≥ the second Dirichlet eigenvalue on length 2, π²; h ∈ H¹₀ ⟹ ≥ (π/2)².) [CITED refinement, not used: the clamped beam gives 31.285 instead of π⁴/4 = 24.35.] ∎

**Theorem A.** For 0 < τ ≤ 0.1 and a := τ²/4,
 c_∞(τ) ≥ C₀ + log(2/τ) + π/2 − τ + κ₀(τ), κ₀(τ) ≥ sup_{0<R≤π} w(R)·[1 − 16(R²+a)³/(27π⁴R²)].
Numerically the supremum is at R* = 2.17, κ₀ ≥ 1.927, and **c_∞(τ) ≥ log(1/τ) − C_A(τ)** with C_A = 5.3722 − log 2 − π/2 + τ − κ₀ ≤ 1.19 + τ.

*Proof.* F ∈ 𝒫_τ, ‖F‖ = 1. By thm:A and 𝒞F(u) = 0 for u ≥ 2τ: 𝔞_∞(F) = C₀ + ∫_{2τ}^∞K + ∫₀^{2τ}(1 − 𝒞F(u))K(u)du. Lemma 1.2 bounds the tail. Scaling F(x) = τ^{−1/2}G(x/τ) (G on [−1,1], ‖G‖ = 1, 𝒞F(u) = 𝒞G(u/τ)) and using 1 − 𝒞G ≥ 0 and τK(τv) ≥ 1/v for v ≤ 2 (Lemma 1.1, 2τ ≤ 0.2): ∫₀^{2τ}(1−𝒞F)K ≥ ∫₀²(1 − 𝒞G(v))/v dv = (1/2π)∫ w(s)|Ĝ(s)|² ds (Plancherel; 1 − 𝒞G(v) = (1/2π)∫(1−cos sv)|Ĝ|²). The Tate condition ∫G e^{±τy/2} = 0 says Ĝ(∓iτ/2) = 0, so Ĝ(s) = (s² + a)H(s) with H entire of exponential type 1 and H ∈ L²(ℝ) (division by a polynomial with no real zeros), H = ĥ with supp h ⊂ [−1,1]. By Lemma 1.3, (1/2π)∫w|Ĝ|² ≥ w(R)[1 − (1/2π)∫(1 − s²/R²)⁺|Ĝ|²]. Now (1−s²/R²)⁺(s²+a)² ≤ M_R := 4(R²+a)³/(27R²) (maximum at s² = (2R²−a)/3), so (1/2π)∫(1−s²/R²)⁺|Ĝ|² ≤ M_R‖h‖², while 1 = (1/2π)∫(s²+a)²|H|² = ‖h″‖² + 2a‖h′‖² + a²‖h‖² ≥ ‖h″‖² ≥ (π⁴/4)‖h‖² (Lemma 1.4; if h″ ∉ L² the left side would be infinite). Hence the low mass is ≤ 4M_R/π⁴, and the formula follows; C_A by arithmetic. ∎

**Verification (NUMERICAL, `r025_p1_lowpass.py`; Galerkin from r024 on a single window, N = 14 and 20 agree to 4 digits):**

| τ | log(1/τ) | Theorem A bound | Theorem B bound (k=1) | c_∞(τ) Galerkin | C_A | C_B | C_gal |
|---|---|---|---|---|---|---|---|
| 0.020 | 3.912 | 2.711 | 2.255 | 3.4019 | 1.201 | 1.657 | 0.510 |
| 0.031 | 3.474 | 2.262 | 1.807 | 2.9636 | 1.212 | 1.667 | 0.510 |
| 0.050 | 2.996 | 1.765 | 1.311 | 2.4856 | 1.231 | 1.684 | 0.510 |
| 0.0619 | 2.782 | 1.540 | 1.087 | 2.2720 | 1.243 | 1.696 | 0.510 |
| 0.0894 | 2.415 | 1.144 | 0.692 | 1.9043 | 1.270 | 1.722 | 0.510 |
| 0.100 | 2.303 | 1.021 | 0.569 | 1.7923 | 1.281 | 1.733 | 0.510 |

The asymptotic c_∞(τ) = log(1/τ) − 0.510 + o(1) is NUMERICAL (constant stable to 3 digits on [0.02, 0.1]); Theorem A proves it with coefficient 1 and constant 1.2–1.3. The loss lies in ∫_{|s|<R}|H|² ≤ ‖h‖² and in π⁴/4: a certified bound on the lower eigenvalue of w(D) with a double zero at 0 (a single-geometry problem, independent of τ) would bring it down to ≈ 0.6.

## 2. Theorem B — direct bound on 𝒱_k (PROVED): (L1) without coupling

**Lemma 2.1 (low-pass leakage of 𝒱_k).** Let F ∈ 𝒱_k (k blocks of half-length τ ≤ 0.1), R > 0, G := P_R F (F̂·1_{|s|≤R}). Then ‖P_RF‖² ≤ δ(Rτ)‖F‖², δ(θ) := cosh²τ·(θ² + τ²/4)²/6.

*Proof.* For a block B centered at c, let r := G − G(c)cosh((x−c)/2) − 2G′(c)sinh((x−c)/2) on B. Then r(c) = r′(c) = 0 and r″ − r/4 = G″ − G/4 =: H, so r(x) = ∫_c^x 2sinh((x−t)/2)H(t)dt and, by Cauchy–Schwarz and 2sinh(z/2) ≤ z cosh(z/2) ≤ z cosh τ (|z| ≤ 2τ), |r(x)|² ≤ cosh²τ·(|x−c|³/3)‖H‖²_{L²(B)}, ∫_B r² ≤ cosh²τ(τ⁴/6)‖H‖²_B. Since the subtracted function lies in span{e^{±x/2}} and F_B ⊥ that span: ⟨F_B, G⟩_B = ⟨F_B, r⟩_B ≤ ‖F_B‖·dist_B. Summing, ‖G‖² = ⟨F, G⟩ (P_R an orthogonal projection) ≤ ‖F‖(Σ_B∫_B r²)^{1/2} ≤ ‖F‖·cosh τ·(τ²/√6)·‖G″ − G/4‖_{L²(ℝ)} ≤ ‖F‖·cosh τ(τ²/√6)(R² + ¼)‖G‖. ∎

**Theorem B.** For every F ∈ 𝒱_k, with τ = T/k ≤ 0.1, θ* the root of δ(θ*) = 1 (θ* ≈ 6^{1/4} = 1.565) and m_lb(R) := max(C₀, log(R/2π) − 1/R − 1/(2R²)) (lem:mbounds ii),
 𝔞_∞(F) ≥ ‖F‖²·[C₀δ(0) + ∫₀^{θ*} m_lb(θ/τ) δ′(θ) dθ] =: ‖F‖²·(log(1/τ) − C_B(τ)).
With δ′(θ) = (2/3)cosh²τ·θ(θ²+τ²/4): C_B(τ) → ¼ − log(θ*/2π) = 1.640 as τ → 0, and C_B ≤ 1.74 for τ ≤ 0.1 (table §1).

*Proof.* Let μ = (1/2π)|F̂|²ds/‖F‖². 𝔞_∞(F)/‖F‖² = ∫m dμ = C₀ + ∫₀^∞ μ(|s| ≥ R) m′(R) dR (m increasing and absolutely continuous, lem:mbounds i; Tonelli). By Lemma 2.1, μ(|s| ≥ R) ≥ (1 − δ(Rτ))⁺. Integrating by parts on [0, R*], R*τ = θ*: ∫₀^{R*}(1−δ(Rτ))m′ dR = ∫₀^{R*}(m(R) − C₀)τδ′(Rτ)dR, whence ∫m dμ ≥ C₀(1 − ∫₀^{θ*}δ′) + ∫₀^{θ*} m(θ/τ)δ′(θ)dθ = C₀δ(0) + ∫₀^{θ*} m(θ/τ)δ′(θ)dθ, and m ≥ m_lb. With a = 0: ∫₀^{θ*}(2/3)θ³ log(θ/2πτ)dθ = log(1/τ) + log(θ*/2π) − ¼. ∎

**Corollary (L1, PROVED).** c(T,k) = min 𝔞_T|𝒱_k ≥ log(k/T) − C_B(T/k) − ‖P|𝒱_k‖, with ‖P|𝒱_k‖ ≤ Σ_{n∈𝒩_T} v_n = 𝒜_T (Cauchy–Schwarz), = 𝒜_T/2 for T ≤ log 2 (R186_104 3a), and ≤ v₂/√2 + (v₃+v₄)/2 = 1.674 on (log 2, ½log5] (R186_104 3b, CITED). Values (`r025_p1_lowpass.py`): T = 0.69, k = 12: 1.164 − 1.124 = +0.04; k = 14: +0.20. ½log5: k = 25: 1.768 − 1.674 = +0.09; k = 26: +0.13; k = 30: +0.28 (dim E = 2k−2 = 58). Without the 1.674 bound (only 𝒜_T = 2.94): k = 85 gives +0.07.

**Comparison with Galerkin (NUMERICAL, N = 8/12/16, r024 `build`/`analyse`; min 𝔞_∞|𝒱_k with no primes):**

| T | k | τ | Theorem B | Galerkin min 𝔞_∞\|𝒱_k | min diag Σ_B𝔞_∞(F_B) = c_∞(τ) |
|---|---|---|---|---|---|
| ½log3 | 7 | 0.0785 | 0.833 | 1.8639 | 2.035 |
| 0.69 | 9 | 0.0767 | 0.858 | 1.8828 | 2.058 |
| ½log5 | 9 | 0.0894 | 0.692 | 1.7290 | 1.904 |
| ½log5 | 13 | 0.0619 | 1.087 | 2.0929 | 2.272 |

Readings: (i) the bound is valid and loses ≈ 1.0 relative to the Galerkin value (which is an upper bound); (ii) the coupling costs only 0.17–0.18 at the Galerkin minimizers (diag − min), nothing like π: the maximizers of ‖𝒦₁‖ are not the minimizers of the form; (iii) the Galerkin computation on 𝒱_k is converged in N (3 digits), as in R186_104.

## 3. (P2) closed: ‖𝒦₁‖_{𝒱_k} = π for a pair, ∈ [π, 2π] for the chain (PROVED)

**3.1 Argument.** Between adjacent blocks B = (c−2τ, c), B′ = (c, c+2τ), in corner variables x′ = c − x, y′ = y − c ∈ (0, 2τ), the coupling kernel is K₁(x′+y′) with K₁(u) = 1/u − 3/2 + O(u) (R186_104 row 2). The Carleman operator 1/(x′+y′) on L²(0, 2τ) is bounded with norm π (Hilbert's inequality, scale-invariant) and has essential spectrum [0, π] (Mellin diagonalization: symbol π/cosh(πσ), CITED Carleman 1923). K₁ − 1/u is bounded on (0, 4τ], hence Hilbert–Schmidt on the square: a compact perturbation. The two Tate conditions per block have finite codimension; a finite-codimension compression preserves the essential spectrum (Weyl). So the pair has norm exactly π on 𝒱 (≤ π from K₁ ≤ 1/u and Hilbert). For the chain of k blocks: ≥ π (take the pair) and ≤ 2π (each block is in two pairs: 2|⟨F_B, HF_{B′}⟩| ≤ π(‖F_B‖² + ‖F_{B′}‖²), sum ≤ 2π‖F‖²; non-adjacent pairs are absorbed by the same argument since their kernel is also ≤ 1/u).

**3.2 Explicit Weyl sequence (PROVED, elementary, no citation needed).** f_M(x′) = x′^{−1/2}1_{[e^{−M}·2τ, 2τ]} on each of the two blocks. ‖f_M‖² = M. With u = log(x′/2τ), v = log(y′/2τ): ∫∫ f_M f_M/(x′+y′) = ∫∫_{[−M,0]²} du dv/(2cosh((u−v)/2)) = πM − O(1) (∫_ℝ dw/(2cosh(w/2)) = π). The −3/2 + O(u) term of K₁ − 1/u contributes O(‖f_M‖₁²) = O(τ). The projection onto the orthogonal complement of {e^{±x/2}} subtracts p with ‖p‖ = O(1) uniform in M (moments ∫f_M e^{±x/2} = O(√τ), Gram ≍ τ), and |Q(f_M, p)| ≤ π‖f_M‖‖p‖ = O(√M). Hence Q(F)/‖F‖² = (πM − O(√M))/(M − O(1)) → π. Numbers (`r025_coupling_norm.py`, exact K₁, exact Tate, independent of τ): 0.023 / 0.307 / 1.415 / 2.463 / 2.867 / 3.017 / 3.082 for M = 2 / 4 / 8 / 16 / 32 / 64 / 128 → π (rate π − O(1/M)); matches the test f = x^{−½+δ} of R186_104 (3.00 at δ = 0.02).

**3.3 The relative bound (what R186_104 asked for).** θ_N := sup_{𝒱_k} Q(F)/Σ_B 𝔞_∞(F_B) (generalized eigenvalue of −(A₀ − diag A₀) relative to diag A₀ on 𝒱_k, N per block): 0.206 / 0.218 / 0.222 (½log3, k = 7), 0.206 / 0.218 / 0.222 (0.69, k = 9), 0.218 / 0.229 / 0.233 (½log5, k = 9), 0.194 / 0.205 / 0.210 (½log5, k = 13) for N = 8/12/16. NUMERICAL, slowly increasing (increments halving), limit ≈ 0.23–0.25; the minimum is −θ_N (symmetry of the coupling). This is consistent with Theorem B: the Weyl sequence has Σ_B𝔞_∞(f_M) ≍ M²/2 (Fourier mass ≍ 1/|s| on 1 ≤ |s| ≤ e^M against log|s|) versus Q ≍ πM, so it is not extremal for the relative ratio. **θ < 1 is not proved**; it is OPEN and, for (L1), unnecessary: Theorem B directly gives 𝔞_∞|𝒱_k = diag − Q ≥ log(1/τ) − C_B, i.e. Q ≤ Σ_B𝔞_∞(F_B) − (log(1/τ) − C_B)‖F‖² (PROVED), which is the relative bound with θ = 1 and a large negative constant, sufficient.

## 4. What remains OPEN for D

- (L1): PROVED (Theorem B + Corollary) with k ≈ 26 at ½log5 (1.674 CITED) or k ≈ 85 (trivial 𝒜_T). It is high-pass coercivity, not arithmetic structure: the entire content of the positivity statement lies in
- **(L2) OPEN: S_T = G_EE − G_E𝒱G_𝒱𝒱^{−1}G_𝒱E ≻ 0 in dimension 2k − 2** (≈ 50–60 at ½log5), E = span{e^{±x/2}1_B} ∩ 𝒫_T. As R186_104 row 6 establishes, S inherits λ_A ≤ λ_S ≤ λ_A(1+‖K‖)² and the decay of thm:margin: it is W ≥ 0 rewritten in an explicit basis; as a reformulation of D it is a valid target, but there is no gain in precision. The only thing PROVED (L1) contributes to (L2): G_𝒱𝒱 ≥ c > 0 explicit, so the resolvent G_𝒱𝒱^{−1} is bounded by 1/c with c PROVED (≈ 0.1–0.3), which makes the Schur tail certifiable with interval arithmetic for T ≤ 0.6 (λ_A ≥ 10⁻⁵).
- Constant improvement (OPEN, standard): C_A from 1.2 to ≈ 0.6 (certified eigenvalue of w(D) with a double zero); C_B from 1.7 to ≈ 1 (smooth-frequency window in Lemma 2.1; use exact m instead of m_lb).
- Explicit NO-GO: (L1) via operator norms (c_∞(τ) − ‖𝒦₁‖ − ‖P‖) for any reasonable k; ‖𝒦₁‖_{𝒱_k} ≥ π cannot be improved by Tate conditions or by any finite-codimension condition.

## Audit notes

- Theorem A: the only hypothesis is τ ≤ 0.1 (Lemma 1.1 with 2τ ≤ 0.2; Lemma 1.3 with R ≤ π). The sup over R is evaluated numerically (R* = 2.17) but any R ≤ π gives a valid bound; with R = 2 by hand: w(2) = log 4 + γ − Ci(4) = 2.104, 1 − 16·64/(27π⁴·4) = 0.903, κ₀ ≥ 1.900.
- Theorem B: δ(θ) uses ‖G″ − G/4‖ ≤ (R²+¼)‖G‖ (Ĝ supported on |s| ≤ R) and ∫_c^x(x−t)²dt = |x−c|³/3; m_lb from lem:mbounds(ii) and m ≥ C₀ = m(0); the integral ∫m_lb δ′ is a 1-D quadrature (scipy quad, error < 10⁻⁸); C₀δ(0) = −5.37·cosh²τ·τ⁴/96 ≈ −10⁻⁷ included.
- §3: the upper bound 2π for the chain is crude; the exact value for the chain is not claimed. The compactness of K₁ − 1/u and Weyl's theorem for finite-codimension compressions are standard; 3.2 does not need them.
- The Galerkin tables are upper bounds (infima over subspaces); the theorems are lower bounds; at every point the lower bound < Galerkin value, as it must be.
- No equivalence between row D and other statements is used.

## For Paper 46

- Can be integrated as archimedean lemmas (verify against thm:A, lem:K, lem:mbounds): Lemma 1.1, Theorem A (short window: λ_A(τ) ≥ log(1/τ) − 1.29, a complement to lem:contA/thm:margin at the T → 0 endpoint), Lemma 2.1 + Theorem B (coercivity of 𝒱_k). Do not integrate anything from R186_024 §3's split (L1) or "‖𝒦₁‖ ≈ 0.74"; if the coupling is mentioned, say "norm π, relative bound ≈ 0.22 NUMERICAL".
- Labels: Lemmas 1.1–1.4, 2.1, Theorems A, B, Corollary (L1): PROVED (with 1.674 CITED from R186_104). §3.1 PROVED (CITED Carleman/Weyl), §3.2 PROVED elementary. θ_N: NUMERICAL. (L2): OPEN. Operator-norm route: NO-GO.
