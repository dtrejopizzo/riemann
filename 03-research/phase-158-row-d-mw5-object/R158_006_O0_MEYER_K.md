# R158_006 — Optional follow-up O0: the number-field version of Meyer's spectral realisation and the `S₃` falsifier

Task O0 of R158_004 §5 and R158_005 §3(b). Inputs: R158_002 §4.7 (Lemma U and the `S₃` remark, A20),
R158_004 rows 11, 12, 12′, R158_005 §1. No numerics. No paper, README or earlier R158 file was edited.
**No sign is claimed, asserted or suggested. Row D: no label change.**

## §0 Verdict

| item | label |
|---|---|
| A number-field version of Meyer's construction **exists in the literature**. It is Meyer, Duke Math. J. 127 (2005), arXiv math/0311468, stated for every algebraic number field `K`. The note math/0412277 is `Q`-only and says so | CITED (§1) |
| The **exact** Laplace-range theorem for `K` (the analogue of the note's Thm "Lap_range") is **not** a numbered theorem in the literature. Duke gives the Laplace range of `𝓗_-` (Lemma "Lap_weighted_Sch"), the multiplicity theorem ("difference_spectrum"), and an in-text description of `(Σ𝓗_+^S)^`. The Jordan structure is stated nowhere as a theorem | CITED, with the gap named |
| **Theorem J_K** (§3): on the trivial sector `H¹_{K,1}` of Meyer's `𝓗⁰_-` over any number field `K`, every nontrivial zero `ρ` of `ζ_K` of order `m_ρ` carries a Jordan chain of length exactly `m_ρ`. The chain survives when the range is replaced by its closure (CCM's `H¹`). Within finite-dimensional subrepresentations it is the whole `ρ`-generalized eigenspace, so it is a single Jordan block | **PROVED** from cited definitions, Duke Lemma "Lap_weighted_Sch", Duke Lemma "Poisson_sumpm" and Tate's thesis. The exhaustion clause also uses Duke Thm "difference_spectrum" |
| **Proposition S** (§4): for `K/Q` Galois with group `S₃`, `ζ_K = ζ·L(χ_{−3})·L(ρ)²`. `L(s,ρ)` is entire and has infinitely many nontrivial zeros, at least `(T/π)log T + O(T)` of them up to height `T`. Each one is a nontrivial zero of `ζ_K` of order `≥ 2` | **PROVED** (classical: Artin, Hecke, Landau) |
| **Corollary F** (§5), the `S₃` falsifier: on `H¹_{K,1}`, for any `c ∈ R`, there is no positive-definite hermitian form with `(Θx,y) + (x,Θy) = 2c(x,y)` on any `Θ`-stable subspace that contains one of the chains of Theorem J_K with `m_ρ ≥ 2`. The same holds on CCM's `H¹` and on every realisation into which such a chain injects `Θ`-equivariantly. This holds **whatever GRH says** | **PROVED** (modulo the citations above). Content CLASSICAL in substance: Meyer stated it as a remark in 2005 (§1.1(c)) |
| Upgrade of record: the `S₃` falsifier changes from "`PROVED` modulo `ANALYSIS` (cyclicity)" to **`PROVED`** | proposed for review |
| Scope: the falsifier does **not** apply to Connes' Hilbert realisation `L²_δ` with `1 < δ ≤ 3`, where multiplicity is capped at 1 (§5.2) | PROVED (from Connes Thm 1) |

## §1 Sources opened, and what they say

I fetched the arXiv e-print sources this review into the scratchpad; they were not added to `00-references`.
Line numbers below refer to those sources: `math/0311468` (`Primes_Rep.tex`, Latin-1, 5381 lines), `math/9811068`
(`zeta.tex`), and `math/0703392` (`Yuri70v2.tex`). For math/0412277 I used the local copy
`00-references/papers-nuevos/C/arXiv-math0412277v3`.

**1.1 Meyer, *On a representation of the idele class group related to primes and zeros of L-functions*, Duke Math. J.
127 (2005) 519–595, arXiv math/0311468.** P46 (X33)(ii) lists this paper as "not read"; it has now been read.

* (a) **Scope** (l.181): "Let `K` be an algebraic number field, that is, a finite algebraic extension of … `Q`". At
  l.293: "Although we state most results only for algebraic number fields, they also work with small modifications for
  global function fields."
