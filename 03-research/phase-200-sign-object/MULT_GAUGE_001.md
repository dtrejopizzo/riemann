# MULT_GAUGE_001 — the multiplicative gauge of the window form (phase 200, round 26a)

**Summary (≤150 words).** Let 𝔐_T be the set of weights η that leave T.1 invariant, i.e. Σ_ρ |ĝ(γ)|²(η(γ)−1) = 0 for
every even g in the level-T core with A(g)=0. There are two results. **Thm M.1 (PROVED):** if η equals 1 at every
ordinate (sufficient condition), then η ∈ 𝔐_T. **Thm M.2 (PROVED):** on the union core (all T), 𝔐 = {η : η_even(γ) = 1
at every ordinate γ}. For fixed T, 𝔐_T is strictly larger (ARGUED, by the Mitkovski–Poltoratski gap theorem), but
only via sequences over the zero set. This gives cases: |D_μ|², |ζP−1|², |1−ζQ|² ∈ 𝔐 and |ζ|²(…) ∉ 𝔐. **R-MOM becomes
a class theorem (PROVED):** the value does not depend on η ∈ 𝔐, so any moment evaluation that computes it correctly
returns W_T(g). The additive gauge 𝒢̄_T and the multiplicative one 𝔐 are two faces of the same statement, "the mass
is at the zeros". Together they generate no new structure (REF-D). **NO-GO** as a route. L′♯ remains OPEN.

## 0. Index check (05-meta-and-planning/ROUTES-TRIED-INDEX/README.md)

- "gauge", "radical", "A.1": l.518 (SPEC_003, Lemma A.1, exterior-summation radical = gauge 𝒢_T) and l.524–525
  (PI_MU_001 and its audit: 𝒢̄_T = Q𝓕(L²₀[−1/λ,1/λ]), annihilator 𝒦_T). Both entries describe the **additive**
  gauge, in the test. None treats multiplicative weights on the symbol.
- "Lemma R", "SQ.0", "mollifier", "P9′": l.515–517 (SPEC_002 T.1; AUDIT_SPEC_002 SQ.0 and P9′; Q2_LADDER Lemma R).
- "R-MOM", "MOMENTS", "D_μ": l.565 (MOMENTS_001; R-MOM PROVED, but only for Conrey's and Motohashi's concrete moment
  weights). Also l.488 and l.501 (phase 199, D_μ as a mollifier).
- "Π_μ": l.524.
- New reason: MOMENTS_001 §9 leaves open the characterization of the complete set of multipliers, and no entry
  contains it. This round retries no construction. Its goal is to turn R-MOM into a class statement and close the
  "weights on the symbol" family.

## 1. Setup

By T.1 (SPEC_002 l.44, PROVED given Guo L4.3–4.4) and by F4, for even g in the core on (−a,a), a = T, with A(g) = 0:

  W_T(g) = (1/2π)·⟨σ, |ĝ|²·|D_μ|²⟩ = (1/2π)·⟨σ, |ĝ|²⟩,  σ = Σ_ρ m_ρ δ_{γ_ρ} (+ poles).

The poles vanish because A(g) = 0. I write γ for the ordinate of the zero ρ = ½+iγ, in the case where every zero of
the family is on the line. The case with off-line zeros is treated in §4. Define

  𝔐_T := {η : ℝ → ℂ measurable, of polynomial growth : Σ_ρ m_ρ |ĝ(γ_ρ)|² (η(γ_ρ) − 1) = 0  ∀ g ∈ core_T, A(g)=0}.

The series converges absolutely: if g ∈ C_c^∞, then ĝ decays faster than any polynomial, and N(T) ≪ T log T.
𝔐 := ∩_T 𝔐_T is the union core's gauge.

## 2. Multiplicative gauge theorem

**Thm M.1 (sufficiency; PROVED).** If η(γ) = 1 at every ordinate γ, then η ∈ 𝔐_T for every T.
*Proof.* Each term's summand is |ĝ(γ)|²·0. ∎

