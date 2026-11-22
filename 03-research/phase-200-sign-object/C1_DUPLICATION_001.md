# C1_DUPLICATION_001: duplication stability (C1), Lemma B.1, and count C3′ (phase 200, round 3)

There is a single computation, and it is a control one: a Mertens sum for C3′, in
exact arithmetic (NUMERICAL).
**No sign is proved. L′♯ OPEN. Row D OPEN.**

**Read.**
- SPEC_SIGN_OBJECT_003, complete (A.1–A.5, B.0, C1, C2, C3/C3′).
- Q2_LADDER_001 (Lemma R, Lemma and Theorem Q2.1, rough comb) and K3_GAMMA_001 (K3.1).
- Phase 199: MORI15_EXTREMAL_001 §4, PATTERN_001 §2 (Mori V κ table), AUDIT_CONSTRAINTS_001 (restrictions 1, 2, 11
  and 17), PROOF_L_SHARP_H_001 (§4, §5, class 𝒦_H).
- Paper 46: def:ext, lem:ext-mob, prop:ext-gauge, lem:ext-ellbound, prob:ext-L, prop:ext-univ, lem:monoT.
- Index: README (PATTERN_001, MECH_001, DD_001), 06_OPEN_RESIDUES (L2_016 at line 50, W-loc at line 37).

**Conventions.**
- μ = e^{2T}, λ = √μ, T′ = T − ½log 2, λ′ = λ/√2.
- 𝒜_T(g) = {f admissible at T : E_T f = g}.
- leak_λ(f) = ∫_{|ξ|>λ}|𝓕f|², with 𝓕 unitary (the convention of def:ext).
- In this memo, "L′♯ at level μ with constant κ" means W_T(g) ≥ κ·ℓ_T(g) on core_T, and κ(μ) is the best possible
  constant. The ratio ℛ = 2W/ℓ from the spec differs only by the factor 2.

---

## 0. Index check (rule)

- **L2_016 ("Frobenius doubling induction in T", NO-GO because Tate does not transport).** The spec's new reason is that
  bridge A.5 is 𝒲-isometric and that the polar row is gauge on the outside. **This is correct for map ι** (A.5 PROVED, I
  verified it: it is lem:monoT read in the quotient). **It does not reach the inductive step.** §2 proves that C1's step is L′♯
  at level μ, up to constants. The difference from L2_016 is real (there the transport failed; here the transport works),
  but the inductive step falls into another wall, that of §2.
- **W-loc / thm:nolocal.** C1 does not localize in x and does not use a partition of unity. The spec's reason holds and C1
  does not clash with W-loc.
- **Class 𝒦_H (H_001) and restriction 11.** Analyzed in §2.3. Verdict: C1(ii) is the version **integrated over a
  duplication block** of H_001's Grönwall scheme. It has the same closure condition, now as a statement about an
  infimum, which is the minimizer problem.
- **DD_001 (Schur, phase 199).** Already recorded that "Z is only bounded with weight ξ^s." §1.4 rediscovers this as an
  obstruction to B.1 and gives an explicit example.

---

## 1. Lemma B.1: ℓ_{T′}(g) versus ℓ_T(g) for g ∈ core_{T′}

### 1.1 The "trivial" argument runs the wrong way

For the **same** f, leak_{λ′}(f) ≥ leak_λ(f) holds. But the two infima run over different sets, with
𝒜_T(g) ⊂ 𝒜_{T′}(g) (A.5(b), PROVED). From the pointwise inequality one only gets

 ℓ_T(g) ≤ inf_{𝒜_T(g)} leak_{λ′}  and  ℓ_{T′}(g) ≤ inf_{𝒜_T(g)} leak_{λ′}.

Both bounds are upper bounds by the same quantity. **They do not compare ℓ_T with ℓ_{T′}.** The whole content of B.1 lies
in what it costs to go from 𝒜_{T′} to 𝒜_T, and that is what is now computed.

### 1.2 Exact description of the two sets (PROVED)

