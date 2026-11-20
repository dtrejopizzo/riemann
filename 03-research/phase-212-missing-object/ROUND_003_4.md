# ROUND_003_4 — Selection: boundary coordinate and null anchor with boundary inside (G)

Selection memo, not a construction memo. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

### Search performed

- Full primary reading: R170_861, 862, 866, 868, 869, 870; beginning and status of 859, 867, 874;
  R182_201 in full and README of phase 182; `REVIEW_002_A.md`, `REVIEW_002_BC.md`, `LEDGER.md`,
  `RULES_AVOID.md` §§B, D, I.
- grep in `03-research/` (all phases), `04-papers/47*`, `04-papers/48*` and
  `05-meta-and-planning/` for: «null anchor», «bordered null», «boundary anchor», «boundary
  coordinate», «β_T(f)», «ancla nula», «ancla con borde», «coordenada de borde», «complemento de
  Schur» / «Schur complement» next to a_T or P_T, «NGF», «invisib» next to núcleo/kernel.
- Hits opened in primary: phase 170 (862–874), phase 182 (`R182_RECTANGULAR_TUNNEL.md`,
  `R182_201_AUDIT_AND_NONLOCAL_GATE.md`), R179_CHAIN_GATE l. 252 (only cites 866). In 211,
  `ROUND_008_A.md` l. 26 and `ROUND_008_D.md` l. 18 cite «POLAR_CAP_001 (bordered Schur complement
  that inverts a_T|P_T itself — consumes λ_A > 0)»; there is no file with that name in the folder of
  211 (search by name without result), so it is known only through those two citations.
  P47 l. 4340–4350 (bordered Schur complement of a_T on P_T, polar term) and l. 5299
  (thm:coer-schur): read only at the cited lines.
- The other textual hits («boundary coordinates» in P121, P3 of phase 120, phases 57,
  72, 77, 78, 114/116) use «boundary» in another sense (Hadamard coordinates, Weyl boundary,
  capacity boundaries); they were not opened in full. I found no memo that writes a positive
  form with the null vector (Λ,1)⊗F ⊕ β_T(F) on all of P_T. That does not prove novelty: §2 shows
  that the format has none.

### (1) Closest antecedent

- R170_862 §§2–6: law of the null anchor with boundary. Lemma 2.1 (positive two-sided family ⟹
  P_N Ḣ P_N = 0); §3 (an anchor outside the kernel does not receive the cancellation, model (3.2)); §4 the
  four obligations of e_T; §5 the Tate column has ‖b‖² = 4(sinh T + εT) > 0.
- R170_868 §5: enlarged null vector ê_T(f) = ((Λ,1)⊗f, β_T(f)) with joint cancellation (5.4);
  §6: β_T(f) is constructed with (ρ_f, ℓ_f) from the first-contact equation PAf = ρ_f b, Q_eAf = ℓ_f.
- R170_869 (0.2)–(0.4) and R170_870 §§2, 4: the boundary class is linear and odd; it is independent of
  everything proved.
- R170_861 (0.3), §§2, 6 and R182_201 §2: a positive extension with fixed Schur complement is a
  triangular congruence; completing the block abstractly is equivalent to what is sought; only
  a non-local source factor remains open (NGF, R182_201 (3.1)–(NGF), OPEN).

Difference of framework requested by the task: all of phase 170 works with a vector f of the radical of a
supposed first-contact window and uses positivity to deduce an equality (Lemma 2.1). Phase
212 asks for the opposite direction: an identity (G) on all of P_T that produces positivity.

### (2) The object, written

Candidate format (bordered variant of (G)). Enlarged space

    Ê_T = (ℝ^N ⊕ ℝ) ⊗ ℋ ⊕ ℬ_T ⊕ 𝒳_T,

a manifest form 𝔾_T ⪰ 0 on Ê_T (for example 𝔾_T = 𝓔_T*𝓔_T with 𝓔_T written), a null vector
ê_T(F) = ((Λ,1)⊗F, β_T(F), 0) with 𝔾_T(ê_T(F)) = 0, an embedding ι_T : P_T → Ê_T and one of the two
readings

    (G-res)   a_T(F) = 𝔾_T(ι_T F),
    (G-Schur) a_T(F) = inf_{y ∈ 𝒴} 𝔾_T(ι_T F + y),   𝒴 ⊂ Ê_T an auxiliary subspace.

