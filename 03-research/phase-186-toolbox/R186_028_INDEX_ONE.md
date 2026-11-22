# R186_028 — Index one: n₋(𝔞_T | L²(I_T)) = 1, the polar bookkeeping and the −1 eigenvalue

Phase 186, round 14. Sources: R186_026 (NUMERICAL finding n₋ = 1, Lemma 2.4, eigenvalue −1 OPEN); Paper 46 (eq:W, thm:A/eq:Aform, lem:K, prop:P, lem:polar, thm:parityschur, prop:polarcap, prop:arch, prop:archneg, thm:index, cor:KEP08, thm:log5W, thm:margin); R183_026 (n₋ ≈ 4T−2 on primitives); R155_047 (Thm P, n₋ ≤ 5/7/8); R185_008 §4 (W11). Parallel audit: R186_106 (robustness of n₋ = 1; here it is assumed and its reason is sought).
Script: `r028_index.py` (standalone; orthonormal Legendre Galerkin on I_T, dim 60, entirely in x-space; `python3 r028_index.py [N]` and `python3 r028_index.py extra`). Controls: 𝔞_T(e^{t/2}1_I) = −5.592275 at ½log5 (R186_026 closed form: −5.592), λ_A(½log3) = 9.46·10⁻⁴ (Paper 46: 9.45·10⁻⁴), stable at N = 30/45/60/80.

## 0. Verdict

1. **The reason n₋ = 1 is the pole, not the primes** (PROVED, §1). On L²(I_T), 𝔞_T = W_T − 2ℓ_ev² + 2ℓ_odd² (eq:W + thm:parityschur(o); ℓ_ev = ⟨F, cosh(t/2)1_I⟩, ℓ_odd = ⟨F, sinh(t/2)1_I⟩). If the full form is ≥ 0 on L²(I_T), then 𝔞_T ≥ 0 on the entire odd sector and has at most one negative direction, even, in the even sector (rank one from −2ℓ_ev²); and it has at least one because 𝔞_T(cosh(t/2)1_I) ≤ Γ(cosh(t/2)1_I) < 0 for T ≥ 0.12. **Theorem 1.4: n₋(𝔞_T|L²(I_T)) = 1 for 0.12 ≤ T ≤ ½log5**, PROVED modulo CITED (λ_W ≥ 0: Zhu Thm 1.2 up to 0.8, cor:KEP08; thm:log5W up to ½log5 with ball arithmetic).
2. **Exact statement for all T** (Theorem 1.2–Corollary 1.3, PROVED): n₋(𝔞_T|L²) = n₋(𝔞_T|𝒬_ev) + [𝔤_ev < 2] + n₋(𝔞_T|𝒬_odd) + [𝔤_odd < −2], with 𝔤_par the polar capacities of prop:polarcap. Hence "n₋ = 1 with an even negative direction" ⟺ D(T) ∧ 𝔤_odd(T) ≥ −2. The exact obstruction to proving n₋ = 1 for all T is row D itself (even sector) plus a weak lower bound on the odd polar capacity. It is not an independent lever.
3. **The −1 eigenvalue explained** (Theorem 2.1, PROVED): in the (A,B) normalization of R186_026, S_k = T𝔞_T⁻¹Tᵀ diagonalizes by parity with eigenvalues 2σ_ev = 2/(𝔤_ev − 2) and 2σ_odd = 2/(𝔤_odd + 2). The −1 is the inverse of the negative square of the pole (lem:polar), attained when 𝔤_ev → 0; the deviation is 𝔤_ev/(2 − 𝔤_ev) ≍ λ_W·‖h_ev‖² (thm:parityschur(a4)): −1.000755 at 0.36 (𝔤_ev = 1.5·10⁻³), −1.000000 from ½log3 on. The +1 at ½log5 is 𝔤_odd → 0 (8·10⁻¹²). With the (ℓ_ev, ℓ_odd) normalization the eigenvalues are −½, +½; with unitary Tate functionals, ∓1/(2 sinh T): the −1 is specific to (A,B), where the pole is exactly 2AB.
4. **Scalar criterion** (§3): for T ≥ 0.12 and 𝔞_T|𝒬 non-degenerate, D(T) ⟺ n₋(𝔞_T|L²) = 1 ∧ σ_ev < 0, σ_ev := ℓ_evᵀ𝔞_T⁻¹ℓ_ev (equivalent to det S_k < 0 from R186_026 L2.4). Under W_T ≥ 0 it reduces to 𝔤_ev < 2, always true with "margin" ≈ 2 that is not coercivity: all the content is in the hypothesis n₋ = 1 (= D ∧ 𝔤_odd ≥ −2), and the T-dependence runs through 𝔞_T⁻¹, whose minimum positive eigenvalue is ≈ λ_A. **NO-GO as a route**; the theorems are kept.
5. **Tension with R183_026 resolved** (§4): n₋(Γ|L²) = n₋(Γ|𝒫_T) + [Γ(h_ev) < 0] + [Γ(h_odd) < 0]; the "−2" of R183_026 are the two polar directions. The primes "remove" negative directions of Γ only in the sense that (i) 𝔞_T|𝒫_T ≥ 0 (that is D) and (ii) 𝔞_T(h_odd) > 0 (full odd positivity; nodal mechanism: Lemma 4.2). NUMERICAL byproduct for W11: A_∞ = Γ + pole dies at T ≈ 0.37 (odd sector), not at 0.4608 (prop:archneg is a bound).

