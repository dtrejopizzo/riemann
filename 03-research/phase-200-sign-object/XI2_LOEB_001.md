# XI2_LOEB_001 — Lemma Ξ2.1 (Loeb form over Ẑ) and closure of the Łoś dichotomy Φ.13

Phase 200, round 16. Pure mathematics, no numerics.
ARGUED / OPEN / NO-GO.

**Summary.** Ξ2.1 is NO-GO and Φ.13 becomes PROVED, in a stronger version than the spec's. The reason is
structural. In the ultrapower ∗ℝ = ℝ^ℕ/𝒰 every internal object is, by definition, a class [x_μ] of standard
objects. This includes ∗μ, ∗N = ∗μ!, the divisors of ∗N, counting measure and any normalization ν. By Łoś, every
assertion "st(∗𝒲/ν) ≥ 0" is equivalent to a standard family of inequalities 𝒲_μ ≥ −ε ν_μ, with ν_μ standard for
𝒰-almost every μ. There is no "internal nonstandard normalization" that is not a disguised standard sequence:
Φ.13's gap is empty. Normalizing by divisors of ∗μ! does nothing to the support of the window, because every
N ≤ ∗μ divides ∗μ!. Nor does ν ≍ ℓ: ν does not vanish on the gauge, while ℓ does. Normalizations by d(∗N) or by
Ẑ's Haar measure are scalars independent of the test, so they only rescale and fall into (b2). There is a single
Λ channel, and it passes through 𝒲_μ. Ẑ is decorative: the object exists equally for Beurling, a_P and Epstein,
and that is why it fails (F9). **Ξ2: NO-GO. Φ.13: PROVED.**

## 0. Corpus and index

Prior reading: SPEC_SIGN_OBJECT_006 §B (Φ.13, l. 211–217), §C row 3 and §D Ξ2 (l. 352–380); K3_GAMMA_001 §1–2
(Γ-limit renormalized by leakage, comb-generic); PI_MU_001 (𝒬_μ = L²/𝒢̄_T with norm ℓ/2); Paper 46
prop:ext-gauge (ℓ(g) = 2 dist²(r_f, 𝒢̄_T), gauge = radical of 𝒲, given Guo L4.4 CITED); K1_OSG_001 l. 15
(exterior datum c_N, FF.0).

Greps in `05-meta-and-planning/ROUTES-TRIED-INDEX/`:
- "Loeb", "ultraprod", "Ẑ" and "Łoś": a single entry each, always README l. 545 (SPEC_006 itself, which opens
  the gap).
- "∗μ": one entry, l. 487 (PROOF_L_SHARP_FF_001). Uses ∗μ as notation, not as an ultrapower.
- "nonstandard", "profinite" and "hyperfinite": 0.
- Nearby entry: l. 278, front I (Γ-convergence dead), which K3 already reopened with a new reason and closed
  again.

**New reason for trying it.** The normalization ν by divisors of ∗μ! is not K3's leakage, and in Φ.13 it was the
only case marked ARGUED. K3 is not retried here. The case K3 did not cover is decided here.

## 1. Rigorous definitions

**1.1 Ultrapower.** 𝒰 is a nonprincipal ultrafilter on ℕ. ∗X := X^ℕ/𝒰. A set or function is *internal* if it is
[A_n] with A_n standard (CITED: Łoś; Goldblatt, *Lectures on the Hyperreals*, ch. 11). ∗μ := [μ_n] with
μ_n → ∞, which is unlimited. ∗N := ∗μ! = [μ_n!].

**1.2 Window data.** For each standard μ there are T_μ = ½log μ, the admissible kernel 𝒞_μ (tests f with
g = Ef) and the Weil form of the declared carrier 𝒲_μ(g), with radical ⊇ 𝒢̄_T (prop:ext-gauge). Take the
leakage ℓ_μ(g) = 2 dist²(r_f, 𝒢̄_T) and λ_A(T;a) = inf{𝔞_T(g) : g ∈ P_T, ‖g‖ = 1}. The internal form is
∗𝒲 := [𝒲_{μ_n}] on ∗𝒞 := ∏𝒞_{μ_n}/𝒰.

**1.3 Hyperfinite space and measure.** Ω := {1,…,∗N} ≅ ℤ/∗Nℤ, internal and hyperfinite. The normalized counting
measure is P(A) = |A|/∗N, and L_P is its Loeb measure. The map π: ℤ/∗Nℤ → Ẑ = lim ℤ/m is well defined because
m | ∗N for every standard m. Moreover π_∗L_P = Haar_Ẑ (CITED: Loeb 1975; the cylinder-by-cylinder computation
is immediate, because P(x ≡ a mod m) = 1/m exactly).

**1.4 Ξ2 normalization.** There are two readings of the spec:
- (ν-i) c_N = c_N(x) are the test's translation coefficients, Ψ̌_c = Σ c_N N^{−½}τ_{log N}g:
  ν(x) := Σ_{N≤∗N, N|∗N} c_N(x)²/N.
