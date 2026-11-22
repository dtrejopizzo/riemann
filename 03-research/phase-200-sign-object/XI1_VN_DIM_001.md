# XI1_VN_DIM_001 — Lemma Ξ1.1: trace of the "Chebyshev element" and ax+b von Neumann dimension (phase 200, round 16)

Objective: L′♯ /

**Short verdict.** Lemma Ξ1.1 falls into case (a) and candidate Ξ1 is **NO-GO PROVED** in the form of
SPEC_SIGN_OBJECT_006 §D. There are three independent reasons:
- **Thm Ξ.1 (Fell).** d_T(g) ≡ 1 for every g ≠ 0, every T, every discrete group. The dimension sees neither g,
  nor Λ, nor h.
- **Thm Ξ.2 (spectral disjointness).** The ax+b representation on L²(ℝ) contains no nonzero L(G)-module, so the
  "intrinsic" reading of the definition is empty.
- **Thm Ξ.3 (trace = identity coefficient).** τ(V*Ш) only reads the n = 0 term. That term is the origin of the
  Ш form and contains no Λ. It equals 0 or −∞ depending on the convention, and in no case is finite, nonzero and
  arithmetic.

Two channel falsifiers add to this: L(G) ≅ L(G_B) ≅ L(G_K) ≅ R, the hyperfinite II₁ factor (Connes), and the
group exists for Beurling as well.

---

## 0. Index and corpus check

grep over `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` and `04_PHASES_100-189.md`:

| term | hits | relevant entry |
|---|---|---|
| "von Neumann" | only "von Neumann–Wigner codimension" (l. 425) | not a module dimension |
| "Murray" | 0 | — |
| module "dimension" | 0 | SPEC_006 §C row 4 "virgin → Ξ1" |
| "trace" | Selberg/Arthur traces NO-GO (l. 252); trace property = MW-5 (l. 254) | different class |
| "ax+b" | G5H-122 (04_PHASES l. 326): full affine carrier, "cofinal regularized-dimension anomaly; braiding sign cancels", DEAD | **closest one**: a regularized dimension was also requested there |
| "Bost–Connes / BC" | l. 250: Bost–Connes, Connes cocycle, Jones, ITPFI/Kakutani, Araki, "dead"; R9-04, G4H-159 G1, G8H-R160 #20, KMS #12 of AUDIT_193 | DEAD family |
| "V2.4", "rank one", "Chebyshev", "Ш" | INV_V_001/002 (l. 414–415): Thm V2.4 Chebyshev rigidity PROVED, NO-GO 𝒦_Ш, "do not retry Ш/Poisson/Zak as a positive form over Hecke vectors" | **hard restriction** |
| "factor type" | 0 | — |

Phase 158 (R158_000…005, "adele class", MW-5, OT-5′): the adèle class space is a restatement and MW-5 reduces
to OT-5′. This memo does not use 𝔸/ℚ^× as a space. It only uses 𝔸/ℚ as the Pontryagin dual of (ℚ,+), in
Thm Ξ.2, and as a disjointness tool, not as a sign object.

LEDGER_L5 row 4 ("positivity via categorical dimension"): virgin. SPEC_006's new reason relative to G5H-122 and
BC is accepted for launching this lemma: Murray–von Neumann dimension instead of KMS, and L²(ℝ) instead of
ℓ²(ℕ). The result below closes that row.

---

## 1. Rigorous definition

### 1.1 Group and algebra

G := ℚ ⋊ ℚ^×_{>0}, with product (b,a)(b′,a′) = (b + a b′, a a′), acting on ℝ by x ↦ ax + b.

- **ICC (PROVED, elementary).**
  - If b ≠ 0, the class of (b,1) contains {(cb,1) : c ∈ ℚ^×_{>0}}, which is infinite.
  - If a ≠ 1, conjugating (b,a) by (c,1) gives (b + c(1−a), a), which is infinite in c.
  - Hence L(G) is a II₁ factor with trace τ(x) = ⟨xδ_e, δ_e⟩ (CITED: Murray–von Neumann).
- **Amenable (PROVED).** G is metabelian.
- **Isomorphism with R (CITED: Connes 1976).** L(G) ≅ R, the hyperfinite II₁ factor.

