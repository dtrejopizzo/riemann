# R162_1001 — Round 10: the ×p / Furstenberg rigidity route from a first-contact vector — **NO-GO (PROVED), one new exact structure**

Note. Inputs: README (F1–F4, rounds 1–9), R162_590 §2 item 5, R162_903 (residual §8),
R160_M12_R1 (Thms 2.1, 3.4–3.6), R157_002 #27, R162_502 B1/B2.1. Conventions of R162_903: X = e^{2T},
F ∈ N = ker H_{T_*}, c_F = autocorrelation of F (supported in [−2T_*, 2T_*]), w_F(n) := n^{-1/2} c_F(log n),
prime term of the Weil form P(F) = Σ_n a(n) w_F(n) (a = Λ for ζ). Pure mathematics; no numerics.

**Status.** The route is built in the form requested (a measure on ℝ/ℤ or on the solenoid, built from F, c_F or the
zero side, invariant or quasi-invariant under ×p for all p, followed by rigidity) and refuted. Labels:
- Thm 2.1 (full-semigroup rigidity is Fourier-trivial) PROVED.
- Thm 2.2 (window data are absolutely continuous; invariance ⇒ trivial data; Cesàro limit = Lebesgue for every F) PROVED.
- Thm 3.1 (torsion-point distribution Φ_a and the ×p cocycle; the cocycle for all p characterises a = Λ) PROVED. **New.**
- Prop 3.2 (Φ_a is the prime term: P(F) = ⟨Φ_a, h_F⟩, h_F a trigonometric polynomial) PROVED.
- Prop 4.1 (zero side: Kronecker image of zeros is Haar; Landau defect is the linear datum Λ) PROVED mod CITED (Landau, Hlawka).
- Thm 5.1 (collapse: every exact use of Φ_Λ against window data is linear in c_F) PROVED.
Gate 1 stays OPEN. No label moves.

## 0. Corpus check (rule )

R162_590 §2 item 5 says "never analysed against W_T". That is inaccurate: **R160_M12_R1** (phase 160, front M12)
analysed it against the Kronecker torus ∏_p S¹: Thm 3.4 (window contraction T ↦ T/p is (×p)_* on each prime circle),
Thm 3.5 (a window marginal invariant under one ×p is Haar; band-limitation replaces entropy), Thm 3.6 (Rudolph–Johnson
positive-entropy measures are exactly Euler-neutral; zero-entropy measures realise both signs). R157_002 #27 EXCL
("positions only"). This memo does **not** redo those. New here: (i) the additive circle ℝ/ℤ with its torsion points,
which is the only place where ×n and the Dirichlet index n are the same object (the ring ℤ); (ii) Thm 3.1; (iii) the
first-contact vector (not generic window data) and the zero side. Grep "torsion", "cocycle", "Landau defect",
"ν_d" in phases 150–162: no hits on these mechanisms. R162_590 §2 item 5 should be amended to point to R160_M12_R1.

**Correction to the task premise.** "Beurling systems have no ×n action" is false as stated: the power map χ ↦ χ^n
exists on the dual solenoid Hom(G_B, S¹) of any Beurling multiplicative group G_B, so R160's Kronecker ×p is
Beurling-valid (its I-6 line). What is integer-only is the **ring** structure: ℕ acts on ℝ/ℤ by x ↦ nx *and* the
characters e(nx) of ℝ/ℤ are indexed by the same n, so the d-torsion points {r/d} are indexed by Dirichlet indices.
Section 3 uses exactly this and nothing else.

## 1. Failing lines, stated first

| model | line that fails | where |
|---|---|---|
| Beurling DMV | Φ_a cannot be formed: torsion points ν_g need g ∈ ℤ; on the solenoid the cocycle holds for Λ_B (§3 Rem) | Thm 3.1(c) |
| Λχ₂ | cocycle (3.1) fails at p = 2 (holds at odd p) | Thm 3.1(b) |
| DH | a*1 ≠ log: cocycle fails at some p | Thm 3.1(b) |
| deletion Λ1_{n≥5}, κ-models | cocycle fails at p = 2, 3 (a(2),a(3),a(4) wrong) | Thm 3.1(b) |
| ζ | nothing fails — and nothing follows (Thm 5.1) | §5 |

So the object Φ_Λ passes F3 completely (it is the first object in phase 162 that Λχ₂ *and* Beurling fail), but it
fails F1 and F2 at the use step (§6).

