# R162_1902 — Width of the residue window and integrality: the B₂/sawtooth route

Pure mathematics, no numerics run. Target: (O1802.3), i.e. Δ(T) = κ₊ − κ₋ ≥ 0 for all T.
Inputs: R162_1802 (Thm H, Thm R, §6), R162_801 (L2, L3, L5), R162_701 (Lemma 2.2), R162_1001 Thm 3.1 (with the
R162_1190 fixes), R162_1502 Lemma 1, R162_590, Paper 47 eq:W.

**Status: NO-GO (PROVED) for the B₂ / sawtooth positivity route, with one correction to the task premise.**
- §1 Restatement of the hyperplane. **PROVED.** The *pair test* c_H has Mellin transform vanishing at **both**
  s = 0 and s = 1. The test H itself satisfies Φ_H(0) = 0 and Φ_H(1) = 2.
- §2 Lemma C (the B₂ weights cancel exactly). **PROVED.**
- §3 Proposition Z (the integral-comb form on the hyperplane is the symbol Re ζ(½+iz)). **PROVED.**
- §4 Proposition I (that form is indefinite on the hyperplane for large T). **PROVED** modulo a standard
  localisation step. The threshold T₁ is not computed.
- §5 The Λ version is the explicit formula. **E1.**
- §6 F2, the DMV line, and one invented alternative (gcd Gram matrices). The alternative is killed by the Beurling line.

No sign is claimed. No label moves. Gate 1 stays OPEN. (O1802.3) stays open.

## 0. Corpus check

- I grepped "B_2", "Bernoulli", "Fejér", "sawtooth", "Euler–Maclaurin", "gcd" in phases 160–162. Three hits bear on this.
  - R162_701 Lemma 2.2 and R162_801 L3 contain the ψ-sawtooth (B₁) decomposition. Both record it as linear in c_F (F2).
  - R161_001–002 contain the Poisson–Chebyshev anomaly.
- Not found anywhere: the B₂ positive-definiteness idea, the restriction to the one-pole hyperplane, and the ζ-symbol
  identity of §3.

## 1. The hyperplane, restated precisely (PROVED)

**Setup.** Φ_F(s) = ∫F(t)e^{(s−½)t}dt, so A = Φ_F(1) and B = Φ_F(0). Let c = F⋆F̃ with F̃(t) = F(−t). Then

  Φ_c(s) = Φ_F(s)·Φ_F(1−s), so Φ_c(1) = Φ_c(0) = AB.

**Correction to the premise.** On {B = 0} it is the test H that has Φ_H(0) = 0 and Φ_H(1) = 2. The quadratic object
that enters the prime and pole sides is c_H, and its Mellin transform vanishes at **both** points 0 and 1 (by the
symmetry s ↔ 1−s). The condition Φ_H(1) = 2 is only a normalisation. It has no effect on the sign question, because
the width is the infimum of a homogeneous form on a cone.

**Consequence.** On the hyperplane the pole term 2κAB vanishes. Equivalently, the PNT main term vanishes: with
f(u) = u^{−½}c(log u),

  ∫_0^∞ f(u) du = Φ_c(1) = 0 and ∫_0^∞ f(u) du/u = Φ_c(0) = 0.

Both the density-1 main term and its reflected partner are gone, so only the fluctuation is left. Up to the prime
weights, this confirms the task's reading.

## 2. Lemma C: the Bernoulli weights cancel (PROVED)

Let g ∈ C_c²(0,∞), and let B̄₂(u) = B₂({u}) = Σ_{ν≠0} e(νu)/(2π²ν²). These Fourier coefficients are positive, so B̄₂
is positive definite on ℝ/ℤ. Euler–Maclaurin to second order gives

  Σ_{m≥1} g(m) − ∫g = ½∫ g″(u) B̄₂(u) du = ½ Σ_{ν≠0} ĝ″(ν)/(2π²ν²) = −Σ_{ν≠0} ĝ(ν)

(Poisson), because ĝ″(ν) = −4π²ν² ĝ(ν).

- The positive coefficients 1/(2π²ν²) of B₂ are multiplied by the negative multipliers −4π²ν² of d²/du².
- The net weight is the constant −1 on every nonzero frequency, so the B₂ pairing is Poisson summation again.
- B̄₂ ⪰ 0 gives a sign only if g″ is positive definite in the **additive** variable u, i.e. only if −ĝ(ν)ν² ≥ 0 for
  all ν.
- The same cancellation holds at every order k: the coefficients of B_k grow like (2πiν)^{−k} and the multipliers of
  d^k/du^k like (2πiν)^k.

**Failing line.** Our g = f is the pullback of a **multiplicative** autocorrelation. Its additive Fourier coefficients
are

  f̂(ν) = ∫c(x) e^{x/2} e(−νe^x) dx,

and they have no sign (§4). Positive definiteness lives on the ℝ/ℤ side, the test's positivity lives on the ℝ^×_{>0}
side, and no map carries one to the other. This is F2 in its sharpest form: the pairing is linear in c.

## 3. Proposition Z: what the integral comb is on the hyperplane (PROVED)

**Prop Z.** Let F ∈ C_c^∞(I_T) be real with B(F) = 0, and set F̂(z) := Φ_F(½+iz). Then

  S₁(F) := Σ_{n≥1} n^{−½}[c(log n) + c(−log n)] = (1/π)∫_ℝ |F̂(z)|² Re ζ(½+iz) dz.

*Proof.*
- Mellin inversion gives Σ_n n^{−½}c(log n) = (1/2πi)∫_{(2)} ζ(s) Φ_c(s) ds, up to the sign convention s ↔ 1−s,
  which the symmetrisation removes.