**Lemma B.1.a.** Let g ∈ core_{T′}, extended by zero to I_T. Let f_g be the Möbius inverse from lem:ext-mob at level T:

 f_g(u) = Σ_{m ≤ λ/u} μ(m)(mu)^{−½} g(log(mu)),  u ∈ [1/λ, λ].

Then:
- (i) f_g = 0 on [λ′, λ]. On [1/λ′, λ′], f_g coincides with the Möbius inverse at level T′.
- (ii) On the ring 𝔸 := (1/λ, 1/λ′), f_g = h_g, with h_g(u) := −Σ_{n≥2} f_g(nu).
- (iii) 𝒜_{T′}(g) = {f : f = f_g on [1/λ′, λ′], free on [0, 1/λ′) except for C², f(0) = ∫f = 0}.
- (iv) 𝒜_T(g) = {f ∈ 𝒜_{T′}(g) : f = h_g on 𝔸}.
- (v) For f′ ∈ 𝒜_{T′}(g), the discrepancy δ_{f′} := f′ − h_g on 𝔸 is exactly the level-T′ aliasing tail, read in the
  window (T′, T):

  δ_{f′}(u) = u^{−½}·Ψ̌^{(T′)}_{f′}(−log u),  and  ‖δ_{f′}‖²_{L²(𝔸, du)} = ‖Ψ̌^{(T′)}_{f′}‖²_{L²(T′,T)}.

*Proof.*
- (i) If u ≥ 1/λ′, every mu with mu ∈ supp g satisfies mu < λ′. The terms with mu ∈ (λ′, λ) vanish because g = 0 on
  [T′, T). This is the level-T′ formula.
- (ii) Möbius inversion in Σ_n f(nu) = u^{−½}g(log u) = 0 for u ∈ 𝔸. Also nu ≥ 2/λ > 1/λ′ if n ≥ 2, so those
  terms are already fixed by (i).
- (iii) This is lem:ext-mob at level T′.
- (iv) At level T, lem:ext-mob fixes f on all of [1/λ, λ]. By (i)–(ii), what is fixed is f_g on the block [1/λ′, λ′] (as at
  T′) plus the value h_g on 𝔸. C² regularity at ±1/λ′ holds because the level-T Möbius formula is C²: g vanishes to
  second order at ±T′.
- (v) For x = log u ∈ (−T, −T′) and n ≥ 2, f′(nu) = f_g(nu). Then
  Φ_{f′}(x) = e^{x/2}(f′(u) + Σ_{n≥2} f_g(nu)) = e^{x/2}(f′(u) − h_g(u)).
  The norm follows from the change of variable u = e^x. □

**Reading.** B.1 does **not** compare two prolate problems with different bands. The large block [1/λ′, λ′] is fixed
by g at both levels and is the same function. The only difference is:
- (α) the leak band drops from λ to λ′;
- (β) at level T the small ring 𝔸 becomes **prescribed**. The prescribed value differs from the level-T′ optimum exactly by
  the T′ aliasing tail on the new window.

### 1.3 The spec's indication (advantage e^{2π(√2−1)μ}) is incorrect (ARGUED, with PROVED cause)

The spec argued that, in the sector saturating K3.1, ℓ_{T′}/ℓ_T is huge because d₄(c_{T′}) ≫ d₄(c_T). By B.1.a this does
not apply: the support of every f ∈ 𝒜_T(g) is [−λ′, λ′] (PROVED). The two leaks are then the same f_g measured outside
λ′ and outside λ, plus the ring adjustment. For a fixed function supported on [−λ′, λ′], the ratio
leak_λ/leak_{λ′} depends on the shape of the tail of 𝓕f beyond the band:
- it is an O(1) ratio;
- it is ≈ (λ′/λ)^{2k−1} if the tail decays like |ξ|^{−k};
- it is not exponential in μ.

**Conclusion: β_μ is O(1) and there is no exponential margin.** B.1 with constant exactly 1 is a fine question.

### 1.4 What is proved: B.1 with a constant, conditioned on a universal, μ-free constant

