# R185_001 — Finite-dimensional circularity of the Λ-statements (box O166.802.1)

Phase 185 (crossword). Pure mathematics, no numerics. RH is never asserted.
Inputs: R166_802 (§1, Thm 0–4, Main theorem), R166_501 (Thm A, Rem A.3), R164_601 Thm 3.1/3.2,
Paper 47 (def:W, def:PD, prop:witness, thm:finZ).

## State

| Item | Statement | Label |
|---|---|---|
| Def 1 | Hierarchy 𝔅₀ ⊂ 𝔅₁, 𝔅₂, 𝔅₃, 𝔅₄; m-dimensional shadow of a statement | definition |
| Lemma 2 | Any set avoids the orthant O_U ⟺ it is contained in ⋃_i{t_i > U_i} | PROVED |
| Cor 2.1 | Boxes, finite unions of boxes, finite boolean combinations of intervals | PROVED |
| Lemma 3 | Half-space a·t ≥ c avoids O_U ⟺ a ≥ 0, a ≠ 0, c > a·U | PROVED |
| Lemma 4 | Moment cone C̄ of the real zeros; C̄* = {a : K_a ≥ 0 on ℝ} | PROVED |
| Thm 5 | (Finite-dimensional reduction) Every statement B, of any form, that excludes the witness through finitely many identities (1.1) implies a 𝔅₀ exclusion of a single admissible test K*, true for Λ_ζ | PROVED, in models (M1) and (M2) |
| Thm 6 | (Vector transfer) Exclusion is equivalent to a zero-side statement about (Z_{K_i}(Σ_ζ))_i, and to Z_{K*}(Σ_ζ) < Q^{hyp}_{K*} − S_{K*} for some K* | PROVED |
| Cor 7 | O166.802.1 is closed for 𝔅₂, 𝔅₃ and the finite shadow of 𝔅₄ | PROVED |
| Residual (ρ1) | Infinite families of non-power-type scales | OPEN |
| Residual (ρ2) | Exclusion of the *discrete* witness set (integer multiplicities) that does not exclude its convex hull | OPEN |
| Residual (ρ3) | Uniform choice of K* across hypothetical parameters | OPEN (not needed for circularity) |

**Corrections to the statement of the task.**
- **K1.** The proposed counterexample (B = {t₁+t₂ ≥ 1} ∩ {t ≤ 2}, U = (0.4,0.4)) is **not** an exclusion without a forced coordinate. Every point of B has t₁ > 0.4 or t₂ > 0.4, because otherwise t₁+t₂ ≤ 0.8. In the orthant model (M1), *no* statement excludes without forcing a coordinate (Lemma 2). The multiscale gain only exists in model (M2) and, even there, reduces to a single test K_a = Σa_iK_i (Thm 5(b)).
- **K2.** The "parabola" t₂ ≥ c t₁² only excludes if U₂ < 0; in that case the 𝔅₀ statement "Tail_{K₂} > U₂" already excludes. This is the particular case of Lemma 2.

## 1. Framework (that of R166_802 §1, unchanged)

- Witness F of type T_c, G = F̂ real with real zeros, G ≢ 0. Hypothetical quadruple at t_q, parameters π = (t_q, G).
- Admissible test: K continuous, K ≥ 0 on ℝ, of type ≤ Δ_max (with slack). The set 𝒦 of admissible tests is a **convex cone**.
- Identity (1.1): Z_K(Σ) = 𝔄_K − Tail_K(λ). The four maps K ↦ Z_K, 𝔄_K, Tail_K, Q_K are **linear** in K, because Ψ = G²K is linear in K and so is Ψ̌.
- Splitting Z_K = Q_K + R_K + O_K, with O_K = Σ_{γ real} G(γ)²K(γ) ≥ 0.

Fix tests K₁,…,K_m ∈ 𝒦 (scales Δ₁ < … < Δ_m allowed, even repeated). For a ∈ ℝ^m let K_a := Σ a_iK_i. Tail vector: t(λ) := (Tail_{K_i}(λ))_i ∈ ℝ^m. By linearity, a·t(λ) = Tail_{K_a}(λ) and likewise for 𝔄, Q, Z.