* (b) **Objects** (l.319–440):
  * `𝓗_+ := S(A_K)/K^×`, the coinvariants.
  * `𝓗_- := S(C_K)_{]−∞,∞[}` (eq. `def_Hilm_m`, l.393), where `S(C)_I = {f : f|x|^α ∈ S(C) ∀α ∈ I}` (l.349).
  * The embeddings `i_+(f) = (Σf, JΣ𝔉f)` and `i_-(f) = (f,f)` into `S(C_K)_{]1,∞[} ⊕ S(C_K)_{]−∞,0[}` (eq.
    `def_i_pm`, l.409).
  * `𝓗⁰_- := 𝓗_-/(𝓗_+ ∩ 𝓗_-)`, with the regular representation `π_-` of `C_K`.
  * `λ_g f(x) = f(g^{−1}x)` (l.322).
* (c) **Unitarity remark** (l.298–304): "For algebraic number fields, each L-function has infinitely many zeros … We can
  modify the representation π so that it lives on a Banach space, even a Hilbert space. However, there is little point
  in doing so because **we cannot make it unitary once there are multiple zeros** or zeros off the critical line." This
  is Lemma U's content over `K`, stated as a remark without proof.
* (d) **Ideal, stated informally** (l.449–456): the Laplace image of `𝓗_- ∩ 𝓗_+` "consists of all holomorphic functions
  that have a zero of order at least `ord(ω,L_K)` at the zeros of `L_K` and that, in addition, satisfy some growth
  conditions". This sentence is in the introduction. It is not a theorem.
* (e) **Lemma "Lap_weighted_Sch"** (l.4449): "The Fourier–Laplace transform maps `S(C_K)_I` isomorphically onto the
  space of holomorphic functions on `{Re ω ∈ I}` whose restriction to `|x|^α \widehat{C_K}` is a Schwartz function for
  all `α ∈ I`." This is the `K`-version of the first half of the note's Thm "Lap_range".
* (f) **The in-text description of `(Σ𝓗_+^S)^`** (l.4567–4591). This is the `K`-version of the second half of
  "Lap_range", phrased through `\widehat{𝓛_S}(ω) = ∏_{v∉S}(1−ω(p_v)^{−1})^{−1}` (l.4547). It is not numbered.
* (g) **Lemma "Poisson_sumpm"** (l.4029): `i_+(𝓗_+) + i_-(𝓗_-) = {(f₀,f₁) : f₀ − f₁ = c₀ − c₁|x|^{−1}}`, with
  `J Σ 𝔉 = Σ + 𝓡` and `𝓡f = f(0) − |x|^{−1}𝔉f(0)` (eq. `Poisson_summation`, l.4022).
* (h) **Theorem "difference_spectrum"** (l.4597): "The spectrum of π consists of the poles and zeros of the L-function
  `L_K` … and we have `mult(ω,π) = ord(ω,L_K)`." Here `mult` is the **algebraic** multiplicity (l.1023): "the maximal
  number of times `C(ω)` occurs as a subquotient in [a Jordan–Hölder series of a finite dimensional subrepresentation]".
  In the proof (l.4619): "the only possible ω-homogeneous functionals are multiples of the evaluation map at ω". So the
  contragredient has geometric multiplicity `≤ 1`. The equality of multiplicities is "easy to see" (l.4627); it is not
  written out.
* (i) **Galois action inert** (l.4398–4418): the automorphisms of `K` act, but "this action is not very interesting …
  Thus it has nothing to do with Artin L-functions." So the Artin factorisation of `ζ_K` is **not** a decomposition of
  `𝓗⁰_-`. That is why a squared Artin factor appears as a Jordan block and not as a semisimple `C²` (§5.3).
* (j) Symmetries (l.4372–4396): `mult(χ) = mult(|x|χ^{−1}) = mult(\barχ)`. A `∗`-structure `Jγ` exists on `𝓗⁰_-`, and
  "GRH is equivalent to the assertion that self-adjoint elements of the ∗-algebra `𝓗⁰_-` have real spectrum". This is
  another restatement.

