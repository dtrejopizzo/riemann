# VERIFY — «clamped ends» vs «moment conditions» for P_T, and the edge law U3

 Verifier memo on INV_U_001 §1 and U3. Sources: Paper 47 main.tex l.112–130
(def. of 𝔞_T, 𝒟_T, A, B, P_T, W_T, Φ_F), thm:Aform/eq:Kprim + rem:Kprim (l.400–440). No paper edited.

## 1. Paper 47's definitions (verbatim content)
- 𝒟_T = {F ∈ L²(I_T): ∫log(2+|τ|)|F̂|² < ∞}; A(F)=∫F e^{t/2}, B(F)=∫F e^{−t/2}; **P_T = {F ∈ L²(I_T): A(F)=B(F)=0}**.
- Φ_F(s)=∫F e^{(s−½)t}dt, so Φ_F(1)=A, Φ_F(0)=B; F̂(τ)=∫F e^{−iτt} gives F̂(i/2)=A, F̂(−i/2)=B.
- c_F = F*F̃ (autocorrelation, written Φ in eq:Kprim); its transform |F̂|² extends to F̂(τ)·conj F̂(conj τ), so F ∈ P_T ⇒
  ĉ_F vanishes to order ≥ 2 at ±i/2 (l.429–430: «order ≥2» refers to **ĉ_F at ±i/2**, not to any edge value).
- The minimizer h*_T of λ_A lives in the **F variable** (P_T ∩ 𝒟_T).

## 2. Exact equivalence (PROVED)
**Proposition.** Let L := ¼ − ∂². The map G ↦ F = LG is a linear bijection H²₀(I_T) → P_T (G extended by 0, H²₀ = {G ∈ H²: G(±T)=G′(±T)=0}),
bounded with bounded inverse (L²→H²), and F̂(τ) = (¼+τ²)Ĝ(τ).
*Proof.* (⇒) For G ∈ H²₀, LG ∈ L²(I_T); integrating by parts twice, ∫(¼G − G″)e^{±t/2} = −[G′e^{±t/2} ∓ ½Ge^{±t/2}]_{−T}^{T} + ∫G(¼ − ¼)e^{±t/2} = 0
because G, G′ vanish at ±T. (⇐) Given F ∈ L²(I_T), the unique solution of G″ − ¼G = −F on I_T with G(−T)=G′(−T)=0 is
G(t) = −∫_{−T}^{t} 2 sinh((t−s)/2) F(s) ds ∈ H²(I_T), and
G(T) = −(e^{T/2}B − e^{−T/2}A),  G′(T) = −½(e^{T/2}B + e^{−T/2}A).
The 2×2 matrix is invertible (det = −1 ≠ 0 up to sign), so G(T)=G′(T)=0 ⇔ A=B=0. Injectivity: LG=0 with G∈H²₀ forces G ∈ span(e^{±t/2}) with
zero Cauchy data, G=0. Fourier identity: G ∈ H²(ℝ) after zero extension. ∎
**Consequence.** Both descriptions are correct **in different variables**:
- in F (the variable of 𝔞_T, λ_A, h*): two moment conditions, **no** boundary condition. INV_U_001 §1 is correct (e.g. 𝟙_{I_T} minus its
  projection on span(e^{±t/2}) is in P_T ∩ 𝒟_T and nonzero at ±T).
- in the potential G = L^{−1}F: exactly clamped ends G(±T)=G′(±T)=0 (beam / H²₀).
The statement «P_T = clamped ends» is **wrong only if read on F (or h*)**. In particular nothing in P_T forces h*(±T)=0.

