# SYNTHESIS_MECHANISM_001 — the mechanism behind L′♯: a Hessian at a radical point, evaluated semiclassically

Phase 199, senior synthesis. Pen and paper. Three short computations were strictly necessary, to decide
labels: the overlap of Mori's vector with Pólya's kernel, the ladder ratios, and the weight 𝔴_μ. They were run in the
scratchpad on the shipped MORI15 data and are not stored in the repo. No
equivalence of any kind is invoked. No zero location is used. Zeros appear only as evaluation points in data already
recorded (MORI15, W_001).

Read in full: PATTERN_001, MECH_001, AUDIT_199, PROOF_L_SHARP_A…V (including W_001, filed during this synthesis),
MORI15_EXTREMAL_001, TEST_CG_001, AUDIT_L_SHARP_1…6.

**Outcome in one line.** L′♯ is NOT proved. I propose one mechanism, in three layers.
- **(M1) PROVED core.** The window value is the Hessian of the full-line Weil form at an exact radical point. Its first
  variation vanishes, so every O(1) piece cancels identically.
- **(M2) NUMÉRICO + ARGUED.** The radical point at the bottom is the prolate deformation of Riemann–Pólya's kernel
  Φ(u) = 2e^{u/2}Σ_n f_P(ne^u). The deformation turns the Gaussian truncation cost e^{−2πμ} into Slepian's e^{−4πμ}.
- **(M3) ARGUED, leading order, the proposed sign source.** On the exterior aliasing chirp the form diagonalises over
  dilates, with weight 𝔴_μ(ω) = Σ_{n≤ω} n^{−1}[Θ_∞(τ(ω)) − 2log n]. Here the leading log² terms of the archimedean and
  collapsed-prime parts cancel. The remainder satisfies 𝔴_μ ≥ log(2μ) > 0, and the minimum is attained exactly at the caustic.
- Corrections of relative size O(c^{−1/2}) remain, plus a rank-one edge channel.
- The leading-order constant is ≈ 2× too large against Mori's μ = 15 data. That mismatch is the first thing to explain.

Two new numerical facts are recorded (§1.4): Mori's vector is Pólya's kernel (overlap 0.99981), and W_T has a spectral
ladder on the self-dual prolate defects.

## 0. Corpus / index check, and why this is not a retry
- **Index searched:** ROUTES-TRIED-INDEX README l.449–469 (phase 199); `semiclass|WKB|chirp|Langer|stationary phase`;
  INV_S_001 (phase 195, exact WKB / resurgence of λ_A in 1/T, NO-GO 𝒦_St); K_001 §2 (Langer tail) and §3 (local symbol
  log(λu/n), ARGUED); R.4 / S.3 (per-harmonic weights log(k/t), ARGUED); S.4 (harmonics not decoupled, NO-GO 𝒦_S^{harm});
  E.5 / constraint 7 (ratio classes indefinite); W_001 (caustic t* ≈ 4πμ − (2k+1)/2, ARGUED); G7A-R165_101 (Riemann–Pólya
  kernel truncated to the window, used there as a witness, a different use); BB_001 (Euler–Lagrange at the minimiser;
  concavity in the comb weight); P46 class K (Pólya).
- **Why the proposal is new.** It differs from each recorded route as follows.
  - (a) INV_S_001 applies WKB to the *window* symbol in the large parameter T, and asks for a sign from Stokes data. Here the
    large parameter is c = 2πμ. The object is the *exterior* form (Λ-free after E.2), evaluated on the out-of-band
    continuation of the carrier datum, which is an explicit chirp. The sign is sought in a leading microlocal weight, not in
    Stokes data.
  - (b) K §3, R.4 and S.3–S.4 wrote local weights for **generic** or endpoint data (ρ(1) ≠ 0, dual harmonics). There the
    decoupling scale is log(l/k), independent of μ, and the cross terms are of diagonal size (S.4). On prolate-continuation
    chirps, dilates decouple at relative resolution 1/c, apart from the explicit resonant pairs (1,n) (§3.3). That changes
    the conclusion, not merely the wording.
  - (c) W_001 found the caustic as an *explanation* of t* and stopped at "the lower side is L′♯ itself". This memo turns
    the caustic into the minimiser of the leading lower weight (§3.4).
  - (d) Pólya's kernel is classical and already in the corpus. **Identifying it with Mori's certified bottom is new**
    (MORI15 did not test it).
  - (e) Everything rests on A_001 Thm 1.1, which is exact and Λ-exact. That is the non-TV-robust input.

## 1. Inventory

