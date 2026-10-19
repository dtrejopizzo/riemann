# D_CONSTRUCTION_001: attempt at direct construction of 𝔇 per SPEC-𝔇 (phase 200, round 22)

Specification source: HORN_B_BIGSHARP_001 §2.3
(S1–S6).
NO-GO.

## Summary (≤300 words)

I developed the "entire correspondences on the window square" strategy across three objects and carried it through to the
deciding lemma.

- **𝔇₀ (discrete square ℕ×ℕ).** Theorem 1 (NO-GO, PROVED): no bilinear form with atomic kernel on
  (log ℕ)² ∩ [−T,T]² matches I_∞ on products of tests. The required weight w(m,n) does not exist. This refines INV_C Thm 4
  to the bilinear case. Consequence: 𝔇 needs continuous fibers.
- **𝔇₁ (comb correspondences with continuous fiber, counted by a Siegel–Dyson system).** χ = #unknowns −
  #conditions is a rank-nullity identity (PROVED). It genuinely reads (ℕ,·): the number of conditions along the
  multiplicative correspondence is Ford's multiplication-table problem (CITED), and the first normal derivative
  produces Λ = μ∗log exactly (PROVED). But the count depends only on the supports. Theorem 3 (NO-GO, PROVED): no
  χ depending only on supports or orders can have leading term ½I_∞. If instead the conditions are sensitive to
  the coefficients and are defined via the form, S1 fails.
- **S3.** Proposition M (PROVED): truncated Möbius inversion is unimodular on any divisor-closed window. As a
  "duality" it gives χ ≡ 0. A duality via a ℤ-perfect pairing is Poisson/van der Geer–Schoof and is therefore linear.
  This is a dichotomy.
- **Escape via mixed volume (Kazarnovskiĭ/BKK + Minkowski).** Gives an integer, quadratic χ with a Hodge signature. But it
  does not see the coefficients, is generic for Beurling and Epstein, and its isometric embedding is equivalent to (W⁰)
  (REF-D, PROVED).
- **𝔇₂ (Siegel–Dyson system evaluated at x_p = log p).** It is the only candidate that feels the coefficients without
  using the form. Its h⁰ is an integer rank over ℚ[x_p]. Order k produces Λ_k = μ∗log^k; order 2 contains Λ∗Λ, which is
  where Λ_cosh lives (S6, ARGUED).

**Deciding lemma (OPEN): Lemma 𝔇-Sch.** One must decide whether the rank defect of the Siegel–Dyson system when evaluating
x_p ↦ log p is nonzero and quadratic in the order. If the defect is zero (what Schanuel predicts), h⁰ is the
generic rank, identical for ζ and for generic Beurling, and 𝔇₂ is NO-GO (CONDITIONAL on Schanuel). If it is not zero, the
defect is an algebraic relation among the log p, with no visible connection to the sign. In either case 𝔇₂ does not give the
sign. Mori μ=15: h⁰ ≈ 0.1918·e^{2T}, the same for every g. Lemma E: 𝔇 does not exist on the positions of Z_Q, and the
failure is localized in the multiplication map H⁰(C)⊗H⁰(C) → H⁰(C²).

Row D / L′♯: unchanged, OPEN.

---

## 0. Corpus and index check (done before designing)

I grepped `05-meta-and-planning/ROUTES-TRIED-INDEX/` (all files), the phase-200 directory and the
crossword for these terms: "Riemann–Roch", "RR", "quadratic", "h⁰", "divisor", "degree", "Serre", "duality", "Möbius",
"semiring", "(ℕ,+,·)", "monoid", "Deitmar", "Durov", "Connes–Consani", "site", "tropical", "Borger", "Witt";
and also "Siegel", "pigeonhole", "Bombieri–Vaaler", "Thue", "Dyson", "Stepanov", "Kazarnovsk", "BKK", "Khovanskii", "Newton
polyg", "mixed volume", "Ehrhart", "Szegő", "Schanuel", "Λ_k".

Entries touching this construction, with the new reason for each:

| entry | what it closed | why this is different |
|---|---|---|
| INV_C_001 (phase 194): h⁰ off the multiplicative diagonal; pair count, Farey, Möbius; Thm 4 "no measure on log ℚ gives 𝔞_T" | pair forms **used as linear functionals** of the test | here h⁰ is an **integer rank** of a system (nonlinear in E). I reuse Thm 4 anyway: Theorem 1 below is its bilinear version and kills 𝔇₀ |
| INV_B (phase 194): pair surface 𝒮, Hodge/CS/nef | intersection form on pairs defined by the form | here χ is obtained by counting |
| P41-1: scale-site square (Allermann–Rau), PARTIAL, real and non-integral | real intersection of flow correspondences | here everything is ℤ-rank; the object is the system of conditions |
| P44-2: 𝒜rith category of correspondences, NO-GO | δ is not a character | δ is not used |
| G1_B9 / H2 "Stepanov over ℤ" (phase 159/193), DISCARD/REF-D | one-variable auxiliary polynomial vanishing at zeros/points | here the auxiliary polynomial is in **two** Dirichlet variables and vanishes along the multiplicative correspondence s = w (Dyson type). What vanishes is not the zeros, and a rank is measured |
| Phase 138 D.16–17: Khovanskii–Teissier form of the I_∞ cones, DEAD | KT as a *form* of I_∞ | here mixed volume appears as a zero count (Kazarnovskiĭ). It falls into §5 the same way |
| C_006 E3 Ax–Schanuel (phase 193), CIT | Schanuel as a source of positivity | here Schanuel only decides a rank (§6) and is used in a negative sense |
| W-det / R164_502c (Szegő–Widom), NO-GO | Toeplitz determinants | mentioned only to rule it out (§3.4) |