**Sign contact: none.** Nothing here certifies λ_min(W|𝒫_T) < 0: λ_A > 0 in both sectors at every computed T (table §1.5), consistent with Paper 46.

## 1. Parity, pole and inertia

Notation (Paper 46 §thm:parityschur): 𝒟_T^{par} even/odd sectors of the form domain; ℓ_ev, ℓ_odd as above; 𝒬_par = ker ℓ_par ∩ 𝒟_T^{par}, so that 𝒫_T ∩ 𝒟_T = 𝒬_ev ⊕ 𝒬_odd; ε_ev = +1, ε_odd = −1; h_par the 𝔞_T-orthogonal vector to 𝒬_par with ℓ_par(h_par) = 1 (exists if 𝔞_T|𝒬_par is non-degenerate); 𝔤_par := W_T(h_par) = 𝔞_T(h_par) + 2ε_par (polar capacity, prop:polarcap). Γ := 𝔞_T with no primes.

**Lemma 1.1 (PROVED; eq:W, prop:P, thm:parityschur(o)).** For real F in 𝒟_T, 𝔞_T(F) = W_T(F) − 2ℓ_ev(F)² + 2ℓ_odd(F)², and the sum over sectors is orthogonal for L², 𝔞_T and W_T. In particular ℓ_ev and ℓ_odd are the only Tate functionals that matter: A = ℓ_ev + ℓ_odd, B = ℓ_ev − ℓ_odd, 2AB = 2ℓ_ev² − 2ℓ_odd² (lem:polar: signature (1,1)).

**Theorem 1.2 (inertia bookkeeping; PROVED).** Let 𝔅 ∈ {𝔞_T, Γ} and suppose 𝔅|𝒬_par is non-degenerate in both sectors (for 𝔞_T, λ_A > 0 suffices). Then
 n₋(𝔅|𝒟_T) = n₋(𝔅|𝒬_ev) + [𝔅(h_ev) < 0] + n₋(𝔅|𝒬_odd) + [𝔅(h_odd) < 0],
with 𝔅(h_par) = 1/σ_par, σ_par := ℓ_parᵀ𝔅⁻¹ℓ_par (the resolvent of 𝔅 at 0 on the polar vector).
*Proof.* thm:parityschur(a1) (whose proof uses only non-degeneracy): 𝒟_T^{par} = 𝒬_par ⊕ ℝh_par orthogonally for 𝔅, so 𝔅(G + xh) = 𝔅(G) + x²𝔅(h). That h_par = 𝔅⁻¹ℓ_par/σ_par and 𝔅(h_par) = 1/σ_par is the definition (𝔅(h,G) = 0 ∀G ∈ ker ℓ ⟺ 𝔅h ∝ ℓ). ∎

**Corollary 1.3 (PROVED).** (i) If 𝔞_T(cosh(t/2)1_I) < 0 then n₋(𝔞_T|L²) ≥ 1 and, under even-D (n₋(𝔞_T|𝒬_ev) = 0), 𝔞_T(h_ev) < 0 (thm:parityschur(a3): 𝔞_T(h_ev) = min{𝔞_T(F) : ℓ_ev(F) = 1}). Since Π_T ≤ 0 on positive functions (𝒞_F ≥ 0), 𝔞_T(cosh 1_I) ≤ Γ(cosh 1_I), which is an explicit function of T (R186_026 Lemma 1.2 with one block) negative for T ≥ 0.12 (1-D NUMERICAL, script §7a: −0.047 at 0.12, −0.84 at 0.25, −3.31 at ½log5; certifiable by interval arithmetic, not done).
(ii) Under D(T) and T ≥ 0.12: n₋(𝔞_T|L²) = 1 + [𝔤_odd < −2].
(iii) For T ≥ 0.12 and 𝔞_T|𝒬 non-degenerate: [n₋(𝔞_T|L²) = 1 ∧ σ_ev < 0] ⟺ [D(T) ∧ 𝔤_odd ≥ −2]. (⟸ by (ii); ⟹: n₋ = 1 and σ_ev < 0 force n₋(𝒬_ev) = n₋(𝒬_odd) = 0 and 𝔞_T(h_odd) ≥ 0.) Without the sign of σ_ev, n₋ = 1 does NOT imply D: the case n₋(𝒬_ev) = 1, σ_ev > 0 is compatible with n₋ = 1.