What the task asks to fix and what there is: β_T, according to R170_868 §6, comes from the first-contact
equation, which exists only for f in the radical of a window with λ_A(T) = 0. On a general F ∈ P_T
there is no first-contact equation. Its only extension to all of P_T, the
Euler–Lagrange equation of λ_A, holds only at a minimizer (pattern B9). The literal definition of R170_856
(8.7), β(F) = (b, PȦF) − (h, P𝒞F) − ρ_F g_ε, does make sense for every F as a linear functional. 
§2 proves that, within (G-res) or (G-Schur), no β_T and no null vector influences the
identity. That is why there are no new ℋ_T, V_T, ρ_T to write: the format reduces to (G) without boundary.

### (3) Does it evade the difficulty of the antecedent?

No. The difficulty of 862/870 is that the boundary class is linear and odd and positivity is even.
Within (G) everything is quadratic and parity disappears, but only because the anchor ceases to act
(Lemma 1). The difficulty of 861 and R182_201 §2 (fixed Schur = congruence) is reproduced: with 𝔾_T
manifest, (G-Schur) is (G) with explicit V_T (Lemma 3); with 𝔾_T not manifest, 𝔾_T ⪰ 0 is equivalent to the
goal (861 (1.2)).

### (4) Connection with global positivity

None new: if (G-res) or (G-Schur) hold with 𝔾_T ⪰ 0, then a_T ≥ 0 on P_T
immediately, as with (G). All the content is in writing 𝔾_T (or V_T) manifestly
positive with the exact identity. The anchor contributes no intermediate inequality (Lemma 1,
Proposition 2).

### (5) Breaking lines for cΛ and a_P

- The nullity of the anchor fails in R170_866 (2.1), row k = 2: Σ_{d|2} cΛ(d) − log 2 = (c − 1) log 2 ≠ 0;
  for a_P with P > 2, (a_P∗1)(2) − log 2 = −log 2 ≠ 0. PROVED (direct computation).
- Those breakings are not breakings of (G): by Lemma 1, ê_T can be removed from ι_T without changing the
  identity. The line that would have to break is the proof of 𝔾_T ⪰ 0 (or of ρ_T ≥ 0), which is not
  written. Moreover, for cΛ the breaking near c = 1 is automatic in the format (Lemma 4) and
  contributes no sign. Point (5) without answer: the candidate is not ready for construction.

## 1. Conventions

E is a real or complex vector space and 𝔾 a positive semidefinite Hermitian form on E,
without topological hypotheses. Write 𝔾(x) = 𝔾(x,x) and K = {k : 𝔾(k) = 0}.

## 2. Lemmas (all PROVED, with complete proof)

**Lemma 1 (invisibility of the kernel).** K is a subspace, 𝔾(x, k) = 0 for every x ∈ E and k ∈ K, and
𝔾(x + k) = 𝔾(x). Consequently, for every map ι : P_T → E (linear or not), every map
κ : P_T → K and every subspace 𝒴 ⊂ E:

    𝔾(ι F + κ F) = 𝔾(ι F),
    inf_{y∈𝒴} 𝔾(ι F + κ F + y) = inf_{y∈𝒴} 𝔾(ι F + y) = inf_{y∈𝒴+K} 𝔾(ι F + y).

*Proof.* Cauchy–Schwarz for semidefinite forms: |𝔾(x,k)|² ≤ 𝔾(x)𝔾(k) = 0. Hence
𝔾(x + k) = 𝔾(x) + 2Re 𝔾(x,k) + 𝔾(k) = 𝔾(x). K is closed under sums (𝔾(k + k′) = 𝔾(k) = 0) and under
scalars. The second line follows from the first applied to x = ιF + y. ∎

**Corollary 1.** In (G-res) and in (G-Schur), the identity holds with ι_T if and only if it holds with
ι_T − κ_T for every κ_T : P_T → K. In particular, neither the nullity of ê_T(F) nor the value of β_T(F)
enter the identity. If ι_T = ê_T + w_T, the identity is equivalent to a_T(F) = 𝔾_T(w_T F) (or to the
corresponding infimum). The induced form on Ê_T/K is the only one that matters, and in it the anchor is
the zero vector.

**Proposition 2 (the bordered format is equivalent to (G)).** Every identity (G),
a_T(F) = ‖V_T F‖² + ρ_T(F) with ρ_T(F) = Σ_j |r_j(F)|² written, is realized in (G-res) with any
β_T and with null ê_T. Conversely, every realization (G-res) with 𝔾_T = 𝓔_T*𝓔_T gives (G) with
V_T = 𝓔_T ι_T and ρ_T = 0.

