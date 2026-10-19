# R157_005 — The one-round test Lemma P157.S1 on (P152.2), the Berkovich-line difference kernel

*Phase 157, round 1, No computation was run. No sign is claimed for ζ at any window, in
either form. Row D has no label and nothing here changes a label. Papers and READMEs were not edited. The form is
stated each time: **primitive** = `λ^A_T = λ_min(A_T|P_T)`, **complete** = `λ^W_T` (the Weil form on `L²(I_T)`).*

Sources read for this memo: `R157_000` (filters F1–F5); `R157_002` §1.2 (O1–O4), row 26a/26b, §5 (Lemma P157.S1);
`R152_001` §3 (B.0–B.4); `R152_002` §4.2–4.3 (the auditor's formulation of (P152.2) and gates g1–g3); `R152_005`;
Paper 47 `main.tex` `def:W`/`eq:nuw`, `thm:Z`/`eq:fw`, `thm:SC`, `cor:SC1`, `thm:finmod`, `cor:void`; Paper 46
`main.md` Lemma 12.4A, Thm 12.4, Restatement 12.4a/12.4a′, §27.4 (H-DMV, BE1–BE8, Remark 27.16), import (X31);
phase 114 `114_d_195_CONTACT_GNS_POISSON_CP_AND_TATE_JET_DEFECT.md` §3; `MAP_1_WALLS_AND_MASTER_DOCS.md` l.48 (NG-E1).

---

## §0 Verdict

**EXCLUDED, by clause (b).** Clause (c) excludes independently the only branch that carries a structural sign.
Clause (a) excludes independently every branch whose weights are attached by hand.

**[amended per R157_006, B1]** This memo was written against the *unamended* Lemma P157.S1. Under R157_004 (A19–A22)
clause (b) is not an exclusion criterion, because `W = Σ_v Q_v` already. The verdict is therefore: **(P152.2) CLOSED,
no survivor, category EQUIV (restatement), not EXCL-by-(b).** Every realization in the enlarged class 𝔄⁺ (R157_006
§2.3) that reproduces `W` is the explicit formula on the skeleta, D.195 (3.5) (≡ `RD_T`), a finite-prime form, or P47's
dual problem (D) on the norm line. The positivity *mechanisms* are excluded by (b′) (local/finite-`S` inference), by
the (a) schema (`cor:void` + `thm:finmod`(ii), derivations) and by the (c) schema (P46 Prop 12.4B + Hardy,
derivations). (d) is not reached. In the table below, read "(c) … ⇒ excluded" as "model-uniform derivations
excluded", and read "Lemma 4.8" as FRL **Prop 4.5, eq. (23)**.

| clause | answer | label |
|---|---|---|
| (a) definability for Beurling systems and for `ζ·E` | **Split.** Poineau's space needs the Banach ring `(Z,|·|_∞)`, so it does *not* exist for a Beurling system. But every construction that reaches `W` factors through data that do exist there (Lemma 5.1). **Yes** in factored form for weights-by-hand constructions ⇒ excluded (`thm:finmod`, `cor:void`; T3 modulo (H-DMV)). **No** for purely geometric constructions. Those go to (b) and (c). | PROVED (factorization); the split is exhaustive only within class 𝔄 |
| (b) locality: `𝓔 = Σ_v 𝓔_v` | **Yes, within class 𝔄** (Theorem 4.1). The additive group law of `A^{1,an}_Z` is *relative* to `M(Z)` (Lemma 2.1), so difference kernels see only same-fibre pairs. Across fibres, the only canonical data are (i) the base `M(Z)`, a tree, which gives Prop B.3's meet regime, and (ii) global sections with the product formula. (ii) is **the** cross-place coupling. It produces exactly the prime comb's cross terms (Lemma 3.2), and it produces them as the Weil local decomposition `Σ_v Q_v` on the common norm line, which is (b). | PROVED within 𝔄; "𝔄 exhausts the cited literature" is a survey claim, CITED/HEURISTIC |
| (c) `Ξ_a`: defined and `⪰ 0`? | **Defined: yes.** The `Ξ_a` weights are evaluations at the points `ε = ½ ± a` of the same branches of `M(Z)` (Lemma 6.1). **`⪰ 0`: yes for every structurally positive 𝓔 ∈ 𝔄** (FRL Prop 2.6/Lemma 4.8 local energies, tree kernels). That branch would prove a false statement for `Ξ_a` (P46 Thm 12.4) ⇒ excluded. The non-structural branch carries no sign and is (b). | defined: PROVED; `⪰0` for the structural branch: PROVED; the transfer of a *derivation*: RESTATEMENT (schema, as P46 Restatement 12.4a) |
| global constraint from the product formula: can it create `thm:SC`'s collective positivity? | **No.** On test-function measures it acts only as (i) the identification of all local value lines with one norm line, which is already built into `W = Σ_v Q_v`, (ii) the divisor-sum identity `log = 1∗Λ` on integer sections (Lemma 3.1), and (iii) a degree-zero condition whose Weil counterpart is primitivity `P_T`. `P_T` does not depend on which primes are present, and `thm:SC` is already stated on `P_T`. | PROVED for (iii); (i), (ii) are RESTATEMENTS (identities) |

**Survival test (the lemma's last clause).** One can name the step where the global structure couples the
branches **[amended per R157_006, B4: together with the global function `ℓ = −log|T|`, of which the `ℓ_v` are the
restrictions]**: the product formula along integer sections, `ℓ_∞(σ_n) = Σ_p ℓ_p(σ_n)` (Lemma 3.2). That coupling does
produce the prime comb's cross terms. But it produces them as the Weil local decomposition itself, a sum of
per-place difference-kernel forms `Q_v` of one common `f`, each of which is indefinite (Lemma 3.3). The candidate
therefore meets the survival condition's *second* half and fails its first ("(b) fails") **[amended per R157_006,
B1: read "supplies no independent positivity input: a restatement"]**. **Mechanism B is dead
for the full Q5 of phase 152, not just for the tree.** This settles the auditor's prediction in `R152_002` §4.2
("the explicit formula written twice") with a proof inside class 𝔄. What remains open is exactly the exhaustion
claim about 𝔄 (§8, doubt 1).

---

## §1 Corpus grep (first, as the rule requires)

Counts (files, `.md/.tex/.txt`, `.bak` excluded, over `03-research/ 04-papers/ 05-meta-and-planning/ 00-references/`):
Berkovich 16 · Poineau 9 · Thuillier 5 · Chambert-Loir 5 · Rumely 2 · Fekete **0** · Chinburg **0** ·
Favre / Rivera-Letelier **0** · "adelic energy/measure" 2 · Arakelov–Green 4 · capacity 191 (overwhelmingly
operator/shorted capacity, not arithmetic capacity).

What the hits contain:
* The Berkovich/Poineau/Rumely hits are all in the phase 151–157 planning chain and `AUDIT_A_CATEGORY_CHANGES.md`
  ("no Berkovich space over `Spec Z` … built anywhere"). **Nothing beyond `M(Z)` was ever built.** `A^{1,an}_Z` is
  named only in `R152_002` §4.2, `R152_005` §2 and `R157_002` §5.
* The four `00-references` hits are Berkovich papers over a *fixed* valued field (tropical Hodge theory,
  specialization, Hodge index), not over `Z`.
* **The one substantive precedent.** Phase 114 D.195 §3, eq. (3.3)–(3.5), and D.196 already wrote row C's
  quadratic form as an *adelic energy*: `B_P = A_P I − 𝓔_P`, with
  `𝓔_P = L_∞ + Σ_{p∈P} log p · c_p (I − M_p)` a sum of **nonnegative local Dirichlet forms** (Poisson–Markov at each
  `p`, the Gamma jump generator at `∞`) and `A_P = m_0 + Σ_p log p (c_p − 1)` a global constant. The desired
  inequality `𝓔_P ≥ A_P` on the primitive space is recorded there as "exactly the global Poincaré/shorted-capacity
  statement equivalent to row D". This is the capacity-theoretic shape that any Arakelov–Green energy on
  `A^{1,an}_Z` lands on (§4.2). It was built in phase 114. It was never connected to Berkovich language, and that
  connection is the only new thing needed here.
* Grep over phases 153–156 for the test of (P152.2): 0 hits (confirming `R157_002`).

---

## §2 The object, as explicitly as the literature permits

**(2.0) Facts about `A^{1,an}_Z`.** CITED from J. Poineau, *La droite de Berkovich sur Z*, Astérisque **334**
(2010), and Lemanissier–Poineau, *Espaces de Berkovich globaux* (the primary texts were not re-read here; the
fibre description is standard and is the one used by the auditor in `R152_002` §4.2).
* `A^{1,an}_Z` is the set of multiplicative seminorms on `Z[T]` whose restriction to `Z` is bounded by `|·|_∞`.
  Restriction to `Z` gives `π : A^{1,an}_Z → M(Z)`.
* The fibres are: over `|·|_∞^ε` (`0 < ε ≤ 1`), `C/conj` with the norm `|·|^ε`; over `|·|_p^ε` (`0 < ε < ∞`), the
  Berkovich line `A^{1,an}_{Q_p}` (rescaled); over the end `ε = ∞` of the `p`-branch, `A^{1,an}_{F_p}` with the
  trivial norm; over the root `|·|_0`, the line over `Q` with the trivial norm.
* Every `α ∈ Z` (more generally every Galois orbit in `Q̄`) gives a continuous section `σ_α` of `π`.

**(2.1) Potential theory in the literature. What is fibrewise and what is global.**
* *Local Arakelov–Green energies.* CITED: Favre–Rivera-Letelier, *Équidistribution quantitative des points de
  petite hauteur sur la droite projective*, Math. Ann. **335** (2006) 311–361 (arXiv math/0407471, checked this
  round). Local mutual energy `(ρ,ρ′)_v = −∬_{z≠w} log|z − w|_v dρ dρ′` (their eq. (7)). The height is
  `h_ρ(F) = ½ Σ_{v∈M_K} (([F]−ρ_v, [F]−ρ_v))_v` (their Def. 1.2 and eq. (3)), and **the product formula is used
  exactly once**, to kill the diagonal-excluded self-energy of the global point set `F`. Positivity: at
  archimedean `v`, `(ρ,ρ) = ∫ dg ∧ d^c g ≥ 0` for mass-zero `ρ`, with equality iff `ρ = 0` (their Prop 2.6); at
  non-archimedean `v`, the Berkovich analogue on mass-zero measures (their Lemma 4.8). Same structure: Baker–Rumely
  (Hsia kernel, Arakelov–Green functions on `P^{1,an}_{C_v}`), Thuillier's thesis, Chambert-Loir (Crelle 2006).
  These are CITED from standard knowledge and were not re-read.
  **[amended per R157_006, B2]** Checked in math/0407471: the adelic height is Def. 1.2, **eq. (4)**. Eq. (3) is the
  naive-height identity, derived just before using the product formula. Non-archimedean positivity is **Prop. 4.5,
  eq. (23)** (`(ρ,ρ) = ∫_{H_p} f_ρ² dλ`). Lemma 4.8 is a regularization lemma. The non-archimedean kernel is the Hsia
  kernel `log sup{S,S′}` (Lemma 4.4, eq. (22)), not a function of a difference.
* *Global capacity.* Cantor; Rumely, *Capacity theory on algebraic curves*, LNM 1378; Chinburg–Rumely. The global
  capacity is the **product of local capacities**, `γ(𝔼) = Π_v γ_v(E_v)^{n_v}`, and Fekete–Szegő is a threshold
  statement `γ(𝔼) ≶ 1` about algebraic point sets. CITED from standard knowledge, not re-read. Its outputs are
  finiteness/existence statements about point sets, i.e. class-type inequalities.
* *Genuinely over `Z`.* CITED from abstracts checked this round: Poineau, *Dynamique analytique sur Z. I: Mesures
  d'équilibre sur une droite projective relative*, arXiv 2201.08480 (J. Inst. Math. Jussieu). For a polarized
  endomorphism of the relative projective line over a good Banach ring (including `Z` and `O_K`), the **family of
  fibrewise equilibrium measures is continuous** over the base. The global content is continuity of a fibrewise
  family. Also J. S. Morrow, *Global pluripotential theory for adelic line bundles*, arXiv 2507.10410 (abstract
  only): an equivalence between adelic line bundles and metrized line bundles on global Berkovich
  analytifications. Whether its energies are sums of local energies is **not stated in the abstract**, so this is
  doubt 1 (§8).
  **[amended per R157_006, B2]** Read in full (R157_006 §2.1). Morrow has **no energy**. It has fibrewise
  Monge–Ampère measures (§7.1) and a "global" measure that is their disintegration against a hand-chosen base
  measure on `M(Z)` (weights `1/(p log p)`, eq. (8.1.0.1), Def. 8.2.1). Its cross-fibre data are continuity,
  norm-equivariance (Def 3.1.3(2)) and global sections (tropical Fubini–Study metrics, Def 3.3.1). Poineau Dyn-I
  pairs measures only fibre by fibre (Cor. D). Lemanissier–Poineau (arXiv 2010.08858) contains no potential theory.
  Chambert-Loir (arXiv 1001.2517 §3.4.1) has one non-local term, `−2ĥ_NT`, and it vanishes in genus 0.

**(2.2) The candidate, written out.** The constructions the literature permits have the following shape. A
*place set* `S ⊂ M(Z)` (for Weil: one point on each branch, `s_p = |·|_p^{ε_p}`, `s_∞ = |·|_∞^{ε_∞}`). A linear
map `f ↦ μ_f = (μ_{f,s})_{s∈S}`, with `μ_{f,s}` a (signed) measure on `π^{-1}(s)`. A kernel of the form

    g(x,y) = 1_{π(x)=π(y)} g_{π(x)}(x,y)  +  h(π(x),π(y))  +  G(x,y)·1_{x,y ∈ Σ}                          (2.1)

Here `g_s` is a fibrewise kernel (a difference kernel `k_s(x−y)` from the group law, or an Arakelov–Green / Hsia
kernel), `h` is a kernel on the base, and `Σ = ⋃_α σ_α(S)` is the set of values of global sections, `G` being any
function of the pair of global points `(α,β)` and the pair of places. The energy is `𝓔(f) = ∬ g dμ_f dμ̄_f`,
possibly restricted to a subspace cut out by global linear constraints (mass/degree zero, product formula).
**Class 𝔄** := all energies of this form. The auditor's (P152.2) ("difference kernel along the archimedean fibre,
meet kernel across branches") is the sub-case `G = 0`, `h = κ(s∧s′)`.

**Lemma 2.1 (the group law is relative; PROVED).** The additive law of `G_a^{an}` over `Z` is a morphism
`m : A^{1,an}_Z ×_{M(Z)} A^{1,an}_Z → A^{1,an}_Z` over `M(Z)`. In particular a point of the source has two
projections with the same image in `M(Z)`, and no difference `x − y` is defined for `π(x) ≠ π(y)`.

*Proof.* `A^{1,an}_Z ×_{M(Z)} A^{1,an}_Z = A^{2,an}_Z`: its points are multiplicative seminorms on `Z[T_1,T_2]`
bounded on `Z`. The restriction to `Z ⊂ Z[T_i]` is one seminorm, so both projections lie over one point of
`M(Z)`. The addition is induced by `Z[T] → Z[T_1,T_2]`, `T ↦ T_1 + T_2`, which is `Z`-linear, so it commutes
with `π`. ∎

**[amended per R157_006, B3]** The equality `A^{1,an}_Z ×_{M(Z)} A^{1,an}_Z = A^{2,an}_Z` holds in the **category**
of `Z`-analytic spaces (Lemanissier–Poineau Thm 4.3.8). It does **not** hold as sets: the map to the set-theoretic
fibre product is surjective but not injective. Over `|·|_∞` the fibre is `C²/conj ≠ (C/conj)²` (Poineau
0809.2880). Over a pair of Gauss points lie both the bidisc Gauss norm and `P ↦ |P(T,T)|`. The proof above
establishes exactly what is used: every point of `A^{2,an}_Z` lies over one point of `M(Z)`, and `m` is over
`M(Z)`. `x − y` is a map on `A^{2,an}_Z`, not on pairs of points. A "difference kernel" on pairs is a
symmetrization or a choice (the two lifts on `C/conj`, the Hsia kernel non-archimedean). The exception is
`k(ℓ(x) − ℓ(y))`, read through the multiplicative law and the global function `ℓ`, which is defined on all pairs
(R157_006 §3).

So any "difference kernel" on `A^{1,an}_Z` is supported on the fibre diagonal `{π(x) = π(y)}`. This is the
precise sense in which the group object `A^{1,an}_Z` does **not** escape Prop B.3. Its translation structure is
fibrewise, and the cross-fibre part of any kernel must come from somewhere else. That is why (2.1) has three terms.

**Lemma 2.2 (canonical cross-fibre data; PROVED for the list, survey for exhaustion).** Two points `x, y` over
distinct `s ≠ s′` are related by exactly two canonical kinds of data: through the base (`s, s′` and the tree
structure of `M(Z)`, including the topology near the root, where all branches meet), and through global sections
(`x = σ_α(s)`, `y = σ_β(s′)`). Everything else (an isomorphism `Q̄_p ≅ C`, a choice of embeddings) is
non-canonical. The list is proved from (2.0). That the cited constructions use nothing else is a survey claim over
§2.1 (CITED / HEURISTIC). Poineau's Dyn-I uses the base topology (continuity in `s`), and FRL/BR/CL use global
point sets with the product formula.

**[amended per R157_006, B4] Lemma 2.2 FAILS as stated.** Two further kinds of canonical cross-fibre data exist.
(1) **Global functions**: `x ↦ |P|_x` for `P ∈ Z[T]`, in particular `ℓ = −log|T|`, which is defined on pairs over
different places. (2) **The scaling flow** `x ↦ x^ε` along a branch (Poineau's `Φ_ε`, Morrow's norm-equivariance).
Also, `M(Z)` is a tree as a set, but its topology at the root is strictly coarser than the tree topology (Poineau
0809.2880). R157_006 §2.3 enlarges 𝔄 to 𝔄⁺ and closes the new branches. Flow kernels are branch-local (Lemma B.1).
Finitely many global functions distinguish only finitely many primes on the skeleton (Lemma B.2 → (b′), `thm:SC`).
Norm-line kernels `H(ℓ(x) − ℓ(y))` are P47's dual problem (D) (Lemma B.3, RESTATEMENT), and the (a) schema applies to
them.

---

## §3 The product formula is the cross-place coupling, and it produces the comb

**Lemma 3.1 (Λ from the geometry; PROVED, elementary).** For an integer `m ≠ 0`:
(i) `−log|m|_p = Σ_{k≥1} Λ(p^k) 1[p^k | m]`. So the `p`-adic Green kernel `−log|x−y|_p` on integer points is a sum
over congruence levels, each level weighted by `Λ(p^k) = log p`.
(ii) The product formula `log|m|_∞ + Σ_p log|m|_p = 0` is the identity `log m = Σ_{d|m} Λ(d)`, i.e. `log = 1∗Λ`.
(iii) `Λ = Σ_p Λ_p` with `Λ_p := μ ∗ (−log|·|_p)`, and `Λ_p(n) = log p · 1[n is a power of p]`.

*Proof.* (i) `−log|m|_p = ord_p(m) log p = Σ_{k≤ord_p m} log p`. (ii) Sum (i) over `p`. (iii) `−log|·|_p =
log p · ord_p` is additive, and for additive `φ`, `μ∗φ` is supported on prime powers with
`(μ∗φ)(q^j) = φ(q^j) − φ(q^{j−1})`. For `φ = ord_p` this is `1` if `q = p` and `0` otherwise. ∎

Reading. The geometry of `A^{1,an}_Z` (its `p`-adic Green kernels at integer sections) *does* produce exact `Λ`,
without a weight inserted by hand. F1 is satisfiable intrinsically. But it produces `Λ` in two ways only: through
the additive variable `x − y` (congruences), and through the global identity `log = 1∗Λ`. Neither is a sign
input. (ii) is an identity (the filter's "identity" item, `R157_002` row 30 region), and (iii) is a per-place
decomposition.

**Lemma 3.2 (the coupling step, named; PROVED).** Let `ℓ_v(x) := −log|T(x)|_v` (the skeleton coordinate of
`G_m^{an}` in the fibre over `|·|_v`). For every integer section, `ℓ_∞(σ_n) + Σ_p ℓ_p(σ_n) = 0`, so
`log n = Σ_p ord_p(n) log p`. For `n = p^k` the archimedean coordinate of `σ_{p^k}` and its `p`-adic coordinate
coincide up to sign, and both equal `k log p`, the location of the `p`-atoms of the Weil explicit formula.

*Proof.* The product formula, evaluated on `T(σ_n) = n`. ∎

**[amended per R157_006, B6]** At the points `ε_v = 1` (unrescaled absolute values). On the fibre over `|·|_v^ε`,
`ℓ_v` scales by `ε`, and the product formula holds only for the normalized absolute values. "Coincide … both equal
`k log p`" is meant in absolute value.

This is the step the survival clause asks for. The global structure of `A^{1,an}_Z` (sections plus the product
formula) identifies every local value line `log|Q_v^×|_v` with one common line `R`, the log of the idele norm
(`C_Q/C_Q^1 ≅ R_{>0}`). On that line the prime atoms of all places sit together, and a single test function `f`
is evaluated at all of them. **That is exactly what creates the cross terms** `f(u) f̄(u − k log p)` of
`W(f∗f̃)`. The coupling exists, it is canonical, and it matches the comb.

**Lemma 3.3 (what the coupling produces: the Weil local decomposition, with indefinite summands; PROVED).** With
`g = f∗f̃` and the normalization of P47 `eq:fw`, `W(g) = Q_∞(f) + Σ_p Q_p(f)`. Here
`Q_p(f) = (2π)^{-1} ∫ |f̂(τ)|² σ_p(τ) dτ`, with
`σ_p(τ) = −Σ_{k≥1} v_{p^k} cos(kτ log p)` and `v_{p^k} = 2 log p · p^{−k/2}`. Q_∞ collects the archimedean term,
the constant and the pole terms. Each `Q_p` is a difference-kernel form in the common variable `u ∈ R`. For every
`p` and every `T` with `2T > log p`, `Q_p` restricted to `C_c^∞(I_T)` (with the comb truncated to `k log p < 2T`,
as `eq:fw` does automatically for `supp g ⊂ (−2T,2T)`) is **negative definite on subspaces of every finite
dimension** (in both the complete and the primitive form).

*Proof.* The decomposition is `eq:fw` regrouped by the prime of `n = p^k`, which is Weil's local decomposition.
As a quadratic form, `Q_p(F) = −Σ_{k: k log p < 2T} v_{p^k} c_F(k log p)` with `c_F` the autocorrelation (the
convention of P47 `thm:finmod`(ii), where the comb enters as `−(2c/√n_0) c_F(log n_0)`). Put `u_0 = log p < 2T`.
Following the construction in the proof of P47 `lem:cpos`, choose `0 < ℓ < min(u_0, 2T − u_0)` and
`J = (−T, −T + ℓ)`, so that `J, J + u_0, J + 2u_0, J + 3u_0` are pairwise disjoint and `J ∪ (J + u_0) ⊂ I_T`. For
real `φ_1, …, φ_m ∈ C_c^∞(J)` with pairwise disjoint supports, put `F_j = φ_j + φ_j(· − u_0)`. Then
`c_{F_i,F_j}(u_0) = ⟨φ_i,φ_j⟩ = δ_{ij}‖φ_j‖²` and `c_{F_i,F_j}(k u_0) = 0` for `k ≥ 2`, by disjointness. So
`Q_p(Σ x_j F_j) = −v_p Σ x_j² ‖φ_j‖² < 0` for `x ≠ 0`, and `Q_p` is negative definite on an `m`-dimensional subspace
of `C_c^∞(I_T)`. Intersecting with `P_T` costs codimension `≤ 2`, so the same holds in the primitive form for
`m ≥ 3`. ∎

*(This is NG-E1, the computed indefiniteness of the per-place forms, now proved for every `p` and every
`T > ½ log p` by `lem:cpos`'s device. `Q_p` also has positive directions: use `F_j^- = φ_j − φ_j(· − u_0)`.)*

**[amended per R157_006, B5]** Signs and truncation verified against P47 `eq:A`/`thm:finmod`(ii): PASS. Two
simplifications. (i) `J + 3u_0` is superfluous, since `ℓ < u_0` already makes all translates `J + ku_0` pairwise
disjoint. (ii) Disjoint supports are unnecessary: `Q_p(F_φ) = −v_p‖φ‖²` for **every** `φ ∈ C_c^∞(J)`, so `Q_p` is
negative definite on the infinite-dimensional subspace `{F_φ}`, and on its intersection with `P_T` (codimension `≤ 2`).
Under (b′) (R157_004 A20) this is corroboration, not an exclusion: indefinite summands do not forbid a positive sum.

---

## §4 Clause (b): locality

**Theorem 4.1 (decomposition in class 𝔄; PROVED).** Every `𝓔 ∈ 𝔄` has the form

    𝓔(f) = Σ_{s∈S} 𝓔_s(μ_{f,s}) + Σ_{s,s′} h(s,s′) m_s(f) m̄_{s′}(f) + 𝓖(f) ,   m_s(f) := μ_{f,s}(π^{-1}(s)),     (4.1)

with `𝓔_s` the fibrewise energy of `g_s`. The middle term is a quadratic form in the fibre masses, one linear
functional per place. `𝓖` is supported on pairs of global points. If the `μ_{f,s}` are absolutely continuous in
the fibres (as they must be for `f ∈ C_c^∞`, and not atomic at sections), then `𝓖 = 0`: the product-formula
coupling enters `𝓔` only through the *definition* of `μ_{f,s}` (where its mass is placed), i.e. through
Lemma 3.2's identification of the value lines.

*Proof.* Insert (2.1) into `∬ g dμ_f dμ̄_f`. Lemma 2.1 puts the first term on the fibre diagonal, where it is the
sum over `s` of fibrewise energies. The second depends only on base points, so it integrates to the mass form.
The third lives on `Σ × Σ`, a countable set, which is null for measures without atoms at sections. ∎

**[amended per R157_006, B6]** Replace "absolutely continuous in the fibres (as they must be for `f ∈ C_c^∞` …)" by
"**without atoms on `Σ`**". Nothing forces absolute continuity, and the skeleton measures of §4.2 are not absolutely
continuous, but they charge no type-I section value. The class must be 𝔄⁺ (R157_006 §2.3): add the global-function /
norm-line term `𝓣` and the branch-local flow kernels. Theorem 4.1 is then PROVED within 𝔄⁺. Its content is a
classification **by restatement**, not an impossibility theorem.

If the `μ_{f,s}` *are* atomic at the sections `σ_{p^k}(s)` (the "Dictionary B.1" choice, with weights), then
`𝓖` is a quadratic form in the finitely many atom values `f(k log p)`, `k log p < 2T`, with `G(α,β)` a function
of pairs of integers. By Lemma 3.1 the only canonical such `G` built from the product formula is
`Σ_v n_v log|α − β|_v = 0` (FRL's use). So `𝓖` is identically zero, or it is a kernel on integer pairs chosen by
hand, and then (a) applies to it.

**4.2 Consequence for (b).** (4.1) is a sum of per-place energies plus a base-mass term. Two cases.

* *Fibrewise energies match the local forms, `𝓔_{s_v}(μ_{f,v}) = Q_v(f)`.* Then (b) holds on the nose, and 𝓔 is
  the explicit formula written on the skeleta. The realization exists: push `f(u)du` to the `G_m`-skeleton of each
  fibre via `ℓ_v` and use the multiplicative difference kernel `W_v(ℓ_v(x) − ℓ_v(y))`. It is an identity with no
  sign content. No fibrewise kernel of that form is positive: Lemma 3.3 and NG-E1 say `Q_p` is indefinite.
  **Excluded** (NG-E1; `thm:SC`: no proper sub-family carries the sign, so the positivity of `Σ_v Q_v` is not
  visible in any `Q_v` or finite sum of them).
  **[amended per R157_006, B7] "Excluded" FAILS as a reason.** This case infers no sign. It is the identity
  `W = Σ_v Q_v` on `A^{1,an}_Z`, and its positivity question is `λ^W_T ≥ 0` itself. Label: RESTATEMENT (identity).
  It is not a survivor because it supplies no sign input. (b′) would exclude only an *inference* from the `Q_v`.
* *Fibrewise energies are structurally positive* (FRL Prop 2.6 / Lemma 4.8 type, or tree kernels `κ(s∧s′)`, which
  are of negative type by `R152_001` §B.1, confirmed by `R152_002` §4.2). Then 𝓔 is `⪰ 0` termwise, and matching
  `W` requires a redistribution `D_v := 𝓔_{s_v}(μ_{f,v}) − Q_v(f)` with `Σ_v D_v + (mass term) = 0`. Each
  `D_v ⪰ −Q_v` has infinite positive index (Lemma 3.3). This is exactly the D.195 shape (§1): positive local
  Dirichlet forms `𝓔_P = L_∞ + Σ_p log p c_p(I − M_p)` and a leftover global constant `A_P`, with
  `W ≅ 𝓔_P − A_P`. Positivity of `W` is then the global Poincaré/capacity inequality `𝓔_P ≥ A_P` on the
  primitive space, recorded in D.195 (3.5) as **equivalent to row D**. The sign is not produced by the energy. It
  is moved into a capacity inequality that *is* the question. Note `A_P = m_0 + Σ_{p∈P} 2 log p · r_p/(1 − r_p)`
  grows without bound with `P`: in capacity language the "capacity constant" diverges as `Σ_p log p/√p`, which is
  the `∼ 4e^T` of `cor:SC1` window by window. **Excluded** as a mechanism (termwise sign, F3 via `lem:Rrig`/
  `thm:SC`). What survives is the restatement D.195 (3.5).
  **[amended per R157_006, B7]** (b′) excludes the *inference* "`𝓔_v ⪰ 0 ∀v ⟹ W ⪰ 0`". The construction itself
  reduces to a RESTATEMENT of `RD_T`, not to an impossibility. D.195 (3.5) was re-audited against P47 (R157_006 §7):
  D.195's `B_P` is **minus** the Weil form, and (3.5) is a window statement after compression to `L²(I_T)` (primes
  with `log p ≥ 2T` cancel exactly). With `P ⊇ {p < e^{2T}}`, (3.5) on `P_T` is `RD_T`: PASS. The scale match is an
  identity, not a heuristic: `A_P + C_0 = Σ_{p∈P,k≥1} v_{p^k}` (the untruncated comb mass over `P`), and
  `A_P = 𝒜_T + O(T)` for `P = {p < e^{2T}}`. The `∼ 4e^T` is in the text after `cor:SC1` (B13), not in the
  corollary. Only the reading as a "capacity threshold" is HEURISTIC.

**4.3 Can the global constraint create the collective positivity `thm:SC` requires? (PROVED: no.)** In class 𝔄 the
global constraints are of three kinds.
(i) The identification of value lines (Lemma 3.2). It is already built into `W = Σ_v Q_v` and adds no inequality.
(ii) The divisor-sum identity `log = 1∗Λ` on sections (Lemma 3.1(ii)). It is an equality between two ways of
    writing the same comb and adds no inequality.
(iii) A degree/mass-zero condition, the hypothesis under which FRL's local energies are positive. On the Weil side
    its counterpart is primitivity: `P_T = {F̂(±i/2) = 0}`, the pole conditions coming from global Poisson
    summation.

The constraint in (iii) is defined by archimedean data alone and does not depend on which primes carry weight.
`thm:SC` is **stated on `P_T`**: for every sub-family of contacts with mass `A < −C_0`, the form is negative on
`P_T` for `T > T_0(A)`. So the global constraint is present in `thm:SC`'s hypothesis and does not prevent
sub-comb negativity. A constraint that does not see the difference between the complete comb and a sub-comb
cannot be what makes the complete comb positive.

One could object that the product formula itself fails for proper subsets of places, so it *is* collective. But
it acts on global points `α ∈ Q^×`. A test function `f ∈ C_c^∞(R)` is not a global point, and on `f` the product
formula has no content beyond (i). Its collective character is exhausted by the fact that `R` is the norm line of
*all* places, which `W` already uses. ∎

**[amended per R157_006, B8]** (iii): `P_T = {A = B = 0}` is cut out by the **polar** data (the pole of ζ), not by
"archimedean data alone". What matters is that it is independent of the prime weights, and that holds. For `Ξ_a` the
constraint has four conditions (P46 Lemma 12.4A). The PROVED part is: restriction to `P_T` does not by itself yield
positivity (`thm:SC` is stated on `P_T`). The last paragraph ("on `f` the product formula has no content beyond
(i)") is HEURISTIC.

**Verdict (b): YES within 𝔄 ⇒ EXCLUDED.** Label: PROVED within class 𝔄. That 𝔄 contains every construction in
the cited literature is CITED (FRL checked; BR, Thuillier, CL, Rumely, Chinburg–Rumely from standard knowledge;
Poineau Dyn-I and Morrow from abstracts). HEURISTIC for Morrow 2025.

---

## §5 Clause (a): definability

**Lemma 5.1 (factorization; PROVED).** Let `𝓔 ∈ 𝔄` satisfy `𝓔(f) = W(f∗f̃)` on `C_c^∞(I_T)` for all `T`, with
`μ_{f,v}` placed via `ℓ_v` (as Lemma 3.2 forces for the atoms to sit at `k log p`). If the weights of `μ_{f,v}` are
attached by hand (numbers `a(p^k)p^{−k/2}` not produced by the fibre geometry), then `𝓔` depends on the fibre over
`v` only through (log `N v`, the value lattice `Z log p`, the weights). Hence the same formula defines `𝓔_𝒫` for
every Beurling system (local term at `q_j` with lattice `Z log q_j`) and for every `ζ_a = ζ·E` of `thm:finmod`
(weight `log 2 + c` at `n_0 = 2`).

*Proof.* A skeleton-supported measure and a difference kernel along `ℓ_v` depend on the fibre only through `ℓ_v`'s
image and the kernel's values, i.e. through `R` with its lattice. The weights are inputs. ∎

Then `thm:finmod`(ii) at `n_0 = 2`, `c > c_*`, gives a member of the class for which the same formula would
certify a false `RD_T`. So the derivation "𝓔 ⪰ 0 by construction" cannot exist (`cor:void`, closure under
amplification, every `T > ½ log 2`). With (H-DMV): T3, METHOD-CONSTRAINT modulo the CITED (secondary source)
import. The `thm:finmod` exclusion is unconditional; the T3 one is conditional.
**[amended per R157_006, B8]** Per R157_004 A19, T3 is supplementary. It applies only with a bridge
"`𝓔_𝒫 ⪰ 0 ⟹ (ZFS_δ)`", which does not exist for DMV. The primary exclusion (of *derivations*) is `cor:void` +
`thm:finmod`(ii).

**Purely geometric constructions.** If the weights are produced by the geometry (Lemma 3.1: `log p` from the
Green-kernel levels, `Λ = Σ_p μ∗(−log|·|_p)`), the construction uses the ring `Z` and is **not** defined for a
Beurling system (no Banach ring, no fibres, no sections). It is also not defined for `ζ·E`: no ring has
`log 2 + c` as its Green level. So (a) **fails** for this branch, as `R157_002` §5 predicted. But the geometry
produces only the `log p`. The factor `p^{−k/2}` is not a Green-kernel datum. It is `|p^k|_p^{1/2}`, an evaluation
at the point `ε = ½` of the `p`-branch of `M(Z)`, a slice chosen by hand (the fixed point of `s ↦ 1 − s`). That is
the entry point of (c).

**Verdict (a): split.** PROVED: yes (excluded) for weights by hand; no for purely geometric weights, which pass to
(b) (§4, excluded) and (c) (§6).

**[amended per R157_006, B9]** The split is exhaustive once "geometric" is defined: weights that are values of
canonical functions on `A^{1,an}_Z` (Green kernels, evaluations at points of `M(Z)` or of fibres). Everything else is
by hand. "(b), §4, excluded" should read "(b′) or restatement, §4". A derivation using the **single** slice `{½}` is
not model-uniform over `Ξ_a` and escapes (c). It does not escape Theorem 4.1 (case 1 or 2), so it reduces to the
same restatement.

---

## §6 Clause (c): the falsifier `Ξ_a`

**Lemma 6.1 (slices; PROVED).** For `0 < a < ½`, `Ξ_a(s) = ξ(s+a)ξ(s−a)` has
`−Ξ_a′/Ξ_a(s) ⊃ Σ_n Λ(n)(n^{a} + n^{−a}) n^{−s}`. At `s = ½ + iτ` the prime-power weight is
`log p (|p^k|_p^{½−a} + |p^k|_p^{½+a})`: the sum of the evaluations at the two points `ε = ½ ∓ a ∈ (0,1)` of the
`p`-branch of `M(Z)`. That pair is symmetric about `½`, so the functional-equation symmetry does not single out
`ε = ½` against `{½ − a, ½ + a}`. The archimedean factor `Γ_R(s+a)Γ_R(s−a)` is the local Tate integral at the
shifted parameters.

*Proof.* Logarithmic derivative of `ξ(s±a)`. ∎

Hence every construction of §5's geometric branch (Green levels for `log p`, slice for the half-power) is defined
for `Ξ_a` on **the same space `A^{1,an}_Z`**, by moving the slice from `{½}` to `{½−a, ½+a}`. The space does not
distinguish them.

* *Structurally positive branch* (every fibrewise energy FRL-positive on mass zero, `h` of negative type). Then
  `𝓔_{Ξ_a} ⪰ 0` by the same local positivity theorems. If the identity `𝓔 = W` were derived from the explicit
  formula and the geometry, the derivation would read verbatim for `Ξ_a` (its explicit formula is the sum of the
  two shifted ones) and give `W_{Ξ_a} ⪰ 0` on the `Ξ_a`-primitive class. By P46 Prop 12.4B that puts all zeros of
  `Ξ_a` on `Re s = ½`, contradicting Hardy (P46 Thm 12.4). **Excluded.** Label: `𝓔_{Ξ_a} ⪰ 0` PROVED for this
  branch. The derivation transfer is RESTATEMENT (schema), exactly in the sense of P46 Restatement 12.4a/12.4a′.
  It excludes derivations, not functions. A function `𝓔` that equals `W_ζ` by an argument inspecting `ζ` beyond
  the space is not excluded by (c), but then its positivity is not structural, and it falls under §4.2 case 1.
  **[amended per R157_006, B10] FAIL (doubt 5).** Such an `𝓔` is termwise positive by hypothesis. What is
  non-uniform is the *identity* `𝓔 = W_ζ`. It falls under **§4.2 case 2** and is **not excluded**: with the identity
  it would prove `RD_T`, i.e. close D.195 (3.5). Filing it under case 1 would dispose of a function by
  reclassification, which is what P46 Remark 12.4a′ forbids. Also: the contradiction is with **P46 Prop 12.4B +
  Hardy (X16)**, not Thm 12.4 (R157_004 A21). The transferred positivity must hold on a class containing the
  `Ξ_a`-primitive tests (four conditions, Lemma 12.4A). An unconditional `𝓔_{Ξ_a} ⪰ 0` shows only that the identity
  fails for `Ξ_a`.
* *Non-structural branch.* 𝓔 has no sign by construction, so (c) does not apply, and it is the identity of §4.2
  case 1.

**Verdict (c): defined for `Ξ_a`: YES (PROVED). `⪰ 0` for `Ξ_a`: YES on the structural branch (PROVED) ⇒ that
branch is excluded.**

---

## §7 Final verdict and the next lemma

**EXCLUDED.** The decisive clause is (b). Clause (c) independently kills every structurally positive variant, and
clause (a) kills every weights-by-hand variant. The survival condition's naming requirement is met: the coupling
is the product formula along integer sections, Lemma 3.2. It does produce the comb's cross terms, and it produces
them as `Σ_v Q_v`, which is (b). Mechanism B is closed for `A^{1,an}_Z`, not only for `M(Z)`.

What the round adds to the record:
* **Lemma 2.1** (the group law of `A^{1,an}_Z` is relative to `M(Z)`): the reason Prop B.3's conclusion extends
  from the tree to the Berkovich line. PROVED.
* **Lemma 3.1(iii)** (`Λ = Σ_p μ∗(−log|·|_p)`, with the Green levels of the `p`-adic kernel carrying `Λ(p^k)`):
  a RESTATEMENT with a precise geometric reading. Candidate for one remark in Paper 44, next to Dictionary B.1.
  **[amended per R157_006, B11]** Dictionary B.1 (R152_001:266) is **not** in Paper 44. The remark is cleared only
  together with it, if B.1 is added. Label: classical (`Λ = μ∗log` split by primes), no novelty.
* **Theorem 4.1 + §4.2**: every Arakelov–Green / capacity energy on `A^{1,an}_Z` either is the explicit formula on
  the skeleta, or is termwise positive with a leftover capacity constant, which is D.195 (3.5) ≡ row D. This
  connects phase 114's "adelic energy" to the Berkovich literature. It is a restatement, not a mechanism.
* **Lemma 6.1** (`Ξ_a` = slice move `½ → ½ ± a` on the same branches): a clean statement of why the Berkovich
  space cannot see the difference between ζ and `Ξ_a`.

**[amended per R157_006, B12] Clause (d)**, which is missing above. Poineau Dyn-I and Lemanissier–Poineau work over
`O_K`, and Lemma 2.1 and Theorem 4.1 hold verbatim over `M(O_K)`. A positivity derivation would be field-uniform,
so T1 requires GRH for every `ζ_K`: a standard, not an exclusion. No derivation is proposed, so (d) and the Pass
clause (A3 plus one of A7/A8/A9) are not reached. Final verdict per R157_006 §11: **CLOSED, EQUIV (restatement)**.
Clearance per R157_006 §12.

**No next lemma is proposed for (P152.2).** The only unexcluded territory is outside class 𝔄: a cross-fibre kernel
that is neither a base kernel nor a function of global points. Lemma 2.2 says no canonical one exists. Proposing
one would be inventing the candidate. If the exhaustion claim is to be closed, the precise check is to
read Morrow (arXiv 2507.10410) and Lemanissier–Poineau for any global energy on a relative Berkovich line that is
not of the form (4.1). One reading round, no construction.

---

## §8 Doubts for the audit

1. **Exhaustion of 𝔄.** Theorem 4.1 is proved for kernels of shape (2.1). "The literature permits nothing else"
   rests on Lemma 2.2 (canonical cross-fibre data = base + sections) plus a survey. FRL was checked this round.
   Poineau Dyn-I and Morrow 2025 were checked from abstracts only. Baker–Rumely, Thuillier, Chambert-Loir, Rumely
   LNM 1378 and Chinburg–Rumely were not re-read. The weakest point: a kernel using the *topology* of
   `A^{1,an}_Z` near the root fibre (where all branches accumulate) in a way not factoring through `h(s,s′)`.
   I argue it must factor through the base, since the root fibre is itself over one base point, but this is not
   a theorem.
2. **Lemma 3.3's proof.** It reuses the disjoint-support device from the *proof* of P47 `lem:cpos`, with a
   fourth disjoint translate `J + 3u_0` added so that all `k ≥ 2` contacts vanish. Check it against P47's
   comb-sign convention (as in `thm:finmod`(ii)) and against the truncation `k log p < 2T`.
3. **§4.2 case 2 is a reduction, not an impossibility.** Termwise-positive energies plus a redistribution are
   excluded as a *mechanism* only in the sense that the sign moves into D.195 (3.5), which is recorded as
   equivalent to row D. I have not re-audited D.195's equivalence claim, and D.195 predates Paper 47's
   definitions. The identification `A_P ↔ 4e^T` is heuristic (scale only).
4. **(a) "factored" definability.** Lemma 5.1 assumes the atoms are placed via `ℓ_v`. A construction placing mass
   elsewhere and recovering `W` by a non-local identity is covered by (b), not by (a). The auditor should check
   that the case split in §5 is exhaustive.
5. **(c) is a schema.** As P46 Restatement 12.4a′ insists, it excludes derivations, not functions. I have tried to
   state it that way. The auditor should check that I have not used it to exclude a *function*.
6. **Fibre description of `A^{1,an}_Z`.** Taken from the standard account and `R152_002`, not from a re-reading
   of Astérisque 334. Lemma 2.1 uses only the definition of `A^{2,an}_Z` as seminorms on `Z[T_1,T_2]`, which is safe.

---

## §9 Closing paragraph

The Berkovich line over `Z` was the last candidate left unexcluded by the phase-157 search. This round writes down
what the literature actually builds on it and runs the pre-registered test. The finding is simple once seen: the
additive group law of `A^{1,an}_Z` lives *over* the base `M(Z)`, so a difference kernel only ever compares points
at the same place. The only thing that ties places together is the product formula along integer points. That
coupling is real, and it is exactly what puts all the prime atoms on one line where a single test function sees
them all. But what it produces there is Weil's own decomposition of the explicit formula into per-place pieces,
each of which is indefinite. Every energy the potential-theory literature knows how to build (Arakelov–Green,
capacity, equilibrium measures) is a sum of local energies of this kind. When those local energies are made
positive, as Favre–Rivera-Letelier and Baker–Rumely do, the sign moves into a global capacity inequality that the
corpus already wrote down in phase 114 and recorded as equivalent to row D. The space also cannot tell ζ from the
falsifier `Ξ_a`: moving from one to the other is sliding a point along the same branches. So the candidate is
excluded, mainly because the energy splits into per-place pieces. I propose no follow-up construction. The one
residual doubt is bibliographic: whether some recent global potential theory (Morrow 2025, Lemanissier–Poineau)
contains an energy of a different shape. That is one reading round if it is to be closed. With this, the
phase-157 search has no survivor, which is option (A) of the reduced statement. No sign is claimed or suggested
for ζ at any window, in either form.

Sources checked this round (open): arXiv math/0407471 (Favre–Rivera-Letelier; Def. 1.2, eq. (3), (7),
Prop 2.6, Lemma 4.8); arXiv 2201.08480 (Poineau, Dynamique analytique sur Z I, abstract); arXiv 2507.10410
(Morrow, abstract).
