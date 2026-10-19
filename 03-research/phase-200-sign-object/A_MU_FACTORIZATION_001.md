# A_MU_FACTORIZATION_001 — Round 4 of phase 200: the factorization operator A_μ in the leak quotient

Phase 200 ("sign object"), pen and paper.

Written only in this file; the index entry goes in §6 so the coordinator can copy it.

**Assignment (AUDIT_200_SPEC_003 §7.2).** Give, by formula, before knowing the sign of 𝒲, an operator A_μ: 𝒬_μ → ℋ
built with (ℕ,+,·) and an exact identity 𝒲(r) = ‖A_μ r‖² − ℰ_μ(r) with ℰ_μ ≥ 0 explicit. The operator must stop
existing, or ℰ_μ must stop being ≥ 0, for a_P, for cΛ with c = 2, and for Beurling/DH. Per R-Q6, the test is applied at the
descent.

**One-line result.** None of the five requested families (a)–(e) gives an admissible factorization: (a) and (d) are
NO-GO by F4 + P4, (b) is C8/thm:shape, (c) is NO-GO by Lemma R, and (e) is the already-recorded SQ. The new family (f) is the
**semi-annular derivative**. Its exact identity (PROVED) writes the outer prime term as the derivative, at ε = 0,
of the norm ‖Z^{(ε)}r‖² of the deformed comb n ↦ n^{ε}. Thus, the + / · coupling (log(nξ) = log n + log ξ) becomes
the sole source of primes. From that identity comes a factorization 𝒲 = ‖A_ε r‖² − ℰ_ε, with ℰ_ε = ‖Z^{(ε)}r‖²/ε, **as
soon as the function F(ε) = ‖Z^{(ε)}r‖² is convex in ε**. Convexity is the new, exact unknown (Lemma F, OPEN). Its
analogue on the full line is the convexity of three lines (CITED). On the full line, however, it is symmetric under the
functional equation and gives the null symbol (REF-D). The content thus lives in the truncation (T,∞). Beurling does
**not** die in the formula, only at the descent, so filter P10 holds only halfway. L′♯ OPEN. Row D OPEN.

---

## 0. Corpus and index check; why this is not a retry

- **Read:** AUDIT_200_SPEC_003 §6–7 (R-Q6, "what to change"); SPEC_002 (T.1, T.2, T.3, SQ.0–SQ.1, Q1 §5: predicted death of
  SQ); Q2_LADDER_001 (Lemma R; 𝔊_{YY′} ≡ W_T(g); W_T(g) = 𝒲[0/1 μ-rough comb]); MORI15_EXTREMAL_001 §1–2; Paper 47 §22
  (thm:ext-half, rem:ext-killing, prop:ext-gauge, prob:ext-L, prop:ext-consol, prop:ext-grouped, prop:ext-latred).
- **Index:** searched for "factoriz", "SOS", "square", "Cholesky", "Schur", "Fejér", "Z_log", "log ξ", "n^ε", "three lines",
  "Doetsch", and "Hardy convex".
  - Relevant hits: l.40 (SOS/dual certificates = D, pure arithmetic of squares empty); l.50 (Schur/pencil/inertia, walls
    W-lin… W-mom); l.249 (no Schur factorization via product kernels); l.255 (G0: squares = Gram → REF-D or
    certificate); l.294 (Grothendieck/SDP/Lasserre = G0/thm:sos); l.452 (A_001, half-line identity); l.455 (E_001,
    pairs (m,n)); l.390 (INV_C, normalized Möbius ζ(2σ)^{−1}∫|ζ(σ+it)|²); phase 183 (Sonin/Gram); GRAM_INERTIA_001.
  - **No entry** writes the Z_log term of thm:ext-half as the derivative of a norm along the deformation
    n ↦ n^{ε}, nor poses convexity in ε of the truncated comb.