### 1.1 Exact identities (status after the audits)
| # | identity | where | label |
|---|---|---|---|
| I1 | **Half-line identity** W_T(g) = 𝒲_ext[Ψ_f] = −𝒲(g,Ψ_f), g = Ef\|_I, Ψ_f = Ef\|_{(−∞,−a)}, f(λ) = 0 | A Thm 1.1 (Guo 4.4–4.5) | PROVED |
| I2 | **Möbius bijection** E: L²[1/λ,λ] → L²(I), inverse Σμ(m)(mu)^{−½}g(log mu), norms ≤ 2√μ; gauge (−1/λ,1/λ) = radical; ℓ = dist²(r,𝒢̄) | MECH Prop 3.1, A Prop 2.1 | PROVED |
| I3 | **Universal form** 𝒲_ext[Zr] = λ^{−1}𝔔[ρ]: 𝔔 is one μ-free form on L²(1,∞); ρ ∈ PW_μ | F Prop F.0 | PROVED |
| I4 | **Critical-line form** 𝔔 = (1/2π)∫[Θ_∞\|F\|² − 2Re F̄F_log] + 2AB, F = ∫ρX^{−s}ζ_X(1−s); Θ_∞ = −2Re ζ′/ζ on the line | F Thm F.1 | PROVED |
| I5 | **R.1** Θ_∞\|F\|² − 2Re F̄F_log = \|ζ\|²∂_u\|Φ(s,w)/ζ(w)\|² at w = 1−s | R_001 | PROVED (REF-D) |
| I6 | **Remainder pairing** 𝒲_refl[u] = ∫e^{−t/2}(u∗u)dR_Λ; W_T(g) = ∫_0^∞e^{−t/2}(ǧ∗Ψ̌)(t)dR_Λ(t), R_Λ = ψ(e^t) − e^t + ½log(1−e^{−2t}) | V.2.1 | PROVED (REF-D) |
| I7 | **Mirror** Q(G,G) = −𝔔_line[c] + 2𝔅 − R(1)G_h(0) + c₀ρ₀² − 2ρ₀ρ₁ (Poisson self-duality + Re M′/M = Θ_∞) | AUDIT_4 §6 | PROVED on C_c^∞; CONDITIONAL on PW tails |
| I8 | **U.1 edge reflection** 𝔉_μ ↔ R_a; W_T = ΣL_j(ǧ)L_j(Ψ̌) + 𝒫(ǧ,Ψ̌) − A(ǧ)A(Ψ̌) | U_001, AUDIT_6 | PROVED (polarisation of I1) |
| I9 | **Comb collapse** −2Σc_q⟨Ψ̌,S_{log q}Ψ̌⟩ = −2⟨Zr,Z_log r⟩ (Λ∗1 = log) ⇒ 𝒲_ext is Λ-free | E Thm E.2 | PROVED |
| I10 | **P.1** 𝔔 = −Q(G,G) + 2Q(F,G) + 2AB. **P.2** the pole's F₀-piece is the s = 0 residue of the coupling | P_001, AUDIT_3 | PROVED (P.2 NUMÉRICO 1e−6) |
| I11 | **S.1 dual structure** G = ρ₀/s − conj F_c; the harmonics are dilates of one function | S_001 | PROVED |
| I12 | **J.1 kernels** prime part = Σlog(mn)J(m,n), J(m,n) = m^{−1}C_{n/m}(mλ); archimedean pairing of dilates = (mn)^{−½}c_r̃(log n/m) (polarised); Stieltjes form 𝒲_ext = ã-form − 2⟨H,𝒞H⟩ | J_001 | PROVED |
| I13 | Pole–Chebyshev cancellation (residue 1) | B L3.1 / E.4 | PROVED |
| I14 | Q.2 a_c = (1−c)Θ_∞\|ζ\|², a_1 ≡ 0 | Q_001 | PROVED |
| I15 | Deep quasi-mode 2(ξ′/ξ)(1)B_φ²e^D | J Thm J.3 | PROVED given PNT (outside PW) |
| I16 | Caustic of the dominant exterior prolate, t_c = min_ω ω√((c²ω²−χ_k)/(ω²−1)) ≈ 4πμ − (2k+1)/2 | W_001 | ARGUED, NUMÉRICO-consistent |

### 1.2 The 18 constraints (AUDIT_L_SHARP_1 §6.3, 2 §7, 3 §7, 4 §8, 5 §6, 6 §4)
1. Not TV-robust on the window. On the exterior carrier the comb is not a parameter, and only a polynomial relative margin exists.
2. Not identity + Bochner/C–S/Schur (N_018).
3. Not symbolic. The full-line on-line symbol vanishes, there is no Mellin-diagonal weight, and the off-line pairing is not a
   square. All of it is a truncation defect at ξ = nλ.
