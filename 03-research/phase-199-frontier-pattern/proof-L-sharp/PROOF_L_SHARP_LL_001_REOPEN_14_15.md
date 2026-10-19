# PROOF_L_SHARP_LL_001 — Joint reopening of constraints 14 and 15 (AUDIT_CONSTRAINTS_001 §3)

Prover (pure mathematics; NUMERICAL only on the already-existing boundary model of S_001).
No equivalence with RH or zeros is invoked.

## 0. Corpus / index and new reason
Index (ROUTES-TRIED-INDEX README, entries S_001, AUDIT_4, TEST_CG_001, AUDIT_5, U_001, AUDIT_CONSTRAINTS_001).
What is recorded as "do not retry": sign by harmonic; k≠l decoupling by PW type; free amplitudes; (C_G)(b) as
reduction; (C_G) in the L² gauge. **New reasons (AUDIT_CONSTRAINTS_001 §3, items 5–6):** (14) *grouped* sign with
*forced* coefficients ≡ 1 (not free amplitudes, not decoupling); (15) (C_G)(b) in the canonical gauge Π (U.2), not in the
L² gauge of TEST_CG, and on Π data (not C_c^∞), where the AUDIT_4 mirror is only CONDITIONAL.

## 1. Constraint 14: grouped form {1,2} ⊕ {k≥3}
**1.1 (PROVED, rewriting).** By S.1(a), G_h = Σ_{k≥1}G_k with G_k the truncated dilate u_k(v) = k^{−1/2}u_1(v+log k)1_{v>0},
forced coefficients 1. Set 𝔄 := G_1+G_2, 𝔅₃ := Σ_{k≥3}G_k (sum in L²(dτ) by S.1(b)). Then exactly
  Q(G_h,G_h) = A₁₂ + 2C + B₃,  A₁₂ = Q(𝔄,𝔄), B₃ = Q(𝔅₃,𝔅₃), C = Q(𝔄,𝔅₃),
i.e. the 2×2 form [[A₁₂,C],[C,B₃]] evaluated on the forced vector (1,1). Nothing else is free.

**1.2 (ARGUED, leading order, boundary law S.3).** Diagonal: Σ_k ρ(1)²(log k−1)/(2π²k²). Block {1,2}: ρ(1)²(−1+(log2−1)/4)/(2π²)
= −0.05455ρ(1)²; block k≥3 diagonal: ρ(1)²(−ζ′(2)−ζ(2)+1−(log2−1)/4)/(2π²) = +0.01871ρ(1)²; total −0.03584ρ(1)² (= S.5).
The cross terms have no closed form at this order (they are boundary terms at v = 0, scale log(l/k), S.4): NUMERICAL below.

**1.3 NUMERICAL** (boundary datum ρ = e^{−(X−1)}, ρ(1)=1, script S_001_endpoint extended to K=16, v ≤ 5, dv = 2·10⁻⁵;
`PROOF_L_SHARP_LL_001_grouped.py`):

| K | A₁₂ | B₃ | C | A₁₂+2C+B₃ | det |
|---|---|---|---|---|---|
| 8 | −0.06370 | +0.00614 | −0.00421 | −0.06598 | −4.1e−4 |
| 12 | −0.06370 | +0.00849 | −0.00503 | −0.06528 | −5.7e−4 |
| 16 | −0.06370 | +0.00993 | −0.00548 | −0.06473 | −6.6e−4 |

Row Q(G_1,G_l) ≈ −(log-type)/l², l=2…16 (−1.8e−3 … −6.5e−5): C converges; B₃ grows toward ≈ +0.0187 (diagonal) minus negative
cross terms (row 3: Q(G_3,G_l) < 0 for l ≥ 5). Block {k≥3} PD (λ_min = 3.4e−4 at K=16). Extrapolation K→∞ (ARGUED):
total ≈ −0.06 with margin |A₁₂| − B₃ − 2|C| ≈ 0.03 > 0. det < 0: the 2×2 is **indefinite**; its sign on (1,1) comes only from
|A₁₂| ≫ B₃, i.e. from harmonic k = 1 (diag −0.0557). With the pole (S.6): total −2.578 (as in S_001).