- **New reason stated for (f) relative to G0/l.255 and C8.**
  - (i) It is not SOS in a fixed basis. The square ‖Z^{(ε)}r‖² is formed with the n^{ε}-coefficient comb, whose existence
    as an identity for 𝒲 requires Λ*1 = log (rem:ext-killing(ii)). For cΛ or a_P the prime term is not a derivative.
  - (ii) The missing inequality is not a Gram/inertia problem. It is a one-dimensional convexity in an external
    parameter ε, of the Hadamard–Doetsch three-lines family, which does not appear in the index.
  - (iii) INV_C uses the normalization |ζ(σ+it)|² with σ varying only to read weights; it does not differentiate in σ.

---

## 1. Inventory of factorizations in 𝒬_μ

Notation as in SPEC_002. r ∈ L²(λ,∞), Ψ̌ = (Zr)(e^·)1_{(T,∞)} with (Zr)(e^y) = e^{y/2}Σ_n r(ne^y), and likewise
Z_log with weights log n. 𝒜[Ψ] = (1/2π)∫m|Ψ̂|² is the archimedean part, and by thm:ext-half
 𝒲(r) = 𝒜[Ψ̌] + 2A(Ψ̌)B(Ψ̌) − 2⟨Ψ̌, (Z_log r)(e^·)⟩_{L²(T,∞)}.   (1.0)

### (a) Fejér–Riesz / spectral factorization of the symbol — NO-GO (PROVED, given F4)

- **Formula.** By T.1, 𝒲 = (1/2π)∫|ĝ|²|D_μ|²σ with σ(t) = m(t) − Σv_n cos(t log n). Factoring σ = |h|² with h in H²
  would make A_μ multiplication by h·D_μ.
- **Obstruction.** By F4, m(t) + 2Re(ζ′/ζ)(½+it) = 0 away from the ordinates, so σ ≡ 0 as a function. The exact form is
  as follows. With Ξ = Γ_ℝζ, σ(t) = 2Re(Ξ′/Ξ)(½+it) = ∂_σ log|Ξ(σ+it)|²|_{σ=½}, and |Ξ(σ+it)| = |Ξ(1−σ+it)| by the
  functional equation. The derivative vanishes by symmetry.
- **Consequence.** As a function, σ does not factor. As a distribution it lives on the ordinates, and that is REF-D by P4.
- **Useful reading, which reappears in (f).** The symbol is a derivative in the transversal direction σ, and it vanishes by the
  reflection σ ↔ 1−σ. Any factorization must break that symmetry. The only thing breaking it in the problem is the
  truncation (T,∞) of the outer part.

### (b) Cholesky of the grouped matrix (prop:ext-grouped / prop:ext-latred) — NO-GO as a sign object (C8)

- **Formula.** 𝒲 = vᵀGv, with G the Gram matrix of 𝒲 on {Υ_m} ∪ {Υ_0} and v = (μ(m)) ⊕ 1. G is not PSD: it is the Weil form
  on arbitrary outer vectors, and contains negative directions (prop:ext-latred gives no sign; GRAM_INERTIA_001: mixed
  inertia). An LDLᵀ with D of mixed sign gives 𝒲 = Σd_i⁺(…)² − Σd_j⁻(…)². That is the "cancelling basis" C8: the basis Υ_m is
  fixed and depends on Λ only through 𝒲.
- **Why it is not admissible.** The sign would run through v ∈ positive cone of G, which is REF-D (l.255 G0). Moreover thm:shape
  (L3 F1) excludes the decomposition into squares for T ≥ ½log3.
- **Λ.** G depends on Λ only through the form; v is pure Möbius. The construction exists just the same for a_P and c = 2 (with
  another G), so **it does not pass P10**.

### (c) Multiplicative operators on the rough comb — NO-GO (PROVED, given Guo L4.4)

- **Formula.** By Q2_LADDER, W_T(g) = 𝒲[Σ_{N>1, P⁻(N)≥μ}N^{−½}τ_{log N}g]. Candidates: A r := ×n (subcomb p | N), or
  "N ↦ N/rad_μ(N)" (divide by the μ-smooth part).
- **Lemma C.1 (PROVED, given Guo L4.4).** Let 𝔇 be the algebra generated by the translation operators τ_{log d}, d ∈ ℕ, on
  combs of the form ζP(∂)g. Every element of 𝔇 applied to a radical comb gives a radical comb. Hence, for
  K ∈ 𝔇, 𝒲(K Ψ̌) depends on KΨ̌ only modulo the image of 𝔇 on Z_g.
  *Proof.* Lemma R, step 3: translation invariance preserves the radical. □