"Siegel" in the index appears only as Siegel–Walfisz (progressions, NO-GO), anti-Siegel (NG-B3) and Riemann–Siegel.
**Siegel's lemma, Bombieri–Vaaler, Dyson's lemma and Kazarnovskiĭ's count have no entry.** They are the new content
of this memo. Every result below is proposed for the index in §9.

## 1. What needs to be extended: D^W and I_∞ (P46 §11, §12, §19)

- **D^W (P46 Def 11.1).** Real functions g ∈ C²(ℝ) with g^{(j)}(t) = O(e^{−(1+ε)|t|}) for j = 0,1,2. It is a ⋆-algebra
  with involution g^∨(t) = g(−t) and translations τ_a (Lemma 11.2).
- **Intersection form.** I_∞ (Def 11.4) is the polarization of ⟨X⋆X^∨, W_fin + ω_∞⟩: the prime term plus the
  archimedean term of the explicit formula evaluated on the autocorrelation. It has radical 𝓝_∞ (Thm 11.11).
- **Canonical class.** K is the Pólya class (Φ_K = ξ). One has deg E = I_∞(E,2K) = a+b with (a,b) = M(E) = (Φ_E(1),Φ_E(0)),
  and also I_∞(K,K) = ½, I_∞(E,K) = ½deg E, and the comparison identity I_∞(E,E) = 2ab − W(E).
- **The Riemann–Roch functional.** R(E) := ½I_∞(E,E) − ¼deg E + χ (Def 19.1). It is Serre-symmetric under σ_K: E ↦ K−E
  (Thm 19.2), and the proof uses only bilinearity.
- **What Thm 12.3 requires.** A function h⁰ with (a), (b′) and (c): h⁰(E) + h⁰(K−E) ≥ R(E). Horn A (Theorem HA, PROVED) shows
  that any h⁰ with (c′) **on D^W** falls into (W⁰). That is why 𝔇 must be a strict extension with sections that are
  not tests.
- **What must be proved.** By HORN_B §2.2, the inequality h⁰(nE) ≥ χ(nE) − h⁰(K−nE) − h²_err(nE), with
  χ(nE) ~ ½n²I_∞(E,E) and h²_err = o(n²), where χ is a dimension **calculation** (S1).

I fix the window notation: P_T = primitive classes supported on [−T,T] (no polar part, S4). The comb is
ν_Λ = Σ_n Λ(n)n^{−½}δ_{log n}. The prime term of I_∞ on g⊠g is Σ_n Λ(n)n^{−½}(g⋆g^∨)(log n) plus the symmetric part.

## 2. 𝔇₀: the discrete square. The weight w does not exist

**Definition 2.1.** Let X = e^{T}. Set Q_X = {(m,n) ∈ ℕ² : m,n ≤ X} and 𝔇₀(X) = ℤ^{Q_X}, i.e. entire correspondences
on the window square. To each test g ∈ D^W I associate its sampling Φ_g(m,n) := g(log m)g(log n) (real version) or
any linear sampling of g⊠g with weights at the lattice points. The strategy's question is whether there exists a weight
w: Q_X × Q_X → ℝ such that

  I_w(Φ_g,Φ_g) := Σ_{x,y ∈ Q_X} w(x,y)Φ_g(x)Φ_g(y) = I_∞(g,g)  for every g ∈ P_T. (2.1)

**Theorem 1 (NO-GO for 𝔇₀; PROVED, with the cited input).** There is no w satisfying (2.1), and there is also no
sampling of g⊠g that is linear and supported on a countable set of points of (log ℕ)².

*Proof.*

1. The left side of (2.1) is a quadratic form in g depending only on the values of g on the finite set
   L_X = {log m : m ≤ X} ⊂ [0,T]. In the version with a sampling fiber, the set is countable and closed in [−T,T].
