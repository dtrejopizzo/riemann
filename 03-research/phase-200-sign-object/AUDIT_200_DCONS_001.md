# AUDIT_200_DCONS_001: audit of D_CONSTRUCTION_001 (phase 200, round 22)

Object audited: `D_CONSTRUCTION_001.md` (𝔇₀, 𝔇₁, mixed area, 𝔇₂, Lemma 𝔇-Sch).
Checked against HORN_B_BIGSHARP_001 §2.3 (S1–S6), HORN_A_001 (Theorem HA, def. of (W⁰)), LEMMA_12_1_H3_001, INV_C_001 Thm 4.
Row D / L′♯ as independent goal.

## Summary (≤200 words)

The central finding is that **Theorem 6 does not need Schanuel**. System (3.1) is block-diagonal in N = mn, and each
block is a Vandermonde matrix (log^k n_j) with distinct nodes. Its real rank and its generic rank over Frac(R_X) both equal
min(t, r_N), where r_N is the number of divisor pairs of N in the window. Hence δ ≡ 0 is **PROVED, for every t and
with no hypothesis**: it suffices that log be injective. The "Precision" claim of §6.1 confuses the degree of the minors with what
is actually needed for them not to vanish.

There is also a second closure, likewise independent of Schanuel: system (3.1) does not contain g, so δ depends only on
(X, t) and falls under Theorem 3. Lemma 𝔇-Sch is **unconditionally false** and the Siegel–Dyson route is closed.

The only reading where transcendence enters is that of h⁰ as a ℤ-rank. There what is involved are homogeneous relations of
degree ≥ 2 among log p, which are of four-exponentials type and not full Schanuel. That reading is still blind to the test.

- Theorem 1: correct, with a restriction to closed sets.
- Theorem 3: correct with a fix in the proof. Cor 3.7 is over-claimed and I replace it with Thm 3′ (rank genericity).
- Prop M: correct.
- Theorem 5(c): direction ⇒ is PROVED and ⇐ is ARGUED.
- Prop 6.4: downgraded to ANALOGY, because the weights do not match (Λ/log vs Λ).
- No object satisfies S1 ∧ S3 in the variable E.

---

## 1. Theorem 1 (𝔇₀ NO-GO)

**Verdict: correct in essence (PROVED). The statement needs to be restricted.**

- **Signed weights, diagonal weights, w(n,n) of type "m".** It does not matter what w is: signed, concentrated on the
  diagonal, or not symmetric. The left side of (2.1) is Σ w(x,y)Φ_g(x)Φ_g(y), and Φ_g vanishes on all of Q_X when
  g ∈ V_J ⊂ C_c^∞(J) with J ∩ L_X = ∅. That is why the form vanishes identically on V_J, for any w. The proof uses no
  property of w, which makes it complete on this point.
- **Absorbing the archimedean part into a diagonal weight.** Impossible for the same reason. The archimedean term
  C₀‖F‖² + Lévy(c_F) is a form on the autocorrelation **in a continuous variable**: Lévy(c_F) = ∫∫F(u)F(v)K(u−v), with K
  singular at 0 (log|u| plus a principal part). If F is discretized to the points log n, the term is completely lost,
  because it is not a function of the samples. On V_J every sample is 0, while ⟨g⋆g^∨, ω_∞⟩ > 0 if |J| is small
  (local positivity for small support, L02 of the index, CITED). In step 6 that **strict positivity** suffices: the
  argument about "infinite rank of the log kernel" is correct but unnecessary.
- **Codimension of P_T.** The conditions Φ_g(0) = Φ_g(1) = 0 are two continuous linear functionals (∫g e^{±t/2}), so
  the codimension is ≤ 2. ✓
- **Overclaim.** The statement says "any sampling supported on a countable set". The proof only covers **closed**
  sets (or, more generally, sets whose complement contains an interval). For a countable dense set,
  such as log ℚ_{>0}, the J of step 2 does not exist, and the case is not covered. There INV_C Thm 4 applies only to measures, not to
  bilinear forms with Σ|w| < ∞. Samplings that include derivatives at lattice points
  (point distributions) are also valid: the proof covers them unchanged.
- **Correction.** Replace "countable" with "countable and closed (or nowhere dense)". The dense case remains OPEN, although it is
  irrelevant for 𝔇₀, which is finite.

## 2. Theorem 3 (the count does not see the test)

**The statement is correct for the class it declares, but the proof has a gap.**

- **Gap in step 2.** E + εh with h ∈ C_c^∞(int supp E) **can change the vanishing orders**, if supp h contains
  zeros of E. Also h must lie in P_T.
