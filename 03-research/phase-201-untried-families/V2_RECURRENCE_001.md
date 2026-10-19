# V2_RECURRENCE_001 — Family B-V2: additive-multiplicative recurrence {x+y, xy}

Phase 201, stage 3, single file I am writing.

## Summary (≤250 words)

I first ran the C-emb pre-test on the object proposed by FAMILIES_B_001 §V2 and SPEC_201_001. The result is
**NO-GO PROVED** for the object as declared, and **NO-GO ARGUED (by class)** for its infinite dynamical
extensions.

(1) **Theorem V2-0 (PROVED).** R_T(F) is a polynomial in the weights v_n and in the indicators
1{F(log n) > 0}, with n ≤ e^{2T}. It is therefore constant on each cell of the sign pattern of the finitely
many linear functionals F ↦ F(log n). That is C-emb (a). With the Thm 3′ argument, no identity with 𝔞_T is
possible. Against an inequality, each cell contains tests with 𝔞_T of both signs the class allows (ARGUED,
same as AUDIT_201 §2). Lemma V2.1 ("R_T is not a function of 𝔞_T") is true but useless: it dodges branch 5
and falls into C-emb (a).

(2) **Lemma V2-1 (PROVED).** Since F has compact support, A_F is finite and has density 0, so every
density-recurrence theorem is vacuous on A_F. Moreira, applied to the 2-coloring {A_F, ℕ∖A_F}, always gives
the configuration in the cofinite color. The only possible "infinite structure" requires extending F outside
the window, and then one of two things happens. Either the measure is independent of the test and the
functional is linear in g (branch b, Φ.1). Or the positivity holds only for functions ≥ 0, while the sign of
𝔞_T lives in g = f∗f̃, which is indefinite. This is the "estimate" branch.

(3) The cubic correlation ∫F·F∘(+y)·F∘(×y) has a first-order term linear in g. It has no "second-order" term
that is 𝔞_T with a remainder carrying a sign.

I give an index entry and a stricter criterion for returning to the inventory.

---

## 0. Index and corpus check (mandatory)

- **Index grep** (`05-meta-and-planning/ROUTES-TRIED-INDEX/`) with "Moreira", "Bergelson", "{x+y",
  "monochromat", "Furstenberg", "Ramsey": **0 hits** for the joint recurrence.
  - "sum-product": AUDIT_2026-10-15 l.72 (H4 Erdős–Szemerédi/Solymosi: "set statements ignore weights", only
    an estimate) and README l.259 ("sum-product (estimate)").
  - "Kronecker/solenoid": README l.61, 249, 263, 286 (measure on the Kronecker line; Kronecker minus Haar;
    additive/multiplicative frustration) and G4H/G4E phase 159–160 (Witt–Kronecker, DEAD).
  - "C-emb": README l.551–552 (SPEC_SIGN_OBJECT_007 + AUDIT_200: NO-GO accepted).
  - V1_1_NONNEG_001 l.575 (blocks j = kn).
- **Phase 161** (sum×product): uses Λ∗1 = log with additive Poisson in a *quadratic* construction and ends
  in the reverse Markov pullback (R161_016: the automatic direction of the norm does not close). V2 differs
  from 161 only by the recurrence theorem: a measure positivity for the affine action, instead of a
  quadratic identity. **The new written reason** (FAMILIES_B §V2) is that the joint recurrence is not a
  correlation inequality on a graph, so the frustration Thm 1.3 does not apply. I accept that reason as
  sufficient to *run* the pre-test, not to build further.
- **Literature** (FAMILIES_B / SPEC_201 table A, I did not redo the web searches): Bergelson–Richter
  (dynamical PNT), Frantzikinakis (averages with Λ weights, arXiv 1606.05630), Charamaras (TAMS 2025). None
  touches the Weil form.

## 1. Starting facts (with precision)