**Lemma B.1.b (PROVED).** For g ∈ core_{T′} and f′ ∈ 𝒜_{T′}(g),

 ℓ_T(g) ≤ ( leak_λ(f′)^{½} + C₂^{½}·‖Ψ̌^{(T′)}_{f′}‖_{L²(T′,T)} )²,  with C₂ := 2 + C_β(√2 − 1),

where C_β := ‖β‖²_{L²} for a fixed profile β ∈ C²_c(−1, 1) even, with β(0) = 0 and ∫β = 1.

*Proof.*
1. Let δ̃ equal δ_{f′} on ±𝔸 (even extension), plus −b on [−1/λ, 1/λ].
2. The profile b is chosen as in lem:ext-ellbound: b(x) = 2λI·β(λx) with I = −∫_𝔸 δ (so ∫δ̃ = 0), plus C² splices at ±1/λ
   of arbitrarily small L² cost. This is the lem:ext-ellbound technique.
3. δ̃ is C², supported on [−1/λ′, 1/λ′], and has δ̃(0) = ∫δ̃ = 0. Hence δ̃ ∈ 𝒢_{T′}.
4. f′ − δ̃ equals h_g on 𝔸 and f_g on the large block, so f′ − δ̃ ∈ 𝒜_T(g) by B.1.a(iv).
5. Triangle inequality in L²(|ξ| > λ):
   √leak_λ(f′ − δ̃) ≤ √leak_λ(f′) + ‖δ̃‖_{L²(ℝ)}.
6. Bounds: ‖δ̃‖² ≤ 2‖δ‖² + ‖b‖² + o(1), and ‖b‖² ≤ λ·C_β·|I|²·(1+o(1)) ≤ C_β(√2 − 1)‖δ‖², by Cauchy–Schwarz on 𝔸, whose
   length is (√2 − 1)/λ.
7. One concludes with B.1.a(v). □

**Corollary B.1.c (CONDITIONAL on Lemma B.1♭).** Let

 τ_* := sup ∫_1^{√2} |(Zϱ)(X)|² dX/X / ‖ϱ‖²_{L²(1,∞)},

over ϱ ∈ (𝒢̄_1)^⊥ with ϱ in the closure of the admissible tails, in the universal normalization of prop:ext-univ.
- **τ_* does not depend on μ.** Rescaling r(ξ) = λ′^{−1}ϱ(ξ/λ′), the window (λ′, λ) becomes (1, √2) and both sides scale
  by λ′^{−1}. This is prop:ext-univ at level T′ (PROVED).
- If τ_* < ∞, take f′ nearly optimal at level T′: leak_{λ′}(f′) ≤ ℓ_{T′}(g) + ε, with r_{f′} nearly orthogonal to 𝒢̄_{T′}.
  Then leak_λ(f′) ≤ leak_{λ′}(f′), and ‖Ψ̌‖² ≤ τ_*·‖r‖² = τ_*·leak_{λ′}(f′)/2.
- Result:

 **β_μ := inf_{core_{T′}} ℓ_{T′}/ℓ_T ≥ θ₀ := (1 + (C₂τ_*/2)^{½})^{−2} > 0, uniform in μ.**

**Lemma B.1♭ (OPEN, Λ-free, μ-free): τ_* < ∞.**
- **Obstruction (PROVED): Z is not bounded on L²(1,∞).** Example:
  - Fix X₀ ∈ (1, √2), K ≥ 1, and w < X₀/(3K).
  - Let ϱ = Σ_{n≤K} n^{−1}·b((ξ − nX₀)/(nw)), with b ≥ 0 a bump supported on (−1, 1). The supports are disjoint.
  - Then ‖ϱ‖² ≍ w·Σ n^{−1} ≍ w·log K.
  - Instead Zϱ ≥ (Σ_{n≤K} n^{−1})·b((X − X₀)/w) near X₀, so ∫|Zϱ|² ≳ w·log²K.
  - The ratio is ≳ log K → ∞.

  This agrees with DD_001 ("Z bounded only with weight ξ^s").