**1.2 Meyer, math/0412277 (local copy).** It is `Q`-only. At l.217–220: "Our constructions for the ζ-function generalise
to Dirichlet L-functions … We run into problems, however, for number fields with more than one infinite place." At
l.1353–1362 it covers imaginary quadratic fields in one paragraph and says "Once there is more than one infinite place,
we need the more general setup of [Duke]". So the note's Thm "Lap_range" has **no** `K`-version in the note. The field
`Q(∛2, ζ₃)` is totally imaginary of degree 6, with three complex places, so Duke is required.

**1.3 Connes, math/9811068.** §III is set over a global field `k`.
* **Theorem 1** (l.873–884) concerns `L²_δ`, `δ > 1`: the spectrum is the **critical** zeros, and the multiplicity is
  "the largest integer `n < (1+δ)/2`, `n ≤` multiplicity".
* The remark at l.949–952: "When the zeros of L have multiplicity and δ is large enough the operator D is not
  semisimple and has a non trivial Jordan form (cf. Appendix I). This is compatible with the almost unitary condition
  (22) but not with skew symmetry for D."
* The number-field extension of §VIII (l.2717 ff., "This gives the analogue of Lemma 1, Theorem 5, and Lemma 3",
  l.2832) is by analogy.

R158_004 cites these passages as l.574–645 and l.2205–2215. That numbering is different from the e-print's; the text
is the same.

**1.4 CCM, math/0703392.**
* Def "motH1AKCK": `𝓗¹(A_K/K^×, C_K)` is the cokernel of `ρ^♮`, taken, per the text right after the definition, as
  the quotient "by the closure of the range".
* Def "rangeTrpi": `𝒱 = {Σξ : ξ ∈ S(A_K)_0}`, where `S(A_K)_0 = ker ε₀ ∩ ker ε₁`.
* Lemma "varthetaH1V" (≈ Lemma 4.17): `ϑ_m(f)` acts on "the quotient of `S(C_K)` by `𝒱`".
* Thm "varthetagTrH1" (Thm 4.16): trace formula over every global field; l.1773–1776: "all zeros contribute … with their
  natural multiplicity. This follows from the choice of function space as in [Meyer]". Prop "specrealH1mot":
  "essentially reduces to the result of [Meyer]".
* CCM therefore **defer the multiplicity to Meyer Duke** and say nothing about the Jordan structure.

**Answer to "does Meyer treat number fields?"** Yes, in Duke 2005, not in the note. **Is cyclicity a cited theorem?** No,
in no source. The multiplicity is a theorem (Duke 1.1(h), algebraic multiplicity). Non-semisimplicity is stated by
Meyer (1.1(c)) and by Connes (1.3) as remarks. The chain therefore has to be proved. §3 proves it, using only (b), (e)
and (g) of Duke plus Tate's thesis. Clause (iv) of the theorem also uses (h).

## §2 Setting over `K`

* Fix a number field `K` with `n = [K:Q] = r₁ + 2r₂`.
* `C_K = C_K^1 × R_+^*`. The splitting uses `t ↦ (t^{1/n}, …, t^{1/n})` at the archimedean places, whose idele norm is
  `t`.
* `P` is averaging over the compact group `C_K^1`. It is a bounded idempotent that commutes with `λ`, `Σ`, `𝔉` and `J`,
  so it preserves `𝓗_±` and `𝓗_+ ∩ 𝓗_-`.

**Definition.** The **trivial sector** is `H¹_{K,1} := P𝓗⁰_- = P𝓗_-/P(𝓗_+∩𝓗_-)`. It is the `Ẑ^×`-invariant sector
when `K = Q`.

* By Duke 1.1(e), the Laplace transform `h(s) = \hat k(|x|^s)` identifies `P𝓗_-` with
  `𝒪 := {h entire : t ↦ h(σ+it) is Schwartz for every σ ∈ R}`. A function on `Ω(C_K)` that is supported on the
  identity component is Schwartz on `|x|^α\widehat{C_K} = \widehat{C_K^1} × (α+iR)` exactly when its restriction to
  `α+iR` is Schwartz.
* Let `I_K ⊂ 𝒪` be the image of `P(𝓗_+∩𝓗_-)`. Then `H¹_{K,1} ≅ 𝒪/I_K`.
* `Θ` is the generator of `R_+^*`. Since `(λ_g k)^(ω) = ω(g)\hat k(ω)`, `Θ` acts as multiplication by `s`. On this sector
  it does not depend on the splitting, because `C_K^1` acts trivially.
