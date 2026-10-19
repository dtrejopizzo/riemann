# R186_033 — Four new objects on the sign of the window form; one developed

Goal of the memo: propose objects that are **not** linear reductions in a fixed basis (W-lin), that do not fall
under Lemma R (R155_010: no flat top has ŵ ≥ 0) nor under BR (R185_005: schemes in 𝔐 with L/D/C/Q statements
over Λ), and develop the first lemma of one of them. Standalone script: `r033_pnt_window_identity.py`.

Notation (Paper 47): 𝔞_T(F) = C₀‖F‖² + ∫₀^∞ K(u)(Φ(0) − Φ(u))du − Σ_{n∈N_T} v_nΦ(log n), Φ = 𝒞_F autocorrelation,
K(u) = 2e^{−u/2}/(1 − e^{−2u}) = 2Σ_{k≥0}e^{−(2k+½)u}, C₀ = ψ(¼) − log π = −5.37218, v_n = 2Λ(n)/√n,
𝒫_T = {A(F) = B(F) = 0}, λ_A(T) = inf 𝔞_T over the sphere of 𝒫_T.

**Summary of labels.** Lemma 1 (PNT-window identity) PROVED. Lemma 2 (Bochner of e^{−s_T}) PROVED.
Log-convexity law NO-GO (NUMERICAL, falsified on the grid). Jensen bounds (scalar and operator) NO-GO due to O(1)
loss (ARGUED with a number). **No contact with the sign in this memo.**

---

## 0. What the map says and what is respected

- Walls read: grid §3 (W1–W12, W11′, W-Sonin, W-factor, W-dither, W-lin), log 13–27; BR (R185_005 §1–2);
 CROSSWORD-TO-D; phase 186 rounds 1–15 (README), R186_029/030/031/107; Paper 47 def:W, def:PD,
 thm:A, lem:K, thm:S, thm:Z, thm:margin, thm:log5W, thm:parityschur, prop:polarcap.
- What already exists and is **not** repeated: Metzler/Perron of −𝔞_T (R160_C7 Rem. 3.3), Doob transform of the
 ground state (phase 61 OPEN-PROBLEMS §Step 2.3, phase 114 d_118), Kreĭn flow / canonical system in T
 (G2_B5_R1, R162_802, R186_004), Szegő/Widom on s_T (R164_502 L0/L2/L6/L9), rate formula dλ/dT
 (R153_012/013), homotopy in the coupling sΛ (R162_1801 Thm D), block Schur and block Tate
 (R186_024/025: there it is already observed that two Tate moments per block cancel the term 2e^{−u/2} of K).
- Loss rule (what decides everything below): λ_A(½log5) ≈ 3.4·10⁻¹² and thm:margin makes it super-exponential.
 Every inequality that is not an **identity at the minimizer** loses O(1) and cannot decide the sign.
 Only exact identities, integer invariants, or multiplicative structures survive (sign = product of signs).

---

## 1. The ideas (a)–(e)

### Idea 1 — PNT-window identity on the primitive class (CHOSEN)

**(a) Object.** For Φ ∈ 𝒦_prim (autocorrelation of F ∈ 𝒫_T) the Stieltjes functional of the Chebyshev error
 E_ψ(Φ) := 2 ∫₁^{e^{2T}} x^{−1/2} Φ(log x) d(x − ψ(x)),
and the Lévy energy of the archimedean remainder K₁ := K − 2e^{−u/2} = 2e^{−5u/2}/(1 − e^{−2u}) ≥ 0,
 Lev_{K₁}(Φ) := ∫₀^∞ K₁(u)(Φ(0) − Φ(u))du ≥ 0.