*Proof.* Direct: take Ê_T = (ℝ^{N+1} ⊗ ℋ) ⊕ ℬ_T ⊕ (ℋ_T ⊕ ℓ²), 𝓔_T(x, b, h) = h (projection
onto the last summand) and ι_T(F) = ((Λ,1)⊗F, β_T(F), (V_T F, (r_j(F))_j)). Then 𝓔_T ê_T(F) = 0
and 𝔾_T(ι_T F) = ‖V_T F‖² + Σ_j |r_j(F)|² = a_T(F). The converse is the definition. ∎

Reading: requiring that (Λ,1)⊗F ⊕ β_T(F) be null does not restrict which V_T are admissible. Every V_T
admits that enlargement. It is a reformulation (patterns B3 and A4), not a mechanism.

**Lemma 3 (the Schur variant is (G) or is the goal).** Let 𝓔 = [E_X, E_Y] with E_X : X → 𝒦 and
E_Y : 𝒴 → 𝒦 linear and 𝒦 a Hilbert space, and 𝔾 = 𝓔*𝓔 on X ⊕ 𝒴. Then

    inf_{y∈𝒴} 𝔾(x + y) = ‖P^⊥ E_X x‖²,   P^⊥ = orthogonal projection onto (cl Ran E_Y)^⊥.

*Proof.* inf_y ‖E_X x + E_Y y‖² = dist(E_X x, Ran E_Y)² = dist(E_X x, cl Ran E_Y)² =
‖P^⊥E_X x‖² (projection onto a closed subspace of a Hilbert space). ∎

Thus, with 𝔾_T manifest, (G-Schur) is (G) with V_T = P^⊥E_X ι_T and ρ_T = 0. If 𝔾_T is not manifest and its
auxiliary block is G > 0, R170_861 (1.2) gives 𝔾_T ⪰ 0 ⟺ a_T ⪰ 0 (CITED, checked in primary): the
problem is transferred entirely. It coincides with R182_201 §2.

**Lemma 4 (automatic breaking under cΛ in the format linear in the weight).** Suppose that 𝔾 ⪰ 0 does not
depend on the weight, that ι_a(F) = ι_0(F) + J(a ⊗ F) with J linear, and that a_T(F; a) = 𝔾(ι_a F) holds for
every F ∈ P_T and for a = Λ + tδ with t in an open interval, where δ is supported in [2, N) and is not
zero. Then a contradiction is reached. In particular, the identity can only hold at isolated
values of c for cΛ (δ = Λ) and for Λ + s(a_P − Λ).

*Proof.* The right side is a polynomial of degree ≤ 2 in t with leading coefficient
𝔾(J(δ⊗F)). The left side is affine in t, with slope −Σ_n (2δ_n/√n) Re c_F(log n). Equality
on an interval forces 𝔾(J(δ⊗F)) = 0, that is J(δ⊗F) ∈ K. By Lemma 1 the right side then does not
depend on t, so the slope is zero for every F ∈ P_T. But the form
F ↦ Σ_n (δ_n/√n) Re c_F(log n) has symbol τ ↦ Σ_n (δ_n/√n) cos(τ log n), which is almost periodic
and non-zero on ℝ. Its values on |F̂|², with F ∈ P_T, are not all zero: by polarization it would
vanish as a sesquilinear form on P_T, and P_T has codimension two in L²(I_T), which allows
choosing F, G ∈ P_T with F̂ Ĝ‾ whose integral against the symbol is not zero. ∎

Reading: in this format, clause O4 for cΛ near 1 is satisfied for free. That «the identity
breaks under cΛ» does not, by itself, indicate any sign machinery.

Note on the last line: the step «the non-zero symbol does not vanish as a form on a subspace of
finite codimension» is used in the following elementary form. If ∫ σ F̂ Ĝ‾ = 0 for every F, G ∈ P_T,
taking F fixed and G varying in a subspace of codimension two, the function σF̂ restricted (via
inverse transform) to I_T lies in the span of e^{±t/2}. Varying F in a subspace of
dimension ≥ 3 yields σ ≡ 0 by the independence of the translations by log n, n < N. I leave it with this
wording. The part of the Lemma used below (zero leading coefficient and invisibility) is
complete; the non-vanishing argument for the slope is ARGUED in this summarized form, although the
fact is standard.

## 3. Class of the negative result