## 2. Rigidity for the full semigroup, and window data

**Thm 2.1.** A Borel probability ν on ℝ/ℤ is invariant under x ↦ px for every prime p iff ν = αδ_0 + (1−α)Leb,
α ∈ [0,1]. (Same on the solenoid 𝕊 = (𝔸_ℚ/ℚ): invariance under ×ℕ ⇒ ν = αδ_0+(1−α)Haar.)
*Proof.* (×p)_*ν = ν ⟺ ν̂(pk) = ν̂(k) ∀k ∈ ℤ. For all p: ν̂(k) = ν̂(sgn k) for k ≠ 0, and ν̂(−1) = conj ν̂(1) = ν̂(1)
(apply to k = −1 and invariance under ×p for k = ±1 with ν̂(−p) = ν̂(−1)); also ν̂(1) = ν̂(p) for all p, and a
positive-definite sequence constant = β off 0 is β·1 + (1−β)δ_0-coefficient, i.e. β ∈ [0,1] real, ν = βδ_0 + (1−β)Leb.
Solenoid: same with ℚ in place of ℤ. ∎

So with *all* primes no Furstenberg/Rudolph–Johnson theorem is needed: the rigidity is Fourier algebra. The deep
theorems concern sub-semigroups ({2,3}); restricting to them only weakens the conclusion.

**Thm 2.2 (window data).** Let σ be any finite signed measure on ℝ/ℤ built from finite-window data of F, i.e.
σ̂(k) = φ(k) with φ supported on |k| ≤ X (e.g. φ = w_F, |w_F|², Möbius transforms of w_F, any element of 𝒜_T acting on
w_F). Then (a) σ = f dx, f a trigonometric polynomial; (b) σ is ×p-invariant for one prime p iff φ(k) = 0 for 0<|k|≤X;
(c) for every such σ ≥ 0 and every Følner/Cesàro average over n ∈ ℕ, (1/N)Σ_{n≤N}(×n)_*σ → σ̂(0)·Leb weak*.
*Proof.* (a) finite Fourier support. (b) φ(pk) = φ(k) iterated gives φ(k) = φ(p^j k) = 0 for p^j|k| > X. (c) the k-th
coefficient of the average is (1/N)Σ_{n≤N} φ(nk), which is ≤ X/N·‖φ‖_∞ → 0. ∎

**Failing line (F1, F3).** (c) holds for every F, every λ, every coefficient system (ζ, Beurling on its solenoid,
Λχ₂, DH): Krylov–Bogolyubov from a first-contact vector always returns Lebesgue. (b) is R160 Thm 3.5 on the additive
circle. Singular (atomic or zero-dimensional) invariant measures require infinitely many nonzero coefficients, hence
T → ∞, where the first-contact information is diluted below every detectable scale (R162_801 L5 / Theorem M).

## 3. The integer-only object: torsion points and the ×p cocycle (PROVED, new)

For d ≥ 1 let ν_d = (1/d)Σ_{r mod d} δ_{r/d} (uniform on the d-torsion of ℝ/ℤ); ν̂_d(k) = 1_{d|k}. For an
arithmetic function a with a(1) = 0 define the distribution
  Φ_a := Σ_{d≥2} a(d)(ν_d − Leb),  Φ̂_a(k) = Σ_{d|k} a(d) = (a*1)(|k|) for k ≠ 0, Φ̂_a(0) = 0.
(Converges in 𝒟′(ℝ/ℤ): coefficients grow at most polynomially.) The transfer operator of ×p acts on coefficients by
(ℒ_pΦ)^(k) = Φ̂(pk).