**Lemma 1 (PROVED, §2):** 𝔞_T(F) = (C₀ + 4)Φ(0) + E_ψ(Φ) + Lev_{K₁}(Φ) for every F ∈ 𝒫_T, with C₀ + 4 = −1.37218.
**(b) Why it does not fall under the walls.** It is not a reduction in a fixed basis nor a Schur complement: it is
an identity in the form domain, exact at the minimizer (zero loss, so the rule of §0 does not kill it). It is not
a dual certificate (there is no measure ν outside the window; Lemma R does not apply). It is not a statement about
Λ alone: it couples the measure d(x − ψ) with the energy K₁ (outside 𝔐 by O4 of BR). **Honesty:** it is an
exact reformulation; on its own it inherits the margin (W-lin in its "rewriting" version); its value is that it
localizes where the near-cancellation lives (§3) and changes the arithmetic object: it is no longer the comb, it is
d(x − ψ) with weight x^{−1/2}.
**(c) First lemma.** Lemma 1 (proved in §2) and its numerical corollary (§3).
**(d) Falsifier.** For the identity: none (it is algebra). For the reading "the near-cancellation is archimedean":
that Lev_{K₁}(h*) − 1.372‖h*‖² does not track |E_ψ(h*)| at some T ≤ ½log5 (§3 confirms it on the grid).
**(e) Check.** grep "x − ψ", "ψ(x) − x", "d(x − ψ" in 03-research: appears only as the global D-ψ form
(R186_000 l.232; R160_001 l.192: "ψ(x) − x ≪ x^{½+ε}"), never as a per-window identity with remainder Lev_{K₁}.
The cancellation of the term 2e^{−u/2} by Tate is in R186_024/104 per block, not globally; the constant −1.372 and
the breakdown of §3 are new.

### Idea 2 — Log-convexity law of log λ_A in a canonical variable (NO-GO NUMERICAL)

**(a) Object.** The function T ↦ log λ_A(T) and its reparametrizations w = e^{2T}, e^{4T}, 𝒜_T.
**(b) Escape.** It is nonlinear in the form (logarithm of an infimum); a differential law in T is not a fixed
basis. Exact argument: if f = log λ_A is convex on [a, b) and finite with finite right derivative at a, then
f ≥ f(a) + f′₊(a)(w − a) > −∞ on [a, b): λ_A cannot vanish at b. That is, **convexity in the region where
λ_A > 0 ⟹ λ_A > 0 forever**, without margin or compactness (it is not W2: it does not bound λ, it bounds the shape
of its graph).
**(c) First lemma.** "log λ_A is convex in w on [½log2, ½log5]".
**(d) Falsifier.** Second differences of mixed sign on the grid. **It happens:** with 25 points on [0.36, 0.80]
(script §4) the second differences give 5 (+)/19 (−) in T, 7/17 in e^{2T}, 10/14 in e^{4T}: mostly concave, convex
in no variable. Consistent with thm:margin (−log λ_A super-exponential ⟹ concave in T). NO-GO.
**(e) Check.** "log-convex|log-concav" (54 files) refers to Pólya/Laguerre and to weights; not to λ_A(T).
The rate formula of R153_012 does not establish convexity.

### Idea 3 — Bochner positivity of e^{−s_T} and Feynman–Kac representation (structure PROVED; bounds NO-GO)