**Thm M.2 (characterization on the union core; PROVED, given T.1).** η ∈ 𝔐 ⟺ η(γ) + η(−γ) = 2 at every ordinate γ. If
η is even (the case for every weight of the form |E(½+it)|² with E real-coefficient), the condition is η(γ) = 1.

*Proof.* (⇐) Since g is even, |ĝ|² is even, and σ is symmetric (γ ↦ −γ). Then the term at γ and the term at −γ add to
|ĝ(γ)|²(η(γ)+η(−γ)−2) = 0.

(⇒) Let η ∈ 𝔐 and let η_s(γ) := ½(η(γ)+η(−γ)) − 1. The condition is Σ m_ρ|ĝ(γ)|²η_s(γ) = 0. Polarize over the real
space of even g with A(g)=0 (it is linear and the condition is real quadratic). For all pairs g₁, g₂ one obtains
Σ m_ρ Re(ĝ₁ conj ĝ₂)(γ) η_s(γ) = 0. For real even g, ĝ is real, so Σ m_ρ ĝ₁(γ)ĝ₂(γ)η_s(γ) = 0.

Fix g₂ and define c_ρ := m_ρ ĝ₂(γ)η_s(γ), which has polynomial growth. The tempered distribution
S := Σ_ρ c_ρ cos(γx) satisfies ⟨S, g₁⟩ = 0 for every even g₁ of arbitrary compact support (union core), with
A(g₁)=0. The condition A(g₁) = 0 is a single linear functional, ∫g₁ cosh(x/2) (since g₁ is even). Hence
S = κ·cosh(x/2) as a distribution over even functions. S is tempered and cosh(x/2) is not, so κ = 0 and S = 0. Its
Fourier transform is the measure Σ c_ρ(δ_γ+δ_{−γ})/2, of discrete support, and it is null. Hence c_ρ = 0 for every ρ.

Given γ₀, choose g₂ even, of compact support, with A(g₂)=0 and ĝ₂(γ₀) ≠ 0. Such a g₂ exists: the space of these
functions has codimension 1 in even C_c^∞, and the functionals g ↦ ĝ(γ₀) and g ↦ A(g) are linearly independent
because γ₀ is real and cosh(x/2) ≠ cos(γ₀x). One concludes η_s(γ₀) = 0. ∎

**Prop M.3 (fixed T; ARGUED).** 𝔐_T ⊋ 𝔐. The same computation reduces the condition to: the measure ν = Σ m_ρ
η_s(γ)δ_{±γ} has a transform equal to κ·cosh on (−2a, 2a), since products ĝ₁ĝ₂ are dense in even PW_{2a}. The
density of ordinates on [R, R+1] is ~(log R)/2π → ∞. By the Mitkovski–Poltoratski gap theorem (CITED, Adv. Math. 224
(2010)), the zero set supports nonzero measures with a spectral gap of any finite length. Hence there exist η_s ≢ 0
over the zeros with η ∈ 𝔐_T. One point remains unclosed, which is what leaves this at ARGUED: reconciling the
polynomial growth with the mass m_ρ. In any case, the extra elements of 𝔐_T are **sequences indexed by the zero set,
with a spectral gap**. They are defined by zero data, not by arithmetic on the ℕ side.

This answers the separation question from MOMENTS §9. A.3 is not needed (SPEC_003 l.54, OPEN). Individual
separation of each zero holds on the union core and fails, in general, at fixed T.

**Cases.**
- η = |D_μ|² = |ζM_μ − 1|²: D_μ(ρ) = −1, so η(γ) = 1 ✓. This is MOMENTS_001's Prop 3.2.
- η = |ζP − 1|² with P a finite Dirichlet polynomial: ζ(ρ)=0 gives η = 1 ✓. This is the pointwise version of Lemma R
  (Q2_LADDER l.49). Lemma R says more, since it asserts radicality of the test, not just invariance of the value.
