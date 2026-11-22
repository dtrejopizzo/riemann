# R162_1002 — Fourier-quasicrystal route to Gate 1

Note. Pure mathematics, no numerics.
Inputs: README (F1–F4), R162_590 (dead-end map), R162_903 §8 (residual: a discontinuous functional separating
integer support from Beurling support and 1 from χ₂). Corpus check: R157_002 row 42 (Lee–Yang/Kurasov–Sarnak:
EQUIV), G2_P1_R3 l.150 ("the Kreĭn/Guinand quasicrystal problem"), G2_P4_R3/R4 and G2_B6_R5 ((H_Q), crystalline
uniqueness, OPEN, "not a sign"), R160_S5 l.140, phase-46/138 l.277 (Olevskii–Ulanovskii as sampling context).
The literature below is cited from memory and not re-verified: Lev–Olevskii (Invent. 2015, uniformly discrete
support and spectrum), Olevskii–Ulanovskii (Fourier quasicrystals with unit masses = zero sets of real-rooted
exponential polynomials), Kurasov–Sarnak (arXiv:2004.05678, real stable polynomials).

**Verdict: NO-GO (reduction).** The rigidity theorem requested is equivalent, window by window, to W_T ≻ 0 on the
radical at T = T_*. Taken over all T it is Theorem Z of Paper 46 (RH ⟺ one-sided smoothing for every T). No
quasicrystal theorem applies, because each of them assumes the reality of the zero support. Section 2 gives
three exact facts (P1–P3, PROVED) that locate the obstruction.

## 0. Falsifier lines, stated first

A closing theorem would say: (S) support of the prime side ⊂ ±log ℕ, and (Λ) a*1 = log exactly, together
exclude a localized null direction unless the zero side is real. It must fail on these lines:

