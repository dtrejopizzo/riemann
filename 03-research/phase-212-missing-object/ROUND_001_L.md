# ROUND_001_L — Rigidity of Carathéodory-type comparators on the power ladder

Global status: **PROVED** (relative to three classical CITED theorems, stated in §1) the rigidity lemma
L-comp in the class "Carathéodory-type comparator on the same carrier"; **PROVED** its unconditional
exclusion form; **CONDITIONAL** the converse (existence of admissible comparators).
It is not a sign step: it contributes no positivity of the form. No paper or other file modified.

Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`, `POWER_CONE_001.md`, `POWER_BRIDGE_002.md`.
Cited as "211/GLOBAL" = `../phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, "211/HYP" =
`../phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`.

## Cross-check

**(1) Closest antecedent.** 211/GLOBAL, "Small hyperbolic comparison: necessary vanishing
condition" and "Closing of the small hyperbolic comparison": for ONE comparator (the hyperbolic model
a = 2π) it is proved that K_Phi ≥ εK_h ⟹ U_Phi = 0, and an interval certificate gives U_Phi ≠ 0. §6 of this
memo checks that this necessary condition is literally that of L-comp for that comparator. Other
more distant antecedents:
- 211/GLOBAL, "Reusable general filter": if D = o(1/u) and K_D is PSD on pairs, D ≡ 0 (rigidity at
  infinity, only 2×2 blocks, without boundary measure).
- 211/GLOBAL, "Primitive comparisons: analytic transfer of the discard": PSD on primitive
  blocks of an interval ⟹ full PSD, for odd real-analytic D (used in §7.4).
- 211/GLOBAL, comparisons K_Phi − K_(2π) and K_Phi − K_asinh (only ε = 1, by certified jet minors).
- Index: README line 1791 ("POWER uses its real Pick-type kernel"); 04_PHASES_100-189 rows
  G2F-phase-102/115,116 ("positive boundary measure", reformulation), G1F-R160_S3 §2.1#2, G7F-R162_803;
  CW D-16. All record Herglotz-type positivity as a reformulation of the target; none
  states a rigidity of comparators.
- Paper 20 thm:boundary: unconditional boundary identity (re-proved in §0 for M, in two lines).
- P47 thm:noimport / IDX CPOS_CLASS_001: "imported positivity" for constructions uniform in the
  comb; different hypothesis class (uniformity in the datum), does not use the boundary measure.
- Search for "medida de borde", "boundary measure", Herglotz, Carathéodory, Pick, Nevanlinna in the
  index, the grid, the crossword, P48 and phase 211: no statement of the general lemma. A search
  without matches does not prove novelty; the principle used (uniqueness of the integral representation of
  a real-positive function) is classical and no novelty is attributed to it.

**(2) New claim with respect to the corpus.** The general statement: for EVERY Carathéodory-type
comparator and every ε > 0, the domination K_M − εK_{M0} ⪰ 0 on a uniqueness set (the
ladder 31.5 + n suffices) forces M0 = Σ_k m_k·2u/(u² + τ_k²) with iτ_k poles of M on the imaginary axis and
0 ≤ m_k ≤ r_k/ε; no linear term, no continuous part, no foreign atoms. Its contrapositive is
unconditional. New corollary: K_M − ε·K_asinh is not PSD for ANY ε > 0 (the corpus only had
ε = 1), without numerical certificate.

**(3) Why it avoids the difficulty of the antecedent.** The antecedent needed, for each comparator, an
operator realization of the model, continuity in H_η, the identity W_Phi[Phi] = 0 and a certificate.
Here the necessary condition comes from the uniqueness of the boundary measure and holds for the whole class
at once. It does not avoid, nor claim to avoid, the final certificate when the comparator is purely atomic
(§6.2): deciding whether a concrete atom of the model is or is not a pole of M remains a computation.

**(4) Connection with global positivity.** None as a sign step. It is a design restriction
(OBJECT_SPEC §3): within the Carathéodory class, the space ℋ of a Gram realization of the ladder
kernel is a weighted subspace of L²(μ_M), with μ_M the boundary measure of M. It knowingly falls into
RULES_AVOID B4 as a discard tool, not as a route.

