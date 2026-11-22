# L2_BUILD_022 — Large deviations for the random clamped-span matrix; ζ's matrix in the same coordinates

Setting of 021 §1 (Poisson comb, intensity ρ(u) = κe^u/u on (log 2, ∞), weights w(u) = 2u e^{−u/2}, mean measure 2κe^{u/2}du).
For F ∈ P_T put f_F(u) := w(u)Re c_F(u). Random form: 𝔞^ν(F) = 𝔞_∞(F) − Σ_j f_F(u_j). 021 is not edited (under review).

## Corpus check
021 (Campbell mean/variance, CLT at φ₀), 009/010 (Z_T(φ₀) identity, centre criticality), Paper 46 Thm Z / lem:roughEF (explicit formula
as identity), thm:finZ, R186_114 Lemma A (Tate correction of size e^{−T′}). grep "Laplace functional / Chernoff / exponential moment of the
Weil form / independent lag windows": none. New: §1–§4.

## 1. Exact exponential moments (PROVED; Laplace functional of a Poisson process, CITED)
For θ ∈ ℝ: 𝔼 exp(θΣ_jf_F(u_j)) = exp(∫(e^{θf_F(u)} − 1)ρ(u)du) (finite: f_F bounded, ρ integrable on (log 2, 2T)). Hence for every F:
  P(𝔞^ν(F) ≥ 0) = P(Σf_F ≤ 𝔞_∞(F)) ≤ inf_{θ>0} exp(θ𝔞_∞(F) + ∫(e^{−θf_F} − 1)ρ du).            (C1)
  P(𝔞^ν(F) < 0) ≤ inf_{θ>0} exp(−θ𝔞_∞(F) + ∫(e^{θf_F} − 1)ρ du).                                    (C2)

## 2. What linear-functional bounds can and cannot give (PROVED)
(a) Positivity of M := (𝔞^ν restricted to a subspace H) implies 𝔞^ν(F) ≥ 0 for every F ∈ H; so P(M ⪰ 0) ≤ inf_{F∈H} P(𝔞^ν(F) ≥ 0).
(b) For H = clamped span of low modes (dimension d ≍ T), every unit F ∈ H is low-frequency with Var(Σf_F) = 4κ∫u(Re c_F)²du ≍ T² and
    |𝔼𝔞^ν(F)| = O(1) (021 §2); the CLT gives P(𝔞^ν(F) ≥ 0) → ½ uniformly on H (Lyapunov ratio O(T^{−3}), uniform since the shapes
    c̃_F range over a compact set of smooth functions for fixed mode cutoff). Hence the best bound obtainable from (a) and (C1) is
    P(M ⪰ 0) ≤ ½ + o(1).
(c) A union bound over a net of the sphere of H bounds P(∃F: 𝔞^ν(F) < 0) from above — the wrong direction for an upper bound on
    P(M ⪰ 0). **NO-GO (PROVED): exponential moments of single linear functionals plus nets cannot give P(M ⪰ 0) → 0 on the clamped
    span faster than ½ + o(1).** Decay needs independence across several functionals.

## 3. Independence route (PROVED reduction; construction OPEN)
Poisson functionals Σf_k(u_j) with disjointly supported f_k are independent (CITED: complete independence of Poisson processes on
disjoint sets). If F_1, …, F_K ∈ P_T have f_{F_k} supported (on (log 2, 2T)) in pairwise disjoint lag windows I_k, then
  P(λ_A(T; ν) ≥ 0) ≤ Π_k P(𝔞^ν(F_k) ≥ 0),
and if each factor ≤ 1 − c, P ≤ e^{−cK}. With windows of fixed length, K ≍ T: a rate exp(−cT). Obstruction to construct F_k: f_F always
contains the lags near 0 (c_F(0) = ‖F‖²) and the Tate correction of a two-bump test at separation D carries moments of size e^{D/2}
(N_BUILD_001 (A): the polar density is converted into +κ𝔭 on P_T, so the e^{D/2} mean must be cancelled by the correction, which then
spreads f_F over many lags). Whether F_k ∈ P_T with lag-disjoint random parts and means ≲ standard deviations exist: OPEN. If yes,
rate exp(−cT) for κ = 1 and for every κ > κ* alike (density changes the means by O(1), fluctuations are ≍ √(lag window mass)).
The GOE-type rate exp(−cd²) ≍ exp(−cT²) of 021 §3 is NOT obtained; it remains ARGUED only.

## 4. ζ's clamped-span matrix in the same coordinates (identity; sizes CITED/ARGUED)
For F, G in the clamped span H ⊂ P_T, the explicit formula as an IDENTITY (Paper 46 Thm Z / lem:roughEF, CITED; polar terms vanish on P_T):
  𝔞_ζ(F, G) = Σ_ρ F̂(γ_ρ)·conj(Ĝ(conj γ_ρ)),  γ_ρ := −i(ρ − ½).
Mean in the Poisson coordinates: 𝔼𝔞^ν(F, G) = (1/2π)∫ m^♯ F̂ conj Ĝ dτ (κ = 1), entries O(1). So ζ's "fluctuation matrix" is
  X_ζ := 𝔞_ζ − 𝔼𝔞^ν = Z − M₀,  Z_{FG} = Σ_ρ F̂(γ_ρ)conj Ĝ(conj γ_ρ),  M₀ = m^♯-form.
Size of Z on H: low modes have |F̂(γ)| ≲ T(γT)^{−3}·(γ² + ¼)² ... (008 §2b: Ĝ ≍ T(γT)^{−3}, F̂ = (γ²+¼)Ĝ), so the contribution of zeros
on the line with |γ| ≥ 14 is O(T^{−4}) per entry (Σ_ρ γ^{−2} log γ convergent; CITED density of zeros). For windows T with
e^{T} ≪ H^{c} (H = height to which all zeros are verified on the line, CITED Platt–Trudgian), off-line zeros above H contribute
≤ e^{T}Σ_{γ>H}(…)γ^{−2} — ARGUED negligible. Hence, in that range, **X_ζ = −M₀ + O(T^{−4}): ζ's fluctuation on the clamped span is
O(1)**, whereas a Poisson comb's is ≍ T (021 §2).
Distance from the ensemble (ARGUED): the event "‖X_ν + M₀‖ = O(1) on H" (Poisson fluctuation within O(1) of a prescribed matrix) has
probability ≈ Π over d asymptotically independent directions of O(1/T) (local CLT) ≈ exp(−d log T) ≈ exp(−cT log T). So in the
verified range ζ's comb is "super-regular" on low modes — like the lattice combs of 018 — and an exp(−cT log T) outlier relative to
density-matched Poisson combs. (This uses verified zeros as data only; it is not used to infer anything about other windows.)

## 5. Review
- §1 standard. §2(b) uniformity of the CLT over H: shapes of low modes vary in a compact family for a fixed number of modes; for
  d ≍ T modes the uniformity is ARGUED. The NO-GO §2(c) is a statement about the method (single functionals + nets) and is correct.
- §3 reduction is correct (independence on disjoint sets); the construction is OPEN with a clearly identified obstacle (Tate correction).
- §4: the identity is CITED; the O(T^{−4}) size for on-line zeros uses decay of the cos² clamped mode, exact minimizer ARGUED; the off-line
  tail beyond H is ARGUED; the "exp(−cT log T)" distance is ARGUED (independence of directions not proved). Labels kept.
- Important honesty point: §4 does not prove anything about ζ's sign; it measures, with verified-zero data in a finite range, how far
  ζ's low-mode matrix is from random density-matched combs. No sign certified; no negative value of 𝔞_T for ζ.