- **What is missing.** B.1♭ must use either the orthogonality to 𝒢̄_1, or the C²/admissible structure of the tails. It is a
  question of pure harmonic analysis: is the orthogonal complement of the universal gauge contained in the domain with
  weight ξ^s?
- **Mismatch with the target.** The target asked for β_μ ≥ 1. **This is not needed**: β_μ ≥ θ₀ > 0 uniform gives a loss
  θ₀^{log₂ μ} = μ^{−log₂(1/θ₀)} over the duplication chain, which is polynomial. **B.1 with constant 1: OPEN.** No
  proof or falsifier was found, because the cross term of 1.4 has an indefinite sign.

**B.1 labels.**
- B.1.a and B.1.b: PROVED.
- B.1.c: CONDITIONAL on B.1♭.
- B.1 with constant 1: OPEN.
- The spec's exponential indication: WITHDRAWN (ARGUED).
- C1(i), in the necessary form β_μ ≥ θ₀: reduced to B.1♭, a universal prolate-and-gauge constant, Λ-free.

---

## 2. C1 against restriction 11 and class 𝒦_H

### 2.1 Condition (iii) of C1 is free (PROVED)

√ℓ_T is a seminorm on core_T. It is the distance to a subspace, composed with g ↦ r_f, which is linear (prop:ext-gauge
plus lem:ext-mob). Hence, for every decomposition g = g_o + g_n,

 ℓ_T(g) ≤ 2ℓ_T(g_o) + 2ℓ_T(g_n).

No angle bound is needed; only a factor 2 is lost per step.

### 2.2 The inductive step is equivalent to L′♯ at level μ (PROVED, modulo the existence of the projection)

**Proposition C1.1.** Let κ_new(μ) := inf_{ℐ^{new}_μ} W/ℓ_T. Suppose the 𝒲-orthogonal decomposition
core_T = core_{T′} ⊕_𝒲 ℐ^{new} exists. In finite dimension (Galerkin) it is automatic if W ≻ 0 on core_{T′}; in
infinite dimension it is CONDITIONAL. Then

 ½·min(β_μ κ(μ/2), κ_new(μ)) ≤ κ(μ) ≤ κ_new(μ).

*Proof.*
- **Right side:** the infimum over a subset is at least as large.
- **Left side:**
  - W_T(g) = W_T(g_o) + W_T(g_n), by orthogonality.
  - W_T(g_o) = W_{T′}(g_o) ≥ κ(μ/2)ℓ_{T′}(g_o) ≥ κ(μ/2)β_μ ℓ_T(g_o), by lem:monoT and the definition of β_μ.
  - W_T(g_n) ≥ κ_new ℓ_T(g_n).
  - One concludes with 2.1. □

**Consequence.** C1(ii), "κ_new(μ) ≥ θκ(μ/2)," is thus sandwiched:
- κ(μ) ≥ θκ(μ/2) implies C1(ii), because κ_new ≥ κ(μ);
- C1(ii) implies κ(μ) ≥ ½θβ_μ κ(μ/2).

**C1(ii) is "κ(μ) ≥ θ′κ(μ/2)" up to absolute constants.** This is exactly the form of the target, "κ(2μ) ≥ θκ(μ)," and the
duplication chain turns it into L′♯ by induction. The complement ℐ^{new} is not a fixed codimension independent
of W: W itself defines it. Moreover, in raw coordinates, the form restricted to ℐ^{new} is the **Schur complement**

 S_new = W_nn − W_no W_oo^{−1} W_on.

W_oo^{−1} has norm of order 1/(κ(μ/2)·d₄(c_{T′})) ~ e^{+2πμ}·poly, and that is the "Schur plank" structure from DD_001.
**That is why the spec's observation ("(ii) is not 𝒲[g]") is not enough for P10.** (ii) is not literally 𝒲[g], but it is
equivalent to L′♯ at level μ given level μ/2: **REF-D (PROVED as an equivalence up to constants).**