## 0. Objects and starting facts

Π = {Re u > 0}. H(u) = ½a(a−1)π^{−a/2}Γ(a/2)ζ(a) with a = u + ½; M = H′/H, so that
M(u) = L(u + ½) with the L of POWER_CONE_001 §1. For f defined on a set of nodes X ⊂ (0,∞),

    K_f(u,v) = [f(u) + f(v)]/(u + v),   u, v ∈ X.

The kernel is linear in f: K_M − εK_{M0} = K_{M−εM0}.

**F1 (CITED, POWER_CONE_001 §2, §7).** H is entire, even, real on ℝ, and H(u) = C∫_0^∞ Φ(t)cosh(ut)dt
with C > 0, Φ > 0. In particular H > 0 on ℝ, M is meromorphic on ℂ, odd, real-analytic on all of ℝ,
M(0) = 0, and M is holomorphic on Re u > ½.

**F2 (PROVED). Boundary identity.** For real τ with H(iτ) ≠ 0, Re M(iτ) = 0.
Proof. H even and real on ℝ gives H(iτ) = H(−iτ) = conj H(iτ), hence τ ↦ H(iτ) is real; its derivative
iH′(iτ) is real, hence H′(iτ) ∈ iℝ and M(iτ) ∈ iℝ. ∎ (It is thm:boundary of Paper 20 in the variable u;
it only uses parity and reality of H.)

**F3 (PROVED). Poles.** The poles of M are simple, with integer residue r ≥ 1 (order of vanishing of H
at the point). The poles on the imaginary axis form a discrete set {±iτ_k}, τ_k > 0, symmetric
(M odd), and 0 is not a pole (H(0) > 0). Write r_k for the residue at ±iτ_k. Nothing is claimed or used
about the existence or absence of poles of M in 0 < Re u ≤ ½.

**F4 (PROVED). Growth.** (a) M(x) = O(log x) for real x → +∞. (b) |M(u)| ≤ C(1 + |u|) on
Re u ≥ 3/2.
Proof. With a = u + ½, Re a ≥ 2: |1/a| + |1/(a−1)| ≤ 2; |ζ′/ζ(a)| ≤ ΣΛ(n)n^{−2} < ∞; and for
Re z ≥ 1, ψ(z) = −γ + Σ_{k≥0}(z−1)/((k+1)(k+z)) with |k+z| ≥ k+1 gives |ψ(z)| ≤ γ + (π²/6)|z−1|. This
proves (b). For (a), for real z > 0 one has log z − 1/z ≤ ψ(z) ≤ log z (the bounds used in
POWER_CONE_001 §5). ∎

## 1. Classical tools (CITED)

A function F is **real-positive** (Carathéodory) on Π if it is holomorphic on Π with Re F ≥ 0.

**C1 (CITED, Herglotz–Riesz representation on the half-plane).** F is real-positive on Π if and only if

    F(u) = iβ + c·u + ∫_ℝ [1/(u − iτ) − iτ/(1+τ²)] dμ(τ),

with β real, c ≥ 0 and μ a positive measure with ∫dμ/(1+τ²) < ∞. The triple (β, c, μ) is unique:
c = lim_{x→+∞} F(x)/x, and μ is the weak-* limit of (1/π)Re F(σ + iτ)dτ as σ ↓ 0 (Stieltjes
inversion on continuous functions of compact support). μ is the **boundary measure** of F. If F is real
on (0,∞), then β = 0, μ is even and F(u) = c·u + ∫ u/(u²+τ²) dμ(τ).