2. Choose an open interval J ⊂ (0,T) disjoint from L_X. It exists, because L_X is finite.
3. The subspace V_J = {g ∈ C_c^∞(J) : g ∈ P_T} has codimension ≤ 2 in C_c^∞(J). The two conditions of P_T are
   linear (Φ_g(0) = Φ_g(1) = 0 in P46's normalization). Hence V_J is infinite-dimensional.
4. On V_J the left side is identically 0.
5. I_∞ is not identically 0 on V_J. For g ∈ V_J with |J| < log 2, the prime term vanishes, because g⋆g^∨ is
   supported on (−|J|,|J|) and does not reach log 2. What remains is I_∞(g,g) = ⟨g⋆g^∨, ω_∞⟩, the archimedean form.
6. The archimedean form is non-degenerate on C_c^∞ of any interval. Its kernel is K(u) plus a singular part at 0
   (CITED: P46 Thm 11.3, local small-support positivity of Yoshida/Bombieri, which is L02 of the index). If it were ≡ 0 on
   a codimension-≤2 subspace of C_c^∞(J), by polarization the kernel would have rank ≤ 2 on J×J. That is false: the
   kernel contains −(1/2π)log|u| plus a smooth function, which has infinite rank.
7. Contradiction. ∎

**Reading.** Theorem 1 is the bilinear version of INV_C Thm 4. A **purely discrete** square cannot carry the
archimedean part, and S6 (Λ_cosh is archimedean in the sense of the degree-2 Γ) dies right there. Hence 𝔇 must
have continuous fibers: correspondences **of comb type over a continuous fiber**. That is what Q2_LADDER does, where the
integer lives in the coefficients and the test in the fiber.

## 3. 𝔇₁: comb correspondences and Siegel–Dyson counting

### 3.1 The object

**Definition 3.1 (𝔇₁).** Fix g ∈ D^W (the "fiber"). For an integer vector a = (a_{m,n}) ∈ ℤ^{Q_X} define the correspondence

  C_a := Σ_{m,n ≤ X} a_{m,n}(mn)^{−½} τ_{(log m, log n)}(g⊠g) ∈ D^W ⊗̂ D^W,

and its two-variable Dirichlet polynomial A_a(s,w) := Σ a_{m,n} m^{−s}n^{−w}. Then

  𝔇₁(X,g) := D^W ⊕ {C_a : a ∈ ℤ^{Q_X}}

contains D^W as the test summand and the entire correspondences, which are not tests (as required by Horn A). The
strategy's natural correspondences are particular cases:

- [m | n] is a = 1_{m|n};
- [m = kn] is the twisted diagonal Γ_k;
- [mn = N] is the multiplicative antidiagonal;
- [m + n = N] is the additive antidiagonal.

The first three read (ℕ,·) and the fourth reads (ℕ,+).

**Lemma 3.2 (Q2_LADDER, CITED from phase 200).** For g in the core with A(g) = 0, the window form is
W_T(g) = 𝒲[Σ_{N>1, P⁻(N)≥μ} N^{−½}τ_{log N}g], a **0/1** comb over the μ-rough integers. Hence the window
form is already a form evaluated on an entire correspondence of 𝔇₁ (diagonal, a_{1,N} = 1_{rough}). This confirms that
𝔇₁ is the natural setting.

### 3.2 h⁰ as a Siegel–Dyson system

Let E = (X, t). The window is X and t is the vanishing order along the multiplicative correspondence
Δ_· = {s = w} (the "diagonal" of the square in Mellin coordinates). Define

  H⁰(E) := {a ∈ ℤ^{Q_X} : ∂_w^k A_a(s,w)|_{w=s} ≡ 0 for 0 ≤ k < t}.

Expanding, ∂_w^k A_a|_{w=s} = (−1)^k Σ_N (Σ_{mn=N} a_{m,n} log^k n) N^{−s}. By uniqueness of Dirichlet coefficients,
the condition is a linear system: for each N ∈ M(X) := {mn : m,n ≤ X} and each k < t,

  L_{N,k}(a) := Σ_{mn=N} a_{m,n} log^k n = 0. (3.1)

Set h⁰(E) := rank_ℤ H⁰(E) and h¹(E) := dim coker of the map ℝ^{Q_X} → ℝ^{M(X)×t} given by (3.1).

**Proposition 3.3 (rank-nullity; PROVED).** χ(E) := h⁰(E) − h¹(E) = |Q_X| − t|M(X)| = ⌊X⌋² − t·|M(X)|.

*Proof.* System (3.1) has real coefficients, so H⁰(E) ⊗ ℝ is the real kernel if it has a rational basis.
This is resolved in §6. Here I take rank_ℝ, and then χ = dim domain − dim codomain. ∎

**Proposition 3.4 (S2: genuinely reads (ℕ,·); CITED).**
|M(X)| = #{distinct products mn with m,n ≤ X} ≍ X²/((log X)^{δ}(log log X)^{3/2}), with δ = 1 − (1+log log 2)/log 2 ≈ 0.086
(Ford 2008, Annals). Hence h⁰(E) ≥ χ(E) > 0 as long as t ≲ (log X)^{δ}(log log X)^{3/2}. There are nonzero integer
auxiliary polynomials that vanish to order t along Δ_·, and they exist **exactly because of the defectivity of the
multiplication table**, a phenomenon of the distribution of Ω(n) in (ℕ,·). By Siegel's lemma / Bombieri–Vaaler (CITED,
Bombieri–Vaaler 1983) there is also a solution with height
‖a‖_∞ ≤ (√|Q_X| · max coef)^{t|M|/(|Q_X| − t|M|)}, if (3.1) is rationalized.