### 2.3 Is it 𝒦_H? (restriction 11)

H_001 §4 fixes the closure condition of the Grönwall scheme with a polynomial budget: the relative loss per contact
must be O(A log²μ/μ) on average, and the drift between contacts (ρ_N − ρ_L at the minimizer) must compensate the observed
sawtooth. In a block [μ/2, μ) there are of order μ/(2 log μ) new contacts. The block's total budget is a factor
2^{−A}, a constant, and that is exactly C1's θ. Therefore:
- **C1(ii) = (H) integrated over a duplication block.** log κ(μ) − log κ(μ/2) is the telescoping sum of the jumps at
  new contacts plus the drift between them. By 2.2, that sum is what C1(ii) bounds.
- **The formal difference is real:** C1 is discrete and does not differentiate with respect to T. But it is cosmetic. The
  infimum κ_new is realized, in Galerkin, in the new component of the level-μ minimizer. **Any lower bound on κ_new
  goes through the μ-minimizer, or is a uniform bound over ℐ^{new}.**
- **A uniform bound of that type is a quantitative positivity statement.** It is W ≥ θκ ℓ on an infinite-codimension
  subspace defined by W. It is neither a square nor a count. §3 shows that in the new directions there is no
  exact signed counting term.

**New reason against 𝒦_H: not found.** The requested decomposition does not exist (old directions = ι-image, and new ones
with positivity that is a square or a count):
- the old ones are controlled (B.1, conditional on B.1♭);
- the new ones are the Schur complement;
- the only exact appearance of Λ among them is radical (§3.2).

**Verdict: C1 as a route to L′♯ is NO-GO (REF-D by Prop. C1.1 + integrated 𝒦_H class, restriction 11).** Kept
as tools: B.1.a, B.1.b, the factor 2 from 2.1, Prop. C1.1, and A.5.

---

## 3. The new directions, explicitly

### 3.1 The form on the new directions

Let g ∈ core_T and let P_o be the 𝒲-projection onto core_{T′}. For the new part g_n = g − P_o g, in the window:

 W_T(g_n) = (1/2π)∫m|ĝ_n|² + 2A(g_n)B(g_n) − Σ_{n<μ/2} v_n c_{g_n}(log n) − Σ_{μ/2≤n<μ} v_n c_{g_n}(log n).

The new contacts n ∈ [μ/2, μ) are 8, 9, 11, 13 when μ = 15 (prime powers in [7.5, 15)). They only read c_{g_n} at
lags u ∈ [2T′, 2T). That requires mass of g_n at both edges |x| ∈ (T′ − ε, T). The weight is v_n = 2Λ(n)n^{−½}: **Λ enters
exactly**, with no averaging.

Outside, the level-μ representative has c_N = −μ(N) on the block [μ, 2μ). Q2.1(c)'s comparison says that, between
levels, the data difference Ψ̌^{[μ]} − Ψ̌^{[μ/2]} = R_{M_μ − M_{μ/2}} is radical at level T′ and **not** at level T.
That is all the bridge contributes.

### 3.2 In the rough representative, the new exact Λ is radical (PROVED)

- **(a) At level μ.** The rough representative (Q2.1(4)) has no exact alignments with any contact n < μ (A.4(iv)).
  In particular, the new contacts p ∈ [μ/2, μ) act only through near-alignments.
- **(b) At level μ/2.** Exact alignments (N, pN), with p prime in [μ/2, μ) and N μ/2-rough, exist. But pN lies
  in the subcomb {p | ·}, which is **radical** at level T (Q2.1(3), Lemma R).
  - Its total pairing with any datum is 0 in 𝒲.
  - The count of exact alignments is, then, a piece of a P10-tautological partition. It is exactly cancelled by the
    rest (archimedean plus near-alignments) of the radical subcomb's pairing.
- **(c) Powers of old primes.** The new contacts that are not primes (8 = 2³ and 9 = 3² at μ = 15) have no
  exact alignment in any rough representative, because pN has a factor < μ/2.