- (ν-e) c_N is the fixed exterior datum FF.0, c_N = Σ_{m|N, m<μ} μ(m) (K1_OSG l. 15), and then ν does not depend
  on x.

The functional is 𝔏(x) := st(∗𝒲(x)/ν(x)) for ν(x) ≠ 0 finite-non-infinitesimal relative.

**1.5 Lemma Ξ2.1 (exact statement).** *There exist standard constants 0 < c ≤ C such that, for 𝒰-almost every μ
and every g ∈ 𝒞_μ, c·ℓ_μ(g) ≤ ν_μ(g) ≤ C·ℓ_μ(g).* The upper bound is what transfers 𝔏 ≥ 0 to the ℓ scale of
L′♯.

## 2. Results

**Lemma 2.1 (Łoś reduction; PROVED).** Let ν = [ν_{μ_n}] be any internal normalization. Then:

  𝔏 ≥ 0 on ∗𝒞  ⟺  ∀ε ∈ ℚ_{>0}: {n : 𝒲_{μ_n}(g) ≥ −ε ν_{μ_n}(g) ∀g ∈ 𝒞_{μ_n}} ∈ 𝒰.

*Proof.* If x = [x_n] and st(∗𝒲(x)/ν(x)) ≥ 0, then ∗𝒲(x) ≥ −εν(x) for every standard ε. For "⟹" proceed by
contrapositive. If for some ε the set on the right is not in 𝒰, its complement is. Choose witnesses x_n with
𝒲 < −εν (coordinate-by-coordinate choice), and x = [x_n] satisfies 𝔏(x) ≤ −ε. For "⟸" use Łoś coordinate by
coordinate. ∎

What the lemma shows: ∗μ!, the divisors and Ẑ only enter through the standard sequence ν_μ. There is no third
type of functional. A ν "nonstandard via ∗μ(∗N)" is, by the definition of the ultrapower, the sequence
n ↦ ν_{μ_n} computed with μ_n!.

**Lemma 2.2 (the divisibility filter is trivial in the window; PROVED).** If supp c ⊂ [1, X_μ] with X_μ ≤ μ, the
filter N | μ! excludes nothing. If X_μ = μ^A, it excludes only the N with a prime factor p > μ or with
v_p(N) > v_p(μ!), and that set is determined by the index, not by the comb.
*Proof.* Every N ≤ μ divides μ!. In general N | μ! ⟺ v_p(N) ≤ v_p(μ!) for every p (Legendre), and that does not
depend on a. ∎

In particular, ν is a diagonal form with weights w_N = 1_{N|μ!}/N ≥ 0 that do not depend on the comb. It is a
weighted, archimedean ℓ² norm (R-Π).

**Theorem 2.3 (Ξ2.1 is false; PROVED in (ν-i) under injectivity of f ↦ (c_N) on the kernel, which is the
definition of Ψ̌_c).** The upper bound ν ≤ Cℓ fails for every C and every μ.
*Proof.* By prop:ext-gauge, a nonzero φ ∈ 𝒢_T satisfies ℓ(Ef + Eφ) = ℓ(Ef) with 𝒲 invariant, so in the gauge
direction ℓ(Eφ) = 0. φ's translation coefficients are not all zero, so ν(φ) > 0 = Cℓ(φ). The bound also fails in
the quotient. Let ν_q := inf_{coset} ν. The comparison ν_q ≤ C_μ ℓ on the finite-dimensional kernel exists, but
C_μ cannot be uniform. If it were, ν_q would be a comb-independent norm equivalent to ℓ with standard constants.
By Lemma 2.2, ν_q does not see the comb, and neither does ℓ (it is archimedean). Then the inequality
"𝒲 ≥ −εν" would be, as ε → 0, exactly the ℓ-scale version (branch 2: the same statement, no new object). In
both cases Ξ2.1 contributes no new carrier. In (ν-e), ν is a number depending only on μ and 𝔏 = st(𝒲/ν_μ) is a
rescaling of 𝒲: Ξ2.1 does not even type-check, and 𝔏 ≥ 0 ⟺ 𝒲 ≥ −o(ν_μ), which is a weaker bound than L′♯ by a
factor independent of the test. ∎

**Ξ2.1's label: NO-GO.** The literal version is false. The quotient version, if true, would coincide with L′♯
and would contribute no new object.

## 3. Φ.13 complete (PROVED)

**Theorem 3.1 (Łoś dichotomy).** Let ν be an internal normalization and 𝔏_ν = st(∗𝒲/ν).

(a) **Unnormalized, at standard T.** Let T be fixed and the constant sequence. Then ∗λ_A(T;Λ) = λ_A(T;Λ) by
Łoś, because λ_A(T;Λ) is a real number defined in the standard structure and its ∗-image is itself. Hence
st ∗λ_A = λ_A and "∗λ_A ≥ 0" ⟺ "λ_A ≥ 0": it is the statement restricted to Λ, REF-D (branch 2). With
∗T = [T_n] unlimited, the same argument gives "λ_A(T_n) ≥ 0 for 𝒰-almost every n". This is a standard statement
about the family, which is also REF-D.
*PROVED* (Łoś CITED).