4. Not multiplier bounds, classwise SOS, Bochner on the Lévy part, "Son ≥ 0 + remainder", or uniformised certificates.
5. It must use a_n ≡ 1, residue 1, conductor 1 and lattice aliasing together. It must fail for cΛ, a_P, Beurling and F-DH.
6. Scale: quadratic in the leakage. The upper side is linear (Guo), so κμ^{−A}(1−χ_k) is forced at the bottom.
7. The semiring sits in the ratio classes, and cross-class cancellation is needed (built on E.5's deep-bump data).
8. There is no Hilbert matrix in the integer index. The archimedean dilate symbol is bounded and positive-definite, peaked at 1/μ.
9. Deep-mode value 0.046 (a consistency test only; outside PW).
10. The pole term couples the Q-null vector, so no block argument may ignore 2AB.
11. No flow or continuation argument works without an independent virial bound at relative precision 1/c.
12. No E-image of a single prolate with a small repair exists. The denominator must be dist²(ρ,𝒢̄₁).
13. The pole couples only through rank-one residues.
14. The harmonics are dilations of one function with forced coefficients. There is no per-harmonic sign.
15. (C_G)(b) is a mirror, not a reduction. The ℕ-constants are 𝔔[c]'s constants.
16. Sonin class versus PW: a transfer is needed (resolved structurally by U.2: the canonical gauge is the projection onto
    the Sonin annulus).
17. Gauge. Q(G,G) is unbounded on radical cosets, so a gauge must be fixed first.
18. A sector reduction is either the parity split or a NO-GO.

### 1.3 The certified extremal at μ = 15 (NUMÉRICO; MORI15, reproduced by AUDIT_6)
Basic data:
- Galerkin bottom 4.763·10⁻⁷⁰ (even) and 6.109·10⁻⁶⁶ (odd). The certified Schur margin is 2.40·10⁻⁷⁰.
- Even pieces: Γ_ℝ −5.3722, Lévy +3.9164, pole +1.5190, comb −0.0632 (n = 2: 99.0 %, n = 3: 1.0 %). These sum to 4.8·10⁻⁷⁰.
- The ã-form equals R_Λ, both −0.785800.

Prolate side:
- f* = 1.106ψ₀ − 1.822ψ₄ + 3.3·10⁻⁵ψ₈ + …, with a_{4j+2} ≤ 6·10⁻³⁸. The self-duality is parity, by co-Poisson (AUDIT_6).
- 1−λ₄ = 1.16682·10⁻⁷⁰, W/(1−λ₄) = 4.08, and a₄²(1−λ₄) = 3.87·10⁻⁷⁰.
- ℓ ∈ [4.4, 8.45]·10⁻⁷⁰, so κ_emp = W/ℓ ≥ 0.56 (the upper end 1.09 is ARGUED).
- The exterior datum ρ* is the continuation of ψ₄, with Langer phase and amplitude 10⁻³⁵.

Reflected pieces on ǧ*:
- A² = 2.9415280, 𝒫 = 2.9403889, ΣL_j² = 1.1391·10⁻³.
- Hence 𝒫 − A² = −ΣL_j² to 12 digits.

Zero check (evaluation only):
- |Fg*(γ)| ≤ 10⁻³⁸ below t* ≈ 185. There is a peak at n = 71–72 (γ ≈ 185.6) in both sectors, and a plateau ≈ 10⁻³⁶ above.
- Edge value J = g*(T) = −1.42·10⁻³⁴, and J²·Σ|ρ|⁻² = 4.66·10⁻⁷⁰.

### 1.4 Two new facts (NUMÉRICO; scratchpad, shipped data)
**N1. Mori's bottom vector is Riemann–Pólya's kernel.**
- Definition. Φ(u) := 2Σ_n(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}} = 2(Ef_P)(e^u), with f_P(v) = (2π²v⁴ − 3πv²)e^{−πv²}.
  This is the classical kernel whose cosine transform is Ξ.
- Overlap. Restricted to I = (−½log15, ½log15) and normalised, |⟨g*,Φ̂⟩| = 0.99981 and ‖g* + Φ̂‖² = 3.75·10⁻⁴. Pointwise:
  - x = 0: −1.598 against −1.580;
  - x = 0.2: −1.070 against −1.077;
  - x = 0.5: −0.0886 against −0.1063.
- Hermite form. f_P ∝ H₄ − 12H₀ at the scale v√(2π), so in normalised Hermite functions a₄/a₀ = −√384/12 = **−1.633**.
  Mori's prolate coefficients give **−1.6466**. The scale √c/λ = √(2π) is μ-independent.
