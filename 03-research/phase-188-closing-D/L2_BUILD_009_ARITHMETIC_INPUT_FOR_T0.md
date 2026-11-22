# L2_BUILD_009 — Arithmetic input for 𝒯₀: what actual Λ can and cannot give

## Corpus check
Paper 46 thm:finZ (no finite zero set carries a flat-top certificate), cor:void (classes C_PNT(ε),
C_zeros, C_BT decide no window T > 0.75), prop:wit-sens, rem:wit-cheb; MEMORY "zero-side reverse
engineering always negative"; R186_033 (PNT-window identity); N_BUILD_001 (F) (no F-uniform bound).
Nothing tests a single fixed clamped mode with a fourth-order smoothed Chebyshev functional.

## 1. Three candidate inputs and their fate
(i) PNT with classical error, ψ(x) − x ≪ x exp(−c√log x): after four integrations by parts (008 §4) the
    fluctuation term is bounded by ∫|ψ̃ − 2e^{u/2}|·|𝓖^{(4)}|… ≪ e^{T}exp(−c√T)‖φ₀‖², which exceeds |C₀+4|‖φ₀‖²
    for large T. Gives no sign. NO-GO by cor:void (class C_PNT) — PROVED there.
(ii) Finitely many verified zeros (CITED: zeros on the line up to height H) via the explicit formula
    𝔞_T(F) = zero sum: for smooth F ∈ P_T the verified zeros contribute ≥ 0 and the remaining zeros at
    most e^{T}‖F^{(N)}‖₁²·H^{1−2N}log H in absolute value (|F̂(γ)| ≤ e^{T/2}‖F^{(N)}‖₁|γ|^{−N} for |Im γ| ≤ ½).
    This gives 𝔞_T(F) ≥ −(small), never ≥ 0, and needs smooth F — the ground state φ₀ is only ARGUED
    smooth (008 §2b). Within class "finite zero data", thm:finZ is the matching NO-GO for certificates.
    Status for the single test: a NEAR-test 𝔞_T(φ₀) ≥ −ε(T,H), PROVED for smooth near-minimizers
    (cos² modes), useless for the sign. Not pursued (also numerics would be needed to use it).
(iii) Exact multiplicative structure: (¼ − ∂²)² dψ̃ on [0, 2T] is the measure Σ Λ(n)n^{−1/2}(¼−∂²)²δ_{log n}.
    Its pairing with the positive-definite 𝓖 is Σ_n Λ(n)n^{−1/2}[(¼−∂²)²𝓖](log n) — the original sum; no
    cancellation is created by rewriting. An Euler-specific identity would have to give a sign to
    Σ_n Λ(n)n^{−1/2}h(log n) for the specific h = (¼−∂²)²𝓖 with 𝓖 = autocorrelation of a clamped mode.
    Such h is a "Tate-annihilated positive-definite" test: ĥ(τ) = (τ²+¼)²|Ĝ(τ)|² ≥ 0 with double zeros at ±i/2.

## 2. Proposition (PROVED): reduction of 𝒯₀ to a one-function Chebyshev inequality
For every T,
  Σ_n 2Λ(n)n^{−1/2} h_T(log n) ≤ μ₀(T),  h_T := (¼ − ∂²)²(𝓖_{G₀}),  ‖φ₀‖ = 1,
where G₀ ∈ H²_0(I_T) is the clamped ground mode (008 §1–§3). Proof: 008 §3–§4 (v_n = 2Λ(n)/√n). ∎
Right side < 0 for T > ½log5 (CITED, 006). The left side is a Weil-type explicit sum with test ĥ_T ≥ 0 on ℝ
vanishing to order 2 at ±i/2.

## 3. What is missing (OPEN), stated sharply
(Ω₀) For every T > ½log5: Σ_n 2Λ(n)n^{−1/2}h_T(log n) < 0 for the clamped ground test h_T.
By cor:void, any proof must use a property of Λ not shared by its finite modifications preserving PNT
asymptotics; by (i)–(ii) neither PNT-type error terms nor finitely many zeros suffice. (Ω₀) is the
(L2)/(N) meeting point at its smallest possible size: one test function per window.

## 4. Review
- §1(i): correct direction; the constant tracking after integration by parts is schematic but the
  conclusion follows from cor:void anyway. (ii): bound on off-line zeros uses |Im γ| ≤ ½ and N(H) ~ H log H;
  standard; CITED inputs. (iii) is an observation.
- §2 is exact given 008. (Ω₀) is NECESSARY for (L2) at each T, not sufficient (007 §3; rem:bar-loc).
- No sign certified, no negative value of 𝔞_T. This track has reached a statement that is the same kind
  as (N)'s first case (E_γ); further progress requires the arithmetic input the track (N) is building.
