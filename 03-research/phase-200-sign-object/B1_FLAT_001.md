# B1_FLAT_001: Lemma B.1♭ (phase 200, round 4, parallel)

Pure mathematics, no numerical computation.
OPEN / NO-GO. **No sign is proved. L′♯ OPEN. Row D OPEN.**

**Read.** C1_DUPLICATION_001 §1 (B.1.a–c, B.1♭, obstruction in L²); Paper 46 def:ext, lem:ext-mob, prop:ext-gauge,
lem:ext-ellbound, prop:ext-univ, thm:ext-margin; K3_GAMMA_001 §2 (K3.1); index README (C1_DUPLICATION_001 entry, line
520). Index search for "B.1♭", "pile-up/stacking", "bounded Z": only the C1 entry appears (B.1♭ OPEN) and the
observation from DD_001 ("bounded Z only with weight ξ^s"). **The route does not appear as previously attempted.**

**Verdict.** B.1♭ is **FALSE** (NO-GO, PROVED), and for a stronger reason: **B.1 itself, in the uniform form
β_μ ≥ θ₀ > 0, is FALSE.** We construct g ∈ core_{T′} with ℓ_{T′}(g)/ℓ_T(g) ≤ C/log μ. The mechanism is a **harmonic
pile-up**: Möbius inversion in the ring, h_g = −Σ_{n≥2} f_g(n·), sums n dilations of bumps of height 1/n, and the
sum Σ1/n ≈ log K is paid at level T but not at level T′.

---

## 1. Exact statement of B.1♭ and gauge choice

**Conventions** (those of C1). μ = e^{2T}, λ = √μ, T′ = T − ½log 2, λ′ = λ/√2. The universal normalization of
prop:ext-univ is used **at level T′** (rescaling t = λ′x):
- representatives h(t) = f(t/λ′), supported on [−N′, N′] with N′ = μ/2;
- level-T′ gauge supported on [−1, 1]; level-T gauge supported on [−1/√2, 1/√2];
- leak band: 1 (level T′) and √2 (level T);
- ring 𝔸 = (1/√2, 1); tail window (T′, T) ↔ X ∈ (1, √2), or u = 1/X ∈ 𝔸.

Both leaks scale with the same factor λ′ (𝓕h(X) = λ′𝓕f(λ′X)), so **ℓ_{T′}/ℓ_T is invariant** under this
rescaling.

**Union or intersection?** The gauges are nested: 𝒢_T ⊂ 𝒢_{T′} (support [−1/λ, 1/λ] ⊂ [−1/λ′, 1/λ′]). Then:
- ∪_{S ≥ T′} 𝒢_S = 𝒢_{T′};
- ∩_S 𝒢_S = {0} (supports shrinking to the origin, with φ(0) = 0).

The correct object for B.1.c is the gauge **at the level where the starting infimum is taken**: 𝒢̄_{T′}. In the
universal normalization this is 𝒢̄_1. This is what C1 uses (f′ nearly optimal at T′ ⇒ r_{f′} ⊥ 𝒢̄_{T′}). The
intersection is trivial and useless.

**Statement (B.1♭).** Let
 τ_*(μ) := sup { ∫_1^{√2} |Zϱ(X)|² dX/X / ‖ϱ‖²_{L²(1,∞)} : ϱ ∈ (𝒢̄_1)^⊥, ϱ = 𝓕h|_{(1,∞)}, h ∈ 𝒟_{N′} },
where 𝒟_{N′} is the data class of prop:ext-univ with g = Eh ∈ core_{T′}. B.1♭ asserts sup_μ τ_*(μ) < ∞.

**Useful identity (PROVED, def:ext, Poisson with h(0) = 𝓕h(0) = 0).** For X > 1 and u = 1/X:
 Zϱ(X) = X^{−1/2} Σ_{n≥1} h(n/X),
 ∫_1^{√2} |Zϱ|² dX/X = ∫_{1/√2}^1 |S_h(u)|² du,  with S_h(u) := Σ_{n≥1} h(nu).

S_h restricted to 𝔸 is exactly the discrepancy δ from B.1.a(v), in this normalization.

---

## 2. Falsifier for B.1 (and hence for B.1♭)

### 2.1 Construction

