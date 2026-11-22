# R186_051 — Coherence functional of the comb: 𝒞₀ on the Nyquist grid, (E_γ) as an object, what the known bounds on Λ give and the exact missing term

Phase 186, round 24. Paper 46, grid and crossword are not touched. Standalone script: `r051_coherence.py` (imports from `r043_wh.py`
only the Legendre discretization; `python3 r051_coherence.py` ≈ 3 min; `… G` only the (E_γ) part). Read: R186_044 (Lemma Q, Prop. K, Lemma P), R186_046 §3, R186_048,
R186_049, R186_114 §1, R186_035 (Lemma 1, cone, Lemma 3.1), R186_050 §3.1, §4 (freezing, adapted family, (E_γ)), §7–8; Paper 46
thm:A/eq:Aform, eq:Kprim, def:PD, lem:mbounds, lem:roughEF, lem:K.

## 0. Verdict

1. **Object.** Three functionals of the symbol σ = (m, Λ|𝒩_T) are defined (§1): the fluctuation measure η_T := Σ_{n<e^{2T}} v_n δ_{log n}
 − 2e^{u/2}du on [0, 2T]; the zero-order coherence 𝒞₀(T, ω) := −Re η̂_T(ω)/(4T) (normalized: a pair of simple zeros
 on the line at ω = γ is worth 1); and the coherence in (γ, slope) 𝔖_T(γ) of R186_050 Def. 4.4, with its finite
 version 𝒞(T) := sup_γ[𝔖_T(γ) − m(γ)]₊ and the exact version 𝒞̃(T) := sup_γ[𝔖_T(γ) − 𝔪_T(γ)]₊ (𝔪_T = archimedean term of the family).
2. **(i) PROVED (Theorem 2.1).** For M₁: 𝒞₀^{M₁}(T, γ₁) − 𝒞₀^ζ(T, γ₁) = 2·sinh(2δT)/(2δT) + ε, |ε| ≤ cosh(2δT)/(γ₁T): grows as
 e^{2δT}/(δT). And 𝔖_T^{M₁}(γ₁) − 𝔖_T^ζ(γ₁) = −Q_δ(F_T)/‖F_T‖² ≥ (3e^{2δT}/(δ²T))(1 − 1/δT)²(1 + o(1)) − 3e^{2δT}/(γ₁²T) (Lemma 2.3,
 PROVED from Lemma Q): grows as e^{2δT}. Measured: 1.30 (T = 5), 13.8 (10), 205 (20), 1645 (30) at δ = 0.1.
3. **But the O(1) separation in the first-contact windows does NOT carry the sign (Prop. 2.2, PROVED).** For T ≤ ½log7, δ ≤ 0.1:
 the difference 𝒞₀^{M₁} − 𝒞₀^ζ is 2 + O(δ²T²) and the 2 is the multiplicity of the triple zero (positive-definite part, Lemma Q);
 the part carrying the sign is 2(g(δT) − 1) = (2δT)²/3 ≤ 1.3·10⁻² (δ = 0.1), 1.3·10⁻⁴ (δ = 0.01). No pointwise functional
 of σ separates witness from non-witness with a larger margin than that in those windows: the pair (M₁(δ), M₁(0)) proves it.
4. **(ii) for ζ.** PROVED (mod. CITED Montgomery–Vaughan): in mean square in ω over [0, Y], Y ≥ e^{2T}:
 RMS 𝒞₀^ζ = ½ + O(1/T) + O(e^{T}/√Y) (Theorem 3.1; measured 0.32–0.41 in the four windows, exact to 3 digits with
 Σv_n²). CITED (Vinogradov–Korobov, Ford): pointwise |𝒞₀^ζ(T, ω)| ≤ C(1+|ω|)e^{T}exp(−0.2098(2T)^{3/5}(log 2T)^{−1/5})/T
 (Theorem 3.2). **What is exactly missing** (Prop. 3.3): going from |ψ(y) − y| ≤ y·e^{−cL(y)} to |ψ(y) − y| ≪ y^{1/2}·(log y)² in
 the twisted form (order-3 Riesz mean at frequency γ): the missing factor is e^{T}·e^{−cT^{3/5}}, i.e. **the whole**
 exponent between 1 − o(1) and ½. There is no intermediate form: (E_γ) for a single γ, by the explicit identity (CITED), already
 is equivalent to absence of quartets at every height (zero side, R186_050 §4.3(iii)). OPEN as a statement about (m, Λ).
5. **(iii).** PROVED: sampling identity (Theorem 4.1, Poisson): for F ∈ L²(I_T), 𝔞_T(F) = (1/4T)Σ_{k∈ℤ}|F̂(kπ/2T)|² s_T(kπ/2T),
 s_T = symbol with the Lévy measure truncated to the window; and E_ψ(F) = Σ_k|F̂(kπ/2T)|² 𝒞₀(T, kπ/2T) (verified to 10⁻⁸ in 12 tests).
 So the form only sees the symbol on the Nyquist grid ω_k = kπ/2T weighted by the samples |F̂(ω_k)|². **The weak
 version requested of (iii) is FALSE with the sign** (Prop. 4.3): a witness does not require coherence ≥ A(T) at its
 peak frequency; it requires averaged coherence **less** than −𝔟₀(F)/(4T) (Cor. 4.2), and the growing coherence that produces it lives at a
 frequency where F̂ has a **node** (M₁: γ₁ ∉ peak of h*, |ĥ*(γ₁)|² = 3·10⁻¹⁴). The correct, PROVED version (Theorem 4.4,
 class ζ + quartet): witness ⟹ 4T(g(δT) − 1) > λ_A(T), with γ-independent exclusion of every quartet with δ < δ*(T)
 (δ* = 0.093 at ½log3; 9·10⁻⁴ at log 2). **Inherits λ_A(ζ): no contact with the sign of ζ.**
 "bounded 𝒞 ⟹ D" is FALSE for every bounded coherence functional (Prop. 4.5, counterexample by rescaling the comb: v_n →
 (1 + 10⁻⁵)v_n changes λ_A(log 2) from +1.0·10⁻⁷ to −7.8·10⁻⁷ moving 𝒞₀ by ≤ 8·10⁻⁶).