**Theorem 1.4 (index one on the certified range; PROVED modulo CITED).** For 0.12 ≤ T ≤ ½log5, n₋(𝔞_T|L²(I_T)) = 1, the negative direction is even, and 𝔞_T ≥ 0 on {F : ℓ_ev(F) = 0} = ker(A + B) (a single Tate functional).
*Proof.* λ_W ≥ 0 for T ≤ 0.8 (cor:KEP08, Zhu CITED) and at ½log5 (thm:log5W, certified), and λ_W is non-increasing in T. By Lemma 1.1, on the odd sector 𝔞_T = W_T + 2ℓ_odd² ≥ 0; on the even one 𝔞_T = W_T − 2ℓ_ev² matches W_T ≥ 0 on ker ℓ_ev (codimension 1), so n₋ ≤ 1 (min–max). n₋ ≥ 1 by Corollary 1.3(i). ∎
Remark: for T < ½log2 there are no primes and n₋(𝔞_T|L²) = n₋(Γ|L²) = 1 already at T = 0.25 (script table §5), 0 for small T (Γ(cosh 1_I)/‖·‖² = +1.79 at 0.02).

**1.5 Table (NUMERICAL, N = 60).** Inertias per sector (ev, od); λ_A per sector; λ_W.

| T | primes | n₋(Γ) | n₋(Γ\|𝒫) | n₋(𝔞_T) | n₋(𝔞_T\|𝒫) | λ_A(ev) | λ_A(od) | λ_W |
|---|---|---|---|---|---|---|---|---|
| 0.36 | 2 | 1,0 | 0,0 | 1,0 | 0,0 | 4.8e-1 | 8.2e-1 | 8.5e-4 |
| 0.45 | 2 | 1,1 | 0,0 | 1,0 | 0,0 | 6.6e-2 | 4.8e-1 | 1.6e-5 |
| ½log3 | 2 | 1,1 | 0,0 | 1,0 | 0,0 | 9.47e-4 | 3.3e-2 | 5.6e-8 |
| 0.62 | 2,3 | 2,1 | 1,0 | 1,0 | 0,0 | 1.8e-5 | 1.2e-3 | 3.9e-10 |
| log 2 | 2,3 | 2,1 | 1,0 | 1,0 | 0,0 | 1.0e-7 | 1.1e-5 | 8.4e-13 |
| 0.75 | 2,3,4 | 2,1 | 1,0 | 1,0 | 0,0 | 7.5e-10 | 9.4e-8 | 7.8e-14 |
| ½log5 | 2,3,4 | 2,1 | 1,1 | 1,0 | 0,0 | 3.4e-12 | 6.4e-10 | 7.4e-14 |

(λ_W and λ_A(ev) at ½log5 are at the double-precision floor; Paper 46 certifies λ_A ≥ 2.5·10⁻¹², λ_W ≥ 10⁻¹⁸.) The identity of Theorem 1.2 is checked row by row: e.g. ½log5, Γ: (1+1) + [Γ(h_ev) = −1.25 < 0] + [Γ(h_odd) = +303 > 0] = 3; 𝔞_T: 0 + [−2.000 < 0] + 0 + [+2.000 > 0] = 1.

## 2. The −1 eigenvalue and the negative direction

**Theorem 2.1 (PROVED).** Let S = T𝔞_T⁻¹Tᵀ with the rows of T being the functionals (A, B) (normalization of R186_026 L2.4). With L = [[1,1],[1,−1]] (LLᵀ = 2I) one has LSLᵀ = 2·diag(σ_ev, σ_odd) (the sectors decouple 𝔞_T⁻¹ and ℓ_ev ⊥ ℓ_odd by parity), so
 spec S = {2σ_ev, 2σ_odd} = { 2/(𝔤_ev − 2), 2/(𝔤_odd + 2) }.
