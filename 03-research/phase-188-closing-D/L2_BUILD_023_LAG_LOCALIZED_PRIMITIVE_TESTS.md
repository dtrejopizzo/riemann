# L2_BUILD_023 — Lag-localized primitive tests: a standalone lemma, exact polar/archimedean cancellations, independence and a
# rigorous large-deviation rate exp(−c T log T); two-sided sharpening of N_BUILD_014 Theorem A

## Corpus check
N_BUILD_014 §1 (two-copy identity F₀ + τ_dF₀, PNT main term vanishes since Re(AB̄)(F₀) = 0, archimedean cross term O(e^{−d/2}),
Theorem A / Cor A′ one-sided (Ξ)); Paper 46 thm:nyq-cone (F = (¼−∂²)G), lem:wit-freeze (extension by zero); R160_D4 Thm 5.1
(translations); L2_BUILD_022 §3 (independence route, obstacle = Tate correction). New here: (L) the general lag-localization lemma with
the observation that NO Tate correction is needed for translates; (C) the exact cancellation of the k = 0 archimedean term and of the
whole polar kernel (cross terms O(e^{−5d/2}), not O(e^{−d/2})); (T) two-sided version of (Ξ); (P) rigorous rate for random combs.

## 1. Lemma L (lag localization; PROVED)
Let T₀ > 0, G₀ ∈ H²_0(I_{T₀}) real, F₀ := (¼ − ∂²)G₀ (so F₀ ∈ P_{T₀}, thm:nyq-cone), c₀ := c_{F₀}, supp c₀ ⊂ [−2T₀, 2T₀].
For translations a_1 < … < a_K and real s_k, put F := Σ_k s_k τ_{a_k}F₀. Then:
(i) F ∈ P_T for every T with I_T ⊃ ∪_k(a_k + I_{T₀}) — no correction: A(τ_aF₀) = e^{a/2}A(F₀) = 0, B(τ_aF₀) = e^{−a/2}B(F₀) = 0.
(ii) c_F(u) = Σ_{k,l}s_ks_l c₀(u − (a_k − a_l)); supp c_F ⊂ ∪_{k,l}[a_k − a_l − 2T₀, a_k − a_l + 2T₀] (difference set + [−2T₀,2T₀]) — optimal:
    each window is attained when s_ks_l ≠ 0 and c₀ ≢ 0 near ±2T₀.
(iii) If 2T₀ < log 2, the central window [−2T₀, 2T₀] contains no comb atom (atoms at log n ≥ log 2): near-0 lags carry only the
    archimedean energy Σ s_k² 𝔞_∞(F₀).
(iv) Exact moment cancellation in every off-diagonal window: for any D, ∫c₀(u − D)e^{±u/2}du = e^{±D/2}∫c₀(v)e^{±v/2}dv = e^{±D/2}A(F₀)B(F₀) = 0.
    Hence the PNT/polar density 2κe^{u/2} contributes 0 in each window: the "e^{D/2} moment cost" is exactly 0 (the obstacle of 022 §3
    disappears).
*Proof.* (i) translation of the Tate integrals; (ii) bilinearity of c; (iv) ∫∫F₀(t)F₀(t−v)e^{v/2}dvdt = A(F₀)·B(F₀). ∎

## 2. Lemma C (exact cancellation of the archimedean and polar cross terms; PROVED)
For d > 4T₀ (disjoint copies, lags v + d > 0), with K(u) = 2Σ_{k≥0}e^{−(2k+½)u} (lem:K):
  ∫c₀(v)K(v + d)dv = 2Σ_{k≥1}e^{−(2k+½)d}∫c₀(v)e^{−(2k+½)v}dv,  |·| ≤ 2e^{−5(d−2T₀)/2}·4T₀/(1 − e^{−4(d−2T₀)})·…  = O(e^{−5d/2+5T₀}),
because the k = 0 term is 2e^{−d/2}∫c₀(v)e^{−v/2}dv = 0 by Lemma L(iv) (c₀ even). And the polar kernel of κ/(¼+τ²) is κe^{−|u|/2}, whose
cross term κe^{−d/2}∫c₀e^{−v/2} = 0 exactly. So N_BUILD_014's archimedean cross term O(e^{−d/2}) improves to O(e^{−5d/2}), and the
G_κ cross term vanishes up to O(e^{−5d/2}). ∎

## 3. Theorem T (two-sided local fluctuation bound; PROVED — sharpens N_BUILD_014 Cor A′)
Let F₀ be as in Lemma L, ‖F₀‖ = 1, a₀ := 𝔞_{T₀}(F₀), and X(d) := Ξ(d) + ∫c₀(v)K(v+d)dv with Ξ(d) := Σ_n v_n c₀(log n − d) (N_BUILD_014).
For every s ∈ ℝ and T ≥ T₀ + d/2: 𝔞_T(F₀ + sτ_dF₀) = (1 + s²)a₀ − sX(d). Hence
  𝔞_T ⪰ 0 on span{F₀, τ_dF₀} ⟺ |X(d)| ≤ 2a₀.
Consequently the target (λ_A ≥ 0 ∀T) implies, for every T₀, F₀, and d > 4T₀:
  −2a₀ − O(e^{−5d/2}) ≤ Ξ_{F₀}(d) ≤ 2a₀ + O(e^{−5d/2})     (two-sided (Ξ)),