- **Beurling (DMV).** Support ±log 𝒩_B with 𝒩_B ⊄ ℕ; a_B*1_B = log on 𝒩_B; off-line zeros. It must violate (S).
- **DH.** Support ±log ℕ; a functional equation; no Euler product. Here Λ_DH := −(L'/L) coefficients, and
  Λ_DH * a_DH = log·a_DH with a_DH ≠ 1. It must violate (Λ) in the form "a = 1".
- **Λχ₂.** Support ±log ℕ; Λχ₂ * χ₂ = log·χ₂. It must violate "a = 1" (character ≠ trivial).
- **F1.** The argument must use λ = 0 and minimality. **F2.** It must not be invariant under A_M → −A_M.

## 1. Why the quasicrystal theorems do not apply (hypothesis audit)

The Guinand–Weil pair is μ = Σ_ρ δ_{γ_ρ} ↔ ν = −Σ Λ(n)n^{−1/2}(δ_{log n}+δ_{−log n}) + Ω_∞(x)dx + (pole terms).
Here Ω_∞ is the archimedean density, which is absolutely continuous.

1. **Spectrum not discrete.** ν has the ac part Ω_∞. After subtracting the smooth counting density (1/2π)log(t/2π)
   from μ, the zero side becomes a signed measure. Positivity is lost on one side or the other.
2. **Not uniformly discrete.** log(n+1) − log n → 0, so Lev–Olevskii does not apply.
3. **Masses.** Λ(n)n^{−1/2} is not integer-valued and has the wrong sign. The Olevskii–Ulanovskii unit-mass
   classification is about the zero side and requires the dual to be a measure with locally finite support.
   The resulting description ("the zeros of a real-rooted exponential polynomial with finitely generated
   frequencies") fails for ζ, because {log p} is ℚ-linearly independent and of infinite rank.
4. **Reality is an input.** Every crystalline-measure theorem is a statement about measures on ℝ. If ρ is off
   the line, μ is not a measure on ℝ: it is a distribution with complex translates e^{±Im γ·x}. The theorems
   begin by assuming what Gate 1 has to prove. Kurasov–Sarnak make this explicit: reality comes from real
   stability, which is Lee–Yang, which is EQUIV by R157_002 row 42.

So a new theorem cannot be an instance of known rigidity. It would have to be proved directly on the window form.

## 2. Exact facts (PROVED)

**P1 (window locality).** For supp F ⊂ [−T,T], the form W_T(F) = ν(F*F̃) involves only a|_{n ≤ e^{2T}} and Ω_∞.
Hence T_*(a) depends only on a restricted to [1, e^{2T_*}].
*Proof.* supp F*F̃ ⊂ [−2T,2T], and ν restricted to (−2T,2T) sees only the atoms log n < 2T. ∎

**Corollary P1′ (Beurling line, automatic).** Let B be a Beurling system with 𝒩_B ∩ [1,X] = ℕ ∩ [1,X]. If B has a
first contact, then T_*(B) ≥ ½ log X. *Proof.* If T_*(B) < ½ log X, then by P1 ζ has the same window form and a
first contact at the same T, which is excluded below ½log5 by R162_303, and in general it is exactly what is in
question. Stated carefully: T_*(B) = T_*(ζ) whenever T_*(ζ) < ½log X. ∎
So a window theorem does separate Beurling for free. But it does so by *identifying* the data with ζ's data, not
through any rigidity.

**P2 (singleton class).** On support ⊂ ℕ, the relation a*1 = log on [1,N] determines a on [1,N] uniquely
(a(1) = 0, then recursively a(n) = log n − Σ_{d|n, d<n} a(d)). The same holds for Λχ₂ with 1 replaced by χ₂, and for
DH with a_DH. *Proof.* Möbius inversion on the divisor-closed set [1,N]. ∎
**Consequence.** The class C_T = {window data with (S) and (Λ) at a = 1} is a single point: ζ's data on
[1, e^{2T}]. A "rigidity theorem for the class C_T" is therefore the statement "the one form W_T^ζ has trivial
radical at λ = 0". Over all T this is Theorem Z / thm:Zexh, which is equivalent to RH. The discontinuous
functional asked for in R162_903 exists: it is the indicator of C_T. But it only *names* ζ. It gives no
mechanism. This is the precise sense in which the route reduces.

**P3 (the pair gives no local uniqueness).** Take a null direction F at T_*, write g = F*F̃, and let μ' = μ + εδ
be any perturbation of the zero side whose Fourier transform vanishes on (−2T_*,2T_*). Then μ' pairs with g
exactly as μ does. Hence the null condition μ(ĝ) = 0 does not determine μ modulo such δ, and "zero side real" is
not a function of the window data unless the answer is already RH on that window.
*Proof.* ĝ extends to an entire function of exponential type 2T_*. Paley–Wiener duality gives δ(ĝ) = δ̂(g) = 0,
because supp g ⊂ [−2T_*,2T_*] and δ̂ = 0 there (extend by density to the closed interval using the tempered
bounds). ∎
This is why a *localized* null direction cannot be excluded by a *global* rigidity principle. Global rigidity
(μ is determined by ν on all of ℝ) is trivially true, since the explicit formula determines μ, and it is
sign-blind. Local rigidity is false modulo the class of Fourier transforms that vanish on (−2T_*,2T_*).

## 3. Attempted invention and why it closes negatively

Candidate: "a positive discrete μ whose Guinand dual has atoms only at ±log ℕ with weights obeying Λ*1 = log
admits no g ≥ 0 of type ≤ 2T with μ(ĝ) = 0 and ν(g) = 0". Checks:
- **F3/Φ.** By P2 the hypothesis selects ζ. The candidate cannot be tested on DH or Λχ₂, because those lie
  outside the class by construction. Hence the falsifier lines "pass" only vacuously. Beurling is excluded by P1′
  for T < ½log X, and beyond that by (S) through identification only.
- **F1.** For λ > 0 eigenvectors, μ(ĝ) = λ‖F‖² > 0, and the candidate is consistent. It carries information only
  at λ = 0, and there it is the definition of first contact. There is no non-perturbative content.
- **F2.** The candidate is stated through μ(ĝ), which is linear in the pair. It is invariant under the orientation
  flip that preserves the square of (PC). It does not orient.
- **Positivity hypothesis "μ positive discrete"** already means the zeros are real: circular (§1.4).
  Dropping it leaves the candidate equivalent to W_{T_*} having no radical.

## 4. Status

- P1, P1′, P2, P3: PROVED (elementary).
- Quasicrystal rigidity as a Gate 1 closure: **NO-GO**. Known theorems presuppose reality (§1.4) and fail their
  hypotheses (§1.1–1.3). Any new window theorem on the class C_T is W_{T}^ζ-definiteness (P2), which over all T is
  Theorem Z ⟺ RH. The residual of R162_903 is sharpened as follows: the required discontinuous functional must act
  through a *mechanism uniform over a family containing ζ as a non-isolated point*. Otherwise it is the
  indicator of C_T, a restatement.
- Dead-end map entry: "Fourier quasicrystal / crystalline rigidity (Guinand pair) | R162_1002 | reality presupposed;
  class C_T is a singleton (P2); local uniqueness false modulo PW-annihilated perturbations (P3) | E1, F2".