**Decision: L(G), not the Bost–Connes crossed product.** C(Ẑ) ⋊ ℕ^× (or its ℚ/ℤ ⋊ ℕ^× version) belongs to the
DEAD family of the index (l. 250). The spec defines Ξ1 with L(G) precisely to get out of it (new reason
(i)–(ii)). I use L(G); in §3 I compare line by line with BC.

### 1.2 Representations

- **Natural representation.** π(b,a)f(x) := a^{1/2} f(ax+b) in L²(ℝ). It is unitary. By the composition rule it
  is an anti-representation, so I take π(g^{-1}), which changes nothing that follows.
- **Spec module.** 𝓗 := L²(ℝ) ⊗ ℓ²(G) with diagonal action U_g = π(g) ⊗ λ_g. This is the only reading in
  which "L²(ℝ) ⊗ ℓ²(G) left Hilbert module" makes sense.
- **Window data.** For g ∈ P_T, f_g := 𝓜⁻¹(test) in L²(ℝ), with INV_V_001's convention.
- **Spec objects.** 𝔐_T(g) := closed span of {U_h(f_g ⊗ δ_e) : h ∈ G}, and d_T(g) := dim_{L(G)} 𝔐_T(g).

### 1.3 The Chebyshev element

- **Ш as an operator.** In ℓ²(G), Ш := Σ_{n∈ℤ} λ_{(n,1)}, i.e., convolution by 1_{ℤ×{1}}.
- **V*Ш.** INV_V_002's transfer (V*Ш = 2 log|x|·Ш, Λ∗1 = log) gives V*Ш := Σ_{n≠0} 2 log|n| · λ_{(n,1)}.
- **Kernel in ℓ²(G).** K((b,a),(b′,a′)) = 2 log|b − b′| · 1[a = a′, b − b′ ∈ ℤ∖{0}].
- **Fourier representation.** In ℓ²(ℚ), Ш is multiplication by the measure δ_{Ẑ} on 𝔸/ℚ = (ℝ × Ẑ)/ℤ, the
  annihilator of ℤ in the dual of ℚ_disc. That set has zero Haar measure. Consequently Ш is **not** a bounded
  operator, is not in L(G) and is not affiliated with finite trace: its coefficient vector 1_ℤ is not in ℓ²(G).

### 1.4 The projector and the proposed quantity

- **Projector.** P_g is the orthogonal projector onto 𝔐_T(g). It commutes with U, so it is in the commutant.
- **Element E_T ≥ 0.** It is "built from V*Ш and the Γ_ℝ multiplier" (the spec does not give it explicitly). It
  acts on 𝓗 as x ↦ Σ c_h U_h.
- **Quantity.** τ(P_g E_T P_g) is understood as the module trace Tr_𝓗(P_g E_T P_g). It is the only sense in
  which "τ(PEP)" is defined for P in the commutant.
- **Conjectured relation (spec, OPEN).** 𝔞_T(g) = ‖g‖² τ(P_g E_T P_g) − ε_T(g), with
  ε_T(g) ≤ C μ^{−A} dist²(g, 𝒢̄_T), where 𝔞_T is the form from P46 def:W / eq:nuw (feasible dual (ν_w, 2, 0)).

---

## 2. Lemma Ξ1.1 and closing theorems

### Thm Ξ.1 (trivial dimension by Fell absorption) — PROVED

For any countable discrete group Γ, any unitary representation π of Γ on a Hilbert space H and any nonzero
ξ ∈ H, the cyclic submodule of (H ⊗ ℓ²(Γ), π ⊗ λ) generated by ξ ⊗ δ_e has dim_{L(Γ)} = 1.

*Proof.*
1. Let W(η ⊗ δ_h) := π(h^{-1})η ⊗ δ_h. It is unitary and satisfies W(π(g) ⊗ λ_g)W* = 1 ⊗ λ_g (Fell).
2. Since W(ξ ⊗ δ_e) = ξ ⊗ δ_e, the image of the submodule is the closure of {ξ ⊗ δ_h}, i.e.,
   ℂξ ⊗ ℓ²(Γ) ≅ ℓ²(Γ).
3. The dimension of ℓ²(Γ) as an L(Γ)-module is 1. ∎

