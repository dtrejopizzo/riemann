# INTEGRATION_206_ZCERT_001 — integration of rem:zcert into Paper 46 (phase 206)

Inputs: AUDIT_206_ZCERT_001.md (§8), ZCERT_001.md + data. Backup: `04-papers/46-row-d-sign-radial-intersection-form/main_pre_zcert.tex`.

## 1. Verification against the paper's definitions

- **eq:W / lem:roughEF.** W_T(F) = 𝔞_T(F) + 2Re(A B̄) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ), Φ_F(s)=∫F e^{(s−½)t}, sum over all zeros, no extra constant. For even real F: Φ_F(1−ρ)=Φ_F(ρ) (t→−t) and A(F)=B(F)=∫F cosh(t/2)=⟨F,χ_ev⟩. On c^⊥ the polar term vanishes: 𝔄_ev = 𝔞_T = W_T = Σ_ρ Φ_F(ρ)². **Factor 1** (the "factor 2" of the audit is just the ±γ pairing when summing over γ>0). Statement written with the sum over all ρ: consistent. PROVED.
- **def:W.** It is the class of weights 𝒲 / ν_w, not a normalization of W_T; λ^W is defined in eq:W (λ^W = inf W_T over 𝒟_T, ‖F‖=1). Upper bound by F* ∈ c^⊥ normalized: valid for λ^W. λ_A is not touched.
- **lem:combsine / rem:chiev-sine.** e_k = (−1)^{(k−1)/2}T^{−1/2}cos ω_k x (k odd); ∫cos ωx cos zx = sin((ω−z)T)/(ω−z)+sin((ω+z)T)/(ω+z), with cos ωT=0 giving sinωT·cos zT·2ω/(ω²−z²) ⇒ Φ_k = T^{−1/2}cos(zT)·2ω_k/(ω_k²−z²). At ρ=1 (z=−i/2): 2ω_k cosh(T/2)/(√T(¼+ω_k²)) = c_k from rem:chiev-sine. ✓
- **rem:finitesign.** N(T)=⌈2Tt₀/π⌉−1 and 𝔄_ev match its notation. c^⊥ has codim 1 in the block ⇒ n₋ ≤ 1 (not "=1").
- **cor:margin1/eq:closedmargin.** At T=4: 4·10⁹·4·e^{−61.8} ≈ 2·10⁻¹⁷ ✓; correct comparison (both upper bounds of λ^W).
- **Mori.** P46 cites \cite{Mori15} with λ^W ≥ 2^{−2904}; the 2.4·10⁻⁷⁰ is the even minimum of the reproduced Arb certificate (AUDIT_ZENODO_FRONTIER). Worded as "Arb certificate of Mori15 (stated bound 2^{−2904}) gives even minimum ≥ 2.4·10⁻⁷⁰", a lower bound, not "≈". "without floor / infimum 0" withdrawn.
- lem:archcount, cor:H1minus, prop:H: not used in the proof of the remark; no conflict (prop:H is not invoked).

## 2. Changes to main.tex
1. New `\begin{remark}...\label{rem:zcert}` between rem:finitesign and prop:H (§11, rem. 11.13, p. 73): identity on c^⊥, closed-form Φ_k, method (2000 Arb zeros, Cholesky on balls, τ ≤ 3·10⁻³³ with H=3·10¹² and Trudgian 2.510), result n₋ ≤ 1 on the grid {0.75,…,4.24}∪{4.245} (double precision), 2N/4N blocks, continuum OPEN, fails at N=16→17 due to margin, rate 22→28 and T*≈3 log H/26 (numerical), byproduct λ^W_4 ≤ 1.47·10⁻³¹, λ^W_{4.2} ≤ 3.05·10⁻³² (proved given cited inputs; not λ_A).
2. `\bibitem{Trudgian2014}` after Titchmarsh1986 (alphabetical order).
3. Verified existing entries: Johansson2017 (IEEE Trans. Comput. 66 (2017) 1281–1292) and PlattTrudgian2021 (Bull. LMS 53 (2021) 792–797). Correct.

## 3. Compilation
pdflatex ×2: 0 errors, 0 undefined references/citations, 192 pages.

Labels: identity and Φ_k PROVED; node on the grid PROVED given CITED; continuum OPEN; rate/T* NUMERICAL.