**C2 (CITED, Pick's theorem, finitely many nodes).** Let u_1,…,u_n ∈ Π be distinct and w_1,…,w_n ∈ ℂ. There exists F
real-positive on Π with F(u_i) = w_i if and only if the matrix [(w_i + conj w_j)/(u_i + conj u_j)] is
positive semidefinite. (It is the Carathéodory form of the Nevanlinna–Pick theorem; it is obtained from the
disc form with z = (u−1)/(u+1), S = (F−1)/(F+1), via
(1 − S(u)conj S(v))/(1 − z conj z′) = [(u+1)/(F(u)+1)]·conj[(v+1)/(F(v)+1)]·(F(u)+conj F(v))/(u+conj v);
the factor is defined because the PSD diagonal forces Re w_i ≥ 0.)

**C3 (CITED, Blaschke condition for bounded type).** If G ≢ 0 is a quotient of two bounded holomorphic
functions on Π, its zeros u_n satisfy Σ Re u_n/(1+|u_n|²) < ∞. Every real-positive F is of
bounded type: F = (1+S)/(1−S) with |S| ≤ 1, S ≢ 1.

**Lemma 1.1 (PROVED). Easy direction with explicit Gram.** If F is real-positive with data (β, c, μ),

    [F(u) + conj F(v)]/(u + conj v) = c + ∫ dμ(τ)/[(u − iτ)·conj(v − iτ)],   u, v ∈ Π,

which is a Gram in ℂ ⊕ L²(μ). Proof: add the representations C1 and use
1/(u−iτ) + 1/(conj v + iτ) = (u + conj v)/[(u−iτ)(conj v + iτ)]. ∎

**Definition (uniqueness set).** X ⊂ (0,∞) is a uniqueness set if
(i) X has an accumulation point in (0,∞), or
(ii) Σ_{u∈X, u≥2} 1/u = ∞.

**Lemma 1.2 (PROVED). The ladder is a uniqueness set.** X = {31.5 + n : n ≥ 0} satisfies (ii) (harmonic series).
Moreover, in both cases Σ_{u∈X} u/(1+u²) = ∞ (since x/(1+x²) ≥ 1/(2x) for x ≥ 1), and for every c ≥ 0 the
translated set {u − c : u ∈ X, u > c + 1} still fails the Blaschke condition of Π in
case (ii). ∎

The condition is also necessary for uniqueness in the bounded class: if Σ u/(1+u²) < ∞ the
Blaschke product of X exists (CITED), and the conclusion of Theorem 3.1 is no longer determined by X.

**Lemma 1.3 (PROVED). Pick on infinite sets and uniqueness.** Let X ⊂ (0,∞) be a uniqueness set and f: X → ℝ.
If K_f is PSD on every finite subset of X, there exists a unique real-positive F on Π with F|_X = f;
moreover F is real on (0,∞).
Proof. Uniqueness: if F_1, F_2 interpolate, F_1 − F_2 is of bounded type and vanishes on X, which violates the
Blaschke condition; by C3, F_1 = F_2. Existence, X countable: let x_1, x_2,… be an enumeration and F_n
real-positive with F_n(x_j) = f(x_j), j ≤ n (C2). The S_n = (F_n − 1)/(F_n + 1) are bounded by 1;
by Montel a subsequence converges locally uniformly to S with |S| ≤ 1 and
S(x_j) = (f(x_j)−1)/(f(x_j)+1) ≠ 1, hence S ≢ 1 and F = (1+S)/(1−S) is real-positive and interpolates.
X uncountable: choose X′ ⊂ X countable and a uniqueness set, with interpolant F; for x ∈ X, the interpolant
of X′ ∪ {x} coincides with F by uniqueness, hence F(x) = f(x). Reality: conj F(conj u) also interpolates;
by uniqueness it coincides with F. ∎

## 2. General theorem (no hypothesis on M or on the comparator)

**Theorem 2.1 (PROVED, relative to C2–C3).** Let X ⊂ (0,∞) be a uniqueness set, M0: X → ℝ arbitrary, ε > 0.
The following are equivalent:
(a) K_M − εK_{M0} is PSD on every finite subset of X;
(b) there exists F real-positive on Π, real on (0,∞), with M − εM0 = F on X.
In that case F is unique.
Proof. (a)⟹(b) is Lemma 1.3 with f = (M − εM0)|_X; (b)⟹(a) is Lemma 1.1 restricted to X. ∎

**Corollary 2.2 (PROVED). Case M0 = 0; reformulation already recorded.** The blocks of the ladder
[(L(32+i)+L(32+j))/(63+i+j)] are PSD for every size if and only if M is real-positive on Π.
Proof. If they are PSD, there exists real-positive F with F = M on the ladder. By F4(b), M/(u+1) is bounded on
Re u > 3/2, hence M − F is of bounded type there and vanishes on a set that violates Blaschke (Lemma 1.2):
M = F on Re u > 3/2, and by the identity theorem for meromorphic functions on the connected Π, M = F on Π.
Converse: Lemma 1.1. ∎
This is the reading "real Pick-type kernel" already noted in the index (README line 1791); it is used here
as a tool and is not presented as progress (RULES_AVOID B3).

## 3. Rigidity of real-positive comparators

**Theorem 3.1 (PROVED, relative to C1–C3; no hypothesis on the sign of K_M).** Let X ⊂ (0,∞) be a
uniqueness set (for example the ladder 31.5 + n, or any interval), ε > 0, and M0 real-positive on Π,
real on (0,∞), with Herglotz data (c_0, μ_0). If K_M − εK_{M0} is PSD on every finite subset of
X, then:

1. M − εM0 extends to a real-positive function F on Π; in particular M has no poles in Π and
   Re M ≥ 0 on Π (and hence K_M is PSD at all nodes of Π: the hypothesis contains the sign of the
   whole ladder).
2. The boundary measure of M is purely atomic: μ_M = Σ_k r_k(δ_{τ_k} + δ_{−τ_k}), with ±iτ_k the
   poles of M on the imaginary axis and r_k their residues; the linear coefficient of M is c_M = 0.
3. c_0 = 0 and εμ_0 ≤ μ_M. That is,

       M0(u) = Σ_k m_k · 2u/(u² + τ_k²),   0 ≤ m_k ≤ r_k/ε,   Σ_k m_k/(1+τ_k²) < ∞.

   In particular μ_0 has no absolutely continuous nor singular continuous part, no atoms outside
   {±τ_k}, no atom at 0, and M0 has no linear term.

Proof.
*Step 1.* By Theorem 2.1 there is real-positive F with M − εM0 − F = 0 on X. Let G = M − εM0 − F.
Case (i): G is meromorphic on Π (M is; M0 and F are holomorphic) and vanishes on a set with an
accumulation point x* ∈ (0,∞), which is not a pole of G (F1: M is holomorphic on the real axis); G ≡ 0 on Π.
Case (ii): on Re u > 3/2, M is of bounded type (F4(b): M/(u+1) bounded and 1/(u+1) bounded) and so are M0, F
(C3); G is of bounded type on that half-plane and vanishes on {u ∈ X, u > 5/2}, which violates the Blaschke
condition of the half-plane Re u > 3/2 (Lemma 1.2). Hence G ≡ 0 on Re u > 3/2 and, by the identity theorem for
meromorphic functions on Π, G ≡ 0 on Π. In both cases M = εM0 + F on Π: the right-hand side is holomorphic
with real part ≥ 0. This gives 1.
*Step 2.* M is now real-positive, real on (0,∞); by C1, c_M = lim M(x)/x = 0 (F4(a)). Let φ be continuous
with compact support in an open interval J of the axis without poles of M. M is holomorphic in a neighbourhood of
i·supp φ, hence Re M(σ+iτ) → Re M(iτ) = 0 uniformly on supp φ (F2), and ∫φ dμ_M = 0. Near a pole
iτ_k, M(u) = r_k/(u − iτ_k) + g(u) with g holomorphic; Re g(iτ) = 0 for nearby τ ≠ τ_k (F2 and
Re[r_k/(i(τ−τ_k))] = 0), and by continuity also at τ_k. For φ supported near τ_k,

    ∫φ dμ_M = lim_{σ↓0} (1/π)∫φ(τ)·r_kσ/(σ² + (τ−τ_k)²)dτ + 0 = r_kφ(τ_k).

By a partition of unity, μ_M = Σ r_k(δ_{τ_k}+δ_{−τ_k}); 0 is not a pole (F3). This gives 2.
*Step 3.* M = εM0 + F with all three real-positive; by uniqueness in C1, c_M = εc_0 + c_F and
μ_M = εμ_0 + μ_F with c_F ≥ 0, μ_F ≥ 0. Hence c_0 = 0 and εμ_0 ≤ μ_M. A positive measure dominated by
a purely atomic one is atomic with atoms at the same points and smaller masses; μ_0 even and C1 give the
formula of 3. ∎

**Remark 3.2 (PROVED). Space of the realization.** Under the hypothesis of the theorem, the Gram of
Lemma 1.1 for the comparator is K_{M0}(u,v) = Σ_k m_k[1/((u−iτ_k)(v+iτ_k)) + 1/((u+iτ_k)(v−iτ_k))]:
it lives in ℓ² over the poles of M on the axis, with weights m_k ≤ r_k/ε. A Carathéodory-type space ℋ that
minorizes the target cannot come from a model whose boundary spectrum is not a part of that set.

## 4. Unconditional form and conditional converse

**Corollary 4.1 (PROVED, unconditional). Exclusion.** Let M0 be real-positive on Π, real on (0,∞), and
suppose one of:
(E1) c_0 > 0;
(E2) μ_0 has a non-zero continuous part (absolutely continuous or singular continuous);
(E3) μ_0 has an atom at a point τ* such that iτ* is not a pole of M (including τ* = 0);
(E4) μ_0({τ_k}) > r_k/ε for some pole iτ_k of M.
Then, for that ε (in E1–E3, for every ε > 0) and for each uniqueness set X, there exist a finite block
of nodes in X and a real vector with negative energy for K_M − εK_{M0}. In particular this happens
with nodes on the ladder 31.5 + n.
Proof. Contrapositive of Theorem 3.1. ∎
Nothing is assumed or concluded about the sign of K_M; the size of the block and the vector are not given.

**Proposition 4.2 (CONDITIONAL on "M real-positive on Π", that is, on the sign of the ladder,
Cor. 2.2). Converse.** If M is real-positive on Π, then M = Σ_k r_k·2u/(u²+τ_k²) and, for every
choice 0 ≤ m_k ≤ r_k/ε, M0 = Σ m_k·2u/(u²+τ_k²) satisfies K_M − εK_{M0} ⪰ 0 at all nodes of Π.
Proof. Step 2 of Theorem 3.1 (which only uses that M is real-positive) gives the representation of M; then
M − εM0 = Σ(r_k − εm_k)·2u/(u²+τ_k²) is real-positive and Lemma 1.1 applies. ∎

**Summary of what is conditional and what is unconditional.**
- Unconditional: Theorem 3.1 (implication) and Corollary 4.1 (exclusion). The hypothesis "PSD difference
  with real-positive M0" does NOT need to assume M real-positive: it implies it (trivially, since
  K_M = (K_M − εK_{M0}) + εK_{M0}; the content of the theorem is the passage from the nodes to Π and the measure).