**1.4 Λ-specificity (ARGUED).** With dual weights b_k instead of 1 (cΛ / Beurling without Poisson has no object, S.7):
the diagonal total is Σb_k²(log k−1)/k², with no forced sign (b_1 = b_2 = 0 makes it positive). For the lattice αℤ (same
Poisson, dual α⁻¹ℤ) the law becomes (log(k/α)−1)/k², total ∝ −ζ′(2) − (1+log α)ζ(2) < 0 ⟺ α > e^{−0.430} = 0.650:
the grouped sign depends on the lattice normalization, which is that of ζ (coefficients 1, α = 1). It is not comb-generic
but neither is it a feature of Λ beyond "a_n ≡ 1" (consistent with S.7(iii)).

**1.5 NO-GO (ARGUED + NUMERICAL falsifier) for the fixed grouping.** The sign boundary of the diagonal is k* =
⌊√(X̄ξ₀)⌋ (S.3, localized data: ξ₀=10 ⇒ k* = 4): with {1,2} ⊕ {k≥3} the "positive" block contains negative harmonics and
stops being PD, while the total remains negative (−0.227). No fixed cutoff k* works for the whole class PW_μ.
The data-dependent cutoff, k*(ρ) ≈ √(τ/2π), is the point of the AFE (S.1(d)/R.4): grouping into k ≤ k* vs k > k* is
the approximate functional equation of the transform F_c, a partition of the plane (k,τ), not of harmonics.
**Closed class 𝒦^{group}:** proofs of Q(G,G) ≤ 0 via (block {k≤k₀} negative) + (block {k>k₀} PD) + (cross-term bound)
with k₀ independent of the datum. The variant with k₀ = k*(ρ,τ) is the AFE of the dual datum: it is not grouping.
**What survives (OPEN):** in the boundary model the sign is harmonic k = 1 against the rest; the relevant
quantity is the inequality |Q(G_1,G_1)| ≥ Q(Σ_{k≥2}G_k, ·) + 2Q(G_1,Σ_{k≥2}G_k) in the closed boundary form
(cross terms of G_1 in closed form with incomplete Γ: not computed here).

## 2. Constraint 15: (C_G)(b) in the canonical gauge Π
**2.1 Definition.** For an exterior datum ρ, Πρ ∈ 𝒱_μ ⊂ 𝒮(1,1)⁺ (U.2.1). G_Π := G[Πρ] := ρ₀(Πρ)/s − conj F_{c_Π},
c_Π := 2∫_1^∞Πρ·cos(2πξX)dX = (Πρ)^ (ρ even in |t|>1), via S.1(b).
**Prop 2.1 (PROVED, given that G_Π is defined).** Q(G_Π,G_Π) depends only on the class ρ + 𝒢̄: Π(ρ+r) = Πρ for r ∈
𝒢̄ = (𝒮(1,1)⁺)^⊥ (U.2.1(a)). This is the repair (i) of TEST_CG §6 (minimal-leak representative). In particular the radical
vector of TEST_CG §4 (Q(G,G) = +0.095‖ρ‖²) satisfies Πρ = 0 ⇒ G_Π = 0: the gauge falsifier **disappears**.
**Existence of G_Π: CONDITIONAL.** S.1 requires ρ = O(X^{−2}) (absolute convergence, one IBP); Πρ is only L² (Sonin
vectors not explicit, AUDIT_5). Hypothesis (H_Π): Πρ has decay O(X^{−2}) and c_Π = O(1/ξ) ("PW-type tails").