* CCM's version is `𝒪/\overline{I_K}`. Their `S(C_K)` is Meyer's `𝓗_-`. Their `𝒱` equals `𝓗_+∩𝓗_-` inside `𝓗_-`:
  * `i_+(f) ∈ i_-(𝓗_-)` forces `𝓡f = 0` by 1.1(g), that is `f(0) = 𝔉f(0) = 0`.
  * Conversely, `𝓡f = 0` gives `Σf = JΣ𝔉f ∈ S_{]1,∞[} ∩ S_{]−∞,0[} = S_{]−∞,∞[}`. The last equality holds because
    `|x|^α ≤ |x|^{α₁} + |x|^{α₂}` for `α₁ < α < α₂`.
* The cyclic-module layer, `Tor(C^♮, ·)` in CCM eq. "TorH1mot", is not re-verified here. It is doubt 3 in §7.

Write `m_ρ` for the order of `ρ` as a zero of `ζ_K`. All nontrivial zeros satisfy `0 < Re ρ < 1` (Hecke:
`ζ_K(1+it) ≠ 0`, plus the functional equation).

## §3 Theorem J_K (Jordan chains on the trivial sector)

**Lemma 1 (the ideal vanishes to full order).** For every `h ∈ \overline{I_K}` (closure in `𝒪`) and every nontrivial
zero `ρ`: `h^{(j)}(ρ) = 0` for all `j < m_ρ`.

*Proof.*
1. **Unfolding.** Let `h ∈ I_K`. Then `h` is the Laplace transform of `k = Σf ∈ 𝓗_-`, with `f ∈ S(A_K)`, projected to the
   trivial component. For `Re s > 1`, unfolding (Tate) gives
   `h(s) = ∫_{C_K} Σ_{a∈K^×} f(ax)|x|^s d^×x = Z(f,s) := ∫_{A_K^×} f(x)|x|^s d^×x`.
2. **Factorisation.** By definition of the Bruhat–Schwartz space, `f = f_T ⊗ 1_{Ô^T}` for some finite set of places
   `T ⊇ ∞`, with `f_T ∈ S(A_T)`. Hence
   `Z(f,s) = Z_T(f_T,s) · c_T ζ_K(s) ∏_{v∈T, v∤∞}(1 − q_v^{−s})`.
3. **Holomorphy.** `Z_T(f_T,s)` converges absolutely for `Re s > 0`, since `|f_T(x)| ≤ C_N ∏_{v∈T}(1+|x_v|)^{−N}` and
   `∫_{K_v^×}(1+|x|)^{−N}|x|^σ d^×x < ∞` for `0 < σ < N`. So `h = G_f ζ_K` on `Re s > 1`, with `G_f` holomorphic on
   `Re s > 0`. By uniqueness of continuation this holds on `Re s > 0`, so `ord_ρ h ≥ m_ρ`.
4. **Closure.** Each `ℓ_{ρ,j}(h) = h^{(j)}(ρ) = ∫ k(x)(log|x|)^j|x|^ρ d^×x` is a bounded functional on `S(C_K)_{]−∞,∞[}`.
   It vanishes on `I_K`, so it vanishes on the closure. ∎

**Lemma 2 (an ideal element of exact order).** Fix a nontrivial zero `ρ`. There is `E ∈ I_K` with `ord_ρ E = m_ρ`.

*Proof.*
1. **The seed functions.** Let `f₀ = ⊗_{v∤∞}1_{O_v} ⊗ ⊗_{v real}e^{−πx²} ⊗ ⊗_{v complex}e^{−2π|z|²}`. By Tate,
   `Z(f₀,s) = C·Γ_R(s)^{r₁}Γ_C(s)^{r₂}ζ_K(s) = C′B^sΛ_K(s)`, with `C′ ≠ 0` and `B > 0`.
   * Take `b ∈ C_c^∞(R_+^*)` with `\hat b(ρ) ≠ 0`, where `\hat b(s) = ∫b(t)t^s d^×t`.
   * Put `u := (t∂_t)(t∂_t + 1)b`. Then `\hat u(s) = s(s−1)\hat b(s)`.