6. **(c) (E_γ) and D (§5).** D ⇒ (E_γ) (R186_050 Prop. 4.5, PROVED). (E_γ) ⇏ D within the declared class: by freezing
 (R186_050 Lemma 4.1) a witness F₀ of T₀ is not in the family F_T^γ and (E_γ) does not see it; the converse implication only exists
 on the zero side. **The exact arithmetic form of D is not (E_γ) but Paper 46 thm:A** (Target-theorem 5.2, with
 constants): ∀T, ∀Φ ∈ 𝒦_prim: Σ_{n<e^{2T}} v_nΦ(log n) ≤ C₀ + ∫₀^∞(1 − Φ(u))K(u)du, C₀ = ψ(¼) − log π = −5.3721834.
 (E_γ) is its trace on a one-dimensional family indexed by γ; 𝒞̃(T) = 0 ∀T is a uniform (E) and is strictly weaker than D.
7. **Numerics (§6).** 𝒞̃^ζ(T) = 0 at T = ½log3, log 2, ½log5, ½log7, 1.5, 2, 3, 4, 5 (min_γ 𝔞_T(F_T^γ)/‖F_T‖² = 0.98, 0.47, 0.36,
 0.16, 1.1·10⁻², 2.5·10⁻³, 3.5·10⁻⁴, 8.2·10⁻⁵, 9.5·10⁻⁴ > 0); 𝒞̃^{M₁}(T) = 0 for T ≤ 4 and 1.26 at T = 5 (δ = 0.1): **the adapted
 family sees the quartet only from T ≈ 4.5 (δ = 0.1), while the minimizer h* sees it from T = 0.573** (R186_050 Thm 4.6).
 𝔖_T^ζ(γ₁) → m(γ₁) = 0.8106: 0.847, 0.848, 0.793 at T = 2, 3, 5 (convergence of (E_{γ₁}) with slack 𝔞_T(F_T)/‖F‖² = 0.04–0.004).
8. **Contact with the sign: none for ζ.** Theorem 4.4 bounds λ_A^{M₁} ≥ λ_A(ζ) − 4T(g(δT) − 1): it inherits. Row D: OPEN.

---

## 1. Definitions and normalizations

Paper 46 conventions: v_n = 2Λ(n)/√n, 𝒩_T = {n < e^{2T}}, c_F(u) = ∫F(t)F(t − u)dt, 𝔞_T(F) = C₀‖F‖² + Lev(c_F) − Σ_{n∈𝒩_T}v_n c_F(log n),
K(u) = 2e^{−u/2}/(1 − e^{−2u}) (lem:K), 𝒫_T = {∫F e^{±t/2} = 0}. Identity of R186_035 Lemma 1 (CITED): 𝔞_T = 𝔟₀ + E_ψ with
𝔟₀(F) = (C₀ + 4)c_F(0) + Lev_{K₁}(c_F), K₁ = K − 2e^{−u/2} ≥ 0, E_ψ(F) = 2∫₀^{2T}c_F e^{u/2}du − Σv_n c_F(log n).

**Def. 1.1 (fluctuation measure).** η_T := Σ_{n∈𝒩_T}v_n δ_{log n} − 2e^{u/2}du on [0, 2T]; η̂_T(ω) := ∫e^{iωu}dη_T = S_T(ω) − M_T(ω),
S_T(ω) = Σv_n n^{iω}, M_T(ω) = 2(e^{(½+iω)2T} − 1)/(½ + iω). Then E_ψ(F) = −∫₀^{2T}c_F dη_T = −(1/2π)∫|F̂|² Re η̂_T.
By Perron/Stieltjes (PROVED, elementary): η̂_T(ω) = 2∫₁^{e^{2T}}y^{−½+iω}d(ψ(y) − y).

**Def. 1.2 (zero-order coherence).** 𝒞₀(σ; T, ω) := −Re η̂_T(ω)/(4T) = [Re M_T(ω) − P_T(ω)]/(4T), P_T = Σv_n cos(ω log n)
(comb part of σ_T). It is a function of (Λ|𝒩_T) alone; m does not enter.
*Lemma 1.3 (normalization; PROVED).* A "coherent term of amplitude a and rate δ at γ" is the density a·cos(γu)cosh(δu)du on
[0, 2T] added to −η_T. Its 𝒞₀ at ω = γ equals (a/4)·g(δT) + ε, g(x) := sinh(2x)/(2x), |ε| ≤ a·cosh(2δT)/(8γT). *Proof.*
∫₀^{2T}cos(γu)cosh(δu)e^{iγu}du = ½∫₀^{2T}cosh(δu)du + ½∫₀^{2T}cosh(δu)e^{2iγu}du; the first is sinh(2δT)/(2δ) = T·g(δT); the
second, by parts, has modulus ≤ cosh(2δT)/(2γ) (summing the boundary terms and ∫δ sinh ≤ cosh − 1). ∎
So a pair of simple zeros on the line (a = 4, δ = 0) is worth 1, a quartet (a = 8) is worth 2g(δT) → e^{2δT}/(2δT), and the PNT
density 2e^{u/2} (a = 4 at γ = 0, δ = ½) would be worth e^{T}/T: the normalization by 4T is what makes the coherence of a zero O(1).

**Def. 1.4 (anticoherence).** For a finite measure μ on [0, 2T], 𝒜(μ; T) := −min spec(Q_μ|𝒫_T), Q_μ(F) := ∫₀^{2T}c_F dμ.
*Lemma 1.5 (PROVED, Kreĭn CITED).* 𝒜(μ; T) = 0 ⟺ the even extension of μ is positive definite on (−2T, 2T) modulo the two Tate
functionals ⟺ (Kreĭn 1940, without the functionals) μ is the restriction of ∫cos(τu)dρ(τ) with ρ ≥ 0: **superposition of cosines of
constant amplitude**. A coherent term with δ > 0 has 𝒜 > 0 (Lemma Q: Q = 4|Φ_c|² − 4|Φ_s|², rank (2,2)); with δ = 0, 𝒜 = 0.
This is the exact meaning of "the measure contains no coherent term of growing amplitude".