with a₀ = 𝔞_∞(F₀) when 2T₀ < log 2 (no prime in the central window). N_BUILD_014 had only the upper side (s = 1); s = −1 gives the lower side.
*Proof.* c_{F₀+sτ_dF₀} = (1+s²)c₀ + s(c₀(·−d) + c₀(·+d)); expand eq:Aform as in N_BUILD_014 §1; min over s of (1+s²)a₀ − sX is ≥ 0 iff X² ≤ 4a₀². ∎
Meaning: a smoothed Chebyshev fluctuation of the primes at scale x = e^d, with the main term removed by the Tate conditions, must lie in
the fixed band [−2a₀, 2a₀] at EVERY scale — square-root strength, two-sided, explicit constant.

## 4. Theorem P (random combs: rigorous large deviation; PROVED with CITED Esseen inequality)
Poisson comb of 021 (intensity κe^u/u on (log 2,∞), weights 2ue^{−u/2}), any κ > 0. Fix 2T₀ < log 2 and F₀ with a₀ = 𝔞_∞(F₀) > 0
(e.g. any unit F₀ ∈ P_{T₀}, T₀ < 0.29 < T*_{∞,P}, cor:Tarch CITED). Take lags D_k := 4T₀ + 1 + 4T₀k, k = 1, …, K, with D_K + 2T₀ ≤ 2T − 2T₀.
(a) The random variables X_ν(D_k) are independent (their atom windows [D_k − 2T₀, D_k + 2T₀] are disjoint; Poisson independence, CITED)
    and their means are O(e^{−5D_k/2}) (Lemma L(iv), Lemma C).
(b) Var X_ν(D) = 4κ∫u c₀(u − D)²du ≥ 4κ(D − 2T₀)‖c₀‖₂² =: σ_D².
(c) Concentration (Esseen, CITED: Q(R;λ) ≤ C_E λ∫_{|t|≤1/λ}|φ_R(t)|dt): with φ_R(t) = exp(−∫(1 − cos(t f))ρ), f(u) = 2ue^{−u/2}c₀(u−D),
    1 − cos x ≥ (2/π²)x² for |x| ≤ π, and t·sup f ≤ (D + 2T₀)e^{−(D−2T₀)/2}/(2a₀) ≤ π for D ≥ D*(a₀, T₀):
    P(|X_ν(D)| ≤ 2a₀) ≤ C_E·2a₀∫exp(−(2/π²)t²σ_D²)dt ≤ C_E·2a₀·π^{3/2}/(√2 σ_D) =: C₁ a₀/σ_D.
(d) By Theorem T (positivity on every span{F₀, τ_{D_k}F₀} is necessary) and independence:
  P(λ_A(T; ν) ≥ 0) ≤ Π_{k: D_k ≥ D*} min(1, C₁a₀/(2√(κ(D_k−2T₀))‖c₀‖₂)) ≤ exp(−½Σ_k log(D_k) + K·log(C₁a₀/(2√κ‖c₀‖₂)) + O(1)).
With K ≈ (2T − 4T₀ − 1)/(4T₀) − O(1) ≈ T/(2T₀) and Σ_k log D_k = K log T·(1 + o(1)):  **P(λ_A(T;ν) ≥ 0) ≤ exp(−(1/(4T₀))·T log T·(1 + o(1)))**, for every κ (κ = 1 and κ > κ* alike).
With T₀ ↑ ½log 2 (= 0.3466): rate constant 1/(4T₀) → 1/(2 log 2) ≈ 0.72. Explicit, no GOE analogy. (021 §3's exp(−cT²) is not reached;
this is the rigorous replacement.)

## 5. Comparison with 018 and with ζ
- 018's lattice combs have deterministic |X(D)| = O(quadrature error) ≪ a₀: they satisfy Theorem T trivially; Poisson combs violate it with
  probability 1 − O(1/√D) per scale.
- For ζ, Theorem T is a NECESSARY condition (two-sided (Ξ)) at every scale d. Via the explicit formula as an IDENTITY (Thm Z, CITED),
  X_ζ(d) = Σ_ρ |F̂₀|²-type terms with phases e^{iγd} (on-line zeros) and the bound |X| ≤ Σ_ρ|F̂₀(γ_ρ)|² = a₀ − 0 is what on-line zeros give; this
  is recorded as an identity check only (data/heuristic; not used as a criterion).
- The "super-regularity" of ζ on low modes (022 §4) remains DATA/HEURISTIC only (verified zeros, finite range).

## 6. Review
- Lemma L: correct and simple; the key point (translates of a primitive function are primitive, so the Tate correction is unnecessary) is
  why 022's obstacle disappears. N_BUILD_014 already used it for one translate; the general difference-set form and (iii) are added here.
- Lemma C: the k = 0 cancellation uses evenness of c₀ and ∫c₀e^{v/2} = A(F₀)B(F₀) = 0 — correct. The displayed constant is schematic; O(e^{−5d/2+5T₀}) PROVED.
- Theorem T: exact; strictly stronger than N_014 Cor A′ (adds the lower side). PROVED.
- Theorem P: independence requires the atom sets in disjoint windows (yes) AND that the event {positivity} implies each pair event (yes, by
  Theorem T applied to the 2-dim spans, which are subspaces of P_T for T ≥ T₀ + D_K/2 + …). Esseen's concentration inequality is CITED; the
  Gaussian lower bound for 1 − cos on the relevant t-range verified; D ≥ D* discards O(1) windows. Rate exp(−T log T/(4T₀)) PROVED (count of windows K ≈ T/(2T₀) checked).
- No sign certified for ζ; no negative value of 𝔞_T for ζ.