2. **The test function.** Set `f_u(x) := ∫ u(t) f₀(t^{−1}x) d^×t`, with `t` embedded at `∞` as in §2. Then
   `f_u ∈ S(A_K)` and `Z(f_u,s) = \hat u(s)Z(f₀,s)`.
3. **`f_u` has no singular part.** `f_u(0) = \hat u(0)f₀(0) = 0` and `𝔉f_u(0) = \hat u(1)𝔉f₀(0) = 0`. So `𝓡f_u = 0`, and
   by §2 `Σf_u ∈ 𝓗_+∩𝓗_-`.
4. **The element.** `E := ` the Laplace transform of `PΣf_u`, namely
   `E(s) = C′ s(s−1) \hat b(s) B^s Λ_K(s)`.
5. **Its order.** `s(s−1)Λ_K` is entire, and its zeros are exactly the nontrivial zeros of `ζ_K`, with multiplicity:
   the simple poles at `0` and `1` cancel, and the trivial zeros are cancelled by the Γ-poles. Since `\hat b(ρ) ≠ 0`,
   `ord_ρ E = m_ρ`. ∎

**Theorem J_K.** Let `ρ` be a nontrivial zero of `ζ_K` of order `m = m_ρ`. Let `E` be as in Lemma 2, and set
`v_k := [E/(s−ρ)^k] ∈ 𝒪/\overline{I_K}` for `1 ≤ k ≤ m`.
* (i) `v_k ∈ 𝒪`, and `(Θ−ρ)v_k = v_{k−1}` for `k ≥ 2`, `(Θ−ρ)v_1 = 0`.
* (ii) `v_1, …, v_m` are linearly independent in `𝒪/\overline{I_K}`, hence also in `𝒪/I_K`.
* (iii) `span{v_k}` is a `C_K`-subrepresentation.
* (iv) For every finite-dimensional subrepresentation `W` of `H¹_{K,1}`, the `ρ`-generalized eigenspace of `Θ|_W` lies in
  `span{v_k}`. So, on the union of finite-dimensional subrepresentations, the `ρ`-part is **one Jordan block of length
  `m_ρ`**. Clause (iv) is for Meyer's `𝓗⁰_-`, where Duke Thm "difference_spectrum" applies.

*Proof.*
* **(i).** `E/(s−ρ)^k` is entire. On each vertical line it is Schwartz: near `ρ` it is smooth, and away from `ρ` the
  factor `(s−ρ)^{−k}` has bounded derivatives. Also `(s−ρ)v_1 = [E] = 0`.
* **(ii).** The matrix `ℓ_{ρ,j}(v_k)`, `0 ≤ j < m`, is triangular with nonzero antidiagonal, because
  `ord_ρ E/(s−ρ)^k = m−k`. The functionals are well defined on the quotient by Lemma 1.
* **(iii).**
  * Take `g ∈ C_K` with `|g| = e^t`. Write
    `e^{ts} = e^{tρ}Σ_{j<k}t^j(s−ρ)^j/j! + (s−ρ)^kR_k(s)`.
    Then `π_-(g)v_k = e^{tρ}Σ_{j<k}(t^j/j!)v_{k−j} + [R_kE]`.
  * `R_k\hat b` is a Paley–Wiener transform of a function `b′ ∈ C_c^∞(R_+^*)`. It is the difference of `\widehat{λ_{e^t}b}`
    and `\widehat{P(t∂_t)b}`, it vanishes to order `k` at `ρ`, and division by `(s−ρ)^k` preserves exponential type and
    decay on vertical lines.
  * So `R_kE` is Lemma 2's element built from `b′`, and it lies in `I_K`.
* **(iv).** `W + span{v_k}` is a finite-dimensional subrepresentation. By Duke Thm "difference_spectrum" and the
  definition 1.1(h), `C(|x|^ρ)` occurs at most `m_ρ` times in its Jordan–Hölder series. For a finite-dimensional
  `R_+^*`-module, that count is the dimension of the `ρ`-generalized eigenspace. The span already has dimension `m_ρ`
  by (ii). So the generalized eigenspace of `W + span` equals `span{v_k}`. The block is a single one because
  `ker(Θ−ρ) ∩ span = Cv_1`. ∎