- Conditional: that some non-zero real-positive comparator exists. One exists if and only if M is
  real-positive on Π and has at least one pole on the axis (PROVED as an equivalence; neither of the two
  sides is asserted).
- If M0 is not real-positive (comparator with K_{M0} not PSD), only Theorem 2.1 holds: the conclusion is
  "M − εM0 is real-positive", without domination of measures, because M0 has no positive boundary measure.
  If moreover M0 is meromorphic on Π and X is of type (i), then M0 = (M − F)/ε on Π: M0 has on Π
  exactly the poles of M, with residues r/ε (PROVED, identity of meromorphic functions).

## 5. Infinity and linear term

- **PROVED.** c_M = 0 by F4(a), without hypothesis. Hence c_0 = 0 and c_F = 0 in every domination: no
  comparator with linear term c_0·u, c_0 > 0, is admissible. The kernel of c_0·u is the constant c_0
  (rank one, vector of ones): K_M − ε·c_0·𝟙𝟙ᵗ is never PSD in all sizes of a
  uniqueness set.
- **PROVED.** At the origin: M(0) = 0 and M is analytic at 0; there is no atom at τ = 0. A comparator with
  term m/u, m > 0 (atom at 0) is excluded for every ε.
- **PROVED.** The logarithmic growth M(x) ~ ½log x does not contradict c_M = 0: for a
  real-positive function with c = 0, F(x) = ∫x/(x²+τ²)dμ can grow like log x if μ([−R,R]) ~ R log R.
