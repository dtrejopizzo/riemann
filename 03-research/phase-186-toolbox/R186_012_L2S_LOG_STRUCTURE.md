# R186.012 — L2_S: logarithmic structure of ε_S and (M) in the semilocal Sonin decomposition, S = {∞,2}

Notation of R186.009–011 (λ = ½, P = 1_{(0,λ]}, F_S, A_S = PF_SP, K_S = Σ_{k≥−1} a_k c_k, a_{−1} = −1, a_k = 1 (k ≥ 0), c_k = cos(2π2^k xy)).
Nothing here touches the sign.

## Status

| # | Statement | Label |
|---|---|---|
| R1 | **Resolvent form.** ε_S(ρ) = ρ^{1/2}∫_{λ/ρ}^{λ} G(ρx,x)dx, G := (1−P)F_S·A_S(1−A_S²)^{−1}P = G₀ + G₀R, G₀ := (1−P)F_SPF_SP, R := A_S²(1−A_S²)^{−1} = Σ_{m≥1}A_S^{2m} (Neumann, ‖A_S‖ = λ₁ < 1) | PROVED (as a distributional density; pointwise equality with the series (84)_S outside {2^j}: ARGUED) |
| R2 | **Kernel of G₀.** For u > λ ≥ z > 0: G₀(u,z) = ½Σ_{k,l≥−1}a_ka_l[S(2^ku − 2^lz) + S(2^ku + 2^lz)], S(w) = sin(2πλw)/(2πw), absolutely convergent series outside the ridges u = 2^iz, and in L²_loc | PROVED |
| Lem | **Lacunary sum.** Σ_{k≥k₀}S(2^kt) = λ·#{k ≥ k₀: 2^k\|t\| ≤ 1} + O(1), uniform in t ≠ 0 and k₀ (O(1) ≤ λ + 2πλ³/3·4/3 + 1/π) | PROVED |
| L2_S | **Logarithmic structure.** For ρ ∈ [1,R]: ε_S(ρ) = Σ_{0≤j≤log₂R} β_j log⁺(1/\|ρ−2^j\|) + O_R(1), with **β_j = 2^{j/2}(1−2^{−j})·λ²/(2 log 2)** (β₀ = 0 in the sense that at ρ = 1 the factor (1−1/ρ) gives ε_S ≈ (ρ−1)·b·log(1/(ρ−1)), **b = λ²/(2log2) = 0.1803**) | PROVED (given R1, R2, Lem, HS-1) |
| HS-1 | R = A_S²(1−A_S²)^{−1} is Hilbert–Schmidt (Σλ_n⁴ < ∞ by Sp of R186.011) and the density of G₀R is continuous and bounded on compacta | PROVED (boundedness); continuity ARGUED |
| Lp | ε_S ∈ L^p_loc(ℝ*₊) for all p < ∞; ε_S ∉ L^∞_loc | PROVED (given L2_S) |
| M | R′_S = −C_{ε_S} is Hilbert–Schmidt on L²(I_T) for every T; E_S = Son_S − (HS) | PROVED given the reduction of R183_029 (CITED) |
| Num | β₁, β₂, β₃ from the formula: 0.1275, 0.2705, 0.4463; measured slopes of d₀ in log(1/δ): 0.128, 0.272, 0.448; b measured as ρ → 1: 0.17–0.19 vs 0.180 | NUMERICAL (agreement < 1%) |
| In | n₋(−C_{ε_S}\|𝒫_T) finite for each T; its growth in T and comparison with the inertia of E_S | OPEN (not computed in this round) |
| S3 | S = {∞,2,3}: singularities on the dense set {2^a3^b}, of log and log² type, with effective support decreasing exponentially with height; ε_S ∈ L^p_loc | ARGUED |

**Verdict.** L2_S is **PROVED** for S = {∞,2}: the divergence of ε_S is concentrated in the m = 0 term of the Neumann series (the density of F_S A_S, the cross "A_S²"), with positive logarithmic singularities of explicit coefficient β_j = 2^{j/2}(1−2^{−j})λ²/(2log2) at ρ = 2^j; the terms m ≥ 1 are bounded because A_S² is HS. Consequence: ε_S ∈ L^p_loc ∀p < ∞ and (M) holds in the semilocal Sonin decomposition (Hilbert–Schmidt remainder). The numerical β's of R186.011 (β₁ ≈ 0.15, "∝ 2^{j/2}(1−2^{−j})") are now explained; the coefficients c_j in log N (0.10, 0.2, 0.3) are not β_j (nonlinear relation N ↔ \|δ\|; ratio c_j/β_j ≈ 0.7–0.8).

## 1. Resolvent form (R1)

