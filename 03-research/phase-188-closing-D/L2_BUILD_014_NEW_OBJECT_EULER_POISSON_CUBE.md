# L2_BUILD_014 — A new object: the Euler–Poisson cube and its integrality locus

Order: invent, define, axiomatize, prove basic properties, then test against the input map.

## Corpus check
grep "cube / [0,1]^ / prime weights t_p / interaction / Möbius transform over subsets / Boolean lattice / concave in
the weights / deformation of Euler factors": Paper 46 prop:wit-sens (sensitivity to weights), finmod (deletion,
amplification: single directions), N_BUILD_005 §2 (partial Euler products, powers Z^α), R160_M12 (×2 orbits), R184_004
(inertia of B_p blocks). Nobody defines the joint multi-parameter deformation of all local Euler factors with the
Poisson (coefficient-1) locus as a distinguished subvariety, nor its interaction expansion. Not a repeat; but it
contains finmod-type directions as edges, so its edges are known.

## 1. Definition
Let 𝒫_T = {p prime: p < N = e^{2T}}, d = |𝒫_T|. For t = (t_p) ∈ [0,∞)^{𝒫_T} define in 𝔄_T (s = ½):
  Z(t) := Π_{p∈𝒫_T} (δ₀ − t_p p^{−½}δ_{log p})^{−1},  comb(t) := −∂_s log Z(t) = Σ_{p,k} t_p^k log p · p^{−k/2}δ_{k log p},
  𝔞_T^{(t)}(F) := 𝔞_∞(F) − 2⟨comb(t), c_F⟩,  λ(t) := inf{𝔞_T^{(t)}(F): F ∈ P_T ∩ D_T, ‖F‖ = 1}.
(t_p^k enters because the local factor with parameter t_p is the Euler factor of the "twisted" prime p with p^{−s}
replaced by t_p p^{−s}; −∂_s of log(1 − t_p p^{−s})^{−1} = Σ_k t_p^k log p p^{−ks}.)
Distinguished loci:
 - Euler locus: all of [0,∞)^d (every Z(t) is an Euler product with nonnegative local log-coefficients).
 - Poisson (coefficient-1) locus 𝔓 := {t : every coefficient of Z(t) at log n, n < N, equals n^{−½}} — the window
   shadow of "Dirichlet coefficients exactly 1", i.e. of Poisson summation over ℤ (the FE at conductor 1, 012 §2).
 - Integrality: t ∈ {0,1}^d gives integer-supported products with coefficients in {0,1} (a_S of N_BUILD_005 §2).

## 2. Axioms satisfied (PROVED)
(A1) Multiplicativity: Z(t) = Π_p Z_p(t_p), and comb(t) = Σ_p comb_p(t_p) (additive over primes).
(A2) Concavity: λ is concave on [0,∞)^d along every line on which comb(t) is affine — in particular in each
     coordinate t_p restricted to the variable t_p ↦ comb_p is NOT affine (t_p^k), so concavity holds in the
     reparametrization w = (w_{p,k}) = (t_p^k): λ is concave in the full weight vector w (inf of affine functions). 
(A3) Edges: t = 0 gives λ_{∞,P}(T); t = 1 (all ones) gives λ_A(T); t = 1_S gives a_S; t = (1+ε)1 is Z^{1+ε}-like
     only to first order (Z^α of N_BUILD_005 has comb αΛ, i.e. w = α·1, which is NOT of the form t_p^k unless α = 1).
(A4) Poisson locus is a point (PROVED): coefficient of Z(t) at n = Π p^{k_p} is Π t_p^{k_p} n^{−½}; equal to n^{−½} for
     all n < N forces t_p = 1 for every p < N (take n = p). So 𝔓 = {1}.
(A5) Integral FE-vertex: among the vertices {0,1}^d only 1 lies in 𝔓 (from A4).
(A6) Interaction expansion: for the set function Λ(S) := λ(1_S), Möbius inversion on the Boolean lattice gives
     Λ(𝒫_T) = Σ_{R⊆𝒫_T} Λ̂(R), Λ̂(R) := Σ_{S⊆R}(−1)^{|R∖S|}Λ(S). With Λ(∅) = λ_{∞,P}(T) < 0 for T ≥ 0.60 (CITED),
     positivity at the full set requires Σ_{R≠∅}Λ̂(R) ≥ |λ_{∞,P}(T)|. Since λ is a minimum (non-linear), Λ̂(R) ≠ 0 for
     |R| ≥ 2 in general: positivity is carried by genuine multi-prime interactions.

## 3. Basic properties (PROVED)
(P1) Monotonicity fails: λ is not monotone in any t_p (comb_p has an atom at log p, and δ_{log p} ∉ ±𝒦_T^*,
     N_BUILD_007 §1(iv)): there are F with c_F(log p) > 0 and others with < 0.
(P2) Single-prime interactions are bounded: |Λ({p}) − Λ(∅)| ≤ 2Σ_k v_{p^k} (|c_F| ≤ ‖F‖²).
(P3) The amplification direction w = α·1 (Z^α) has λ concave in α with λ → −∞ as α → ∞ (finmod(ii) argument) and
     λ(0) < 0; so λ(1) > 0 holds iff the concave function α ↦ λ(α·1) is positive at α = 1, i.e. 1 lies in the
     (open) positivity interval (α₋, α₊) ∋ 1 with α₋ > 0. (Restatement.)
(P4) FE enters only through A4: the coefficient-1 condition singles out t = 1 among all Euler products.

## 4. Test against the input map (011)
- a_P = 1_{p≥P}: a vertex of the cube, Euler, not in 𝔓 → the object distinguishes it (A4). ✓
- Epstein/DH: not Euler products → not in the cube at all. ✓
- Beurling: not ℤ-integral frequencies → not in 𝔄_T's {log n} lattice → not in the cube. ✓
- M_m (zero-side forms), W-tail (tail modifications): not in the cube (no Euler factorization / tail-blind). ✓
So the cube with its distinguished point passes every discrimination test.

## 5. Review — what the object is and is not
- The passes in §4 are BY IDENTIFICATION: A4 shows the Euler ∩ Poisson locus is the single point t = 1, i.e. ζ's
  window comb. By crossword I5 (W-identification), a property set identifying ζ reduces the question to D for ζ
  unchanged. This is not a stop criterion, but it means the object has content only through a QUANTITATIVE
  statement relating λ at t = 1 to the geometry of the cube around it.
- (A2) corrected in writing: concavity is in w = (t_p^k), not in t. PROVED.
- (A6)/(P3) are restatements; their value is structural: positivity must be a multi-prime interaction effect at the
  integral FE-vertex, never a single-prime or monotone effect (P1, P2). This is consistent with Theorem X (R183/185:
  new primes must cancel σ on U at resolution π/T) and gives it a combinatorial shape.
- Genuinely new candidate statement (OPEN), to make the object quantitative:
  (Q) an "integral vertex dominance" inequality bounding λ(1) below by the values of λ at the Hamming neighbours
      1 − e_p plus explicit single-prime corrections (a discrete recursion over the prime lattice, with A4 fixing the
      terminal vertex). It is NOT yet a well-formed statement: the correction term must be chosen so that it is not
      a monotone/inertia statement (P1, I7) and not killed by Prop 0 of 013. Recorded only as the direction for 015.
- No sign certified; no negative value of 𝔞_T for ζ.