- Relation with the "Reusable general filter" of 211/GLOBAL (D = o(1/u) and PSD pairs ⟹ D ≡ 0): it is
  the case where F = D has c_F = 0 and zero total mass; here one obtains with all sizes the
  stronger conclusion (F is determined by its measure), at the price of asking for all sizes.

## 6. The small hyperbolic comparison of phase 211 as an instance

**6.1 (PROVED). Same type and same carrier, without intermediate congruence.** In 211, K_Phi is K_f with
f = M_Phi = Z_Phi′/Z_Phi, Z_Phi(u) = ∫Φ(t)e^{ut}dt; by F1, Z_Phi = H up to a positive constant, hence
M_Phi = M (also checked against the expansion ½log(u/2π) + 7/(4u) + … of 211/GLOBAL: the terms
2/u of 1/a + 1/(a−1) and −1/(4u) of ½ψ(a/2) add up to 7/(4u)). K_(2π) is K_f with f = M_a = Z_a′/Z_a,
a = 2π, on the same positive real nodes ("blocks of rates u > ½"). Both are kernels
[f(u)+f(v)]/(u+v) on the same carrier. The only congruence present in the ladder is the diagonal one
d_i = c_iζ(u_i+½) of POWER_CONE_001 §1, common to both kernels; a common invertible congruence
preserves the PSD order of the difference in each block, so the statement does not change.

