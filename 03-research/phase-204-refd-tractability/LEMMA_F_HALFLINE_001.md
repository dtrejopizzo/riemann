# LEMMA_F_HALFLINE_001 — Lemma F on the half-line as a statement in its own right (phase 204g, route 3 of TRACT_001)

The only numerical check is T10.1,
run on the existing F0_TEST pipeline (NUMERICAL). Scripts and outputs in `LEMMA_F_HALFLINE_001_data/`.

## Summary (≤ 250 words)
Lemma F is treated, without Λ, as a statement about r ∈ L²(λ,∞): F_r(ε) = ‖Z^{(ε)}r‖²_{(T,∞)} is convex near 0.

**Structure (PROVED).** F_r(ε) = ∫e^{εt}dν_r(t). Here ν_r = Σ_{m,n}K_r(m,n)δ_{log mn} is a signed measure, and
K_r(m,n) = ⟨h_m,h_n⟩_{(T,∞)}. At ε = 0, F″ is the second moment of ν_r. The kernel [(log m + log n)²] has signature
(2,1), so the Schur argument gives nothing.

**Theorem F⁻ (NO-GO as a standalone theorem, PROVED).** Take ρ = φ + cφ(·/2), with φ a bump at ω₀ ∈ (1.2, 1.45) and
c ∈ (−½, 0). For that family, F″(0) = 2λ‖φ‖²(log 2)²c(1+2c) < 0 holds exactly. There are infinite-dimensional
subspaces where F″(0) is negative definite. That is why the lemma also fails, ARGUED, among minimal-leak
representatives and in the Paley–Wiener class.

**T10.1 (NUMERICAL).** The formula is confirmed to 16 digits. On 12 even Paley–Wiener modes, the 12 random
combinations give F″/ℓ ∈ [0.066, 0.46], all positive. The minimal direction, by contrast, gives F″/ℓ = −0.0054,
stable across X = 60…240: there is an explicit Paley–Wiener counterexample.

**Cones where it holds (PROVED).**
- If K_r ≥ 0 entrywise, or if ρ ≥ 0, then F_r is log-convex over the whole convergence interval. It is a Laplace
  transform of a positive measure.
- On the cone ρ ≥ 0, the three Hadamard lines give the same thing.
- Mori's r* is in neither cone (⟨h₁,h₂⟩ = −1.32).

**The bound 𝒲 ≥ 𝒜 + 2AB − (F(ε)−F(0))/ε.** As an inequality it is correct, but it is CONDITIONAL on the convexity
*of that specific r*. At r* it is NUMERICAL and contributes nothing about 𝒲(r*), which Theorem D already gives
exactly. It also does not control the infimum over r. **It is not an input for D.** Route 3: NO-GO as a uniform
theorem; PROVED on the cones.

---

## 0. Corpus and index