(b) **Normalized.** By Lemma 2.1, 𝔏_ν ≥ 0 is equivalent to the standard family 𝒲_μ ≥ −εν_μ for every ε and
𝒰-almost every μ. There are three cases and they are exhaustive:
- (b1) ν_μ ≍ ℓ_μ uniformly: the limit is K3's Γ-limit (K3_GAMMA §2, PROVED there). It is comb-generic: Λ only
  enters in Q₁ = O(1). Branch 1.
- (b2) ν_μ independent of the test (scalar) or a comb-independent norm not equivalent to ℓ: it is an
  information-free rescaling or a weaker, archimedean bound (R-Π, K3 §2). Branch 1.
- (b3) ν_μ depends on the comb: then 𝒲_μ + εν_μ ≥ 0 is a stability or certificate inequality on the standard
  window form, and falls into Φ.1 / BARRIER_D2 Thm 1 (branch 2).

Exhaustiveness follows from Lemma 2.1: every internal ν is a standard sequence, and every standard sequence
falls into one of the three cases depending on whether it depends on the comb and on the test. This was the
ARGUED part of the spec, and it becomes PROVED.

**Third normalization: does not exist.**
- Via d(∗N): d(μ!) is a scalar depending only on μ. It falls into (b2), and st(𝒲/d) = 0 or ±∞ gives no sign
  information beyond that of 𝒲.
- Via Ẑ's Haar measure: the test supported on N ≤ μ^A has counting mass ≤ μ^A/μ!, which is infinitesimal. Its
  L²(L_P) norm is 0, so 𝔏 is either undefined or, rescaled by ∗N, falls into (b2).
- Mixed normalizations, e.g., ν = ℓ + ε·(divisors): are standard sequences and fall into (b1) or (b2) depending
  on which dominates.

PROVED.

## 4. Λ channel and falsifiers (F9)

By Lemma 2.1, the only Λ channel of 𝔏 is 𝒲_μ (I1–I10). The divisibility of ∗N and the ring structure of Ẑ do
not enter the inequality, only ν, and ν does not depend on the comb (Lemma 2.2).
- **Beurling.** The space Ω = ℤ/∗Nℤ and Haar measure are built on the *indices* N ∈ ℕ, not on the generalized
  integers. The object (Ω, L_P, ν) still exists, and 𝔏 is defined with 𝒲_μ^{Beurling}. That Beurling has no
  profinite Ẑ with Haar measure compatible with Poisson does not kill the object, because Ξ2 never uses Poisson
  on Ẑ. The object does not stop existing and does not separate.
- **a_P.** Ẑ_{(P)} = ∏_{p∉P}ℤ_p would only appear if ν used the places of P. By Lemma 2.2 it does not, and the
  same 𝔏 is formed with 𝒲(a_P). It is comb-generic.
- **Epstein (h > 1).** Ô_K and Cl(K) do not appear in ν. 𝔏 is formed with the Epstein 𝒲, with no discrete
  dependence on h, so it fails (F2) C-E′.

For Ẑ to be a real channel one would need the Plancherel form 𝔊 of the ring Ẑ from §D's "target theorem". But
every internal form 𝔊 compared with 𝒲 is, again by Łoś, a standard family 𝔊_μ. The identity 𝔏 = 𝔊 then
amounts to 𝒲_μ = 𝔊_μ + o(ν_μ) at each standard level. That construction is no longer nonstandard: it is a
standard object at each level, and it falls outside Ξ2 (it falls into Ξ1/Ξ3 or into the hard risk "adèle class
space", a closed family, phase 158).

## 5. Labels and index entry

- Lemma Ξ2.1: **NO-GO** (Theorem 2.3).
- Ξ2, the Loeb form on Ẑ: **NO-GO** as an object. Nonstandard analysis adds no carriers (Lemma 2.1), and Ẑ's
  channel is decorative (§4).
- Φ.13: **PROVED** (Theorem 3.1), with Łoś CITED, K3 PROVED and prop:ext-gauge given Guo L4.4 CITED.
- L′♯: OPEN. Row D: OPEN.

**Proposed entry (README, phase 200):**
- **XI2_LOEB_001 (round 16): Ξ2 Loeb form on Ẑ / ultraproduct / normalization by divisors of ∗μ! — NO-GO.**
  Łoś reduction lemma: every internal normalization is a standard sequence ν_μ, and
  𝔏 ≥ 0 ⟺ 𝒲_μ ≥ −εν_μ for 𝒰-almost every μ. Φ.13 becomes PROVED with an exhaustive trichotomy (ν≍ℓ ⇒ K3
  Γ-limit; ν combless ⇒ archimedean; ν with comb ⇒ stability). The filter N | ∗μ! is trivial in the window.
  Ẑ/Haar is not a channel (Beurling, a_P and Epstein form the same object). Do not retry nonstandard,
  hyperfinite or Loeb analysis without a standard form at each level.