**(a) Object.** The exponentiated symbol e^{−s_T(τ)}, s_T = m − Σ v_n cos(τ log n).
**Lemma 2 (PROVED).** e^{−s_T} is positive definite in the Bochner sense: e^{−m} = e^{−C₀}e^{−ψ_Lévy} is the
characteristic function at time 1 of the process of thm:S (Schoenberg), and e^{Σ v_n cos(τ log n)} =
∏_n Σ_k I_k(v_n)cos(kτ log n) is a Dirichlet-cosine series over the N_T-smooth numbers with coefficients
∏ I_{k_n}(v_n) > 0 (modified Bessel). So e^{−s_T} = ĥ_T with h_T = e^{−C₀}p₁ ∗ (positive smooth comb) ≥ 0.
Consequence: e^{−tA^{conv}} preserves positivity and λ_min(𝔞_T|L²(I_T)) = C₀ − 𝒜_T + λ₁^{Dir}(ν_T; I_T), with ν_T
= ½K(|u|)du + ½Σ v_n(δ_{log n} + δ_{−log n}) and λ₁^{Dir} the survival exponent of the arithmetic Lévy process
killed upon exiting I_T (Feynman–Kac). The symbol of the form is "negative constant + Lévy–Khintchine exponent
with atoms at ±log n".
**(b) Escape.** Object nonlinear in the symbol (exponential), probabilistic, not a fixed basis.
**(c) First lemma.** Lemma 2 (done). The next step would be a lower bound of λ_A by Jensen:
λ_A ≥ −log‖Q e^{−A^{conv}}Q‖ (Hansen–Pedersen operator Jensen with f = e^{−x} − 1), or the family
λ_A ≥ c_T + [λ_min(Q(s_T − c_T)^pQ)]^{1/p}, p ∈ (0,1], c_T = C₀ − 𝒜_T.
**(d) Falsifier (kills it).** The Jensen loss at the minimizer is (∫X dμ)^p − ∫X^p dμ with X = s_T − c_T
of variance ≍ 𝒜_T² under μ = |ĥ*|²/2π (R186_018/101: positivity at h* is 94% cancellation between two
positives, not concentration): loss ≍ (1 − p)𝒜_T^p ≫ λ_A unless 1 − p ≲ λ_A/𝒜_T. NO-GO by the rule of §0.
What remains alive is only the structure (Lemma 2) and the reading "λ₀ = survival exponent", without a sign.
**(e) Check.** "Feynman–Kac" 0 files; "e^{−s_T}" 0; "Bessel I_k" only phase-4/114 in another context;
Metzler/Doob already in R160_C7 and phase 61 (cited, not repeated). What is new is the Bochner factorization with
a smooth comb and Bessel; its use for bounds is NO-GO.

### Idea 4 — Determinantal object (Szegő–Widom / Schur complement determinant)

Delegated to R186_034. Prior status to be respected: R164_502 L0 (s_T(0) < 0, strong Szegő not
applicable to s_T), L2 (via circular Szegő), L6 (Widom finite-section identity PROVED), L9 (Kreĭn index form).
Useful observation from Lemma 2: the **positive** symbol e^{−s_T} does admit Szegő/Kac–Akhiezer on the symbol,
but log σ = −s_T grows like −log τ and has Fourier atoms at ±log n (almost periodic): the term
∫u|ŝ(u)|²du diverges; and P e^{−s}P ≠ e^{−PsP}, so a determinant of e^{−s_T} does not decide that of s_T.

---

## 2. Lemma 1: proof

**Lemma 1.** Let F ∈ 𝒫_T, Φ = 𝒞_F (even, support [−2T, 2T]). Then
 𝔞_T(F) = (C₀ + 4)Φ(0) + 2∫₀^{2T}Φ(u)e^{u/2}du − Σ_{n<e^{2T}} v_nΦ(log n) + Lev_{K₁}(Φ),
and the two central terms are E_ψ(Φ) = 2∫₁^{e^{2T}} x^{−1/2}Φ(log x) d(x − ψ(x)).

*Proof.* By thm:A, 𝔞_T = C₀Φ(0) + Lev_K(Φ) − Σ v_nΦ(log n) and K = 2e^{−u/2} + K₁ with K₁ ≥ 0 (lem:K, series
of exponentials). Lev_{2e^{−u/2}}(Φ) = 4Φ(0) − 2∫₀^∞Φ(u)e^{−u/2}du. The primitive condition, in the form eq:Kprim of
thm:A, is ∫_ℝ Φ(u)cosh(u/2)du = 0; since Φ is even, ∫₀^∞Φ(u)(e^{u/2} + e^{−u/2})du = 0, so
∫₀^∞Φe^{−u/2} = −∫₀^∞Φe^{u/2}. Thus Lev_{2e^{−u/2}}(Φ) = 4Φ(0) + 2∫₀^{2T}Φ(u)e^{u/2}du. With x = e^u:
2∫₀^{2T}Φ(u)e^{u/2}du = 2∫₁^{e^{2T}}x^{−1/2}Φ(log x)dx and Σ v_nΦ(log n) = 2∫₁^{e^{2T}}x^{−1/2}Φ(log x)dψ(x)
(Λ(n) ≠ 0 ⟺ jump of ψ; Φ(2T) = 0 covers the boundary). ∎

