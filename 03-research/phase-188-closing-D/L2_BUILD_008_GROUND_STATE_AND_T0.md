# L2_BUILD_008 — The archimedean ground state of P_T and the test 𝒯₀

Inputs: N_BUILD_001 (read in full): (A) polar elimination, (B) 𝔞_T = 𝔞^♯ − 𝓕_T on P_T with
m^♯ = m + 1/(¼+τ²), m^♯(0) = C₀+4, (C) exact (E_γ), (E) slack λ^♯(T) → C₀+4. Used below as PROVED there.

## Corpus check
grep "H^2_0 / (¼−∂²) / ground state / Tate selects / x^{-1/2} extremal / E_0 / γ = 0":
R186_026 (piecewise Tate Gram) and R166_301 (Toeplitz kernel) use the factorization F̂ = (τ²+¼)Ĝ;
R186_052 gives the weight (τ²+¼)²; Paper 47 prop:wit-Egamma states (E_γ) for γ > 0 only;
rem:coer-nogo gives the x^{-1/2} extremals for sharp blocks. No memo describes the ground state of
𝔞_∞ or 𝔞^♯ on P_T, and none states 𝒯₀ or (E_0). §1 is corpus-known; §2–§5 are new in this form.

## 1. Parametrization of P_T (PROVED; known: Paper 47 thm:nyq-cone, cf. N_BUILD_002 review)
P_T = {F = ¼G − G″ : G ∈ H²_0(I_T)}, ‖F‖² = (1/2π)∫(τ²+¼)²|Ĝ|².
*Proof.* If G ∈ H²_0(I_T) (G, G′ vanish at ±T), then F = ¼G − G″ ∈ L²(I_T) and F̂ = (τ²+¼)Ĝ vanishes at τ = ±i/2,
i.e. ∫F e^{±t/2} = 0. Conversely, for F ∈ P_T put G(t) := −∫_{−T}^{t} 2 sinh((t−s)/2) F(s) ds. Then G = 0 for t ≤ −T, and
G″ = ¼G − F (variation of constants: 2sinh(x/2) is the solution of ¼y − y″ = 0 with y(0) = 0, y′(0) = 1),
so ¼G − G″ = F. For t ≥ T, G(t) = −e^{t/2}∫F e^{−s/2}ds + e^{−t/2}∫F e^{s/2}ds = 0 by the two Tate
conditions; hence G, G′ vanish at ±T and G ∈ H²_0(I_T). ∎

## 2. Description of the ground state (PROVED where marked)
(a) Variational form: with w(τ) = (τ²+¼)²,
  μ₀(T) = min_{G∈H²_0(I_T)} ∫m w|Ĝ|² / ∫w|Ĝ|²,  μ₀^♯(T) = same with m^♯.
The two Tate conditions are encoded entirely by the clamped boundary conditions G(±T) = G′(±T) = 0.
(b) Low-frequency selection (PROVED): μ₀^♯(T) ≤ m^♯(0) + O(T^{−2}): take G(t) = cos²(πt/2T)·c_T ∈ H²_0(I_T);
Ĝ concentrates at scale 1/T and w|Ĝ|² puts mass O(T^{−2}) away from |τ| ≲ 1/T... precisely
∫(m^♯(τ) − m^♯(0))w|Ĝ|²/∫w|Ĝ|² ≤ sup_{|τ|≤R}(m^♯(τ)−m^♯(0)) + (tail of w|Ĝ|² beyond R) with m^♯ − m^♯(0) = O(τ²)
near 0 and |Ĝ(τ)| = O(|τ|^{−3}) (G″ has bounded variation) — giving O(T^{−2}) after the scaling τ ↦ τT. Same for m. ∎
Hence μ₀(T) ≤ C₀ + O(T^{−2}) and the ground state is a LOW-frequency object (concentrated at frequency
scale 1/T): a clamped bending mode G of the full window, F = ¼G − G″. It is not an edge/Hilbert-type
object: the x^{−1/2} extremals of rem:coer-nogo live at high frequency (cost log τ) and are not
competitive for the bottom. (Edge regularity of the exact minimizer: ARGUED only — the Euler–Lagrange
equation is m^♯(D)w(D)G = μ w(D)G + boundary terms, a log-order pseudodifferential problem; no closed form.)
(c) Negative eigenspace (PROVED count lower bound, ARGUED upper): every G in the span of the first J
clamped modes with frequency ≲ τ_* where m(τ_*) = 0 gives 𝔞_∞ < 0, so n_∞(T) ≳ (2T/π)τ_* (Weyl, ARGUED);
τ_* is the positive zero of m (m(0) = C₀ < 0, m increasing, m → ∞). n_∞(T) grows linearly in T.