- Autocorrelations. c_Φ(log2) = 0.0756 and c_Φ(log3) = 8.9·10⁻⁴, against g*'s 0.0638 and 4.9·10⁻⁴.
- Truncation cost. Φ's mass outside I is 1.16·10⁻³⁴ (the e^{−2πμ} scale).

**N2. Spectral ladder.** Using MORI15's eigenvalues and exact 1−λ_k (arithmetic):
- even sector: λ_j(W_T)/(1−λ_{4j}) = 4.082, 1.988, 1.793 for j = 1, 2, 3;
- odd sector: λ_j(W_T)/(1−λ_{4j+2}) = 3.026, 1.575 for j = 1, 2.

So the low spectrum of W_T is, within factors 1.5–4, the parity-matched prolate defect ladder at c = 2πμ. One index is
removed by f(0) = 0: index 0 in the even sector, index 2 in the odd sector. This corrects MORI15 §2, which compared steps
of 2, not 4. N2 is L′♯ with A = 0 *on the first three rungs*, and it gives the matching upper side.

## 2. What every failed route has in common, and what they all lack
**Common feature.** Each of A–W does one of three things to the *same* exact form, on an *unstructured* data class:
1. **Re-expresses** it by an identity (I1–I14: half-line, Mellin, pairs, Euler–Maclaurin, T+H, σ-derivative, mirror,
   sectors, remainder pairing). That gives REF-D, by N_018.
2. **Bounds** it uniformly over a class containing falsifiers or radical directions (TV, Schur, multipliers, Bochner,
   Carleson). That is excluded by constraints 1, 2 and 4, or broken by the gauge (17).
3. **Flows** it (H). That needs a virial at the minimiser (11).

Every evaluation that produced a *number* did so on data **outside** the regime where the bottom lives:
- deep bumps (J.3, E.5, F.4);
- endpoint data with ρ(1) ≠ 0 (S.3–S.4);
- radical vectors (TEST_CG §4);
- Sonin-class data (T).

None of these is the near-bottom carrier datum.

**The missing structural feature: the large parameter.** Near the bottom, every carrier datum has the same rigid shape:
- in the window, a prolate deformation of Pólya's kernel (N1);
- outside, an aliasing chirp of phase ≈ c√(ω²−1), with c = 2πμ (K.2, MORI15 §2, W_001).

So ħ = 1/c is a small parameter *carried by the data*. In it the exterior form stops being a global, symbol-null object and
becomes **local in phase space**. No route used that parameter. The exact routes cannot use it, because they are identities.
The robust routes cannot use it, because they quantify over classes that contain non-chirps.

The mechanism therefore has to be an **asymptotic evaluation** with three properties:
- it is not an identity (so it escapes constraint 2);
- it is not a bound over a class (so it escapes constraint 4);
- it is built on top of the Λ-exact reduction I1 (so it escapes constraint 1).

## 3. The mechanism

### 3.1 (M1) Why three O(1) pieces must cancel: the window value is a Hessian at a radical point (PROVED)
Take admissible f with f(0) = f̂(0) = 0. Then Φ_f = Ef satisfies WΦ_f = 0 a.e. on ℝ (Guo 4.4).
- Mellin side: ζ(s)f̃(s) = ζ·(entire, vanishing at s = 1).
- The proof is Riemann's 1859 theta-function argument: Poisson summation for a_n ≡ 1, residue 1 and Γ_ℝ with conductor 1.

So Φ_f is a **critical point** of the full-line form 𝒲, with value 0 and gradient 0. For g = Φ_f|_I and Ψ = Φ_f − g:
  W_T(g) = 𝒲(Φ_f − Ψ) = 𝒲(Φ_f) − 2𝒲(Φ_f,Ψ) + 𝒲(Ψ) = 𝒲(Ψ).
This is I1 read as a Taylor expansion. **The window value is exactly the Hessian of 𝒲 at a radical point, in the
truncation direction.**

Every O(1) piece (Γ_ℝ, Lévy, pole, comb) cancels because the zeroth- and first-order terms vanish identically. That
cancellation is forced by the four Λ-ingredients acting together. It is not a numerical accident. On g* this is visible as
𝒫 − A² + ΣL_j² ≈ 0 to the double-precision floor (V.4), and as the four-piece sum 0 (MORI15 §3).

**Hessian in the comb weights (answers "is there a role for the second-order structure").** Two separate facts:
- The comb-weight Hessian of λ_min is ≤ 0. This is concavity (BB_001), −2Σ_j|⟨g_j,∂C g*⟩|²/(λ_j − λ₁). With the ladder
  gaps of N2 (λ₂/λ₁ ≈ 10⁸) it measures the TV needle (constraint 1). It is a barrier, not a sign source.
