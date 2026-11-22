# CA_L_001 — The literal "magic function for row D": attainment, slackness, Poisson signs, modular-data genericity (seeds L1, L2, L3, L4, L7, L9)

Phase 193. Pen and paper; **no numerics**. Notation of Paper 46 (P46): window I_T, symbol σ_T, primal value λ_P (≥ λ_A
notation as in P46 rem:D1complete), K_P the annihilator class, flat-top class 𝒲 (def:W), ν_w (eq:nuw), f_w = σ_T + ν̂_w + 2ĝ₀.
Verified against P46 def:W (l.1179), eq:nuw (l.1183), thm:Z (l.1194), thm:O (l.729), rem:OvsB, def:shape-ops (l.8330).
**No sign contact. No negative value for ζ.**

## 1. Exact attainment is forbidden: the slackness set is ℝ
In Viazovska/CE the method is an *exact* dual optimum: the magic function g satisfies the sign conditions and the complementary-slackness
vanishing on the support of the primal optimum (the lattice shells), so the bound is attained.

**Theorem 1.1 (no exact magic certificate; PROVED from P46 thm:O).** For every T > 0, every finite even signed measure ν on {|u| ≥ 2T} and every
finite family of K_P-annihilators with coefficients β, the dual objective inf_τ[σ_T + ν̂ + Σβ_jĥ_j] is **strictly** below λ_P. In LP language:
the primal optimum μ_⋆ = |F̂_⋆|²dτ/2π has support ℝ (F̂_⋆ entire of exponential type, zeros discrete), so the slackness condition
"certificate − λ_P vanishes on supp μ_⋆" is the identity ϱ ≡ 0, which P46 thm:O shows to be inconsistent (K(u) ~ 1/u and the window atoms
cannot be matched by a bounded continuous function on 0 < |u| < 2T).
*Proof.* This is thm:O; the LP reading is its proof's first step (∫ϱ|F̂_⋆|² = 0, ϱ ≥ 0 ⇒ ϱ = 0 off a discrete set). ∎

**Remark 1.1′ (ARGUED).** The same contradiction holds for any tempered ν supported in {|u| ≥ 2T} whose transform is continuous and of
polynomial growth (the proof only restricts to 0 < |u| < 2T, where ν = 0). So passing to distributional "magic" objects does not help.

**Corollary 1.2 (what a magic function would have to be).** Every admissible object is an ε-certificate family (P46 thm:D1), whose total variation
diverges (rem:OvsB). A "magic function for row D" is therefore not an object but a *sequence* whose value approaches λ_P; by class (D) /
Problem (R) l.9006 it is admissible only as the final object of a computation that already carries the margin. **(V1) fails structurally:**
the primal of the window LP is continuous, not discrete. ∎