**Def. 1.6 ((E_γ), from R186_050 §4.3).** F_T^γ := (¼ − ∂_t²)[t sin(γt)η_T(t)] ∈ 𝒫_T (η_T ∈ C⁴_c(I_T), = 1 on I_{T−w}, w = min(1, T/2);
here η = 1 − S₉(x), S₉ a degree-9 smoothstep). 𝔖_T(γ) := Σv_n c_{F_T}(log n)/‖F_T‖²; 𝔪_T(γ) := [C₀‖F_T‖² + Lev(c_{F_T})]/‖F_T‖²;
𝔞_T(F_T^γ)/‖F_T^γ‖² = 𝔪_T(γ) − 𝔖_T(γ); 𝔪_T(γ) → m(γ). (E_γ): limsup_T 𝔖_T(γ) ≤ m(γ).
𝒞(T) := sup_γ[𝔖_T(γ) − m(γ)]₊ (the one originally requested) and 𝒞̃(T) := sup_γ[𝔖_T(γ) − 𝔪_T(γ)]₊ = sup_γ[−𝔞_T(F_T^γ)]₊/‖F_T^γ‖² (the
resolution-error-free version: 𝔪_T(γ) − m(γ) = O(1/(γT)) + O(m″/T²) and for γ ≤ 3, T ≤ 1 it is as large as 1.5; that is why 𝒞(T) ≠ 0 for ζ in §6 with no content).
*Lemma 1.7 (PROVED).* The polar term of 𝔖_T is bounded: 2∫₀^{2T}c_F e^{u/2}/‖F‖² = −2∫₀^{2T}c_F e^{−u/2}/‖F‖² ∈ [−4, 4]
(by ∫c_F cosh(u/2) = 0 and |c_F| ≤ ‖F‖²). Measured: −0.002…−0.005 (§6). Hence 𝔖_T(γ) = O(1) + ℱ_T(γ),
ℱ_T(γ) := 2∫₁^{e^{2T}}y^{−½}w_T(log y)d(ψ(y) − y), w_T := c_{F_T}/‖F_T‖², |w_T| ≤ 1, w_T(2T) = 0.

## 2. (i): M₁ has growing coherence; why that does not separate in the first-contact windows

**Theorem 2.1 (PROVED).** η_T^{M₁} = η_T^ζ − 8cos(γ₁u)cosh(δu)du (R186_114 §1.1: the quartet adds ∫_{−2T}^{2T}c_F·4cos cosh to 𝔞_T).
Hence 𝒞₀^{M₁}(T, γ₁) = 𝒞₀^ζ(T, γ₁) + 2g(δT) + ε, |ε| ≤ cosh(2δT)/(γ₁T) (Lemma 1.3 with a = 8), and 𝒞₀^{M₁}(T, γ₁) ≥ 𝒞₀^ζ(T, γ₁) +
e^{2δT}/(2δT) − 1/(2δT) − cosh(2δT)/(γ₁T) → ∞. Outside |ω − γ₁| ≲ π/T, 𝒞₀^{M₁} − 𝒞₀^ζ = O(cosh(2δT)/(T|ω − γ₁|)).
Measured (§6): difference at γ₁ = 1.98, 2.06, 2.05, 1.98 (bound on ε: 0.13–0.09) in the four windows; 2g(δT) = 2.0004–2.0126.

**Prop. 2.2 (PROVED; the 2 does not carry the sign).** Let M₁(0) := ξ·(s − ½ − iγ₁)²(s − ½ + iγ₁)² (triple zero on the line; R186_114 §1.3).
Then (a) 𝒞₀^{M₁(δ)} − 𝒞₀^{M₁(0)} = O((2δT)²/3) uniformly in ω (Lemma 1.3 with cosh − 1 ≤ 2δ²u²); (b) λ_A^{M₁(0)}(T) ≥ λ_A(T) ≥ 0
(adds 4|F̂(γ₁)|² ≥ 0), while λ_A^{M₁(δ)}(log 2) < 0 for δ ≥ 2.5·10⁻³ (R186_044 Lemma P, NUMERICAL). Hence any functional
𝒢 of σ Lipschitz with respect to ‖𝒞₀‖_∞ that separates witness from non-witness at log 2 has margin ≤ L·(2δT)²/3 ≤ 1.3·10⁻²·L (δ = 0.1),
2.5·10⁻⁵·L (δ = 2.5·10⁻³). ∎ This is the unifying fact of rounds 14–23 (every first-order quantity that distinguishes belongs to
h*, not to σ) in quantitative form for coherence functionals: **the O(1) separation of 𝒞₀ is the multiplicity, the separation
carrying the sign is δ²T²**, and for T ≤ ½log7 it is ≤ 1.3·10⁻².

**Lemma 2.3 (adapted family; PROVED from Lemma Q).** For F = F_T^γ (even), Φ_s = i(γ² + ¼)∫t sinh(δt)sin²(γt)η_T + O(γe^{δT}/δ)
and Φ_c = 2δγ∫t sinh(δt)sin²(γt)η_T + O(γ²e^{δT}/δ) (the part of (¼ − ∂²) on cosh(δt)cos(γt): the term (¼ − δ² + γ²)cosh cos is
oscillatory). With ∫_{−T}^{T}t sinh(δt)η dt = (2T/δ)e^{δT}(1 − 1/δT)(1 + O(e^{−2δ})) and ‖F‖² = (γ² + ¼)²(T³/3)(1 + O(1/T)):
 −Q_δ(F_T)/‖F_T‖² = (4|Φ_s|² − 4|Φ_c|²)/‖F‖² = (3e^{2δT}/(δ²T))(1 − 1/δT)²(1 − δ²/γ² + o(1)).
It corrects the constant of R186_050 (4.1) (which omits (1 − 1/δT)² and the term −4|Φ_c|²; at δT = 3 the factor is 0.44). Measured vs
formula: 1.30/1.63·0.44 = 0.72 (T = 5; η also trims), 205/819·0.72 = 0.59 (T = 20), 1645/4034·0.79 (T = 30): order and exponent
correct, constant within a factor of 1.5 (tail of η). **(i) for 𝔖: PROVED**, grows as e^{2δT}.