**Conclusion:** on ℐ^{new} the exact Λ appears in only two ways, and neither is a signed count:
- in the window term −Σ_{[μ/2,μ)} v_n c_{g_n}(log n), which is a **bound to be proved**;
- in counts that lie inside the radical.

### 3.3 What fails in the identity for the falsifiers

This matches the spec and was checked against Lemma R:
- **cΛ, c < 1, and Beurling:** there is no Lemma R, so there is neither a radical nor a rough version.
- **DH:** the rule c_N = −μ(N) for the block [μ, 2μ) fails, because the truncated inverse is not multiplicative.
- **a_P and cΛ with c = 2:** pass all the identities of §1–§2, because they are generic.

That is why **all the discriminating content lies in the bound from 3.1, not in an identity.** That is the REF-D
pattern.

### 3.4 Do prime counts in intervals suffice? (NO-GO, restriction 1)

If positivity on ℐ^{new} were attempted via ψ(μ) − ψ(μ/2) ≥ cμ:
- the tool would be CITED: Bertrand–Chebyshev, or the explicit Rosser–Schoenfeld bounds (|ψ(x) − x| < εx with ε
  explicit);
- the precision needed is the scale of the margin, W ≍ κ·d₄(2πμ)‖·‖² ~ μ^{9/2}e^{−4πμ} relative to ‖g‖².

The step would be TV-robust. Erasing K primes from [μ/2, μ) changes ψ(μ) − ψ(μ/2) by O(K log μ), far below the slack of
Rosser–Schoenfeld (which is ≫ √μ). By contrast, the form changes by v_p c_{g*}(log p): per the sawtooth of PATTERN_001
(NUMERICAL), that is 8 to 15% of the margin per prime. A handful of erasures suffice to flip the sign of the margin,
while the counting bound stays the same.

**Conclusion: the counting bound cannot separate Λ from a_P at scale e^{−4πμ}.** NO-GO by restrictions 1 and 2
(HARD). The risk the spec flagged is confirmed. Bertrand is not "a problem": it is insufficient by a factor
e^{4πμ}.

---

## 4. C3′: closed formula for the pair count and check against Q2.1(b) at μ = 15

### 4.1 Formula

In the comb Ψ = Σ_N a_N N^{−½}τ_{log N}g, the pairing with contact p restricted to exact alignments N′ = pN is

 v_p·Σ_N a_N a_{pN}(N·pN)^{−½}·c_g(0) = (2 log p / p)·‖g‖²·Σ_N a_N a_{pN}/N.

In the μ/2-rough representative, with a ≡ 1 on the N > 1 that have P⁻(N) ≥ μ/2 (and pN is then also rough):

 **𝒞′_μ(X) = 2‖g‖²·(Σ_{p∈[μ/2,μ)} log p / p)·S_{μ/2}(X),  with S_Y(X) := Σ_{1<N≤X/p, P⁻(N)≥Y} 1/N.**

Mertens (CITED) gives two approximations:
- Σ_{p∈[μ/2,μ)} log p / p = log 2 + o(1);
- S_Y(X) ~ Π_{q<Y}(1 − 1/q)·log X ~ e^{−γ} log X / log Y.

Hence 𝒞′_μ(X) ~ 2 log 2·e^{−γ}·(log X / log(μ/2))·‖g‖². **The series diverges as X → ∞**, just like C3: it violates P2.
Truncated, it is of size O(‖g‖²), against a margin of order e^{−4πμ}‖g‖².

### 4.2 Check at μ = 15 (NUMERICAL, exact arithmetic)

- New primes in [7.5, 15): {11, 13}.
- Q2.1(b): the squarefree odd band in [7.5, 15) is {11, 13}, because 9 is not squarefree and 15 is
  excluded. Then c_{2M} = −[11 | M] − [13 | M].
  - **Exact coincidence of sets (PROVED):** the primes that emerge from the rough comb in the step 7.5 → 15 are
    exactly the divisors that activate c_{2M} in Q2.1(b).
  - For μ in general, Q2.1(b)'s band also contains the squarefree odd composites of [μ/2, μ); C3′
    only sees the primes.