**2.2 Structure of the dual on Π data (PROVED, L² algebra).** Πρ = σ + βe₀, σ ∈ 𝒮(1,1), e₀ ∈ 𝒮(1,1)⁺ ⊖ 𝒮(1,1).
(a) (Πρ)^ ≡ const = β·ê₀(0) on (−1,1), and ρ₀(Πρ) = ½(Πρ)^(0): **the polar mode of S.6 is exactly the e₀ component** (σ
has ρ₀ = 0). (b) 𝒮(1,1) is 𝔉-stable: c_σ = σ̂ ∈ 𝒮(1,1), and by sector orthogonality (T Prop 3.3, CONDITIONAL
(H1)) 𝔔[σ̂] = 𝔔[σ_+ − σ_−] = 𝔔[σ].
**Theorem 2.2 (CONDITIONAL on (H_Π) + extension of the AUDIT_4 mirror to Sonin data + (H1) + (C1)).** Let
I(ρ) := 2𝔅[ρ] − R(1)G_h(0) + c₀ρ₀² − 2ρ₀ρ₁ (interface + residue + pole). On σ ∈ 𝒮(1,1) (β = 0):
  Q(G_σ,G_σ) = −𝔔[σ] + I(σ),   I(σ) = 2𝔅[σ] − R(1)G_h(0),
hence **(C_G)(b)_Π on 𝒮(1,1) ⟺ 𝔔[σ] ≥ I(σ) + κμ^{−A}‖σ‖².** *Proof:* mirror with c = σ̂, 𝔔_line[σ̂] = 𝔔[σ] by 2.2(b). □
With P.1 (𝔔 = −Q(G,G) + 2Q(F,G) + 2AB) this gives I(σ) = 2Q(F,G) + 2AB − 0, consistent with the constraint identity of
T_001 (on 𝒮_±: Q(F,G) − 𝔅 + ½R(1)G_h(0) = 0).

**2.3 Verdict on 15 (NO-GO for "(b) as reduction", CONDITIONAL on the same hypotheses).** On Π data the
mirror **closes on the same space**: the dual of a datum in 𝒮(1,1) lies in 𝒮(1,1) and has the same 𝔔. Thus
(C_G)(b)_Π is not 𝔔[c] ≥ 0 for another object, but 𝔔[σ] ≥ I(σ) for the same σ: **REF-D + shift I**. It is
strictly stronger than 𝔔 ≥ 0 if I ≥ 0, weaker if I ≤ 0, and equivalent modulo I. The reopening 15 thus reduces to a
single question: **the sign of I on 𝒱_μ**.
**Sign of I (ARGUED: indefinite).** In the direction e₀, I contains c₀ρ₀² − 2ρ₀ρ₁ with ρ₀ = β/2 and ρ₁ = ρ₁(σ) + βρ₁(e₀): the
cross term −βρ₁(σ) is linear in β and in σ, and there is no known compensation from 𝔅 in that off-diagonal cross term
(𝔅 is a finite-rank off-diagonal Θ_∞ coupling at y = 0). Without a link ρ₁(σ) ↔ 𝔅(σ,e₀), I is indefinite on the plane (σ, βe₀). On 𝒮(1,1) (β = 0)
I = 2𝔅 − R(1)G_h(0), sign OPEN.
**Computation at μ = 15 (NOT EXECUTED, justified):** the TEST_CG/EXTERIOR data are in the L² gauge or min-leak M=28, not in
Π; Π requires the projection onto 𝒮(1,1)⁺, with no explicit basis (AUDIT_5 §3); and (b) is unsolvable in double precision in the
directions near the band (TEST_CG §5). No honest number is available.

## 3. Honest result
- PROVED: 1.1 (grouped form = 2×2 on (1,1)); Prop 2.1 (gauge independence of Q(G_Π,G_Π), modulo existence);
  2.2(a) (polar mode = e₀ component of Πρ).
- ARGUED: 1.2 block constants; 1.4; 1.5 NO-GO 𝒦^{group} (NUMERICAL falsifier of S.3); indefinite sign of I.
- CONDITIONAL: Theorem 2.2 (H_Π, mirror on Sonin, (H1), (C1)).
- NUMERICAL: table 1.3 (boundary model, truncation v ≤ 5).
- NO-GO: (14) grouping with fixed cutoff; (15) (C_G)(b) as reduction also in gauge Π (closes on the same 𝒮(1,1)).
- OPEN: sign of I = 2𝔅 − R(1)G_h(0) (+ pole) on 𝒱_μ; dominance of k = 1 in closed boundary form.
**Do not retry:** fixed harmonic cutoffs {k≤k₀}⊕{k>k₀}; mirror of (C_G)(b) in gauge Π as reduction. No sign. Row D OPEN.