- **Consequence.** The operator "divide by the μ-smooth part" acts on the rough comb as the identity (every N with
  P⁻(N) ≥ μ has μ-smooth part 1). Any subcomb p | N lies in 𝔇·Z_g + (finite comb); its 𝒲 reduces to a finite comb
  (Q2: 𝔊 constant).
- **Verdict.** A norm ‖K·‖² with K ∈ 𝔇 in L² is unrelated to the radical. A multiplicative A_μ gives at most an arbitrary
  ‖K r‖² with no exact relation to 𝒲. For an identity to exist, ℰ_μ would have to contain the whole of 𝒲. **NO-GO**
  as a factorization. The operator rad_μ is trivial on the rough comb.

### (d) A_μ = 1 − ζM_μ(∂) ("truncated Möbius") — NO-GO (PROVED with T.1)

- **Exact formula.** By T.1(a), 𝓕Ψ̌_c = ĝ·D_μ(½+it) with D_μ = ζM_μ − 1. Let A_μ := multiplication by D_μ, so that
  A_μ g = Ψ̌_c. The question was whether 𝒲 = ‖(1 − ζM_μ)g‖²_ℋ − ℰ for some ℋ.
- **Identity.** With any weight w ≥ 0, ‖A_μ g‖²_w = (1/2π)∫|ĝ|²|D_μ|²w. T.1(c) gives 𝒲 = (1/2π)∫|ĝ|²|D_μ|²σ. Hence
  ℰ = (1/2π)∫|ĝ|²|D_μ|²(w − σ), and one needs w ≥ σ in the distributional sense.
- **Obstruction.** By (a), σ = 0 away from the ordinates and σ is a positive measure on the ordinates only in the reading of
  the zeros (rem:ext-killing(iii)). Moreover D_μ(ρ) = −1 at each zero (SPEC_002 §A.2). The choice of w remains free away from
  the ordinates, and ℰ ≥ 0 amounts to w ≥ (mass at zeros), which is REF-D.
- **Λ.** A_μ = D_μ is pure Möbius and exists for every falsifier. **Does not pass P10.**

### (e) Selberg operator A_μ r := (√φ(k)·y_k(r))_k — already recorded (SQ, SPEC_002 Q1); NO-GO expected by P2

- **Formula.** S_1(1) = Σ_k φ(k)y_k² is an exact square (T.3, Selberg CITED). The question is what 𝒲 − θS_1 is.
- **Identity (PROVED, SQ.0).** 𝒲 = yᵀ𝔅(g)y with 𝔅_{kk′} = 𝒲(F_k, F_{k′}), F_k finite. Then
  𝒲 − Σφ(k)y_k²β_k = −ℛ, with ℛ = 𝒫 − yᵀ𝔅y.
- **Sign.** ℛ has no sign. At μ = 15, 𝒫(g*) ≈ 0.43·O(1) and 𝒲 = 4.76·10⁻⁷⁰, so ℛ cancels 𝒫 to 70 digits
  (death prediction SPEC_002 Q1 §5).
- **Λ.** y_k is pure Möbius. The dependence on Λ lies in 𝔅 via SQ.0 (radicality of Z_g), i.e. at the descent, as
  R-Q6 requires. That is a correct hit, but the output is a bound with ℰ = ℛ of size O(1), not a factorization: P2.
- **Verdict.** Duplicate of SQ (SPEC_002). Not reopened.

### Inventory table

| family | exact identity | ℰ ≥ 0 | depends on Λ | verdict |
|---|---|---|---|---|
| (a) spectral | yes (T.1) | only with mass at zeros | yes | NO-GO (F4 + P4) |
| (b) Cholesky | yes (latred) | no (mixed inertia) | only in G | C8, thm:shape |
| (c) ×n, rad_μ | trivial | — | no | NO-GO (Lemma R) |
| (d) 1 − ζM_μ | yes | ⟺ mass at zeros | no | NO-GO (REF-D, P10) |
| (e) Selberg | yes (SQ.0) | no, ℛ = O(1) | at the descent | duplicate SQ, P2 |
| **(f) semi-annular derivative** | **yes** | **⟸ Lemma F (OPEN)** | **yes (Λ*1 = log)** | **candidate** |