- The relevant second-order object is the **state-space** Hessian 𝒲(Ψ) above. It is quadratic in the out-of-band datum r.

### 3.2 (M2) The scale: a prolate deformation of Pólya's kernel (NUMÉRICO + ARGUED)
By N1, the bulk of the extremal is Φ = E f_P (Riemann–Pólya), a μ-independent radical vector.
- **Pólya's kernel itself.** f_P is Gaussian-concentrated, so its truncation costs |Φ|² beyond T, about 10⁻³⁴ (e^{−2πμ}
  scale). It is not the bottom.
- **The bottom.** It replaces the Hermite pair (h₀, h₄) by the prolate pair (ψ₀, ψ₄) at c = 2πμ. The combination is fixed
  by f(0) = 0, and f̂(0) = 0 follows from self-duality up to O(1−λ). Slepian's optimal concentration squares the Gaussian
  cost: ℓ ≍ a₄²(1−λ₄(2πμ)) ~ μ^{9/2}e^{−4πμ}.
- **Why e^{−4πμ} is forced.** (M1) makes W quadratic in r, and the minimal r over self-dual f with f(0) = 0 is the ψ₄
  continuation.

This answers "why is the comb 99 % n = 2":
- the bulk is Pólya's kernel, a fixed shape with doubly-exponential decay, so c_g(log q) dies super-exponentially in q;
- the comb's role in the O(1) cancellation belongs to the first contact by shape;
- the contacts 11 and 13 are 10⁻³² of it.

The O(1) balance is the full-line radicality of a fixed vector. So it is **not local at the first contact**. The contact
2 is simply the only lag inside the support of the autocorrelation. Prediction (testable): the n = 2 share stays ≈ 99 %
for every μ. The bulk converges to Φ as μ → ∞, and only the tails change.

### 3.3 (M3) The sign: semiclassical dilate calculus on the exterior chirp (ARGUED, leading order)
Setting:
- Let r(ξ) = f̂(ξ) on ξ > λ, with ω = ξ/λ.
- For f in the concentrated prolate span (index below the plunge, k ≤ 2c/π − C log c), r is a sum of Langer/WKB waves
  sharing the leading phase cS(ω), S = √(ω²−1), with slowly varying amplitudes (CITED Dunster, uniform asymptotics).
  Their |r|² density is ∝ 1/(ω√(ω²−1)).
- In the log variable, every dilate n of Ψ̌ = Σ_n n^{−½}r̃(·+log n)1_{(a,∞)} has local Mellin frequency τ(ω) = cω²/√(ω²−1)
  at the point where it samples ω. Dilation is translation in log. Dilate n samples only ω ≥ n, which is the truncation at
  the window edge: **the n ≈ λ/u boundary**.

Stationary-phase consequences:
1. **Pairs.** Two dilates (m,n), m ≠ n, have coincident local frequency only at resonant pairs (1,n). There
   ω₁ = √(1+n⁻²) on the edge branch of dilate 1 and ω_n = √(n²+1), at frequency c(n+1/n). For m, n ≥ 2 both sit on the
   increasing branch, so there is no stationary point. The resonant cross terms are of size c^{−½}n^{−2}log(μn) (ARGUED;
   Fresnel width (cn³)^{−½}, amplitudes n^{½}·n^{−1}). Their total is O(c^{−½}) ≈ 10 % at μ = 15, which is the size of the
   contact sawtooth (PATTERN_001, 8–15 %).
2. **Archimedean part.** On a WKB wave, Θ_∞(D) acts as multiplication by Θ_∞(τ(ω)) = log(μω²/√(ω²−1)) + O(τ^{−2}).
   Conductor 1 enters here: the 2π of Γ_ℝ against c = 2πμ.
3. **Prime part.** After the collapse (I9, a_n ≡ 1, Λ∗1 = log) the prime part is diagonal with weight 2log n on dilate n,
   plus the resonant pairs.
4. **The leading form.** It is a weighted L² norm of r:
     𝒲_ext[Zr] = ∫_1^∞ 𝔴_μ(ω)|r(λω)|²λdω·(1 + O(c^{−½}log c)) + (edge channel, §3.5),
     **𝔴_μ(ω) := Σ_{n≤ω} n^{−1}[log(μω²/(n²√(ω²−1)))] = H(ω)·log(μω²/√(ω²−1)) − 2H₁(ω)**,
   with H(ω) = Σ_{n≤ω}1/n and H₁(ω) = Σ_{n≤ω}(log n)/n. This is E.1′'s harmonic cut, now one-variable and evaluated.

