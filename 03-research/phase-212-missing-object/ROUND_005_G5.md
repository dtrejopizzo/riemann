# Round 5, memo G5: free invention from A1–A6 (backward deduction of object types)

Notation from `../phase-211-sign-sandbox/STATEMENT_001.md`. Arch(F) = C_0‖F‖² + ∫_0^∞ (c_F(0) − Re c_F(u))K(u)du;
Π_p(F) = Σ_{k: k log p < 2T} v_{p^k} Re c_F(k log p); a_T = Arch − Σ_p Π_p. For the weight cΛ, a_T^{(c)} = Arch − cΣ_pΠ_p.
Parity sector: P_T^± = P_T ∩ {F even / odd}; in each sector there is a single Tate vector, τ_+ = cosh(t/2) (even)
and τ_− = sinh(t/2) (odd), and P_T^± = τ_±^⊥ within the sector.

## Cross-check (goes first, by rule)

1. **Closest antecedents, read as primary sources.**
   - `phase-160-row-d-infinite-T/R160_C7_R1.md` §§5–6, especially §6.3(2) and §7 item 2 (P160.C7.1): asks for a
     polynomial of degree k ≥ 3 whose Hessian is −a_T, with an independent source of nonnegative coefficients;
     discards the candidates Str(Γ_F^k). Read in full in §§5–7.
   - `phase-159-row-d-two-front-construction/G2_B8_R1.md` §§1–2 (Theorem S and Corollary S′: emptiness of the
     Satake torus) and `G2_B8_R5.md` §§1–2 (Theorem D: local certification with Lévy–Khintchine distribution of the
     archimedean factor; threshold T_loc ≤ 0.5925). Read in those sections.
   - `phase-200-sign-object/SPEC_SIGN_OBJECT_010.md`, variant 20.3 (a_T as log θ; "its sign is that of the
     Hessian of log θ, an indefinite second cumulant"). The passage was read.
   - `phase-193-creation-campaign/CA_G_000_SEEDS.md` G6 and `CA_F_000_SEEDS.md` F5; `phase-201-untried-families/FAMILIES_A_001.md`
     A1: Lorentzian polynomials recorded as "retry, no sign" / NON-VIRGIN. The pertinent lines were read.
   - `ANNEX_COTEJO_LORENTZ_1.md` §§3–5 and `ANNEX_COTEJO_LORENTZ_2.md` §§3–5 of this folder: M5 "closure under
     product of Euler factors applied to the signature with the archimedean factor fixed, and its check at
     c = 2" appears as not found.
2. **What is new here.** Not an object: three class lemmas (PROVED, elementary) that close, in declared
   classes, the object types that the backward deduction points to as "native" for A1–A6:
   (L1) every object whose sign comes from log-concavity (or log-convexity) at an interior point —
   determinants, partition functions, homogeneous Lorentzian polynomials at a point of the cone— gives a_T as
   a Gram form whose vector is exactly the V_T of (G), with no sign contribution of its own; (L2) closure under
   product of Euler factors of that log-concavity is equivalent to a local distribution a_T = Σ_v q_v, q_v ⪰ 0, which
   with unrestricted distributions is the statement (trivial Farkas) and with distributions covariant under local rotation
   falls into Theorem S of G2_B8_R1; (L3) in the homogeneous Lorentzian format the direction of the gradient is
   forced to be the Tate vector of the sector. L2 answers point M5 of the annex (closure by product with the
   archimedean factor fixed, with its check at c = 2): the breaking at c = 2 is exactly in the
   archimedean budget, but the mechanism has no sign content.
3. **Why it does not repeat.** R160_C7_R1 §6.3(2) examines only Str(Γ_F^k) and leaves the class open; G2_B8 treats
   Lévy–Khintchine distributions (translation-invariant) and Satake rotations, not closure under product
   of log-concavity of arbitrary factors. L1–L3 cover the class "sign by log-concavity at an interior
   point, closed under products", which includes item P160.C7.1 insofar as one wants to prove it with the
   product closure rules.
4. **Connection with global positivity.** None: the three lemmas show that in those classes
   global positivity is equivalent to the existence of V_T (L1) or of the distribution (L2), i.e. to the target. No
   sign is claimed.

Result in advance: **I did not manage to write an object satisfying A1–A6.** What follows is the deduction and the
class lemmas.

## 1. Backward deduction (steps (1)–(3) of the seed)

| Property forced by A1–A6 and the facts | Types that have it natively | What remains after L1–L3 or after what is PROVED in the corpus |
|---|---|---|
| (P1) Non-affine dependence on the weight that degenerates at c = 1 (A1) | determinant, partition function, index, dimension, jumping cohomology | Indices and dimensions: constant near c = 1 in a fixed window (R4-f). Determinant / partition: L1 |
| (P2) Positivity without margin (λ_A ≤ 4·10⁹Te^{−15.449T}) | identity "= Σ squares"; inequality with an equality case; integer quantity | Integer quantity: R4-f. Identity: it is (G) itself |
| (P3) Uses the two moment conditions essentially (A3) | object whose gradient at the base point is the Tate vector | L3: in the Lorentzian format this is forced, not a choice |
| (P4) Window in c closing on 1 from both sides | concave function of c with maximum at c = 1 (λ_A(T;c) is an infimum of affine functions) | Any mechanism whose hypothesis holds on a set of c independent of T fails (P46 thm:shape, cor:void) |
| (P5) Euler product and fixed archimedean factor; c = 2 must break through the archimedean factor (A5) | closure under product (log-concavity, Lorentzianity, stability) | L2: closure by product is a local distribution; with free distribution it is the target, with covariant distribution it falls into Theorem S |
| (P6) c = 1 unique: lattice ℤ self-dual by Poisson | Poisson / theta identity | D6, D14, D15 of `RULES_AVOID.md` (theta, completion of squares, local metrics) |

Intersection of (P1)–(P5) in object types: "positive function p near a base point x_0, with log p
concave, product of an archimedean factor and per-prime factors, gradient at the Tate vector, and Hessian of
log p equal to −a_T". The following lemmas show that this intersection contributes no sign of its own.

## 2. Class lemmas

**Lemma L1 (log-concavity at an interior point = Gram of (G); PROVED).** Let E ⊂ P_T be a finite-dimensional
subspace (or P_T ∩ 𝒟_T with the graph norm topology), U ⊂ ℝ^d open, x_0 ∈ U, ℓ : E → ℝ^d linear and
p : U → (0, ∞) of class C² with

  ∇² log p(x_0)[ℓF, ℓF] = −a_T(F)  for all F ∈ E.  (2.1)

(a) If log p is concave near x_0, then a_T ⪰ 0 on E and there exist a Hilbert space ℋ and V : E → ℋ linear
with a_T(F) = ‖VF‖² (i.e., (G) with ρ = 0).
(b) Determinant case: p(x) = det(X_0 + Σ_i x_i A_i) with X_0 ≻ 0 and arbitrary symmetric A_i. Then
−∇² log p(0)[y, y] = tr((X_0^{−1}A(y))²) = ‖X_0^{−1/2}A(y)X_0^{−1/2}‖²_HS, A(y) = Σ y_iA_i; the sign uses
no positivity of the A_i.
(c) Partition case: p(x) = ∫ e^{⟨x, X⟩} dμ with μ a probability measure with exponential moments. Then
∇² log p(0)[y, y] = Var_μ⟨y, X⟩ ≥ 0; (2.1) with the sign changed (log-convexity) gives a_T(F) = Var_μ⟨ℓF, X⟩, and such a μ
exists for some ℓ if and only if a_T ⪰ 0 on E.
(d) Conversely, if a_T ⪰ 0 on E, there exist log-concave p and ℓ with (2.1): p = exp(−½a_T∘ℓ^{−1}) on the image.

*Proof.* (a) Concavity of log p ⇒ ∇²log p(x_0) ⪯ 0 ⇒ by (2.1) a_T ⪰ 0; the square root of the form
(spectral theorem in finite dimension, or completion of E by a_T in general) gives V. (b) ∂_y log det(X) =
tr(X^{−1}A(y)), ∂_y² = −tr(X^{−1}A(y)X^{−1}A(y)); with X_0 ≻ 0, tr((X_0^{−1}A)²) = tr((X_0^{−1/2}AX_0^{−1/2})²) =
‖X_0^{−1/2}AX_0^{−1/2}‖²_HS ≥ 0 because X_0^{−1/2}AX_0^{−1/2} is symmetric. (c) Standard cumulant formula:
∂² log ∫e^{⟨x,X⟩}dμ = covariance under the tilted measure; at x = 0 it is Var_μ. If a_T ⪰ 0 on E, the
centred Gaussian field with covariance a_T exists (Kolmogorov; in finite dimension, the Gaussian with matrix a_T); if
not, the variance cannot be negative. (d) Direct. ∎

*Reading.* In the class "the sign comes from log-concavity (or log-convexity) of a positive function at an
interior point", the constructed object is exactly a V_T of (G); log-concavity contributes nothing other than
the existence of V_T. This includes determinants and partition functions (P1) and answers variant 20.3
of `SPEC_SIGN_OBJECT_010.md`: there the second cumulant was indefinite; here, when it is definite, it is a
Gram and its existence is the target.

**Lemma L3 (homogeneous Lorentzian format and Tate vector; PROVED).** Let p be homogeneous of degree k ≥ 2, positive
on an open cone containing x_0, of class C². Set g = ∇p(x_0) ≠ 0 and H = ∇² log p(x_0). Then
∇²p(x_0) = p(x_0)(H + ĝĝᵀ), ĝ = g/p(x_0), and the following are equivalent:
 (i) ∇²p(x_0) has at most one positive eigenvalue;
 (ii) H ⪯ 0 on g^⊥.
If moreover (2.1) holds with ℓ an isomorphism of the sector P_T^± ⊕ ℝτ_± onto ℝ^d such that ℓ(P_T^±) = g^⊥, then (i)
for p is equivalent to a_T ⪰ 0 on P_T^±, and the hyperplane g^⊥ is the image of the kernel of the Tate functional.

*Proof.* ∇²p = ∇(p∇log p) = p(∇²log p + ∇log p ∇log pᵀ). By Euler, ∇²p(x_0)x_0 = (k−1)g and
∇²p(x_0)[x_0,x_0] = k(k−1)p(x_0) > 0. (i)⇒(ii): x_0 is a positive direction; the ∇²p-orthogonal complement of x_0 is
{y : ⟨g, y⟩ = 0} = g^⊥; with at most one positive eigenvalue, ∇²p ⪯ 0 on that complement, and there ∇²p = p·H because
⟨ĝ, y⟩ = 0. (ii)⇒(i): ∇²p ⪯ 0 on the hyperplane g^⊥, hence by min-max at most one positive eigenvalue. The last
sentence is (2.1) restricted. ∎

*Reading.* (P3) is not a design choice: in any homogeneous Lorentzian object whose Hessian
reproduces a_T in a sector, the gradient at the base point is the Tate functional. The sign content is
H ⪯ 0 on g^⊥, which is (2.1) with a_T ⪰ 0: again the target, unless the Lorentzianity of p is obtained by
a closure rule. The native closure rule with the Euler product is the product; that is the next lemma.

**Lemma L2 (closure by product of Euler factors = local distribution; PROVED in finite dimension).** Let E ⊂ P_T
be finite-dimensional and Π_T the set of primes p < e^{2T}. Suppose p = p_∞ ∏_{p∈Π_T} p_p, each factor positive
and C² near x_0, and (2.1). Set q_v(F) := −∇²log p_v(x_0)[ℓF, ℓF].
(a) a_T = q_∞ + Σ_p q_p on E. If each factor is log-concave (in particular if each factor is Lorentzian, by the
log-concavity of Lorentzian polynomials on the open orthant, CITED: Brändén–Huh, Ann. Math. 2020, Thm 2.30), each
q_v ⪰ 0.
(b) (Free distribution.) There exist symmetric forms r_p on E with r_p − Π_p ⪰ 0 for all p and Arch − Σ_p r_p ⪰ 0 if and
only if a_T ⪰ 0 on E.
(c) (Distribution with only local dependence on the weight.) If the construction holds for every weight w in a neighbourhood of Λ,
with p_∞ independent of w and p_p depending only on (w_{p^k})_k, then q_p^{(w)} = r_p − Π_p^{(w)} with r_p
independent of w_p, and q_∞ = Arch − Σ_p r_p.
(d) (c = 2 and non-integer c.) Under (c), for the weight cΛ the same construction gives a_T^{(c)} = (Arch − cΣ_pr_p) +
Σ_p c(r_p − Π_p). The prime terms are c·q_p ⪰ 0 for all c > 0; the only line that can fail is
q_∞^{(c)} = Arch − cΣ_pr_p ⪰ 0, the budget of the fixed archimedean factor.
(e) (Covariance under rotation.) If the log-concavity of p_p is deduced from a property of the local data that
holds for Haar-almost every α_p = e^{iθ_p} (temperedness, local Lee–Yang stability, degree-one form), the
construction proves a_T^{(v(θ))} ⪰ 0 for almost every θ of the Satake torus, which is false for T ≥ 0.60
(G2_B8_R1 Theorem S(1) and Corollary S′, CITED from the corpus, read as primary sources).

*Proof.* (a) log p = log p_∞ + Σ log p_p; differentiate twice. (b) ⇒: adding, a_T = (Arch − Σr_p) + Σ(r_p − Π_p) ⪰ 0.
⇐: if Π_T = ∅ there is nothing to prove; otherwise, r_p := Π_p + a_T/|Π_T| gives r_p − Π_p = a_T/|Π_T| ⪰ 0 and Arch − Σr_p =
a_T − a_T = 0. (c) Differentiating the identity a_T^{(w)} = q_∞ + Σq_p^{(w)} with respect to w_{p^k}: the left-hand side gives
−(2/√(p^k))Re c_F(k log p) = −∂_{w_{p^k}}Π_p^{(w)}(F), and only q_p^{(w)} depends on w_{p^k}; since a_T^{(w)} is
affine in w, q_p^{(w)} is affine in (w_{p^k})_k with the same linear part as −Π_p^{(w)}; define r_p := q_p^{(w)} +
Π_p^{(w)}, independent of w_p and, by the locality hypothesis, of the other weights; then q_∞ = a_T − Σq_p =
Arch − Σr_p. (d) Substitute w = cΛ in (c). (e) The hypotheses of (e) are preserved under rotation, hence the
construction (if it exists for Λ by that route) exists for v(θ), contradicting S(1) on a set of θ of
positive measure. ∎

*Reading of L2.* Closure by product, which is the only thing the Euler product contributes to
log-concavity, turns the sign into a distribution of the archimedean factor among primes. With unrestricted
distributions the distribution exists exactly when the target holds (b): the mechanism has no content. With
Lévy–Khintchine distributions it is the local certification of G2_B8_R5, which does not exist for T ≥ 0.5925. With
rotation-invariant local properties it is the Satake void. The only thing not excluded is an r_p depending
on the exact phase α_p = 1 (not on an almost-sure property of the torus) and not translation-invariant; I did
not manage to write one with its own formula.

## 3. Object

Not written. The intersection of §1 reduces, by L1–L3, to "V_T of (G)" or to "local distribution (r_p) with
Arch − Σr_p ⪰ 0 and r_p ⪰ Π_p", and neither of the two carries a sign source independent of the statement.

## 4. Identity

L1(a), L1(d) and L2(b) are the exact identities between the examined classes and a_T: (2.1) ⟺ (G) with ρ = 0; product
of log-concave factors ⟺ a_T = q_∞ + Σq_p with q_v ⪰ 0 ⟺ a_T ⪰ 0 on E. Check in the simplest case: for
T < ½log 2 there are no primes, L2 reduces to q_∞ = a_T = Arch, and L1 gives a_T = ‖VF‖² exactly when Arch ⪰ 0 on P_T,
which is what is certified in that range. No computation was done: the proofs are two lines long.

## 5. Mechanism

The natural candidate was: "p Lorentzian as a product of Lorentzian factors (Brändén–Huh, closure under
product, CITED) ⇒ ∇²p with at most one positive eigenvalue ⇒ (L3) a_T ⪰ 0 on P_T^±". Hypotheses: (H1) each local
factor is Lorentzian; (H2) (2.1) with gradient at the Tate vector. (H2) is consistent (L3). (H1) for all
factors implies, by L2(a), q_v ⪰ 0 for each v, and then the content of (H1) is the distribution of L2(b)–(e).
Open hypothesis pointed out: existence of r_p with its own formula, depending on the exact phase, not translation-invariant,
with r_p ⪰ Π_p and Σr_p ⪯ Arch on P_T for all T. This is equivalent to the target (L2(b)), so it is not
a weaker hypothesis: it is recorded only as a form of the problem, not as progress (B3).