**Thm 3.1.** (a) For a = Λ: ℒ_pΦ_Λ − Φ_Λ = log p·(δ_0 − Leb) for every prime p. (3.1)
(b) Conversely, if a(1)=0 and (3.1) holds for every prime p, then a = Λ. If a*1 = log fails, the first failing prime
is computable: (3.1) fails at the least p dividing the least n with (a*1)(n) ≠ log n. For Λχ₂ (χ₂(2^k) = (−1)^k or
the mod-4 character: a(2^k) ≠ log 2) it fails at p = 2 only in the first case / at p=2 in both; for deletion and
κ-models at p ∈ {2,3}; for DH at some p.
(c) For a Beurling system with generalized integers 𝒩_B ⊄ ℤ, Φ_{Λ_B} is not defined on ℝ/ℤ (ν_g needs g ∈ ℤ). On the
Beurling solenoid Hom(G_B, S¹) the analogue of ν_d does not exist either (G_B is torsion-free divisible-free; its dual
has no "g-torsion indexed by g ∈ 𝒩_B" compatible with an additive index), so the only Beurling-valid transport of
(3.1) is the multiplicative one, which is B2.1 of R162_502.
*Proof.* (a) Φ̂_Λ(k) = log|k|; log|pk| − log|k| = log p for k ≠ 0; at k = 0 both sides give 0 − 0 on the left and
log p(1 − 1) = 0 on the right; the right side has coefficients log p for k ≠ 0. (b) (3.1) for all p and Φ̂(±1) =
a(1)·… = 0 give Φ̂(k) = log|k| by induction on Ω(k); Möbius inversion gives a = μ*log = Λ. The failing-prime statement
is the same induction read in the contrapositive. (c) definitional. ∎

**Reading.** (3.1) is the ×p form of Λ*1 = log: log is an additive cocycle for the multiplicative semigroup acting on
the additive circle, and Φ_Λ is the unique torsion-supported distribution with that cocycle. Unlike every object of
rounds 1–9 it is **discontinuous in the support**: moving a single index off ℤ destroys ν_d. This is exactly the kind
of functional R162_903 §8 asks for. The question is whether it can be *used* on F.

**Prop 3.2 (Φ_a is the prime term).** Let ĥ_F(k) := Σ_{j≥1} μ(j) w_F(|k|j) (finite: w_F supported on n ≤ X). Then
h_F is a trigonometric polynomial of degree ≤ X and ⟨Φ_a, h_F⟩ = Σ_d a(d) w_F(d) = P(F) for every a.
*Proof.* ⟨ν_d − Leb, h⟩ = Σ_{j≠0} ĥ(dj) (conjugation conventions: h real-even since c_F is even), and
Σ_{j≥1} ĥ(dj) = Σ_{j}Σ_i μ(i) w_F(dji) = Σ_m w_F(dm)Σ_{i|m}μ(i) = w_F(d). Factor 2 from ±j absorbed in the
normalisation of P. ∎

So the Weil form reads Q(F) = A^∞(F) − ⟨Φ_Λ, h_F⟩, and via (3.1): ⟨Φ_Λ, h_F∘(×p) − h_F⟩ = log p·(h_F(0) − ∫h_F).
The right side is Σ_{k≠0} ĥ_F(k) log p; the left side, on the F side, is the compressed shift by log p of c_F.
**This is B2.1 (Z X̂ Z^{-1} = X̂ + M_T(Λ), R162_903 Thm 3.2) in circle coordinates** — a linear identity in c_F.

## 4. The zero side

**Prop 4.1.** Let κ: γ ↦ (γ log p / 2π)_p ∈ ∏_p ℝ/ℤ (Kronecker map; dual of ℚ_{>0}). (a) (1/N(T))Σ_{0<γ≤T} δ_{κ(γ)}
→ Haar (Hlawka). (b) The defect (2π/T)[Σ_{γ≤T} δ_{κ(γ)} − N(T)·Haar] → 𝔇 in 𝒟′, with 𝔇̂(x) = −Λ(x) for x ∈ ℕ_{≥2},
−Λ(1/x) for 1/x ∈ ℕ_{≥2}, 0 on all other x ∈ ℚ_{>0} (Landau's formula Σ_{γ≤T} x^{iγ} = −TΛ(x)/2π + O_x(log T),
unconditional). (c) Neither limit is invariant under any power map χ ↦ χ^n (n ≥ 2) except Haar in (a); (b)
transforms as 𝔇̂(x^n) = −Λ(x^n) = −Λ(x) iff x is a prime power — a statement about Λ on powers, not about zeros.
*Proof.* (a),(b) CITED (Landau 1912; Hlawka 1975; unconditional). (c) direct. ∎

**Failing line.** (a) is Haar for ζ, for Beurling systems with off-line zeros (their Landau formula holds with Λ_B),
and for Λχ₂; (b) is the linear datum Λ again (it is the explicit formula at second order). Rigidity applied to (a)
gives Haar, which is its hypothesis; nothing about λ = 0 at T_*. The first-contact F enters the zero side only as
|F̂(γ)|² weights of total zero-sum = A^∞(F) − P(F) (the explicit formula), again linear in c_F.