**Why 𝔴 > 0: the cancellation of three O(1) quantities, at the level of the sign.**
- For large ω, H ≈ log ω + γ and 2H₁ ≈ log²ω + 2γ₁.
- The **log² terms cancel**: archimedean log(μω)·log ω against prime log²ω. This is the vanishing full-line symbol
  (constraint 3) seen locally.
- What survives is log μ·log ω + γ log(μω) − 2γ₁ > 0 (with −2γ₁ = +0.146).
- **The survivor is a truncation effect.** The archimedean frequency of the depth-ω sample is μω, not ω. The factor μ is
  the window's band, and it appears only because the dilate is cut at ξ = nλ.

Computed exactly (NUMÉRICO, quadrature of the explicit sum; ω ∈ [1, 10⁵]):
  **min_ω 𝔴_μ(ω) = log(2μ) for every μ ≥ 2, attained at ω = √2.**
- ω = √2 is exactly the caustic: τ(√2) = 2c = 4πμ.
- For ω ∈ (1,2) one has H = 1, and 𝔴 = log(μω²/√(ω²−1)) ≥ log 2μ.
- For ω ≥ 2, the dilates n ≥ 2 only *raise* the weight above log 2μ.
- For μ = 1 the minimum is 0.56, at ω = 2.

**Leading-order coercivity (conjectural, no polynomial loss):**
  𝒲_ext[Zr] ≥ (log(2μ) − O(c^{−½}log c))·∫_λ^∞|r|²dξ = ½(log 2μ − o(1))·leak.

For the ψ₄-chirp mass distribution the leading value is ½D(μ)·leak, with D(μ) = ∫𝔴_μ dm, m = (2/π)dω/(ω√(ω²−1)):
- D = 3.49, 3.97, 4.48, 5.05, 5.46, 6.76 at μ = 5, 7, 10, 15, 20, 50 (NUMÉRICO);
- the n = 1 term is exactly log 4μ.

### 3.4 Answers to the specific questions
**(a) Why the first ≈ 70 zeros are "killed" (t*).**
- It is not a count of degrees of freedom. The checks:
  - local density crossing (1/2π)log(t/2π) = T/π gives t = 2πμ = 94;
  - cumulative crossing gives 2πeμ = 256;
  - N(2c) = 72.9 against Tt/π = 81.2 at t = 2c.
  W_001 reached the same conclusion.
- It is the caustic t_c ≈ 4πμ − (2k+1)/2 (W_001). The mechanism is the identity Φ_g(ρ) = −Φ_ℓ(ρ) (C_001).
- The prime-side statement asked for is this. Ψ̌ has no Mellin spectrum below t_c, up to Airy-dark terms. W is a full-line
  convolution, so the comb is a sum of translations (a multiplier). Hence **the full-line Weil residual Wg = −WΨ, computed
  by the explicit prime sum, is high-pass at t_c**. Equivalently: in the band |τ| < t_c, g is an eigenfunction of the comb
  operator with eigen-symbol Θ_∞ plus the pole, to the precision of the tail.
- N1 makes this concrete. The bulk transform Fg* ≈ −Ξ(t)/‖Φ‖, and Ξ vanishes where ζ(½+it) does, by its definition.
- The new point of (M3) is that the caustic is also **where the lower weight is smallest**: min 𝔴 = 𝔴(√2) = log 2μ.
  The caustic is the bottleneck of the sign, not only the edge of the killed zeros.

**(b) Why κ_emp ≈ 1 (no polynomial loss).** Both sides of L′♯ are quadratic in the same chirp r:
- the leakage is ∫|r|²;
- the form, by (M1), is ∫𝔴|r|²;
- 𝔴 ∈ [log 2μ, O(log²)] on the chirp's mass.

So W/ℓ is a ratio of two weighted norms of one function, and it is O(1)·log μ. In the window picture this is N2: the
spectrum of W_T tracks the leakage ladder rung by rung, with O(1) ratios.

**Quantitative mismatch (honest).**
- Leading order predicts W/leak ≈ ½D(15) = 2.53, with lower bound ½log 30 = 1.70.
- The data give W/(a₄²(1−λ₄)) = 1.23 and κ_emp ≥ 0.56.
- The prediction is high by a factor of 1.4–4.5. Resonances, at about 10 %, do not account for it.
- The leading candidate is the **edge channel**. g* is not in the core: J = g*(T) ≠ 0, so f*(λ) ≈ J/√λ ≈ 7·10⁻³⁵ ~ √ℓ.
  A_001 Rem 1.1(iv) adds a rank-one block f(λ)²W_T(h_p) + 2f(λ)Re⟨h_p,XΨ_v⟩ to W and a jump term to ℓ. MORI15's
  "coincidence" J²Σ|ρ|⁻² = 4.66·10⁻⁷⁰ ≈ W says the edge channel is of leading order. The model must include it as a
  2×2 (chirp, edge) block (Lemma S3).