- Values, with S_{7.5}(X) over N with P⁻(N) ≥ 11 and weight Σ_{p∈{11,13}} 2 log p / p = 0.8306:

| X | S_{7.5}(X) | 0.8306·S |
|---|---|---|
| 10³ | 1.1604 | 0.9638 |
| 10⁴ | 1.6872 | 1.4013 |
| 10⁵ | 2.2135 | 1.8385 |

- Growth per decade: 0.526. The Mertens prediction is Π_{q≤7}(1 − 1/q)·ln 10 = 0.2286·2.3026 = 0.526 ✓.
- Divergence confirmed.
- Consistency with Q2.1(b): the pairs (M, 2M) of contact 2 (an old contact) carry a nonzero coefficient only if 11 | M
  or 13 | M. That is, **old contact 2 only sees the datum through the new primes**. That is the "old" face of the same
  count, and Q2.1(2) proves that its total contribution is 0.

**C3′ label.**
- The formula is PROVED.
- As a source of sign it is NO-GO, for two reasons: it diverges (P2), and the count lies inside the radical (§3.2(b), P10).

---

## 5. Test at μ = 15: what C1 predicts for κ(30)/κ(15)

- **Prediction.** With θ₀ (B.1.c) and C1(ii) with θ, one would have κ(30)/κ(15) ≥ ½θθ₀ > 0, an absolute constant.
- **Data to compare with: none exists.** Certificates go up to μ = 15. Galerkin (Mori V, NUMERICAL) goes up to μ = 20. And
  μ = 30 is not computed: PATTERN_001 estimates N ≈ 769 for μ = 31 in the margin law, without running it.
- **Only pair (μ/2, μ) with data: (7, 14), in the band normalization** λ_min ≈ κ_band(1 − λ₄(2πμ)):
  κ_band(14)/κ_band(7) = 4.55/4.21 = **1.08** (NUMERICAL, Mori V).
  - Between 7 and 14, 5 contacts enter (8, 9, 11, 13, plus the edge at 7), each with an 8 to 15% drop. Their product,
    ≈ 0.85⁵ ≈ 0.44–0.66, is offset by the drift between contacts.
  - This is consistent with "θ constant." It also shows that the step's content is **the compensation of drift**:
    the quantity ρ_N − ρ_L from H_001, evaluated at the minimizer. This is the numerical confirmation of §2.3.
- **Passing from κ_band to κ(μ) = inf W/ℓ** requires K3.1 (κ₁ → 8/11) and the comparison ‖f‖ ↔ ‖g‖ (Lemma A 4.2). Both are
  O(1)-stable in μ: ARGUED.
  - κ_emp(15) ∈ [0.56, 1.09] (MORI15 §4). There is neither κ_emp(7.5) nor κ_emp(30).
  - The spec's pointwise prediction (ℓ_{T′} ≥ ℓ_T for the projection of g* onto core_{T′} at μ = 7.5) **is not computed**:
    Mori's matrices at μ = 7.5 are not among the audited ones.
- **Conclusion of the test.** The data are compatible with C1, and also with its negation in the form "θ → 0 slowly":
  they do not discriminate. C1 makes no prediction that the sawtooth data do not already contain.

---

## 6. Labels, restrictions, index entry, what remains

**Labels.**
- **B.1.a** (exact description of 𝒜_T ⊂ 𝒜_{T′}; discrepancy = T′ aliasing tail on the new window): **PROVED.**
- **B.1.b** (ℓ_T ≤ (√leak_λ + √C₂‖Ψ̌^{(T′)}‖_{(T′,T)})²): **PROVED.**
- **B.1.c** (β_μ ≥ θ₀ uniform): **CONDITIONAL** on B.1♭.
- **B.1** with constant 1: **OPEN.**
- Spec's exponential indication: **WITHDRAWN** (the support of 𝒜_T(g) is [−λ′, λ′]).
- **B.1♭** (τ_* < ∞, universal constant, μ-free and Λ-free): **OPEN.** Its obstruction, that Z is not bounded on L², is
  **PROVED**.
