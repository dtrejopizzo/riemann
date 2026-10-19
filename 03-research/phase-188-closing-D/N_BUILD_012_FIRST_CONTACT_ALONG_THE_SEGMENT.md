# N_BUILD_012 — First contact along λ_t = (1−t)ρ_κ + tΛ: monotonicity, the trichotomy for t_∞, Euler–Lagrange, and why the sawtooth cannot absorb a fixed fraction

Pen and paper. Notation of N_BUILD_011 (not edited): κ > κ*, g_κ = m + κ/(¼+τ²), η_κ = inf g_κ > 0, κ_t = (1−t)κ + t,
G_κ(F) := (1/2π)∫g_κ|F̂|², 𝔞^♯ = G_1, 𝓕_T Chebyshev fluctuation (N_BUILD_001). On P_T:
 𝔞_t(F) := 𝔞_T^{(λ_t)}(F) = (1−t)G_κ(F) + t(𝔞^♯(F) − 𝓕_T(F)) = (1−t)G_κ(F) + t𝔞_T(F),   b_T(t) := bottom.

## Corpus check
Paper 47 lem:monoT, thm:wit-Tc (i)–(v), lem:wit-freeze, lem:flowdet (Hellmann–Feynman), thm:mult (KKT/Tate multipliers);
N_BUILD_006 Thm 1 (sawtooth O(1 + ‖F′‖²)); L2_BUILD_015 §2 (Hessian in weights). grep "first contact in t|homotopy in the comb|
t*(T)|fraction of the fluctuation": none. New: §1–§4 (the family is new, N_BUILD_011).

## 1. Monotonicity and the limit t_∞ (PROVED)
(a) For fixed t, T ↦ b_T(t) is nonincreasing (extension by zero, as lem:monoT: the comb λ_t paired with c_F does not see
lags ≥ 2T₀ for F supported in I_{T₀}). Hence t*(T) := sup{t ∈ [0,1]: b_T(t) ≥ 0} is nonincreasing in T, t*(T) > 0 (011 §4),
and t_∞ := lim_{T→∞} t*(T) ∈ [0,1] exists.
(b) b_T(t) is concave in t (inf of affine), b_T(0) ≥ η_κ > 0, so {t: b_T(t) ≥ 0} = [0, t*(T)].
(c) **Trichotomy.** (target) ⟺ t*(T) = 1 ∀T ⟺ t_∞ = 1. *Proof.* (⇒) trivial. (⇐) if the target fails, there are T₀ and
F₀ ∈ P_{T₀} with 𝔞_{T₀}(F₀) = −c < 0 (‖F₀‖ = 1); by lem:wit-freeze the same F₀ (extended by zero) gives, for every T ≥ T₀,
𝔞_t(F₀) = (1−t)G_κ(F₀) − tc, independent of T, negative for t > t₁ := G_κ(F₀)/(G_κ(F₀) + c) < 1. So t_∞ ≤ t₁ < 1. ∎
So t_∞ ∈ [0,1) ∪ {1}, with t_∞ = 1 exactly the target, and **"t_∞ > 0" (a fixed fraction of the ℤ-prime fluctuation is
harmless at every window) is a strictly weaker statement**, not equivalent to the target by any argument in the record
(a failing window gives only t_∞ ≤ t₁, with t₁ depending on the witness).

## 2. First contact at t* (PROVED)
Let T be such that t* := t*(T) < 1. Then b_T(t*) = 0 and every minimizer h (‖h‖ = 1, exists: discrete spectrum, L2_007 §1)
satisfies:
(i) Euler–Lagrange on P_T: 𝔞_{t*}(h, G) = 0 for all G ∈ P_T ∩ D_T; on L²(I_T) with Tate multipliers (thm:mult form):
 [(1−t*)g_κ(D) + t*(m^♯(D) − 𝒱^♯_T)]h = β₀e^{t/2} + β₁e^{−t/2} on I_T, (β₀, β₁) ∈ ℂ²,
where 𝒱^♯_T is the operator of 𝓕_T (comb minus polar, compressed);
(ii) balance: t*𝓕_T(h) = (1−t*)G_κ(h) + t*𝔞^♯(h), i.e. **𝓕_T(h) − 𝔞^♯(h) = ((1−t*)/t*)G_κ(h) ≥ ((1−t*)/t*)η_κ > 0**;
(iii) Hellmann–Feynman (lem:flowdet, simple bottom): b_T′(t*) = −G_κ(h) + 𝔞_T(h) = −G_κ(h) − (1/t*)·0 + … precisely
b_T′(t*) = 𝔞_T(h) − G_κ(h) = −G_κ(h)/t* < 0 (using (ii)): the crossing is transversal.
Reading: at first contact the minimizer is an F on which the ℤ-prime fluctuation exceeds the ξ-normalized archimedean form by
the explicit positive amount ((1−t*)/t*)G_κ(h). t_∞ > 0 ⟺ such an excess, relative to G_κ, is bounded uniformly in T:
 **(Ω_{t₀}) sup_{T, F ∈ P_T} [𝓕_T(F) − 𝔞^♯(F)]₊ / G_κ(F) < ∞**, and then t_∞ ≥ 1/(1 + sup).

