# Round 1, candidate K4 — non-linear multiscale inequality with Λ beyond the window

Selection memo. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`; N = e^{2T}, X = e^{2T_0},
0 < T_0 < T. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO.

Result in advance: **no new mechanism**. The object could not be written. Delivered are (a) the precise
statement of what the cell asks for, with all quantifiers; (b) a PROVED classification of
"partial completeness beyond X" in the class of linear atoms with convex constraints, which closes
that direction as a source of sign (NO-GO PROVED in one case, total identification in another, and in the
third a statement strictly stronger than (★) with explicit margin); (c) the two-scale identity of
degree two written out, with the proof that it is linear in the new contacts for N ≤ X² and
that the form does not see the degree in Λ.

## 0. Cross-check

Sources consulted: IDX `06_OPEN_RESIDUES_DEAD_SUBROUTES.md` R7; IDX `README.md` (phase 191, SPEC_A and
SPEC_B; semiring principle); IDX `04_PHASES_100-189.md` (rows localized N′, R185-circ,
G3A-R166_802); GRID §8 entries 28 and 30 of the phase 186 register; CW §3.3 (closure), §4.2 (U1), §5 and
later appendix; P48 "Statements weaker in appearance", "The live gate", tab:signobject (hierarchical
contact ladder); P47 lem:shape-ident, thm:shape, cor:void, prop:wit-sens, lem:degen,
thm:geo-split, thm:X, thm:noimport, rem:conjunctions, rem:spec-scope; `phase-186-toolbox/R186_005`
(with the correction of `R186_092`); `phase-185-*/R185_004`; 211 `SQUARE_COMPLETENESS_OBSTRUCTION.md` §§1–2,
`POWER_CORPUS_OPPORTUNITY_AUDIT.md` (row "Partial completeness outside a window"), `LEDGER.md` C43,
C45, C47, `POWER_DESCENT_016.md` §2, `POWER_RECURRENCE_BOUNDARY_036.md` §7.

**(1) Closest antecedent.**
- `phase-186-toolbox/R186_005_DEGREE_TWO_SELBERG.md`: Lemma S0 (the degree-two identity
  μ_b ∗ (N_b log²) = b·log + b∗b holds for every b with its own system (N_b, μ_b)), Lemma S1
  (triangularity), Theorem TB3-neg (what is closed by deletion beyond X does not decide; what uses
  total completeness identifies) and §5: "only partial completeness beyond X survives …
  OPEN; there is no candidate". The note of `R186_092` corrects item (ii) of that theorem.
- `phase-185-*/R185_004`, Theorem U3 (deletion or identification) and Lemma 3 (exact completeness).
- P47 thm:geo-split: positivity on a class containing Λ splits into the sign at Λ plus a
  rigidity property without sign.
- 211 `SQUARE_COMPLETENESS_OBSTRUCTION.md`: a concrete family of partial completeness (perfect
  powers) contains a negative member.
- IDX README, phase 191, SPEC_A (exact induction in T by contacts): NOT ADMISSIBLE.

**(2) New object or claim.** No object 𝒪 = (ℋ_T, V_T, ρ_T). New claims with respect to the
antecedents, all in the language of the form a_T:
- Theorem B (§3): for linear atoms (λ∗1)(n) = log n on an arbitrary set E ⊂ [X,N) and
  any closed convex constraint K, complete classification of the statement "a_T^λ ≥ 0 on P_T
  for every λ in the class". It is the step "specify E first" requested in
  `POWER_CORPUS_OPPORTUNITY_AUDIT.md`, solved for all E at once.
- Corollary C (§3): with support on prime powers and N ≤ X², exact combinatorial criterion in
  terms of E (divisors and exact valuations).
- Proposition D (§4): the two-scale identity of degree two is linear in the new contacts if
  N ≤ X²; the first term quadratic in new contacts appears at N > X² and lives on the semiprimes.
- Lemma A (§2): the degree in Λ is invisible to the form (a_T is affine in the comb and every polynomial fact
  about Λ on [2,N) is a consequence of the linear atoms).

**(3) Why the change avoids the difficulty of the antecedent.** It does not avoid it. R186_005 left open the branch
"partial completeness" for lack of an E; here it is proved that no E turns it into a mechanism: either
an atom stays free and the class contains a comb with negative form (PROVED, by unbounded
amplification, without using the sign of λ_A), or E identifies Λ on [2,N) and the statement about the class is
(★) at T with no added information, or the class is a bounded polytope containing Λ in its
relative interior and the statement is (★) with an explicit margin, which is stronger than (★). The design proposed in
the task (recursion X → X² with Σ_{d|n}Λ(d) = log n entering in degree two) falls into the recorded failures:
see §5.

**(4) Connection with global positivity.** There is no identity (G). The only connection proved is
negative: an identity (G) whose premises about the comb are completeness atoms on E and membership in
K gives positivity on the whole class Π(E,K) (transfer principle, §3), and by Theorem B that is only
compatible with clause O4 of `OBJECT_SPEC.md` if Π(E,K) = {Λ}.

**(5) Line that breaks for cΛ and a_P.** There is no sign step, hence no line to point to. For the
two-scale identity (I2) of §4, which is the only identity written: it breaks for cΛ, c ≠ 1, in the
datum g = μ∗log² (the left-hand side of (E2) equals c g + (c² − c)·Λ∗Λ at every n with (Λ∗Λ)(n) ≠ 0) and for
a_P in the same datum at the first n ≥ 2 with a prime factor smaller than P; but the version with their own (N_b, μ_b)
holds for both (Lemma S0 of R186_005), and (I2) contains no non-negative quantity. According to
`OBJECT_SPEC.md` §4, the candidate **is not ready for construction**.

The cross-check does not identify a literal repetition (the classification of §3 does not appear in the corpus), but it does
identify that the constructive design repeats SPEC_A and the compensation between scales without per-atom positivity. The
memo continues only to leave the classification and the precise statement of the cell PROVED.

## 1. Preliminaries

For a real vector b = (b(n))_{2 ≤ n < N} and real F ∈ P_T ∩ 𝒟_T,

    w_n(F) = 2 n^{−1/2} c_F(log n),   W[b](F) = Σ_{2 ≤ n < N} b(n) w_n(F),
    𝔪_T(F) = (1/2π) ∫ m |F̂|² dτ,    a_T^b(F) = 𝔪_T(F) − W[b](F),

so that a_T = a_T^Λ. For every F, the map b ↦ a_T^b(F) is affine.

**Lemma 1 (test atoms). PROVED.** Let 2 ≤ n_0 < N, ε ∈ {+1, −1}. There exists real F ∈ P_T ∩ C_c^∞(I_T),
F ≠ 0, with w_{n_0}(F) = 2 ε n_0^{−1/2}‖φ‖² ≠ 0 and w_n(F) = 0 for every n ≠ n_0, 2 ≤ n < N.

*Proof.* Let u = log n_0 ∈ (0, 2T) and η > 0 with u/2 + η < T and 2η < min(log 2, 1/N). Let φ be real, C^∞,
non-zero, supported in (−η, η) with A(φ) = B(φ) = 0 (two linear conditions in an infinite-dimensional
space). Set F(t) = φ(t + u/2) + ε φ(t − u/2). Then A(F) = (e^{−u/4} + ε e^{u/4}) A(φ) = 0, and
likewise for B; the support of F is in I_T. Moreover
c_F(s) = 2 c_φ(s) + ε c_φ(s − u) + ε c_φ(s + u), and c_φ is supported in (−2η, 2η). For 2 ≤ n < N,
log n ≥ log 2 > 2η, log n + u > 2η, and, if n ≠ n_0, |log n − u| ≥ log(1 + 1/m) > 1/(m+1) > 1/N > 2η with m = min(n, n_0) (since m + 1 < N). Hence
c_F(log n) = ε c_φ(0) = ε‖φ‖² if n = n_0 and 0 otherwise. ∎

**Corollary 1 (independence). PROVED.** If δ is a real vector on [2,N) and W[δ](F) = 0 for every
F ∈ P_T ∩ 𝒟_T, then δ = 0. If δ ≠ 0 there exists F with W[δ](F) > 0.

*Proof.* With δ(n_0) ≠ 0 and ε = sign of δ(n_0), Lemma 1 gives W[δ](F) = 2 |δ(n_0)| n_0^{−1/2} ‖φ‖² > 0. ∎

## 2. The degree in Λ is not visible to the form

Let R = ℝ[x_n : 2 ≤ n < N] and, for 2 ≤ n < N, the completeness atom

    κ_n(x) = Σ_{d | n, d ≥ 2} x_d − log n      (affine-linear polynomial).

**Lemma A. PROVED.** (i) The ideal (κ_n : 2 ≤ n < N) is the maximal ideal of the point Λ: it coincides with
(x_n − Λ(n) : 2 ≤ n < N). (ii) Consequently, every polynomial P ∈ R with P(Λ) = 0, of any degree,
is a combination with coefficients in R of the linear atoms κ_n. (iii) For E ⊂ [2,N) ∩ ℕ, the ideal
I_E = (κ_n : n ∈ E) is prime and is the ideal of all polynomials vanishing on the affine subspace
V(E) = {x : κ_n(x) = 0, n ∈ E}.

*Proof.* (i) By Möbius inversion on the divisor lattice,
x_n − Λ(n) = Σ_{d | n, d ≥ 2} μ(n/d) κ_d(x), using Σ_{d|n} μ(n/d) log d = Λ(n); and κ_n = Σ_{d|n, d≥2}
(x_d − Λ(d)). (ii) A polynomial vanishing at a point belongs to the maximal ideal of that point.
(iii) The linear system κ_n = 0, n ∈ E, is consistent (Λ solves it); after an affine change of coordinates
I_E = (y_1, …, y_r), which is prime and is the vanishing ideal of {y_1 = … = y_r = 0}. ∎

Reading. The degree-two identity Λ·log + Λ∗Λ = μ∗log², and any other polynomial relation among the
values Λ(n), n < N, adds no information to the linear atoms; the only thing that distinguishes one relation from
another is the set E of atoms of which it is a consequence. And since a_T^b(F) is affine in b, substituting a
polynomial relation in the comb term rewrites W[Λ] as W[b′] with b′ = Λ: the form only receives the
weight vector. A non-linearity in Λ that decides the sign has to be in the coupling of Λ with F
(in V_T F), not in a relation among the weights.

## 3. Classification of partial completeness

**Class.** Let E ⊂ [X, N) ∩ ℕ and K ⊂ ℝ^{[2,N)} closed convex with Λ ∈ K. Define

    D(E) = {δ : δ(n) = 0 for n < X,  Σ_{d | n} δ(d) = 0 for every n ∈ E}      (linear subspace),
    Π(E,K) = {λ ∈ K : λ = Λ on [2,X),  Σ_{d | n, d ≥ 2} λ(d) = log n for every n ∈ E} = (Λ + D(E)) ∩ K.

Π is the set of combs that share with Λ the data of scale X, completeness on E and the
properties K. The associated statement is

    (MS_{X,N,E,K})    a_T^λ(F) ≥ 0   for every λ ∈ Π(E,K) and every F ∈ P_T ∩ 𝒟_T.

**Transfer principle. PROVED.** Every deduction of "a_T^Λ ≥ 0 on P_T" whose only premises
about the comb are: its values on [2,X), the atoms κ_n = 0 with n ∈ E and membership in K, proves
(MS_{X,N,E,K}). In particular, if V^x and ρ^x depend polynomially on x, ρ^x(F) ≥ 0 for x ∈ K, and for
each F the polynomial a_T^x(F) − ‖V^x F‖² − ρ^x(F) belongs to I_{[2,X) ∪ E}, then
(MS_{X,N,E,K}) holds.

*Proof.* The premises hold for every λ ∈ Π. In the polynomial case, by Lemma A(iii) the
identity holds at every point of V([2,X) ∪ E) = Λ + D(E), and at the points of K the right-hand side is ≥ 0. ∎

For fixed F let h_Π(F) = sup_{λ ∈ Π} W[λ − Λ](F) ∈ [0, +∞].

**Theorem B. PROVED.**
(i) (MS_{X,N,E,K}) is equivalent to:  a_T(F) ≥ h_Π(F) for every F ∈ P_T ∩ 𝒟_T.
(ii) If Π is unbounded, (MS_{X,N,E,K}) is false: there exist λ ∈ Π and F ∈ P_T with a_T^λ(F) < 0. This uses
no hypothesis about the sign of λ_A.
(iii) h_Π ≡ 0 on P_T ∩ 𝒟_T if and only if Π = {Λ}. In that case (MS_{X,N,E,K}) is literally (★) in the
window T.
(iv) If Π is bounded and Π ≠ {Λ}, (MS_{X,N,E,K}) is equivalent to the positivity of a_T^λ at the extreme points
λ of Π, implies (★) at T and is strictly stronger in the following sense: there exists F ∈ P_T with
h_Π(F) > 0, and for every segment [Λ − sδ, Λ + sδ] ⊂ Π (s > 0) and all real F, G ∈ P_T ∩ 𝒟_T,

    s |W[δ](F)| ≤ a_T(F),        s |W[δ](F,G)| ≤ 2 (a_T(F) a_T(G))^{1/2},

where W[δ](F,G) is the symmetric bilinear form of W[δ].

*Proof.* (i) a_T^λ(F) = a_T(F) − W[λ − Λ](F); take the infimum over λ ∈ Π.
(ii) Π is convex, closed and unbounded, hence it has a recession direction δ ≠ 0: Λ + sδ ∈ Π for
every s ≥ 0. By Corollary 1 there is F ∈ P_T ∩ C_c^∞ with W[δ](F) > 0, and
a_T^{Λ+sδ}(F) = a_T(F) − s W[δ](F) < 0 for s > a_T(F)/W[δ](F) (a_T(F) is finite).
(iii) If λ ∈ Π, λ ≠ Λ, Corollary 1 applied to δ = λ − Λ gives h_Π(F) ≥ W[δ](F) > 0 for some F. The
converse is trivial, and then (i) is (★).
(iv) For fixed F, λ ↦ a_T^λ(F) is affine and Π is convex compact, hence its minimum is attained at an
extreme point. Λ ∈ Π gives (★). The existence of F with h_Π(F) > 0 is (iii). The first inequality is (i) with
λ = Λ ± sδ. For the second, q_± = a_T ± s W[δ] are non-negative forms on P_T ∩ 𝒟_T with q_± ≤ 2a_T;
from 2s W[δ](F,G) = q_+(F,G) − q_−(F,G) and Cauchy–Schwarz for each q_± one gets
2s |W[δ](F,G)| ≤ 2·(2a_T(F))^{1/2}(2a_T(G))^{1/2}. ∎

**Case of the classical constraints.** Let K_0 = {λ ≥ 0, λ(n) = 0 if n is not a prime power}. Let
Div(E) be the set of divisors of elements of E.

**Corollary C. PROVED.**
(a) Π(E,K_0) is unbounded if and only if some prime power q ∈ [X,N) divides no element of
E. In that case Λ + c·1_{n=q} ∈ Π(E,K_0) for every c ≥ −Λ(q) and (MS) is false. In particular (MS) is
false unless E contains all prime powers of [N/2, N), and, for each j ≥ 1 and each prime power
q ∈ [N/(j+1), N/j), one of q, 2q, …, jq.
(b) Suppose N ≤ X². For each prime p let 𝒯_p = {j : X ≤ p^j < N} and
J_p(E) = {v_p(n) : n ∈ E, p^{v_p(n)} ≥ X}. Then Π(E,K_0) = {Λ} if and only if 𝒯_p ⊂ J_p(E) for every p;
that is, if and only if for each prime power q = p^j ∈ [X,N) there is n ∈ E with p^j ∥ n.
(c) If N ≤ X², every prime power of [X,N) divides an element of E, and some level j ∈ 𝒯_p is missing from
J_p(E), then Π(E,K_0) is a bounded polytope, a product of polytopes indexed by primes p < N^{1/2},
with Λ in its relative interior. Minimal example: 𝒯_p = {a, a+1}, J_p = {a+1}; Π contains the segment
λ_s = Λ + s(1_{n=p^a} − 1_{n=p^{a+1}}), |s| ≤ log p, and (MS) contains the inequality

    a_T(F) ≥ 2 log p · | p^{−a/2} c_F(a log p) − p^{−(a+1)/2} c_F((a+1) log p) |   for every F ∈ P_T.

*Proof.* (a) The recession cone of Π is D(E) ∩ K_0. If δ ≥ 0 and Σ_{d|n} δ(d) = 0 with n ∈ E, then
δ(d) = 0 for every d | n; hence D(E) ∩ K_0 = {δ ≥ 0 supported on prime powers of [X,N) ∖ Div(E)}.
If q ∉ Div(E), no atom with n ∈ E contains the variable x_q and Λ + c·1_{n=q} ∈ Π for c ≥ −Λ(q);
Theorem B(ii). A multiple of q smaller than N is one of q, 2q, …, jq when q ≥ N/(j+1).
(b) The admissible directions at Λ within K_0 are the δ ∈ D(E) supported on prime powers
(both signs, since Λ(q) > 0), and Π = {Λ} if and only if there is no non-zero one. If n < N ≤ X² had
divisors p^i ≥ X and p′^{i′} ≥ X with p ≠ p′, then n ≥ X². Hence for n ∈ E the prime powers
≥ X dividing n are powers of a single prime p, namely p^i with i ∈ 𝒯_p, i ≤ v_p(n), and the atom at
n is the equation Σ_{i ∈ 𝒯_p, i ≤ v_p(n)} δ(p^i) = 0 (empty if p^{v_p(n)} < X for every p). The system
decouples by primes, and on the tower of p it says that the partial sums S_j = Σ_{i ∈ 𝒯_p, i ≤ j} δ(p^i)
vanish for j ∈ J_p(E). It has only the zero solution if and only if J_p(E) ⊃ 𝒯_p.
(c) By (a) Π is bounded; by (b) it does not reduce to Λ and the directions are sums of tower directions;
a tower with a single level is covered by the divisibility hypothesis, hence only
primes with p² < N intervene. In the example, the only equation is δ(p^a) + δ(p^{a+1}) = 0 and λ_s ≥ 0 is equivalent to
|s| ≤ log p; the inequality is Theorem B(iv). ∎

**Remark 1 (variant with atoms N_λ(n) = 1). PROVED as far as stated.** R186_005 uses the atom
N_λ(n) = 1, with N_λ given by N_λ(1) = 1, N_λ(n) log n = Σ_{d|n, d≥2} λ(d) N_λ(n/d). By induction on n,
N_λ(n) depends only on the λ(d) with d | n; hence if q ∉ Div(E) the atom λ(q) stays free and
Corollary C(a) holds unchanged. If E is divisor-closed the two notions coincide (the recursion with
N_λ ≡ 1 on the divisors is the linear atom). For N > X² the varieties differ and the N_λ version is
worse: with primes q_1 ≠ q_2 in [X, N^{1/2}) and E = {q_1 q_2}, within K_0 one has
N_λ(q_1 q_2) = (λ(q_1)/log q_1)(λ(q_2)/log q_2), and the class contains the hyperbola λ(q_1) = t log q_1,
λ(q_2) = t^{−1} log q_2, t > 0, unbounded; the argument of Theorem B(ii) with Lemma 1 at n_0 = q_1 gives
a member with negative form.

**Remark 2 (first coupling between distinct new contacts). PROVED.** With linear atoms and
K_0, an atom couples two distinct new primes only if N > X² and n is a multiple of a product q_1 q_2 of
powers of distinct primes of [X,N): the equation is δ(q_1) + δ(q_2) + … = 0. For E formed by
semiprimes q_i q_j (primes q_i ∈ [X, N^{1/2})), D(E) ∩ {support on the q_i} is the space of alternating
functions on the graph with edges {i,j}: zero on the components with an odd cycle, of dimension
one on the bipartite ones. Thus, even where partial completeness is genuinely multiscale, the
alternative remains identification or polytope.

**Status of case (iv)/(c).** CONDITIONAL NO-GO. By Theorem B(iv), (MS) forces
s|W[δ](F)| ≤ a_T(F) on all of P_T. If there exists a real unit minimizer F_⋆ of a_T on P_T with
W[δ](F_⋆) ≠ 0 and λ_A(T) < s |W[δ](F_⋆)|, (MS) is false; by P47 cor:margin1 (CITED) it suffices, for T ≥ 1,
s|W[δ](F_⋆)| > 4·10⁹ T e^{−15.449T}. It is the same unverified hypothesis that makes
P47 thm:shape (A′) conditional for the amplification of one term. Without it, (MS) remains an OPEN statement
strictly stronger than (★) at T, and by P47 thm:geo-split (CITED) its sign content is the sign
at Λ: the added part is rigidity, not mechanism.

**Conclusion of §3. NO-GO (class), PROVED in cases (ii)/(a) and (iii)/(b), CONDITIONAL in (iv)/(c).**
Class: deductions whose premises about the comb are data on [2,X), linear completeness atoms on an
E ⊂ [X,N) and membership in a closed convex K. Within that class "partial completeness beyond X"
is not a mechanism: either it is false as a source of positivity, or it is total identification (and then the class
restricts nothing: by Lemma A(ii) every polynomial equality true at Λ is derivable), or it requires a
margin. Clause O4 of `OBJECT_SPEC.md` (the identity is false for every other comb) is equivalent, for
an identity of this class, to Π(E,K) = {Λ}.

## 4. The two-scale identity of degree two, written out

Let g = μ∗log² (function on the integers). Write Λ_< = Λ·1_{[2,X)}, Λ_≥ = Λ·1_{[X,N)}.

**Proposition D. PROVED.** Suppose N ≤ X². For X ≤ n < N,

    (E2)   Λ(n) log n + 2 Σ_{k | n, 2 ≤ k ≤ n/X} Λ(k) Λ(n/k) = g(n) − Σ_{km = n; k,m < X} Λ(k) Λ(m).

The operator (𝖳f)(n) = f(n) log n + 2 Σ_{k | n, 2 ≤ k ≤ n/X} Λ(k) f(n/k) on functions on [X,N) is
triangular with diagonal log n > 0 and coefficients Λ(k), k < N/X ≤ X, from the old window. Hence
Λ_≥ = 𝖳^{−1}[(g − Λ_<∗Λ_<)|_{[X,N)}] and, for every F ∈ P_T ∩ 𝒟_T,

    (I2)   a_T(F) = a_T^{Λ_<}(F) − W[ 𝖳^{−1}((g − Λ_<∗Λ_<)|_{[X,N)}) ](F).

(I2) is linear in the new datum g|_{[X,N)}. If N > X² there also appears in (E2) the term
Σ_{km=n; k,m ≥ X} Λ(k)Λ(m), which is the first term quadratic in new contacts; it is non-zero only at
n = q_1 q_2 with q_1, q_2 prime powers ≥ X, where Λ(n) log n = 0 unless n is a prime power.

*Proof.* The degree-two identity Λ(n) log n + (Λ∗Λ)(n) = g(n) (coefficients of ζ″/ζ = (ζ′/ζ)′ +
(ζ′/ζ)², or directly from Λ∗1 = log) splits according to the pairs (k,m), km = n: both < X; exactly one
≥ X (then the other is ≤ n/X < N/X ≤ X), counted twice; both ≥ X, impossible if n < X². This gives (E2);
𝖳 is triangular with respect to the order of n because n/k < n. (I2) is a_T = a_T^{Λ_<} − W[Λ_≥]. ∎

**What (I2) does not give. PROVED.** (1) It contains no manifestly non-negative quantity: by
Lemma 1, W[b] is an indefinite form on P_T for every b ≠ 0, and a_T^{Λ_<} is not controlled by
positivity at T_0, which only says a_{T_0}(F) ≥ 0 for F supported in I_{T_0}. (2) It is generic in the
comb: by Lemma S0 of R186_005 (CITED) the same identity holds for every b with g_b = μ_b∗(N_b log²);
what is non-generic is g_b = μ∗log² on [X,N), which by the invertibility of 𝖳 is equivalent to b = Λ on [X,N):
total identification, case (iii) of Theorem B. (3) By Lemma A, (I2) is the rewriting W[Λ_≥] =
W[𝖳^{−1}(…)] of one and the same weight vector: the form does not distinguish the left member from the right. It falls into
pattern B1 of `RULES_AVOID.md` (identity valid for every comb) plus pattern B3 (reformulation).

The variant "copies scaled by divisors" (Λ = μ∗log substituted into the comb) is
W[Λ](F) = Σ_{k<N} μ(k) Σ_{n<N/k} log n · 2(kn)^{−1/2} c_F(log k + log n): it is the form on the integer
lattice with the collapsed comb, recorded as SPEC_B T*₃ in IDX README (phase 191) and as "integer-lattice
matrices (reformulation)" in `RULES_AVOID.md` §C. It is not retried.

## 5. Answer to the recorded failures

| Recorded failure | Does the design differ? | Reason |
|---|---|---|
| Compensation between scales without per-atom positivity; telescoping without a new bound on the remainder (memory in the project rules; 211 `POWER_DESCENT_016` §§2–4, `POWER_RECURRENCE_BOUNDARY_036` §§5–7) | No | The increment between scales is −W[Λ_≥], an indefinite form (Lemma 1); (I2) rewrites it without signing it. There is no new bound on the remainder. |
| "There is no upward induction in T, there is no Grönwall" (CW I15, I16) | No | Positivity at T_0 does not control a_T^{Λ_<} outside the functions supported in I_{T_0}; the recursion X → X² is an upward induction. |
| SPEC_A, exact induction by contacts (IDX README, phase 191) | No | The step X → N inherits the full margin of the window N; Theorem B(iv) further shows that any relaxation of the step to a class larger than {Λ} asks for margin, which is what SPEC_A lacked. |
| P47 thm:geo-split and defect/continuation barrier (phase 197) | No | Theorem B(i),(iv) is an instance: positivity on Π = sign at Λ + rigidity h_Π without sign. |
| Hierarchical contact ladder (P48 tab:signobject: generic in the comb) | No | (I2) is generic by Lemma S0. |
| Circularity PROVED for single tests and families of powers (IDX 06 R7) | Different scope, does not avoid it | §3 treats inequalities of arbitrary degree, but only those derivable from linear partial completeness plus K; it does not extend the recorded theorem to every non-linear B. |
| 211 LEDGER C45/C47 (ℕ at the right edge of the positive segment; no variational leverage) | No | Consistent with Theorem B(iv): a polytope Π with Λ in its relative interior asks for positivity on both sides of Λ. |

None of the differences avoids the recorded reason for the failure. In accordance with the instruction, the
construction stops here.

## 6. Falsifier battery

There is no sign step to submit. For the classes Π(E,K_0) of §3: finite deletion and amplification are
in Π if and only if the modified atom lies outside Div(E) (Corollary C(a)); cΛ with c ≠ 1 and a_P are not
in Π because they violate the data on [2,X) (and, if those data are removed, they violate each atom κ_n, n ∈ E, since
c log n ≠ log n); b_θ = Λ·½(1 + cos(γ log n + ϑ)) is in Π only if it coincides with Λ on Div(E) ∩ prime
powers. The quartet models and f_t preserve the values Λ(n) of the window: they satisfy every atom
κ_n with n < N (respectively n < λ_1), so that no completeness premise, partial or total,
separates them; any object would have to break them on a line that uses the archimedean factor, and this memo
does not provide that line. Davenport–Heilbronn, Epstein and the Beurling systems violate the atoms as soon as
E contains an integer where their comb differs from Λ.

## 7. Precise statement of what the cell asks for

After §3, "partial completeness beyond X" can only mean one of two things.

**(P1) Total identification with non-linearity in the coupling.** An object (ℋ_T, V_T, ρ_T) with V_T
polynomial in the weights, such that the locus of the identity

    Z_T = {x ∈ K : a_T^x(F) = ‖V_T^x F‖² + ρ_T^x(F) for every F ∈ P_T ∩ 𝒟_T}

is Z_T = {Λ|_{[2,N)}} for every T. By the transfer principle and Theorem B this is necessary if
one does not want to pay margin: (★) for every T follows from (G) if and only if Λ ∈ Z_T, and positivity
transfers to all of Z_T, hence a_T(F) ≥ sup_{x ∈ Z_T} W[x − Λ](F). The non-linearity cannot be in a
relation among the weights (Lemma A): it has to be in V_T^x F as a joint function of x and F. Status:
OPEN, without candidate; it is clause O2 ∧ O4 of `OBJECT_SPEC.md`, not a weaker statement.

**(P2) Inequality with margin on a polytope.** For some (X, N, E, K) with Π(E,K) bounded and ≠ {Λ}:

    for every F ∈ P_T ∩ 𝒟_T:   a_T(F) ≥ max_{λ extreme point of Π(E,K)} W[λ − Λ](F).

It is strictly stronger than (★) at T; CONDITIONAL NO-GO (§3). It is not a reasonable target.

There is no third reading within the class of linear atoms with convex constraints. Outside
it (non-convex constraints on the comb, for example integrality of multiplicities, or premises
that are not properties of the comb on [2,N)) this memo claims nothing.

## 8. Closing

**Result.** No new mechanism. PROVED piece: classification of partial completeness (Theorem B,
Corollary C) and linearity of the two-scale identity for N ≤ X² (Proposition D). NO-GO with class:
deductions from data on [2,X), linear completeness atoms on E ⊊ generator and a closed convex K
— PROVED when Π is unbounded, CONDITIONAL when Π is a non-trivial polytope.

**What was proved.** Lemma 1 and Corollary 1 (test atoms; independence of the functionals
F ↦ c_F(log n) on P_T). Lemma A (every polynomial fact about Λ on [2,N) is a consequence of the linear
atoms; I_E is the ideal of an affine subspace). Transfer principle. Theorem B. Corollary C
(criterion in terms of divisors and exact valuations for N ≤ X²). Remarks 1 and 2 (variant
N_λ; semiprime graph for N > X²). Proposition D.

**What failed and why.** (ℋ_T, V_T, ρ_T) could not be written: the only proposed source of non-linearity
(Λ·log + Λ∗Λ = μ∗log² at two scales) is linear in the new contacts for N ≤ X², is generic in the
comb except for total identification, and the form, affine in the comb, does not see the degree. The increment
between scales −W[Λ_≥] has no sign and no written identity signs it. Case (iv) of Theorem B could not
be closed without the hypothesis W[δ](F_⋆) ≠ 0 on a minimizer.

**Next concrete step.** (1) Record in IDX 06 R7 and in GRID §8 that the direction "partial completeness
beyond X" is classified (this file, §3) and that the live residue of R7 is (P1). (2) To
close case (iv): prove or refute, for the tower segment of Corollary C(c) with p = 2, that there exists
F ∈ P_T with a_T(F) < 2 log 2 · |2^{−a/2} c_F(a log 2) − 2^{−(a+1)/2} c_F((a+1) log 2)|; it is a question
about an explicit two-atom form. (3) For (P1), the only piece of the record that couples weights and
vector in a single step is the finite Poisson–Chebyshev identity (P47 thm:PCfinite), which corresponds to
candidate K1; K4 does not provide an object independent of it.