- η = |1 − ζQ|², with Q any function holomorphic in the strip ✓. Same for η = |1 + ζF|²·|1 + ζG|², and for every
  η = 1 + ζ·H with H continuous on the line: the set is an affine ideal, 1 + (ideal of functions vanishing at the
  zeros).
- η = |ζ|²·K: η(γ) = 0 ≠ 1 ✗, unless K has poles at the zeros. For example, η = |ζ/ζ|² ≡ 1 is trivial.
- η = |ζ|^{2k}, k ≥ 1: ✗. That is why an unmollified moment of ζ changes the value (it is a different form), while a
  mollified one of type |ζM−1|² does not.

**§2 label:** M.1 and M.2 PROVED (M.2 given T.1, which in turn is given Guo L4.3–4.4). M.3 ARGUED.

## 3. R-MOM as a class theorem (PROVED)

**Thm R-MOM.** Let η ∈ 𝔐_T (in particular, any η = |1 + ζH|²) and let I_η(g) := (1/2π)⟨σ, |ĝ|²η⟩. Then
I_η(g) = W_T(g). Moreover, every decomposition I_η = Σ_j I_j evaluated piece by piece (with moments, asymptotics or
exact formulas of Conrey, Motohashi or Estermann, on the line) satisfies: if the evaluation is correct, the sum of
the pieces is W_T(g). Every arithmetic constant depending on η (a_2, c(θ,P), M_μ's coefficients, auxiliary
L-function values) enters with net coefficient 0.

*Proof.* I_η − W_T = (1/2π)⟨σ, |ĝ|²(η−1)⟩ = 0 by 𝔐_T's definition, and by M.1 for η ≡ 1 at the zeros. A correct
evaluation of each I_j gives a number whose sum is I_η. Hence Σ_j I_j = W_T. Let c be a constant appearing in I_j
that is not determined by g and T (it is a parameter of η: η = η_c). Then dI_η/dc = 0 for every c, because
I_{η_c} = W_T is independent of c. ∎

*Corollary.* Every family of weights {η_c} ⊂ 𝔐 carries no information about the sign of W_T, beyond W_T itself.
This covers at once MOMENTS_001's Cor 3.3, DH_TRANSFER §6, and any future mollifier (Levinson, Feng, BCY, of
arbitrary length). **Do not retry: any weight of type |1 + ζH|² in the window formula.**

## 4. What it teaches; falsifiers

**4.1 The two invariances.** There are two invariances of the window form.
- The additive one, in the test: g ↦ g + r with r ∈ 𝒢̄_T. Equivalent to ĝ ↦ ĝ + r̂, with r̂ vanishing at the zeros at
  the level of the form (Lemma A.1, Π.0).
- The multiplicative one, in the symbol: |ĝ|² ↦ |ĝ|²η with η ∈ 𝔐.

Both are the same fact, supp σ ⊂ {zeros}, read in two places. W_T's dual is the measure σ, and a form on the tests
only sees |ĝ|² restricted to supp σ. The additive one changes the factor ĝ for something with the same restriction.
The multiplicative one changes the weight for something equal to 1 on the restriction. Together they generate the
transformation group G = {|ĝ|² ↦ F : F|_{zeros} = |ĝ|²|_{zeros}} (on the union core). Its only complete invariant is
the sequence (|ĝ(γ)|²)_γ evaluated against σ, i.e. the form itself written on the zero side. **They generate no new
structure: it is REF-D (PROVED as the statement that G-invariance ⟺ factoring through the restriction to supp σ).**
Any positivity proved "modulo G" is a positivity of Σ m_ρ|ĝ(γ)|². That is the form itself, or the statement that
every γ is real, not an intermediate lemma. For an object to contribute something it must act outside G, changing
the test's class modulo the radical (P9′/P10, l.516), as MOMENTS §9 already said.