**6.2 (PROVED). Boundary measure of the model.** By 211/HYP §4 (REP), M_a(u)/u = ½Tr(H_a + u²/4)^{-1}
with H_a = −D_r² + a²e^{2r} (Dirichlet at 0), positive, with trace-class resolvent. With eigenvalues
λ_1 ≤ λ_2 ≤ … and ω_k = 2√λ_k,

    M_a(u) = Σ_k 2u/(u² + ω_k²),

real-positive with c = 0 and μ_a = Σ_k(δ_{ω_k} + δ_{−ω_k}): purely atomic, masses 1.

**6.3 (PROVED). Coincidence of the necessary conditions.** Theorem 3.1 gives:
K_M ⪰ εK_a on the ladder ⟹ for every k, iω_k is a pole of M with residue ≥ ε; that is G(ω_k) = 0
for every k, with G(ω) = 2∫_0^∞Φ(t)cos(ωt)dt = H(iω)/C′. The condition of 211 is U_Phi = 0 with
U_Phi = ∫Φ(t)exp(2it√H_a)dt, which by functional calculus and parity of Φ is equivalent to G(ω_k) = 0 for
every k. They are the same condition. The closing of 211 (G < −10⁻⁸ on [17, 41/2] ∋ ω_1, certified) is
then exactly the verification of (E3) of Cor. 4.1 at the first atom of the model.
What Theorem 3.1 adds: (a) it holds for every a > 0 and for the Robin variants and the sums
w·b·M_{a,β}(bu) of 211/GLOBAL, without redoing the chain of density and continuity in H_η nor using
W_Phi[Phi] = 0; (b) the ladder suffices; (c) the bound on residues (for ε > 1 it requires r_k ≥ ε).
What it does NOT replace: the certificate that a concrete atom of the model is not a pole of M. For a
purely atomic comparator the exclusion still requires that pointwise datum. **NUMERICAL/CITED** the
certificate of 211; it is not recomputed.