**Index search.** grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` for: "Lemma F", "logarithmic moments", "F″",
"F0_TEST", "A_MU", "convex", "three lines", "Stein", "interpolation", "log-convex", "Hadamard three lines". Findings:
- README l.521 (A_MU (f)): Lemma F OPEN, without Λ.
- l.523 (AUDIT_AMU): (f) is NO-GO as a factorization. It notes that "convexity is not automatic (requires
  ⟨h_m,h_n⟩ ≥ 0)."
- l.532 (F0_TEST): F″(r*) = +18.3·10⁻⁷⁰; the lemma remains OPEN.
- l.553: the log-convexity of λ_A is FALSIFIED (R186_033). It is a different object, the function of T, not of ε.
- l.593 (TRACT_001): route 3 = T10.1/T10.2.
- 04_PHASES l.136 (R186-PNTcone): log-convexity of λ_A, FALSE. It is a different variable.

**Why this is not a retry.** No entry proves or disproves Lemma F *as a universal statement in r*. AUDIT_AMU left
convexity as "not automatic" without giving a counterexample. F0_TEST tested a single vector. This memo does what
TRACT_001 §6.3 asked for: a cheap falsification (T10.1) and the identification of the class where it holds (T10.2).

**Sources read.** TRACT_001 §R10 and §6.3; A_MU_FACTORIZATION_001 §2 (def. (2.1), F″, "possible obstruction");
AUDIT_200_AMU_001; F0_TEST_001 and `step3_F.py`, `step4_diag.py`.

## 1. Exact definition
Using the conventions of A_MU §2 and F0_TEST (`step3_F.py`), λ = √15, T = ½log15, ρ(ω) := r(λω) for ω > 1, and
variable s = e^{y−T} ∈ [1, ∞). Then:

  (Z^{(ε)}r)(y) = e^{y/2} Σ_{n≥1} n^{ε} r(n e^{y}),  y > T;
  F_r(ε) = λ ∫_1^∞ S_ε(s)² ds,  with S_ε(s) := Σ_n n^{ε} ρ(ns).

In the computation it is truncated at ns ≤ X. The n^{−½} normalization appearing in the brief ("n^{ε−½}") is not in
the definition: the factor e^{y/2} already absorbs the Haar weight. What follows holds equally with any fixed weight
w_n > 0, substituting h_n ↦ w_n h_n.

Writing h_n(s) := ρ(ns) and K_r(m,n) := λ∫_1^∞ h_m h_n ds (the Gram matrix of the dilates restricted to s ≥ 1), one gets

  F_r(ε) = Σ_{m,n} (mn)^{ε} K_r(m,n),
  F_r′(0) = 2⟨Zr, Z_log r⟩,
  F_r″(ε) = 2‖Z_log^{(ε)}r‖² + 2⟨Z^{(ε)}r, Z_{log²}^{(ε)}r⟩.   (1.1)

This matches F0_TEST §5. The series converges absolutely for |ε| < ½ if ρ = O(ω^{−2}), as in A_MU §2.

## 2. Structure: Laplace transform of a signed measure

**Proposition 2.1 (PROVED).** F_r(ε) = ∫_ℝ e^{εt} dν_r(t), where ν_r := Σ_{m,n} K_r(m,n) δ_{log m + log n}. Hence,
F_r^{(k)}(0) = ∫ t^k dν_r: F″(0) is the second moment of a signed measure whose total mass is F(0) ≥ 0.

*Proof.* Immediate from (1.1), by absolute convergence. ∎

**Remark 2.2 (PROVED; answer to the brief's Schur question).** Write F″(0) = ⟨K_r, W⟩_{Schur}, with
W_{mn} = (a_m + a_n)² and a = log.
- W = a²·1ᵀ + 2aaᵀ + 1·(a²)ᵀ has rank ≤ 3.
- As a quadratic form, x ↦ Σ_{m,n}(a_m+a_n)²x_m x_n = 2(Σa²x)(Σx) + 2(Σax)². The product of two independent linear
  forms has signature (1,1), and the square adds an independent +. If a takes ≥ 3 distinct values (1, a, a²
  independent), the signature is (2,1). Example: with a = (0, log2, log3), the matrix W has a negative eigenvalue.
- Hence Schur's theorem (PSD ∘ PSD = PSD) does not apply. F″(0) ≥ 0 is not automatic, not even for K_r PSD, which it
  always is because it is a Gram matrix.
- Multiplying by (mn)^{ε} = u_m u_n, a positive diagonal congruence, changes nothing.

**Remark 2.3 (PROVED; the brief's "e^{εB}").** Pointwise in s, S_ε(s) = Σ_n e^{ε log n}h_n(s) is a real exponential
polynomial in ε. The identity (S²)″ = 2S′² + 2SS″ says that the integrand is convex where S·S″ ≥ 0 and can be
concave where S > 0 and S″ < 0. That happens when two dilates with distinct frequencies log n overlap with opposite
signs. The deformation acts *before* summing, on non-orthogonal vectors h_n. It is not e^{εB} applied to a vector,
and spectral log-convexity (Σe^{2ελ_j}|v_j|²) is not inherited.

## 3. Theorem F⁻: Lemma F is false as a standalone theorem

**Theorem F⁻ (NO-GO, PROVED).** Fix 1.2 < ω₀ < 1.45, 0 < w < min(ω₀ − 1.2, 0.05) and φ ∈ C_c^∞((ω₀−w, ω₀+w)),
φ ≢ 0, real. For c ∈ ℝ let ρ_c(ω) := φ(ω) + cφ(ω/2), which is C^∞ with compact support in (1, ∞). Then, for every X ≥ 3,

  F_{ρ_c}(ε) = λ‖φ‖²_{L²}[(1 + c·2^{ε})² + 2c²],   F″_{ρ_c}(0) = 2λ‖φ‖²(log 2)² c(1 + 2c).

In particular F″(0) < 0 for all c ∈ (−½, 0). Moreover F is strictly concave in a neighborhood of ε = 0 when
c ∈ (−½, 0), so log-convexity and the bound F″ ≥ c·ℓ also fail.

*Proof.* The n-th summand of S_ε(s) is n^{ε}[φ(ns) + cφ(ns/2)]. One must check which pieces have support in s ≥ 1.
- φ(ns) ≠ 0 requires ns ∈ (ω₀ ± w) ⊂ (1.15, 1.5). With s ≥ 1 only n = 1 is possible, at s ∈ (ω₀ ± w).
- φ(ns/2) ≠ 0 requires ns ∈ (2ω₀ ± 2w) ⊂ (2.3, 3). With s ≥ 1, n ∈ {1, 2}: the n = 1 piece lives at
  s ∈ (2ω₀ ± 2w) and the n = 2 piece at s ∈ (ω₀ ± w).
- The case n = 3 would give s < 3/3 = 1 and falls outside the half-line. This is where the cutoff at T is used: the
  piece that on the full line would compensate the concavity falls on the other side of T.
- n ≥ 4 is excluded.

Thus, S_ε(s) = (1 + c·2^{ε})φ(s) on (ω₀ ± w) and S_ε(s) = cφ(s/2) on (2ω₀ ± 2w). The two intervals are disjoint,
because 2ω₀ − 2w > ω₀ + w ⟺ ω₀ > 3w. Also ∫φ(s/2)²ds = 2‖φ‖². Integrating and differentiating twice at ε = 0, with
(1 + c2^{ε})² ↦ 2(log2)²c(1 + 2c) at 0, gives the formula. ∎

**Corollary F⁻.1 (infinite-dimensional negative subspace; PROVED).** Take centers ω₀^{(1)}, …, ω₀^{(K)} ∈ (1.2, 1.45)
with windows w small enough that the 2K intervals (ω₀^{(k)} ± w) and (2ω₀^{(k)} ± 2w) are pairwise disjoint. Then the
quadratic form r ↦ F_r″(0) block-diagonalizes on span{ρ_{c}^{(k)}} and is negative definite on that subspace of
dimension K. Since K is arbitrary, F″(0) has infinite negative index on C_c^∞(1, ∞).

*Proof.* That of F⁻ applied to each k. The cross terms vanish by disjoint supports. ∎

**Corollary F⁻.2 (minimal-leak representatives and the Paley–Wiener class; ARGUED).**
(a) **Minimal leak.** Paper 46's §22 / MORI15 minimal-leak gauge projects onto the complement of a finite-dimensional
gauge space (M = 28 modes at μ = 15). A negative subspace of dimension ≥ 29 intersects that complement. Hence there
exists r that is its own minimal-leak representative and has F″(0) < 0.
(b) **Paley–Wiener class.** The restrictions to (λ, ∞) of 𝓕f, with f ∈ L²[−λ, λ], are dense in L²(λ, ∞) with
polynomial weight (Hahn–Banach argument and analyticity in the half-plane). F″(0) is continuous in the norm
‖ω^{1+δ}ρ‖_{L²}. Hence the negative index carries over to the admissible class.
**Gaps toward PROVED.** It remains to write out the continuity of F″ in that norm and to verify that the admissibility
condition g(T) = 0 (F0_TEST (iii)) does not break the density. T10.1 also gives an explicit Paley–Wiener example
without appealing to density.

**Reading.** The brief asks whether Lemma F is true ∀r, false, or true only on a cone. The answer is: **false
∀r** (F⁻), **true on cones** (§5), and at the extremal **true numerically** (F0_TEST), because r* is in neither
of the proved cones.

## 4. T10.1 — numerical falsification (NUMERICAL)
**Pipeline.** That of `step3_F.py`, with the same mesh and the same cutoff: y = log s, dy = 1.5·10⁻⁵…3·10⁻⁵, ns ≤ X.
Scripts: `LEMMA_F_HALFLINE_001_data/t10_1.py` and `t10_1b.py`; outputs `t10_1_X{60,120,240}.json` and `t10_1b.out`.

**(i) Verification of Theorem F⁻.** With ω₀ = 1.3, w = 0.04, X = 60:

| c | F″(0) quadrature | 2λ‖φ‖²(log2)²c(1+2c) |
|---|---|---|
| −0.05 | −8.9152149554084·10⁻⁴ | −8.9152149554084·10⁻⁴ |
| −0.25 | −2.4764485987246·10⁻³ | −2.4764485987246·10⁻³ |
| −0.45 | −8.915214955408·10⁻⁴ | −8.915214955408·10⁻⁴ |
| +0.10 | +2.3773906547756·10⁻³ | +2.3773906547756·10⁻³ |

Agreement to 16 digits. With ω₀ = 1.5 the n = 3 case does enter, with s ∈ (0.97, 1.03), leaving an extra term
c²(log 9)²·(≤ ⅔)‖φ‖². Even so, F″(0) gives −8.09·10⁻⁴ (c = −0.05) and −1.05·10⁻³ (c = −0.2), stable across
X = 60 → 240 to 10⁻¹².

**(ii) Twelve Paley–Wiener modes away from the extremal.** Basis: f_j(u) = P_{2j}(u/λ) − P_{2j+2}(u/λ) for |u| ≤ λ,
j = 0…11. They are even, vanish at ±λ, and so r_j = 𝓕f_j|_{(λ,∞)} = O(ξ^{−2}) is admissible in decay. The closed
form is r_j(λω) = 2λ[(−1)^j j_{2j}(z) + (−1)^j j_{2j+2}(z)], with z = 30πω.

This basis is polynomial, not prolate. In the range used, its spaces coincide with those of the first 12 even
prolates of bandwidth c = 30π up to exponentially small errors, so the test is equivalent to the one requested. **The
gauge was not fixed** (see F⁻.2).

Results (X = 240; identical to 3 figures with X = 60):
- **The 12 random combinations** (seed 204), normalized by ℓ = ‖r‖²_{(λ,∞)}, give
  F″(0)/ℓ ∈ {0.244, 0.115, 0.214, 0.102, 0.398, 0.234, 0.363, 0.462, 0.076, 0.271, 0.066, 0.258}: all > 0.
  F(0)/ℓ ∈ [1.04, 1.15].
- **Diagonal:** F″/ℓ ∈ [0.261, 0.282].
- **Generalized problem** (Q, G), with G whitened over its 6 non-degenerate eigenvalues. The 6 remaining eigenvalues
  are < 10⁻¹¹ relative: the high modes barely leak.
  κ ∈ {−0.0054, −0.0005, 0.0097, 0.064, 1.057, 2.867}.
- **Minimal direction v_min, recomputed directly:** F″(0) = −5.42·10⁻³, ℓ = 1.000 (quadrature up to ω = 400) / 0.998
  (up to ω = 2000), F(0) = 0.980, F′(0) = −0.0101. Stable across X = 60, 120, 240.

**Verdict T10.1.** Random sampling finds no negatives: the positive cone is "large" in measure. But optimization does
find them. There is an r of Paley–Wiener type (combination of 12 even modes with decay ξ^{−2}) with
F″(0)/ℓ ≈ −5.4·10⁻³. The margin is small but has no sign ambiguity, because Q(v) is computed directly and does not
depend on the whitening. Together with F⁻ (exact) this **closes Lemma F as a uniform inequality**. This is the "there
is a negative ⇒ close it" branch of TRACT_001 §6.3.

**Caveats.**
- v_min is not fixed in gauge nor does it satisfy g(T) = 0.
- The exact counterexample is the one in §3. The minimal-leak part in Paley–Wiener is ARGUED (F⁻.2).

## 5. Where it holds: cones and three lines (T10.2)

**Proposition 5.1 (positive Gram cone; PROVED).** If K_r(m,n) ≥ 0 for all m, n, then ν_r ≥ 0 and
F_r(ε) = ∫e^{εt}dν_r is log-convex on every interval of convergence, by Hölder:
F((ε₁+ε₂)/2) ≤ F(ε₁)^{½}F(ε₂)^{½}. In particular F″ ≥ F′²/F ≥ 0. ∎

**Proposition 5.2 (pointwise cone; PROVED).** If ρ ≥ 0 on (1, ∞), then S_ε(s) is a sum with coefficients ≥ 0 of
exponentials e^{ε log n}. Hence it is log-convex in ε for each s. Its square is also log-convex, and the integral of
log-convex functions is log-convex (Hölder). Thus F_r is log-convex. This is a particular case of 5.1. ∎

**Proposition 5.3 (three lines; PROVED/CITED).** For ε = σ + iτ in the strip |σ| < ½, ε ↦ Z^{(ε)}r is holomorphic and
bounded with values in L²(T, ∞). By the vector-valued Hadamard three-lines theorem (CITED, e.g. Reed–Simon II,
IX.4), the function M(σ) := sup_τ ‖Z^{(σ+iτ)}r‖ is log-convex in σ.

Always M(σ)² ≥ F_r(σ). On the cone ρ ≥ 0 there is equality, because |Σ n^{σ+iτ}ρ(ns)| ≤ Σ n^{σ}ρ(ns): there the
three lines reproduce 5.2. Outside the cone the sup is attained at τ ≠ 0, and M does not control F′(0).

**Conclusion T10.2 (PROVED).** The convexity given by complex interpolation (three lines or Stein) is that of M(σ),
not that of F(σ). They coincide exactly on the positive cone, and F⁻ shows that outside it F is not convex. No
"boundary" version can rescue the universal statement, because the F⁻ counterexample *uses* the boundary: the n = 3
piece falls at s < 1. A Hardy condition on the trace at λ, as T10.2 proposed, is not enough either: F⁻ has ρ ≡ 0
near ω = 1.

**Is the extremal the only point where it holds?** No.
- It holds on the cones 5.1/5.2, which have nonempty interior in L²(λ, ∞): for example ρ ≥ 0 with compact support.
- It holds on 100% of 12 random Paley–Wiener samples.
- It holds at r* (NUMERICAL, F0_TEST).

But r* is **not** in any proved cone. ⟨h₁,h₂⟩ = −1.32 < 0 (F0_TEST §4), so K_{r*} is not ≥ 0, and ρ* changes sign.
No proved criterion gives convexity at r*. What remains is a numerical datum for a single vector.

## 6. The A_MU bound as an independent inequality: is it an input?

**Lemma 6.1 (PROVED, without D).** For admissible r, in a fixed gauge and with ε > 0: if F_r is convex on [0, ε], then

  𝒲(r) ≥ L_r(ε) := 𝒜[Zr] + 2AB − (F_r(ε) − F_r(0))/ε.

*Proof.* By Theorem D (A_MU (f), PROVED given thm:ext-half; verified to 10⁻¹⁰ in F0_TEST), 𝒲 = 𝒜 + 2AB − F_r′(0).
Convexity on [0, ε] gives F′(0) ≤ (F(ε) − F(0))/ε. ∎

The inequality is correct, and AUDIT_AMU did not refute it: it refuted the *factorization*. But its hypothesis is the
convexity **of the given r**. By F⁻ this is not a universal theorem, so 6.1 is CONDITIONAL vector by vector and
PROVED on the cones 5.1/5.2.

**Honest evaluation of the "alternative certificate at μ = 15."**
1. **At r*.** L_{r*}(0.186) ≈ 2.5·10⁻⁷⁰ > 0 (F0_TEST, NUMERICAL). The convexity of F_{r*} on [0, 0.186] is only
   verified on a mesh (NUMERICAL): r* is in no proved cone. So "𝒲(r*) ≥ 2.5·10⁻⁷⁰" is not PROVED; it is NUMERICAL
   twice over.
2. **Even if it were proved.** L_r(ε) uses the same data (𝒜, F at two points) as 𝒲(r) = 𝒜 + 2AB − F′(0), which
   Theorem D gives *exactly*. A weaker lower bound of a quantity already computed exactly at the same cost certifies
   nothing new: 2.5 < 4.98.
3. **It does not control the infimum.** Positivity at μ = 15 is a statement about inf_r 𝒲(r), the minimal
   eigenvalue, not about a vector. Certifying it with 6.1 would require inf_r L_r(ε) > 0 over all r. That requires
   uniform convexity (false by F⁻) and moreover L_r ≤ 𝒲_r, so inf L > 0 would be stronger than what one wants to
   prove. On the cone ρ ≥ 0 the bound is PROVED, but nothing indicates that the minimizer lives there: r* does not
   live there.
4. **Gauge dependence.** F is not gauge invariant (F0_TEST (i)). One could maximize L_r(ε) over the gauge, but it is
   still a per-vector bound, with the same defects as in 3.

**Verdict §6.** Lemma 6.1 is correct. As an input for D: **no**. It gives no information about 𝒲 that Theorem D does
not already give exactly, and the uniform version that would be needed is false (F⁻).

## 7. Verdict and labels
| statement | label |
|---|---|
| F_r(ε) = ∫e^{εt}dν_r, ν_r = Σ K_r(m,n)δ_{log mn} (Prop 2.1) | PROVED |
| [(log m+log n)²] has signature (2,1); Schur does not apply (Obs 2.2) | PROVED |
| **Theorem F⁻**: F″(0) = 2λ‖φ‖²(log2)²c(1+2c) < 0 for ρ = φ + cφ(·/2), ω₀ ∈ (1.2, 1.45), c ∈ (−½, 0) | **PROVED (NO-GO of the universal Lemma F)** |
| Infinite negative index of r ↦ F″_r(0) on C_c^∞(1, ∞) (Cor F⁻.1) | PROVED |
| Also fails for minimal leak / Paley–Wiener (Cor F⁻.2) | ARGUED (+ NUMERICAL PW example) |
| T10.1: 12/12 random PW samples with F″ > 0; minimal PW direction with F″/ℓ = −5.4·10⁻³ | NUMERICAL |
| Log-convexity on the cones K_r ≥ 0 and ρ ≥ 0 (Props 5.1–5.2) | PROVED |
| Three lines: M(σ) log-convex; = F only on the cone (Prop 5.3) | PROVED/CITED |
| T10.2 "three lines with boundary" for the universal F | NO-GO (F⁻ uses the boundary and has zero trace at λ) |
| Convexity of F_{r*} (Mori μ = 15) | NUMERICAL (r* outside the cones) |
| Lemma 6.1: 𝒲 ≥ 𝒜 + 2AB − (F(ε)−F(0))/ε given F_r convex | PROVED conditional per vector; not an input for D |
| L′♯, row D | OPEN |

**Route 3 of TRACT_001: closed.** It is closed as a uniform theorem by an explicit falsifier (F⁻). What remains
proved is a cone lemma that does not reach the extremal. It is not reopened unless someone gives a cone 𝒞 with two
properties at once: (i) F convex on 𝒞 (PROVED) and (ii) the minimizer of 𝒲 is in 𝒞 (PROVED). Moreover 𝒞 would
have to lie outside K ≥ 0 and ρ ≥ 0, which do not contain r*.

## 8. Entry for the index (ROUTES-TRIED-INDEX, phase 204)
- **LEMMA_F_HALFLINE_001 (phase 204g, route 3 of TRACT_001; NO-GO).**
  - Lemma F (convexity of ε ↦ ‖Z^{(ε)}r‖²_{(T,∞)}, without Λ) false as a standalone theorem. Exact falsifier PROVED:
    ρ = φ + cφ(·/2), with a bump at ω₀ ∈ (1.2, 1.45), gives F″(0) = 2λ‖φ‖²(log2)²c(1+2c) < 0 for c ∈ (−½, 0). The
    n = 3 piece falls below T. Infinite negative index; minimal leak / PW ARGUED.
  - T10.1 NUMERICAL: 12/12 random PW samples positive, but the minimal PW direction gives F″/ℓ = −5.4·10⁻³.
  - PROVED: log-convexity on the cones K_r ≥ 0 / ρ ≥ 0. Three lines = M(σ) = F only on the cone. r* outside both.
  - Bound 𝒲 ≥ 𝒜 + 2AB − ΔF/ε correct but per vector; not an input (Theorem D already gives 𝒲 exactly).
  - Do not retry: uniform Lemma F, three lines/Stein for F, Hardy condition at λ.