NO-GO with class (PROVED, Lemma 1, Proposition 2 and Lemma 3). Class: exact realizations of a_T on
P_T by restriction or by partial infimum of a **positive semidefinite** Hermitian form 𝔾_T on
any enlarged space, with any null vector (in particular (Λ,1)⊗F ⊕ β_T(F), with any
β_T, linear or not). In that class:

(a) the anchor and the boundary coordinate do not influence the identity;
(b) the bordered format coincides with (G);
(c) the Schur variant is (G) if 𝔾_T is manifest, and is the goal if it is not.

What the class does NOT exclude:

1. **Indefinite forms (Kreĭn).** If 𝔾_T is indefinite, a neutral vector (𝔾_T(v) = 0) is not in
   the radical and Lemma 1 fails. It is the case of the grading of R170_854 (indefinite metric) and of
   861 §4. Positivity is no longer manifest and another mechanism would be needed. Without object.
2. **Schemes by families and contradiction.** The original use of the anchor in 862 is Lemma 2.1, which
   goes from two-sided positivity to an equality at first contact. That scheme is not an identity
   (G) and remains OPEN in phase 170 (VIR–LB; 869 §5; 870 §5, odd coupling or second common
   radical). This memo does not touch it.
3. **(G) itself** with V_T constructed from exact Λ, and the non-local source factor NGF of R182_201,
   which is an instance of (G) with Schur structure (Lemma 3). Both OPEN.
4. **Null vectors that restrict 𝔾_T** when 𝔾_T is fixed in advance for other reasons (for
   example 𝔾_T built only with the comb and the ports, without Λ). Proposition 2 says that the
   nullity condition does not restrict V_T in general. It does not say that, for a given 𝔾_T, the condition
   lacks content. But then the content is the positivity of that 𝔾_T on the quotient,
   and none is known with the exact identity.

## Result

No new mechanism, plus one class NO-GO piece (PROVED). The null anchor with boundary and the
coordinate β_T are invisible in any semidefinite Gram identity, and the bordered format
is equivalent to (G). The candidate does not pass the selection gate: it cannot write (2) beyond (G)
nor (5).

## What was proved

- Lemma 1 (invisibility of the kernel) and Corollary 1: PROVED.
- Proposition 2 (the bordered format is equivalent to (G); the nullity of (Λ,1)⊗F ⊕ β_T(F) does not restrict
  V_T): PROVED.
- Lemma 3 (Schur variant = (G) with V_T = P^⊥E_Xι_T, or the goal via R170_861): PROVED, without
  closed-range hypothesis.
- Lemma 4 (in the format linear in the weight, the breaking under cΛ and under Λ + s(a_P − Λ) near the exact
  weight is automatic): leading coefficient and invisibility PROVED; the non-vanishing of the
  slope is ARGUED in the wording given.
- Breaking lines of the nullity: R170_866 (2.1) at k = 2 for cΛ (c ≠ 1) and for a_P (P > 2):
  PROVED.

## What failed and why

- β_T has no definition on all of P_T with the content of 868 §6: it comes from the first-contact
  equation, which exists only on the radical. Its natural extension, the Euler–Lagrange equation, holds
  only at the minimizer (B9).
- Even if β_T is defined on all of P_T (for example with the linear formula of R170_856 (8.7)),
  Lemma 1 makes it irrelevant in a semidefinite identity. The parity of 870 disappears for the
  same reason: there is no odd class to sign because the anchor does not act. That contributes no sign.
- The Schur variant repeats 861 and R182_201 §2.

## Concrete next step

Do not relaunch the bordered anchor as an object of (G) in the semidefinite class. If one wants to use the
zone, the two non-excluded exits have a precise statement:

(i) an indefinite Kreĭn form 𝔾_T, built with the comb and the ports, in which
(Λ,1)⊗F ⊕ β_T(F) is a neutral vector and from which a_T comes out as the restriction to a positive
subspace. One would first have to write what mechanism would give the positivity of that subspace, which
cannot be any of those of 861 §4 nor of R170_854 (3.4);

(ii) the NGF factor of R182_201 (3.1) as an instance of (G), with the admissibility written there.

Neither has a written object. Suggested annotation for the index and the grid (not made from here):
«P212-3.4: null anchor with boundary in the format (G) — NO-GO with class PROVED (invisibility of the
kernel in semidefinite forms; the bordered format is equivalent to (G)). Does not exclude: indefinite
forms, family schemes of 862, NGF».