## 3. (ii): what the known bounds on Λ give for 𝒞₀ and for 𝔖_T

**Theorem 3.1 (mean square; PROVED mod. CITED).** For Y ≥ e^{2T}:
 (1/Y)∫₀^Y 𝒞₀^ζ(T, ω)²dω = Σv_n²/(32T²)·(1 + θ·3πe^{2T}/Y) + O(e^{2T}/(TY)) + O(1/T²), |θ| ≤ 1,
and Σ_{n<x}v_n² = 4Σ_{n<x}Λ(n)²/n = 2log²x + O(log x) = 8T² + O(T). Hence RMS_{[0,Y]}𝒞₀^ζ = ½ + O(1/T) + O(e^{T}/√Y).
*Proof.* Montgomery–Vaughan (1974, Cor. 3; CITED): ∫₀^Y|Σa_n n^{iω}|²dω = Σ|a_n|²(Y + θ·3πn). For Re: |Re S|² = ½|S|² + ½Re S²,
and ∫₀^Y Re S² = Σ_{n,m}v_nv_m∫cos(ω log nm) = O(Σv_nv_m/log(nm)) = O(e^{2T}/T). The term M_T: ∫₀^Y|M_T|² ≤ 4e^{2T}·π.
Σ_{n≤x}Λ(n)²/n = ½log²x + O(log x) (elementary: Σ_{p≤x}log p/p = log x + O(1), by parts). ∎
Measured (§6): RMS over [0, 400] = 0.319, 0.406, 0.382, 0.410 vs √(Σv_n²/2)/(4T) = 0.315, 0.409, 0.384, 0.411 (diagonal only).
**Reading.** This is the rigorous form of "the phases γ log p are equidistributed": on average over ω ≫ e^{2T} the coherence of ζ is ½.
**But M₁ satisfies the same thing**: its extra term has support of width π/T and height 2g, with contribution O(T·g²/Y) to the mean. The
mean square does not localize at any fixed frequency: it sees no quartet, no zero, nothing of width π/T.
For 𝔖_T: with w_T ≈ cos(γu)(1 − u/2T)³ (ARGUED, plus the correction r_T that cancels the pole, Lemma 1.7), the same bound gives
RMS_{[0,Y]}ℱ_T ≤ √(Σv_n²(1 − log n/2T)⁶)/2·(1 + o(1)) = T/√14·(1 + o(1)) = O(T): against m(γ) ~ log γ, whose RMS over [0, Y] is
≥ log Y ≥ 2T: consistent and empty (the average mixes γ ~ e^{2T} with fixed γ).

**Theorem 3.2 (pointwise; CITED).** With ψ(y) = y + E(y), |E(y)| ≤ C·y·exp(−c L(y)), L(y) = (log y)^{3/5}(log log y)^{−1/5}, c = 0.2098
(Ford 2002, Vinogradov–Korobov zero-free region with the constant; C not given explicitly in the literature read), by parts in
η̂_T(ω) = 2[y^{−½+iω}E]₁^x − 2(−½ + iω)∫₁^x E(y)y^{−3/2+iω}dy:
 |𝒞₀^ζ(T, ω)| ≤ [2 + 2C|½ + iω|·(2 + o(1))e^{T}e^{−cL(e^{2T})}]/(4T) = O((1 + |ω|)e^{T − 0.2098(2T)^{3/5}(log 2T)^{−1/5}}/T).
For 𝔖_T (Lemma 1.7, R186_035 Lemma 3.1: ℱ_T = −2∫₀^{2T}R₁(u)φ′(u)du, φ = w_T e^{−u/2}, |φ′| ≤ (γ + 1)e^{−u/2}):
 |ℱ_T(γ)| ≤ 2(γ + 1)C∫₀^{2T}e^{u/2}e^{−cL(u)}du ≤ 8(γ + 1)C·e^{T}e^{−cL(2T)}(1 + o(1)).
Van der Corput/Vinogradov bound Σ_{n≤N}n^{iγ} (integers), and the zero-free region comes from that; over primes weighted by Λ(n)n^{−½}
they give nothing better than (3.2) (Vaughan + vdC: Σ_{p≤X}p^{−½−iγ}log p ≪ X^{½}e^{−c′L(X)} is the same thing).

**Prop. 3.3 (the exact missing improvement; PROVED as arithmetic of exponents).** (E_γ) uniform in T requires |ℱ_T(γ)| ≤ m(γ) + o(1)
= O(log γ) for every T, that is (by Lemma 1.7 and parts):
 |∫₀^{2T}R₁(u)e^{−u/2}·γ sin(γu)(1 − u/2T)³du| = O(log γ) ∀T, R₁(u) = e^u − 1 − ψ(e^u).
The known bound is γ·e^{T}e^{−cL(2T)}. The ratio between what is known and what is needed is e^{T(1 − o(1))}: **the needed improvement is
to move the exponent of E(y) from 1 − o(1) to ½ (in twisted, Riesz-3 form)**, not a polynomial factor. No intermediate form
suffices: by the explicit identity (CITED, lem:roughEF), ∫₀^{2T}R₁(u)e^{−u/2}sin(γu)(1 − u/2T)³du = Σ_ρ ∫₀^{2T}e^{(ρ−½)u}·(…)du + O(1),
and a quartet {½ ± δ_q ± iγ_q} contributes ≍ e^{2δ_qT}/(T(δ_q² + (γ_q − γ)²)²): not bounded in T **at any height γ_q**, only
polynomially suppressed in |γ_q − γ|. So "(E_γ) for a γ" ⟺ "no quartet at any height" (R186_050 §4.3(iii)):
the needed improvement is exactly the full zero side, not a partial zero-free region (which only gives δ_q ≤ c·T^{−2/5}
in the window and hence e^{2δ_qT} ≤ e^{cT^{3/5}}, which is (3.2)). **OPEN as a statement about (m, Λ); S2 of Ω.**
The same holds for pointwise 𝒞₀: 𝒞₀^ζ(T, ω) = O(log(2 + |ω|)) ∀T is OPEN for the identical reason.