- **Fix.** Choose an open set U where |E| ≥ c > 0 and take h ∈ C_c^∞(U) ∩ (codimension-2 subspace of P_T), with
  ε‖h‖_∞ < c. Thus E + εh has the same support, the same zeros with their orders, the same polygon and the same set of
  nonzero lattice points. Step 3 still works, because the positivity of §1 holds on a short subinterval of U.
  With this, Theorem 3 is PROVED.
- **Tests with g-dependent nodes.** The nodes (the set of zeros) and their orders **are** discrete data of the
  declared class, so Theorem 3 already covers them. What it does **not** cover are conditions that use **values** of g, such as
  Σ_{mn=N} a_{mn} g(log n) = 0, or vanishings at node positions that vary continuously with g.
- **Corollary 3.7 overclaimed.** Its dichotomy ("if the conditions are sensitive to the values, they are defined by the form,
  so it is REF-D") is not proved. A condition can use values of g without using I_∞. It should be replaced by the
  following.

> **Theorem 3′ (ARGUED, short proof).** Let χ_n(E) = rank, nullity or their difference of matrices whose entries are
> **real-analytic** functions of finitely many continuous linear functionals of E (values, derivatives, positions of simple
> nodes). Then, for each n, χ_n is constant on a dense open set of P_T, because the rank is generic outside a
> proper analytic set. Since I_∞(E,E) is not constant on any open set, the identity χ_n(E) = ½n²I_∞(E,E) + O(n) fails.

From Theorem 3′ the correct conclusion follows: a χ that sees the test must depend on E in a **non-analytic** way, such as
sign conditions or semialgebraic inequalities. The only inequalities naturally available are those of the
form itself. That conclusion (and not that of Cor 3.7) is what leads to REF-D. The nodes of the minimizer (LEDGER_L2, Theorem X)
are functionals of h*, so REF-D applies. The nodes of an arbitrary g are not REF-D, but Theorem 3/3′ leaves them blind.

**Decision.** Theorem 3 is not overclaimed. Corollary 3.7 is.

## 3. Prop M and Cor M′ (unimodular Möbius)

- **Prop M: PROVED.** For M_c to preserve ℤ^Ω it is required that Ω be closed under divisors: N ∈ Ω ⇒ N/d ∈ Ω. That is the
  exact hypothesis. [1, e^{2T}] ∩ ℕ is closed under divisors ✓. The μ-rough numbers together with 1 too ✓, because the divisors of
  a rough number are rough. Triangularity with diagonal c(1) = 1 gives det = 1 ✓. The case "μ∘(m,n) ↦ mn on the square" goes from
  ℤ^{Q_X} to ℤ^{M(X)}, which is not an endomorphism. It must be removed from the statement or reformulated.
- **Non-unimodular dualities.**
  - (a) **Completely multiplicative weights.** If f is completely multiplicative, then
    Σ_{d|N} μ(d)f(d)a(N/d) = f(N)·(M_μ(a/f))(N). That is, M_{μf} = D_f M_μ D_f^{−1}, with D_f = diag f. The determinant
    is 1 and the only thing that changes is the scale. With f(n) = n^{−½} the covolume relative to ℤ^Ω moves by Σ log f(N), which is
    **linear**, and falls under branch (ii).
  - (b) **Dirichlet inverse of c with c(1) ∉ {±1}.** det = c(1)^{|Ω|}, again linear in the log.
  - (c) **Dirichlet convolution with respect to another, not completely multiplicative, function.** It remains triangular, with
    determinant Π c(1).
  - I found no Möbius-type duality that escapes the dichotomy.
- **Cor M′.** It is PROVED **for rank and determinant invariants of ℤ-linear operators**. "There is no third option" must
  be restricted to that class. A nonlinear duality (Bost theta) likewise satisfies h⁰_θ(L) − h⁰_θ(L^∨) = deg, which is linear
  (CITED). This reinforces the closure rather than weakening it.

## 4. Theorem 5 (mixed area)

- **(a) and (b): PROVED**, as an instance of the corrected Theorem 3: P_A depends only on supp a.
- **(c): the equivalence is not proved in both directions.**
  - **Direction ⇒: PROVED.** An isometry injects indices: n₊(P_T ⊕ ℝK) ≤ n₊(target) = 1, because the target has
    2V = Σ(1−k²)|ĥ_k|². Since I_∞(K,K) = ½ > 0, it follows I_∞ ≤ 0 on K^⊥ = {deg = 0}, which is the (W⁰) form of HORN_A Theorem HA
    restricted to the window.
  - **Direction ⇐: ARGUED.** "Sylvester" does not suffice in non-countable Hamel dimension with a radical. One must (1) send the
    radical 𝓝_∞ ∩ P_T to a totally isotropic subspace orthogonal to the image. The target has only 2 radical
    dimensions (k = ±1) and n₊ = 1, so an infinite-dimensional radical **does not** fit in the radical of the target: it must go to
    non-radical null vectors, and that clashes with orthogonality to ι(K). And one must (2) embed the negative
    semidefinite part, with Hamel cardinality ≤ that of the target. (2) is plausible. (1) is a real obstacle if dim 𝓝_∞ ∩ P_T > 2.
- **Corrected label.** Thm 5(c): "isometry ⇒ (W⁰)_T" PROVED; "(W⁰)_T ⇒ isometry" OPEN/ARGUED. The NO-GO does not change,
  because it uses only ⇒ and the blindness.

## 5. 𝔇₂, Prop 6.3 and the rank: the most important part

**The system is block-diagonal.** The unknowns a_{m,n} are distributed by N = mn, and each condition L_{N,k} only
involves the block B_N = {(d, N/d) : d | N, d ≤ X, N/d ≤ X}, with r_N := |B_N|. Within the block the values n = N/d are
**pairwise distinct**. The block matrix is

  V_N = (log^k n_j)_{0≤k<t, 1≤j≤r_N},

which is a **Vandermonde** matrix with distinct nodes y_j = log n_j. Hence rank_ℝ V_N = min(t, r_N).

**Generic side.** The forms ℓ(n_j) = Σ_p v_p(n_j)x_p are **distinct** in R_X for distinct n_j (unique factorization). The
formal Vandermonde matrix (ℓ(n_j)^k) has rank min(t, r_N) over Frac(R_X): its maximal minors are products Π(ℓ(n_i) − ℓ(n_j))
≠ 0.

**Evaluation.** The evaluated minors are Π(log n_i − log n_j), which are ≠ 0 because log is **injective**. There is not even
any need for ℚ-linear independence of the log p.

**Theorem 6* (PROVED, unconditional, for every t).** h⁰_ev(E) = h⁰_gen(E) = Σ_N (r_N − t)⁺ and h¹ = Σ_N (t − r_N)⁺. Hence
δ ≡ 0.

**Where the memo's error lies.** The "Precision" claim of §6.1 reasons by the degree of the minors ("high degree ⇒ algebraic
independence"). But a Vandermonde minor factors into **linear** factors ℓ(n_i) − ℓ(n_j). For it not to vanish upon
evaluation it suffices that each linear factor does not vanish, and that is injectivity. The relations needed are linear
(in fact, trivial), not polynomial. Schanuel plays no role. Theorem 6(i) moves from CONDITIONAL to **PROVED**.

**Honest nuance: h⁰ as ℤ-rank.** The memo defines h⁰ := rank_ℤ H⁰ (§3.2) and later uses the real rank (§6.1). If the
ℤ-rank is taken, the rational kernel of a system with real coefficients is smaller than the real one. Under ℚ-linear independence of the
**homogeneous monomials of degree k** in {log p}, for each k < t, the ℤ-rank coincides with the ℚ-rank of the formal
coefficient-by-coefficient system. This is PROVED for k ≤ 1. For k ≥ 2, the two-prime case is given by Gelfond–Schneider (CITED):
log 3/log 2 is transcendental, so there is no homogeneous relation. With three or more primes it is OPEN. It contains cases of the
four-exponentials conjecture, such as log a·log d = log b·log c: it is weaker than Schanuel but remains open.

**This reading saves nothing.** System (3.1) **does not contain g** (the fiber enters only through C_a, not the conditions). Hence
h⁰_ℝ, h⁰_ℤ and any defect between them are functions of (X, t) only, and Theorem 3 kills them with no transcendence
hypothesis at all. The claim of §6 ("escapes Theorem 3's hypothesis") is **false**: the coefficients
log^k n are fixed arithmetic, not test data.

**Conclusion.** The route of Siegel–Dyson entire correspondences is **closed without Schanuel**, for two
independent reasons: (A) Vandermonde gives δ ≡ 0, and (B) the system is independent of the test.

**Check for t = 1.** The block is the row (1, …, 1), of rank 1 if r_N ≥ 1. h⁰ = Σ(r_N − 1) = |Q_X| − |M(X)| ✓, with
integer coefficients and no rationality issue whatsoever ✓.

**Prop 3.3.** Its "proof" is circular with respect to the rational basis. With the real rank it is correct as χ = |Q_X| − t|M(X)|
(rank plus nullity) ✓. With the ℤ-rank, the Euler identity becomes an inequality χ_ℤ ≤ χ_ℝ, whose equality is the
nuance above.

## 6. Lemma 𝔇-Sch

- **In the memo's reading (real rank).** δ ≡ 0 PROVED by §5, so the lemma is **false**: no such family exists.
- **In the ℤ-rank reading.** The defect depends only on (X_n, t_n). It suffices to take F with the same data and I_∞(F,F) ≠
  I_∞(E,E) (Theorem 3), so the lemma is also **false**, unconditionally.
- **"Transcendence defect of log p".** The log p are transcendental (Hermite–Lindemann) and ℚ-linearly independent
  (unique factorization; Baker for algebraic coefficients). The "defect" can only mean homogeneous relations of
  degree ≥ 2 over ℚ, and those are independent of the test. As the source of a quadratic form **in E**, the expression does not make
  sense.
- **Statement.** Lemma 𝔇-Sch: **NO-GO (PROVED), vacuous.** It is withdrawn as a "deciding lemma".

## 7. S1–S6

| | 𝔇₀ | 𝔇₁ | mixed area | 𝔇₂ |
|---|---|---|---|---|
| S1 (χ by computation, without the form) | — | yes, blind | yes, blind | yes, blind (Thm 6*) |
| S2 (integer, reads (ℕ,+,·)) | — | ℤ, only (ℕ,·) | ℤ, only positions | ℤ/ℝ, only (ℕ,·) |
| S3 (non-Poisson duality, χ quadratic **in E**) | — | no (M′) | quadratic in the polygon, not in E | no |
| S4 (P_T) | yes | yes | yes | yes |
| S5 (localized failure for Epstein) | — | yes (Ω_C is not a semigroup) | no | same as 𝔇₁ |
| S6 (Λ_cosh) | no | no | no | weight analogy, not PROVED |

**S1 ∧ S3: none.** The mixed area appears to satisfy both, but it is quadratic in the polygon's support function, not in E.
That is exactly what Theorem 5(a) says.

**Prop 6.4 / S6.** LEMMA_12_1 (PROVED as an identity) gives order 2 as (1/h)Σ_χ y_χ∗y_χ, with y-coefficients of type
Λχ/log. The memo, for its part, writes y·y′, which corresponds to (Λ/log)∗Λ. Neither of the two is the Λ∗Λ of Λ_2. Also, for
h = 3, κ₃ ≠ 0, so the cosh is an accident of h = 2. Prop 6.4 is downgraded from ARGUED to **STRUCTURAL ANALOGY**
(order-2 convolution, different weights). And even if it were exact, it would enter as a fixed coefficient, not as a χ depending on E.

**Other points.**
- **§7.1 (Mori μ = 15).** The constant Π_{p<15}(1 − 1/p) = 0.19181 is correct. The "unconditional" count is trivial, but
  correct.
- **§7.2.** Remains ARGUED.

## 8. Verdict and corrections

**Verdict: ACCEPTED WITH CORRECTIONS.** The memo is honest and nearly all of its NO-GOs hold. The main change **strengthens**
the closure: Theorem 6 moves to unconditional PROVED and Lemma 𝔇-Sch to NO-GO.

Mandatory corrections:

- (C1) Theorem 1: "countable" → "countable and closed (nowhere dense)". Step 6 rests on strict local positivity.
- (C2) Theorem 3, step 2: take h supported where |E| ≥ c and inside P_T.
- (C3) Corollary 3.7: withdraw the dichotomy and replace it with Theorem 3′ (rank genericity, ARGUED).
- (C4) Corollary M′: restrict to rank and determinant invariants. Remove "μ∘(m,n) ↦ mn" from Prop M. Add the
  D_f conjugation.
- (C5) Theorem 5(c): ⇒ PROVED, ⇐ OPEN, due to the radical obstacle.
- (C6) Prop 6.3 and Theorem 6: replace them with Theorem 6* (block Vandermonde, PROVED, all t). Remove
  "CONDITIONAL on Schanuel". Add the ℤ-rank nuance (four exponentials, irrelevant due to Theorem 3).
- (C7) Lemma 𝔇-Sch: NO-GO, vacuous.
- (C8) Prop 6.4: ANALOGY (weights Λ/log vs Λ).
- (C9) Correct "escapes Theorem 3" in §6: the system does not depend on the test.

Row D / L′♯: **OPEN, no change.**

## 9. Entry for ROUTES-TRIED-INDEX

- **AUDIT_200_DCONS_001 (phase 200, r22, audit of D_CONSTRUCTION_001).** There are two independent reasons beyond
  Schanuel. (1) The Siegel–Dyson system (3.1) is block-diagonal in N = mn with Vandermonde blocks (log n_j)^k, so
  h⁰_ev = h⁰_gen = Σ(r_N − t)⁺ and δ ≡ 0 (PROVED, all t). (2) The system does not contain the test. Hence Lemma 𝔇-Sch is NO-GO
  and the Siegel–Dyson/Möbius/mixed-area entire correspondences are closed as quadratic RR.
- Theorem 3′: every rank-type χ with analytic dependence on the test is generically constant (ARGUED). A χ that sees the
  test needs non-analytic (sign) dependence, which points it toward REF-D.
- Theorem 5(c): only direction ⇒ is PROVED. Prop 6.4 (Λ∗Λ ↔ Λ_cosh) is an analogy with different weights. Do not retry.