**Remarks.**
1. Only **one** of the two Tate relations is used (the cosh one); the u·sinh one does not enter. The identity
 therefore holds on the larger class {∫Φcosh = 0}.
2. The constant −(C₀ + 4) = log π − ψ(¼) − 4 = 1.37218 is the only fixed arithmetic-archimedean number: it is the
 "price" of the pole after the exact cancellation of the first term of Γ.
3. E_ψ is linear in the measure d(x − ψ) (main term x minus primes) with kernel x^{−1/2}Φ(log x), which is
 positive definite in log x. In the primitive class, the entire comb of the window has turned into the Chebyshev
 error with weight x^{−1/2}, without invoking any bound on it (D-ψ is not used; no zero is used).

---

## 3. Numerical corollary: where the near-cancellation lives (NUMERICAL, script §4)

Legendre Galerkin N = 60 in x-space (as r024/r028; reproduces λ_A(½log3) = 9.47·10⁻⁴, λ_A(log2) = 1.01·10⁻⁷,
λ_A(½log5) = 3.4·10⁻¹², cf. R186_104). Identity residual at h*: ≤ 7·10⁻¹⁴ across the whole grid.

| T | λ_A | (C₀+4)‖h*‖² | E_ψ(h*) | Lev_{K₁}(h*) | E_exp(h*) | E_prime(h*) | inf_{𝒫_T}[(C₀+4)+Lev_{K₁}] |
|---|---|---|---|---|---|---|---|
| 0.36 | 4.78e-1 | −1.372 | −0.055 | 1.906 | −0.013 | −0.043 | +0.521 |
| 0.44 | 8.66e-2 | −1.372 | −0.255 | 1.714 | — | — | — |
| ½log3 | 9.47e-4 | −1.372 | −0.173 | 1.546 | −0.025 | −0.148 | +0.112 |
| 0.60 | 6.66e-5 | −1.372 | −0.147 | 1.519 | −0.026 | −0.121 | +0.028 |
| log 2 | 1.01e-7 | −1.372 | −0.116 | 1.488 | −0.028 | −0.088 | −0.108 |
| ½log5 | 3.4e-12 | −1.372 | −0.091 | 1.464 | −0.029 | −0.062 | −0.245 |

(E_exp = 2∫Φe^{u/2}, E_prime = −Σv_nΦ(log n); E_ψ = E_exp + E_prime.)

Reading:
1. **The arithmetic term is small and decreasing at the minimizer:** |E_ψ(h*)| drops from 0.25 (T ≈ 0.44) to
 0.09 (½log5). The near-cancellation of λ_A is between Lev_{K₁}(h*) (energy of the k ≥ 1 terms of Γ, ≈ 1.46) and
 the constant 1.372: Lev_{K₁}(h*) − 1.372‖h*‖² = 0.091 = |E_ψ(h*)| + λ_A at ½log5. In the identity, the
 "archimedean part" is the one that nearly vanishes; the comb enters as a 6% correction.
2. **The archimedean background without the term 2e^{−u/2} dies around T ≈ 0.62** (inf_{𝒫_T}[(C₀+4)Φ(0) + Lev_{K₁}] < 0
 afterward), but at h* it equals +0.09 > 0: the real minimizer is not where the archimedean background is minimal;
 the measure d(x − ψ) **pulls it away** from that direction (consistent with R186_021: prime 2 acts only through
 C at s₀). So E_ψ is strongly positive in the negative archimedean direction and slightly negative at
 h*: positivity is a balance between two functionals with different minimizers, not a dominance.
