# Round 20 A — Gauge-fixed tail inequality: representatives, the comb-null quadric, and canonical sections

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_019_B: admissible f, E, Φ_f, Ψ_f, gauge 𝒢_T, gauge radicals Φ_φ,
𝒲̂ = 𝒜_∞ − 𝒞 + 𝒯, 𝒜𝒫 = 𝒜_∞ + 𝒯, 𝒲̂^c = 𝒜𝒫 − c𝒞. V_T := {Ψ_f : f admissible, Ef ∈ P_T} (a real vector space),
R_T := {Φ_φ : φ ∈ 𝒢_T} ⊂ V_T. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

Idea under test. 𝒲̂ is constant on each fibre Ψ_f + R_T (radical identity, Λ-specific), 𝒲̂^c is not. Hence (★) would
follow from: every fibre contains a representative on which the comb-robust inequality 𝒜𝒫 − c𝒞 ≥ 0 holds for c in a
neighbourhood of 1; better, from a canonical (Λ-free) section on which it holds with a uniform margin δ.

## 0. Corpus check
Read: ROUND_019_B (Prop 1.1, Cor 1.2, Thm 2.1, Cor 2.2–2.3, the OPEN (ii_s)), ROUND_018_B (Lemma 1.1, c-scan on prolate
representatives), ROUND_001_B (Thm 1.1 radical lemma, Prop 1.4–1.5), ROUND_016_B (ℓ_g), phase 199 proof-L-sharp MM_001
("lossless loop; passivity margin = W_T itself"), Paper 46 prop:ext-gauge, prob:ext-L, prop:ext-consol; index rows
P211-18B, P211-19B. What differs from the indexed attempts: 19B closed comb-robust inequalities on the WHOLE class of
admissible tails; it left open the gauge-fixed version (ii_s). This memo (a) settles the existential version ("some
representative") completely, by a pure-math argument, and (b) measures the Λ-free sections that (ii_s) could use. No
indexed route is retried.

## 1. The existential version is binary (PROVED)

**Lemma 1.1 (comb on a fibre).** For Ψ ∈ V_T and Φ ∈ R_T: 𝒞[Ψ + Φ] = 𝒞[Ψ] + 2𝒜𝒫(Ψ, Φ) + 𝒜𝒫[Φ].
*Proof.* Φ is 𝒲̂-radical (ROUND_001_B Thm 1.1), so 𝒞(Φ, ·) = 𝒜𝒫(Φ, ·). Expand. ∎

**Lemma 1.2 (every fibre meets the comb-null quadric).** For every Ψ ∈ V_T there is Φ ∈ R_T with 𝒞[Ψ + Φ] = 0.
*Proof.* By ROUND_019_B Thm 2.1 there are Φ_± ∈ R_T with ±𝒜𝒫[Φ_±] > 0. On the line t ↦ Ψ + tΦ_±, 𝒞 is a quadratic in t
with leading coefficient 𝒜𝒫[Φ_±] (Lemma 1.1), so 𝒞 → ±∞ along the two lines. The fibre is an affine space, hence
path-connected, and 𝒞 is continuous on the finite-dimensional affine span of {Ψ, Φ_+, Φ_−}; the intermediate value
theorem gives a zero. ∎

**Theorem 1.3 (representative margins carry exactly one bit).** Fix T and Ψ ∈ V_T, w := 𝒲̂[Ψ] (fibre constant). For
I ⊂ ℝ put Rep(I) := {Ψ′ ∈ Ψ + R_T : 𝒲̂^c[Ψ′] ≥ 0 for all c ∈ I}.
 (a) For every single c ≠ 1, Rep({c}) ≠ ∅, whatever the sign of w.
 (b) For every interval I ∋ 1 (of any length, including I = ℝ): Rep(I) ≠ ∅ ⟺ w ≥ 0.
 (c) If w ≥ 0 the comb-null representatives (𝒞 = 0, Lemma 1.2) lie in Rep(ℝ); 𝒲̂^c = 𝒜𝒫 = w on them for every c.
*Proof.* 𝒲̂^c[Ψ′] = w + (1 − c)𝒞[Ψ′]. (a) By Lemma 1.1 and Thm 2.1 of 19B, 𝒞 takes every real value on the fibre
(Lemma 1.2's argument, with any target value in place of 0); pick 𝒞[Ψ′] with (1 − c)𝒞[Ψ′] ≥ −w. (b) ⟸ by (c); ⟹ take
c = 1 ∈ I. (c) direct. ∎

**Corollary 1.4 (the "clever representative" statement is (★); PROVED).** By 19B Cor 1.2,
  (★) at T ⟺ every fibre of V_T contains a representative with 𝒲̂^c ≥ 0 for all c in some interval around 1
       ⟺ 𝒜𝒫[Ψ] ≥ 0 for every Ψ ∈ V_T with 𝒞[Ψ] = 0.
The last form is invariant under Λ ↦ cΛ (it involves 𝒞 only through its zero set). It is still not a falsifier failure
in the sense of rule 4(a): its equivalence with (★) uses the radical identity (Λ-specific); for the comb cΛ the
statement about the quadric {𝒞 = 0} says nothing about a^c_T, because 19B Cor 2.2 makes 𝒲̂^c non-constant on fibres.

**Theorem 1.5 (the S-lemma multiplier is forced to be 1; PROVED on finite-dimensional sections, ARGUED in general).**
Let S ⊂ V_T be a finite-dimensional subspace containing Φ_+ and Φ_− of Thm 2.1 (19B). If 𝒜𝒫 ≥ 0 on S ∩ {𝒞 = 0}, the
equality-constrained S-lemma (Finsler; CITED: Pólik–Terlaky 2007, Thm 2.2 for an indefinite constraint form) gives
μ ∈ ℝ with 𝒜𝒫 − μ𝒞 ⪰ 0 on S. Letting S increase through the gauge directions of 19B Thm 2.1, μ ≥ 1 (from Φ_−:
𝒜𝒫[Φ_−] − μ𝒞[Φ_−] = (1 − μ)𝒜𝒫[Φ_−] ≥ 0 with 𝒜𝒫[Φ_−] < 0) and μ ≤ 1 (from Φ_+). So μ = 1 and the certificate is
𝒲̂ ⪰ 0 on S: the comb-null quadric version contains no information beyond 𝒲̂ ⪰ 0 itself.
*Proof.* As written; for an infinite-dimensional V_T the S-lemma needs a closedness hypothesis on the joint range
(ARGUED: it holds on every finite-dimensional S, which is all a Galerkin or density argument uses). ∎

Reading. "Choose the representative cleverly" is exactly the multiplier choice in the S-lemma, and the multiplier is
pinned at 1 by the gauge radicals of both signs. The choice of a good representative already uses the sign: the best
representative (comb-null) has margin ℝ if w ≥ 0 and ∅ otherwise. This is the MM_001 circle in its sharpest form:
the passivity margin of the lossless loop on any representative is w itself.

## 2. Canonical Λ-free sections: measured c-margins (NUMERICAL)

Tools. tools/gauge_section.py T w R L h: admissible data f(y) = |y|^{−1/2}g(log|y|), g a combination of C^∞ bumps of half-width w
(spacing w), window bumps centred in (−T, T), gauge bumps centred in (−T − R, −T); Φ_f(x) = Σ_n n^{−1/2}g(x + log n) (exact
finite sums on a midpoint grid of step h on (−T − L, −T)); 𝒜_∞, 𝒞, 𝒯 as in rung_gram_tail.py; constraints ℱf(0) = 0 and
Ef ∈ P_T; leakage Gram ℓ(f) = ∫_λ^∞|ℱf|² = ∫_0^∞ f² − ∫_0^λ|ℱf|² (Parseval, so only the band ξ ≤ λ is computed).
tools/gauge_section_anal.py npz: gauge space, classes (window part, Mw-orthonormal), four sections of each fibre:
none (gauge part fixed by one pivot bump), ell (min ℓ), f2 (min ∫_0^{1/λ} f²), tail (min ‖Ψ‖²_{L²(−∞,−T)}); for each,
the c-interval on which 𝒜𝒫 − c𝒞 ⪰ 0 on the section and δ := inf 𝒲̂/|𝒞| on it.
Validation. Radical identity: max|𝒲̂(Φ_φ, ·)| / max|𝒜_∞(Φ_φ, ·)| ≤ 5·10⁻⁴ in every run (grid error); 𝒲̂ on classes agrees
across the four sections to 4 digits (fibre invariance reproduced).

| T | w | R | classes | gauge rank | λ_min 𝒲̂ (classes) | δ none | δ ell | δ f2 | δ tail | c-interval (tail) |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.8 | 0.1 | 2 | 13 | 19 | 0.0203 | 0.179 | 0.027 | 0.73 | 1.29 | [−0.40, 2.29] |
| 0.8 | 0.1 | 3 | 13 | 29 | 0.0203 | 0.179 | 0.058 | 0.29 | 1.27 | [−0.27, 2.32] |
| 0.8 | 0.07 | 2 | 19 | 27 | 0.0225 | 0.067 | 0.013 | 0.47 | 0.97 | [−0.50, 1.96] |
| 0.8 | 0.07 | 3 | 19 | 41 | 0.0225 | 0.067 | 0.006 | 0.23 | 1.01 | [−0.37, 2.00] |
| 0.8 | 0.05 | 2 | 29 | 39 | 0.0276 | 0.035 | 0.006 | 0.36 | 0.74 | [−0.47, 1.73] |
| 0.8 | 0.035 | 2 | 42 | 56 | 0.0356 | 0.017 | 0.0035 | 0.24 | 0.37 | [−0.79, 1.36] |
| 1.0 | 0.1 | 2 | 17 | 19 | 0.0109 | 0.124 | 0.0005 | 0.70 | 1.22 | [−0.40, 2.21] |
| 1.0 | 0.07 | 3 | 25 | 41 | 0.0133 | 0.061 | 0.019 | 0.23 | 0.89 | [−0.35, 1.89] |

Findings (NUMERICAL).
(a) ℓ-minimising section: no margin. δ = 0.027 → 0.0035 as the span grows; the minimiser pushes tail mass deep (‖Ψ‖² up to
2·10⁵ times the window norm at T = 1); the c-interval closes onto c = 1 from above. (ii_s) on the ℓ-section fails as a
robust statement.
(b) f2 / prolate-type section (smallest small-y profile, the analogue of the band-concentrated prolate representatives
of 18B): δ falls 0.73 → 0.24 with resolution and with R.
(c) tail-L² section: the best of the three; R-stable, but δ falls 1.29 → 0.97 → 0.74 → 0.37 as the window/gauge resolution
w goes 0.1 → 0.035. No uniform δ is visible; the trend is compatible with δ → 0.
(d) best representative over the fibre: by Thm 1.3 its margin is ℝ when 𝒲̂ ≥ 0. In the finite spans the comb-null
representative is found on a single gauge line whenever 𝒞|gauge is indefinite (13/13 classes at w = 0.1); at w = 0.035,
R = 2, 𝒞 = 𝒜𝒫 is positive definite on the finite gauge span (0/42) — the negative directions of 19B Thm 2.1 need deep
(R → ∞) low-frequency gauge support, not reached at R = 2. A finite-rank effect, not a counterexample to Lemma 1.2.
Mechanism of (c) (ARGUED). If the gauge-tail span is L²-dense in L²(−∞, −T) (19B (α), ARGUED), the tail-L² minimiser
is not attained in the limit (inf ‖Ψ‖ = 0 on each fibre with 𝒲̂ fixed); the finite-rank section then moves to higher
frequency as the rank grows and its margin is a truncation artefact. The same holds for f2 (closure of the gauge in
L²(0, 1/λ) is {∫ = 0}; the limit minimiser is the constant profile on (0, 1/λ), not admissible).

## 3. The split (A) + (B) and whether (B) is a restatement

(A) (PROVED, Λ-specific): 𝒲̂ is constant on fibres (ROUND_001_B Thm 1.1) and a_T(Ef) = 𝒲̂[Ψ_f] on P_T (Cor 1.2).
(B_δ, s) (OPEN): for a Λ-free linear section s of the fibres, 𝒜𝒫[Ψ] − c𝒞[Ψ] ≥ 0 for all Ψ ∈ Ran s and c ∈ [1 − δ, 1 + δ];
equivalently 𝒲̂ ≥ δ|𝒞| on Ran s.
Status. (A) + (B_δ, s) ⟹ (★) (PROVED: Ran s meets every fibre). Converse: not formal, but (B_δ, s) contains (★) on every
class with room δ|𝒞|; it is a coercivity of 𝒲̂ in the unit |𝒞| on a section — the same type as prob:ext-L (unit ℓ) and
eq:ext-starstar with κ > 0. By Thm 1.5 the only multiplier that survives the whole gauge is c = 1, so a crude
("archimedean beats the comb with room") proof of (B) must exploit that Ran s excludes the deep low-frequency radicals
of 19B Thm 2.1, i.e. the section must do the work that the radical identity does — the MM_001 circle (the passivity
margin on any representative is 𝒲̂ itself). ARGUED: (B) is not weaker than prob:ext-L; for the three natural Λ-free
sections it is numerically not uniform (§2).
Does choosing the representative use the sign? For the existential choice: yes, exactly (Thm 1.3(b): the best
representative has margin ℝ or ∅ according to the sign of 𝒲̂). For a Λ-free section: the choice is sign-blind, but no
uniform margin is observed.
Falsifier test (rule 4). (a) cΛ: (A) fails (19B Cor 2.2, ROUND_001_B Prop 1.4), so the chain breaks — consistent. Note
that (B_δ, s) for Λ implies (B) for c₀Λ, |c₀ − 1| < δ, on the same section: (B) by itself is comb-robust and carries no
sign; the sign sits in (A). (b) a_P, (d) finite modifications: (A) fails (ROUND_001_B Prop 1.3). (c) Beurling: no Poisson
summation, (A) unavailable. Consistent; the split does not pass any falsifier.

## Result
NO-GO (PROVED) for the existential version, PIVOT (NUMERICAL) for canonical sections.
### What was proved
- Lemma 1.1–1.2: 𝒞 on a fibre is 𝒞[Ψ] + 2𝒜𝒫(Ψ, Φ) + 𝒜𝒫[Φ]; every fibre meets the comb-null quadric {𝒞 = 0}.
- Thm 1.3: the c-margin of the best representative is ℝ if 𝒲̂ ≥ 0 and ∅ otherwise; for single c ≠ 1 a good representative
  always exists. "Choose a representative with comb-robust positivity" is (★) exactly.
- Cor 1.4: (★) ⟺ 𝒜𝒫 ≥ 0 on V_T ∩ {𝒞 = 0} (a weight-scaling-invariant restatement, Λ-specific only through (A)).
- Thm 1.5: the equality S-lemma multiplier is forced to 1 by the two-signed gauge radicals (finite-dimensional sections).
### What failed and why
A canonical Λ-free gauge with uniform δ: none found. ℓ-section δ → 0 (0.027 → 0.0035); f2 (prolate-type) 0.73 → 0.24;
tail-L² 1.29 → 0.37 with resolution, T = 0.8 and 1.0. Mechanism ARGUED: L²-type minimisers are not attained once the
gauge closure is dense; their finite-rank margins are truncation artefacts. The large margin of 18B is a representative
effect (19B) and, per this memo, also a resolution effect.
### Next concrete step
Decide whether the tail-L² margin has a positive limit: run w = 0.025 and 0.018 (R = 2, 3) at T = 0.8 and fit δ(w); if
δ(w) → 0, record the closure of the gauge-fixed tail-form line (every margin must sit in the radical identity). If it
stabilises, formulate (B) on the limit section with its non-attainment handled by a weighted (H¹-type) tail norm.

## Index row and ledger line
Index (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md): row P211-20A. Ledger (LEDGER.md): line C42.
