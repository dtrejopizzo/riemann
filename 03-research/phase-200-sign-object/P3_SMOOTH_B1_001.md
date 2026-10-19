# P3_SMOOTH_B1_001: Lemma B.1 restricted to a smooth sector (phase 200, round 7)

Pure mathematics; a single numerical computation (Hermite masses of the Mori extremal from the coefficients
published in MORI15 §4). **Leak lemma: it does not involve Λ,
does not involve the comb, gives no sign. L′♯ OPEN. Row D OPEN.**

**Read.** META_200_BARRIER_001 §P3; B1_FLAT_001 (complete); C1_DUPLICATION_001 §1 (B.1.a, B.1.b, B.1.c); K3_GAMMA_001 §1–2,
§4; PI_MU_001 §1.4, §2.1; MORI15_EXTREMAL_001 §3–4 (shape of g*, f₁, ρ*, prolate coefficients); data p1_*.json.
**Index.** grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` for "smooth sector", "B.1-sector", "sawtooth", "ξ^s weight":
only B1_FLAT (which leaves (B.1-sector) OPEN) and PROOF_L_SHARP_E/F (sawtooth inside 𝒲, not in the leak) appear. This
route does not appear as tried. New reason compared with B1_FLAT: the class of tails is restricted, not the support.

**Conventions** (those of B1_FLAT §1). Universal normalization at level T′: representative h(t) = f(t/λ′), level-T′
gauge on [−1,1], leak band 1 (level T′) and √2 (level T), ring 𝔸 = (1/√2, 1). Tail of h: r := ĥ|_{(1,∞)},
‖r‖² = leak₁(h)/2. Stacking ratio
 τ(r) := ∫_1^{√2} |Σ_{m≥1} r(mX)|² dX / ‖r‖²_{L²(1,∞)}.

---

## 0. Starting identity (PROVED)

For h even, C², with h(0) = ĥ(0) = 0, Poisson gives Σ_{n∈ℤ}h(nu) = u^{−1}Σ_k ĥ(k/u), hence S_h(u) := Σ_{n≥1}h(nu) =
u^{−1}Σ_{k≥1}ĥ(k/u). With X = 1/u:
 ‖δ_{h}‖²_{L²(𝔸)} = ∫_𝔸 |S_h|² du = ∫_1^{√2} |Σ_{k≥1} r(kX)|² dX = τ(r)·‖r‖².
(Only values ĥ(Y) with Y ≥ X > 1 enter: the out-of-band tail. This is the identity of B1_FLAT §1 written in the
variable X.)

**Lemma 0 (B.1 from τ; PROVED).** If g ∈ core_{T′} and f′ ∈ 𝒜_{T′}(g) has tail r with τ(r) ≤ τ̄, then
 ℓ_T(g) ≤ (1 + (C₂τ̄/2)^{1/2})² · leak_{λ′}(f′).
*Proof.* B.1.b: ℓ_T ≤ (√leak_λ(f′) + √C₂‖δ‖)²; leak_λ ≤ leak_{λ′}; ‖δ‖² = τ̄‖r‖² = τ̄·leak_{λ′}(f′)/2. □
No orthogonality to the gauge is needed: a near-optimal representative with controlled tail suffices.

---

## 1. The two candidates for 𝒮 and why neither works as is

### 1.1 Support sector "|t| ≤ 1.4" (B1_FLAT proposal)

**Prop. 1.1 (PROVED).** If the representative h is supported on |t| ≤ 1.4 (< √2), then for u ∈ 𝔸 and n ≥ 2, nu ≥ 2/√2 > 1.4,
so S_h = h on 𝔸: **no stacking is possible**, because no dilate n ≥ 2 falls in the ring. With ‖h|_𝔸‖ ≤ ‖h‖ and
leak₁(h) ≥ (1 − χ₀)‖h‖² (χ₀ = largest prolate concentration for time [−1.4, 1.4], band [−1, 1], c = 2.8π; CITED
Slepian–Pollak) one gets θ₀ = (1 + (C₂/(1−χ₀))^{1/2})^{−2} > 0 independent of μ (tiny: 1 − χ₀ ≈ 5·10⁻⁷, Fuchs,
NUMERICAL).

This **explains** the 1.4 threshold: it is the condition 2u ≥ √2 > 1.4 for u ∈ 𝔸. But the sector is degenerate and
**does not contain the Mori extremal** (§4): the mass condition "≥ 1 − δ on |t| ≤ 1.4" fails by a factor of 2–4.
Moreover the mass version (not the support version) does not control the tail: the mass fraction δ outside
|t| ≤ 1.4 can stack (B1_FLAT) and the leak is O(e^{−c}) of the mass, so the mass condition is irrelevant for τ.
**Discarded.**
(The literal reading of META, "ĝ supported on |t| ≤ 1.4," is vacuous: g of compact support does not have ĝ of
compact support.)

### 1.2 Prolate sector span{ψ_{4j}, j ≤ J}

Contains f* (a₈²/‖f*‖² = 2.5·10⁻¹⁰). But (i) the truncated ψ_k have nonzero boundary values and are not C² at ±N′: the
sector meets core_{T′} only in its closure; (ii) the leak of a truncated prolate is **dominated by the boundary**:
integrating the integral equation by parts, the tail is jump-type (amplitude ∝ ψ_k(boundary), oscillation at
frequency N′ in Y). So the relevant object is not the prolate index but **the shape of the tail**. This leads to
the definition in §2.

---

## 2. Definition of 𝒮 and statement

**Edge mode.** For p ≥ 1 and φ ∈ ℝ: F_{p,φ}(Y) := sin(2πpY + φ)/(πY), Y > 1. It is the tail of a jump at t = ±p.

**Weighted norm.** For σ > 1: ‖E‖_σ² := ∫_1^∞ Y^{2σ−1}|E(Y)|² dY (≥ ‖E‖²).

**Definition (smooth sector 𝒮(σ, η)).** g ∈ core_{T′} is in 𝒮(σ, η) if for every ε > 0 there exists f′ ∈ 𝒜_{T′}(g) with
leak_{λ′}(f′) ≤ ℓ_{T′}(g) + ε whose tail (universal normalization) is written
 r = J·F_{p,φ} + E,  p ≥ 1, J ∈ ℝ,  ‖E‖_σ ≤ η‖r‖.
Cases: J = 0 is the **smooth-tail sector** (relative moment Y^{2σ−1} bounded by η²); η = 0 is the **single-edge sector**.

**Theorem P3 (PROVED).** For g ∈ 𝒮(σ, η):
 ℓ_{T′}(g) ≥ θ₀(σ,η)·ℓ_T(g),  θ₀(σ,η) := (1 + (C₂/2)^{1/2}·(2.122(1+η) + ζ(σ)η))^{−2},
independent of μ.

---

## 3. Proof

**Step 1 (smooth part; Minkowski).** For X ∈ (1,√2), X^{2σ−1} ≥ 1, hence
 ‖Σ_m E(m·)‖_{L²(1,√2)} ≤ ‖Σ_m E(m·)‖_{L²((1,∞),X^{2σ−1}dX)} ≤ Σ_m ‖E(m·)‖_{…} = Σ_m m^{−σ}‖E‖_σ = ζ(σ)‖E‖_σ,
since ∫|E(mX)|²X^{2σ−1}dX = m^{−2σ}∫|E(Y)|²Y^{2σ−1}dY. (Equivalent to Mellin Plancherel at Re s = σ with multiplier ζ(s).)

**Step 2 (edge lemma; sawtooth).** Let θ = 2πpX. With S(θ) := Σ sin(mθ)/m = (π − θ)/2 on (0, 2π) and
Σ cos(mθ)/m = −log|2 sin(θ/2)|:
 Σ_{m≥1} F_{p,φ}(mX) = (πX)^{−1}[cos φ·S(θ) − sin φ·log|2 sin(θ/2)|].
By Cauchy–Schwarz (cos² + sin² = 1):
- ∫_1^{√2} S²/(π²X²) dX ≤ (1/4)(1 − 1/√2) = 0.0732 (|S| ≤ π/2);
- ∫_1^{√2} log²|2 sin(πpX)| dX ≤ (0.4142 + 1/p)·π²/12 ≤ 1.163 for p ≥ 1 (the interval covers ≤ 0.4142p + 1 periods of
  length 1/p, and ∫_0^1 log²|2 sin πs| ds = π²/12 by Parseval); divided by π²: 0.1179.
Numerator ≤ 0.1911. Denominator: ‖F_{p,φ}‖² = π^{−2}∫_1^∞ sin²(2πpY+φ)Y^{−2}dY ≥ π^{−2}(½ − 1/(4πp)) ≥ 0.0426
(integration by parts: |∫_1^∞cos(aY+b)Y^{−2}dY| ≤ 2/a, a = 4πp). Hence
 **τ(F_{p,φ}) ≤ 4.49 uniformly in p ≥ 1 and φ** (PROVED); √4.49 ≤ 2.122.

**Step 3 (sum).** ‖J F‖ ≤ ‖r‖ + ‖E‖ ≤ (1+η)‖r‖. By steps 1–2,
 τ(r)^{1/2} ≤ 2.122(1+η) + ζ(σ)η.
**Step 4.** Lemma 0 with near-optimal f′ and ε → 0. □

**Constant.** With η = 0 (one edge): θ₀ = (1 + 1.5·C₂^{1/2})^{−2}; with C_β ≈ 1, C₂ ≈ 2.41, θ₀ ≈ 0.09. With J = 0
(smooth tail): θ₀ = (1 + ζ(σ)(C₂A/2)^{1/2})^{−2}, A := ‖r‖_σ²/‖r‖².

---

## 4. Why harmonic stacking does not enter 𝒮

**Cor. 4.1 (PROVED, contrapositive).** The falsifier g_K of B1_FLAT §2 satisfies ℓ_{T′}/ℓ_T ≤ C_b/log K. If g_K ∈ 𝒮(σ,η),
Theorem P3 gives ≥ θ₀(σ,η). So **g_K ∉ 𝒮(σ,η) for K ≥ exp(C_b/θ₀)**, for every pair (σ, η).

Mechanism (ARGUED, consistent with the above): the tail of g_K lives at Y ~ K³/n (bumps of width nK^{−3}), with
relative moment A ≳ K^{3(2σ−1)}; and it is not of a single edge: it is a sum of ~K modes at rationally linked
frequencies that the sum Σ_m r(mX) **aligns in phase** at X = 1/u₀. The edge mode, in contrast, produces the
sawtooth S(θ), which is bounded because Σ sin(mθ)/m is conditionally convergent: the phases of a single edge do
**not** align.

---

## 5. Consequence for the doubling chain (restricted to 𝒮)

**Cor. 5.1 (PROVED given P3).** Let μ_k = 2^kμ₀ and g ∈ core_{T_0}. If g ∈ 𝒮(σ,η) **at every level** T_0 ≤ T_k ≤ T_m
(stability hypothesis, OPEN: the near-optimal representative changes with the level), then
 ℓ_{T_m}(g) ≤ θ₀^{−m} ℓ_{T_0}(g) = (μ_m/μ₀)^{log₂(1/θ₀)} ℓ_{T_0}(g)  (polynomial loss; ≈ μ^{3.5} with θ₀ ≈ 0.09).

**Transport of L′♯ (CONDITIONAL).** If L′♯ holds at level μ′ = μ/2 in the form W ≥ κ(μ′)ℓ_{T′} and ι preserves 𝒲
(A.5), then for g ∈ core_{T′} ∩ 𝒮: W(g) ≥ κ(μ′)ℓ_{T′}(g) ≥ θ₀κ(μ′)ℓ_T(g). Iterating: κ_𝒮(2^mμ₀) ≥ θ₀^mκ(μ₀) **on
the base-level data** core_{T_0} ∩ 𝒮.

**This gives no sign.** P3 is an inequality between two leaks of the same g; it only transports upward an
already-existing leak bound. The sign of the base case is that of Mori (μ ≤ 15, CITED/NUMERICAL) and is not
extended: new core_T data that do not come from core_{T′} remain uncovered. **L′♯ OPEN.**

---

## 6. Is the Mori extremal in 𝒮?

### 6.1 Support sector |t| ≤ 1.4: NO (NUMERICAL)

Hermite approximation for the prolates of [−λ, λ] with c = 2πμ: ψ_k(u) ≈ (2π)^{1/4}h_k(√(2π)u), **scale independent
of μ** (K3 §1.4, CITED). With a₀ = 1.106365, a₄ = −1.821723: ‖f‖² = 4.5427 (datum: 4.54272) and f(0) ≈ −0.011
(control). Mass on |u| ≤ U:

| Mori usage | λ′ | |t| ≤ 1.4 ⇔ |u| ≤ | mass |
|---|---|---|---|
| 15 → 30 (Mori as level T′) | √15 | 0.3615 | **22.6 %** |
| 7.5 → 15 (Mori as level T) | √7.5 | 0.5112 | **49.9 %** |
| (raw variable u, not universal) | — | 1.4 | 99.3 % |

The "1.4" of B1_FLAT (universal variable t) and the "f* lives in u ≲ 1.5" of MORI15 (raw variable u) are numbers
in different variables. In the correct variable the extremal has mass 1 − δ with δ ≈ 0.5–0.8, and since its scale
in u is fixed, in t it scales as λ′: **the fraction → 0 as μ → ∞**. Sector discarded as a carrier of the extremal.

### 6.2 Sector 𝒮(σ, η): NO as a single edge; YES as multiple edges (ARGUED)

- g* is not literally in core_{T′}: g*(T) = −1.42·10⁻³⁴ ≠ 0 (edge layer, MORI15 §3). The core approximants have an
  edge layer of width ε and a jump-type tail cut off at Y ~ 1/ε.
- The jump of g* at the boundary produces jumps of f₁ of size μ(m)g*(T)/√λ at u = λ/m (MORI15 §3), i.e. **~6μ/π²
  edges coupled by Möbius**, at frequencies p_m = μ′/m in the universal variable (10 edges at μ = 15).
- With J = 0 (smooth tail) Mori **does not** enter: a 1/Y tail has ‖·‖_σ = ∞ for σ ≥ 1, and A → ∞ on the
  approximants.
- With a single edge it **does not** enter: there are ~μ edges of equal amplitude.
- What does hold without cancellation (ARGUED, triangle inequality + Gram matrix G of the F_{p_j}): τ ≤
  4.49·K·‖G^{−1}‖, with K ≍ μ ⇒ θ₀ ≍ 1/μ: a loss that destroys the chain (superpolynomial). Möbius cancellation
  is needed.
- **Stacking computation with Möbius signs (ARGUED).** The relevant sum is Σ_{m<μ′}μ(m)S(2πμ′X/m) =
  π[½M(μ′) − Σ_{m<μ′}μ(m){μ′X/m}]. In mean square (Franel correlations ⟨ψ(x/m)ψ(x/m′)⟩ = (m,m′)²/(12mm′), with
  (m,m′)² = Σ_{e|(m,m′)}J₂(e)) this gives
  Σ_e J₂(e)e^{−2}(Σ_{k<μ′/e, (k,e)=1}μ(k)/k)²,
  and with the bound |Σ_{k≤y,(k,e)=1}μ(k)/k| ≤ 1 (NOT VERIFIED: BIBLIO_CHECK_001 does not locate this statement;
  Ramaré Acta Arith. 165 (2014) gives 2.4(q/φ(q))/log(x/q); use that version) this is ≤ μ′ ≍ ‖r‖²/J². **ARGUED
  result: τ = O(1) for the Möbius-edge tail**, i.e. the Mori extremal would be in a sector of multiple Möbius
  edges with uniform θ₀. Gaps: (i) the Franel mean is taken over the full period mm′ and the window X ∈ (1,√2) is
  shorter; (ii) the term ½M(μ′) enters without cancellation; (iii) the exact shape of the smooth part of the tail
  of f* is not certified. Reading of the data: |ρ*| ≈ flat (7·10⁻³⁵ on [1,1.2], 8·10⁻³⁶ on [1.5,4]) with dense
  zero crossings, consistent with overlapping jump-type tails, not with a smooth tail (NUMERICAL, qualitative
  reading).

### 6.3 μ = 5, 10

**No data available**: the p1_*.json files (`p1_eig`, `p1_pieces`, `p1_zeros_check*`) are all for μ = 15.
Prediction (ARGUED): the Hermite scale is independent of μ, so the mass on |t| ≤ 1.4 is even smaller relative to
the ring at μ = 5, 10 just from the change in λ′ (analogous fractions 39 % at μ′ = 10 and 58 % at μ′ = 5, same
table), and the edge structure is the same with 4 (μ=5) and 7 (μ=10) Möbius edges.

---

## 7. Labels

- Identity §0 and Lemma 0 (B.1 from τ, without gauge orthogonality): **PROVED.**
- Prop. 1.1 (support |t| < √2 ⇒ no stacking, θ₀ tiny but uniform): **PROVED**; degenerate sector.
- Edge lemma τ(F_{p,φ}) ≤ 4.49 uniform: **PROVED.**
- **Theorem P3 on 𝒮(σ,η): PROVED**, θ₀ = (1 + (C₂/2)^{1/2}(2.122(1+η) + ζ(σ)η))^{−2}.
- Cor. 4.1 (stacking ∉ 𝒮): **PROVED.**
- Cor. 5.1 (polynomial chain on 𝒮): **CONDITIONAL** on the stability of 𝒮 across levels (OPEN).
- Mori ∈ sector |t| ≤ 1.4: **NO** (NUMERICAL, 23 % / 50 %). Mori ∈ 𝒮(σ,η) with a single edge or smooth tail: **NO**
  (PROVED given MORI15's jump structure). Mori ∈ sector of Möbius edges with τ = O(1): **ARGUED.**
- P3 in the requested form (sector containing the extremal, uniform θ₀): **OPEN**, reduced to Lemma P3-Möb (§8).
- Sign: none. **L′♯ OPEN. Row D OPEN.**

## 8. Entry for the index

> - **P3_SMOOTH_B1_001 (phase 200 r7; new reason vs B1_FLAT: the shape of the tail is restricted, not the support):**
>   B.1 restricted PROVED on 𝒮(σ,η) = {tails = one edge mode sin(2πpY+φ)/(πY) + remainder with moment Y^{2σ−1} ≤ η}:
>   θ₀ = (1+(C₂/2)^{1/2}(2.122(1+η)+ζ(σ)η))^{−2} (bounded sawtooth + Minkowski); harmonic stacking ∉ 𝒮
>   (contrapositive). Sector "|t| ≤ 1.4": no stacking (2u > 1.4) but does not contain Mori (mass 23 %/50 %). Mori has
>   ~6μ/π² edges coupled by Möbius: neither a smooth tail nor a single edge; τ = O(1) ARGUED via Franel +
>   |Σ_{(k,e)=1}μ(k)/k| ≤ 1. No sign. Do not retry: sectors by mass/support in t.
>   (`03-research/phase-200-sign-object/P3_SMOOTH_B1_001.md`)

**Next lemma (P3-Möb).** For p_m = P/m (P ≥ 1 real, m < P squarefree) and r = Σ_m μ(m)F_{p_m,φ} + E:
τ(r) ≤ C absolute. It is a mean-square inequality for Σ_{m<P}μ(m){PX/m} over X ∈ (1,√2) (Franel on a short window
+ coprime bounds for Σμ(k)/k), without Λ and without sign. If it goes through, the Mori extremal enters a sector
with uniform θ₀ and the chain of §5 becomes polynomial on that sector, except for the stability between levels.