**Witness set.** For fixed parameters π, the witness is compatible with the tail vector t if there exist admissible o (contribution of real zeros) and r (other quadruples) with t = 𝔄 − Q^{hyp} − r − o. Two models:
- **(M1) R166_802 model (per-test bounds).** Only o_i ≥ 0 and r_i ≥ −S_i are used, for each i separately. Witness set: W₁ = O_U := {t : t ≤ U}, with U_i := 𝔄_{K_i} − Q^{hyp}_{K_i} + S_i.
- **(M2) Joint model.** Uses that the o_i come from the *same* real zeros and that r is controlled as a vector: r ∈ 𝓡 with 𝓡 closed convex (typical case: a single quadruple, 𝓡 = {0}). Convexified witness set: W₂ := 𝔄 − Q^{hyp} − 𝓡 − C̄, with C̄ the moment cone of Lemma 4.

## 2. The hierarchy of Λ-statements

**Def 1.** A Λ-statement is a property B of arithmetic functions λ that does not mention Σ, with B(Λ_ζ) true.
- **𝔅₀** (one test): Tail_K(λ) ∈ I, I an interval, K ∈ 𝒦.
- **𝔅₁** (power-size families): Tail_{K_Y}(λ) = O(Y^{δ'}) or Ω(Y^{δ}) with Δ = log(Y/X) → ∞ (R166_802 Thm 3).
- **𝔅₂** (linear multiscale): finite boolean combinations of 𝔅₀ conditions on K₁,…,K_m, and linear inequalities Σ a_i Tail_{K_i} ≥ c with arbitrary signs.
- **𝔅₃** (degree-d polynomial): P(Tail_{K₁}(λ),…,Tail_{K_m}(λ)) ≥ 0, or statements involving Tail_K(λ*λ), (Tail_K λ)², products Tail_K·Tail_{K′}.
- **𝔅₄** (non-polynomial multiplicative structure): Euler product, μ, support on prime powers, values log p, "λ = μ * log on ℤ".

**Shadow.** For B and K₁,…,K_m, the shadow is Sh_K(B) := {t(λ) : λ satisfies B}. If only the m identities (1.1) for K₁,…,K_m are used, then B excludes the witness exactly when Sh_K(B) ∩ W = ∅. This is Thm 0 of R166_802 read in coordinates. Let t_ζ := t(Λ_ζ) ∈ Sh_K(B).

**Coverage.**
- R166_802 covers 𝔅₀ (Thm 1–2) and 𝔅₁ (Thm 3). Both PROVED.
- O166.802.1 asks about 𝔅₂, 𝔅₃ and 𝔅₄. For these classes the "argued" rule of the Main theorem must be replaced by a proof.
- Every statement in 𝔅₂ or 𝔅₃ is by definition finite-dimensional (shadow in ℝ^m; for Tail_K(λ*λ) add the test corresponding to λ*λ: see Obs 8).
- A 𝔅₄ statement enters the framework through its shadow for any finite choice of tests. This is all that an argument using finitely many identities can extract from it.

## 3. Elementary lemmas

**Lemma 2. PROVED.** Let U ∈ ℝ^m and A ⊂ ℝ^m arbitrary. Then A ∩ O_U = ∅ ⟺ A ⊂ ⋃_{i=1}^m {t : t_i > U_i}.

*Proof.* t ∉ O_U ⟺ not (t_i ≤ U_i ∀i) ⟺ ∃i: t_i > U_i. Apply to each t ∈ A. ∎

**Cor 2.1. PROVED.**
- (a) A box ∏ I_i, with I_i nonempty intervals, avoids O_U ⟺ there is an i with I_i ⊂ (U_i, ∞).
- (b) A finite union of boxes avoids O_U ⟺ each box avoids it.
- (c) Every finite boolean combination of conditions "Tail_{K_i} ∈ I" is, in disjunctive normal form, a finite union of boxes, because the complement of an interval is a union of ≤ 2 intervals. Hence, if it excludes, for each box j there is a forced index i(j).

*Proof.* (a) If for every i there is s_i ∈ I_i with s_i ≤ U_i, then s = (s_i) ∈ box ∩ O_U. Conversely, if I_i ⊂ (U_i,∞), no point of the box lies in O_U. (b) is immediate. (c) is DNF plus (a) and (b). ∎

**Lemma 3. PROVED.** Let a ∈ ℝ^m and c ∈ ℝ, and let H = {t : a·t ≥ c}. Then H ∩ O_U = ∅ ⟺ a ∈ ℝ^m_{≥0}∖{0} and c > a·U. (The case a = 0 gives H = ∅ or H = ℝ^m; H = ∅ is false for Λ_ζ and is excluded.)

*Proof.*
- If a_j < 0, take t = U − s e_j, so that a·t = a·U + s|a_j| → ∞ as s → ∞. Then t ∈ O_U ∩ H for large s.
- If a ≥ 0, sup_{O_U} a·t = a·U, attained at t = U. So H ∩ O_U = ∅ ⟺ a·U < c. ∎

In test form: with a ≥ 0, K_a ∈ 𝒦 and a·t = Tail_{K_a}. The statement is the 𝔅₀ statement "Tail_{K_a} ≥ c". The condition c > a·U is Thm 1(a) of R166_802 for K_a with S_{K_a} := Σ a_iS_i. Mixed signs never exclude in (M1).

**Lemma 4 (moment cone). PROVED.** Let v(γ) := (G(γ)²K_i(γ))_i ∈ ℝ^m_{≥0}, and let C̄ be the closed convex cone generated by {v(γ) : γ ∈ ℝ}. Every vector o = (O_{K_i})_i of a real-zero configuration whose sums converge lies in C̄. Moreover:
  C̄* := {a : a·o ≥ 0 ∀o ∈ C̄} = {a : K_a(γ) ≥ 0 ∀γ ∈ ℝ}.

*Proof.*
- o = Σ_γ v(γ), a convergent series of elements of C̄. Its partial sums lie in the cone and C̄ is closed, so o ∈ C̄.
- a ∈ C̄* ⟺ a·v(γ) = G(γ)²K_a(γ) ≥ 0 ∀γ. This gives K_a ≥ 0 off the zeros of G, which are isolated because G is entire and nonzero. By continuity, K_a ≥ 0 on ℝ. The converse is immediate. ∎

Thus a ∈ C̄* ⟺ K_a ∈ 𝒦 (type ≤ max Δ_i ≤ Δ_max). The coefficients a_i can have **mixed signs**, as long as the combination is nonnegative on ℝ. When the K_i have distinct scales, C̄* is in general strictly larger than ℝ^m_{≥0}: this is the only possible "multiscale gain".

## 4. Finite-dimensional reduction theorem

**Thm 5. PROVED.** Fix π, K₁,…,K_m ∈ 𝒦 and any Λ-statement B (of any class 𝔅₂–𝔅₄, or any other). Suppose B excludes the witness through the identities (1.1) for K₁,…,K_m, i.e. Sh_K(B) ∩ W = ∅.
- **(a) Model (M1).** There is an index i such that Tail_{K_i}(Λ_ζ) > 𝔄_{K_i} − Q^{hyp}_{K_i} + S_i. That is, the 𝔅₀ statement for test K_i, true for ζ, already excludes the witness (R166_802 Thm 1(a)). Moreover B ⟹ ⋁_i [Tail_{K_i} > U_i].
- **(b) Model (M2), 𝓡 closed convex.** There exists a ∈ C̄*, i.e. K* := K_a ∈ 𝒦, such that
  Tail_{K*}(Λ_ζ) > 𝔄_{K*} − Q^{hyp}_{K*} + S_𝓡(a), with S_𝓡(a) := sup_{r∈𝓡} (−a·r) (finite for the chosen a).
  That is, the 𝔅₀ statement for the single test K*, true for ζ, already excludes the convexified witness. One can take a on an extreme ray of C̄* when C̄* has a compact base.

*Proof.*
- (a) By hypothesis Sh_K(B) ∩ O_U = ∅. By Lemma 2, Sh_K(B) ⊂ ⋃_i{t_i > U_i}. Since B(Λ_ζ) is true, t_ζ ∈ Sh_K(B), so there is i with (t_ζ)_i > U_i.
- (b) W₂ = w₀ − (𝓡 + C̄), with w₀ = 𝔄 − Q^{hyp}. If 𝓡 + C̄ is closed (e.g. if 𝓡 is compact), W₂ is convex and closed; in general replace W₂ by its closure, which only strengthens the exclusion hypothesis. Since t_ζ ∉ W₂, the strict separation theorem in ℝ^m (projection onto a closed convex set: if p is the projection of t_ζ onto W₂, then a := t_ζ − p ≠ 0 satisfies a·w ≤ a·p < a·t_ζ for every w ∈ W₂) gives a with
  a·t_ζ > σ(a) := sup_{w∈W₂} a·w.
  Now σ(a) = a·w₀ + sup_{r∈𝓡}(−a·r) + sup_{o∈C̄}(−a·o). The last term is +∞ unless a ∈ C̄*, and equals 0 in that case. Since σ(a) < ∞, a ∈ C̄*. By Lemma 4, K_a ∈ 𝒦, and the inequality is exactly as written, by linearity.
  Extreme ray: the function a ↦ a·t_ζ − σ(a) is positively homogeneous and concave, so the minimum of σ(a) − a·t_ζ over a compact base of the cone C̄* ∩ dom S_𝓡 is negative. If 𝓡 = {0}, it is linear and is attained at an extreme point of the base. ∎

**Logical consequence.** In either model, B ⟹ "∃ admissible test K* such that Tail_{K*} > U(K*)". The disjunction is finite in (M1) and indexed by C̄* in (M2). Hence **the exclusion of B factors through 𝔅₀**. The form of B is irrelevant: linear, quadratic, degree-d polynomial, or the shadow of a multiplicative statement. Only the support half-space in which the true vector t_ζ falls matters.

**Thm 6 (vector transfer). PROVED.** With the true data, t_ζ = 𝔄 − Z(Σ_ζ), with Z(Σ) := (Z_{K_i}(Σ))_i. Hence:
- (i) B excludes (Sh_K(B) ∩ W = ∅) ⟹ Z(Σ_ζ) ∉ 𝔄 − W, that is:
  - (M1): ∃i: Z_{K_i}(Σ_ζ) < Q^{hyp}_{K_i} − S_i;
  - (M2): Z(Σ_ζ) ∉ Q^{hyp} + 𝓡 + C̄.
- (ii) Equivalently, ∃K* ∈ 𝒦: Z_{K*}(Σ_ζ) < Q^{hyp}_{K*} − S(K*). This is the zero-side inequality of R166_802 Thm 2 for a single test.
- (iii) The weakest excluding statement is B_min := {λ : t(λ) ∉ W}. B_min(Λ_ζ) is **equivalent**, via the true (1.1), to the zero statement Z(Σ_ζ) ∉ 𝔄 − W. Every excluding B implies B_min, and B_min is exactly that zero statement.

*Proof.* Substitute t_ζ = 𝔄 − Z(Σ_ζ) into Thm 5 and into the definition of B_min. For B_min: Sh_K(B_min) ⊂ W^c by construction, and every excluding B satisfies Sh_K(B) ⊂ W^c, hence B ⟹ B_min on the tails. ∎

If the witness is real (Q^{hyp} = Q^{true} and r^{true} ∈ 𝓡), then Z(Σ_ζ) ∈ Q^{hyp} + 𝓡 + C̄ and (i) is false. So (i) is true only if the witness is absent. This is the circularity of R166_802, point 2, now for **every** finite-dimensional shadow.

**Cor 7. PROVED.** The Main theorem of R166_802, point 2, holds for the whole of 𝔅₂ and 𝔅₃ and for the finite shadow of 𝔅₄:
- every such statement that excludes the witness does so through a single lower bound on Tail_{K*}, K* ∈ 𝒦 a nonnegative-on-ℝ combination of the K_i;
- that inequality is equivalent to the zero-side inequality Z_{K*}(Σ_ζ) < Q^{hyp}_{K*} − S(K*), at the quadruple's frequency (R166_802 Prop 2.1 for K* located at γ_q).

**Obs 8 (concrete 𝔅₃). PROVED except where noted.**
- *Cauchy–Schwarz.* For λ ≥ 0 and weights w₁, w₂ ≥ 0 with w₂ > 0 where w₁ ≠ 0, (Σλw₁)² ≤ (Σλ w₁²/w₂)(Σλw₂) holds. It holds for every nonnegative measure, hence is **class-blind** (W3): every falsifier with λ ≥ 0 satisfies it. In the shadow it is a region that, by Thm 5, can only exclude by forcing a single tail. Moreover, since Ψ̌_K is not ≥ 0 for the family P (R164_601 Thm 3.2), Tail_K is not of the form Σλw with w ≥ 0, and the inequality does not even apply directly to the tails of P.
- *Selberg.* Λ log + Λ*Λ = μ * log² is an **identity** (W12). If a statement involves Tail_K(λ*λ), it reduces via the identity to tails of μ*log² and of Λ log. Λ log is Λ with weight log n, i.e. another test K′ (multiplying Ψ̌ by u): the shadow still lies in a finite ℝ^{m′} and Thm 5 applies. For tails of μ*log², they only count if an identity (1.1) ties their shadow to Σ; if not, they do not enter W and exclude nothing (Thm 0).
- *Parabola* t₂ ≥ c t₁² (c > 0). Meets O_U ⟺ U₂ ≥ 0, taking (0,0) or (t₁, ct₁²) with t₁ ≤ U₁ and ct₁² ≤ U₂, which is possible if U₂ ≥ 0 (t₁ = 0 or t₁ = −√(U₂/c)). If U₂ < 0, it excludes, but so does "Tail_{K₂} ≥ 0", which is 𝔅₀ (positivity, Prop 4.1 of R166_802) if Ψ̌_{K₂} ≥ 0 beyond X. No gain.

## 5. What remains of O166.802.1

**(ρ1) Infinite families. OPEN except for the power-type ones (𝔅₁, PROVED in R166_802 Thm 3).** With infinitely many tests at once, W lives in an infinite-dimensional space. Separation produces continuous functionals that may fail to be admissible tests, but rather limits of K_a (measures on the test space, non-summable combinations). This is the only way the factorization through 𝔅₀ can fail. It matches what Thm 3(c) says: the asymptotic information is global (exponent Θ − ½), not localized at γ_q.

**(ρ2) Discreteness. OPEN.** Thm 5(b) excludes the convexified witness U − 𝓡 − C̄. The real set uses sums of v(γ) with integer multiplicities and Riemann–von Mangoldt density. A non-convex B could avoid the real set without avoiding its hull. Such a B would use the integrality of the zero count, which is zero-side data (not Λ-side). Hence, even an exclusion of this type would be zero-side via Thm 6(i), though it would not factor through a single test. In (M1) this residual does not exist (Lemma 2 does not use convexity).

**(ρ3) Uniformity.** K* depends on π = (t_q, G). Circularity does not require uniformity. Whether a single K* works for all π is the ordinary certificate question (Paper 47). It is not resolved here.

**Can a statement about finitely many zero-side quantities Z_{K_i} be "weaker than RH" and still exclude?** Formally yes. Z_{K*}(Σ_ζ) < Q^{hyp}_{K*} − S is a single numerical inequality about Σ_ζ, for fixed π. What is known:
- (i) by Thm 6(i), if the quadruple π is present it is false, so its truth is equivalent (modulo the 𝓡 input) to the absence of that quadruple, not of all of them;
- (ii) thm:finZ (Paper 47) forbids a finite zero truncation from carrying a flat-top certificate, so excluding *all* π at once with finitely many tests cannot rest on finitely many zeros. What could be done is to cover the π's with tests K*(π), which is (ρ3);
- (iii) Theorem M / thm:finZ give no bound on the Z_{K*}(Σ_ζ) without zeros. Label: the existence of a proof of (i) from Λ-data for all π is exactly the open problem; this is not a new NO-GO.

## For the audit

1. **Linearity.** Everything depends on K ↦ Tail_K, 𝔄_K, Q_K, Z_K being linear and on 𝒦 being a cone. Both hold for Ψ = G²K with G fixed. If G is changed between tests (families of distinct witnesses), the reduction holds for each G separately.
2. **Model (M1) is that of R166_802.** There the only information about R is R_K ≥ −S_K test by test. With that information the conclusion is the strongest: always an original coordinate. There is no multiscale gain. The task's example was wrong (K1).
3. **(M2) requires 𝓡 closed convex** and uses the closed hull C̄. If someone proposes a B that exploits the non-convexity of the real zero set, it falls into (ρ2): explicitly OPEN, but by Thm 6 it is still a zero-side statement.
4. **Mixed signs.** Lemma 3 in (M1) excludes mixed signs. In (M2) they are allowed, but K_a must be ≥ 0 on ℝ, i.e. K_a ∈ 𝒦: nothing outside the R166_802 cone.
5. **Non-constructive choice.** Thm 5(a) produces "there exists i", not which one. A proof of B gives a proof of the disjunction, not of a disjunct. The disjunction is, by Thm 6, a disjunction of zero-side statements. Circularity is unaffected.
6. **Check against the paper's definitions:** 𝔄_K, Q_K and the class P are those of R166_501/R166_802. Before integrating, the editor must check the linearity of 𝔄_K in K against def:W/eq:nuw of Paper 47, in particular that the polar term is linear in Ψ.
7. RH is not asserted. Nothing here excludes a quadruple; the *form* of every possible exclusion is classified.

## For Paper 47

**Definition.** Let G be fixed and 𝒦 the cone of continuous K, ≥ 0 on ℝ, of type ≤ Δ_max. For K₁,…,K_m ∈ 𝒦 and a statement B about λ, let Sh(B) = {(Tail_{K_i}(λ))_i : B(λ)}. For hypothetical parameters π and a closed convex set 𝓡 ⊂ ℝ^m, the witness set is W_π = 𝔄 − Q^{hyp}_π − 𝓡 − C̄, with C̄ the closed convex cone generated by (G(γ)²K_i(γ))_i, γ ∈ ℝ. The per-test witness set is O_U, U_i = 𝔄_{K_i} − Q^{hyp}_{K_i} + S_i.

**Lemma (orthant).** A ∩ O_U = ∅ ⟺ A ⊂ ⋃_i {t_i > U_i}.

**Lemma (dual cone).** C̄* = {a ∈ ℝ^m : Σ a_iK_i ≥ 0 on ℝ}.

**Theorem (finite-dimensional reduction).** Let B be a statement true for Λ_ζ with Sh(B) ∩ W = ∅, with W = O_U or W = W_π. Then there exists K* ∈ 𝒦 in the cone generated by K₁,…,K_m over C̄* (K* = K_i for some i if W = O_U) such that
  Tail_{K*}(Λ_ζ) > 𝔄_{K*} − Q^{hyp}_{K*} + S(K*).
Equivalently, by the true explicit formula,
  Z_{K*}(Σ_ζ) < Q^{hyp}_{K*} − S(K*).
In particular, every linear multiscale, polynomial, or multiplicative statement that excludes the witness through finitely many identities factors through a single tail lower bound, and is equivalent to a zero-side inequality that is false if the hypothetical quadruple is present.

**Remark.** The reduction fails only at (ρ1) for infinite families of non-power-type tests and (ρ2) for exclusions using the integrality of the zero count. Both are OPEN.

## Honest assessment

O166.802.1 is **closed in finite dimension**. No statement about Λ (linear, quadratic, of any degree, or the finite shadow of multiplicative structure) excludes the witness in any way other than a lower tail bound of a single admissible test. By transfer, that bound is the zero inequality of R166_802 Thm 2. The question reduces to two genuine boxes: (ρ1) simultaneous use of infinitely many tests that do not form a power-type family, where separation may produce non-admissible functionals, and (ρ2) use of the integrality of the zeros, which is Σ-side information. Neither is a Λ-statement in the sense of 𝔅₂–𝔅₄. Labels: Lemmas 2–4, Thm 5, Thm 6, Cor 7 PROVED; (ρ1), (ρ2), (ρ3) OPEN; the cell "new finite-dimensional Λ-inequality" moves to NO-GO (circular, PROVED).

## Note (R185_091)

* Thm 5(b): "replace W₂ by its closure" does not hold; one must require t_ζ ∉ cl W₂, or 𝓡 compact, or rec(𝓡)∩(−C̄)={0}. W₂ is a relaxation: Cor 7 and "For Paper 47" should say "excludes W", not "excludes the witness". Lemma 4: C̄ generated over all γ∈ℝ (state it). Extreme ray: convex function. Thm 6: cite Weil admissibility for Ψ=G²K.
* Ready for Paper 47: Lemmas 2–4, Thm 5(a), Thm 6; Thm 5(b)/Cor 7 after correction.