## 4. (iii): sampling identity, the correct version of the necessary condition, and what is missing

**Theorem 4.1 (Nyquist sampling of the form; PROVED).** Let F ∈ L²(I_T) with |F̂|² ∈ L¹ and F̂ of class C¹ (e.g. F of Legendre or
F_T^γ); ω_k := kπ/2T. Then
 (a) Σ_{n∈𝒩_T}v_n c_F(log n) = (1/4T)Σ_{k∈ℤ}|F̂(ω_k)|²P_T(ω_k); (b) ‖F‖² = (1/4T)Σ_k|F̂(ω_k)|²;
 (c) E_ψ(F) = Σ_{k∈ℤ}|F̂(ω_k)|²·𝒞₀(T, ω_k);
 (d) 𝔞_T(F) = (1/4T)Σ_k|F̂(ω_k)|²·s_T(ω_k), s_T(τ) := C₀ + ∫_{2T}^∞K + ∫₀^{2T}(1 − cos τu)K(u)du − P_T(τ) (= σ_T(τ) + ∫_{2T}^∞cos(τu)K(u)du).
*Proof.* Let μ be a finite even measure supported in [−2T, 2T] with no atoms at ±2T and f := |F̂|², whose transform is c_F, supported
in [−2T, 2T] with c_F(±2T) = 0. The function f·μ̂ has transform (2π)⁻¹c_F * μ, supported in [−4T, 4T], and (c_F * μ)(±4T) =
∫c_F(±4T − u)dμ(u) = 0 (4T − u ≥ 2T and c_F(2T) = 0). Poisson with step π/2T: Σ_k(fμ̂)(ω_k) = (2T/π)Σ_j (c_F * μ)(4Tj)·(2π)⁻¹·2π = (2T/π)(c_F * μ)(0)
= (2T/π)·2π∫c_F dμ (the j ≠ 0 terms vanish). With μ = Σv_n½(δ_{log n} + δ_{−log n}) one gets (a); μ = δ₀ gives (b); μ = the symmetrized
measure of η_T gives (c); (d) is (a)+(b)+ the same identity for the truncated Lévy measure ½K(|u|)1_{|u|<2T}du (which has finite mass
against c_F(0) − c_F(u) ~ u²). Regularity: f ∈ L¹ with f′ ∈ L¹ suffices for Poisson in the sense of Σ_k f(ω_k) absolutely convergent. ∎
Verified (§6): 12 tests (h* and random vectors in 𝒫_T, four windows), K = 2·10⁵, error ≤ 10⁻⁸; (d) reproduces λ_A to 3–4 digits.
*Reading.* The form never sees σ_T on a continuum: it sees s_T **on the Nyquist grid** weighted by the samples of |F̂|²; the
constraint F ∈ L²(I_T) is that (|F̂(ω_k)|²)_k be the samples of a ≥ 0 function of Paley–Wiener type 2T (Shannon), and
F ∈ 𝒫_T that F̂(±i/2) = 0. It is the exact version of "energy of σ in windows of width π/T". New in the corpus as a tool
(grep: "Shannon" appears only as the Shannon number). s_T < 0 on the grid at 3, 6, 7, 15 points (k ≤ 400) in the four windows; h* splits
its mass as −0.306/+0.307 (½log3), −0.218/+0.218 (log 2), −0.265/+0.265 (½log5): the cancellation of R186_040 on the grid.

**Cor. 4.2 (correct necessary condition; PROVED).** If F ∈ 𝒫_T, ‖F‖ = 1, 𝔞_T(F) < 0, then
 Σ_k|F̂(ω_k)|²𝒞₀(T, ω_k) < −𝔟₀(F), i.e. 𝒞̄_F := (1/4T)Σ_k|F̂(ω_k)|²𝒞₀(T, ω_k) < −𝔟₀(F)/(4T),
and in particular min_k 𝒞₀(T, ω_k) < −𝔟₀(F)/(4T) ≤ −λ_min(𝔟₀|𝒫_T)/(4T) = −0.051 (½log3), +0.039 (log 2), +0.076 (½log5), +0.149 (½log7)
(λ_min(𝔟₀|𝒫_T) = +0.112, −0.108, −0.245, −0.413; reproduces R186_035). *Proof.* 𝔞_T = 𝔟₀ + E_ψ and Theorem 4.1(c),(b). ∎
**The direction is the opposite one**: a witness needs **low or negative** coherence on average over its samples.
The positive coherent term (bump 2g at γ₁) is positive definite and *helps* positivity; what subtracts is its indefinite part
(cosh − 1), which in 𝒞₀ is the alternating leakage ∝ δ sinh(2δT)/(δ² + (ω_k − γ₁)²) to the neighboring grid points, and which is only
charged against samples with a node at γ₁ (Lemma P: −4δ²|F̂′(γ₁)|²).

**Prop. 4.3 (the version "amplitude ≥ A(T) at the peak frequency" is FALSE; PROVED by M₁).** At log 2, δ = 0.01, M₁ has a
witness (λ_A^{M₁} = −1.66·10⁻⁶) with h*^{M₁} = h*^ζ + O(10⁻³) (R186_044), spectral peak at τ ≈ 7–8 (R186_040), |ĥ*(γ₁)|² = 3·10⁻¹⁴
(node at γ₁). 𝒞₀^{M₁} ≡ 𝒞₀^ζ outside |ω − γ₁| ≲ π/T (Theorem 2.1): at the witness's peak frequency there is **no** additional
coherence. The growing coherence lives at the node. ∎ As a necessary condition on sup/inf/peak of 𝒞₀, what remains (Cor. 4.2)
is satisfied by ζ in every window (inf 𝒞₀^ζ = −0.58, −0.82, −0.92, −0.89 on [0, 60]): **no bite**. NO-GO for weak-(iii)
in this form; Cor. 4.2 survives as an identity.