## 3. Corpus grep («clamped», «G(±T)», «G′(±T)», «extremos sujetos», «vanish to order 2», «sujet*», H²₀)
| place | usage | verdict |
|---|---|---|
| phase-190 EXP_004_OMEGA0.md l.1,3; scripts/omega0.py | P_T = (¼ − ∂²)H²₀(I_T), clamped ground mode G₀ | **correct** (G variable) |
| phase-116 row_d_gamma_fourier_tate_v89–v93_audit.tex | «clamped potentials φ», F = Lφ | **correct** (potential variable) |
| R186_025 Lema 1.4 | H²₀ Poincaré for h with h″ ∈ L² | correct, a statement about the potential, not about P_T∩𝒟_T elements |
| Paper 47 l.429–430 | order ≥2 vanishing of ĉ_F at ±i/2 | correct (frequency side) |
| INV_U_001 §1 | «no clamping» | correct for F; add that clamping holds for G |
| R186_048 §4 (l.184–190), SPEC_A §1 (l.43) | h* ~ (T−|t|)^a, a≈0.15–0.25 (fitted); not a clamping claim | not the wrong description; see §4 |
| R186_019 / R186_100, other «sujet*» hits | unrelated | — |
No file in 03-research/, 05-meta-and-planning/ or Paper 47 attributes clamped ends to F or h*. The wrong reading lived only in
working notes. **No result depended on it.** (R186_048's argument against the fold uses measured h*(±T), not clamping.)

## 4. U3 (edge law h* ~ a_±(log κ/δ)^{−1/2})
- **Citation.** H. Chen, T. Weth, «The Dirichlet problem for the logarithmic Laplacian», Comm. PDE 44 (2019) 1100–1139: exists,
  correct bibliographic data (CITED). The *optimal* boundary law ℓ(δ)^{1/2}, ℓ = 1/log(1/δ), with a Hopf-type lemma, is in
  V. Hernández-Santamaría, L. F. López Ríos, A. Saldaña, «Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems
  involving the logarithmic Laplacian», DCDS-A (2024), doi:10.3934/dcds.2024084, arXiv:2401.18033 (CITED from abstract; full theorem
  not re-read). INV_U_001 should cite HLS 2024 for the exponent ½, Chen–Weth for the Dirichlet framework.
- **Scope.** Their operator: L_Δ (symbol 2log|ξ|, kernel c_N|z|^{−N} near 0 plus a fixed long-range part), Dirichlet exterior
  condition, N ≥ 1 (N=1 included), RHS bounded/Dini. Ours: the killed (support in I_T) form C₀‖F‖²+Lev(c_F) with kernel K(u) ~ 1/(2u)
  (lem:K), plus bounded comb term, plus finite-rank Lagrange terms α e^{t/2}+β e^{−t/2} (smooth), Euler–Lagrange L_K h* = λh* + comb + Tate.
  Not literally in scope: (i) K − c/|u| must be shown to be a perturbation the barrier argument tolerates (needs K(u) − 1/(2u) =
  O(1) or O(|log u|) near 0 — lem:K gives the leading term; the remainder order is not checked here); (ii) h* is sign-changing, so the
  Hopf part (lower bound, needed for a_± ≠ 0) does not apply; only the upper bound |h*| ≲ ℓ(δ)^{1/2} is plausibly transferable;
  (iii) the comb term is a nonlocal bounded operator (translations by log n), fine as bounded RHS once h* ∈ L^∞ is shown.
  Verdict: U3 stays **ARGUED**; upper bound |h*(t)| ≲ (log 1/δ)^{−1/2} is «CONDITIONAL on a perturbation lemma (i)+L^∞»; the exact
  asymptotic with a_± ≠ 0 (needed for U4's onset 2η/log) is OPEN (no Hopf for sign-changing minimizer). The matched-asymptotics balance
  of INV_U §2 is checked: with g = L^{−α}, the regional and killing terms balance iff α = ½ (constant c cancels). ✓
- **Relabel of R186_048 / SPEC_A fits.** Under U3 the collar mass is ≍ ε/log(1/ε), local exponent 1 + 1/log(κ/ε), slowly varying;
  a fit ε^{2a+1} over ε ∈ [.002, .032] at M = 40–48 returns 2a+1 ≈ 1.2–1.5, and the R186_048 local exponents increase with ε as the
  log law predicts. Relabel «a ≈ 0.15–0.25» from NUMÉRICO-exponent to **«NUMÉRICO fit; power reading ARGUED to be a resolution artefact
  of (log 1/δ)^{−1/2}»**. Dependency: SPEC_A §1 uses it «only to size»; the bound «ν_j ≤ 4·10⁹Te^{−15.449T}ε_j^{−1.5} (PROVED modulo
  the numerical edge-mass exponent)» depends on it: the ε_j factor becomes (ε_j/log(1/ε_j))^{−1} under U3 — the T-exponential part
  is unaffected; SPEC_A's verdict (OPEN identity version, gap (θ)) is unaffected.

## 5. Labels
PROVED: §2 equivalence. CITED: Chen–Weth 2019, HLS 2024. ARGUED: U3, the artefact relabel. CONDITIONAL: transferred upper bound.
OPEN: a_± ≠ 0. Row D: OPEN; this memo carries no sign.
