# AUDIT_201_SPEC_001: audit of SPEC_201_001 (B-V1, non-negative rank with threshold)

I did not wait for the V1.1′ computation:
this audit is structural and states what that computation has to show.

## Summary (≤200 words)

The diagonal invariance lemma is correct (PROVED). But the family, as written, has a structural defect that the
V1.1′ computation cannot repair. (1) I_T^X(g) is an entire semialgebraic function of finitely many linear functionals
of g (values g(log m/k) and local κ_∞) and of the finite weights v_n^X. Hence it is locally constant on a dense open
subset of P_T: it escapes the letter of Thm 3′, but not its argument. (2) The comb channel is the threshold pattern of
a matrix of near-coincidences m = kn ± 1. That is C-emb branch (a), and moreover it appears on the "do not retry" list
of SPEC_007 §C4. The spec gives no written reason for this. (3) T201-a ∧ T201-b is, for Λ, literally L′♯ (branch 2).
Its X-uniform version is falsified by a_P or cΛ if T201-b uses only v_n ≥ 0. (4) r_+ cannot see whether a polytope is
empty. (5) With minimum matrix size ≤ 3, I ≡ 0.

**Verdict: conditional NO-GO (branch 2 + C-emb a)**, reversed only if V1.1′ satisfies conditions V1–V3 of §7.
Second option: B-V2.

---

## 1. Diagonal invariance and the threshold: genuine channel or artifact?

**Lemma** r_+(D₁MD₂) = r_+(M) for positive diagonal D_i: PROVED. The factorization carries over, and the same holds
with D_i⁻¹. Its consequence (b), that r_+ does not separate cΛ without a threshold, is also well proved.

**The consequence the spec does not draw.** With a threshold, entry (k,n),(m,ε) is positive iff
v_n^X·g(log m/k) > κ_∞(g;m,k). Within a sign cell the matrix is

  M = D_v ∘ G(g) − K(g) restricted to the support σ,

and r_+ depends on the comb only through two things: (i) **which entries exceed the threshold**, a Boolean pattern
determined by the ratios κ_∞(g;m,k)/g(log m/k) compared to v_n; (ii) the values v_n within the support, which **no
longer factor** as D_v·(·) because K(g) is subtracted. Point (ii) is the only part that is not a pattern.

**A hand-picked choice?** Yes, twice. First, δ_T = ½log(1+1/N_T) is a chosen window, and κ_∞ is not any term of
𝔞_T: the archimedean part of the form is ∫_{[−2T,2T]} gK_∞, and the spec chops it into windows of width 2δ_T around
the points log(m/k). The windows overlap, because different (m,k) give equal or nearly equal ratios, and they leave
out almost all of [−2T,2T]. Second, the comparison "a pointwise comb contribution against a local archimedean cell"
has no justification in def:PD or thm:Z. Changing δ_T changes the threshold pattern, and the spec does not require
I_T to be stable under δ_T.

**Decision: C-emb branch (a). ARGUED, and I consider it solid.** All dependence of M_T^X(g) on the comb passes
through the finite list {(n, v_n^X) : n ≤ N_T} and through the positions log((kn+ε)/k). This is exactly a functional
that reads ν through the window: a finite list with its factorizations. Moreover: the block ε = ±1 is by definition
an **additive near-coincidence matrix**, and SPEC_SIGN_OBJECT_007 §C4 states verbatim "Do not retry: … matrices or
spectra of near-coincidences …". The spec does not mention that item nor give the written reason required. The new
reason it does give (the threshold, as opposed to diagonal invariance) answers a different objection. There is an
honest caveat: C-emb (a) alone does not kill it. 𝔞_T is also a function of the finite list, so that (a) degrades to
"datum" and only kills when combined with §4 (the use made of the datum is REF-D). The "comb" discontinuity is
discontinuity in the inequalities v_n ≷ κ_∞/g, which is a finite pattern of comb-vs-threshold comparisons. The
threshold is not a channel of Λ: it is a channel of the *ratio* between the weight and a hand-truncated archimedean
piece.

**Beurling, additional remark.** The spec says the blocks ε = ±1 are empty for Beurling. In fact, if the columns are
integers m and the kn are not integers, **the block ε = 0 is also empty**: the separation is by indexing. That is
trivial support separation (Lemma A.0 / C-emb branch c), not G1 overcome.

## 2. Thm 3′ and "no generic value"

The spec is right at the letter level: (·)_+ is not analytic, and r_+ is not the rank of an analytic matrix. Thm 3′
does not apply literally. **But the argument of Thm 3′ does apply.**

