# L2_BUILD_013 — The Euler cone paired with primitive autocorrelations: dies

## Corpus check
N_BUILD_007 (cone 𝒦_T^* dual to primitive autocorrelations; δ₀, δ₀ ± δ_a, e^{−u/2}du ∈ 𝒦_T^*; δ_a ∉ ±𝒦_T^*; convolution
by δ_a does not preserve 𝒦_T^*; resolvent order-indefinite), R186_052 (𝒦^{(0)*} via Kreĭn, conditional), Paper 46
rem:nyq-dual, 011 row 8 (a_P), 012. No memo on exp(ν) for ν ≥ 0 on prime powers paired with c_F.

## 0. Convention reconciliation with the (N) track (PROVED both)
Two exact splits of the s = ½ integer comb Z := Σ_{n<N} n^{−½}δ_{log n} in 𝔄_T:
 (mine, 012)  M₁ := ½δ₀ + e^{u/2}du: 𝓛M₁ = ½ + 1/(z−½) = (z+3/2)/(2(z−½)); M₁^{−1} ↔ 2(z−½)/(z+3/2) = 2 − 4/(z+3/2),
              M₁^{−1} = 2δ₀ − 4e^{−3u/2}du; −∂_s log M₁ ↔ 2/((z−½)(z+3/2)) = 1/(z−½) − 1/(z+3/2) → (e^{u/2} − e^{−3u/2})du.
 (N_BUILD_007) M₂ := δ₀ + e^{u/2}du: 𝓛M₂ = (z+½)/(z−½); M₂^{−1} ↔ 1 − 1/(z+½), M₂^{−1} = δ₀ − e^{−u/2}du;
              −∂_s log M₂ ↔ 1/((z−½)(z+½)) = 1/(z−½) − 1/(z+½) → (e^{u/2} − e^{−u/2})du.
(Here −∂_s acts on e^{(1−s)u} giving u e^{u/2}, 𝓛 = 1/(z−½)²; δ₀ has no s-dependence.) Both correct.
Bookkeeping on P_T (N_BUILD_001 (A): 2∫₀^{2T}c_F e^{u/2} = −𝔭, 2∫₀^{2T}c_F e^{−u/2} = +𝔭, 𝔭 = (1/2π)∫|F̂|²/(¼+τ²);
2∫₀^{2T}c_F e^{−3u/2} = (1/2π)∫|F̂|²·3/(9/4+τ²)):
 𝔞_T = (1/2π)∫m^♯|F̂|² − 2⟨R^♯,c_F⟩, m^♯ = m + 1/(¼+τ²), R^♯ = comb − e^{u/2}du           (N_BUILD_001)
     = (1/2π)∫m^♭₁|F̂|² − 2⟨R₁,c_F⟩, m^♭₁ = m^♯ + 3/(9/4+τ²), R₁ = R^♯ + e^{−3u/2}du         (012)
     = (1/2π)∫m^♭₂|F̂|² − 2⟨R₂,c_F⟩, m^♭₂ = m^♯ + 1/(¼+τ²) = m + 2/(¼+τ²), R₂ = R^♯ + e^{−u/2}du.
m^♭₁(0) = C₀ + 16/3 ≈ −0.039; m^♭₂(0) = C₀ + 8 ≈ +2.63. The three agree (totals identical). 
**Proposition 0 (PROVED): the "archimedean slack" is not an invariant.** For every positive-definite causal kernel
k (k̂ ≥ 0) and c > 0, 𝔞_T = (1/2π)∫(m^♯ + c k̂)|F̂|² − 2⟨R^♯ + (c/2)k, c_F⟩. So the value of the archimedean symbol at 0
can be made arbitrarily positive by moving a positive-definite kernel into the remainder. Only 𝔞_T itself is
invariant; statements "slack δ" are meaningful only together with a bound on the corresponding remainder.

## 1. The Euler cone and its first check against a_P — NO-GO (PROVED)
𝓔 := {exp(ν) ∈ 𝔄_T : ν ≥ 0 supported on {k log p}}. Z ∈ 𝓔 (log Z = Σ Λ(n)/log n · n^{−½}δ_{log n} ≥ 0).
Also Z^{a_P} = exp(ν_{a_P}) ∈ 𝓔 (ν_{a_P} = ν_Z restricted to powers of p ≥ P). Any statement "property of all of 𝓔"
holds for a_P, which fails WP_T at 0.60 ≤ T ≤ ½log P (011 row 8). By transfer, no class statement about 𝓔 implies WP_T
there. ∎ (This is the requirement the coordinator asked to check first; 𝓔 alone is Euler-without-FE.)

## 2. Full-cone positivity is false — NO-GO (PROVED, uses N_BUILD_007 §1(iv))
Claim: 𝓔 ⊄ 𝒦_T^* for 2T > log 2. Take ν = tδ_{log 2}, K := max{k : k log 2 < 2T} ≥ 1. exp(ν) = Σ_{k≤K} (t^k/k!)δ_{k log 2}.
By N_BUILD_007 §1(iv) there is F ∈ P_T with Re c_F(K log 2) < 0. Then ⟨exp(tδ_{log 2}), c_F⟩ = Σ_k (t^k/k!)Re c_F(k log 2)
is a polynomial in t with negative leading coefficient, hence < 0 for large t. ∎
So the isolated atom at log 2 kills the Euler cone immediately, as the coordinator suspected.

## 3. Even restricted versions do not see the sign (PROVED)
Restrict to the order interval 𝓔_Z := {exp(ν): 0 ≤ ν ≤ ν_Z}. (a) It contains Z^{a_P} (transfer NO-GO of §1 applies).
(b) Pairings of exp(αν) with c_F are ‖F‖² + α⟨ν,c_F⟩ + O(α²): positivity of ⟨exp(·),c_F⟩ near α = 0 gives no
information on the sign of the linear pairing ⟨ν,c_F⟩ (the δ₀ term ‖F‖² dominates). And the window form is linear in
the comb −∂_s log Z = −∂_s ν_Z; an exp-pairing inequality reaches it only through the derivative at α = 0, where it is
vacuous. ∎

## 4. Review
- §0: both inversions re-derived by Laplace; the bookkeeping identity is the trivial add-and-subtract; Proposition 0
  is correct and important: it retracts any reading of m^♭₁(0) ≈ −0.039 (012) as "small residual slack". PROVED.
- §2 depends on N_BUILD_007 §1(iv) (PROVED there; I did not re-derive it). Label PROVED (modulo that citation).
- §3(b) is elementary. Verdict: Euler cone dead in three independent ways. No sign contact.