**What is proved, and what is not.**
* Proved for every `K`:
  * the chain of length `m_ρ` in Meyer's `H¹` and in CCM's closed-range `H¹`;
  * its maximality among finite-dimensional subrepresentations.
* Not proved:
  * that `H¹_{K,1}` is the closure of `⊕_ρ span{v_k}` (density, the hull-ideal question of R158_002 A22, open as over
    `Q`);
  * the exact `K`-analogue of `I = {h : h/ζ Schwartz …}`. The inclusion used here is `I_K ⊆ {ord ≥ m_ρ}`; the reverse
    inclusion is not needed.
* The falsifier uses only (i) and (ii) with `m_ρ ≥ 2`.

## §4 Proposition S (the `S₃` multiplicity fact)

**Proposition S.** Let `K/Q` be Galois with `Gal(K/Q) ≅ S₃`, for example `K = Q(∛2, ζ₃)`. Let `F = Q(√−3)` be the
fixed field of `A₃`, and `K′` a cubic subfield. Then:
* (a) `ζ_K(s) = ζ(s)·L(s,χ_{−3})·L(s,ρ)²`, where `ρ` is the 2-dimensional irreducible representation;
* (b) `L(s,ρ) = L_F(s,ψ) = ζ_{K′}(s)/ζ(s)`, with `ψ` a nontrivial cubic Hecke character of `F`. So `L(s,ρ)` is entire;
* (c) `N_ρ(T) := #{ρ₀ : L(ρ₀,ρ) = 0, 0 < Re ρ₀ < 1, |Im ρ₀| ≤ T} = (T/π)log T + O(T)`, which is infinite;
* (d) each such `ρ₀` is a nontrivial zero of `ζ_K` of order `≥ 2`.

*Proof.*
* **(a).** Artin's formalism `ζ_K = ∏_π L(s,π)^{dim π}` over the irreducibles of `S₃`: `1`, `sgn` and `ρ`. The fixed
  field of `ker sgn = A₃` is `F`, so `L(s,sgn) = L(s,χ_{−3})` (Neukirch VII §10; P46 (X25a)).
* **(b).** `ρ = Ind_{A₃}^{S₃}ψ`. Invariance under induction gives `L(s,ρ) = L_F(s,ψ)`, and `ψ ≠ 1` makes it entire
  (Hecke). Also `Ind_{⟨τ⟩}^{S₃}1 = 1 ⊕ ρ` for a transposition `τ` gives `ζ_{K′} = ζ·L(s,ρ)`.
* **(c).** Landau's Riemann–von Mangoldt formula for Dedekind zeta functions, `N_{K′}(T) = (3T/2π)log T + O(T)` and
  `N_Q(T) = (T/2π)log T + O(T)`, together with (b): `L(s,ρ)` is entire, so the zeros of `ζ` are among those of `ζ_{K′}`
  with no larger multiplicity. Equivalently, apply the general formula for degree-2 `L`-functions (Iwaniec–Kowalski
  Thm 5.8).
* **(d).** At `ρ₀ ≠ 1`, all three factors in (a) are holomorphic, so
  `ord_{ρ₀}ζ_K = ord ζ + ord L(χ_{−3}) + 2 ord L(ρ) ≥ 2`. Here `0 < Re ρ₀ < 1`: there is no zero on `Re s = 1`, and the
  functional equation leaves only trivial zeros in `Re s ≤ 0`. So `ρ₀` is a nontrivial zero of `ζ_K`. ∎

Nothing here uses GRH or the Artin conjecture: `ρ` is monomial, so (b) is Hecke. The claim in R158_002 A20 is
confirmed exactly: every zero of `L(s,ρ)` appears in `ζ_K` with multiplicity `≥ 2`, and there are infinitely many.

## §5 Corollary F (the `S₃` falsifier) and its reach

**Corollary F.** Let `K` be an `S₃` field. Let `H` be `H¹_{K,1}` (Meyer), or `𝒪/\overline{I_K}` (CCM), or any space
with a `Θ`-equivariant map from one of them that is injective on `span{v₁, v₂}` for some zero `ρ₀` from Proposition S.
Let `c ∈ R`. Then no `Θ`-stable subspace `V ⊆ H` containing `v₁, v₂` carries a positive-definite hermitian form with
`(Θx,y) + (x,Θy) = 2c(x,y)`. This form of Deninger's Thm 2.1 structure covers both `c = ½` and CCM's shifted
normalisation (4.41). The conclusion holds unconditionally, whatever the truth of GRH for `ζ_K`.