**Lemma (PROVED, standard in semialgebraic geometry).** Let L : P_T → ℝ^J, with L(g) = (g(log m/k), κ_∞(g;m,k)),
J finite, linear and continuous. Then I_T^X(g) = Φ_X(L(g)), where Φ_X : ℝ^J → ℤ is semialgebraic. (r_+ ≤ s is a
projection of a semialgebraic set, Tarski–Seidenberg; (·)_+ and rank are also semialgebraic.) Every integer-valued
semialgebraic function is locally constant outside a semialgebraic set of dimension < J. Hence I_T^X is **locally
constant on a dense open subset of P_T** (preimage under L, open and dense in the image).

"No generic value" is true but irrelevant. Thm 3′ does not use that the generic value is *unique*. It uses that χ is
locally constant on a dense open set while the form (linear in g) is not constant on any open set. That kills any
*identity*. Against an *inequality* (T201-a) the argument does not kill it, and I leave that for §4.

**Does I_T depend on the sign of the form or only on the sign pattern of g?** I distinguish:
- Outside the cells, I_T depends on g through the sign pattern σ(g) of v_n g(x_j) − κ_j. That is **not** the node
  pattern of g: it is the pattern of inequalities between values of g and local functionals. Thm 3 (nodes and
  supports) does not cover it literally.
- Inside a cell, I_T depends on the semialgebraic position of L(g), i.e. on **finitely many values** of g. That is
  exactly the case "conditions that use values of g" that AUDIT_200 §66 leaves outside Thm 3 and inside 3′, with the
  sole difference of semialgebraic versus analytic.

**Decision.** I_T does not see the sign of 𝔞_T. It sees the sign of **J linear functionals distinct from 𝔞_T**. The
form 𝔞_T is not a function of L(g), because ∫gK_∞ outside the windows is free. Hence each fiber {L = ℓ} contains tests
with 𝔞_T of any sign the class allows: I perturb f by φ orthogonal to finitely many first-order conditions, and 𝔞_T(g)
varies while L(g) stays fixed (ARGUED, by finite codimension). I_T is, in practice, "a finite datum of values," and
falls within the spirit of Thm 3/3′: it is not blind to the test, but it is blind to the direction that decides the
sign.

## 3. REF-D, branch 2: whose polytope slack is M?