## 3. Can the N_BUILD_006 decomposition give (Ω_{t₀})? NO (PROVED + CITED)
(a) Norm mismatch (PROVED). The controlled (sawtooth) part is bounded by C(1 + ‖F′‖²) (006 Thm 1); G_κ(F) ≍ ∫log(2+|τ|)|F̂|²
(m ~ log|τ|, lem:mbounds). For wave packets at frequency τ (F ∈ P_T after Tate projection, as in L2_005 §3(b)),
‖F′‖² ≍ τ²‖F‖² while G_κ ≍ log τ‖F‖²: the controlled part is not bounded by any multiple of G_κ uniformly in τ.
(b) The mismatch is real, not an artefact of the bound (CITED + ARGUED). For a packet of support length 2L at frequency τ,
⟨Z, c_F⟩ is the real part of a smoothed Dirichlet polynomial Σ_{n<e^{2L}} n^{−½−iτ}w(log n), which for e^{2L} ≫ τ approximates
ζ(½+iτ) up to O(1) (approximate functional equation with smooth weights, CITED); and max_{τ≤X}|ζ(½+iτ)| ≥ exp(c√(log X/log log X))
(Balasubramanian–Ramachandra / Montgomery-type Ω results, CITED). So the integer comb's pairing exceeds any multiple of log τ on
suitable packets. (Whether this transfers to 𝓕_T with the right sign goes through log Z — non-additive — and is not settled.)
(c) Non-additivity (PROVED, 005/006): the comb is 2⟨L, f^μ⟩ = −∂_s log(M + B) paired with c_F; there is no splitting of 𝓕_T into
"sawtooth part + rest" with the sawtooth part entering linearly. So "the sawtooth absorbs a fixed fraction of the deficit" has no
formulation inside this decomposition.
**NO-GO: the Möbius/Euler–Maclaurin decomposition of N_BUILD_006 does not yield t*(T) ≥ t₀ > 0 uniformly.**

## 4. What can be proved for t* (PROVED, weak)
t*(T) ≥ η_κ/(η_κ + A_T + 4 + |C₀+4|) (011 §4, crude: |𝓕_T| ≤ (A_T + 4)‖F‖², 𝔞^♯ ≥ (C₀+4)‖F‖²). Improvement by frequency splitting
fails for the same reason as §3(a): the only available two-sided bound on 𝓕_T at frequency Ω is A_T (comb) or C(1+Ω²) (sawtooth);
neither is O(log Ω) uniformly. So t*(T) ≥ c e^{−T} is the best pen-and-paper statement here.

## 5. Status and next step
(Ω_{t₀}) is a new, strictly weaker target than (N) (by §1(c)). It asks for a one-sided bound of the ℤ-prime fluctuation by a
constant multiple of the log-archimedean energy plus the positive margin η_κ, uniform in T. Its high-frequency part is the
statement "𝓕_T(F) ≤ C∫log(2+|τ|)|F̂|²" for packets — a one-sided, smoothed twisted-Chebyshev bound with LOGARITHMIC loss at height τ
(not exponent-½ at fixed height): the natural next memo is to test it on packets at fixed τ as T → ∞ (that is (E_γ) with a factor C:
limsup 𝓕_T(F_T^γ)/‖F_T^γ‖² ≤ C·g_κ(γ) + 𝔞^♯-term), i.e. (E_γ) weakened by a constant — "(E_γ, C)". Problem (A) of 011 after that.

## Self-review
1. §1(a): monotonicity for a general comb: the proof of lem:monoT uses only that c_F vanishes beyond 2T and the comb is a fixed
measure — correct for λ_t. §1(c): uses lem:wit-freeze for Λ and the explicit formula of 𝔞_t — correct; note it shows t_∞ < 1 if
the target fails, not t_∞ = 0.
2. §2(iii): first draft wrote a garbled derivative; corrected: d/dt 𝔞_t(h) = 𝔞_T(h) − G_κ(h), and at t* 𝔞_T(h) = −((1−t*)/t*)G_κ(h),
so b′ = −G_κ(h)/t*. Transversality requires a simple bottom (stated).
3. §3(b) relies on CITED analytic number theory and an AFE approximation; labelled ARGUED for the transfer; §3(a), (c) PROVED.
4. No claim that t_∞ > 0 is true or false.
No sign contact (for Λ); no negative value certified.