- **CITED.** Moreira, *Monochromatic sums and products in ℕ*, Ann. of Math. 185 (2017): for every finite
  coloring of ℕ there exist x, y with {x, x+y, xy} monochromatic.
- **CITED.** Bergelson–Moreira, *Ergodic theorem involving additive and multiplicative groups of a field and
  {x+y, xy} patterns*, ETDS 37 (2017): for a countable field K and A ⊂ K of positive density with respect to
  a double (additive-multiplicative) Følner sequence of the affine group, there exist x, y ≠ 0 with
  {x+y, xy} ⊂ A. There are also variants in finite fields (counting with error, Shkredov-type and others),
  which I do not use.
- **Elementary fact (PROVED): in ℕ the additive-density version is FALSE for {x+y, xy}.** Let A = odds, of
  density ½. If xy is odd, x and y are odd, and then x+y is even. So A contains no pair {x+y, xy}. The ℕ
  version can only hold with multiplicative-type or affine densities. In ℕ the state of the art is partial
  (later results for ℚ and for {x, y, x+y, xy} by Bowen–Sabok and Alweiss, as I recall). I mark it
  **CITED-unverified**: nothing that follows depends on it.
- **What matters to us.** All these theorems give a positivity for **sets** (or functions ≥ 0) of positive
  density in an **infinite** system. Their finitary version (by compactness) is a Ramsey number N(r): the
  conclusion holds on [1, N(r)] for every r-coloring. It is a combinatorial statement about a finite list.

## 2. The declared object and the C-emb pre-test

**Definition (FAMILIES_B §V2, Lemma V2.1).** Let X = e^{2T}, F ∈ P_T, A_F = {n ≤ X : F(log n) > 0}, and

  R_T(F) = Σ_{x,y ≥ 1; x+y ≤ X; xy ≤ X} v_x v_y 1_{A_F}(x) 1_{A_F}(x+y) 1_{A_F}(xy),

with v_n the comb weights (Λ(n)/√n in def:PD). FAMILIES_B's ergodic variant is
μ_Λ(A ∩ (A−u) ∩ u^{−1}A), averaged over u ≤ X, with μ_Λ a Furstenberg measure built from the comb. I treat
it in §3.

**Theorem V2-0 (PROVED).** There exists a function Φ_T : {0,1}^{⌊X⌋} → ℝ, with coefficients depending only
on {v_n : n ≤ X} (i.e. on the finite list {n ≤ X} with its factorizations), such that

  R_T(F) = Φ_T(σ(F)),  where σ(F) = (1{F(log n) > 0})_{n ≤ X}.

*Proof.* All indices x, y, x+y, xy appearing are ≤ X, because x, y ≤ xy ≤ X. Each summand is v_x v_y times a
product of three coordinates of σ(F). ∎

**Corollary V2-0.a (PROVED).** R_T is a function of the ⌊X⌋ continuous linear functionals L_n(F) = F(log n)
through a semialgebraic function with finitely many values (it is constant on each open orthant). Hence R_T
is locally constant on the dense open set {F : F(log n) ≠ 0 ∀ n ≤ X} of P_T. This is exactly C-emb (a)
(SPEC_007 C4: function of the finite list with its factorizations), in the form of AUDIT_201 §2's lemma.

**Corollary V2-0.b (PROVED, Thm 3′ argument).** There is no identity 𝔞_T(F) = Ψ(R_T(F), data of P_T) with Ψ
continuous in the second argument, nor any identity expressing 𝔞_T from R_T and finitely many linear
functionals other than 𝔞_T. Reason: 𝔞_T is not constant on any open set of P_T, because the archimedean part
∫g K_∞ is free outside the points log n. R_T, by contrast, is locally constant.

**Corollary V2-0.c (ARGUED, same status as AUDIT_201 §2).** Against an inequality of the type
"R_T(F) ≥ c ⇒ 𝔞_T(F) ≥ 0": the fiber {σ = σ₀} is an open cone defined by ⌊X⌋ conditions. Within it,
perturbing f by φ with φ∗f̃ + f∗φ̃ vanishing at the log n (finite codimension) moves 𝔞_T through the
archimedean part without changing σ. So R_T does not see the direction that decides the sign.