**Theorem 4.4 (class ζ + quartet: witness ⟹ growth; PROVED).** For β = 8cos(γu)cosh(δu)du on [0, 2T], Q_β|𝒫_T ≥ −4(sinh(2δT)/(2δ) − T)
= −4T(g(δT) − 1) (Lemma Q: Q ≥ −4|Φ_s|², |Φ_s|² ≤ ‖sinh(δt)‖²_{L²(I_T)}; = R186_050 Lemma 3.1). By Weyl, λ_A^{ζ+β}(T) ≥ λ_A(T) − 4T(g(δT) − 1).
Hence: **witness of ζ + β ⟹ g(δT) > 1 + λ_A(T)/(4T) ⟹ 2(g − 1) = excess coherence of β over its constant-amplitude part > λ_A/(2T)**,
for every γ. γ-independent threshold: δ*(T) := the δ with 4T(g(δT) − 1) = λ_A(T): 0.093 (½log3), 8.9·10⁻⁴ (log 2), 2.6·10⁻⁶ (½log5).
Check: ½log3, δ = 0.01: bound −4.4·10⁻⁵ > −λ_A = −9.5·10⁻⁴ ⟹ no witness; measured λ_A^{M₁} = +9.47·10⁻⁴ ✓. δ = 0.1: bound
allows it (−4.4·10⁻³), measured +5.8·10⁻⁴ (necessary, not sufficient) ✓. log 2, δ = 0.01: −8.9·10⁻⁵ < −1.0·10⁻⁷: allows it; measured −1.66·10⁻⁶ ✓.
The exact bound of the indefinite part is 𝒜(β; T) = −λ_min(Q_β|𝒫_T) = 2.2·10⁻⁵, 4.7·10⁻⁵, 7.5·10⁻⁵, 1.2·10⁻⁴ (δ = 0.01), ∝ δ² (NUMERICAL),
= 4δ²κ_T(γ₁) + O(δ⁴) with κ_T = sup{|∫F t e^{iγt}|²: F ∈ 𝒫_T, ‖F‖ = 1, Φ_c(F) = 0} ≤ T²/3. **Inherits λ_A(ζ)**: nothing bounds λ_A(ζ) from below.

**Prop. 4.5 ("bounded 𝒞 ⟹ D" is FALSE for every bounded functional of σ; PROVED, NUMERICAL constant).** In the weight class of def:PD,
v_n ↦ (1 + ε)v_n changes the form by −εΣv_n c_F(log n) and λ_A by −ε·Σv_n c_{h*}(log n) + O(ε²) = −0.088ε (log 2): λ_A = +1.04·10⁻⁷ → +1.6·10⁻⁸
(ε = 10⁻⁶) → −7.8·10⁻⁷ (ε = 10⁻⁵) → −2.6·10⁻⁴ (ε = 10⁻³), while ‖𝒞₀^{(ε)} − 𝒞₀‖_∞ ≤ εΣv_n/(4T) = 8·10⁻⁶ (ε = 10⁻⁵) and 𝒞₀, 𝔖_T, 𝒞, 𝒞̃
remain bounded by the same constants. Hence no statement "𝒢(σ) ≤ C ∀T" with 𝒢 continuous in the weights implies λ_A ≥ 0.
(This is Lemma T′ of R186_045 for functionals of σ instead of functionals of 𝔞_T.)

**What exactly is missing for (iii).** By Theorem 4.1, D at T is: Σ_k a_k s_T(ω_k) ≥ 0 for every admissible sample vector
a = (|F̂(ω_k)|²)_k, F ∈ 𝒫_T. The necessary condition Cor. 4.2 gives a bound on the average **weighted by a_k** of 𝒞₀ on the grid. To
turn it into an exclusion one would need: (F1) a lower bound for Σ_k a_k𝒞₀(T, ω_k) over the cone of admissible samples — which is the
extremal problem itself (λ_min of the bundle, circular); or (F2) a pointwise **signed** bound 𝒞₀(T, ω_k) ≥ −c_k at the ~N_Sh = 2Tτ_last/π
≈ 10–60 relevant grid points, with Σ_k a_k c_k < 𝔟₀(F) — false for ζ as a uniform bound (inf 𝒞₀ ≈ −0.9 vs 𝔟₀ ≥ −0.4) and
hence only possible by correlating the sign of 𝒞₀ on the grid with the position of the samples of F ∈ 𝒫_T, which is (F1).
**The large sieve gives neither (F1) nor (F2)**: Montgomery–Vaughan controls Σ_k 𝒞₀(ω_k)² over ranges ≫ e^{2T} (Theorem 3.1), with no sign,
no localization, and the global structure of the log n it uses (separation log(n/m) ≥ 1/n) only enters through the error term 3πn/Y.
The missing input is **pointwise, signed, on the Nyquist grid, at fixed frequencies** — S2 of Ω in its most concrete form.

## 5. (c): (E_γ) and D

**Prop. 5.1 (PROVED).** (a) D ⇒ (E_γ) ∀γ (R186_050 Prop. 4.5; 𝔞_T(F_T^γ) ≥ 0 and 𝔪_T → m). (b) D ⇒ 𝒞̃(T) = 0 ∀T (trivial). (c) (E_γ) ⇏ D
and {𝒞̃(T) = 0 ∀T} ⇏ D within the declared class: if F₀ ∈ 𝒫_{T₀} were a witness, by freezing (R186_050 Lemma 4.1) ιF₀ is a witness
at every T with the same value, and neither (E_γ) nor 𝒞̃ evaluate 𝔞_T at ιF₀ (the family F_T^γ is one-dimensional in γ, with a simple node at ±γ
and maximal slope; h* has nodes at every zero ≤ T*, R186_040). An implication (E_γ) ⇒ D would require either that every witness
lie in the cone generated by {F_T^γ}_γ (false: the dimension of the cone ≠ 𝒫_T, and 𝔞_T is not monotone on that cone), or the zero side
(Prop. 3.3), outside the class. ∎ **Only D ⇒ (E_γ).** (E_γ) is the trace of D on the spectral-derivative family; 𝒞̃(T) = 0 ∀T
is a uniform (E) in γ and T, strictly weaker than D.