Parameters:
- K ≥ 10 integer; w := K^{−3};
- u₀ ∈ (0.75, 0.95), outside the set {u : |u − m/n| < 3w for some n ≤ 2K, m ∈ ℕ}. That set has measure
  ≤ Σ_{n≤2K} n·6w ≤ 24K²w = 24/K < 0.2, so u₀ exists;
- b ∈ C^∞_c(−1, 1), b ≥ 0, b ≢ 0; β := b″/‖b″‖. Then β has zero mean and ⟨b, β⟩ = −‖b′‖²/‖b″‖ ≠ 0.

Define
 k₀(t) := Σ_{n=2}^{K} n^{−1} [ b((t − nu₀)/(nw)) + b((−t − nu₀)/(nw)) ]  (even),
 g := E k₀ restricted to the level-T′ window, i.e. g ↔ S_{k₀} on (1, N′).

Size assumption: K u₀(1 + w) + 1 < N′. K ≤ μ/4 suffices.

### 2.2 Properties of g (PROVED)

**(a) Supports.** The bumps of k₀ are centered at nu₀ ≥ 1.5, have width nw ≤ 2K^{−2}, and are disjoint
(separation u₀ ≫ nw). Moreover supp k₀ ⊂ [−N′ + 1, N′ − 1].

**(b) Möbius representative.** By lem:ext-mob (bijection), the Möbius inverse of g on [1, N′] is f_g = k₀|_{[1,N′]}.

**(c) g ∈ core_{T′}.**
- g is C^∞ and vanishes near t = N′ by (a).
- Near t = 1: S_{k₀}(t) = Σ_n k₀(nt) with t ∈ [1, 1 + w]. A term is nonzero only if |nt − mu₀| < mw for some m,
  and that forces |u₀ − n/m| < 3w with m ≤ K, excluded by the choice of u₀. Hence g ≡ 0 near t = 1, and g vanishes to all
  orders at both endpoints.

**(d) The prescribed ring.** By B.1.a(ii), on 𝔸 one has h_g(u) = −Σ_{n≥2} k₀(nu), because nu ≥ 2u > 1.41 > 1.
- Let W := (u₀ − w, u₀ + w). For u ∈ W, the term k₀(nu) receives the bump m only if |n − m|u₀ < mw + nw ≤ 6Kw < u₀,
  i.e. only if m = n.
- The diagonal term equals n^{−1} b((nu − nu₀)/(nw)) = n^{−1} b((u − u₀)/w).
- Therefore:
 **h_g(u) = −(H_K − 1)·b((u − u₀)/w) on W,** with H_K = Σ_{n≤K} 1/n.

This is the pile-up: K bumps of relative width w and heights 1/n all land on the same point u₀.

### 2.3 Upper bound on ℓ_{T′}(g) (PROVED)

Take the representative f′ := k₀ + c₀γ, with:
- γ ∈ C²_c(−1, 1) even, γ(0) = 0 and ∫γ = 1;
- c₀ := −∫k₀ = −2w(K − 1)∫b.

Then f′ is admissible at level T′:
- k₀ vanishes near 0;
- f′(0) = 0 and ∫f′ = 0;
- E f′ = g, because γ is a level-T′ gauge.

Since the leak is bounded by the total norm, leak ≤ ‖f′‖², one gets
 ℓ_{T′}(g) ≤ ‖f′‖² ≤ 2‖k₀‖² + 2c₀²‖γ‖² = 4w‖b‖²(H_K − 1) + O(w²K²) ≤ 5w‖b‖² log K  (K large),
using ‖k₀‖² = 2Σ_n n^{−2}·nw‖b‖² and w²K² = K^{−4} ≪ w log K.

### 2.4 Lower bound on ℓ_T(g) (PROVED)

**Setup.** Let f ∈ 𝒜_T(g) be arbitrary. By B.1.a(iv), f = A + B with:
- A := f·1_{|t|≥1/√2}, **fixed**: equals k₀ on [1, N′] and h_g on 𝔸, extended evenly;
- B := f·1_{|t|<1/√2}, **free**.

Let Q be the Fourier projection onto |X| < √2, so that leak_T(f) = ‖(1 − Q)f‖². Test with
ψ(t) := w^{−1/2}β((t − u₀)/w), which satisfies ‖ψ‖ = 1 and supp ψ = W ⊂ 𝔸.

**Step 1 (duality).** leak(f)^{1/2} ≥ |⟨(1 − Q)f, ψ⟩| = |⟨A, ψ⟩ − ⟨A, Qψ⟩ − ⟨B, Qψ⟩|. The term ⟨B, ψ⟩ vanishes
because the supports are disjoint.