**On FAMILIES_B's Lemma V2.1.** "R_T is not a function of 𝔞_T" is true (seen with two tests in the same sign
cell and different 𝔞_T, or with two cells and the same 𝔞_T). But it only rules out branch 5. **The pre-test
required by AUDIT_201 §7 (C-emb a) fails.**

**Comparison with V1.** R_T does not decompose into blocks by j = kn, because it couples x, x+y and xy, and
so it does not repeat V1.1′-0's death. But that does not save it: it is killed by an earlier mechanism, the
finiteness of the data pattern.

**Pre-test verdict: NO-GO PROVED (branch C-emb (a) + Thm 3′) for the declared object.**

## 3. Does any infinite version escape? What infinite structure enters

The task statement allows an out: that the recurrence involve *all* n via an action on an infinite system. I
examine it.

**Lemma V2-1 (PROVED).** For F ∈ P_T (compact support in positions), the set {n ∈ ℕ : F(log n) > 0} is
finite. Therefore:
- (i) it has additive, multiplicative and affine density all equal to 0, and every density-recurrence
  theorem (Bergelson–Moreira and any ℕ analogue) is vacuous on it;
- (ii) Moreira, applied to the coloring {A_F, ℕ∖A_F}, holds trivially in the cofinite color. Taking
  x > e^{2T} gives {x, x+y, xy} ∩ A_F = ∅ for every y, without using the theorem.

Hence **no infinite structure enters through A_F**. For it to enter, an infinite object must be manufactured
from F or from the comb. There are exactly three natural ways, and I close them.

**(α) Furstenberg measure of the comb, independent of the test.** μ_Λ on a compactification (affine Bohr
compactification of ℚ, ℤ̂, or the solenoid), built as the limit of the empirical measures
Σ_{n≤N} Λ(n)δ_{ι(n)}/N, with F entering as a continuous function F̃ on X. Then:
- every functional ∫F̃ dμ_Λ, or average over u of ∫F̃∘τ_u dμ_Λ, is **linear** in the test. It is C-emb's
  branch (b) (linear in the comb, generic-comb Φ.1).
- Λ's Furstenberg measure is a *global* object (as N → ∞), and by the weighted PNT it is essentially Haar on
  the multiplicative Kronecker factor. That is the index's "Kronecker minus Haar" measure (README l.263,
  PROVED as a rewriting; l.249 and l.286, solenoid), with no information from the window [−T, T].
- The connection with the window only exists if F̃ = F∘log restricted to n, which returns to (Lemma V2-1).

**(β) Periodic or dilated extension of the test.** Let F^{per}(t) = Σ_k F(t − kL), or F_λ(t) = F(t/λ) with
λ → ∞, so that A is infinite with positive density. Then the configuration {x+y, xy} reads F at positions
log(x+y) ≈ log x (for y ≪ x) and log x + log y. The Bergelson–Moreira recurrence gives R^{ext} > 0 for
*every* set of positive density. That is **branch 4**: it does not distinguish ζ from Epstein, because O_K
has + and · and BM holds in every countable field. The quantity also depends on F outside [−T, T], where
𝔞_T sees nothing. ARGUED, and I consider it solid.