---

## 2. The strongest candidate: the semi-annular derivative

### 2.1 Definition (given before knowing the sign)

For ε ∈ ℝ and r ∈ L²(λ,∞) with r = O(ξ^{−2}), define the **deformed comb**
 (Z^{(ε)}r)(e^y) := e^{y/2}Σ_{n≥1} n^{ε} r(ne^y),  y > T,
and F_r(ε) := ‖Z^{(ε)}r‖²_{L²(T,∞)}. For |ε| < ½ the series converges absolutely and uniformly for y > T, because
|r(ne^y)| ≲ n^{−2}e^{−2y}. Hence F_r is real-analytic on (−½, ½) (PROVED).

**Semi-annular reading.** n^{ε} = e^{ε log n} is the character of the monoid (ℕ,·) that turns a product into a sum. In the
variable ξ = ne^y, the identity log ξ = log n + y holds, and therefore
 Z^{(ε)}r = e^{−εy}·Z(ξ^{ε}r).   (2.1)
The deformation ε mixes the multiplicative structure (the index n) with the additive one (the translation y). This is the
+ / · interaction in the most literal sense possible.

### 2.2 Theorem D (semi-annular derivative identity; PROVED given thm:ext-half)

For r = 𝓕f|_{(λ,∞)} with f admissible at T,
 𝒲(r) = 𝒜[Ψ̌] + 2A(Ψ̌)B(Ψ̌) − F_r′(0),   Ψ̌ = Z^{(0)}r.   (2.2)
Moreover, by (2.1),
 −F_r′(0) = 2∫_T^∞ y|Ψ̌(y)|²dy − 2⟨Ψ̌, Z(log ξ·r)⟩.   (2.3)

*Proof.*
1. ∂_εZ^{(ε)}r|_{ε=0} = e^{y/2}Σ log n·r(ne^y) = Z_log r. Differentiation under the sum is justified by the uniform
   convergence of Σ n^{ε}log n·|r(ne^y)|.
2. Then F_r′(0) = 2⟨Z^{(0)}r, Z_log r⟩. Substituting in (1.0) gives (2.2).
3. For (2.3), differentiate (2.1): ∂_ε[e^{−εy}Z(ξ^{ε}r)] = −yZr + Z(log ξ·r) at ε = 0. □

**Where Λ enters (exact).** Before thm:ext-half, the prime term is −Σ v_n c_Ψ(log n). rem:ext-killing(ii) turns it
into Z_log via Λ*1 = log. That is the only place where Λ appears, and (2.2) rewrites it as a derivative. Theorem D is,
therefore, "Λ*1 = log ⟺ the prime term is ∂_ε of a norm."

### 2.3 Conditional factorization

**Lemma F (OPEN).** For every r in the image of the f admissible at T, F_r is convex on [0, ε₀] for some ε₀ = ε₀(μ) > 0.

**Corollary F (CONDITIONAL on Lemma F).** If F_r is convex on [0, ε], then F_r′(0) ≤ (F_r(ε) − F_r(0))/ε, and
 𝒲(r) = ‖A_ε r‖² − ℰ_ε(r) + Δ_ε(r),
with
- ‖A_ε r‖² := 𝒜[Ψ̌] + 2AB + ε^{−1}‖Ψ̌‖²,
- ℰ_ε(r) := ε^{−1}‖Z^{(ε)}r‖² ≥ 0 (explicit, a square),
- Δ_ε(r) := ε^{−1}(F_r(ε) − F_r(0)) − F_r′(0) ≥ 0, the convexity remainder, which vanishes to order ε.

Then 𝒲 ≥ ‖A_ε r‖² − ℰ_ε(r).