**4.2 DH / Epstein.** For DH, Epstein and L with off-line zeros, σ is no longer a measure on ℝ. It is the functional
h ↦ Σ_ρ m_ρ h(γ_ρ) with γ_ρ ∈ ℂ, and the form (Paper 46's rem:ext-killing(iii)) is Σ_ρ Φ(ρ)Φ(1−ρ), not Σ|ĝ(γ)|².
The multiplicative gauge only makes sense for η that analytically continue to the strip: η^{an}(s) = E(s)E^*(1−s),
with E^*(s) := conj E(s̄), which on the line is |E(½+it)|². The condition is η^{an}(ρ) = 1 at every zero ρ of F_DH or
Z_Q, including those off the line. In the product, η^{an}(ρ) = E(ρ)·conj E(1−ρ̄). Hence **1−ρ̄ does enter**, which is
a zero because the FE and the real coefficients give symmetry under ρ ↦ 1−ρ̄. For E = 1+ζ_{DH}H, E(ρ) = E(1−ρ̄) = 1 ✓,
and M.1 still holds. In M.2 the Fourier proof uses complex frequencies: S = Σ c_ρ cosh-exponentials, with c_ρ
e^{±iγx} and γ ∉ ℝ, which is likewise not tempered. Uniqueness becomes uniqueness of generalized Dirichlet series,
which holds (ARGUED) as long as the series converges, which requires decay of ĝ in the strip (which holds for
g ∈ C_c^∞). **Nothing changes structurally.** The multiplicative gauge does not distinguish ζ from DH: it is
"η^{an} ≡ 1 at the zeros", with no hypothesis on their position. That is why it cannot carry a sign (explicit
falsifier: DH has 𝔐^{DH} with the same form and W_T^{DH} < 0 on known tests, CERT_DH_001).

## 5. Labels

| statement | label |
|---|---|
| M.1 (η ≡ 1 at zeros ⟹ invariance) | PROVED |
| M.2 (𝔐 = {η_even ≡ 1 at zeros}, union core) | PROVED given T.1 (Guo L4.3–4.4) |
| M.3 (𝔐_T ⊋ 𝔐 at fixed T, extras = gapped measures over the zeros) | ARGUED (+ CITED Mitkovski–Poltoratski) |
| R-MOM, class version | PROVED given T.1 |
| G = additive + multiplicative gauge = restriction to supp σ; REF-D | PROVED |
| DH/Epstein: condition η^{an}(ρ)=1, includes 1−ρ̄; no structural change | M.1 PROVED; M.2 ARGUED |
| Route "weights on the symbol" | **NO-GO** |
| L′♯ / row D | OPEN |

## 6. Entry for the index

> - **MULT_GAUGE_001 (phase 200, round 26a): multiplicative gauge; NO-GO as a route.** M.1/M.2 PROVED (given T.1): on
>   the union core, η leaves T.1 invariant ⟺ η_even(γ)=1 at every ordinate (Fourier uniqueness of Σc_ρcos γx ∝
>   cosh x/2 ⇒ 0); at fixed T, 𝔐_T is larger (ARGUED, Mitkovski–Poltoratski gap; extras = measures over zeros).
>   R-MOM is a class theorem: every weight |1+ζH|² (mollifiers of any length) gives W_T with net-coefficient-0
>   constants. Additive gauge 𝒢̄_T + multiplicative = restriction to supp σ: REF-D. DH: condition η^{an}(ρ)=1 (with
>   1−ρ̄), same gauge, no sign. **Do not retry: multiplicative weights on T.1's symbol.**

## 7. Next lemma

There is no lemma within this family. The only route compatible with §4.1 is an operator on the test that does
**not** preserve the restriction |ĝ|²|_{zeros}. It must be reformulated as a condition over ℕ, without reference to
zeros: characterize the operators L on the core such that W_T(Lg) − W_T(g) can be written as an explicit sum in Λ
with sign (P9′/P10, l.516). Its index check is left pending for round 27.