**Step 2 (main term).** By 2.2(d),
 ⟨A, ψ⟩ = −(H_K − 1) w^{1/2} ⟨b, β⟩ =: −P,  with |P| ≍ w^{1/2} log K.

**Step 3 (Qψ is small).** ψ̂(X) = w^{1/2} β̂(wX) and β̂(0) = 0, so |β̂(s)| ≤ 2π|s|·‖tβ‖_{L¹}. Hence
 ‖Qψ‖² ≤ 2√2·w·(2π√2 w‖tβ‖₁)², i.e. ‖Qψ‖ ≤ C_β w^{3/2}.

**Step 4 (‖A‖ is moderate).** By Cauchy–Schwarz over the ≤ 2K nonzero dilations,
 ‖Σ_{n≥2} k₀(n·)‖_{L²(𝔸)} ≤ Σ_{n≤2K} n^{−1/2}‖k₀‖ ≤ 3√K‖k₀‖.
Hence ‖A‖ ≤ 4√K‖k₀‖ ≲ (K w log K)^{1/2} = K^{−1}(log K)^{1/2}.

**Step 5 (alternative over B).**
- **If ‖B‖ ≤ R** with R := |P|/(2C_β w^{3/2}) − ‖A‖ ≍ K³ log K: the errors from Step 1 sum to
  ≤ (‖A‖ + ‖B‖) C_β w^{3/2} ≤ |P|/2. Hence leak ≥ P²/4.
- **If ‖B‖ > R:** B is supported on [−1/√2, 1/√2], so ‖(1 − Q)B‖² ≥ (1 − χ_*)‖B‖². Here χ_* < 1 is the largest
  prolate concentration for time [−1/√2, 1/√2] and band [−√2, √2], i.e. c = 2π (absolute constant, Slepian–Pollak,
  CITED). Then leak^{1/2} ≥ (1 − χ_*)^{1/2}R − ‖A‖. This is ≍ K³ log K ≫ |P| for K large.

**Conclusion.** In both cases, and taking the infimum over f,
 **ℓ_T(g) ≥ ¼(H_K − 1)² w ⟨b, β⟩².**

### 2.5 Theorem (NO-GO for uniform B.1; PROVED)

For K ≤ μ/4 and K ≥ K₀ (absolute), the g from 2.1 satisfies g ∈ core_{T′} and
 ℓ_{T′}(g)/ℓ_T(g) ≤ 20‖b‖²/(⟨b, β⟩² log K).

With K = ⌊μ/4⌋:
 **β_μ := inf_{core_{T′}} ℓ_{T′}/ℓ_T ≤ C_b / log μ → 0.**

**Corollary (B.1♭ FALSE; PROVED).** B.1.c (PROVED in C1, conditional) gives: if τ_* < ∞ uniformly, then
β_μ ≥ θ₀ > 0 uniformly. This contradicts the Theorem. Hence **sup_μ τ_*(μ) = ∞**. Quantitatively, inverting the
θ₀ formula: (1 + (C₂τ_*(μ)/2)^{1/2})² ≥ c log μ, i.e. **τ_*(μ) ≳ log μ**.

**Alternative direct construction (ARGUED, not necessary).** One can also exhibit a ϱ ∈ (𝒢̄_1)^⊥ with
‖Zϱ‖²_{(1,√2)}/‖ϱ‖² ≳ log K. Take k = k₀ − σF, with σ a smooth cutoff vanishing on (−1, 1) and F ∈ PW_{[−1,1]} solving
Q₁(σF) = Q₁k₀. That equation is invertible because Q₁σQ₁ ≥ (1 − χ₀)Q₁. The correction F contributes to S_h at most
|F(u)| ≤ √2‖F‖ ≲ ‖k₀‖, and does not destroy the pile-up. This shows that **orthogonality to the gauge does not help**:
(𝒢̄_1)^⊥ only imposes "k constant on (−1, 1)," where k = 𝓕^{−1}ϱ_even, and that is a condition near the origin. The
pile-up lives at |t| > 1.4.

---

## 3. What is false and what is not

- **False (PROVED):**
  - B.1♭ in uniform form;
  - B.1 in the form β_μ ≥ θ₀ > 0;
  - in particular, B.1 with constant 1.