*Proof.* This is Lemma U's Jordan step, with `c` free. Write `w = v₁` and `v = v₂`, so `(Θ−ρ₀)v = w` and `(Θ−ρ₀)w = 0`.
* **Case `(w,w) ≠ 0`.** Taking `x = y = w` gives `2Re ρ₀ (w,w) = 2c(w,w)`, so `c = Re ρ₀`.
* **The pair `(v,w)`.** Taking `(v,w)` gives `ρ₀(v,w) + (w,w) + \barρ₀(v,w) = 2c(v,w)`, that is
  `(w,w) = 2(c − Re ρ₀)(v,w)`. In the case above this forces `(w,w) = 0`, a contradiction.
* **Conclusion.** So `(w,w) = 0` always. Theorem J_K(ii) gives `w ≠ 0`, which contradicts definiteness. The argument
  uses neither the value of `Re ρ₀` nor the value of `c`. ∎

**5.1 Relation to the record.**
* R158_002's transport claim ("by T1, a field-uniform unitarity route on the adelic `H¹` proves something false")
  becomes PROVED, in this sense: a construction of a Lemma U structure on the full-multiplicity `H¹_{K,1}`, uniform in
  `K`, fails at every `S₃` field.
* Over `Q`, SZ is conjectural, so nothing is concluded about `ζ`. The corollary says that the unitarity reading of
  Meyer–CCM's `H¹` is **miscalibrated**: over `K` it forces simplicity of zeros, which is false.
* This supports N-b of R158_005 ("non-cyclic `H¹`" for the definite route). The "`+`" heuristic in N-b stays HEURISTIC.
* The corollary does **not** touch the semidefinite Weil/CCM trace form, which tolerates Jordan tails (R158_002 E-ii;
  R158_004 row 19).

**5.2 Where it does not apply.**
* In Connes' `L²_δ` (Thm 1), a critical zero of order 2 has spectral multiplicity `min(2, ⌈(1+δ)/2⌉−1)`, which is 1 for
  `1 < δ ≤ 3`. There `D` is semisimple at it, and Corollary F says nothing. Off-line zeros are absent from that space.
  Unitarity there is Connes' completeness question, which is equivalent to RH (R158_002 §2.5, 4.1).
* For `δ > 3`, Connes' own remark (1.3) gives the non-semisimple form, provided `L(s,ρ)` has a critical zero. That is
  expected and plausibly known (Hardy-type theorems for GL(2)), but it is not verified here and not used.
* Realisations that kill `v₁` (any quotient by a closed subspace containing `[E/(s−ρ₀)]`) escape the corollary, and so
  does a quotient to `H¹_red`, because only the `ℓ_{ρ,m−1}` coordinate survives on `v₁`. Such quotients discard the
  multiplicity, and then CCM Thm 4.16's "natural multiplicity" trace formula fails for them.

**5.3 Why the Artin structure does not help.** In the étale picture over `F_q`, a squared Artin factor is a semisimple
eigenvalue of multiplicity 2 on `ρ ⊗ (…)`. In Meyer's `H¹` the Galois action is inert (1.1(i)), so the multiplicity
cannot be split along `ρ`, and it appears as a length-2 Jordan block. For the definite route this is the precise sense
in which Meyer–CCM's `H¹` "lacks a correspondence algebra" (N-b). It is ANALYSIS as a diagnosis and PROVED as a fact
about `H¹_{K,1}`.

## §6 Labels proposed

| item | label |
|---|---|
| number-field Meyer realisation | CITED (Duke 2005; the note is `Q`-only) |
| `K`-version of "Lap_range" as a theorem | not in the literature (gap). Lemma 1 supplies the inclusion that is needed |
| Theorem J_K (i)–(iii) | PROVED |
| Theorem J_K (iv) | PROVED modulo Duke Thm "difference_spectrum" |
| Proposition S | PROVED, CLASSICAL |
| Corollary F (`S₃` falsifier) | **PROVED**, content classical in substance (Meyer 2005 remark l.302–304; Connes 1999 l.949–952); no novelty claimed |
| density of `⊕ span{v_k}` in `H¹_{K,1}` | OPEN (not needed) |