**(γ) Weighted cubic correlation (the task's suggestion).** Let

  C(F) = E_y ∫ F(x) F(x+y) F(xy) dμ(x),

with μ any suitable invariant measure. With g = f∗f̃, and 𝔞_T linear in g (def:PD), write F = 1 + εg (or
F = h + εg with h ≥ 0 fixed). Then

  C(1+εg) = 1 + ε [ ∫g + E_y∫g(x+y) + E_y∫g(xy) ] + ε² Q₂(g) + ε³ C(g).

- **The term that could reproduce 𝔞_T is the first-order one**, not the second-order one: 𝔞_T is linear in
  g, and Q₂ is quadratic in g (quartic in f).
  - The multiplicative summand E_y∫g(xy), weighted with Λ in y, gives the comb Σ Λ(n)g(log n), via
    Λ∗1 = log.
  - The additive one gives the translation term, which can approximate the archimedean part (Poisson).
  - So an identity "𝔞_T = (linear part of C)" is possible by adjusting weights. But that linear part is
    branch (b) (Φ.1) and inherits no sign: the sign of ε is free.
- **Recurrence positivity** (bounds of the type C(F) ≥ c(δ) > 0 for 0 ≤ F ≤ 1 with ∫F = δ) applies only to
  **nonnegative** functions. For F = 1 + εg with |ε|·‖g‖_∞ ≤ 1 it gives 1 + O(ε) ≥ c, which says nothing
  about the sign of the O(ε) term. The sign of 𝔞_T is a problem for **indefinite** g (g = f∗f̃ always takes
  negative values away from 0 at def:PD's witnesses). For g ≥ 0, the comb Σ Λ(n)g(log n) ≥ 0 is trivial and
  needs no Moreira at all.
- **There is no exact identity** 𝔞_T(F) = (linear in the {x+y, xy} average) + (remainder carrying a sign from
  recurrence): the remainder Q₂ + C has degree ≥ 2 and has no sign for indefinite g. Recurrence controls
  C(g) only if g ≥ 0. **"Estimate" branch** (like the index's H4 sum-product): at most it gives a bound
  |remainder| ≤ …, never a sign. ARGUED, and I consider it solid.
- **Is it G1?** The Λ channel in (γ) is Λ∗1 = log in the multiplicative summand. The additive one enters in a
  *separate* summand of the same linear order, not in a product with it, so at the order where 𝔞_T lives the
  {x+y, xy} configuration splits into two independent linear pieces. The joint +/· coupling appears only in
  Q₂ and C, which carry no useful sign. From the sign's point of view, the relevant term is "ℕ^× + Poisson"
  separately, which is phase 161's square (R161_002: "canonical square, sign-blindness"). This is not
  literal G1, but it is the registered rewriting.

**Conclusion of §3 (ARGUED by class, on (α)–(γ)).** Every infinite version is linear in the test (b), blind
to ζ (4), or an estimate on functions ≥ 0 that does not see the sign of an indefinite g. The joint recurrence
does not connect with the finite window [−T, T] through any channel other than the finite list (a).

## 4. Battery of falsifiers (for the record)

| falsifier | finite V2 (R_T) | infinite V2 (α–γ) |
|---|---|---|
| Epstein (log of values of Q) | R_T is defined the same way on positions log(values of Q) using + and · of O_K's integers. If S5 requires the multiplicative action to exist on the positions, it fails for Epstein (✓ S5). But R_T is the same type of finite pattern function, with no sign | BM holds in every countable field ⇒ branch 4 ✗ |
| DH (signed weights) | the pattern σ(F) does not see the weights beyond linear v_x v_y ⇒ no separation | linear ✗ |
| a_P (subsemigroup) | subset of summands; does not explain the witness (like C1 in SPEC_007 C5) | Haar on the Kronecker factor ✗ |
| cΛ (rescaling) | R_T(cΛ) = c²R_T(Λ): same sign, same pattern ⇒ no distinction ✗ | linear ⇒ scales ✗ |
| Mori (T ≤ ½log15) | data for n ≤ 15: gives no bound | — |

No falsifier resolves in favor of V2.

## 5. Target theorem

There is no surviving target theorem. What remains PROVED is negative:

**Theorem V2 (NO-GO PROVED, class "recurrence on A_F").** For every T and every recurrence functional R
built from the level set A_F = {n : F(log n) > 0}, with F ∈ P_T, and from the comb's weights, R is a
function of the sign pattern σ(F) ∈ {0,1}^{⌊e^{2T}⌋} and of the finite list {n ≤ e^{2T}}. Consequently it is
locally constant on a dense open set of P_T, and cannot enter any identity with 𝔞_T (C-emb (a) + Thm 3′).
Moreover, density-recurrence theorems are vacuous on A_F (Lemma V2-1).

**Proposition V2′ (ARGUED, class "infinite extension").** The extensions (α) Furstenberg of the comb, (β)
periodization or dilation, and (γ) cubic correlation fall respectively into branches (b), 4 and "estimate".

**First finite lemma** (was FAMILIES_B's Lemma V2.1): now resolved. It is true and useless.

**Residual risk.** A measure μ depending on the test in a way that is **nonlinear** and **not semialgebraic
in finitely many linear functionals** (e.g. an equilibrium or Gibbs measure of the affine system with
potential F, whose pressure is convex, analytic and non-polynomial in F) would escape V2-0. But:
- the pressure P(F) is convex in F, and its derivative is linear (branch b at first order);
- it is the already-registered "KMS / Gibbs" line (README l.249: "KMS beyond…").

I do not launch it without a new written reason.

## 6. Index entry (2–3 lines)

> **V2_RECURRENCE_001 (phase 201, family B-V2): recurrence {x+y, xy} (Moreira 2017, Bergelson–Moreira
> 2017) NO-GO.** Theorem V2-0 PROVED: R_T(F) on A_F = {F(log n) > 0} is a function of the finite sign pattern
> (C-emb a) ⇒ locally constant (Thm 3′). Lemma V2-1 PROVED: A_F is finite ⇒ density recurrence is vacuous;
> additive density in ℕ is false for {x+y, xy} (odds). Infinite extensions ARGUED: Furstenberg of the comb =
> linear (b) / Kronecker−Haar; periodization = branch 4 (BM holds in every field ⇒ Epstein); cubic
> correlation: 𝔞_T only at first order (linear), positivity only for F ≥ 0 ⇒ estimate. Do not retry without
> a nonlinear measure in the test that is not KMS/Gibbs.

(The integrator must add it to the index's README; this task only authorizes me to write this file.)

## 7. What remains of phase 201

- **B-V3 (Forster sign rank).**
  - AUDIT_201 §7 already anticipates that it depends only on the sign pattern of λ(m+n), m, n ≤ e^T, i.e. on
    a fixed finite datum, *independent of the test* (C-emb a/c). Worse than V2: it does not even see F.
  - The connection with the window is ‖H_N‖ = o(N), which is a bound (Chowla), not a sign.
  - Forecast: **NO-GO by the same Theorem V2-0**, without building it (ARGUED). I do not recommend launching
    it.
- **Recommendation: return to the inventory with a stricter search criterion.** The first three deaths (V1
  by blocks and C-emb a, V2 by C-emb a + finiteness, V3 foreseeable) teach that "integer or set invariant
  with no generic value" is not enough. The new criterion I propose is filter **S7**: the invariant must
  depend on the test F through a functional satisfying the following three conditions.
  - (i) it is not linear in g;
  - (ii) it is not a semialgebraic (or analytic) function of finitely many linear functionals of F. In
    particular it is not a function of the sign pattern of F at the points log n;
  - (iii) the nonlinearity does not reduce, at first order, to a linear derivative (pressure convexity,
    branch b).

  Also, as **S8**: the infinite structure must enter *through the window* [−T, T], not through an extension
  of F outside it. Lemma V2-1 shows that every object built from level sets of a compactly supported test is
  finite.
  - Candidates compatible with S7 a priori: functionals involving an infinite variational problem *inside*
    P_T (but that is REF-D/minimizer, README l.263), or spectral indices of infinite-dimensional operators
    built from F (whose index is locally constant: Thm 3′ again).
  - Honest forecast (ARGUED): S7 + S8 leave a very narrow class. The inventory should be measured against
    them first before choosing another family.
</content>