- Φ_c is entire and of rapid decay in vertical strips.
- Shift the contour to Re s = ½. The only residue is at s = 1 and equals Φ_c(1) = AB = 0.
- On Re s = ½, Φ_c(½+iz) = F̂(z)F̂(−z) = |F̂(z)|², since F is real.
- The reflected half c(−log n) gives the complex conjugate. Adding the two halves gives 2Re. ∎

**Reading.** On the one-pole hyperplane, the ℤ-integrality input (the counting measure of ℕ, i.e. Σ⌊·⌋, Stirling
and the B₂ series of §2) is **exactly** the multiplier Re ζ(½+iz) against |F̂|². There is nothing left over. R162_801
L5 already forbids an asymptotic use; this is the exact form, and it is a Mellin symbol.

## 4. Proposition I: indefiniteness (PROVED modulo standard localisation)

**Prop I.** There is a finite T₁ such that for T ≥ T₁ the form S₁ takes both signs on {B = 0} ∩ C_c^∞(I_T).

*Proof sketch.*
- Write ζ(½+it) = Z(t)e^{−iθ(t)}. At the Gram point g_n, Re ζ(½+ig_n) = (−1)^n Z(g_n).
- Gram's law fails at n = 126 (g₁₂₆ ≈ 282.45, a classical fact that I did not recheck). There (−1)^n Z(g_n) < 0, so
  Re ζ(½+it) < −η < 0 on an interval J around g₁₂₆.
- Take F₁ and F₂ to be modulated bumps whose |F̂_j|² concentrate on ±J, up to tails of mass ε(T) → 0 as T → ∞
  (Paley–Wiener localisation at scale 1/T).
- Choose α so that F = F₁ − αF₂ satisfies B(F) = 0. This is possible because the B values are generically nonzero.
  Cross terms are controlled by the same tails. Then S₁(F) < 0.
- Positivity is shown the same way near t ≈ 14, where Re ζ > 0 near a Gram point that obeys the law. ∎

- For small T the symbol cannot be resolved. There S₁ is dominated by the n = 1 term 2c(0) = 2‖F‖², so it is
  positive. That is an archimedean effect, not an arithmetic one.
- So integrality in the B₂ form produces a sign-indefinite form. The indefiniteness comes from the phase θ(t), i.e.
  from Γ, as in any Poisson dual.

## 5. The Λ version (E1)

- Replacing weight 1 by Λ (the ledger L2 of R162_801, which is L1(a)) replaces Re ζ by Re(−ζ′/ζ)(½+iz) in the sense of
  distributions.
- This distribution is singular exactly at the zeros, and Prop Z becomes the explicit formula on the hyperplane:
  width(T) ≥ 0 ⟺ Σ_ρ-positivity on {B = 0}, i.e. Theorem H read on the zero side.
- Every exact route from the ledger to Λ passes through μ∗log (a signed combination; R162_801 L4). Applying it inside
  Prop Z replaces ζ by ζ′/ζ with no inequality gained.
- Verdict: E1.

## 6. F2, DMV, and the invented alternative

- **F2.**
  - Props Z and I show the integrality contribution is linear in |F̂|² with a fixed signed symbol.
  - The (PC) square is never formed. The sign is the sign of a symbol, and Re ζ is indefinite.
  - A_M → −A_M does not even arise. F2 kills the route one step earlier than in R162_701.
- **DMV Beurling.**
  - Prop Z holds verbatim with ζ_B in place of ζ. The Mellin argument uses only the pole of ζ_B at 1 and its
    continuation to Re s = ½, which the DMV systems have (N(x) = ρx + O(x^θ), θ < ½).
  - The ℤ-periodisation (B₂) exists only for ℕ. But §2 shows the periodisation is *representational*: it changes how
    the value is written, not the value.
  - So the "no ℤ periodisation" line fails for DMV only at a step that carries no inequality. It is not a separating
    mechanism.
  - Integrality enters through the symbol ζ versus ζ_B, i.e. through the zeros. That is E1.
- **Invented alternative (killed).**
  - Integrality does yield a genuine PSD object: the gcd Gram matrix
    Σ_{m,n} x_m x_n log gcd(m,n) = Σ_d Λ(d)(Σ_{d|m} x_m)² ⪰ 0, which uses Λ∗1 = log.
  - Three failures:
    - (i) It is Beurling-valid. G_B is free, so gcd exists and Λ_B∗1 = log. It therefore fails the DMV line.
    - (ii) It pairs tests through the divisibility d | m, which is a dilation, i.e. a window shift (R160_D4 Thm 5.1).
    - (iii) Its sign is "prime comb ≥ 0", which is the primes-hurt direction for W = Arch − ΣΛΦ.
  - The torsion cocycle (R162_1001 Thm 3.1), which does separate Beurling, collapses to a linear use by R162_1001
    Thm 5.1. The collar identity (R162_1502 Lemma 1) is inert by R162_1502 Thm 6. Neither supplies a PSD block on
    {B = 0}.

## 7. For R162_590 §1c and the README

- Add the row: "B₂/sawtooth positivity on the one-pole hyperplane | R162_1902 | Bernoulli weights cancel against
  derivatives (Lemma C). The integral comb on {B = 0} is ∫|F̂|² Re ζ(½+iz) (Prop Z), indefinite by Gram failure
  (Prop I). The Λ version is the explicit formula. DMV has the identical ζ_B identity | F2, E1".
- Correction for R162_1802: the pair test c_H vanishes at both s = 0 and s = 1. The pole and the PNT main term both
  drop out.
- (O1802.3) remains open. Any integrality mechanism must be nonlinear in c. Linear in c means a Mellin symbol by
  Prop Z, and no symbol built from ζ is sign-definite on the line.