*On the form A_ε.* ‖A_ε r‖² is indeed a square for small ε. 𝒜 is bounded below by
m(0)‖Ψ̌‖² = −5.372‖Ψ̌‖² (m is even and increasing for t > 0, SPEC_002 PROVED). The pole has rank one. For ε < 1/5.372, the sum
𝒜 + ε^{−1}‖·‖² is PSD except for the polar term, and in the class A(g) = 0 the polar term vanishes (T.1(b)). Thus A_ε is the
square root of a positive Fourier operator given by formula: A_ε = 𝓕^{−1}(m + ε^{−1})^{½}𝓕 ∘ Z on the quotient (PROVED in the
class A = 0, for ε < 0.186).

**What the corollary says.** The sign of 𝒲 reduces to the comparison between two L² norms of combs on (T,∞): the
undeformed one and the n^{ε}-deformed one, plus the archimedean part. It is the same comparison made by Q2's "0/1
μ-rough comb," now with weights n^{ε}. The condition L′♯ takes the form
 ε^{−1}‖Z^{(ε)}r‖² − Δ_ε ≤ 𝒜[Ψ̌] + ε^{−1}‖Ψ̌‖² − κμ^{−A}ℓ(r).   (2.4)

### 2.4 Why Lemma F is the right unknown, and its status

- **F″.** F_r″(ε) = 2‖∂_εZ^{(ε)}r‖² + 2⟨Z^{(ε)}r, ∂_ε²Z^{(ε)}r⟩, with ∂_ε² ↔ weights (log n)². The first term is ≥ 0. The
  second has no sign. F″ ≥ 0 ⟺ the "logarithmic variance" of the comb dominates the cross-covariance. This is an
  inequality on the weights (log n)^j n^{ε}, in which Λ no longer appears: Λ was absorbed into the derivative. **Λ-free
  problem**, of the B.1 type (AUDIT_200 §7.2).
- **Analogue on the full line (CITED + PROVED).** If the cutoff (T,∞) is replaced by ℝ, Plancherel-Mellin gives
  F_r(ε) = (1/2π)∫|ζ(½ − ε + it)|²|R(t)|²dt, with R independent of ε. For G = ζ·ρ with ρ entire, log∫|G(σ+it)|²dt is
  convex in σ (Hadamard–Doetsch three-lines convexity for mean squares on strips, CITED; growth control outside the
  line 1 is needed, which ζ provides on bounded strips). **But:** when 𝒜 is added, the sum 𝒜 + (prime term) is exactly
  ∂_σ∫|Ξ(σ+it)|²w, and the symmetry |Ξ(σ)| = |Ξ(1−σ)| annihilates it (§1(a)). On the full line, the
  convexity exists and is useless: it produces the null symbol, and all the mass reverts to the ordinates (REF-D).
- **Structural conclusion (ARGUED).** If Lemma F carries content, that content is the defect of the symmetry
  σ ↔ 1−σ created by the cutoff at T. That is exactly the object thm:ext-half isolates, with the killing term κ(y) of
  rem:ext-killing(i), and there is no other. Lemma F is the "three lines on the half-line" version of prob:ext-L. It is not a
  proof: it is the translation into a single one-dimensional convexity.
- **Possible obstruction (OPEN, unverified).** F_r(ε) ≈ ∫|Σn^{ε}h_n|² with h_n ≥ 0 not guaranteed. If r changes sign, as
  at Mori's self-dual extremal, F″(0) could be negative. Lemma F must first be checked at g* (§3).

### 2.5 Falsifier test (at the formula and at the descent, R-Q6)

| falsifier | does formula (2.2) exist? | does the descent exist? | status |
|---|---|---|---|
| a_P (primes P erased) | **no**: Λ_P*1 = log − (contribution from P), and the prime term is ∂_ε‖Z^{(ε)}‖² − (correction at P), which is not a derivative | no (radical Z^P) | dies in both (PROVED: Λ_P*1(P) = 0 ≠ log P) |
| cΛ, c = 2 | yes, formally: the term is −2F′(0) = ∂_ε at twice the speed (2Λ*1 = 2log) | **no** (thm:ext-half uses Λ*1 = log so that the radical comb is Z; with c = 2 the radical is not Z_g) | dies only at the descent |
| Beurling (ℕ_B, Λ_B) | **yes**: Λ_B*1 = log holds in every Beurling system, and n^{ε} is defined | **no** (Poisson over ℕ, Guo L4.4) | **dies only at the descent** |
| DH | yes (Λ_DH*1 = log formally for its series) | no (radical = DH image) | dies only at the descent |