**6.4 (PROVED). asinh comparator: exclusion for every ε without certificate.** M_0(u) = ½asinh(u/c),
c = 4π. asinh maps Π conformally onto {Re w > 0, |Im w| < π/2} (sinh(x+iy) = sinh x cos y +
i cosh x sin y), hence M_0 is real-positive. On the boundary, asinh(iτ/c) = arccosh(|τ|/c) + i·sgn(τ)π/2
for |τ| > c: μ_0 has density (1/2π)arccosh(|τ|/c) > 0 on |τ| > c. It is absolutely continuous and
non-zero: (E2). By Cor. 4.1, K_M − ε·K_{M_0} is not PSD for any ε > 0, with a negative block on the
ladder. The corpus only had ε = 1 (jet minor with interval certificate).

## 7. Scope: what the lemma does NOT cover

7.1 **PSD comparators that are not of Carathéodory type (PROVED that the general class has no rigidity).**
If N(u,v) is any PSD kernel, K_M − εN ⪰ 0 imposes nothing of the above kind: if K_M is PSD
and non-zero, N = g⊗g with g = K_M(·,w) and ε = 1/K_M(w,w) satisfies the domination (Cauchy–Schwarz in the
reproducing space); conversely any domination of a PSD kernel gives K_M PSD. Thus "there exists a non-zero PSD N
dominated" is equivalent to "K_M PSD and non-zero": the general class does not restrict the design and Theorem 3.1 says
nothing about it.

7.2 **Carathéodory-type comparators after a NON-common congruence.** Kernels
g(u)g(v)[M0(u)+M0(v)]/(u+v) with non-constant g, or comparators that are of Carathéodory type in another
coordinate (for example in the coefficients c_i and not in d_i = c_iζ(u_i+½), or in x = u²), are not
differences K_{M−εM0}; not covered. The common congruence is covered (§6.1).

7.3 **Joint compensations.** Decompositions K_M = Σ_j N_j with summands without individual sign, or
K_M − εK_{M0} + (correction) with non-PSD correction, fall outside: the theorem only treats the difference
of two kernels of the type. Nor does it cover signed comparators (M0 not real-positive) beyond
Theorem 2.1.

7.4 **Restriction to primitive blocks (CITED + PROVED).** If M0 is moreover odd and real-analytic on
all of ℝ (for example μ_0 with a gap around 0, like M_a and asinh), the lemma "Primitive
comparisons" of 211/GLOBAL (c = ½) gives: PSD of K_{M−εM0} on the primitive blocks of an open interval
I ⊂ (½,∞) ⟹ full PSD. Then Theorem 3.1 and Cor. 4.1 also hold with the
hypothesis restricted to primitive blocks of an interval. For the discrete ladder with the two
moment restrictions the cited lemma does not apply as is (it asks for an interval): **OPEN**.

7.5 **Node sets that only accumulate at 0.** If X ⊂ (0,∞) only accumulates at 0 with Σu = ∞,
uniqueness is obtained by working on a half-disc {|u| < δ, Re u > 0}, where M is bounded and the
Blaschke condition for real points tending to 0 is Σu < ∞. **ARGUED** (the conformal map is not
written); not needed for the ladder.

7.6 **Dominations in a finite number of sizes or on Blaschke nodes.** If Σ_{u∈X}u/(1+u²) < ∞
(for example nodes 2^n), the interpolant is not unique and there is no rigidity. Blocks of bounded size:
nothing.

7.7 **Fixed window.** The lemma lives on the power ladder (all windows at once). It says
nothing about comparators of the form a_T for a fixed T.

## 8. Falsifier battery

The lemma is not a sign step; it is indicated which line uses each structure, so that it is not read as one.
- Theorem 2.1 and Step 1 of Theorem 3.1 hold for any M meromorphic on Π, real on (0,∞) and
  of bounded type on some half-plane Re u > c: they are generic (RULES_AVOID B1) and carry no sign.
- Steps 2–3 (atomic measure) only use F2 (parity of H) and F4(a). Hence they hold identically
  for every model with the same symmetry: Davenport–Heilbronn, Epstein, quartets and f_t. In those
  models the theorem remains true as an implication; what changes is that its hypothesis is empty
  when the M of the model has poles in Π. It does not distinguish those models by itself: correct for a
  discard tool, insufficient as a mechanism.