**Corollary.**
- d_T(g) = 1 for every g ∈ P_T∖{0}, every T and every μ.
- The same holds for G_K with any K (h = 1, 2, 3, …), for any subgroup ℚ^×_{(P)} and for any "Beurling" group
  (§2.4).
- Moreover P_g = W*(p_{f_g} ⊗ 1)W, and hence Tr_𝓗(P_g E_T P_g) = ‖f_g‖² · τ(E_T).

**Consequence for the target theorem (NO-GO PROVED in this class).** The spec's identity would force
𝔞_T(g) = c_T ‖g‖² − ε_T(g), with c_T = τ(E_T) constant. Take g in the radical/core 𝒢̄_T, where ε_T(g) = 0 by
the spec's bound. There 𝔞_T(g) = c_T ‖g‖²:
- If c_T > 0, this contradicts the fact that 𝔞_T has a radical: Thm V1.3 / INV_V_001; the radical exists and
  𝔞_T ≡ 0 there (TEST_CG_001 "𝔔 ≡ 0 on the radical").
- If c_T = 0, then 𝔞_T = −ε_T ≤ 0 everywhere on P_T, which contradicts the certified positive values (Thm A of
  P46, Mori's ½log15).

So **there is no E_T in L(G) satisfying the identity**, however it is constructed. The reason is structural: a
cyclic projector in the commutant only remembers the norm of the generating vector.

### Thm Ξ.2 (spectral disjointness: the ax+b representation on L²(ℝ) is not an L(G)-module) — PROVED

π has no nonzero subrepresentations contained in λ_G^{⊕∞}. That is, no closed G-invariant subspace of L²(ℝ)
has a defined von Neumann dimension.

*Proof.*
1. Restriction to the additive part. In L²(ℝ), π|_ℚ is translation. By Fourier it is multiplication by
   e^{2πibξ}, so its spectral measure is ι_*(Lebesgue), with ι : ℝ → (ℚ_disc)^∧ = 𝔸/ℚ.
2. ι(ℝ) is the image of ℝ × {0} in (ℝ × Ẑ)/ℤ. Its preimage ℝ × ℤ is Haar-null, because ℤ ⊂ Ẑ is null.
3. So π|_ℚ has spectral type singular with respect to Haar measure.
4. By contrast λ_G|_ℚ ≅ ℓ²(ℚ)^{⊕|ℚ^×|} has Haar spectral type, and so does every subrepresentation of
   λ_G^{⊕∞}.
5. Mutually singular spectral types imply disjoint representations. ∎

Hence the reading "𝔐_T(g) ⊂ L²(ℝ), dim_{L(G)}" is empty, and the only meaningful reading is that of Thm Ξ.1,
which is trivial.

Thm Ξ.2 is what brings down new reason (ii) of the spec: "L²(ℝ) instead of ℓ²(ℕ)". L²(ℝ) is precisely the space
in which G has no dimension.

### Thm Ξ.3 (Lemma Ξ1.1 proper: τ(V*Ш)) — PROVED, case (a)

1. Neither Ш nor V*Ш are in L(G) nor affiliated with finite τ-measure (§1.3: the coefficients 1_ℤ and 2log|n|
   are not in ℓ²).
2. The formal trace τ(Σ c_h λ_h) := c_e gives:
   - τ(Ш) = 1, the n = 0 term;
   - τ(V*Ш) = 2 log|0|, which equals −∞ under the literal convention, or 0 if the origin is excluded, which is
     V2.1's convention (Σ_{n≠0}).
3. Spectral regularizations give the same result. Let p_N := 1_{(−1/2N, 1/2N) × Ẑ} ∈ L^∞(𝔸/ℚ) ⊂ L(ℚ). Then
   τ(p_N) = 1/N → 0, and N p_N → Ш weakly with τ(N p_N) = 1. The spectral support of Ш has τ-measure 0, so
   its spectral projector is 0.
4. **Structural point.** τ is the coefficient at the identity. The identity of G corresponds to Ш's n = 0 term,
   which is exactly the origin term ϑ(0) (C.1). The arithmetic is in log|n| = (Λ∗1)(n), n ≠ 0, and lives outside
   the identity, where τ is zero.
5. For any E in the algebra generated by V*Ш, translations and dilations, τ(E) is a function of the coefficient
   at e. For example, τ((V*Ш)*(V*Ш)) = Σ_{n≠0} 4 log²|n| = ∞. τ sees Λ only as divergent total mass or does
   not see it.

**The spec's case.** It is case (a): τ(E_T) ∈ {0, ∞} (or −∞). Moreover, by Thm Ξ.1, even if τ(E_T) were finite
and nonzero, the quantity τ(PEP) would be ‖g‖² τ(E_T) and would remember nothing of g. **Lemma Ξ1.1: NO-GO
PROVED.**

The relation with V2.4 is explained in §3: the NO-GO does not depend on V2.4, but it reinforces it.

### 2.4 Λ channel and falsifiers (phase-201 rule)

**Channel declared by the spec.** Joint action of (ℚ,+) and (ℚ^×,·), with Λ entering through E_T.

**What the analysis shows.**
- **(i) Euler as group structure.** ℚ^×_{>0} ≅ ⊕_p ℤ, so L(ℚ^×_{>0}) ≅ L^∞(∏_p 𝕋). This is a free abelian
  group of countable rank, isomorphic to the group of any Beurling prime system Γ_B. "Euler as a group" does
  not distinguish Λ from Beurling: **the Euler-as-group channel is empty (PROVED)**. What distinguishes Λ is
  the embedding log : ℚ^× → ℝ (the values log p), and τ does not see that embedding.
- **(ii) FE/Poisson.** Here the relevant co-compactness is ℚ ⊂ 𝔸, not ℤ ⊂ ℝ, and it enters only via
  𝔸/ℚ = dual of ℚ (Thm Ξ.2). The trace τ on L(ℚ) is the Haar integral on 𝔸/ℚ, which is the quotient's
  "Tamagawa measure". It is a constant, with no g.
- **(iii) Beurling falsifier.** The spec claims "Beurling has no ℚ, there is no G". **This is false.** Let A_B be
  the subring of ℝ generated by the Beurling numbers and their inverses (countable), and let
  G_B := A_B ⋊ Γ_B ⊂ Aff(ℝ). This group is ICC and amenable, so L(G_B) ≅ R ≅ L(G), and by Thm Ξ.1 d_T ≡ 1. The
  object exists for Beurling and gives the same number (PROVED). The falsifier kills Ξ1, because Ξ1 does not
  use the channel in a way the dimension registers.
- **(iv) a_P.** ℚ ⋊ ℚ^×_{(P)} is a subgroup of infinite index and is also ICC, with d ≡ 1. The spec's remark
  "Ш_P not G-invariant" affects E_T, but not the dimension, and τ(E_T) is again the coefficient at e.
- **(v) Epstein h = 2, K = ℚ(√−5) (D = −20).**
  - G_K = K ⋊ K^×/𝒪_K^× with 𝒪_K^× = {±1}. It is ICC and amenable, so L(G_K) ≅ R.
  - The class group **does not appear**: K^× only contains principal ideals, and the non-principal ideals are
    not elements of any group acting on K by multiplication.
  - So the formula "d = ½ d_principal + ½ d_non-principal" **does not exist in L(G_K)**. It requires replacing
    G_K with the groupoid of lattices / Hecke algebra of K-lattices (Connes–Marcolli–Ramachandran; Ha–Paugam).
    That is BC for imaginary quadratic fields, a DEAD family.
  - **Exactly: dim_{L(G_K)} = 1 for h = 1, 2, 3. The dimension is NOT sensitive to h (PROVED).**
- **(vi) cΛ and DH.** Same group, same d ≡ 1. The difference (c−1)·2log|x|Ш lives outside e, so τ does not see
  it.

**C-τ (discontinuity in the comb).** The spec counted on "the dimension jumping with the group's structure".
But L(G) ≅ R for every group in play (ICC + amenable, Connes), and the dimension of the cyclic submodule is 1
in all of them. There is no jump. **C-τ fails (PROVED)**, and C-θ as well.

---

## 3. V2.4 and Bost–Connes: line-by-line comparison

| aspect | Ξ1 (here) | V2.4 (INV_V_002) | Bost–Connes (R9-04, G4H-159, G8H-R160 #20, KMS #12) | G5H-122 |
|---|---|---|---|---|
| algebra | L(ℚ⋊ℚ^×) ≅ R | lattice kernels in L²(ℝ) | C*(ℚ/ℤ) ⋊ ℕ^×, flow σ_t(μ_n) = n^{it} | full affine carrier, ℓ²(ℕ) |
| where Λ lives | coefficients outside e of V*Ш | exact transfer V*Ш = 2log·Ш | partition function ζ(β) = Tr(e^{−βH}), H δ_n = log n δ_n | log p anomaly |
| positive functional | τ = coefficient at e, blind to Λ (Thm Ξ.3) | Hermitian lift ⇒ rank one | KMS_β states, β > 1: Gibbs with weights n^{−β} | cofinal regularized dimension |
| disguised rank one? | **yes**: P_g ≅ p_{f_g} ⊗ 1, rank one in the L²(ℝ) factor after Fell (Thm Ξ.1) | yes (PROVED) | the vacuum state is rank one in ℓ²(ℕ) | yes ("braiding cancels") |
| KMS state? | no; τ is the only trace state, KMS at β = 0 of the trivial flow | — | yes | — |
| Beurling | same object (G_B), same number | separates quantitatively, no sign | "core flow the same for Beurling" | — |
| h-sensitive | no (Thm Ξ.1, (v)) | — | yes, but only via the groupoid of K-lattices (DEAD) | — |

**Conclusion of §3.**
- The V2.4 risk materializes, although via a stronger route than V2.4's. Hermiticity is not needed: Fell reduces
  any cyclic projector to p_f ⊗ 1, which is rank one in the L²(ℝ) leg, and the dimension is exactly the
  dimension of that rank one.
- The BC risk appears as soon as one tries to recover sensitivity to h. The only structure weighting the
  principal fiber by 1/h is the system of K-lattices, which is BC for K (Ha–Paugam). G5H-122 had already died
  from the "regularized-dimension anomaly", and here the dimension has no anomaly because it is trivial.

---

## 4. Target theorem and SPEC_006 filter A

**How it would give L′♯.**
- If the identity of §1.4 existed, the output would be a bound of the type 𝔞_T ≥ −ε_T, not a count. The
  "dimension" only enters as the coefficient τ(PEP).
- A Murray–von Neumann dimension is real in [0,∞]. In this case it is integer (= 1) because the module is
  cyclic and free.
- By Thm Ξ.1 the identity is impossible (§2). Even if it were possible, "τ(PEP) ≥ 0 because E ≥ 0" would be
  positivity of a factorization E = F*F, i.e., G0: REF-D or certified.

| criterion | result |
|---|---|
| C-pol (lives in P_T) | the tests are in P_T, but d_T does not depend on the test (Thm Ξ.1). Passes formally, with no content |
| C-data (depends on g) | **fails**: P_g ↦ Tr(P_g E P_g) = ‖g‖² τ(E) |
| C-hom | trivial: τ is homogeneous |
| C-θ / C-τ (discontinuous in the comb) | **fails**: L(G_*) ≅ R for all and d ≡ 1 |
| C-E′ / C-Guo (h not averaged) | **fails**: h invisible in L(G_K) (2.4 (v)) |
| C-𝔖 / 13.1 | no average, but because there is nothing to average |
| REF-D | if E_T were defined with the kernel of 𝒲, it would be REF-D. But the prior objection (Thm Ξ.1) suffices |
| F10 (V2.4) | **fails**: rank one via Fell |
| F9 (channel + falsifier) | channel declared; the Beurling falsifier **kills** the object (2.4 (iii)) |

---

## 5. Tests

- **Mori μ = 15.** The prediction is d_T(g*) = 1 and τ(PEP) = ‖g*‖² τ(E_T) ∈ {0, ∞}. The margin
  4.98·10⁻⁷⁰ against ℓ* ≈ 8.6·10⁻⁷⁰ cannot be produced: the object gives no number depending on μ. **Vacuous
  (PROVED as a consequence of Thm Ξ.1 and Ξ.3).**
- **Lemma E (x² + 5y², T = 8/5, degree-56 witness G, value −3.479).** The G_K object predicts
  τ(PEP) = ‖G‖² τ(E) ≥ 0 if E ≥ 0, the same value as for ζ. It does not detect the negative witness, because it
  has no 1/h factor (2.4 (v)). **Falsified as an Epstein detector.**
- **h = 3 (D = −23), calibrator.** Q₁ +3.555 and Q₂ +1.763 are not reproduced: all relative dimensions are 1.

Numerical: none. None was necessary.

---

## 6. Labels, new restriction, index, next lemma

**Labels.**
- ICC and amenability of ℚ ⋊ ℚ^×_{>0}, G_K and G_B: PROVED (elementary).
- L(G) factor II₁: CITED (Murray–von Neumann). L(G) ≅ R: CITED (Connes 1976).
- Thm Ξ.1 (Fell, d ≡ 1, Tr(PEP) = ‖g‖² τ(E)): PROVED.
- NO-GO of the target identity: PROVED (via the radical, and the positive values of Thm A / Mori, CITED from
  the corpus).
- Thm Ξ.2 (spectral disjointness of π and λ_G): PROVED.
- Thm Ξ.3 / Lemma Ξ1.1 = case (a): **NO-GO PROVED**.
- Euler-as-group channel empty (ℚ^× ≅ Γ_B): PROVED.
- Beurling falsifier exists and gives the same thing: PROVED. What the spec says about it ("there is no G") is
  refuted.
- h-insensitivity in L(G_K): PROVED. h-sensitivity only via the groupoid of K-lattices = BC family: ARGUED, by
  identification with Ha–Paugam / CMR, CITED.

**New restriction (C-MvN).** No Murray–von Neumann dimension nor trace of a countable discrete group can carry
the window form. There are three reasons:
- (a) By Fell, every cyclic submodule of π ⊗ λ is free of rank 1, and its compression only remembers ‖g‖.
- (b) By spectral disjointness, geometric representations on L²(ℝ) of groups with a dense additive part are not
  L(Γ)-modules.
- (c) τ is the coefficient at the identity, and in a lattice that coefficient is the origin term, which contains
  no Λ.

Moreover, ℚ^×_{>0} is isomorphic as a group to any Beurling group, so the Euler product "as a group" is not a
channel. The arithmetic information is in the log embedding, and group traces do not see it. Row 4 of §C of
SPEC_006 is closed.

**Index entry (README, phase 200):**
> - **XI1_VN_DIM_001 (round 16, Ξ1 = ax+b von Neumann dimension over ℚ/K; Lemma Ξ1.1): NO-GO PROVED.** By Fell,
>   the submodule of L²(ℝ) ⊗ ℓ²(G) generated by f_g has dim_{L(G)} = 1 for every g, T and group, and
>   Tr(P_g E P_g) = ‖g‖² τ(E) (Thm Ξ.1). π ax+b on L²(ℝ) is disjoint from λ_G, because its spectrum on 𝔸/ℚ is
>   Haar-null (Thm Ξ.2). τ(V*Ш) is the coefficient at e = origin term, with no Λ (0 or −∞; Thm Ξ.3).
>   ℚ^×_{>0} ≅ Γ_Beurling and G_B exists (falsifier). L(G_K) ≅ R is blind to h, and sensitivity to h only via
>   K-lattices = BC (DEAD).
>   Restriction C-MvN: do not retry dimensions or traces of discrete groups (nor L(Γ) ≅ R) as carriers of the
>   window form. Closes §C row 4.

**Suggested next lemma.** The lesson is that the channel lies in the *embedding* log : ℚ^× → ℝ, not in the
abstract group. A candidate using Λ must use data that are not invariant under group isomorphism. Within the
round, Ξ3 > Ξ2 becomes the order. For Ξ3/Ξ2 a one-line prior test is required: "is the invariant a function only
of the isomorphism class of (ℚ^×, ℚ)? If so, NO-GO by C-MvN."

No Ξ1′ is proposed. The variants (Connes–Marcolli dimension of K-lattices, L² cohomology dimensions of G) fall
respectively into BC (DEAD) and into invariants of G's isomorphism class. For example, β^{(2)}_k of infinite
amenable groups are 0 (CITED: Cheeger–Gromov), so they too are empty.