**Verdict P10: PARTIAL.** Formula (2.2) kills a_P by itself. For c = 2, Beurling, and DH, the death occurs only at the
descent, as R-Q6 predicted for any construction using (1.0). The target asked that the construction "stop existing in
the formula" for c = 2 and Beurling. **It does not.** The reason is structural: (1.0) already incorporates Λ*1 = log, and any
operator built on (1.0) inherits the only dependence on Λ that (1.0) retains. I record this as a new restriction R-F1 (§5).

---

## 3. Test at μ = 15

**Available data.** MORI15_EXTREMAL_001_data/p0_prolate_M28.json contains the outer datum of the even extremal: f* in the
prolate basis at c = 30π, with gauge M = 28. MORI15 gives W* = 4.763·10⁻⁷⁰, pieces in window coordinates Γ_ℝ −5.3722, Lévy +3.9164,
pole +1.5190, primes −0.0632, and ℓ ≈ (4.4–8.5)·10⁻⁷⁰.

**No new numerical computation was run.** The requested directory phase-199/proof-L-sharp/{data,scripts} does not exist; the
data are in MORI15_EXTREMAL_001_data with scripts at the root of proof-L-sharp. Evaluating F_{r*}(ε) requires reconstructing
r* = 𝓕f* outside the band to 70 digits of cancellation and summing the comb Z^{(ε)} on (T,∞). It is a computation of the same
class as EXTERIOR_DATUM_001 and does not fit in this round without risking numerical floor effects. Test label: **OPEN (not NUMERICAL)**.

**Exact predictions (PROVED except where noted) for whoever runs it.**
1. By (2.2), 𝒜[Ψ̌*] + 2AB − F′(0) = W* = 4.763·10⁻⁷⁰. In the outer part, the pieces do not match the window ones (the
   translation from thm:ext-half redistributes them). The magnitudes are O(‖Ψ̌*‖²), and ‖Ψ̌*‖² is of the order of the leak:
   ‖Ψ̌*‖² ≲ C·ℓ* (lem:ext-mob plus Cauchy–Schwarz on the comb, ARGUED).
2. **Life-or-death prediction (P2 applied to (f)).** With ε ≍ 1/|m(0)| ≈ 0.19, ‖A_ε r*‖² and ℰ_ε(r*) are both
   ≍ ε^{−1}‖Ψ̌*‖² ≍ ℓ*. **(f) does not violate P2 at the outset**, unlike (e): its pieces live at the scale of the leak, not at
   O(1), because they are built in the outer region and not in the window. This is the only candidate in the inventory with
   that property.
3. The decisive test is the sign of Δ_ε(r*) = ε^{−1}(F(ε) − F(0)) − F′(0), equivalently that of F″ on [0, ε]. If
   F″_{r*}(0) < 0, Lemma F is false at the extremal and (f) dies as a factorization (only identity D would survive). If
   F″_{r*} > 0 with margin ≍ ℓ*, Lemma F is the next lemma.
4. The ventana's prime piece −0.0632 is O(1) and cancels to 70 digits. In the outer part, the term F′(0) groups all the
   (m, n) alignments of E_001. Prediction (ARGUED): F′(0) is dominated by n ∈ {1, 2}, consistent with the resonance
   (1, 2) in AUDIT_16 §6 (−0.481 W*). Then F″(0) ≈ 2(log 2)²‖h_2‖² + 2(log 2)²⟨h_1, h_2⟩ + …, and its sign depends on
   ⟨h_1, h_2⟩, with h_n(y) = e^{y/2}r*(ne^y). This is the concrete quantity to compute first.
5. Control arithmetic data (exact, SPEC_002): y_k, S_1 = 0.432234, S_2 = S_4 = 0.154645. These do not enter (f): (f) does not use
   the Selberg basis. This is consistent with R-Q6.

---

## 4. Labels