If moreover W_T|par ≥ 0 and invertible, with ρ_par := ℓ_parᵀW_T⁻¹ℓ_par (Sherman–Morrison on 𝔞_T = W_T − 2ε_parℓ_parℓ_parᵀ): σ_par = ρ_par/(1 − 2ε_parρ_par), 𝔤_par = 1/ρ_par, and
 2σ_ev = −1/(1 − 𝔤_ev/2) = −1 − 𝔤_ev/2 + O(𝔤_ev²), 2σ_odd = 1/(1 + 𝔤_odd/2).
*Proof.* Algebra; 𝔤_par = 1/ρ_par is prop:polarcap (minimum of W_T with ℓ_par = 1). ∎
Reading: the −1 is −J⁻¹ in the (A,B) basis, the inverse of the negative square of the pole; S → −J exactly when both polar capacities → 0, which is the degeneration of the full form in each sector; by (a4), 𝔤_par/‖h_par‖² ∈ [λ_W,par, 2λ_W,par] when 2λ_W < λ_A. The "−1 as k grows" convergence of R186_026 is 𝔤_ev^{(k)} ↓ 𝔤_ev (the minimum restricted to E_k decreases with k).

NUMERICAL (script §2–3): 2/(𝔤_ev − 2) reproduces the negative eigenvalue of S to every printed digit at the seven T values (−1.000755, −1.000013, −1.000000, …); 𝔤_ev = 1/ρ_ev matches 𝔞_T(h_ev) + 2 in both columns (1.5·10⁻³, 2.6·10⁻⁵, 8.5·10⁻⁸, 5.8·10⁻¹⁰, 1.2·10⁻¹², ~10⁻¹³, ~10⁻¹³); 𝔤_odd = 7.5, 0.26, 1.3·10⁻³, 1.2·10⁻⁵, 3.6·10⁻⁸, 2.5·10⁻¹⁰, 8·10⁻¹². Three normalizations of T at ½log5: (A,B): −1.00000, +1.00000; (ℓ_ev, ℓ_odd): −0.50000, +0.50000; (A,B)/‖e^{±t/2}1_I‖: −0.55902, +0.55902 = ∓1/(2 sinh T).

**2.2 The negative direction (PROVED + NUMERICAL).** It is the negative eigenvector of W_e − 2ℓ_evℓ_evᵀ: v ∝ (W_e − μ₁)⁻¹ℓ_ev with μ₁ < 0 the root of 2ℓ_evᵀ(W_e − μ)⁻¹ℓ_ev = 1 (rank one, standard). It is not exactly any Tate mode: cos(v, cosh(t/2)1_I) = 0.988–0.998, cos(v, e^{t/2}1_I) = 0.972–0.983, cos(v, sinh 1_I) = 0, cos(v, h_ev) = 0.94 (0.36) → 0.66 (½log5); μ₁ = −1.34 (0.36) → −3.33 (½log5). The hypothesis is confirmed in shape: the negative direction ≈ the **even** Tate mode cosh(t/2)1_I (the sum e^{t/2} + e^{−t/2}), and 𝔞_T ≥ 0 on ker ℓ_ev (Theorem 1.4), which is more than the orthogonal complement.

## 3. Scalar criterion and honesty

**Proposition 3.1 (PROVED).** For T ≥ 0.12 with 𝔞_T|𝒬 non-degenerate: D(T) ⟺ [n₋(𝔞_T|L²) = 1 ∧ σ_ev < 0] ⟺ [n₋(𝔞_T|L²) = 1 ∧ det S < 0] (the second by Theorem 2.1: det S = 4σ_evσ_odd, and σ_odd < 0 with σ_ev > 0 would require n₋(𝔞_T|par) = 0, impossible by 1.3(i)). Haynsworth equivalent at the polar vector: 𝔞_T⁻¹ evaluated at cosh(t/2)1_I is negative.
**Structure.** σ_ev = 1/(𝔤_ev − 2). Under W_T|ev ≥ 0 the criterion is 𝔤_ev < 2 and holds with 𝔤_ev ≍ λ_W‖h_ev‖² ≪ 1: the "margin" 2 − 𝔤_ev ≈ 2 is the square of the pole, not coercivity; it does not measure the distance to λ_A = 0. At a first even contact (λ_A(ev) → 0), 𝔞_T|𝒬_ev degenerates, h_ev ceases to be defined (thm:parityschur(b)) and σ_ev passes through a 0/0 (the minimum positive eigenvalue of 𝔞_T|ev is ≈ λ_A, R186_026 §2.3, by interlacing with 𝒬_ev). All analytic T-dependence sits in 𝔞_T⁻¹, i.e. it inherits thm:margin. **NO-GO as a route.** What is kept: Theorem 1.2 (bookkeeping), Corollary 1.3, Theorem 1.4 (certified index one), Theorem 2.1 (the −1), Lemma 4.2.

