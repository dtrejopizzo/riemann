# Round 1, memo A — Candidate K1: Gram realization from the exact separator with Poisson and the archimedean factor

Selection memo. Target (★): λ_A(T) ≥ 0 for every T > 0, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md`. Design question: whether the exact separator
Σ_{d|n}Λ(d) = log n, used together with Poisson summation over the integers (coefficients b ≡ 1) and the
archimedean factor at conductor 1, can be converted into a Gram identity (G) of `OBJECT_SPEC.md` §1
with V_T non-linear in the exact values Λ(n), in particular via the degree-two relation
Λ·log + Λ∗Λ = μ∗log².

Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO. No computations.

**Verdict in advance: no new mechanism.** The cross-check identifies repetition in the class of
multipliers and derivation (not independence) in the class with X, J and 𝓕. By rule 3 of the brief the
memo builds no object. Recorded, with proof, are the three algebraic pieces that explain
why the degree-two relation does not produce an oriented square (§3); two of them do not appear literally
in the sources cross-checked and they are not sign results.

Notation (P47 sec:firstcontact). X = multiplication by t; V_a translation; J reflection;
𝓜 = m(D); 𝓕 = u_∞(D)J, with 𝓕² = 1, 𝓕* = 𝓕, JX = −XJ, X + 𝓕X𝓕 = 𝓜. For α: ℕ → ℂ,
Φ(α) = Σ_n α(n) n^{−1/2} V_{−log n}; S = Φ(1), L = Φ(Λ), S′ = Φ(log), S″ = Φ(log²), L′ = Φ(Λ·log),
with subscripts N, M for the truncations n ≤ N, d ≤ M. Φ(α)Φ(β) = Φ(α∗β) (untruncated) and
[X, Φ(α)] = −Φ(α·log). A = 𝓜 − L − L*; a_T(F) = ⟨F, A F⟩ for F ∈ L²(I_T) in the form domain
(only d < N = e^{2T} intervene).

---

## 0. Sources cross-checked

P47: thm:PCfinite, rem:Sren, prop:GEgap, prob:annihilate, prop:annihilate-equiv, rem:returnremarks,
prop:opcalc, thm:sos and its extension to real frequencies, rem:sosatoms, prop:cone, lem:shape-ident,
thm:noimport, rem:conjunctions, rem:spec-scope, def:ext (summation map). P48: scope note after
req:spec, codes F1–F3, row "Selberg difference channel". Phase 211: LEDGER C33, C33b, C47;
ROUND_015_B §§3.4, 4.1; ROUND_023_A Lemma 2.1; ROUND_022_A Lemma 3.1; POWER_GLOBAL_ROUTE_REVIEW §1,
"Return to (S)", "Complete Selberg", "Grouped divisorial covariance", "The divisorial remainder is
indefinite", "Factorial extension before resonance", "Control of the orthogonal substitution". Phase 188:
N_BUILD_018, N_BUILD_019, N_BUILD_022 §1. Phase 204: P1_BBSTAR_001 §§2.6–2.8. Phase 162: R162_2301
(Lemma S), R162_501, R162_502 (M_T(Λ) = ZXZ⁻¹ − X), R162_901. Index: README (NODE_001 Prop N.2 and
candidates (a)–(c); AUDIT_206_001; A_MU_FACTORIZATION_001 (e)); 04 rows G6C-R166_502, G6C-R162_501/901,
G6A-R163_802, G4A-R164_502, G6C-R166_103A; 06 (TB-3, R186_005). Grid §§ of witnesses and "Already NO-GO"
(Selberg difference channel). Crossword: row TB-3.

---

## 1. Cross-check

**(1) Closest antecedent.** There are three, and together they cover the whole question.

- Joint use, of degree one, of the three inputs: P47 thm:PCfinite,
  S_N A_M 𝓕 = {X, E_N} − L_M* E_N − J H_{M,N} − H_{M,N} 𝓕, with E_N the Poisson defect and H_{M,N} the
  incomplete divisor hyperbola; its square is invariant under A ↦ −A (code F2), and the oriented form
  that would be needed is prob:annihilate, which prop:annihilate-equiv identifies with (★). The same
  content in the image of the summation map: 211 C33/C33b ("comb on Poisson tails
  = 2⟨𝒯_log u, 𝒯u⟩"), with a ledger robust against the comb.
- Degree two in the class of multipliers: phase 204 P1_BBSTAR_001 §2.8 (PROVED): L² = Φ(Λ₂) − Φ(Λ·log);
  S_T²/4 = (Im ℓ)² + comb of (Λ₂ − Λ·log); σ_T = |1 − ℓ|² + (m − 1 − |ℓ|²); every completion of the square
  falls into the extension of thm:sos. "Selberg enters 𝒞², not 𝒞*𝒞." Same content in
  POWER_GLOBAL_ROUTE_REVIEW "Complete Selberg" (Re⟨g, B²g⟩ = ‖Bg‖² − ½‖(B − B*)g‖²) and in row
  G6C-R166_502 of the index ("Selberg acts on V² and not on V∗V"; repetition of E70_11/12).
- Genericity of Selberg-type relations: index README NODE_001 Prop N.2 (PROVED: they hold for
  every Dirichlet series; a_P, cΛ, DMV, DH satisfy them), R186_005 Thm TB3-neg (every degree),
  AUDIT_206_001 ("Selberg in the window: universal identity, log is a derivation"); operator form
  in 211 ROUND_023_A Lemma 2.1 (C47), used there in a first variation without leverage.

**(2) Really new object or claim.** None that carries a sign. No mechanism was found that
differs from the antecedents: in the class of multipliers the question is answered (P1_BBSTAR §2.8,
thm:sos, N019); outside it (operators with X, J, 𝓕) the degree-two relation is not an independent
input but the Leibniz rule applied to the degree-one one (Lemma B, §3), so the candidate
reduces to thm:PCfinite and prob:annihilate without adding anything to them. All this memo contributes are three
algebraic statements for the record (§3): mirror symmetry of the formal algebra (Lemma A), degree-two
defect derived from the degree-one one (Lemma B), and zero trace of the linearizable part (Lemma C, which is
rem:sosatoms and P1_BBSTAR §2.8 in another wording). None of them is a sign step.

**(3) Why the change would avoid the difficulty of the antecedent.** It does not avoid it. The difficulty of
thm:PCfinite is that its oriented content is in the defects E_N and H_{M,N} and only appears in bilinear
form between two distinct vectors; degree two produces the defect L_M H_{M,N} − [X, H_{M,N}]
(Lemma B), which lies in the left ideal generated by H and [X, H], vanishes exactly where the degree-one
one vanishes and contains no new oriented datum. The difficulty of P1_BBSTAR §2.8 is that Selberg
linearizes ℓ² and not |ℓ|²; that is a property of the relation, not of the way it is used (Lemma C).

**(4) Identity or inequality that would connect with global positivity.** There is no new one. The only
exact connection available is the one already recorded: thm:PCfinite solved for A,
⟨F, A_M F⟩ = ⟨(S_N^{−1})* F, [{X, E_N} − L_M* E_N − J H_{M,N} − H_{M,N} 𝓕] 𝓕 F⟩ (formal in S_N^{−1}),
bilinear in two distinct vectors and without sign. What is missing is indicated in §4.

**(5) Line that breaks for cΛ and a_P (item (5) of `OBJECT_SPEC.md` §4).** There is no identity (G) whose
line could break. One can, however, point to the identification line, which is the same in degree one and in
degree two (Lemma B): "H_{M,N} has no coefficient at k ≤ N". For weights a with δ(k) = Σ_{d|k}a(d) − log k,
the interior defect of degree one is δ(k) and that of degree two is (a∗δ)(k) + δ(k) log k. For cΛ,
δ(k) = (c − 1) log k ≠ 0 at every 2 ≤ k ≤ N; for a_P, δ(k) = −Σ_{p<P} v_p(k) log p, non-zero at k = 2
(and, if P > N, equal to −log k at every k ≤ N). In both cases the identity remains an identity,
with one more interior term; since no later step signs anything, this does not constitute the breakdown
that O4 requires. By the final clause of `OBJECT_SPEC.md` §4, **the candidate is not ready for construction.**

The cross-check identifies repetition. What follows is the record of the obstruction, requested for this memo;
it is not a construction.

---

## 2. Answer to the five known obstacles

(i) *thm:sos / N019 (pure arithmetic squares impossible for T ≥ ½log3).* In force and not evaded. The
degree-two relation lives in the algebra of multipliers; a square formed with L, L′, Φ(Λ₂), Φ(μ)
is a square of an almost-periodic polynomial and falls into the extension of thm:sos to real frequencies
(P1_BBSTAR Thm P1.A). With a free positive-definite part it is the dual class (N019 Prop 1). CITED.

(ii) *prop:opcalc / N018 (identities linear in the autocorrelation plus Bochner).* To leave the
class one has to use operators that are not multipliers: X, J, 𝓕, Q_T. That is what thm:PCfinite does.
But with respect to those operators Selberg is not a new relation: it is ad_X applied to
[X, S] = −LS (Lemma B). Every consequence of "Poisson + archimedean + Selberg" is a consequence of
"Poisson + archimedean + Λ∗1 = log + Leibniz". PROVED (Lemma B).

(iii) *prob:annihilate requires an oriented identity.* The formal algebra of the three inputs is invariant
under an involution that sends A to −A (Lemma A); hence no formal consequence is oriented, of
any degree. The orientation lies only in the way the relations fail in the realization:
h_{M,N}(k) ≥ 0 with support in k > N, and the structure of E_N. Degree two inherits h₂ = Λ∗h + h·log ≥ 0,
which is a consequence of h ≥ 0 and Λ ≥ 0, not a new datum. PROVED (Lemmas A, B); positivity of
coefficients is not positivity of a form (CITED: "The divisorial remainder is indefinite even on even
primitive tests").

(iv) *Factorial extension: D + E unsigned.* K1 contributes nothing to D + E. The factorial extension already uses the
separator in gcd form (log gcd(q, r) = Σ_{m|q, m|r} Λ(m), positive semidefinite kernel), and the remainder
contains the kernel ½(log λ + log μ), of the form u(λ) + u(μ), with exactly one positive eigenvalue and
one negative. Degree two offers the rank-one kernel log λ · log μ, which is positive semidefinite and
can only pay one of the two signs:
u(λ) + u(μ) = (1/2ε)(1 + εu(λ))(1 + εu(μ)) − 1/(2ε) − (ε/2)u(λ)u(μ). The signature (1,1) does not change.
PROVED (elementary identity); it is not an exclusion of the joint compensation of D + E.

(v) *C33b (ledger of Λ∗1 = log robust against the comb).* In force. The degree-two ledger is
obtained from the degree-one one by derivation in the scale (Lemma B), and derivation preserves robustness:
if the degree-one one survives cΛ, c < 1, and a_P, so does the degree-two one, with the same first failure
index of the identification. ARGUED (the PROVED part is Lemma B; the ledger was not redone).

---

## 3. The algebraic obstruction, recorded

### Lemma A (mirror symmetry of the formal algebra; PROVED)

Let 𝔸 be an associative algebra with unit and elements X, J, 𝓕, S, L such that: J² = 𝓕² = 1; JX = −XJ;
S and L belong to a commutative subalgebra 𝒯 stable under t ↦ t^♭ := JtJ; S is invertible in 𝒯; and

    (a) 𝓜 := X + 𝓕X𝓕 satisfies J𝓜J = 𝓜;   (b) S𝓕 = JS;   (c) [X, S] = −LS.

Then: (1) 𝓜 = L + L^♭, that is A := 𝓜 − L − L^♭ = 0. (2) The substitution
X ↦ X, J ↦ J, 𝓕 ↦ 𝓕° := J𝓕J, S ↦ S⁻¹, L ↦ −L preserves all the hypotheses and sends 𝓜 ↦ −𝓜, A ↦ −A.

*Proof.* (1) From 𝓕² = 1, 𝓜𝓕 = X𝓕 + 𝓕X. From (c), SX = XS + LS. Then, with (b), JX = −XJ and
JL = L^♭J,

    S𝓜𝓕 = SX𝓕 + S𝓕X = (XS + LS)𝓕 + JSX = XJS + LS𝓕 + J(XS + LS)
         = XJS + LS𝓕 − XJS + L^♭JS = (L + L^♭)S𝓕.

Since 𝒯 is commutative, S(𝓜 − L − L^♭)𝓕 = 0, and S, 𝓕 are invertible.
(2) (𝓕°)² = 1. For (c): [X, S⁻¹] = −S⁻¹[X, S]S⁻¹ = S⁻¹LSS⁻¹ = LS⁻¹ = −(−L)S⁻¹. For (b): from (b),
𝓕 = S⁻¹JS, hence 𝓕° = (JS⁻¹J)·S·J = (S^♭)⁻¹SJ and S⁻¹𝓕° = (S^♭)⁻¹J = JS⁻¹JJ = JS⁻¹. For (a):
X + 𝓕°X𝓕° = X + J𝓕(JXJ)𝓕J = X − J𝓕X𝓕J = X − J(𝓜 − X)J = X − 𝓜 − X = −𝓜, and J(−𝓜)J = −𝓜. Finally
−𝓜 − (−L) − (−L)^♭ = −A. ∎

*Reading.* In the realization, (a) is exact (L^♭ = L*); (b) is Poisson for b ≡ 1 and (c) is Λ∗1 = log,
both valid only with defects (E_N; H_{M,N}); (1) with defects is thm:PCfinite (CITED). The mirror
image is the system (Möbius comb, weights −Λ, inverse archimedean factor). Consequence: every
identity deduced formally from (a), (b), (c) —in particular every one that uses the degree-two relation,
which is a consequence of (c) by Lemma B— has a twin with A changed in sign; an identity
"A = Σ V_i*V_i + ρ" obtained in this way would have a twin "−A = Σ V°_i*V°_i + ρ°", and both only say A = 0, which
is (1). **The formal algebra of the three inputs contains no orientation, in any degree.** The
orientation enters exclusively through the asymmetry of the defects between the system and its image: for the
integer comb, h_{M,N} ≥ 0 with support outside [1, N] and E_∞ is of rank two (polar terms) on the
Schwartz core; for the Möbius comb neither of the two holds. This sharpens condition
(ii) of prob:annihilate and code F2 of P48; it does not go beyond them. Statement (2) was not located literally in
the sources cross-checked; nothing more than that is claimed.

### Lemma B (the degree-two defect is derived; PROVED)

For arbitrary weights a (instead of Λ), M, N ≥ 1, let L_M = Φ_{≤M}(a), L′_M = Φ_{≤M}(a·log),
H_{M,N} = L_M S_N − S′_N and H⁽²⁾_{M,N} := (L′_M + L_M²) S_N − S″_N. Then, on the Schwartz core,

    H⁽²⁾_{M,N} = L_M H_{M,N} − [X, H_{M,N}].

Untruncated, with h = a∗1 − log and h₂ = (a·log + a∗a)∗1 − log²: h₂ = a∗h + h·log.

*Proof.* [X, L_M] = −L′_M, [X, S_N] = −S′_N, [X, S′_N] = −S″_N. Hence
[X, H_{M,N}] = −L′_M S_N − L_M S′_N + S″_N = −L′_M S_N − L_M(L_M S_N − H_{M,N}) + S″_N
= −H⁽²⁾_{M,N} + L_M H_{M,N}. The version in coefficients: log·(a∗1) = (a·log)∗1 + a∗log, whence
h·log = (a·log)∗1 + a∗log − log², and a∗h = a∗a∗1 − a∗log; add. ∎

*Consequences (PROVED).* (1) For a = Λ and M ≥ N, H has no coefficients at k ≤ N (thm:PCfinite), and
then neither does H⁽²⁾: L_M H has coefficients at proper multiples of indices > N, and [X, ·] preserves the
support. The degree-two relation "at k ≤ N" is the degree-one one. (2) For weights a with a(1) = 0, if k₀ is
the first index with δ(k₀) ≠ 0, the degree-two defect at k₀ is δ(k₀) log k₀: both degrees fail on the
same line and at the same index. The degree-two relation separates nothing that the degree-one one does not separate
(it coincides with R162_2301 Lemma S: Selberg ⟺ a = Λ, by recursion). (3) If h ≥ 0 and a ≥ 0 then
h₂ ≥ 0: the only oriented datum of degree two is a consequence of that of degree one. (4) By iteration, the
same holds in every degree: the defect of degree j lies in the left ideal generated by
H, [X, H], …, ad_X^{j−1}(H).

### Lemma C (the linearizable part has zero trace; PROVED, with CITED for the isolation of atoms)

Let T > ½ log 3 and L = Φ_{<N}(Λ) the comb in the window. Let V_i = α_i + β_i L + γ_i L*, i ≤ r, with
α_i, β_i, γ_i ∈ ℂ. If the form Σ_i ‖V_i F‖² coincides on P_T with ∫ Re c_F dν for a finite measure ν
on (−2T, 2T) with atoms only in {0} ∪ ±log ℕ, then β_i = γ_i = 0 for every i.

*Proof.* V_i*V_i = |α_i|² + (ᾱ_iβ_i + γ̄_iα_i)L + (ᾱ_iγ_i + β̄_iα_i)L* + (|β_i|² + |γ_i|²)L*L
+ β̄_iγ_i L*² + γ̄_iβ_i L². The atoms of L, L* are at ±log of prime powers; those of L², L*² at
±log(mn) with m, n ≥ 2, of modulus ≥ log 4; L*L = Σ Λ(m)Λ(n)(mn)^{−1/2}V_{log n − log m}. The point
log(3/2) ∈ (0, 2T) is not ±log of an integer and 3/2 = n/m with n, m prime powers only for
n = 3, m = 2 (2n = 3m forces n = 3k, m = 2k, and k = 1). Hence the atom of Σ_i V_i*V_i at log(3/2) is
(log 2 · log 3/√6) Σ_i(|β_i|² + |γ_i|²). Two measures that define the same form on P_T have the
same atoms in (0, 2T) (CITED: isolation argument of rem:sosatoms). Hence the sum is zero. ∎

*Reading.* In the variables x = Re ℓ, y = Im ℓ of the symbol ℓ of L, a sum of squares of degree one
has positive semidefinite quadratic part; the quadratic forms with integer atoms —those that the
degree-two relation linearizes, Re ℓ² = x² − y² and Im ℓ² = 2xy, through L² = Φ(Λ₂) − L′ modulo atoms
≥ 2T— are those of zero trace. Positive semidefinite and zero trace implies zero. The degree-two relation
is an identity of the ring of the semigroup log ℕ, without involution; positivity needs the involution,
which takes one out of the semigroup into log ℚ_{>0}. It is rem:sosatoms and P1_BBSTAR §2.8 in trace wording; it is recorded
because it answers literally the question "what prevents a Selberg-type relation from giving a square
with the right orientation" in this class. For higher degree in (L, L*, L′, …) no separate lemma is
needed: the extension of thm:sos covers every almost-periodic polynomial (CITED).

### Remark D (order in the derivation; ARGUED)

The separator makes Λ enter through the derivation ad_X: L = −[X, S]S⁻¹, that is X + L = SXS⁻¹
(CITED: R162_502, N_BUILD_022 §1). The comb of a_T is of first order in ad_X; the squares formed
with X and S are of order zero or two. For example, for G in the natural domain,
‖(X + L)G‖² − ‖XG‖² − ‖LG‖² = 2Re⟨XG, (Re L)G⟩ − Re⟨G, L′G⟩ (PROVED: XL + L*X = {X, Re L} − ½(L′ + L′*)),
which produces the comb of Λ·log, not that of Λ. Lowering one order requires integrating in the scale, which leads to
the weights Λ/log (homogeneous cone of O10, which cΛ preserves) and to the separate divergence of the two pieces
recorded in "Complete Selberg" (CITED). The degree-two relation is the second-order Leibniz rule
and gives convexity-type information in the scale, closed family "transport in σ"
(RULES_AVOID §C). It is not presented as a theorem.

---

## 4. The missing piece, stated precisely

By Lemmas A and B, an object of type K1 can only obtain orientation from the two facts that the
mirror image does not share: (α) h_{M,N}(k) ≥ 0, with support in k > N; (β) the form of E_N. A datum of
non-negative coefficients only signs a form if it is paired with non-negative functions. The missing
piece is then an identity of the type

    a_T(F) = ‖V_T F‖² + Σ_{k>N} h_{M,N}(k) |ℓ_k(F)|² + (polar terms written as squares),

with ℓ_k explicit linear functionals of F (OPEN; none was found). In thm:PCfinite the
terms of H appear as ⟨Y, V_{−log k} 𝓕F⟩ with Y = (S_N^{−1})*F ≠ 𝓕F: pairings between two
distinct vectors, not squared moduli. Making them diagonal is exactly what
conditions (ii)–(iii) of prob:annihilate ask for; it is not a new target, and prop:annihilate-equiv
identifies it with (★). It is not proposed as a candidate: the operation is missing.

---

## 5. Falsifier battery

There is no sign step to submit to the battery. For the relations used: cΛ (c ≠ 1) and a_P break (c)
at the first index (§1 (5)), in degree one and two alike; finite deletion and amplification break (c)
at the first modified index and at its multiples; Davenport–Heilbronn and Epstein have no weights of
logarithmic-derivative type supported on prime powers, so (c) does not arise with b ≡ 1;
a Beurling system satisfies (c) in its own semigroup and loses (b); b_θ breaks (c). For the quartet models
and f_t, which preserve Λ(n) in the window and the functional equation, the three relations
(a), (b), (c) still hold in the window and do not separate them: consistent with no consequence
of them carrying a sign (Lemma A) and with P47 cor:shape (a). This last sentence is ARGUED: it was not verified
against the definitions of those models in P47 beyond what `RULES_AVOID.md` §E summarizes.

---

## Result

**No new mechanism.** K1, as posed (exact separator + Poisson with b ≡ 1 + archimedean
factor, with non-linearity supplied by the degree-two relation), repeats: P47 thm:PCfinite /
prob:annihilate in the class with X, J, 𝓕; P1_BBSTAR_001 §2.8, thm:sos and N019 in the class of
multipliers; NODE_001 Prop N.2 and TB3-neg as regards genericity. (ℋ_T, V_T, ρ_T) is not written. It is
not a NO-GO of the conjunction (E)∧(F)∧(I) with a non-linear step, which still has no common falsifier
(rem:conjunctions): what is discarded is that the degree-two relation is that step.

## What was proved

- Lemma A (PROVED): the relations (a), (b), (c) imply A = 0 and are invariant under an involution
  that changes A into −A; the formal algebra has no orientation in any degree.
- Lemma B (PROVED): H⁽²⁾ = L_M H − [X, H] for arbitrary weights and truncations; h₂ = a∗h + h·log; the
  degree two fails on the same line and index as degree one and its coefficient positivity is
  inherited.
- Lemma C (PROVED, isolation of atoms CITED): a sum of squares of degree one in (L, L*) with
  integer atoms is constant, T > ½ log 3; the part that Selberg linearizes has zero trace.
- Signature identity of the kernel u(λ) + u(μ) versus the rank-one kernel (PROVED, elementary).

## What failed and why

- Completion of the square with L: generates |ℓ|², with atoms at log(p/q); Selberg only knows ℓ². The
  identity "Σ|V_i|² has integer atoms" fails, because of the atom (log 2 · log 3/√6) Σ(|β_i|² + |γ_i|²) at
  log(3/2).
- Squares with X and S: they are of order zero or two in ad_X and produce the comb of Λ·log; the comb of Λ is of
  order one.
- Use of degree two in the Poisson–Chebyshev identity: it adds no relation (Lemma B) nor orientation
  (Lemma A).
- No identity was obtained that converts h_{M,N} ≥ 0 into a sum of squared moduli.

## Next concrete step

Do not relaunch K1 with another relation of the Dirichlet ring (degree three, Vaughan, convolution
identities): Lemma B derives them from (c) and Lemma A removes their orientation. A reopening requires
an explicit operation that diagonalizes the pairings of H_{M,N} and E_N of thm:PCfinite (the ℓ_k of
§4) and the four points of the filter. Proposed lines for the records (this memo does not
edit other files):

- Phase LEDGER, K1: "NO NEW MECHANISM — degree two = Leibniz of Λ∗1 = log (Lemma B); formal
  algebra without orientation (Lemma A); zero trace (Lemma C); the diagonalization of H_{M,N}, E_N is missing".
- Routes index and grid: "Degree-two (and higher) relation of the Dirichlet ring as a non-linear
  step of the conjunction separator + Poisson + archimedean: repetition of thm:PCfinite /
  P1_BBSTAR §2.8 / Prop N.2; Lemmas A, B, C PROVED in ROUND_001_A of phase 212; not a NO-GO of the
  conjunction".