## 6. Controls (on the mechanism of §5, which proves nothing)

- **c = 2.** Breaks at the line q_∞^{(2)} = Arch − 2Σr_p ⪰ 0 (L2(d)): the doubled prime factors remain
  log-concave (product of two copies), the fixed archimedean factor does not pay the double budget. It is the
  breaking that A5 asks for, but the mechanism has no content for c = 1.
- **Non-integer c.** There is no factorization into copies; with (c) the construction extends to all c > 0 by
  scaling q_p, and the same line q_∞^{(c)} is the only one that can fail. For c < 1, q_∞^{(c)} =
  q_∞ + (1 − c)Σr_p is not ⪰ 0 unless Σr_p ⪰ 0, which is not guaranteed: the breaking to the left of 1
  depends on r_p, not on the archimedean factor. Not verified in any example.
- **a_P (deletion of primes p < P).** The factors p_p, p < P, disappear; if the distribution is not recomputed,
  a_T^{(a_P)} = q_∞ + Σ_{p<P}r_p + Σ_{p≥P}q_p, and the line Σ_{p<P} r_p ⪰ 0 fails (the r_p have no sign of their own).
- **No Euler product (Davenport–Heilbronn).** The hypothesis "p = p_∞∏p_p" cannot be written: the
  first line of L2 fails; L1 still holds (it is generic), which confirms that L1 contributes no sign.
