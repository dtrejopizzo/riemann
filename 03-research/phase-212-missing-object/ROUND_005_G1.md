# Round 5, seed G1: object of degree ≥ 3 whose Hessian is the form

Notation from `../phase-211-sign-sandbox/STATEMENT_001.md`. We work in a parity sector
L²_±(I_T) (F(−t) = ±F(t)); there B = ±A, and P_T ∩ L²_± = ker A ∩ L²_±, a hyperplane of the sector. All
forms are real. "n₊(H)" is the maximal dimension of a subspace on which H > 0.

Own verdict: **I did not manage to write an object satisfying A1–A6.** What does get written is the
whole class of objects the seed asks for (§1), the exact identity linking them to a_T (§2) and a
dichotomy lemma with declared class (§3) explaining why degree ≥ 3 does not provide an independent
sign source in the four families of hyperbolicity certificates that I know
(determinantal, nonnegative change of variables, product of factors, exponential generating function). The
"product" family is the only one where the Euler product enters; it reduces to the local certification of
`phase-159/G2_B8_R5.md` (Thm. D, L″).

## 0. Cross-check (goes first, BRIEF rule 3)

1. **Closest antecedent**, read as primary source: `phase-160-row-d-infinite-T/R160_C7_R1.md` §6.2
   (the Lorentzian class of degree two, closure under limits and Alexandrov–Fenchel reduce to the
   statement) and §6.3(2) (raising the degree: candidates Str(Γ_F^k) without transpose, or with transpose and
   twisted by Φ_F^{k−2}; OPEN for lack of an independent source of nonnegative coefficients).
   Second antecedent, read as primary source: `phase-159-row-d-two-front-construction/G2_B8_R5.md` Def. 1,
   Lemma 2.1, Thm. D and Thm. L″ (local certification by Euler factor: does not exist for T ≥ 0.5925).
   Third: `phase-195-modern-tools/INV_M_001` §§1–3 (real stability and Gårding applied to the definite
   form of the block 𝔸; read §§0–2). Fourth: R4-c (`REVIEW_004.md`; the "target with
   margin" format), read via the review.
2. **What is new here:** the examination of the Hessian of a hyperbolic polynomial of degree d ≥ 3 at the
   base point and the dichotomy of Lemma 3 (the coefficients of degree ≥ 3 can only enter as a margin
   a_T ≥ c|·|^{2/k}); the identification of each class of certificates with (G) with ρ = 0 or with the
   local certification of G2_B8. R160_C7_R1 §6.3(2) only examined Str(Γ_F^k).
3. **Why this does not sidestep the difficulty:** because Lemma 3 proves that it does not; see §3.
4. **Identity with global positivity:** Lemma 1 (exact equivalence of the target in a sector with
   "n₊(H_{e,κ}) ≤ 1") plus the hyperbolic eigenvalue identity (Lemma 2).

Not opened as primary sources: Paper 46; Paper 47 thm:parityschur and prop:polarcap (only via `REVIEW_004`);
`ROUND_004_B.md` (only via `REVIEW_004`); phase 120 and 114_d_244 (only via `ANNEX_COTEJO_LORENTZ_1.md`);
`SURVEY_MODERN_UNTRIED.md` B1 and `FAMILIES_A_001` A4 (grep lines only). Grep for "Renegar",
"hyperbolic polynomial", "hiperbólico respecto", "triple correlation", "trilineal": only the files already
cited and P122_012 (a trilinear form unrelated to this, line 49). This does not prove novelty.

## 1. Object

**Space.** E_T^± := L²_±(I_T) (or any finite compression containing the base point); the object
is defined on finite compressions E ⊂ E_T^± ∩ 𝒟_T with e ∈ E, and "hyperbolic on E_T^±" means
hyperbolic on every finite compression containing e.

**Base point.** Any e ∈ E_T^± with A(e) ≠ 0; the natural one is the Tate vector of the sector,
e_± := (e^{t/2} ± e^{−t/2})1_{I_T}.

**Target form at the base point.** For κ ∈ ℝ,

    H_{e,κ}(F) := −a_T(F) + (2/A(e)) A(F) a_T(e,F) + κ A(F)²,   F ∈ E_T^±.        (1.1)

**Object.** A functional p : E_T^± → ℝ homogeneous of degree d ≥ 3, polynomial on each finite compression,
with

    p(e) > 0,   D²p(e)[F,F] = H_{e,κ}(F)   for all F,                            (1.2)

and hyperbolic with respect to e: for every F the polynomial t ↦ p(F + t e) has only real roots.
Writing p(te + F) = p(e) ∏_{i=1}^{d} (t + λ_i(F)), the λ_i(F) ∈ ℝ are the hyperbolic eigenvalues
(1-homogeneous, continuous, nonlinear in F).

Trivial example (shows that the class is nonempty if and only if the target holds in the sector):
p = ℓ^{d−2}·q with q(F) := ½H_{e,κ}(F) + (terms in ℓ) and ℓ linear, ℓ(e) > 0. It uses nothing.

## 2. Identity

**Lemma 1 (PROVED).** Let e with A(e) ≠ 0 and κ > −a_T(e)/A(e)². Then
(a) H_{e,κ}(e, F) = (a_T(e)/A(e) + κA(e)) A(F) and H_{e,κ}(e) = a_T(e) + κA(e)² > 0;
(b) H_{e,κ} = −a_T on P_T ∩ E_T^±;
(c) a_T ≥ 0 on P_T ∩ E_T^± ⟺ n₊(H_{e,κ}) ≤ 1.

*Proof.* (a) With ℓ := a_T(e,·)/A(e): H(e,F) = −a_T(e,F) + A(e)ℓ(F) + A(F)ℓ(e) + κA(e)A(F)
= A(F)(ℓ(e) + κA(e)), and ℓ(e) = a_T(e)/A(e). (b) A(F) = 0. (c) ⇒: H ≤ 0 on the hyperplane ker A, hence
every subspace on which H > 0 meets ker A only in 0 and has dimension ≤ 1. ⇐: by (a), the H-orthogonal of
e is ker A. If F ∈ ker A with H(F) > 0, on span{e, F} the matrix of H is diag(H(e), H(F)) > 0, and
n₊ ≥ 2. ∎

**Lemma 2 (eigenvalue identity; PROVED, algebra).** If p is hyperbolic with respect to e with (1.2),
then for F ∈ P_T ∩ E_T^±

    Σ_i λ_i(F) = 0,     a_T(F) = p(e) Σ_i λ_i(F)².                                   (2.1)

*Proof.* p(e + sF) = s^d p(e/s + F) = p(e)∏(1 + sλ_i(F)). The coefficient of s is p(e)Σλ_i = Dp(e)[F];
by Euler homogeneity, D²p(e)[e,F] = (d−1)Dp(e)[F], and by (1.2) and Lemma 1(a) this is a multiple
of A(F) = 0. The coefficient of s² is ½D²p(e)[F,F] = p(e)σ₂(λ) = ½p(e)((Σλ)² − Σλ²) = −½p(e)Σλ²; with
(1.2) and Lemma 1(b), −a_T(F) = −p(e)Σλ_i². ∎

(2.1) is a sum of squares of nonlinear functions of F, exact on all of P_T ∩ E_T^±: it has the
form of (G) with V_T F := √p(e)(λ_i(F))_i, except that V_T is not linear. But its content is entirely the
hyperbolicity: the identity is tautological once the roots are real.

## 3. Mechanism, and why it does not work in the classes I can write

**Cited theorem (CITED: Gårding 1959; Renegar 2006; Brändén–Huh 2020).** If p is hyperbolic with respect
to e, D²p(e) has n₊ ≤ 1 (the Renegar derivative D_e^{d−2}p is a hyperbolic quadratic, of
signature (1, ·)). A polynomial with coefficients ≥ 0 is Lorentzian if and only if its support is M-convex
and each ∂^α p with |α| = d − 2 is a quadratic with at most one positive eigenvalue.

With Lemma 1(c), existence of the object gives the target in the sector. The only open hypothesis is
hyperbolicity. The following lemma shows that hyperbolicity is sufficient (and necessary) only along
the lines e + sF, F ∈ P_T, and that there the coefficients of degree ≥ 3 do not help.

**Lemma 3 (degree dichotomy; PROVED).** Let p be homogeneous of degree d ≥ 3 with (1.2), and suppose that
s ↦ p(e + sF) is real-rooted for all F ∈ P_T ∩ E_T^±. Then for 3 ≤ k ≤ d and all F ∈ P_T ∩ E_T^±

    |D^k p(e)[F^k]| ≤ k!·C(d,k)·p(e)^{1−k/2}·a_T(F)^{k/2}.                           (3.1)

Consequently, on ℝe ⊕ (P_T ∩ E_T^±) exactly one of two holds:
(i) D^kp(e)[F^k] = 0 for all k ≥ 3 and all F ∈ P_T; then
    p(αe + F) = α^{d−2}(α²p(e) − ½a_T(F)): the object is ℓ^{d−2} times a quadratic, and its hyperbolicity
    is that of the quadratic, i.e. n₊ ≤ 1 in degree two: R160_C7_R1 Prop. 6.2 verbatim;
(ii) some coefficient of degree k ≥ 3 does not vanish on P_T, and hyperbolicity implies the target with
    margin a_T(F) ≥ c_{d,k} p(e)^{1−2/k} |D^kp(e)[F^k]|^{2/k}.

*Proof.* By Lemma 2, Σλ_i = 0 and Σλ_i² = a_T(F)/p(e), hence |λ_i| ≤ (a_T(F)/p(e))^{1/2}. The
coefficient of s^k is D^kp(e)[F^k]/k! = p(e)σ_k(λ), and |σ_k(λ)| ≤ C(d,k) max|λ_i|^k. In case (i),
p(αe+F) = Σ_j α^{d−j}D^jp(e)[F^j]/j! reduces to j ∈ {0, 2} (j = 1 vanishes by Lemma 2). ∎

For d = 3 the lemma is exact: with p(e) = 1 and Dp(e)[F] = 0, p(e+sF) = 1 − ½a_T(F)s² + c s³, c = p(F);
the cubic x³ − ½a_T x + c (x = 1/s) is real-rooted if and only if a_T(F)³ ≥ 54·p(F)². Hyperbolicity of a
cubic object on P_T **is** the inequality a_T ≥ 54^{1/3}|p|^{2/3}: the strengthened target.

**Reading (PROVED as a consequence of Lemma 3).** Terms of degree ≥ 3 cannot be a sign
source: in case (ii) they are an additional lower bound that the object must pay; in case (i)
they disappear. It is the pattern of R4-c (format with additive defect = target with margin), now in higher
degree. Since λ_A(T) ≤ 4·10⁹Te^{−15.449T}, in (ii) the coefficients D^kp(e)[F^k] must be
≤ C·λ_A^{k/2} on the near-minimizers: the object would have to know the near-minimizers (pattern B9).
This last point is ARGUED (it was not proved that they vanish only there).

**Classes of hyperbolicity certificates.** All that would remain is a proof of real-rootedness of
s ↦ p(e+sF) that does not use the sign of its s² coefficient. The four standard classes:

**C1. Determinantal (PROVED).** p(x) = det(Σ_i x_iM_i), M_i symmetric, M(e) ≻ 0 (for example
det(tI + xE + y·𝒪_F) from hint (iii)). Normalizing M(e) = I and X_F := M(F) (linear in F):
p(e+sF) = det(I + sX_F), λ_i(F) = eigenvalues of X_F, and (2.1) is

    a_T(F) = ‖X_F‖²_HS   on P_T ∩ E_T^±,   with tr X_F = 0 there.

It is (G) with ρ = 0 and V_T = X linear: exactly `OBJECT_SPEC.md` (G). The degree d = rank of X does not
intervene. Hint (iii) adds no mechanism: one has to write X_F, which is the original problem.

**C2. Nonnegative change of variables of a fixed Lorentzian (PROVED).** p = q∘𝒜 with q Lorentzian on
ℝ^N (e.g. an elementary symmetric polynomial) and 𝒜 linear with 𝒜e in the positive orthant. Then
D²p(e) = 𝒜ᵀD²q(𝒜e)𝒜, and D²q(𝒜e) = uuᵀ − GᵀG. On P_T, as in Lemma 1(c), the H-orthogonal of 𝒜e is
diagonalized explicitly and a_T(F) = ‖W G𝒜F‖² with W = I − ww^T/(1 + √(1−|w|²)),
w = G𝒜e/(u·𝒜e), |w| < 1. Again (G) with ρ = 0 and V linear. Moreover, if the coordinates are those of a
basis {φ_i} with F = Σx_iφ_i and q with coefficients ≥ 0, ∂_i²p(e) = H(φ_i) ≥ 0 requires a_T(φ_i) ≤ 0 + polar:
no basis with localized elements works, because a_T(φ_ε) ≍ ‖φ‖² log(1/ε) (R160_C7_R1 Thm. 3(b),
CITED): it is the "diagonal −∞" obstruction of §6.2(a).

**C3. Exponential generating function (hint (ii); PROVED).** Z(F) = Σ_n w_n exp(ℓ_n(F)) (or ∫ dμ), w ≥ 0: log Z is
convex and D² log Z(e)[F,F] = Var_{μ_e}(ℓ_·(F)) is a variance. If a_T = D² log Z(e) on P_T, it is (G)
with ℋ = L²(μ_e) and V F = ℓ_·(F) − E ℓ_·(F), ρ = 0. The Gårding version (Z^{1/d} concave on a cone)
reduces, at the base point, to the same reversed Cauchy–Schwarz of Lemma 1(c). Neither the cone {F ≥ 0} nor the
cone of positive Tate moments gives anything: P_T is on the boundary of the second and {F ≥ 0} ∩ P_T = {0}
(an F ≥ 0 with ∫F e^{t/2} = 0 is zero).

**C4. Product of hyperbolic factors; here the Euler product enters (PROVED except what is cited).**
p = ∏_j p_j with each p_j hyperbolic with respect to e (the product is too, and its cone is the intersection).
Then log p(e+sF) = Σ_j log p_j(e+sF) and, on P_T ∩ E_T^±,

    a_T(F) = Σ_j S_j(F),   S_j := −p(e)·D² log p_j(e) ⪰ 0 on all of E_T^±.             (3.2)

(Lemma 2 applied to each factor: S_j = p(e)Σ_i λ_i^{(j)}(F)², and Σ_j σ₁^{(j)} = 0 on P_T.)
(3.2) is a decomposition of a_T into positive semidefinite forms, one per factor, modulo terms
A·m that vanish on P_T. Without restriction on what each S_j sees the decomposition is trivial (S_1 = a_T).
With the restriction that gives meaning to "Euler product":

- *Genuine Euler factor (without archimedean part).* S_p = −Q_p + A·m_p with
  Q_p(F) := Σ_k v_{p^k} Re c_F(k log p). **It is not ⪰ 0 on P_T (PROVED).** For log p < 2T, let χ ∈ 𝒟 be
  even, with support of width < ½ log 2 near 0, ψ := (¼ − ∂²)χ (then ∫ψ e^{±t/2} = 0, and likewise
  for its translates) and F_± := ψ(· − ½log p) ± ψ(· + ½log p) ∈ P_T ∩ E_T^±. Then
  c_{F_±}(log p) = ±‖ψ‖², c_{F_±}(k log p) = 0 for k ≥ 2, and Q_p(F_±) = ±v_p‖ψ‖². In the even sector
  Q_p(F_+) > 0, hence S_p(F_+) = −v_p‖ψ‖² < 0; in the odd one two pairs of bumps are used with
  signs (+,+) at distance log p, separated symmetrically. Hence the isolated Euler factor is never
  hyperbolic with this Hessian, and the archimedean part has to be distributed among the primes.
- *Euler factors with translation-invariant Lévy archimedean distribution (K_p ≥ 0):* this is
  exactly the local certification of `G2_B8_R5.md` Def. 1 in the primitive form and in the variant with
  polar pieces. Thm. D: it exists if and only if Φ_T ≥ 0; Thm. L″ (CITED; machine-verified, without
  interval arithmetic): Φ_{0.5925} < 0, hence **it does not exist for T ≥ 0.5925**. The class dies already at
  c = 1.
- *Translation-invariant archimedean distribution but with arbitrary symbols m_p (not Lévy),
  Σ m_p = m.* Not covered by G2_B8 (Def. 1 requires 0 ≤ K_p). OPEN; but the factor p ceases to be an
  Euler factor: it is a piece p_p whose logarithmic Hessian is that of the Euler factor plus a chosen
  multiplier, and hyperbolicity of p_p is the sign of the local form, quadratic, of degree two: it returns to
  R160 §6.2 factor by factor. I wrote no such distribution.

**Hint (i), triple correlation (ARGUED/OPEN).** C(F) := Σ_{m,n}Λ(m)Λ(n)(mn)^{−1/2}⟨F, τ_{log m}F ⋆
τ_{log n}F⟩ is a natural candidate for D³p(e)[F³]. By Lemma 3 case (ii) with d = 3,
hyperbolicity would require a_T(F)³ ≥ (const)·C(F)² on P_T: a strengthening of the target, not a
mechanism. Under cΛ, C scales as c² while a_T is affine in c. I did not verify whether that inequality is
even true at c = 1. It would require |C(F)| ≲ λ_A^{3/2} at the near-minimizers, and I see no reason for it
(ARGUED). The relation Λ·log + Λ∗Λ = μ∗log² enters none of the classes C1–C4. In C4 only
Λ ≥ 0 per factor enters.

## 4. Controls

Since there is no object with a mechanism, the controls are done on the classes of §3.

| Control | C1, C2, C3 (= (G) with ρ = 0) | C4 (product) |
|---|---|---|
| c = 2 | The line that breaks is the construction of V_T, which is not written: **I cannot point to it**. | Factor (1−p^{−s})^{−2} = square of a hyperbolic factor, which remains hyperbolic; S_p doubles in its comb part, the archimedean part stays fixed: the decomposition (3.2) needs to reassign the archimedean budget, and breaks there (reading of G2_B8 Thm. D). But the class already fails at c = 1 for T ≥ 0.5925. |
| non-integer c | same | Non-integer powers of factors are not polynomials: polynomial hyperbolicity is not defined. Formal breaking, not a sign one. |
| a_P (deletion) | same | Deleting factors preserves hyperbolicity of the remaining product. The breaking can only come from the archimedean pieces of the deleted primes (C_p < 0 possible, ΣC_p = C_0 < 0) not being ⪰ 0 by themselves. ARGUED. If all the C_p of the deleted ones were ≥ 0, **the mechanism would survive a_P and would be wrong**. |
| no product (Davenport–Heilbronn, Epstein) | same | There is no factorization: the class does not apply. Correct, but empty. |

Conclusion of the controls: in C1–C3 the mechanism is (G) and the controls remain to be done on a V_T
that nobody wrote. In C4 the only distribution with content (Lévy) already fails at c = 1, and the a_P control is
not guaranteed.

## 5. Own verdict

**I did not manage to write an object satisfying A1–A6.**

What was proved (PROVED):
- Lemma 1: exact equivalence of the target in a sector with n₊(H_{e,κ}) ≤ 1, with any e with
  A(e) ≠ 0 as base point (including the Tate vector), without assuming a_T(e) < 0.
- Lemma 2: every hyperbolic object of degree d with that Hessian gives a_T = p(e)Σλ_i(F)² on P_T, a
  nonlinear and tautological sum of squares.
- Lemma 3 (NO-GO with class): in the class "p homogeneous of degree d ≥ 3, Hessian H_{e,κ} at e, real-rooted
  along e + P_T", the coefficients of degree ≥ 3 either vanish (and the object is ℓ^{d−2}·quadratic, the
  class of R160 Prop. 6.2) or force the target with margin a_T ≥ c|D^kp(e)F^k|^{2/k}. For d = 3
  hyperbolicity is exactly a_T³ ≥ 54p². Degree ≥ 3 is not an independent sign source.
- C1–C3 reduce to (G) with ρ = 0 and V linear. The diagonal −∞ excludes localized bases in the
  version with coefficients ≥ 0.
- C4: a genuine Euler factor never has log-Hessian ⪰ 0 on P_T (bumps at distance log p). With
  Lévy distribution it is G2_B8, dead for T ≥ 0.5925 (CITED, without intervals).

What failed and why: the "independent nonnegative coefficient" that R160 §6.3(2) asks for does not exist in these
classes, because at the base point every hyperbolicity certificate reads as a sum of squares
per factor (Lemma 2, (3.2)). Terms of degree ≥ 3 only subtract slack (Lemma 3).

Not excluded (no object): real-rootedness certificates of s ↦ p(e+sF) not listed in C1–C4 (Pólya–Schur
operators or Borcea–Brändén preservers applied to a family in F, limits of non-factorized
real-rooted families); non-Lévy archimedean distributions in C4; a base point depending on F (Lemma 3 is
at a fixed point).

Concrete next step: if reopened, the only gap with a shape is C4 with non-Lévy symbols m_p. One has
to write the m_p and check n₊ ≤ 1 per factor, knowing that this is again degree two factor by
factor. I do not recommend it without a per-factor mechanism that is not the sign itself.