- **Not only via this route:** the falsifier attacks directly the ratio ℓ_{T′}/ℓ_T, not bound B.1.b. **Uniform B.1
  is closed.**
- **What survives (OPEN):**
  - (B.1-log): β_μ ≥ c/log μ. It is plausible because the harmonic pile-up is the worst case for Cauchy–Schwarz on
    Σ_n n^{−1/2}·n^{−1/2} (ARGUED, not proved).
  - (B.1-sector): uniform B.1 restricted to the smooth sector saturating K3.1 (ψ_{4j}). The falsifier is rough, with
    scale w = K^{−3}, and its leak lives at frequency ~K³, far from the low-index prolate sector. K3.1 is unaffected.
- **Consequence for the duplication chain.** Even if (B.1-log) were true, the chain μ_k = 2^k μ₀ accumulates
  ∏_{k≤m} c/log μ_k ≍ c^m/m!. That is exp(−log μ·log log μ·(1 + o(1))/log 2), i.e. **superpolynomial**. The target
  "polynomial loss μ^{−A}" of C1 (iii)/B.1.c **is not reached by transporting ℓ along ι** with the infimum
  over all of core_{T′}. There is a caveat: the worst g may change from one step to the next, and a chain applied to a
  fixed g could lose less. But C1's argument uses the infimum, so the bounded loss is that of the product.
- **Reminder.** B.1/B.1♭ are leak lemmas, with no Λ and no comb. Even in their true form they give no sign; they would
  only control ℓ along ι. This NO-GO does not affect W_T or L′♯ directly: it closes the tool, not the target.

---

## 4. Test at Mori μ = 15

**No comparable datum exists** (no new computation).
- ℓ* ∈ [4.4, 8.5]e−70 is a single extremal infimum at μ = 15. β_μ requires the pair of levels (15, 7.5) evaluated at the
  same g.
- At μ = 15, K ≤ μ/4 ≈ 3. The pile-up factor H_K − 1 ≈ 0.83 is O(1), so the NO-GO is **asymptotic** and
  predicts nothing visible at μ = 15.
- The sector saturating K3.1 (0.7306) is smooth, and the falsifier lives outside it.
- Consistency with C1: κ_band(14)/κ_band(7) = 1.08 (NUMERICAL in C1) does not discriminate either.

---

## 5. Labels

- Statement of B.1♭: correct gauge 𝒢̄_{T′} (= ∪_{S≥T′}𝒢_S); the intersection is trivial. **PROVED.**
- Identity ∫_1^{√2}|Zϱ|²dX/X = ‖S_h‖²_{L²(𝔸)}: **PROVED** (def:ext).
- Theorem 2.5, β_μ ≤ C/log μ: **PROVED** ⇒ **uniform B.1 NO-GO**, and **B.1 with constant 1 NO-GO**.
- B.1♭ (uniform τ_*): **NO-GO, PROVED** (via B.1.c); τ_*(μ) ≳ log μ.
- Direct construction in (𝒢̄_1)^⊥: **ARGUED.**
- (B.1-log) and (B.1-sector K3.1): **OPEN.**
- Polynomial loss from duplication via ι with a global infimum: **NO-GO** (superpolynomial even under (B.1-log)).
- Sign: none. **L′♯ OPEN. Row D OPEN.**

## 6. Index entry

> - **B1_FLAT_001 (phase 200 r4; new reason vs C1: direct test of B.1♭):** B.1♭ FALSE and **uniform B.1
>   FALSE** (PROVED): **harmonic pile-up** falsifier g = E k₀, k₀ = Σ_{n≤K} n^{−1}b((t−nu₀)/(nw)), w = K^{−3}.
>   The prescribed ring h_g = −Σ_{n≥2}k₀(n·) has a peak of height H_K−1 at u₀, which is free at level T′ and costs
>   leak at level T (duality with a zero-mean test plus prolate c = 2π) ⇒ β_μ ≤ C/log μ and τ_* ≳ log μ.
>   Orthogonality to the gauge does not help (it lives near 0). Still alive: β_μ ≥ c/log μ and B.1 on the smooth sector of K3.1 (OPEN).
>   Duplication chain with a global infimum: superpolynomial loss, NO-GO. Do not retry: bounding Z or ℓ_{T′}/ℓ_T
>   uniformly over the whole core. No sign. (`03-research/phase-200-sign-object/B1_FLAT_001.md`)