For P46 §28.3b / Remark 28.6: the `ANALYSIS (cyclicity)` flag on the `S₃` remark can be removed. The citation becomes
Meyer Duke 2005 (Lemma "Lap_weighted_Sch", Lemma "Poisson_sumpm", Thm "difference_spectrum", intro l.298–304) together
with this file's Lemma 1, Lemma 2 and Theorem J_K. (X33)(ii)'s "not read" should be updated. Both are open decisions; nothing was edited here.

## §7 Doubts for the audit

1. **Unfolding.** Lemma 1 step 1 identifies an element of `𝓗_+∩𝓗_-` with `Σf` for an `f ∈ S(A_K)`, and its trivial
   Laplace component with Tate's `Z(f,s)` for `Re s > 1`. Check the identification `i_+(f) = i_-(k) ⇒ k = Σf` against
   Duke eq. `def_i_pm` (first component).
2. **The `T`-factorisation `f = f_T ⊗ 1_{Ô^T}`.** It holds because `S(A_K)` is the algebraic inductive limit over `T`,
   and `S(A_T)` includes the completed archimedean `S(K_∞)`. Check that Meyer's `S(A_K)` is this space (Duke l.319 ff.,
   "Bruhat–Schwartz").
3. **CCM's cyclic-module layer.** `H¹ := Tor(C^♮, 𝓗¹)` (CCM eq. "TorH1mot") was not re-derived. The claim is only that the
   vector space on which `ϑ_m` acts is `S(C_K)/\overline{𝒱}` (their Lemma "varthetaH1V"), and that `𝒱 = 𝓗_+∩𝓗_-`
   (§2).
4. **`S_{]1,∞[} ∩ S_{]−∞,0[} = S_{]−∞,∞[}`** on `C_K`. This is used in §2 and in Lemma 2 step 3. It is interpolation of
   weights, including derivatives along `C_K^1` and `R_+^*`. Check it at the compact factor as well.
5. **Theorem J_K(iii).** The Paley–Wiener step `R_k\hat b = \hat{b′}` with `b′ ∈ C_c^∞(R_+^*)` should be checked. It
   relies on division by `(s−ρ)^k` of a PW function vanishing to order `k`.
6. **Theorem J_K(iv).** This rests on Meyer's "easy to see" equality of multiplicities (l.4627). If only `≥` were
   available, (iv) would weaken to "at least one block of length `m_ρ`". Corollary F does not need (iv).
7. **Normalisations.** Meyer's `Θ` spectrum is `{ρ}`; CCM's `ϑ_m = |γ|^{1/2}W` shifts it by `½`. Corollary F is stated
   for every real `c`, so the normalisation is irrelevant. Check that "compatible" in Deninger's Thm 2.1 is
   `Θ + Θ* = const` and not a weaker relation.
8. **Scope.** Corollary F is about the full-multiplicity realisations (Meyer, CCM). It says nothing about `L²_δ` with
   `δ ≤ 3`, or about quotients that kill `v₁` (§5.2). Any wording in P46 must keep this scope.
9. **Novelty.** None. Meyer 2005 states the non-unitarity at multiple zeros as a remark. The `S₃` multiplicity is
   textbook. The only new text is the explicit chain over `K` (Lemmas 1–2) and the observation that `S₃` fields make
   the hypothesis "multiple zeros" unconditional.

## §8 Corpus check (working rule)

Grep over `03-research/`, `04-papers/` and `05-meta-and-planning/` for "double zero", "multiple zero", "Jordan block",
"non-semisimple", "Dedekind"+multiplicity, "S₃", and `0311468`.
* The `S₃`/Jordan argument appears only in phase 158: R158_002 A20 and R158_004 rows 12–12′.
* Meyer Duke appears only in P46 (X33)(ii) ("not read"), phase 39 `119-forced-axioms-backward-derivation.md` (bibliography) and
  `01-context/RH2025/task31,33` (bibliography).
* Phase 58 `192-conj-179-6` §(iii) discusses Artin L-functions in a different context (off-line zeros, Euler rigidity).
* No earlier phase proves or refutes Theorem J_K or Corollary F.