- The growth also disagrees. Mori V's Galerkin ratio rises by 16 % from μ = 7 to 20, while D rises by 38 %. This is the
  second check.

## 4. The proposed lemma chain (conjectural), with what each step needs
- **S0 (reduction; PROVED).** W_T(Ef) = 𝒲_ext[Zr_f] = Hessian at the radical point (I1, I9, §3.1). Needs Guo 4.3–4.4
  (CITED). It is Λ-exact: the step fails for cΛ, a_P and Beurling (A §6, C Prop 5.1).
- **S1 (canonical gauge and regimes; PROVED + OPEN).**
  - PROVED: ℓ = λ‖Πρ‖², with Π the projection onto the Sonin annulus (U.2).
  - Split Πρ = r_♯ + r_♭: r_♯ in the concentrated prolate span (k ≤ 2c/π − C log c), r_♭ the plunge and bulk.
  - OPEN: an "almost orthogonality" of the split for 𝒲_ext. Gauge vectors (1−P)φ̂ have Mellin frequency ≲ 2πω. Chirps sit
    at ≥ t_c ≈ 2c. The bulk sits at ≳ c (the plunge turning point moves t_c from 2c down to c). So all three are
    microlocally separated at scale c. Needs an Egorov/microlocal partition for Mellin–dilation operators (standard
    tools; not yet written).
- **S2 (semiclassical evaluation; the first theorem, §6).** For r_♯ in the concentrated span:
    𝒲_ext[Zr_♯] = ∫𝔴_μ|r_♯|² + E_res + E_edge + O(c^{−1}log²c)‖r_♯‖².
  Here |E_res| ≤ Cc^{−½}log μ·‖r_♯‖² (resonant pairs (1,n)), and E_edge is the boundary contribution of the dilate
  truncations at ω = n. Their jumps sum to Ψ̌(a⁺) = g(−T), which is 0 on the core. Needs:
  - uniform Langer asymptotics of prolate continuations (CITED Dunster; uniformity in k up to the plunge to be checked);
  - stationary phase with an explicit remainder;
  - the elementary lower bound min 𝔴_μ = log 2μ (to be PROVED; NUMÉRICO now).
  All are Λ-free after S0.
- **S3 (edge channel; OPEN, finite).** For data with f(λ) ≠ 0 (the closure of the core in the form norm), the
  (chirp, edge) block is 2×2:
    W = 𝒲_ext[Zr_v] + 2f(λ)Re⟨h_p,XΨ_v⟩ + f(λ)²W_T(h_p).
  It must be PD with an O(1) constant relative to (‖r‖², f(λ)²/λ). This is a 2×2 determinant of explicit semiclassical
  quantities. It is the step that must account for the factor ≈ 2 in §3.4(b).
- **S4 (bulk block; OPEN, polynomial margin).** On r_♭ (plunge and beyond, leak ≍ ‖g‖²·poly), prove
  W_T ≥ κμ^{−A}‖g‖². The margin is polynomial, so **TV-robust tools are not excluded here**: the barrier of constraint 1
  bounds the slack by λ_min of the *restricted* block, which is polynomial, and not by e^{−4πμ}. Candidates: Lemma 4.1 of
  A (high frequency) plus the plunge structure.
  - **F-DH must fail here.** The leading weight for DH is (4/5)log μ′·log ω > 0 as well: χ(n) has |χ| = 1 off 5ℤ,
    conductor 5, and no pole. So the DH negativity at 9/5 must sit in the bulk or edge regime. Decisive test: is DH's
    first negative vector a chirp (falsifies M3) or a bulk vector (consistent)?
- **S5 (assembly).** If S1's cross terms are ≤ (1−ε)√(diag·diag) and S2–S4 hold, then L′♯ holds with A = A_bulk and
  κ ≥ min(½log 2μ − o(1), κ_edge, κ_bulk). In the concentrated regime there is no loss, matching N2.