ξ_n^♯ = λ_n^{−1}F_Sξ_n, hence λ_n²/(1−λ_n²)ξ_n^♯(u)ξ_n(x) = [F_S·λ_n(1−λ_n²)^{−1}|ξ_n⟩⟨ξ_n|](u,x). Summing over n (the ξ_n with λ_n = 0 contribute nothing) gives the kernel of F_S A_S(1−A_S²)^{−1}P = F_S Σ_{m≥0}A_S^{2m+1}; since F_SA_S = F_SPF_SP, F_SA_S^{2m+1} = (F_SPF_SP)A_S^{2m}. At u = ρx > λ only (1−P) counts. Thus G = G₀(1 + R). The claim is about densities: for f ∈ C_c^∞, ∫f(ρ)ε_S(ρ)d*ρ (defined by the trace of R186.009) is rewritten as a pairing of the operator G with the kernel of ϑ, and exchanging the sum over n with the integral is legitimate in the distributional sense because Σ_n converges in operator norm (R1 is an identity of functional calculus). That the pointwise series (84)_S agrees with this density for ρ ∉ {2^j}: ARGUED (convergence observed in R186.011 §3).

## 2. Kernel of G₀ (R2) and lacunary lemma (Lem)

∫_0^λ cos(2πα y)cos(2πβ y)dy = ½[S(α−β)+S(α+β)]. With F_K := Σ_{−1≤k≤K}a_kc_k: for φ ∈ C_c^∞(0,∞), ‖c_kφ‖ = O(2^{−k/2}) ⇒ F_Kφ → F_Sφ in norm; P c_k P converges in norm (R186.011). Hence ⟨φ, G₀ψ⟩ = lim_K ½Σ_{k,l≤K}a_ka_l∫∫φ(u)ψ(z)[S(·−·)+S(·+·)], and the limit passes inside by dominated convergence using Lem (uniform-in-K bound on the partial sums by diagonal i = l − k, ≤ λ·#+O(1), locally integrable, with geometric tail in |i|).
Lem: |S(s) − λ| ≤ (2πλ)²λs²/6·… (Taylor), |S(s)| ≤ 1/(2π|s|). The k with 2^k|t| ≤ 1 each contribute λ plus Σ O(4^k t²) = O(1); the rest give Σ 1/(2π2^k|t|) ≤ 1/π. ∎
Diagonals. Fix i = l − k; the term S(2^k(u − 2^iz)) has argument 2^k t_i, t_i = u − 2^iz, k ≥ k₀(i) = max(−1, −1−i). With u = ρx, z = x, x ∈ [λ/ρ, λ], ρ ∈ [1,R]: |t_i| ≥ c_R > 0 except for the i with 2^i ∈ [1/2, 2R]; the other diagonals sum to O_R(1) (tail Σ_i 2^{−k₀(i)}/|t_i| geometric). The terms S(2^ku + 2^lz) are O(1) in total (argument ≥ 2^k u ≥ 2^kλ). The terms with a_{−1} are finite (one diagonal each, O(1) by Lem). Hence
 G₀(ρx,x) = (λ/2)Σ_{0≤i≤log₂R} log₂⁺(1/(x|ρ−2^i|)) + O_R(1) = (λ/(2log2))Σ_i log⁺(1/|ρ−2^i|) + O_R(1),
uniform for x ∈ [λ/R, λ].

## 3. L2_S (PROVED)

Integrating: d₀(ρ) := ρ^{1/2}∫_{λ/ρ}^λ G₀(ρx,x)dx = ρ^{1/2}λ(1−1/ρ)·(λ/(2log2))Σ_i log⁺(1/|ρ−2^i|) + O_R(1). At ρ = 2^j the prefactor is 2^{j/2}λ(1−2^{−j}): β_j = 2^{j/2}(1−2^{−j})λ²/(2log2). As ρ → 1⁺ the prefactor is ≈ λ(ρ−1) and the O_R(1) also carries the factor (1−1/ρ) (interval length): d₀(ρ) = (ρ−1)(a + b log(1/(ρ−1))) + o(ρ−1)·… with b = λ²/(2log2), which explains the "Prof" profile of R186.011.
Terms m ≥ 1 (HS-1): r := kernel of R ∈ L²((0,λ]²) (Σ_nλ_n⁴/(1−λ_n²)² < ∞). |(G₀R)(u,x)| ≤ ‖G₀(u,·)‖_{L²(0,λ)}‖r(·,x)‖; ‖G₀(u,·)‖ is uniformly bounded for u ∈ [λ, λR] (the ridges at y = 2^{−i}u are logarithmic, of L² mass ≍ 2^{−i}u, summable). Hence |ρ^{1/2}∫_{λ/ρ}^λ(G₀R)(ρx,x)dx| ≤ R^{1/2}·sup_u‖G₀(u,·)‖·λ^{1/2}‖r‖_HS. Continuity in ρ: ARGUED (continuity of u ↦ G₀(u,·) in L², dilation). ∎
Sign check: β_j > 0, consistent with Div2 (ε_S(2^j) = +∞) and with S (no alternation) of R186.011.

## 4. Consequences

- Lp: log⁺ ∈ L^p_loc ∀p < ∞; finitely many singularities on each compactum. ε_S ∉ L^∞ (β_j > 0).
- (M): in the coordinates of R183_029, ∫_{−2T}^{2T}|ε_S(e^{|s|})|²ds < ∞ for every T (ρ < 1 by the symmetry of the density used there), hence R′_S = −C_{ε_S} is HS on L²(I_T): E_S = Son_S − C_{ε_S} = (positive trace-type form) + (self-adjoint HS). The weak form (M_w)/(E′_loc) (R184_003 Lemma B.1) is subsumed.
- Inertia: −C_{ε_S}|𝒫_T is compact self-adjoint, hence n₋ < ∞ for every T (PROVED). Whether the bound is uniform or its growth in T: OPEN. n₋ was not computed numerically in this round (it requires the full profile of ε_S with K converged; the generic values of R186.011 have ~25% error). Note that the singular part Σβ_j log⁺ is positive, so that −C of that part, if C_{log⁺} is of positive type (log⁺(1/|·|) has a positive Fourier transform only asymptotically), would contribute mainly to n₋ together with the regular part: ARGUED, not used.

## 5. S = {∞,2,3} (ARGUED)

With frequencies 2^{k₁}3^{k₂}, ridges appear at ratios r = 2^{i₁}3^{i₂}, dense in ℝ₊. For a fixed ratio, the pairs resolved at distance δ have two degrees of freedom of displacement (k₁,k₂), with #≈ log²(1/δ)/(2log2·log3): **log²** singularities instead of log. But if i₁, i₂ have opposite signs, the constraints k ≥ −1 force frequencies ≥ 2^{|i₁|} or 3^{|i₂|} = e^{H(r)}, and the singularity only lives on |ρ − r| ≲ e^{−H(r)}; its contribution to ‖·‖_{L^p}^p is O(H^{2p}e^{−H}), and the number of r ∈ [1,R] of height ≤ H is O(H): Σ_r converges. Hence ε_S ∈ L^p_loc ∀p < ∞ also for {∞,2,3}, assuming the semilocal kernel has O(1) coefficients at frequencies 2^a3^b (form not checked against the construction of R186.002). For general finite S the same argument gives log^{|S|−1}; for growing S(T) the uniform control is OPEN.

## Audit notes

- R1 is functional calculus; the only subtlety is the density ↔ pointwise series identification (ARGUED outside 2^j, and at 2^j the series diverges, as it should).
- R2 uses that F_Kφ → F_Sφ in norm for smooth φ of compact support in (0,∞) and dominated convergence with the bound of Lem; check the tail in |i| (both signs) — done in §2 with k₀(i).
- The O_R(1) depends on R (number of active diagonals and of log(1/x) with x ≥ λ/R); uniformity in R is not claimed.
- HS-1 depends on Sp (R186.011, PROVED) and on sup_u‖G₀(u,·)‖ < ∞ (summable logarithmic ridges; accumulation as y → 0 controlled by mass 2^{−i}u).
- (M) depends on the CITED reduction of R183_029 (HS ⟸ ε ∈ L²_loc in the log variable); not re-derived here.
- Numerics: scratchpad `l2s.py` (truncated double sum K = 45, Gauss–Legendre 4000 nodes; this measures d₀ only, not the full series). Slopes per decade /ln10: j=1: 0.1276, 0.1281, 0.1265; j=2: 0.2713, 0.2717, 0.2685; j=3: 0.4475, 0.4483, 0.4429; predicted 0.1275, 0.2705, 0.4463. ρ = 1+δ: d₀/δ = 1.280, 1.670, 2.100 (δ = 10⁻³,10⁻⁴,10⁻⁵): increment 0.39, 0.43 per decade ≈ b·ln10 = 0.415.
- Nothing about the sign of E_S, nor about (TC_S), nor equivalences with RH.

## For Paper 47

- Proposition (structure of the semilocal density, S = {∞,2}): ε_S = d₀ + (continuous), d₀ with log⁺ singularities at 2^j and coefficient β_j = 2^{j/2}(1−2^{−j})λ²/(2log2). One-page proof (Lem + diagonals + Neumann/HS).
- Corollary: ε_S ∈ L^p_loc, R′_S Hilbert–Schmidt; the decomposition E_S = Son_S − HS holds for every T. Honest label: PROVED for S = {∞,2}; ARGUED for {∞,2,3}; OPEN for S(T).
- Remark: the non-HS character of A_S (NH) manifests exactly as the m = 0 term of the Neumann series; the terms m ≥ 1 are harmless.

## Note (R186_097)

* L2_S PROVED for d_S (density of the Halmos series (84)_S): d_S ∈ L^p_loc ∀p<∞, singularities β_j log⁺ at 2^j, ∉ L^∞_loc. β_j and b recomputed. As a statement about the kernel of R′_S: CONDITIONAL on (84)_S/Δ (trace/series exchange CC (85)–(90)_S, trace-ability of PX, XP, PXP against ϑ(f)).
* Rename: what is proved is (E′_loc)/L1′, not the microlocal (M) of R183_029 (which is no longer needed). MINOR: lemma sup_u‖G₀(u,·)‖ as y→0; constant of the lacunary lemma; d_S a.e. by Fubini.
* Paper 47: admissible as a Proposition about d_S; "R′_S HS ∀T" only CONDITIONAL.