| statement | label |
|---|---|
| §1(a): σ = ∂_σlog|Ξ|² at σ = ½, null by FE; Fejér–Riesz impossible | PROVED (given F4) / NO-GO |
| §1(b): Cholesky of latred = C8 | NO-GO (by thm:shape + G0) |
| Lemma C.1 and (c) | PROVED (given Guo L4.4) / NO-GO |
| §1(d): A_μ = D_μ ⇒ ℰ ≥ 0 ⟺ mass at zeros | PROVED / NO-GO (REF-D, fails P10) |
| §1(e) | duplicate of SQ, unchanged |
| Analyticity of F_r on (−½, ½) | PROVED |
| Theorem D (2.2)–(2.3) | PROVED (given thm:ext-half) |
| A_ε PSD in the class A = 0 for ε < 1/5.372 | PROVED |
| Corollary F | CONDITIONAL on Lemma F |
| Lemma F | OPEN |
| §2.4: content of F = symmetry defect from the cutoff | ARGUED |
| Falsifier table §2.5 | PROVED for a_P; c = 2, Beurling, and DH die only at the descent |
| Test μ = 15 | OPEN (not run) |
| L′♯ | OPEN |
| Row D | OPEN |

---

## 5. New restriction

**R-F1 (PROVED, one line).** Every factorization 𝒲 = ‖A r‖² − ℰ built on the outer form (1.0) depends on Λ only
through Λ*1 = log. Beurling and DH satisfy Λ*1 = log, and for cΛ the identity (1.0) does not exist but its formal analogue
does. Consequently, no A_μ built on (1.0) can "stop existing in the formula" for Beurling. This requirement of the target
can only be satisfied with operators using the descent itself: the radical via Poisson over ℕ, i.e., the additive
character e(jN/k) together with the multiplicative structure.
- *Proof.* rem:ext-killing(ii) plus the observation that Λ_B*1_B = log in every Beurling system (definition of Λ_B). □
- *Consequence for the target:* requirement P10 must be split into two. (P10-formula) kills a_P, and it is achievable (theorem
  D satisfies it). (P10-descent) kills c = 2, Beurling, and DH, and only an A_μ using Poisson over ℕ satisfies it. The
  only piece of the corpus that does this is SQ.0 / Lemma R, which so far has only given radicals: linear identities, never norms.

**R-F2 (PROVED).** On the full line, every factorization of the symbol by convexity in the transversal variable σ (three
lines, Fejér–Riesz, Hardy) is annihilated by the functional equation. Its nontrivial content is confined to the cutoff at T.
- *Proof.* §1(a). □

---

## 6. Index entry (copy into ROUTES-TRIED-INDEX/README, phase 200)

- **A_MU_FACTORIZATION_001 (phase 200, round 4; factorization operator A_μ in 𝒬_μ = prob:ext-L):**
  - Inventory: (a) Fejér–Riesz of the symbol NO-GO, because σ = ∂_σlog|Ξ|²|_{½} is null by FE (F4 + P4). (b) Cholesky of
    latred = C8/thm:shape. (c) ×n and rad_μ on the rough comb NO-GO by Lemma R (translation algebra preserves the
    radical; rad_μ = id on rough numbers). (d) A_μ = 1 − ζM_μ: ℰ ≥ 0 ⟺ mass at zeros (REF-D) and fails P10. (e) Selberg = SQ
    duplicate (P2).
  - New: **Theorem D (PROVED given thm:ext-half)**: 𝒲 = 𝒜[Zr] + 2AB − ∂_ε‖Z^{(ε)}r‖²_{(T,∞)}|_0, with deformed comb
    n ↦ n^{ε}. Equivalent: Z_log = Z(log ξ·) − y·Z. Corollary F (CONDITIONAL on **Lemma F**, convexity of ε ↦ ‖Z^{(ε)}r‖²
    on [0, ε₀], OPEN, Λ-free): 𝒲 ≥ ‖A_εr‖² − ε^{−1}‖Z^{(ε)}r‖², with A_ε = (m + ε^{−1})^{½}(∂)∘Z, PSD for ε < 0.186 at A = 0.
  - Partial P10: a_P dies in the formula; c = 2, Beurling, and DH only at the descent.
  - New restrictions: R-F1 (every A built on the outer form sees Λ only via Λ*1 = log, so it does not kill Beurling in the
    formula) and R-F2 (transversal convexity on the full line annihilated by FE; content only in the T cutoff).
  - Test μ = 15 not run. Decisive quantity: sign of F″_{r*}(0), dominated by ⟨h_1, h_2⟩.
  - Do not retry: (a)–(e) as factorizations. (f) only survives via Lemma F.