3. At h*, E_exp ≈ −0.03 is nearly zero: ∫₀^{2T}Φ_{h*}e^{u/2} ≈ −0.015, i.e. h* is almost orthogonal to e^{u/2} and
 to e^{−u/2} separately (not only to cosh): the minimizer tends to cancel the main term x of d(x − ψ)
 and leaves only −Σ v_nΦ(log n) ≈ −0.06.
4. The extremes of E_ψ over 𝒫_T are ±0.49 for T < ½log3 (= v₂/2 = Lemma ½ of R186_031, saturated) and
 [−1.21, +1.01] at ½log5: E_ψ is not small on the class, only at h*.

**What follows and what does not.** The inequality equivalent to D by window is
 (★₃₃) E_ψ(Φ) ≥ 1.37218·Φ(0) − Lev_{K₁}(Φ) for every Φ ∈ 𝒦_prim,
with right-hand side ≤ 0.245Φ(0) at ½log5 (and negative where Lev_{K₁} > 1.372Φ(0)). It is an exact reformulation:
it inherits the margin and does not touch the sign. What it contributes is the **correct hierarchy of the terms**:
(i) the pole and first term of Γ cancel exactly, leaving 1.372; (ii) the archimedean remainder K₁ ≥ 0 is the large
term; (iii) all the arithmetic is the measure d(x − ψ) with weight x^{−1/2}, which at the minimizer is 6% and
decreasing. Open question this raises (OPEN, not attacked here): does Lev_{K₁}(h*_T) − 1.372‖h*_T‖² → 0 and
E_ψ(h*_T) → 0 as T → ∞, and at what rate? If both tend to zero, Zhu's law (thm:margin) is a balance law between
K₁ and the pole, with the arithmetic as a lower-order term at h*; measuring it requires precision beyond doubling
(floor at T ≈ 0.85, R186_023/103) and is not done here.

---

## 4. Script

`r033_pnt_window_identity.py [N=60]`: builds Γ, Π_T, Lev_{K₁}, E_exp in an orthonormal Legendre basis
(Gauss quadrature in t and in u; ∫_{2T}^∞K₁ = τ(2T) − 4e^{−T}), extracts λ_A and h* by SVD of the Tate
restrictions, verifies the identity (residual), tabulates the three terms and tests the convexity of log λ_A in T, e^{2T},
e^{4T}, 𝒜_T. Time ≈ 5 min. The table-§3 values with inf_{𝒫_T} and E_exp/E_prime come from the same class
`Win` (session); all NUMERICAL.

---

## 5. Honest balance

- PROVED: Lemma 1 (PNT-window identity on {∫Φcosh = 0}); Lemma 2 (Bochner of e^{−s_T}, Feynman–Kac for λ₀).
- NO-GO: convexity of log λ_A (falsified numerically in T, e^{2T}, e^{4T}); scalar/operator Jensen bounds
 from Lemma 2 (O(1) loss against super-exponential margin).
- NUMERICAL: breakdown of §3; the near-cancellation at h* is Lev_{K₁} vs 1.372, with d(x − ψ) at 6% and decreasing.
- **No contact with the sign.** Nothing here decides any new window nor touches Paper 47, grid or crossword.
- Proposal for the next round (if wanted): study (★₃₃) as an inequality between two
 functionals with different minimizers: a lower bound of E_ψ on the cone where (C₀+4)Φ(0) + Lev_{K₁}(Φ) < 0
 (negative archimedean direction, low dimension up to ½log5 by R186_028 Thm 1.4), which is where the arithmetic
 must be positive with an O(1) margin, not super-exponential. It is the only stretch of (★₃₃) with a large margin.
