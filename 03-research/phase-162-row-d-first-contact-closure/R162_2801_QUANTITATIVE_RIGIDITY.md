# R162_2801 — Quantitative Hamburger rigidity for finitely many off-line quartets (angle A) — **NO-GO (PROVED) for class rigidity (Hamburger / Bochner / Kaczorowski–Perelli / SMO) as a proof of C_B; PARTIAL: three PROVED lemmas; the exact needed statement is identified and is C_B itself (Pontryagin form), a restatement adjacent to E1**

Cell: 4F (Euler × global transform), nearest routes R162_2601 (Thm H), R162_2501 (M_m), 34/94 §11 (Lemma 11.4).
Corpus check: grep "Hamburger", "Bochner", "Kaczorowski", "strong multiplicity", "almost periodic" over 03-research,
04-papers: Hamburger only as a dictionary (R162_1203, R162_407, R162_2601 Thm H); no file treats ζ/R. Pure math, no numerics.

## 0. Setup
Assume ξ has exactly m ≥ 1 off-line quartets Q_j = {ρ_j, ρ̄_j, 1−ρ_j, 1−ρ̄_j}. Let P(s)=∏_j ∏_{a∈Q_j}(s−a) and
P₀(s)=∏_j ∏_{b∈Q'_j}(s−b) with Q'_j four chosen points on Re s=½ (symmetric under s↦1−s, conjugation). R := P/P₀ is
rational, R(s)=R(1−s), R→1 at ∞. ξ₀ := ξ/R is entire, order 1, same FE, all zeros on the line; ζ₀ := ζ/R.
Then −ζ₀′/ζ₀ = Σ Λ(n)n^{−s} + r(s), r := R′/R·(−1)... explicitly r(s) = −Σ_{a}1/(s−a) + Σ_{b}1/(s−b) (8m terms), and for
Re s > max Re a, r(s) = ∫_0^∞ E(u) e^{−su} du with E(u) = Σ_b e^{bu} − Σ_a e^{au} (the a.c. density of R162_2601).

## 1. Falsifier lines (first)
- **deletion** (remove a finite off-line set from ζ by division): produces exactly ζ₀ above — the "almost Euler product" (Dirichlet series + rational log-derivative, FE, real zeros) is REALIZED. Any property of the pair (Λ, rational r) with r ≠ 0 which is class-level is satisfied by deletion. Kills "rational defect is impossible".
- **M_m** (ξ × rational, R162_2501): the mirror: completed function ξ·R^{−1}-type with Dirichlet log-derivative plus rational, m off-line quartets, all hypotheses of §0 except that the Dirichlet part is ζ's. Shows: FE + (Dirichlet + rational) log-derivative does not constrain m in either direction.
- **Λ̃** (R162_2601 Thm Λ̃): atomic non-log-derivative weights reproduce any finite exponential density E; so "atoms + E" is not detected by the atom/density split — the discriminator must be the Euler product nonlinearly, not the decomposition.
- **DH**: m = ∞, C_B vacuous; kills any argument that proves "m<∞ ⇒ m=0" from FE + Dirichlet data only (DH has both, and finite rational modifications of DH give models with the same data and any m' ≥ the DH count changes by finitely many — i.e. finite-m structure is never seen by FE-level data).

## 2. PROVED lemmas
**Lemma 1 (uniqueness of the defect).** If D₁ + r₁ = D₂ + r₂ on a right half-plane, D_i absolutely convergent Dirichlet
series, r_i rational with r_i(∞)=0, then D₁=D₂, r₁=r₂. Proof: D₁−D₂ is uniformly almost periodic on σ=σ₀ large and
equals r₂−r₁ → 0 as |t|→∞; Bohr mean of |D₁−D₂|² is Σ|c_n|²n^{−2σ₀} = 0. ∎
So "−ζ₀′/ζ₀ = Dirichlet + rational" holds (answer to the question: YES, tautologically) and the rational part r is canonical.

**Lemma 2 (ζ₀ ∉ Dirichlet series, ∉ Selberg class; also ζR ∉).** By Lemma 1 with r ≠ 0: −ζ₀′/ζ₀ is not a Dirichlet series,
hence ζ₀ is not a Dirichlet series (log-derivatives of Dirichlet series with c₁≠0 are Dirichlet series). Same for ζ·R. ∎
Consequence: ζ₀ is a Beurling-type zeta with a continuous (signed) component dΠ = Λ-atoms + E(u)du; it lies in the class
where Beurling DMV already lives. Strong multiplicity one, Kaczorowski–Perelli degree-1 classification and Bochner's
converse theorem all take as input two (or one) elements of S (Dirichlet series); ζ₀ is not one.

**Lemma 3 (Hamburger with rational defect is empty).** Let F = D·R with D a Dirichlet series, R rational, R(s)=R(1−s),
and π^{−s/2}Γ(s/2)F satisfying ζ's FE with finitely many poles. Then D satisfies ζ's FE, so D = cζ (Hamburger), and
F = cζR. No condition on the zeros of ζ results: Hamburger returns ζ for every m. ∎

## 3. NO-GO (PROVED)
**Theorem NG.** No statement whose hypotheses are membership in {Dirichlet series (with or without Euler product) × symmetric
rational} ∩ {ζ-FE} can imply m=0 for ζ from m<∞. Proof: by Lemma 3 the class is {cζR}; the zero multiset of ζ is an input,
not an output. Every class rigidity theorem (Hamburger, Bochner, KP, SMO) is of the form "Dirichlet data + FE ⇒ F=cζ"
and so yields only ζ = ζ, identically in m. The deletion line (§1) shows the complementary class (ζ₀, real zeros, rational
defect) is nonempty whenever m ≥ 1 is hypothesized, and Lemma 2 puts it outside S where the theorems are silent. ∎

## 4. The exact statement that would prove C_B
(QR) *If G is entire of order 1, satisfies ξ's FE, has only real zeros (on Re s=½), and G·R is the completion of an
absolutely convergent Euler product for some symmetric rational R, then R is constant.*
For ζ, (QR) ⟺ C_B (m<∞ ⇒ m=0): given m<∞ take G=ξ₀; conversely C_B ⟹ (QR) since G·R Euler with ζ's FE is cξ (Lemma 3).
The hypothesis "G has only real zeros" is Weil positivity W_G ≥ 0 for the measure Λ + E; W_ζ = W_G + (finite-rank signed
term from Q_j, Q'_j), and ind₋ W_ζ = number of off-line zeros (Yoshida/Bombieri). So (QR) ⟺ **"the Weil form of ζ is
not a nonzero finite-rank negative perturbation of a positive form"**: ind₋W_ζ < ∞ ⇒ ind₋W_ζ = 0 (Pontryagin form of C_B).
Status: this is C_B verbatim (restatement, W6-type tautological transfer), NOT new content. It is not literally E1
(no ∀T per-window law), but its only known attack routes are per-window index counts (R162_2602: N(T)→2κ_off), which are E1.
It satisfies S11 (weaker than ⟺ RH) but fails S4: the only Euler input is through G·R ∈ S, which Lemma 3 collapses.

## 5. What would be new (O2801.1, feeds O2601.1)
A nonlinear Euler statement on ζ₀ itself: e.g. "exp(∫E(u)u^{−1}e^{−su}du)·ζ cannot be a Beurling zeta whose generalized
integers dN have a nonnegative measure with all zeros real" — requires positivity of dN (nonlinear in Λ, exp of Π) together
with real zeros. Deletion: dN₀ = dN_ζ * (inverse Laplace of 1/R) — sign of dN₀ is not known to fail; Λ̃ and DMV show
positivity of dN alone is compatible with off-line zeros and (in DMV-type constructions) with continuous parts. No
candidate inequality; recorded as O2801.1 (positivity of dN₀ vs. real zeros), live, 4F, falls to O2601.1.

## Verdict
NO-GO (PROVED) for quantitative class rigidity; PARTIAL: Lemmas 1–3 PROVED-TOOL; (QR) = C_B (Pontryagin form), restatement;
residual O2801.1 (Beurling positivity of ζ₀'s integer measure) ⊂ O2601.1.