**Target-theorem 5.2 (exact arithmetic form of D; = Paper 46 thm:A, CITED, with constants).** D ⟺ for every T > 0 and every
Φ ∈ 𝒦_prim (Φ = c_F continuous, positive definite, Φ(0) = 1, supp ⊂ [−2T, 2T], ∫Φ cosh(u/2) = 0, ∫Φ u sinh(u/2) = 0):
 Σ_{n<e^{2T}} (2Λ(n)/√n)·Φ(log n) ≤ C₀ + ∫₀^∞(1 − Φ(u))K(u)du, C₀ = ψ(¼) − log π = −5.3721834, K(u) = 2e^{−u/2}/(1 − e^{−2u}),
equivalently (Theorem 4.1) Σ_{k∈ℤ}Φ̂(kπ/2T)·s_T(kπ/2T) ≥ 0 with Φ̂ ≥ 0 the samples of the spectral measure. (E_γ) is the case
Φ = c_{F_T^γ}/‖F_T^γ‖² with T → ∞. **It is the statement to be proved; there is no weaker form within the class that would imply it.**

## 6. Numerics (NUMERICAL; `r051_coherence.py`, Legendre M = 40, t-grid of 3200T points for F_T)

(A) 𝒞₀ (closed forms; quadrature vs closed-form check 0.3620635238 = 0.3620635238):

| T | object | 𝒞₀(γ₁) | sup_{[0,60]} (ω) | inf_{[0,60]} (ω) | RMS_{[0,400]} | g(δT) |
|---|---|---|---|---|---|---|
| ½log3 | ζ / M₁(.01) / M₁(.1) | 0.429 / 2.407 / 2.411 | 0.887 (0) / 2.421 (13.97) / 2.425 | −0.577 (9.45) / −0.904 / −0.905 (9.74) | 0.319 / 0.377 / 0.377 | 1.00002 / 1.0020 |
| log 2 | ζ / M₁(.01) / M₁(.1) | 0.850 / 2.900 / 2.907 | 0.855 (14.25) / 2.903 / 2.910 (14.18) | −0.825 (17.3) / −1.275 / −1.280 | 0.406 / 0.456 / 0.456 | 1.00003 / 1.0032 |
| ½log5 | ζ / M₁(.01) / M₁(.1) | 0.442 / 2.486 / 2.495 | 0.656 (48.4) / 2.488 / 2.497 (14.19) | −0.917 (45.6) / −1.054 / −1.058 | 0.382 / 0.418 / 0.418 | 1.00004 / 1.0043 |
| ½log7 | ζ / M₁(.01) / M₁(.1) | 0.756 / 2.720 / 2.732 | 0.885 (48.7) / 2.740 / 2.752 (14.03) | −0.893 (27.6) / −0.975 / −0.982 | 0.410 / 0.443 / 0.443 | 1.00006 / 1.0063 |

Separation by growth 2(g − 1): 4·10⁻⁵…1.3·10⁻⁴ (δ = 0.01), 4·10⁻³…1.3·10⁻² (δ = 0.1). At fixed δ: 2g = 2.01, 2.35, 3.63, 13.6, 373
at T = 1, 5, 10, 20, 40 (δ = 0.1). Σv_n² = 0.961, 2.570, 3.051, 5.123 (8T² = 2.41, 3.84, 5.18, 7.57: the O(T) term dominates for T < 1).

(B)(C) λ_A = 9.486·10⁻⁴, 1.042·10⁻⁷, 3.84·10⁻¹², −5·10⁻¹⁴ (floor); λ_min(𝔟₀|𝒫_T) = +0.112, −0.108, −0.245, −0.413 (n₋ = 0, 1, 1, 2).
Q_η (Toeplitz of η_T) in L²(I_T): spectrum [−1.00, +0.51], [−1.07, +0.91], [−1.14, +1.15], [−1.43, +1.49], n₋ ≈ 20 of 40: **neither η_T nor
−η_T is positive definite in the window** (η_T contains, besides the zero terms, the density of trivial zeros −K₁ and the
boundary; the p.d. one is 𝔟₀ − Q_η = 𝔞_T, not the fluctuation alone). Lemma P reproduced: log 2, δ = 0.01: −1.660·10⁻⁶ vs −1.633·10⁻⁶.
|ĥ*′(γ₁)|² := |∫h* t e^{iγ₁t}|² = 9.2·10⁻³, 4.3·10⁻³, 3.0·10⁻³, 1.3·10⁻³; δ_A = 0.160, 2.45·10⁻³, 1.80·10⁻⁵ (= R186_044).

(G) (E_γ) with F_T^γ (check at γ₁: ∫c cosh(u/2)/‖F‖² ≤ 4·10⁻¹⁶; pole 2∫c e^{u/2} = −2∫c e^{−u/2} = −0.0022…−0.0048 to all digits shown; Q by the two routes of Lemma Q identical to 4 digits; 𝔪_T vs m(γ₁) = 0.8106):

| T | 𝔖_T^ζ(γ₁) | 𝔪_T(γ₁) | 𝔞_T(F_T)/‖F‖² | −Q/‖F‖² δ=.01 /.1 | 𝒞(T) ζ (γ) | min_γ 𝔞_T(F_T^γ)/‖F‖² | 𝒞̃^{M₁}(T) δ=.1 |
|---|---|---|---|---|---|---|---|
| ½log3 | 0.247 | 1.361 | 1.114 | −2.0·10⁻³ / −1.5·10⁻³ | 1.33 (2.0) | 0.98 | 0 |
| log 2 | 0.096 | 1.235 | 1.139 | −7·10⁻⁴ / +2·10⁻⁴ | 0.65 (2.0) | 0.47 | 0 |
| ½log5 | 0.647 | 1.141 | 0.493 | 0 / +2.0·10⁻³ | 1.66 (2.0) | 0.36 | 0 |
| ½log7 | 0.796 | 1.062 | 0.266 | 0 / +4.0·10⁻³ | 1.18 (2.0) | 0.16 | 0 |
| 2 | 0.845 | 0.881 | 0.035 | +5·10⁻⁴ / +0.050 | 0.92 (2.5) | 2.5·10⁻³ | 0 |
| 3 | 0.848 | 0.852 | 0.004 | +2.2·10⁻³ / +0.221 | 1.01 (2.0) | 3.5·10⁻⁴ | 0 |
| 4 | — | — | — | — | 1.00 (2.0) | 8.2·10⁻⁵ | 0 (sup −𝔞^{M₁} at γ₁ ≈ 0; 𝒞(T) 1.02) |
| 5 | 0.793 | 0.833 | 0.041 | +0.012 / +1.296 | 0.82 (2.0) | 9.5·10⁻⁴ | **1.26** (γ₁) |