## 2. thm:Z: an exact flat-top certificate carries zero information
**Proposition 2.1 (PROVED, restatement of thm:Z(ii)).** For w ∈ 𝒲^reg, f_w(τ) = Σ_ρ ŵ(τ − γ_ρ). Hence the sign data that a Viazovska-type
construction would "read off explicit modular forms" is, for flat-top certificates, the sign of the smoothing of the zero-counting measure by
ŵ. In the sphere-packing case the corresponding sum Σ_{Λ*} f̂ runs over a *known* positive set (V2); here it runs over the object.
So the "explicit modular form" whose positivity would be read is ŵ on the set {τ − γ}: the reading presupposes the set. ∎
**Reading.** A magic certificate built only from modular/archimedean data (i.e. independent of the γ's) cannot be flat-top and exact; it must
leave the flat-top class (exterior signed ν with free β, P46 rem:bar-lin, which this paper does not exclude) — but then Thm 1.1 still applies.

## 3. The Poisson signs: CE gives the wrong direction
Explicit formula (P46 proof of thm:Z): Σ_ρ ĥ(γ_ρ) = 2∫h cosh(u/2)du − Σ_{n≥2} v_n h(log n) + (1/2π)∫m ĥ.
**Proposition 3.1 (PROVED).** (a) If ĥ ≥ 0 and h ≥ 0 on {log n}, then Σ_ρ ĥ(γ) ≤ polar + archimedean: an *upper* bound on the zero side (the
CE/Odlyzko direction, the one used in discriminant and packing bounds). (b) The window form evaluates h = s ∗ s̃ (s ∈ L²(I_T)), for which ĥ = |ŝ|² ≥ 0
but h(log n), n ∈ N_T, has no sign. A CE-type lower bound needs h ≤ 0 on N_T; it therefore yields Weil-positivity only on the cone
C₋ = {s : (s∗s̃)(log n) ≤ 0 ∀ n ∈ N_T}, and there only the inequality form ≥ polar + Arch, with Arch indefinite (CA_K, K-A: C₀ < 0).
*Proof.* (a), (b): sign bookkeeping in the explicit formula; v_n ≥ 0. ∎
So (V2) fails: the prime Dirac comb enters with weight −v_n, and the CE sign mechanism (positive combs on both sides) has no instance. (Seed L3:
DISCARD; L7 (Cohn–Gonçalves) bounds a sign-change radius of a single function, not a quadratic form; comb-generic: DISCARD.)

## 4. Modular-data genericity (the Epstein test)
Viazovska's (V3) uses only: weight, level, character, the Fourier/modular transformation law and finitely many constant terms.
**Definition 4.1.** A *modular-data construction* is a rule 𝔐 which, from the data 𝔇 = (gamma factor, conductor N, root number, pole order and
residue at s = 1, the space M_k(Γ₀(N),χ) in which the theta series lies) and the window T, outputs a dual point (ν, β) (or a sequence), without
using the individual Fourier coefficients of the theta series.
**Theorem 4.2 (NO-GO for modular-data constructions at level 20; PROVED modulo CITED class-group facts and the corpus Epstein falsifier).** Let
Q₁ = x² + 5y², Q₂ = 2x² + 2xy + 3y² (the two classes of discriminant −20). ζ_{Q₁}, ζ_{Q₂} and ζ_{ℚ(√−5)} share 𝔇 (gamma factor (2π)^{−s}Γ(s),
conductor 20, root number +1, a simple pole with the same residue — the residue of an Epstein zeta depends only on the discriminant;
θ_{Q_i} ∈ M₁(Γ₀(20), χ_{−20}), θ_{Q₁} − θ_{Q₂} a cusp form; CITED: Hecke, Siegel). A modular-data construction certifying the window form of
ζ_K for all T certifies that of ζ_{Q₁}, whose full form is negative (P46 O10, Remark twohalves; corpus Epstein falsifier). Contradiction; so no
modular-data construction certifies ζ_K, and any successful construction must use the coefficients (the Euler/Hecke data) at the sign step.
*Proof.* 𝔐 sees identical inputs for ζ_K and ζ_{Q₁}; a dual point is a certificate for a form only through that form's symbol, but 𝔐's output is
claimed valid for every function with data 𝔇; a certificate for a negative form does not exist (weak duality). ∎
**Point (level 1, Hamburger).** For ζ itself the data 𝔇 = (Γ_ℝ, N = 1, ε = +1, simple pole) *determine* ζ among Dirichlet series of finite
order (Hamburger 1921, CITED). So Thm 4.2 does not transfer verbatim to level 1: there is no Epstein partner with ζ's data. But Hamburger's
uniqueness uses the Dirichlet-series shape (support ℤ, i.e. the comb log n) — the *lattice* — so a level-1 modular construction would have
to use: modularity (FE), the support ℤ, and (for O8/O9, FE-preserving non-Dirichlet deformations f_t = ζ + tg and ξR) the coefficient
values. Such a construction is not modular-data-only; it is a construction on the comb, and the comb is where §1–§3 apply. **Verdict L2:
NO-GO for the modular-data class (PROVED at level 20; at level 1 reduced to a comb construction, which inherits Thm 1.1 and class (D)).**

## 5. Mellin vs Fourier: where + and · enter (PRINCIPIO RECTOR)
Viazovska's positivity is Bochner positivity in the *additive* variable x ∈ ℝ^d of the lattice; her vanishing set is |x|² ∈ 2ℕ (additive,
quadratic). Row D's positivity is Bochner positivity in u = log x (multiplicative group ℝ₊^×); the comb is log n. The Mellin transform
θ ↦ ξ is how ℤ (lattice), FE (modularity) and Euler (Hecke) meet, but it does not intertwine the two positive cones: a function PD in x is not,
in general, PD in log x (ARGUED: e.g. e^{−πx²} restricted to x > 0, read as φ(u) = e^{−πe^{2u}}, tends to 1 as u → −∞ while φ(0) = e^{−π} < 1,
so φ is not PD on ℝ_u). The CE/Viazovska sign lives on the additive side; row D's on the multiplicative side; the meeting point is exactly
the explicit formula, i.e. thm:Z — the zero side. This is the precise sense in which "Viazovska's success does not transfer" (complementing
P35-4: interpolation needs μ(ℝ) = ∞ on {γ}).

## 6. Self-review
- Thm 1.1 is P46 thm:O; the only new content is the LP reading (slackness set = ℝ) and the comparison (V1). Correct, not new mathematics.
- Prop 3.1(b) does not prove that C₋ misses negative directions; it records that the CE inequality is one-sided and covers only C₋. Fine.
- Thm 4.2 depends on the Epstein falsifier as recorded in P46 O10; I did not re-derive the negative value. Label: PROVED conditional on corpus fact (CITED).
- Hamburger caveat is genuine: Thm 4.2 does **not** exclude a level-1 construction by itself; the exclusion at level 1 goes through Thm 1.1 + class (D).
- §5 example: φ(u) = e^{−πe^{2u}} → 1 as u → −∞ while φ(0) = e^{−π} < 1, violating |φ(u)| ≤ φ(0); correct.
**Verdicts:** L1 NO-GO (PROVED); L2 NO-GO for modular-data class (PROVED, level 20) / reduced to comb constructions (level 1); L3, L4, L7, L9 DISCARD.