**Proposition 3.5 (Λ appears exactly; PROVED).** If a_{m,n} = μ(m) (the Möbius correspondence μ⊠1), then for
N ≤ X:

- L_{N,0} = Σ_{m|N}μ(m) = [N=1];
- L_{N,1} = (μ∗log)(N) = Λ(N);
- in general L_{N,k} = (μ∗log^k)(N) = Λ_k(N), the generalized von Mangoldt function, with Λ_2 = Λ·log + Λ∗Λ (Selberg).

*Proof.* For N ≤ X all divisor pairs (m, N/m) lie in Q_X, and L_{N,k} = Σ_{m|N} μ(m) log^k(N/m). ∎

**Reading.** This is what the strategy was looking for: the **normal derivative at the multiplicative correspondence of the
Möbius correspondence** is the von Mangoldt comb, without inserting it by hand. It is the first time in the corpus that Λ
emerges as a **coefficient of a condition** of an integer system rather than as the weight of a measure. INV_C Lemma 2 only
gave weight 1 per prime power.

### 3.3 The failure: χ does not see the test

**Theorem 3 (NO-GO by blindness to the support; PROVED).** Let χ: 𝔇 → ℤ be any function depending on E ∈ D^W only
through discrete data: supports, vanishing orders, the Newton polygon of the support, or the set of lattice points where
E ≠ 0. Then χ(nE) does not satisfy χ(nE) = ½n²I_∞(E,E) + O(n) for every E ∈ P_T.

*Proof.*

1. Let E ∈ P_T with I_∞(E,E) ≠ 0 and F ∈ P_T with the same support and I_∞(F,F) ≠ I_∞(E,E).
2. F exists: on the open set supp E, the set {F : supp F = supp E} contains E + εh for every h ∈ C_c^∞ of the interior and
   every small ε, and I_∞(E+εh, E+εh) − I_∞(E,E) = 2εI_∞(E,h) + ε²I_∞(h,h).
3. That difference is not ≡ 0 in h. If I_∞(E,·) ≡ 0 on C_c^∞(int supp E), then I_∞(h,h) ≢ 0 by the argument in steps 5–6 of
   Theorem 1.
4. For every n, nE and nF have the same discrete data, so χ(nE) = χ(nF).
5. The two sides of the identity differ by ½n²(I_∞(E,E) − I_∞(F,F)), which is ≠ O(n). ∎

**Corollary 3.6.** The χ of Proposition 3.3 depends only on (X,t): it is blind to the test and to the fiber vector g. It
cannot be the quadratic RR of SPEC-𝔇. The same happens with every counting variant of the strategy (pigeonhole, Siegel, Thue,
Bombieri–Vaaler): the number of unknowns and the number of conditions are cardinalities of lattice sets.

**Corollary 3.7 (the trivial way out violates S1; PROVED).** For χ to see the test, the conditions must depend on the
values of E. If they are defined as "C_a ⟂_{I_∞} C_b" or via the kernel of the form, then the rank of H⁰ is a function
of the restricted signature of I_∞, and the RR becomes (W⁰) restated. That is REF-D, as in Corollary HB′.

### 3.4 The logarithmic count (Siegel as Minkowski) is linear

Siegel's lemma / Bombieri–Vaaler is, in Arakelov language, the inequality h⁰ ≥ deg − rank·(…) for the lattice
(ℤ^{Q_X}, norm) (CITED: Bombieri–Vaaler 1983; Bost 2020, "Theta invariants of euclidean lattices"). The degree term is
−log covol. If the norm depends on E via weights e^{−E(log m)−E(log n)}, then log covol = Σ_{(m,n)}(E(log m)+E(log n))
(diagonal determinant), which is **linear** in E. If the norm is the Gram matrix of the window form over the comb of 𝔇₁, the
log det is Szegő–Widom: a linear term plus a quadratic term Σk|φ̂_k|² that is a **positive-definite** H^{1/2} norm.
It has no informative sign and is already closed by W-det. This is exactly C-RR / P46 Prop 20.1. **NO-GO (CITED + PROVED
via P46 Prop 20.1).**

## 4. S3: can Serre duality be Möbius?

**Proposition M (Möbius is unimodular; PROVED).** Let Ω ⊂ ℕ be a finite divisor-closed set, for example
{n ≤ X}, the μ-rough integers ≤ X together with 1, or the support of the Q2 staircase. For every truncation of μ (c_N = Σ_{m|N,m<μ}μ(m)
as in FF.1, or μ supported on d < μ), the operator M_c: ℤ^Ω → ℤ^Ω, (M_c a)(N) = Σ_{d|N} c(d)a(N/d) with c(1) = 1, is
triangular with respect to the divisibility order with diagonal 1. Hence det M_c = 1 and M_c ∈ GL(ℤ^Ω). The same holds on
the square (μ⊠1, 1⊠μ, μ∘(m,n)↦mn).