- **C1:** condition (iii) is free (**PROVED**). Prop. C1.1 (κ_new is sandwiched with κ(μ)) is **PROVED**, with
  the projection CONDITIONAL in infinite dimension. **C1 as a route: NO-GO**, for three reasons:
  - REF-D: (ii) is L′♯ at level μ up to constants;
  - it is the integrated 𝒦_H class (restriction 11);
  - the variant with prime counts in intervals falls by restrictions 1 and 2.
- **C3′:** the formula is **PROVED** and its check at μ = 15 is **NUMERICAL**. As a source of sign it is **NO-GO**
  (divergence P2 + radicality P10).

**New restrictions.**
- **R-C1.1.** Every inductive scheme in μ whose step is an infimum over the 𝒲-orthogonal complement (or any
  complement defined by W) is equivalent, up to absolute constants, to L′♯ at the new level. It is REF-D (Prop. C1.1).
- **R-C1.2.** In the rough representative, the exact Λ of the new contacts either does not align (level μ), or aligns
  within a radical subcomb (level μ/2). No exact pair count (N, pN) carries a sign.
- **R-C1.3.** Prime-in-interval bounds (Chebyshev, Bertrand, Rosser–Schoenfeld) cannot close a step
  μ/2 → μ: they are TV-robust at scale O(log μ) and the margin is e^{−4πμ}.
- **R-B.1.** Transporting ℓ between levels is a Λ-free prolate problem with an O(1) constant, not exponential. The
  only thing it needs is the boundedness of Z on (𝒢̄_1)^⊥.

**Index entry (README, Phase 200 section):**
> - **C1_DUPLICATION_001 (phase 200 r3; new reason vs L2_016: 𝒲-isometric transport A.5):** B.1.a/b
>   PROVED (𝒜_T(g) = 𝒜_{T′}(g) with the ring (1/λ,1/λ′) prescribed; cost = T′ aliasing tail on (T′,T)); β_μ ≥ θ₀
>   CONDITIONAL on B.1♭ (Z bounded on (𝒢̄_1)^⊥, μ-free and Λ-free; Z unbounded on L² PROVED); "ℓ_{T′}/ℓ_T exponential"
>   indication WITHDRAWN. C1: (iii) free; Prop C1.1 κ_new sandwiched with κ(μ) ⇒ (ii) = L′♯(μ) up to constants: **NO-GO (REF-D +
>   integrated 𝒦_H, restr. 11)**; count in short intervals NO-GO (restr. 1/2). C3′ formula PROVED (~2log2·e^{−γ}log X/log(μ/2),
>   diverges) and radical: NO-GO. μ=15: new primes {11,13} = Q2.1(b) band ✓. Do not retry induction in μ via W-orthogonal
>   complement nor count of pairs (N,pN). Row D OPEN.

**What remains OPEN and the next exact lemma.**
- L′♯: OPEN. Row D: OPEN.
- **Next exact lemma (tool, no sign): Lemma B.1♭.**
  - *Statement:* there exists C < ∞ such that, for every ϱ ∈ L²(1,∞) orthogonal to 𝒢̄_1 and in the closure of the admissible
    tails, ∫_1^{√2} |Σ_{n≥1} ϱ(nX)|² dX ≤ C‖ϱ‖².
  - *Route:* (𝒢̄_1)^⊥ = even tails whose cosine transform vanishes on [−1, 1] (with the two restrictions). One must prove
    that this spectral vanishing gives the ξ^s weight of DD_001 on dyadic average.
  - *Falsifier to test first:* carry the example from §1.4 (bumps at nX₀) into (𝒢̄_1)^⊥ with a bounded-norm projection.
- B.1♭ does not close L′♯. It only turns C1(i) into a reusable tool for any future argument comparing levels
  μ/2 and μ **without** going through the Schur complement.
