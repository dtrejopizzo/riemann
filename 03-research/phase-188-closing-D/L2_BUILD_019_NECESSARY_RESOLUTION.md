# L2_BUILD_019 — Q3: what resolution does pointwise symbol positivity need?

Setting of 018: comb ν = Σ_j ν_jδ_{u_j} ≥ 0 on [0,2T), density g(u) = 2κe^{u/2}, symbol of the window form on P_T:
σ^ν(τ) = g_κ(τ) − Re E(τ), E(τ) = S(τ) − G(τ), S(τ) := Σ_j ν_je^{iτu_j}, G(τ) := ∫_0^{2T}g(u)e^{iτu}du (|G(τ)| ≤ 2κ(e^T+1)/|w|, w = ½+iτ).
Pointwise positivity (PP_T): σ^ν ≥ 0 on ℝ. L2_BUILD_018 is not edited (under referee review).

## Corpus check
Paper 46 subsec:band (negative set U_T of ζ's symbol), prop:wit-sens, rem:wit-cheb (mean-square/large sieve insufficient for (N)),
N_BUILD_011 (κ*), N_BUILD_013 (packet limits exactly critical at every γ: lim = m^♯(γ)), R167_103 (W-sieve), R186_052 (sinc
smoothings). grep "Fejér / mean square of the comb / resonance method / Σν_j²": rem:wit-cheb and phase-167 use large-sieve
mean squares for (N); no memo bounds sup Re E from below for pointwise positivity. §1–§3 new; §4 is a corrected reading.

## 1. Fejér mean-square lower bound (PROVED; no separation hypothesis)
W_Ω(τ) := (1 − |τ|/Ω)_+, Ŵ_Ω(x) := ∫W_Ω(τ)e^{iτx}dτ = Ω(sin(Ωx/2)/(Ωx/2))² ≥ 0. Then
  ∫W_Ω (Re S)² dτ ≥ ½Ω Σ_j ν_j²,  ∫W_Ω Re S dτ = Σ_jν_jŴ_Ω(u_j) ≥ 0.
*Proof.* (Re S)² = ½|S|² + ½Re S²; ∫W|S|² = Σ_{j,k}ν_jν_kŴ(u_j−u_k) ≥ Σ_jν_j²Ŵ(0) = ΩΣν_j² (all terms ≥ 0 since ν ≥ 0, Ŵ ≥ 0);
Re∫WS² = Σν_jν_kŴ(u_j+u_k) ≥ 0. ∎
With G: ∫W(Re E)² ≥ (√(½ΩΣν²) − √(∫|G|²))², ∫|G|² ≤ 4κ²(e^T+1)²∫dτ/(¼+τ²) = 8πκ²(e^T+1)².

## 2. From mean square to the positive side (PROVED, weak)
On |τ| ≤ Ω put B := Σν_j + 4κ(e^T+1) ≥ |Re E|. If f := Re E has W-mean μ_W (normalized by ∫W = Ω) and f ≥ −B, then
sup f ≥ min{B, (⟨f²⟩_W − 2B|μ_W|)/(2B)} (elementary: ⟨f²⟩ ≤ (sup f_+ + B)(⟨f_+⟩ + ⟨f_−⟩) and ⟨f_+⟩ − ⟨f_−⟩ = μ_W).
With ⟨f²⟩_W ≥ ½Σν² − O(κ²e^{2T}/Ω) and Σν ≈ 4κe^T (low-frequency matching), (PP_T) on |τ| ≤ Ω forces
  ½Σν_j² ≲ 16κe^T · max_{|τ|≤Ω} g_κ ≈ 16κe^T log Ω.
If the atoms are δ-separated, N ≤ 2T/δ + 1 and Σν² ≥ (Σν)²/N ≈ 8κ²e^{2T}δ/T, so (PP_T) forces **δ ≲ 4T e^{−T} log(CT/δ)/κ**.
This necessary resolution is only single-exponential: it does NOT reach the sufficient exp(−9κe^T) of 018, and it does not exclude
integer-log resolution δ ≈ 2Te^{−2T}. Q3 as posed (necessity of doubly exponential resolution): OPEN. Obstruction to sharpening:
the passage mean-square → positive sup loses a factor B ≈ e^T (a function can concentrate its variance in rare negative dips).

## 3. Resonance lower bound (PROVED identity; quantitative use OPEN)
For any a_k ≥ 0 and Φ := W_Ω|Σ_ka_ke^{iτu_k}|² ≥ 0:
  sup_{|τ|≤Ω} Re S ≥ [½Σ_{j,k,l}ν_ja_ka_l(Ŵ(u_k−u_l+u_j) + Ŵ(u_k−u_l−u_j))] / [Σ_{k,l}a_ka_lŴ(u_k−u_l)],
every term ≥ 0. The numerator is large only through ADDITIVE triples u_k ≈ u_l ± u_j (within 1/Ω). For positions log n of integers,
these are multiplicative relations n_k ≈ n_l n_j^{±1} — abundant for the full integer comb, absent for primes alone except through
prime powers. So the resonance method is exactly where ℤ's multiplicative structure would enter a necessary-resolution bound;
quantification not attempted here.

## 4. What this means for the ℤ-comb (corrected reading; PROVED with CITED inputs)
(a) For ζ, (PP_T) fails for a reason independent of resolution: κ = 1 < κ* (N_BUILD_011), so g_1(0) = C₀ + 4 < 0 (N_BUILD_001 (B)),
and at low frequency E is small (PNT-scale fluctuation, weighted): the symbol is negative near τ = 0 — consistent with the non-empty
negative set U_T of Paper 46 subsec:band (CITED). The failure is a DENSITY deficit at low frequency, not an aliasing failure.
(b) At the integer resolution frequency Ω ≈ e^{2T}: Σ_n v_n² = Σ 4Λ(n)²/n ≈ 2(2T)² = 8T² (Mertens-type, CITED), so by §1 the RMS of
Re S over |τ| ≲ e^{2T} is ≥ 2T(1 − o(1)), while g_1(Ω) ≈ log(Ω/2π) ≈ 2T. The oscillation of ζ's comb and the archimedean symbol
are of the SAME size at the integer resolution scale: exactly critical, in the mean-square sense — the frequency-space counterpart
of N_BUILD_013 (packet limits critical at every γ) and of L2_BUILD_010 (centre criticality).
(c) Consequence (PROVED as stated): any proof of positivity for ζ must use correlation inside P_T (a) on the low band where g_1 < 0,
i.e. |τ| < τ₁ with g_1(τ₁) = 0 (a fixed band, independent of T), with deficit at most |C₀+4| ≈ 1.37 in the polar-free normalization
(choice-dependent by 013 Prop 0), and (b) at all frequencies up to ≈ e^{2T} at the critical level, where the comb's RMS oscillation
equals the symbol up to lower-order terms. How much of the band (b) must be handled by correlation is not determined by mean squares
(§2 loses e^T); by N_BUILD_013 the packet limits are critical at EVERY γ, so no fixed frequency band can be discarded.

## 5. Review
- §1 correct (Fejér kernel positivity, ν ≥ 0). §2: elementary inequality checked: ⟨f²⟩ = ⟨f_+²⟩ + ⟨f_−²⟩ ≤ sup f_+⟨f_+⟩ + B⟨f_−⟩.
  The derived resolution bound is honest but weak; Q3 remains OPEN. The coordinator's hoped-for "unless δ ≲ exp(−cκe^T)" is NOT proved.
- §3 is the classical resonance identity (Soundararajan-type, CITED idea); correct as an inequality; not quantified.
- §4(a) corrects the framing: integer positions are not where ζ's pointwise positivity fails first; the density deficit κ = 1 < κ* already
  breaks it at low frequency. §4(b) uses a standard Mertens-type estimate (CITED) and is a mean-square statement only.
- No sign certified; no negative value of 𝔞_T for ζ (symbol negativity is not form negativity, Paper 46 thm:nolocal).