## 4. Relation to R183_026, R155 Thm P, W11

**4.1 (PROVED by Theorem 1.2).** n₋(Γ|L²(I_T)) = n₋(Γ|𝒫_T) + [Γ(h^Γ_ev) < 0] + [Γ(h^Γ_odd) < 0]. The form of R183_026 (CC's K_I) is Γ|𝒫_T: n₋ ≈ 4T − 2; that of R186_026 is 𝔞_T over L²(I_T): the difference is the primes **and** the two polar directions. Values: n₋(Γ|𝒫) = 0, 0, 0, 1, 1, 1, 2 at the T values in the table (the second, odd, one appears at T ≈ 0.8026: λ_min(Γ|𝒬_odd) = +7.3·10⁻⁴ at 0.802, −2.7·10⁻³ at ½log5; consistent with R155_047's "1 at 0.80" and with the excluded intervals of thm:index); Thm P (n₋ ≤ 5/7/8) remains the only PROVED bound. Γ(h^Γ_ev) < 0 at every T ≥ 0.36; Γ(h^Γ_odd) < 0 for 0.45 ≤ T ≤ 0.75 and changes sign through a pole (Γ|𝒬_odd singular) at 0.8026.

**Lemma 4.2 (odd nodal mechanism; PROVED).** If F is odd and F ≥ 0 on (0,T), then 𝒞_F(u) ≤ 0 for u ≥ T; hence −v_n𝒞_F(log n) ≥ 0 for every n ≥ e^T: primes with log n ≥ T only add positivity in those odd directions. *Proof:* for u ≥ T, t ∈ (−T+u, T) ⊂ (0,T) and t − u ∈ (−T, 0). ∎ NUMERICAL: Γ(sinh 1_I)/‖·‖² < 0 from T = 0.5 on (−0.57 at 0.8) while 𝔞_T(sinh 1_I)/‖·‖² > 0 at every T (+0.28…+0.43). This is point (ii) of Verdict 5: full odd positivity is "primes against Γ" in the nodal directions, while (i) is D.

**4.3 Byproduct for W11 (NUMERICAL).** Polar capacities of Γ: 𝔤^Γ_odd = +16.4 (0.34), +5.0 (0.36), −3.0 (0.38); 𝔤^Γ_ev = +2.9·10⁻³ (0.34), +1.1·10⁻³ (0.40), −1.9·10⁻³ (0.42). So A_∞ = Γ + pole (Paper 46's λ_inf) becomes indefinite at T ≈ 0.37 through the odd sector and at ≈ 0.41 through the even one; n₋(A_∞|L²) = 0, 0, 1, 1, 2 at 0.34, 0.36, 0.38, 0.40, 0.42. This is consistent with prop:arch(iii) (≥ 0 for T < ½log2) and with prop:archneg (< 0 from 0.4608, which is a bound from the test F = t, not the threshold). Proposal for the grid: "A_∞ indefinite from ≈ 0.37 (NUMERICAL); PROVED from 0.4608".

## 5. Audit notes (R186_106)

- Theorems 1.2, 2.1 and Lemma 4.2 are algebra over results from Paper 46 (thm:parityschur(a1), prop:polarcap, lem:polar); Theorem 1.4 uses λ_W ≥ 0 CITED/certified up to ½log5 and the 1-D sign of Γ(cosh 1_I), NUMERICAL (closable in closed form with R186_026 (1.3)–(1.5), one block).
- What R186_026 called OPEN (the −1) is 2/(𝔤_ev − 2) with 𝔤_ev ≍ λ_W‖h_ev‖²; there is no new identity to falsify. The "inertia reduction by the primes" is not a mechanism: it is D plus full odd positivity.
- Nothing here certifies λ_min(W|𝒫_T) < 0 or gives information about T > ½log5 beyond the exact equivalence of Corollary 1.3(iii).
- For Paper 46: can be integrated as an observation after prop:polarcap (spec S = {2/(𝔤_ev−2), 2/(𝔤_odd+2)}; n₋(𝔞_T|L²) = 1 on the certified range; the 0.37 cutoff of λ_inf as NUMERICAL). Do not touch thm:margin or the grid from here.