- **Satake rotation.** L2(e).

## 7. Own verdict

**I did not manage to write an object satisfying A1–A6.** Class results, all without sign: L1 (PROVED): sign by
log-concavity or log-convexity at an interior point, including determinant and partition function, is exactly
a V_T of (G); L3 (PROVED): in the homogeneous Lorentzian format the gradient is the Tate vector and the condition
is a_T ⪰ 0 in the sector; L2 (PROVED in finite dimension, (e) relative to G2_B8_R1 Theorem S): closure by product
of Euler factors is a local distribution which with free distribution is equivalent to the target, with Lévy–Khintchine is the
dead class of G2_B8_R5, and with almost-sure local properties on the torus falls into the Satake void; it breaks at
c = 2 only in the archimedean budget.

## Result

NO-GO with class (L1–L3), no new mechanism. No sign statement.

## What was proved

L1(a)–(d), L3, L2(a)–(d) complete; L2(e) relative to a theorem of the corpus.

## What failed and why

Every "native" object type for (P1)–(P5) that obtains the sign from a concavity at an interior point
transfers the sign to a Gram form or to a distribution, and the existence of either of the two is the target.
The only closure rule using the Euler product (product of factors) is additive in the Hessian of log and
reproduces the local certification.

## Concrete next step

If one wants to continue along this class: write an r_p with its own formula depending on α_p = 1 in a way that is not almost
sure on the torus and not translation-invariant, and verify r_p ⪰ Π_p for p = 2, 3 at T = 0.5925 on the
test pair of G2_B8_R5 §4 (where every LK distribution fails). Without that formula, the class remains closed as stated
above. Not cross-checked in primary sources: phases 15, 40–43, 120 (collision matroid, cited by the annex), 137–142,
Paper 47, and `00-references/`.