## 3. 𝒯₀ is positivity at one vector (PROVED)
𝒯₀(T): Σ v_n Re𝓕_{φ₀}(log n) ≤ μ₀(T) ⟺ 𝔞_T(φ₀) ≥ 0, since 𝔞_T(φ₀) = μ₀ − Σ v_n Re𝓕_{φ₀}(log n). In polar-free form
(N_BUILD_001 (B)): ⟺ 𝓕_T(φ₀) ≤ 𝔞^♯(φ₀). Extension to the negative space: ⟺ 𝔞_T ⪰ 0 on span{φ_j: μ_j<0}
— a compression; necessary, not sufficient (007 §3).

## 4. Structural form of 𝓕_{φ₀}(log n) (PROVED)
With F = ¼G − G″, 𝓕_F(u) = ∫F(t)F(t−u)dt = (¼ − ∂_u²)² 𝓖(u), 𝓖 := G ⋆ G̃ (autocorrelation of G, an even
function in C³ supported in [−2T, 2T] with 𝓖, 𝓖′ … vanishing at ±2T to order 3). Proof: F̂ = (τ²+¼)Ĝ, so
|F̂|² = (τ²+¼)²|Ĝ|²; invert. ∎ Hence
  Σ v_n Re𝓕(log n) = Σ v_n [(¼ − ∂²)²𝓖](log n) = 2∫_0^{2T}[(¼−∂²)²𝓖](u) dψ̃(u),  ψ̃(u) = Σ_{log n ≤ u} Λ(n)n^{−1/2},
and integrating by parts four times moves the operator onto the measure: the prime sum is the pairing of
the smooth, positive-definite 𝓖 with (¼ − ∂²)² applied to the Chebyshev measure dψ̃. The main term
2e^{u/2}du of dψ̃ is annihilated: (¼ − ∂²)e^{u/2} = 0 — this is the polar elimination (A) at the level of
measures. So
  Σ v_n Re𝓕_{φ₀}(log n) = −𝔭(φ₀) + 2∫_0^{2T}𝓖(u)·[(¼ − ∂²)²(dψ̃ − e^{u/2}du)](u) + (boundary terms at u = 0).
(Boundary terms at 2T vanish by the clamped conditions; at u = 0 they are explicit in 𝓖^{(j)}(0); not
computed here.)

## 5. Asymptotic test = (E_0) (PROVED reduction)
Along the family φ₀(T) (low-frequency, §2b), 𝒯₀ for all large T is the γ = 0 member of (E_γ) in the exact
form of N_BUILD_001 (C): limsup 𝓕_T(φ₀)/‖φ₀‖² ≤ m^♯(0) = C₀ + 4 < 0. (Proof: §3 and μ₀^♯ → m^♯(0).)
Paper 47 states (E_γ) for γ > 0 only; (E_0) is the boundary case where the spectral-derivative family
degenerates to the clamped bending mode. It is a statement about the primes alone: the fourth-order
smoothed fluctuation of ψ̃ against a clamped bump of length 2T must be ≤ (C₀+4)‖φ₀‖², strictly negative.

## 6. Review
- §1: correct (variation of constants; Tate ⇔ G vanishes beyond T). Corpus-known.
- §2(b): the O(T^{−2}) needs |Ĝ| decay; cos² gives G″ of bounded variation, so |Ĝ| = O(τ^{−3}), w|Ĝ|² =
  O(τ^{−2}) integrable at ∞ only with the log weight m — ∫ log τ·τ^{−2} converges. OK.
- §2(c) Weyl count ARGUED only. §4 boundary terms at 0 not computed: the formula is complete only up to
  them; label PROVED for the identity 𝓕_F = (¼−∂²)²𝓖 and the annihilation (¼−∂²)e^{u/2} = 0.
- §5: the reduction needs φ₀ to qualify for lem:wit-conc (concentration at a single frequency); §2(b)
  shows near-minimizers do, the exact minimizer is ARGUED to. Label: CONDITIONAL on that concentration.
- No sign certified; no negative value of 𝔞_T.