- For cΛ (c ≠ 1), a_P, finite deletion and amplification, b_θ and Beurling systems without symmetry:
  F2 fails (the corresponding function is not H′/H with H even; Re M(iτ) no longer vanishes), and with it Step 2:
  the boundary measure, if it exists, is not purely atomic. Theorem 2.1 still holds.

## 9. Consequence for OBJECT_SPEC §3

The working conjecture L-comp is **correct in its class** and must be read as follows:

- **PROVED.** On the power ladder, a space ℋ coming from a Carathéodory-type comparator
  on the same carrier (K_M = ε·K_{M0} + PSD Carathéodory-type remainder) is
  necessarily ℓ² over a part of the poles of M on the imaginary axis, with weights ≤ r_k/ε, without
  continuous or linear component. No exterior model with continuous boundary measure (asinh) or with an
  atom outside the poles of M (hyperbolic a = 2π) serves, for any ε.
- **PROVED.** Outside that class the restriction does not exist (§7.1): general PSD comparators are
  admissible as soon as the target is true, and they give no prior information.
- Precision to the text of OBJECT_SPEC §3: "the boundary measure of M, which is purely atomic" is a
  conclusion under the domination hypothesis (or under "M real-positive"), not an unconditional fact;
  what is unconditional is Re M(iτ) = 0 outside the poles (F2) and the exclusion form (Cor. 4.1).
  Moreover the linear term is excluded (c_0 = 0), not merely bounded.

## Result

**PROVED** piece (rigidity lemma, relative to the classical C1–C3) and **NO-GO with class**: class =
comparators real-positive on Π, real on (0,∞), compared with the ladder kernel on the same
carrier (or after a common congruence), with domination in all sizes on a uniqueness set.
Within the class only the atomic sub-sums of M are admissible; outside the class the lemma says
nothing. It is not a candidate for construction and contributes no sign.

## What was proved

1. F2: Re M = 0 on the imaginary axis outside the poles (PROVED, unconditional).
2. Lemma 1.2: the ladder 31.5 + n is a uniqueness set (violates Blaschke) (PROVED).
3. Theorem 2.1: domination on X ⟺ M − εM0 coincides on X with a unique real-positive function (PROVED rel. C2–C3).
4. Theorem 3.1: rigidity with real-positive comparator; c_0 = 0, εμ_0 ≤ μ_M atomic (PROVED rel. C1–C3).
5. Corollary 4.1: unconditional exclusion form (E1)–(E4) (PROVED).
6. Proposition 4.2: converse (CONDITIONAL on M real-positive).
7. §6: the small hyperbolic comparison of 211 is an instance with the same necessary condition;
   asinh is excluded for every ε without certificate (PROVED).
8. §7.1: the general PSD class has no rigidity (PROVED).

## What failed and why

- No certificate-free exclusion is obtained for purely atomic comparators (hyperbolic model):
  the condition is "each atom of the model is a pole of M", and deciding it at an atom is a pointwise datum about
  G(ω_k) that the lemma does not produce.
- Rigidity is not extended to the discrete ladder with the two primitive restrictions (§7.4): the available
  continuation lemma asks for an interval. **OPEN.**
- There is no rigidity for general PSD comparators nor for joint compensations (§7.1, §7.3): it is not a
  defect of the proof, it is false that there is.
- C1–C3 are cited as classical theorems; they are not re-proved here. §7.5 remains ARGUED.

## Next concrete step

Adjust OBJECT_SPEC §3 to the statement of §9 (exact class; linear term excluded; "purely atomic"
as a conditioned conclusion) and use Cor. 4.1 as a prior filter for every candidate whose ℋ_T is of
Carathéodory type on the ladder: it must exhibit its boundary measure and show that it is an atomic sub-sum
of that of M, or declare itself outside the class (§7.1–7.3) and say through which of the three exits. Record the
NO-GO with its class in the routes index and in the grid (this memo does not edit them).