---

## 7. Next exact lemma

**Lemma F₀ (the minimal test; OPEN).** For r* = outer datum of Mori's extremal at μ = 15 (p0_prolate_M28.json), compute
with ≥ 90 digits
 F″_{r*}(0) = 2‖Z_log r*‖²_{(T,∞)} + 2⟨Zr*, Z_{log²}r*⟩_{(T,∞)}
and compare it with ℓ*.
- If F″ < 0: (f) dies as a factorization (theorem D remains as an identity) and it is recorded NO-GO.
- If F″ ≥ c·ℓ*: state Lemma F in the class of r with A = 0 as a Λ-free inequality between the logarithmic moments
  M_j(r) := ⟨Z_{log^j}r, Z r⟩, in particular M_1² ≤ ‖Zr‖²·(M_2 + ‖Z_log r‖²)·(1 + o(1)). Attack it as a prolate problem of the
  B.1 type.

Parallel theoretical lemma (OPEN): **three-lines convexity on the half-line.** For Φ with support on (T,∞) and decay
e^{−3y/2}, ε ↦ log∫_T^∞|e^{−εy}Φ_ε(y)|²dy is convex, with Φ_ε = Z(ξ^{ε}r). The defect relative to the full-line case
must be bounded by the killing term κ(y) of rem:ext-killing(i).

L′♯ OPEN. Row D OPEN.

---

## Summary (≤300 words)

Inventory of factorizations 𝒲 = ‖A_μ r‖² − ℰ_μ in the leak quotient (prob:ext-L):
- **(a)** Fejér–Riesz: NO-GO. The symbol is σ = ∂_σlog|Ξ(σ+it)|² at σ = ½, which is null by the functional equation. There is
  only mass at zeros (REF-D).
- **(b)** Cholesky of latred: class C8/thm:shape.
- **(c)** ×n and rad_μ: NO-GO by Lemma R (the translation algebra preserves the radical; rad_μ is the identity on rough numbers).
- **(d)** A_μ = 1 − ζM_μ: exact by T.1, but ℰ ≥ 0 ⟺ mass at zeros, and it does not distinguish falsifiers.
- **(e)** Selberg: duplicate of SQ, violates P2.

**New candidate (f), "semi-annular derivative."** Theorem D (PROVED given thm:ext-half):
𝒲 = 𝒜[Zr] + 2AB − ∂_ε‖Z^{(ε)}r‖²_{(T,∞)}|_{ε=0}, with the deformed comb n ↦ n^{ε}. The prime term is exactly the
derivative of a norm along the character (ℕ,·) → (ℝ,+), via log(nξ) = log n + log ξ. If ε ↦ ‖Z^{(ε)}r‖² is convex
(**Lemma F, OPEN, Λ-free**), then 𝒲 ≥ ‖A_εr‖² − ε^{−1}‖Z^{(ε)}r‖², with A_ε = (m + ε^{−1})^{½}(∂)∘Z PSD (ε < 0.186, A = 0).
It is the only candidate whose pieces live at the scale of the leak and not at O(1).

**Limitations.**
- On the full line, three-lines convexity exists but the functional equation annihilates it (R-F2): the content lies in
  the T cutoff.
- P10 is partial: a_P dies in the formula; c = 2, Beurling, and DH only at the descent.
- New restriction R-F1: every A_μ built on the outer form sees Λ only via Λ*1 = log, so it cannot kill
  Beurling in the formula. The target must split P10 into formula and descent.

**Test μ = 15:** not run (OPEN). The decisive quantity is the sign of F″_{r*}(0), dominated by ⟨h_1, h_2⟩.

**Next lemma:** F₀, computing F″_{r*}(0) against ℓ* with MORI15's outer datum.

L′♯ OPEN. Row D OPEN.