**Compliance.**
- Constraints 1, 2, 3, 5, 6, 8, 10, 12, 13, 16, 17 and 18 are respected, by construction or explicitly.
- Constraint 4: the decisive step is an asymptotic evaluation, not a bound.
- **Tension with constraint 7**, and with S.4 / constraint 14:
  - (M3)'s positivity sits in the *diagonal* dilate class (1,1), with the cross classes O(c^{−½}).
  - Constraint 7 and E.5 rest on deep-bump data, which are radical for PW (J §4.1). S.4 rests on endpoint data, whose
    decoupling scale is μ-free.
  - For chirps the claim is that the decoupling is at 1/c. This is the first thing that must be checked.
  - If true, constraint 7 must be restricted to C_c^∞ data.
- Constraint 15 (ℕ-constants are mirror constants): the leading positive term here is log μ·H(ω) (the archimedean band).
  The γ and γ₁ are subleading, so this is not S.5's source.
- Constraint 11: no flow is used.
- Constraint 9: the deep mode is outside the chirp regime, so there is nothing to reproduce.

## 5. Plausibility ranking (honest)
| step | content | plausibility | why |
|---|---|---|---|
| S0 | exact reduction | done | PROVED |
| N1/N2 | Pólya bulk, ladder | high (data) | NUMÉRICO, one μ only |
| S2 | leading weight 𝔴 ≥ log 2μ on chirps | medium–high | standard semiclassics; weight positivity elementary; but leading constant is 1.4–4.5× off at μ = 15 |
| S3 | edge 2×2 block PD | medium | finite and explicit, but it is exactly where the data disagree with S2 alone |
| S1 | microlocal separation of gauge / chirp / bulk | medium | frequency scales 2πω, c, 2c are separated, but Z is not L²-bounded (C 4.2) and the plunge is a transition region of width log c |
| S4 | bulk block, polynomial margin | low–medium | no tool yet; it is where every falsifier must die; robust tools are allowed in principle |
| overall L′♯ by this chain | | low (≈ 10–15 %), but it is the first chain whose decisive steps are an asymptotic evaluation plus a finite block plus a polynomial-margin problem, and not a restatement | |

## 6. The first step that can be attempted as a theorem
**Theorem target T1 (semiclassical value on the prolate–Pólya family; unconditional, zero-free).** Let f_μ be the
normalised element of span{ψ₀,ψ₄,ψ₈}(c = 2πμ) with f(0) = f̂(0) = 0 and f(λ) = 0, the core version. Then
  W_T(Ef_μ) = ½·D₄(μ)·leak(f_μ)·(1 + O(c^{−½}log c)),  D₄(μ) = ∫_1^∞𝔴_μ(ω)m₄(ω)dω ≥ log 2μ,
with m₄ the normalised Langer mass of ψ₄'s continuation.

Corollaries, if proved:
- (i) λ^W_T ≤ C·μ^{9/2}log μ·e^{−4πμ} for all μ ≥ μ₀, **without zero data**. Mori's Thm K uses RH verified to 3·10¹²
  plus a zero-free region. This is a genuine upper-side improvement.
- (ii) The first PROVED instance that the radical Hessian is positive with no polynomial loss along the extremal direction.

T1 needs only:
- S0, which is exact;
- Langer asymptotics, CITED;
- stationary phase for the explicit Λ-free form E.3.

Prerequisite check (NUMÉRICO, cheap, no Mori matrices). Evaluate 𝒲_ext[Zr] directly for r = ψ̂₄|_{(λ,∞)} at μ = 10, 15,
20, 30. The exterior form is Λ-free and one-dimensional. Compare with ½D₄(μ). If the ratio does not tend to 1, (M3) is
wrong at leading order, and this route stops. If it does, the factor ≈ 2 at the extremal is the edge channel (S3).

## 7. Labels, residuals, do-not-retry
- **PROVED:** §3.1 (Hessian reading of I1, first variation 0); the inventory items as labelled in §1.1.
- **NUMÉRICO:**
  - N1: overlap 0.99981, a₄/a₀ −1.633 vs −1.6466, c_Φ(log 2) = 0.0756;
  - N2: ladder ratios 4.08, 1.99, 1.79 / 3.03, 1.57;
  - min 𝔴_μ = log 2μ at ω = √2 (μ ≥ 2);
  - D(μ) table.
- **ARGUED:**
  - (M2) prolate deformation;
  - (M3) leading form ∫𝔴|r|², the resonance sizes O(c^{−½}), the n = 2 prediction for all μ;
  - the edge channel as the cause of the factor ≈ 2.
- **OPEN:** S1–S5, T1, L′♯, (★★). No sign is claimed. Row D OPEN.
- **Do not retry:**
  - per-dilate or per-harmonic weights on *generic* (non-chirp) data (S.3/S.4 stand there);
  - Pólya's kernel itself as a near-extremal (its truncation cost is e^{−2πμ}, not e^{−4πμ});
  - degree-of-freedom counts for t* (W_001).