**Yannakakis (CITED, verified from the auditor's memory, JCSS 43 (1991) 441–466):** if P = {x : Ax ≤ b} = conv(V),
then xc(P) = r_+(S) with S_{ij} = b_i − a_i·v_j. **Every** non-negative matrix M is the generalized slack matrix of a
nested pair of polyhedra P ⊆ Q (Gouveia–Parrilo–Thomas et al.; "Which nonnegative matrices are slack matrices?",
arXiv 1303.5670, CITED): P = conv of the columns and Q = the polyhedron of the rows, in a space of dimension rank M.

For M_T^X(g) the pair is P(g) = cone of the columns (m,ε), Q(g) = intersection of half-spaces indexed by (k,n). It is
an object **constructed from M**, not the LP polytope of certificates from def:PD/thm:Z. The spec does not claim
otherwise (FAMILIES_B did, when it spoke of "slack"). The relation to Zenodo 23238720 is one of name, not of object.

**Can r_+ say anything about emptiness?** No (PROVED, trivial). Slack and extension complexity are defined for
non-empty pairs. An empty polytope has complexity 0 and no slack. Whether the certificate LP is feasible is a
question of **emptiness**, and r_+ measures the **size** of a representation of a set already assumed non-empty.
Even if M were the slack of the Paper 46 certificate polytope, r_+ would measure "how complicated the certificate
is," not "whether it exists." So the only way r_+ touches positivity is T201-a, and §4 shows that this inequality is
branch 2.

## 4. T201-a: does it have content?

**Decisive observation (PROVED, logical).** The spec combines (T201-b) I_T^Λ ≤ j_T for all g with (T201-a) β_T(j) = 0
for j ≤ j_T. Restricted to the image of I_T^Λ, (T201-a) says exactly "𝔞_T^Λ(g) ≥ 0 for all g ∈ P_T." That is,
**(T201-a) in the form needed to conclude is L′♯ with a decorative index**. The extreme case is even clearer: if
rank ≤ 2 (or minimum size ≤ 3) throughout the window, I ≡ 0 and T201-a is literally L′♯. Branch 2, M4 of the spec
itself.

**A non-tautological version?** Only one: the **X-uniform** one,

  (T201-a_unif) for every comb X in a class 𝒳 ∋ Λ: 𝔞_T^X(g) ≥ −β_T(I_T^X(g))‖g‖.

Then the content would be in the class 𝒳 and the falsifiers would test it. But:
- the sketched proof of T201-b ("node kn = monochromatic rectangle because v_n ≥ 0") uses **only v_n ≥ 0**;
- a_P and cΛ have v ≥ 0, so the same argument gives I^{a_P}, I^{cΛ} ≤ j_T;
- with T201-a_unif one would obtain 𝔞^{a_P} ≥ 0 and 𝔞^{cΛ} ≥ 0 in the windows where the battery certifies 𝔞 < 0.
  **Contradiction** (falsifier rows 7–10 of the battery, CITED in the corpus).

Hence (PROVED, conditional on the proof of T201-b using only signs): **T201-a_unif ∧ T201-b(signs only) is
false.** To survive, T201-b has to use the exact values of Λ against κ_∞, and then it is no easier than the goal.

**Any conceivable mechanism?** For r_+ of a matrix of values of g to control a form *linear in g* (quadratic in f)
would require the region {I = 0} to be contained in {𝔞 ≥ 0}. By §2, {I = 0} is a union of fibers of L, and in each
fiber 𝔞 has degrees of freedom outside the windows. By Cohen–Rothblum, I = 0 is automatic when rank ≤ 2. A large
rank-2 matrix covers an open set of tests with no restriction on ∫gK_∞ outside the windows. I see no mechanism.
**Assessment: T201-a is vacuous (if quantified only over Λ) or false (if uniform with signs-only T201-b).**

## 5. Falsifiers: a_P with a worked example

**Internal contradiction.** C.1 defines R_T = {(k,n) : v_n^X ≠ 0}, so that rows with v_n^{a_P} = 0 **do not exist**.
C.4, instead, reasons with entries (0·g − κ)_+. One must choose:
- **(A) excluded rows:** M^{a_P} is a row-submatrix of M^Λ, with the same values in the remaining rows
  (v_n^{a_P} = v_n for p ∤ n, and for n = p^j the row disappears);
- **(B) included rows:** row (k,p) is ((−κ_∞)_+, …). It is independent of p and of the comb: it is an archimedean
  datum. In that case, **the only difference between a_P and Λ is that in those rows v_p g − κ is replaced by −κ**.

**3×3 example (PROVED, by hand).** For any 3×3 M ≥ 0: if rank ≤ 2, r_+ = rank (Cohen–Rothblum); if rank = 3,
r_+ = 3 ≤ min(3,3). Hence I ≡ 0 for every 3×3, whether Λ or a_P, with or without threshold. Take for example
M^Λ = [[a,0,b],[0,c,d],[e,f,0]] with generic entries > 0 (rank 3) and remove row 2 (version A, a_P): a 2×3 matrix of
rank 2 remains, with I = 0. In version B, row 2 becomes (κ',0,0) and the matrix has rank ≤ 3, with I = 0. **Both the
rank and r_+ change equally, and I^Λ = I^{a_P} = 0.** The caller's suspicion is correct at 3×3, and for stronger
reasons than the null rows.

**The first non-trivial case is 4×4 of rank 3**, for example the slack of the square
[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]: rank 3, r_+ = 4, I = 1 (CITED, classical). If a row is deleted, 3×4 remains,
with I = 0. So a_P **can** change I, but it does so by **lowering the size**: with rule (A), I^{a_P} ≤ I^Λ is the
typical case. That runs **against** the alignment required by V1.1′ ("I^Λ ≤ I^X where 𝔞^X < 0"). For a_P, separation
will come out with the wrong sign, which is exactly criterion M2. Prediction (ARGUED): with rule (A), V1.1′ for a_P
falls into M2.

**Size in the a_P window.** For T ≤ ½log7, N_T ≤ 7, the rows with Λ(n) ≠ 0 and kn ≤ 7 are (1,2), (2,2), (3,2), (1,3),
(2,3), (1,4), (1,5), (1,7): 8 rows and 24 columns, each row with ≤ 3 nonzero entries. It is a very sparse matrix. Rank
and r_+ are essentially combinatorial (rectangle covering of the support, a lower bound for r_+), and the support is a
function of the threshold pattern: C-emb (a) again.

**cΛ.** It separates only in cells stuck to the walls v g ≈ κ/c, as the spec admits. Moreover the blocks ε = ±1 read g
at log n + O(1/kn), so with smooth g they are nearly identical copies of block ε = 0. That tends to lower the rank, not
create excess.

## 6. Citations

Verified from the auditor's memory (no web search was done in this pass; they remain CITED-pending for P46):
- **Yannakakis 1991** (JCSS 43:441–466): xc(P) = r_+(slack). ✓ What the spec attributes is correct.
- **Cohen–Rothblum 1993** (LAA 190:149–168): r_+ = rank if rank ≤ 2 ✓, and examples with r_+ > rank ✓. **The**
  claim "r_+ = 3 and r_+ = 4 occur on open sets of the rank-3 4×4 matrices" is **not** due to them. That belongs to
  the theory of non-negative-rank boundaries (Mond–Smith–van Straten 2003; Kubjas–Robeva–Sturmfels, Ann. Stat. 2015)
  and, for polygons, Padrol–Pfeifle (hexagons with xc 5 or 6 depending on position, both on open sets). **Attribution
  correction needed.** "Regular octagons" is a confused citation: the relevant objects are hexagons.
- **Vavasis 2009** (SIAM J. Optim. 20:1364–1377): deciding r_+ = rank is NP-hard ✓.
- **Moitra** (SODA 2013; SIAM J. Comput. 2016): algorithm in (nm)^{O(r²)} ✓. The spec says 2013 in one place and
  2016 in another: these are the two versions.
- **Fawzi–Parrilo** (Math. Program. 2016, "self-scaled bounds"): SDP lower bounds for r_+ ✓. The "psd rank" as a
  lower bound for r_+ is correct (rank_psd ≤ r_+), but computing it is no easier. The self-scaled bounds must be used.
- **Boolean rank ≤ r_+** ✓.

## 7. Verdict

**Conditional NO-GO, branches 2 + C-emb (a).** What is PROVED:
- (i) T201-a ∧ T201-b is L′♯ rewritten for Λ;
- (ii) the uniform version contradicts the battery if T201-b uses only signs;
- (iii) r_+ is blind to emptiness;
- (iv) I is locally constant on a dense open set, as a function of finitely many functionals distinct from 𝔞_T.

The object also fails the "do not retry" record of SPEC_007 (near-coincidence matrices) without the required written
reason.

**What V1.1′ has to show for the family to survive** (all three conditions, not one):
- **V1.** That there exist tests with minimum size ≥ 4 and rank ≥ 3 for which I^Λ ≠ I^X, **with the row rule fixed**
  (A or B, declared before the computation) and **stable under δ_T** (I equal for δ_T and δ_T/2). If it is not stable,
  the channel is the hand-chosen window: NO-GO.
- **V2.** Alignment with the correct sign for a_P and for cΛ: I^X > I^Λ at the witnesses with 𝔞^X < 0. With rule (A)
  I predict M2.
- **V3.** That the separation is **not** explainable by the Boolean threshold pattern: the Boolean rank of the support
  must differ from r_+ at the witnesses. Otherwise I is a function of the finite comparison pattern (C-emb a) and
  dies.

Even with V1–V3, the family needs a T201-b that uses the exact values of Λ against κ_∞ and an X-uniform statement.
Otherwise branch 2 reappears. If V1.1′ gives M1 (rank ≤ 2 or I ≡ 0), which is likely at N ≤ 7 given the sparsity, the
NO-GO is recorded in the index in this same session.

**Second option: B-V2 (recurrence {x+y, xy}) better than B-V3 (Forster sign rank).**
- B-V3 suffers from everything above, and worse. Sign rank is invariant under positive row and column scalings
  (passes cΛ as in the diagonal lemma). It depends only on the sign pattern (a function of finite data, C-emb a/c).
  λ does not see Λ_cosh (S6 ✗). And Forster gives lower bounds, not signs of forms.
- B-V2 has a different risk (branch 4: blindness to ζ), but its invariant R_T(F) is a function of sets that is not
  tied to a matrix of values in a window. The first lemma V2.1 must prove, before anything else, that A_F cannot be
  defined from the finite list {n ≤ N_T} with factorizations (C-emb a). If it can, it dies the same way as this one.

**Entry for the ROUTES-TRIED index (Phase 201):** "B-V1 / SPEC_201_001: audited. T201-a ∧ T201-b = L′♯ rewritten
(branch 2, PROVED). T201-a_unif is incompatible with a_P and cΛ if T201-b uses only signs (PROVED conditional). r_+ is
blind to emptiness. I_T is locally constant on a dense open set (semialgebraic function of finitely many functionals
≠ 𝔞_T). The block ε = ±1 is a near-coincidence matrix (SPEC_007 §C4 do-not-retry). Conditional NO-GO, pending V1–V3
of V1.1′."