*Proof.* If N ∈ Ω, every N/d is in Ω, and (M_c a)(N) = a(N) + Σ_{d>1} c(d)a(N/d), where every N/d is < N in the
divisibility order. ∎

**Corollary M′ (duality dichotomy; PROVED with the CITED facts).** Let 𝔇 be any object whose sections are ℤ-lattices or
ℤ-modules of the window.

- **(i)** If the "duality" E ↔ K−E is induced by a unimodular operator (Möbius or its truncations), it preserves
  ranks and covolumes: h⁰(E) = h⁰(E′) and log covol(E) = log covol(E′). The RR it produces is χ ≡ 0 (or a constant). A
  symmetry, not a Serre duality.
- **(ii)** If the duality is a dual lattice with respect to a perfect pairing, in the integer version one has
  rank V + rank V^⊥ = |Ω| (linear), and in the logarithmic version covol(L^∨) = covol(L)^{−1} via Poisson for lattices (van der
  Geer–Schoof, CITED). In both cases the RR is linear in E, which is C-RR.

There is no third option for ℤ-linear dualities on window modules. This **refutes the proposal "μ∗ in place of 𝓕**
as a Serre duality". Möbius survives as an **automorphism** of 𝔇₁. There it plays the role of the Weyl group or of
the involution σ_K, not of Serre.

**What Möbius does give (PROVED; partial S5).** M_c is defined on ℤ^Ω for the position semigroup of any
system with unique factorization (ℕ, ideals of O_K, Beurling). For the **positions** of an Epstein Z_Q with h > 1, the
set of norms represented by class C is not closed under multiplication (C·C = C² ≠ C), so Ω_C is not a semigroup. Möbius
inversion over Ω_C is not defined, because "N/d" may fall outside Ω_C. This is a legitimate localization,
**within the object**, of the Epstein failure, but it is a failure of **symmetry**, not of RR.

## 5. The mixed-volume escape (Kazarnovskiĭ / BKK) and why it is not enough

It is the only known way for an **integer count** to give a quadratic form **with a Hodge signature**:

- **(K1) CITED (Kazarnovskiĭ 1984; Bernstein–Kushnirenko–Khovanskii in the algebraic case).** For two generic exponential
  sums A(s,w), B(s,w) in ℂ² with Newton polygons P_A, P_B (in coordinates (log m, log n)), the density of common zeros
  per unit imaginary volume is c·V(P_A, P_B), where V is the mixed volume. The common zeros form an integer count.
- **(K2) PROVED (Ostrowski for Dirichlet sums).** Newton(AB) = Newton(A) + Newton(B): extreme edges do not cancel because
  the logs of the vertices add.
- **(K3) CITED (Minkowski).** V(P,Q)² ≥ V(P,P)V(Q,Q). For virtual polygons with support h = Σĥ_k e^{ikθ},
  2V(h,h) = Σ_k(1−k²)|ĥ_k|²: signature (1, 0 on translations, −∞). This **is** the Hodge index theorem for
  toric surfaces.

So the mixed volume on the square (log m, log n) satisfies S2 (integer), satisfies "quadratic and obtained by counting"
(S1 in the literal sense) and carries its own Hodge index. **But:**

- **Theorem 5 (NO-GO; PROVED).**
  - **(a)** The mixed volume of Newton polygons is blind to the support in the sense of Theorem 3, so it cannot
    be ½I_∞.
  - **(b)** For ζ, for Beurling and for Epstein, the Newton polygon of any window correspondence depends only
    on the set of positions (logs of the norms). It fails S5 (continuity in the comb) and fails S6.
  - **(c)** If one seeks a linear embedding ι: (P_T ⊕ ℝK, I_∞) → (virtual polygons, 2V) that is isometric,
    then it exists ⟺ I_∞ has at most one positive eigenvalue on P_T ⊕ ℝK, i.e. ⟺ (W⁰) (plus the dimension
    condition, which the infinite-dimensional target satisfies).