## 5. Collapse of every use (PROVED)

**Thm 5.1.** Let Ψ be any functional of F of the form Ψ(F) = ⟨Φ_Λ^{⊗d} ⊛ ℳ, 𝐡_F⟩ where 𝐡_F is built from finitely
many window quantities of F (Fourier support ≤ X in each variable), ℳ ranges over products of ν_d, Leb, δ_0, and
transfer operators ℒ_n. Then Ψ(F) = Σ_{d_1,…,d_d} Λ(d_1)…Λ(d_d) W(d_1,…,d_d; c_F^{⊗…}), a finite sum, and the atomic
(torsion) structure of Φ_Λ enters only through the finitely many values Φ̂_Λ(k) = log k, k ≤ X^{O(1)}. In particular
Ψ is a *continuous* function of the finitely many numbers (log n, Λ(n))_{n ≤ X^{O(1)}}, and the discontinuity of Φ_Λ
in the support positions is invisible.
*Proof.* Pairing a distribution with a trigonometric polynomial reads only the coefficients in its Fourier support
(Thm 2.2(a)); the coefficients of Φ_Λ are log|k|; products and ℒ_n preserve finite Fourier support up to X^{O(d)}. ∎

Consequently: to use the torsion atoms one needs a test that is *not* a trigonometric polynomial (e.g. evaluation at a
rational point r/d with an infinite-degree kernel), i.e. data of F at T = ∞. Every such use is a T → ∞ limit of
window quantities and is subject to Theorem M / R162_801 L5 (defect ≤ exp(−exp((2−ε)T)) in relative size).
Degree d > 1 reduces to the tensor model of R162_903 Thm 5.1 with Φ_Λ^{⊗d} = torsion distribution on (ℝ/ℤ)^d, same walls.

## 6. F1, F2

**F1.** Thms 2.1, 2.2, 3.1 and Prop 4.1 do not mention F. Prop 3.2 and Thm 5.1 are identities valid for every F;
λ = 0 enters only as the scalar equation A^∞(F) = ⟨Φ_Λ, h_F⟩ (+ archimedean/polar terms). An eigenvector with λ > 0
satisfies the same identities with that scalar changed. Minimality of T_* is not used by any rigidity step because no
F-built measure is invariant (Thm 2.2(b)). **F1 not passed.**
**F2.** h_F depends on F only through c_F, which is even under F ↦ −F and under A_M → −A_M (the (PC) orientation);
Φ_Λ is F-independent. **F2 not passed.**
F3 is passed by Φ_Λ (§1) but only at the level of the object; at the use step Thm 5.1 makes it a function of the
finite list (log n, Λ(n)), which Beurling systems with integer-close generalized primes approximate continuously.
F4: not a graph limit; n/a.

## 7. Verdict and residual

NO-GO (PROVED). (i) With all primes, ×p-rigidity is Fourier-trivial (Thm 2.1); (ii) window/first-contact data give
a.c. measures, never invariant, and their ergodic averages are Lebesgue for every F and every model (Thm 2.2); (iii)
the zero side gives Haar plus the Landau defect Λ (Prop 4.1); (iv) the one genuinely integer-only object, the torsion
distribution Φ_Λ with the exact cocycle (3.1), characterises Λ among all a and is undefined for Beurling (Thm 3.1), but
it pairs with window data only through finitely many Fourier coefficients and becomes the prime term (Prop 3.2,
Thm 5.1). Rigidity is sign-blind (R160 Thm 3.6) and here also λ-blind.

**Sharpened residual.** The R162_903 residual now has a concrete candidate object: Φ_Λ is a discontinuous-in-support
functional that separates ℤ from Beurling and 1 from χ₂ and is not a congruence invariant. What is missing is a
**non-band-limited test built from the first-contact vector at finite T_*** — a way for F ∈ ker H_{T_*} to produce a
function on ℝ/ℤ with singular behaviour at rationals (e.g. through the analytic continuation of F̂ or the Sonin/Hardy
structure of R162_201), so that ⟨Φ_Λ, ·⟩ reads the torsion atoms rather than finitely many log k. Without that, the
route is B2.1. Add to R162_590 §1c: "×p / torsion rigidity — R162_1001 — Fourier-trivial for all p (2.1), window a.c.
(2.2), torsion cocycle characterises Λ but pairs as the prime term (3.1, 3.2, 5.1) — F1, F2".