(ζ's 𝒞(T) is always attained at the edge γ = 2, where 𝔪_T − m = 1.5…0.8 is resolution error: no content; 𝒞̃^ζ(T) = 0 in
every case.) Lemma Q at large T (no comb): −Q/‖F‖² = 0.116, 0.411, 1.00, 3.49 (δ = 0.01) and 13.8, 61.6, 205, 1645 (δ = 0.1) at T = 10, 15, 20, 30.
Bug fix this round: `r043_wh.contacts` stops at n < 2000 (valid only for T < ½log2000 = 3.80); with that
truncation T = 4, 5 gave 𝔞_T(F_T) = −0.05, −6.6 (false witnesses); `contacts_full` (sieve) corrects them to +8·10⁻⁵, +9.5·10⁻⁴.
**Warning to anyone using r034/r043/r046–r049 at T ≥ 3.8.**

## 7. Self-checks

1. Lemma Q re-derived (§1.5, Theorem 4.4) and Lemma P reproduced to 1.6% (log 2, δ = 0.01); parity-sector jump at δ = 0.1
 (−1.47·10⁻³ actual vs −1.7·10⁻⁴ first order), same as R186_044 §4.2.
2. Closed form of ∫₀^{2T}8cos cosh e^{iωu} vs quadrature: 10 digits. Bound on ε of Lemma 1.3 verified (differences 1.98–2.06 vs 2g ± 0.13).
3. Sampling identity (Theorem 4.1): 12 tests, K = 2·10³/2·10⁴/2·10⁵, convergence to 10⁻⁸; (d) reproduces λ_A to 3–4 digits with
 asymptotic tail from k = 400; (b) gives ‖h‖² = 1.000000.
4. λ_min(𝔟₀|𝒫_T) reproduces R186_035 (−0.108, −0.245) with independent code (Q_η via Toeplitz of the measure).
5. F_T^γ ∈ 𝒫_T: analytically exact (∫g(¼ − ∂²)e^{±t/2} = 0); discrete defect ≤ 4·10⁻¹⁶ after fixing the trapezoid weight at u = 0
 (previously 6·10⁻⁴, and Q by two routes differed by 5·10⁻⁴); degree-9 smoothstep (C⁴). Form in x-space vs
 τ-space for F_T: agree to 10⁻⁵ at (½log3, γ₁), (5, 3), (5, γ₁), (4, 2.5).
6. Theorem 3.1: RMS measured vs √(Σv_n²/2)/(4T): 0.319/0.315, 0.406/0.409, 0.382/0.384, 0.410/0.411.
7. What was NOT checked: Ford's constant C (not in the literature read: CITED with c = 0.2098 and C without a value); the constant of Lemma 2.3 to
 better than a factor of 1.5 (tail of η_T); the term r_T of w_T (ARGUED, only its polar effect is controlled by Lemma 1.7).

## 8. Labels and results sheet

| statement | label |
|---|---|
| Lemma 1.3 (normalization), Theorem 2.1 ((i) for 𝒞₀), Lemma 2.3 ((i) for 𝔖, corrected constant), Prop. 2.2 (margin δ²T²) | PROVED |
| Lemma 1.5 (anticoherence = p.d. in window = superposition of constant-amplitude cosines) | PROVED mod. Kreĭn CITED |
| Lemma 1.7 (pole of 𝔖 bounded by 4) | PROVED |
| Theorem 3.1 (mean square of 𝒞₀ = ½) | PROVED mod. Montgomery–Vaughan CITED |
| Theorem 3.2 (pointwise e^{T − cT^{3/5}}), Prop. 3.3 (needed improvement = exponent ½; no intermediate form) | CITED / PROVED as arithmetic |
| 𝒞₀^ζ = O(log ω) ∀T; (E_γ) from (m, Λ) | OPEN (S2 of Ω) |
| Theorem 4.1 (Nyquist sampling of the form) — new tool | PROVED |
| Cor. 4.2 (witness ⟹ average coherence < −𝔟₀/4T) | PROVED; no bite (ζ satisfies it) |
| Prop. 4.3 (weak-(iii) with "amplitude at the peak") | FALSE (NO-GO) |
| Theorem 4.4 (quartet class: witness ⟹ g(δT) > 1 + λ_A/4T; threshold δ*(T)) | PROVED; inherits λ_A(ζ) |
| Prop. 4.5 ("bounded 𝒞 ⟹ D" for bounded functionals of σ) | FALSE (NO-GO), NUMERICAL constant |
| Prop. 5.1 (D ⇒ (E_γ); (E_γ) ⇏ D in the class), Target-theorem 5.2 | PROVED / CITED (thm:A) |
| 𝒞̃^ζ(T) = 0 up to T = 5; 𝒞̃^{M₁} > 0 from T ≈ 4.5 (δ = 0.1) | NUMERICAL |

**Contact with the sign: none for ζ.** The only thing with its own sign is Theorem 4.4, for the class ζ + quartet, and it inherits λ_A(ζ).
**What this round leaves:** (1) the form is a sum on the Nyquist grid (Theorem 4.1): D ⟺ Σ_k a_k s_T(ω_k) ≥ 0 over the
admissible samples; (2) the correct coherence is not "amplitude at the peak" but "indefinite part at the node", measured by 𝒜 (Lemma 1.5) and,
in the quartet class, by 4T(g − 1); (3) the entire distance between what is known about Λ and what is needed is the exponent ½ in twisted
form (Prop. 3.3), with no intermediate form. Row D: OPEN.