*Proof.* (a) and (b) are Theorem 3, because P_A depends only on supp a. (c): linear isometries of a real quadratic space
into another of signature (1, ∞) exist exactly when the positive index of the domain is ≤ 1 and the radical maps
to null vectors orthogonal to everything (Sylvester's law of inertia). Note that ι(K) must have V > 0 because
I_∞(K,K) = ½. ∎

**Reading.** Mixed volume is the "free Hodge" the strategy expected from the square. But everything Hodge-like about it
comes from convexity (Minkowski), not from the coefficients. The coefficients of an exponential sum enter only through
**non-genericity**: zeros at infinity, tropicalization with valuation −log|a_n| (Ritt–Pólya, CITED), and that is a
lower-order correction to the volume. **Conclusion for S1/S5:** the quadratic term of any counting χ is a
volume (by Ehrhart, or by Davenport for irrational regions, CITED), and a volume sees regions, not coefficients.

## 6. 𝔇₂: the Siegel–Dyson system with logarithmic coefficients, and the deciding lemma

System (3.1) is the only place in this memo where the **coefficients** (log^k n) enter a rank count without using the
form. That dodges Theorem 3's hypothesis: the rank of a system with real coefficients is not a support datum.
I analyze it carefully.

### 6.1 Formalization

By unique factorization, log n = Σ_p v_p(n) log p. Introduce formal variables x_p (p ≤ X) and the ring
R_X = ℚ[x_p : p ≤ X]. System (3.1) lifts to

  L^{form}_{N,k}(a) := Σ_{mn=N} a_{m,n} ℓ(n)^k = 0, with ℓ(n) := Σ_p v_p(n)x_p ∈ R_X, (6.1)

and (3.1) is its specialization ev: x_p ↦ log p.

**Definition 6.1 (𝔇₂).** 𝔇₂(X) = 𝔇₁(X) with the extra structure of (6.1).

- h⁰_gen(E) := rank of the kernel of (6.1) over Frac(R_X). It is an integer and is determined solely by (ℕ,·): the
  factorization gives ℓ, and the pair count gives M(X).
- h⁰_ev(E) := real rank of the kernel of (3.1), i.e. of (6.1) evaluated.

**Proposition 6.2 (PROVED).** h⁰_ev(E) ≥ h⁰_gen(E). The difference δ(E) := h⁰_ev − h⁰_gen is the rank defect of a
matrix with entries in R_X upon specialization. Hence δ(E) > 0 if and only if some nonzero maximal minor of (6.1)
vanishes at (log p)_p. This is an algebraic relation with coefficients in ℚ among the log p (p ≤ X).

*Proof.* The rank can only drop when specializing a nonzero minor to zero, so the nullity increases. ∎

**Proposition 6.3 (PROVED for k ≤ 1; elementary).** For t ≤ 2 (orders k = 0, 1), δ(E) = 0. The minors have degree ≤ 1
in each row, and the ℚ-linear independence of {log p} (which is unique factorization, PROVED) suffices for every
nonzero linear polynomial in x_p with rational coefficients to not vanish at (log p). This holds row by row. Minors of
higher degree, which result from products of rows, require **algebraic** independence. For t ≥ 3 this is OPEN and is contained
in the Schanuel conjecture (CITED as a conjecture).

*Precision.* For k = 1 a maximal minor of size r has degree ≤ r in the x_p, so even t = 2 involves
high-degree polynomials. Correction: **PROVED only for t = 1** (order-0 system, integer coefficients, δ = 0
trivially). For t ≥ 2, δ = 0 remains CONDITIONAL on the algebraic independence of {log p : p ≤ X}, a case of
Schanuel.

### 6.2 Why 𝔇₂ does not give the sign (dichotomy)

**Theorem 6 (NO-GO, CONDITIONAL in branch (i); ARGUED in branch (ii)).**

- **(i) If Schanuel holds for {log p}.** Then δ ≡ 0 and h⁰_ev = h⁰_gen. But h⁰_gen is the same for every Beurling
  system whose log-primes are algebraically independent and have the same free-semigroup structure: the matrix
  (6.1) depends only on the free monoid and on the pair count (G1 of the index, PROVED: the free monoid ℕ^× does not
  distinguish ζ from Beurling). There exist Beurling systems with zeros off the line (Diamond–Montgomery–Vorhauer,
  CITED; this is B″ of the corpus). Then any property of h⁰_ev implying (W⁰) for ζ would imply it for them too, which is
  false. **NO-GO, CONDITIONAL on Schanuel** (only on the independence part; the rest is PROVED).
- **(ii) If Schanuel fails for some set of log p.** Then δ > 0 for some E, and the defect is produced by a polynomial
  relation P((log p)) = 0 with P ∈ ℚ[x]. That relation is a transcendence datum, with no visible relation to the
  position of the zeros or to the sign, and it is not naturally quadratic in E. ARGUED: no known mechanism
  connects a defect of this type with ½I_∞.

**Reading.** This is as far as the mathematics of the strategy goes. The structure (ℕ,·) enters via M(X) (Ford) and
via ℓ (factorization). The comb Λ enters via the conditions (Proposition 3.5, Λ_k). But the **rank** of a system whose
coefficients are polynomials in log p is, barring transcendence, the generic rank, which is Beurling-generic. The semiring
(ℕ,+,·) enters only via (ℕ,·). The additive correspondence [m+n = N] has no analogue of (6.1) with log coefficients: its
normal derivative in Mellin is not a Dirichlet condition, because (m+n)^{−s} does not factor. That is the mark that "+"
does not enter this object. It matches the PROVED anatomy of family H of the index: "weight only additive in log q ×
coefficient only of the monoid".

### 6.3 What 𝔇₂ does see: order 2 and Λ_cosh (S6)

By Proposition 3.5, the order-k=2 condition of the Möbius correspondence is Λ_2 = Λ·log + Λ∗Λ (Selberg). The
Λ∗Λ term is supported on Ω(N) ≥ 2.

For Z_Q with h = 2, LEMMA_E gives Λ_Q = ½(Λ_K + Λ_ψ) + Λ_cosh, with Λ_cosh even in y = ½log(L_ψ/ζ_K) and supported on
even Ω_𝒩(n) ≥ 2. The coefficient of y² in −(d/ds)log cosh y is −(d/ds)(y²/2) = −y·y′. Its Dirichlet series is a
convolution of the coefficients of y and y′, which is **the same structure** as the Λ∗Λ term of Λ_2.

**Proposition 6.4 (ARGUED; formal computation on Dirichlet series).** System (3.1) built over ideals of O_K and
projected to class C decomposes according to the class group. The order-2 condition of the projected Möbius
correspondence contains the cross term (Λ_C ∗ Λ_C)(N), which lives in class C² and not in C. That term is the source of
Λ_cosh. Hence order 2 of 𝔇₂ **feels** Λ_cosh (S6), and it does so in the **multiplication map**
H⁰(C) ⊗ H⁰(C) → H⁰(C²), which is a piece of 𝔇 and not of the sign (S5).

*Status.* This is the positive part of the construction. It is ARGUED, not PROVED: it remains to check in LEMMA_12_1 (cumulants
of the dual class group) that the y² coefficient matches the projection of Λ_C∗Λ_C with the correct sign. I did not verify it
numerically, because it is not strictly necessary for the verdict: Theorem 6 already closes 𝔇₂ as a sign source.

## 7. Requested tests

### 7.1 Mori μ = 15: what h⁰ does it predict for the extremal class?

By Q2_LADDER Theorem Q2.1(4), with S ⊇ {p < 15}, the extremal class in 𝔇₁ is the diagonal correspondence with a_{1,N} =
1_{N>1, P⁻(N) ≥ 15}, i.e. the 0/1 comb over the 15-rough integers. The staircase coefficients c_N (FF.1) are
c_N = Σ_{m|N, m<15} μ(m), and by Proposition M the step between the "c_N comb" and the "0/1 rough comb" is unimodular.

- **h⁰ in 𝔇₁** (section = integer sub-comb supported on the class support, no conditions):
  h⁰ = 1 + #{1 < N ≤ e^{2T} : P⁻(N) ≥ 15} ~ e^{2T}·Π_{p<15}(1 − 1/p) = e^{2T}·(1/2)(2/3)(4/5)(6/7)(10/11)(12/13)
  ≈ 0.1918·e^{2T}. The sieve asymptotic is PROVED (Eratosthenes–Legendre with a fixed window); the constant is an
  exact calculation.
- **Prediction:** the same h⁰ for **every** g in the fiber (Theorem 3), and hence for the Mori extremal and for
  any other core test. h⁰ is exponential in T, not quadratic, and **does not distinguish** the extremal class.
- **In 𝔇₂ with t = 2**, on the rough sub-comb: the order-1 conditions of the truncated Möbius correspondence give
  (c ∗ log)(N), which on the odd band [7.5, 15) reproduces the coefficients c_{2M} = −[11|M] − [13|M] of Q2.1 multiplied
  by log. This is PROVED via Proposition 3.5 with truncated μ. The rank is again generic.

**Verdict:** h⁰(extremal) carries no sign information. This is NO-GO for using 𝔇₁/𝔇₂ at the ½log15 frontier.

### 7.2 Lemma E: does 𝔇 cease to exist for Z_Q, or does h⁰ change nature?

- **𝔇₀ and 𝔇₁ on the positions of Z_Q** (the norms represented by the form Q): **do not exist as objects with
  duality.** The positions do not form a semigroup (C·C = C²), so there is no Möbius inversion (§4) nor a closed
  multiplicative correspondence Δ_· on the window. PROVED, elementary. S5 is localized in 𝔇, as the specification
  requires.
- **But over ideals of O_K 𝔇 does exist, and is Beurling/ζ_K-generic.** Z_Q is a character projection of the
  class group, Z_Q = (1/h)Σ_ψ ψ̄(C)L(s,ψ). "Z_Q's" 𝔇 is the projection to class C of 𝔇(ζ_K), and the failure appears
  because the projection does not commute with the multiplication map (Proposition 6.4). The failure is in 𝔇, in the
  multiplication map, and not in the sign (ARGUED).
- **h⁰ changes nature:** in the C-class sector, h⁰(C) is a module rank over the principal-class ring
  (a rank-1 divisorial sheaf), not the rank of a ring. Its RR is no longer that of a "surface" but that of a twisted sheaf.
  This is ARGUED and is the version of S5 that this object offers.

## 8. Balance against S1–S6

| condition | 𝔇₀ | 𝔇₁ (Siegel–Dyson, counting) | mixed volume | 𝔇₂ (log coefficients) |
|---|---|---|---|---|
| S1 (χ by calculation) | — | yes (rank-nullity), but blind | yes (Kazarnovskiĭ), blind | yes, generic rank |
| S2 (integer, reads (ℕ,·)) | — | **yes** (Ford, Prop 3.4) | integer, positions only | **yes**, (ℕ,·) only; "+" does not enter |
| S3 (non-Poisson duality) | — | dichotomy M′: Möbius = symmetry | Minkowski, not a duality | same as 𝔇₁ |
| S4 (P_T, no polar part) | — | yes | yes | yes |
| S5 (discontinuous in the comb) | — | localized (Möbius does not exist for Epstein) | **no** | generic Beurling-invariant rank (CONDITIONAL) |
| S6 (Λ_cosh) | **no** (Thm 1) | no | no | order 2 ∋ Λ∗Λ, ARGUED |
| ½I_∞ as leading term | NO-GO (Thm 1) | NO-GO (Thm 3) | NO-GO (Thm 5) | NO-GO (Thm 6, CONDITIONAL) |

**The exact deciding lemma (OPEN).**

> **Lemma 𝔇-Sch.** There exists a family E_n in 𝔇₂ (window X_n, order t_n, fiber class E ∈ P_T) such that the rank
> defect δ(E_n) = h⁰_ev(E_n) − h⁰_gen(E_n) under the specialization x_p ↦ log p satisfies δ(E_n) = ½n²I_∞(E,E) + O(n).

- If none exists (which follows from Schanuel for {log p}, because δ ≡ 0), the construction via entire Siegel–Dyson
  correspondences is **closed**: every counting χ is either blind to the test (Theorems 3 and 5) or generic for Beurling
  (Theorem 6).
- If one exists, the sign of I_∞ in degree 0 would be read off a transcendence defect of the log p. That would be an
  entirely new tool, but there is no indication of it whatsoever.

The lemma is **stronger** than what was requested: it demands that the defect, not χ, carry the form. I state it this
way because χ = h⁰_gen − h¹_gen is blind by Theorem 3, and the only part of h⁰ that is not blind is δ.

**Final labels:**

- Theorem 1, Propositions 3.3, 3.5 and M, Corollary M′, Theorem 3, Theorem 5, Proposition 6.2: PROVED.
- Proposition 3.4, (K1) and (K3): CITED.
- Theorem 6(i): CONDITIONAL on Schanuel.
- Theorem 6(ii), Proposition 6.4 and §7.2 (points 2 and 3): ARGUED.
- Lemma 𝔇-Sch: OPEN.
- Row D / L′♯: **OPEN, unchanged**.

## 9. Proposed entry for ROUTES-TRIED-INDEX

- **D_CONSTRUCTION_001 (phase 200, round 22, no audit; new reason: h⁰ = integer rank of a
  Siegel–Dyson system of two-variable Dirichlet correspondences, not a pair form).**
  - 𝔇₀ (discrete ℕ×ℕ): no atomic weight realizes I_∞ (Thm 1, PROVED; bilinear version of INV_C Thm 4).
  - 𝔇₁: χ = |Q_X| − t|M(X)| (rank-nullity); reads (ℕ,·) via Ford's multiplication table (CITED); the normal derivative of
    μ⊠1 along s = w gives Λ_k = μ∗log^k exactly (PROVED). But the count is blind to the test (Thm 3, PROVED), and the
    output sensitive to coefficients via the form is REF-D.
  - Siegel / Bombieri–Vaaler as Minkowski: linear (C-RR). Szegő: W-det.
  - Truncated Möbius is unimodular (PROVED). As a duality it gives χ ≡ 0. The Möbius/Poisson dichotomy closes "μ∗ in place of 𝓕"
    as Serre duality.
  - Mixed volume Kazarnovskiĭ/BKK + Minkowski: free Hodge but blind and Beurling-generic, and the isometric embedding
    is equivalent to (W⁰) (Thm 5, PROVED).
  - 𝔇₂ (formal log p coefficients): evaluated rank = generic rank except for algebraic relations among the log p. Under
    Schanuel it is Beurling-generic (NO-GO, CONDITIONAL).
  - Order 2 ∋ Λ∗Λ ↔ Λ_cosh in the map H⁰(C)⊗H⁰(C) → H⁰(C²) (ARGUED).
  - Mori μ=15: h⁰ ≈ 0.1918·e^{2T}, independent of g.
  - Residue: Lemma 𝔇-Sch (OPEN).
  - Do not retry: pigeonhole, Siegel, Thue, Dyson, Ford or pair counts as quadratic RR; Möbius as Serre duality;
    Newton polygons or mixed volume as I_∞.
  - Row D OPEN.
