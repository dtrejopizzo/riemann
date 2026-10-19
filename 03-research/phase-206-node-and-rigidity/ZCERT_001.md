# ZCERT_001 — Certificate of the node from the zero side (phase 206)

**Nature of the work (mandatory statement).** This is **REF-D with CITED input** (verified zeros of ζ). It is not
a sign mechanism and contributes no new sign: it certifies, window by window and on a finite block, that the zero
form is positive on c^⊥ using that the low zeros are on the line (external datum, CITED) and that any hypothetical zeros off
the line sit at height > 3·10¹² (external datum, CITED). no
equivalence with other statements is used.

## Summary (≤250 words)

For the canonical even block E_N^ev(T) (k odd ≤ N(T) = ⌈2Tt₀/π⌉ − 1) and F ∈ E_N^ev ∩ c^⊥, identity (1.4) of
H1PLUS_001 gives 𝔄_ev(F) = Z_T(F) = Σ_ρ Φ_F(ρ)². I obtained the **closed form** Φ_k(z) = T^{−1/2}cos(zT)·2ω_k/(ω_k² − z²)
(z = −i(ρ−½)), which makes the whole computation elementary and gives, for zeros off the line, the bound
|Φ_F(ρ)|² ≤ ‖x‖²·(e^{T}/T)·Σ_k 4ω_k²/(γ² − ¼ − ω_max²)². With the first K = 2000 zeros computed **with arb**
(python-flint `acb.zeta_zeros`, rigorous ball arithmetic) and a Cholesky factorization **in ball arithmetic** of
M_on + L·ccᵀ − εI, I obtain rigorous lower bounds ε(T) for λ_min(Z_T|_{c^⊥∩E_N}). With H = 3·10¹² (Platt–Trudgian,
CITED) and N(t) ≤ (t/2π)log t (Trudgian, CITED), τ(T) ≤ 3·10⁻³⁴…10⁻³². **Theorem Z:** the node n₋(𝔄_N(T)) ≤ 1 holds at every
T of the grid {0.75, 0.76, …, 4.24, 4.245} (and trivially for T < 0.75, where c^⊥ ∩ E_N = 0); T*_grid = 4.245, right
before the jump N: 16 → 17 at T = 17π/2t₀ = 4.2457. From there μ_on falls below τ. The decay is **faster than
exponential**: log μ_N ≈ −10.7T − 5.9 T log T (local slope 22 → 28 per unit T between T = 2 and 8; linear fit
c ≈ 25.8), not 15.449. The 2N and 4N blocks decay much more (≈ 5 decades per mode) and show no floor at all: they do not
reproduce the "1e−70" of CALIB_R4. Labels: pointwise values PROVED (given arb + citations); "∀T ≤ T*" in the continuum:
ARGUED (grid of step 0.01, no rigorous Lipschitz bound; see §5).

## 0. Corpus check

- H1PLUS_001 (1.4): 𝔄_ev(F) = Z_T(F) − 2⟨F,χ_ev⟩², Z_T(F) := Σ_ρ Φ_F(ρ)², Φ_F(ρ) = ∫_{−T}^{T}F(x)e^{(ρ−½)x}dx. It is
  Σ_ρ Φ_F(ρ)² (not Σ|Φ_F|²); for ρ on the line and F even real, Φ_F(ρ) = ∫F cos(γx) ∈ ℝ, so each term is ≥ 0. For a
  quadruple off the line the terms have indefinite sign (Lemma 5 of AUDIT_207_001: signature (1,1)).
- **Normalization verified** against AUDIT_206_001: at T = ½log5, block {1,3}, F ⊥ c, 600 zeros give
  0.0018523604 (AUDIT: 0.00185236). With K = 2000: 0.0018523932 (AUDIT, from the prime side: 0.0018523954). That is,
  Z_T = 2Σ_{γ>0}Φ_F(γ)², with the factor 2 for ρ, ρ̄; it matches lem:roughEF / eq:W read in the even sector.
- P47 lem:combsine (basis e_k = T^{−1/2}sin(ω_k(x+T)), ω_k = πk/2T), rem:chiev-sine (c_k), lem:archcount (N(T)),
  cor:margin1 (4·10⁹Te^{−15.449T}, upper bound of λ_A over all of 𝒟), AUDIT_207 (H_N) OPEN.
- ROUTES-TRIED-INDEX: "numerical certificate via verified zeros" appears as a REF-D/CALIB-type reformulation
  (CALIB_R4/R5 from the prime side; thm:log5W at ½log5 with balls). There is no record of a closed bound τ(T) for the
  tail off the line nor of the closed form of Φ_k. Explicit new reason: the object changes (zero side with a rigorous
  one-sided bound instead of the prime side), and the goal is not a sign but measuring how far the verified data reach and
  answering (H_N) numerically. It is not presented as a closure route.

## 1. Closed form (PROVED, elementary)

For k odd, sin(ω_k(x+T)) = sin(ω_k x + πk/2) = s_k cos(ω_k x), s_k = (−1)^{(k−1)/2}. For z ∈ ℂ,

  ∫_{−T}^{T} cos(ω x) cos(z x) dx = sin((ω−z)T)/(ω−z) + sin((ω+z)T)/(ω+z),

and with ωT = πk/2: sin((ω∓z)T) = s_k cos(zT). Hence

  **Φ_k(ρ) = s_k² T^{−1/2} cos(zT)·2ω_k/(ω_k² − z²) = T^{−1/2} cos(zT)·2ω_k/(ω_k² − z²),  z := −i(ρ − ½) = γ − i(β−½).**

In particular c_k = Φ_k(1) (z = −i/2): c_k = T^{−1/2}·2ω_k cosh(T/2)/(ω_k² + ¼), matching rem:chiev-sine. The zeros
of the factor cos(zT) (z = π(2j+1)/2T) are the "nodes" of the whole family: this is the reason for the non-monotonicity in T (§4).

For F = Σ x_k e_k: Φ_F(ρ) = T^{−1/2}cos(zT)·Σ_k x_k·2ω_k/(ω_k² − z²), ‖F‖² = ‖x‖².

## 2. Decomposition Z_T = Z_on + Z_rest + Z_off

Let 𝒦 = {ρ_n = ½ + iγ_n : 1 ≤ n ≤ K} (γ_n > 0) and their conjugates.
- Z_on(F) = 2Σ_{n≤K} Φ_F(γ_n)² = xᵀM_on x, M_on(k,l) = 2Σ_n Φ_k(γ_n)Φ_l(γ_n).
- Z_rest: zeros on the line not listed (includes 0 < γ ≤ H, γ > γ_K): each term ≥ 0 ⇒ Z_rest ≥ 0. Discarded.
  (If a zero were multiple and listed only once, the omitted term is also ≥ 0.)
- Z_off: zeros with β ≠ ½. By Platt–Trudgian 2021 (CITED) all zeros with 0 < γ ≤ H = 3·10¹² are on the line,
  so Z_off only involves |γ| > H.

**Lemma Z.1 (PROVED).** For ρ = β + iγ, 0 < β < 1, |γ| > H ≥ ω_max+1:
|Φ_F(ρ)²| ≤ |Φ_F(ρ)|² ≤ ‖x‖²·(e^{T}/T)·Σ_k 4ω_k²/(γ² − ¼ − ω_max²)².
*Proof.* |cos(zT)| ≤ cosh(|β−½|T) ≤ e^{T/2}; |ω² − z²| ≥ |z|² − ω² ≥ γ² − ¼ − ω_max²; Cauchy–Schwarz in k. ∎
(No need to integrate by parts: the closed form already gives γ^{−2} decay per mode.)

**Lemma Z.2 (CITED + PROVED).** With N(t) ≤ (t/2π)log t for t ≥ H (Trudgian 2014, CITED; the explicit bound
(t/2π)log(t/2πe) + 0.112 log t + 0.278 log log t + 3.385 is less than (t/2π)log t for t ≥ 3·10¹²) and Stieltjes,
Σ_{γ>H} γ^{−4} ≤ ∫_H^∞ t^{−4}dN(t) ≤ 4∫_H^∞ N(t)t^{−5}dt ≤ (4/2π)(log H/(3H³) + 1/(9H³)).
Counting γ and −γ (factor 2) and the ratio (H²/(H² − ¼ − ω_max²))²:

  **|Z_off(F)| ≤ τ(T)‖x‖²,  τ(T) = (e^{T}/T)·Σ_{k≤N} 4ω_k² · 2·(4/2π)(log H/(3H³) + 1/(9H³))·(H²/(H²−¼−ω_max²))².**

Numerically τ(T) ≈ 1.9·10⁻³⁴ (T = ½log5) … 2.6·10⁻³³ (T = 4) … 1.4·10⁻³¹ (T = 8). Note: the absolute-value bound
on each term of a quadruple is legitimate (each term separately); no internal cancellation is used.

**Theorem Z (zero-side certificate of the node).** If ε(T) := rigorous lower bound for λ_min(M_on|_{c^⊥∩E_N}) satisfies
ε(T) > τ(T), then for F ∈ E_N^ev(T) ∩ c^⊥: 𝔄_N(F) = Z_T(F) ≥ (ε − τ)‖F‖² > 0, hence n₋(𝔄_N(T)) ≤ 1 (min–max,
codimension 1); with cor:H1minus, = 1.
*Proof.* (1.4) on c^⊥ (PROVED, H1PLUS_001) + Z_rest ≥ 0 + Lemma Z.1–Z.2. ∎

## 3. Rigor of the computation

- **Zeros:** `flint.acb.zeta_zeros(1,K)` (arb, Johansson; isolates and refines each zero with ball arithmetic and verifies
  the count). Radii ≤ 10⁻¹¹⁰. This is more than "mpmath at 40 digits": the γ_n are certified balls. Label:
  **CITED (arb/FLINT, verified implementation) + Platt–Trudgian** for being on the line.
- **Matrix:** M_on is assembled in balls at 300–2200 bits of precision (depending on T and block).
- **Compression to c^⊥ without loss of rigor:** if M_on + L·ccᵀ − εI ≻ 0 for some L > 0, then xᵀM_on x ≥ ε‖x‖²
  for x ⊥ c. Verified with Cholesky in balls (all pivots balls > 0), ε = 0.999·μ_num, L = 10²…10⁴⁸ ·tr/‖c‖².
  The "cert" column is that **certified** ε. μ_num (mpmath, Householder on c^⊥) is only used to choose ε.
- **Monotonicity in K:** each term is ≥ 0, so ε(K) increases with K; the convergence (table) is informative, not
  necessary for rigor.

## 4. Results

### 4.1 Main table (K = 500/1000/2000; "cert" = rigorous ε with K = 2000; τ with H = 3·10¹²)

| T | N | block | dim c^⊥ | μ_on (K=500) | μ_on (K=1000) | μ_on (K=2000) | ε cert | τ(T) | node |
|---|---|---|---|---|---|---|---|---|---|
| ½log5 | 3 | N | 1 | 1.852343e−3 | 1.852384e−3 | 1.852393e−3 | 1.8505e−3 | 1.9e−34 | PROVED |
| ½log5 | | 2N | 2 | 4.54514e−5 | 4.54551e−5 | 4.54559e−5 | 4.5410e−5 | 6.8e−34 | PROVED |
| ½log5 | | 4N | 5 | 1.15235e−8 | 1.15288e−8 | 1.15300e−8 | 1.1518e−8 | 5.5e−33 | PROVED |
| 1 | 4 | N | 1 | 8.22560e−4 | 8.22585e−4 | 8.22590e−4 | 8.2177e−4 | 1.2e−34 | PROVED |
| 1 | | 2N | 3 | 3.26652e−9 | 3.26713e−9 | 3.26726e−9 | 3.2640e−9 | 1.0e−33 | PROVED |
| 1 | | 4N | 7 | 7.8138e−14 | 7.8289e−14 | 7.8321e−14 | 7.8243e−14 | 8.3e−33 | PROVED |
| ½log15 | 5 | N | 2 | 1.96674e−6 | 1.96682e−6 | 1.96683e−6 | 1.9649e−6 | 2.5e−34 | PROVED |
| ½log15 | | 2N | 4 | 1.21237e−11 | 1.21285e−11 | 1.21295e−11 | 1.2117e−11 | 1.2e−33 | PROVED |
| ½log15 | | 4N | 9 | 1.70916e−21 | 1.71523e−21 | 1.71652e−21 | 1.7148e−21 | 9.4e−33 | PROVED |
| 2 | 8 | N | 3 | 1.71241e−11 | 1.71276e−11 | 1.71284e−11 | 1.7111e−11 | 3.5e−34 | PROVED |
| 2 | | 2N | 7 | 3.68723e−23 | 3.69525e−23 | 3.69695e−23 | 3.6933e−23 | 2.8e−33 | PROVED |
| 2 | | 4N | 15 | 3.537e−42 | 3.603e−42 | 3.618e−42 | 3.614e−42 | 2.3e−32 | not cert. |
| 2.5 | 10 | N | 4 | 5.02957e−16 | 5.03194e−16 | 5.03238e−16 | 5.0274e−16 | 5.8e−34 | PROVED |
| 2.5 | | 2N | 9 | 1.01098e−31 | 1.01550e−31 | 1.01636e−31 | 1.0153e−31 | 4.7e−33 | PROVED |
| 2.5 | | 4N | 19 | 5.017e−58 | 5.216e−58 | 5.259e−58 | 5.254e−58 | 3.8e−32 | not cert. |
| 3 | 12 | N | 5 | 7.12069e−21 | 7.12529e−21 | 7.12632e−21 | 7.1192e−21 | 9.6e−34 | PROVED |
| 3 | | 2N | 11 | 5.1996e−41 | 5.2334e−41 | 5.2414e−41 | 5.2361e−41 | 7.7e−33 | not cert. |
| 3 | | 4N | 23 | 4.011e−75 | 4.277e−75 | 4.354e−75 | 4.350e−75 | 6.2e−32 | not cert. |
| 4 | 16 | N | 7 | 1.43026e−31 | 1.43357e−31 | 1.43428e−31 | 1.4328e−31 | 2.6e−33 | PROVED |
| 4 | | 2N | 15 | 1.0149e−60 | 1.0389e−60 | 1.0446e−60 | 1.0435e−60 | 2.1e−32 | not cert. |
| 4 | | 4N | 31 | 1.911e−111 | 2.195e−111 | 2.281e−111 | 2.279e−111 | 1.7e−31 | not cert. |
| 5 | 20 | N | 9 | 5.40848e−43 | 5.43412e−43 | 5.43978e−43 | 5.4343e−43 | 7.1e−33 | not cert. |
| 5 | | 2N | 19 | 1.608e−81 | 1.679e−81 | 1.696e−81 | 1.695e−81 | 5.7e−32 | not cert. |
| 5 | | 4N | 39 | 5.25e−150 | 6.97e−150 | 7.54e−150 | 7.54e−150 | 4.6e−31 | not cert. |
| 6 | 24 | N | 11 | 3.23372e−54 | 3.25782e−54 | 3.26336e−54 | 3.2601e−54 | 1.9e−32 | not cert. |
| 6 | | 2N | 23 | 1.901e−103 | 2.036e−103 | 2.073e−103 | 2.071e−103 | 1.6e−31 | not cert. |
| 6 | | 4N | 47 | 7.20e−191 | 1.16e−190 | 1.33e−190 | 1.33e−190 | 1.2e−30 | not cert. |
| 8 | 32 | N | 15 | 1.11971e−78 | 1.14517e−78 | 1.15123e−78 | 1.1501e−78 | 1.4e−31 | not cert. |
| 8 | | 2N | 31 | 2.312e−149 | 2.711e−149 | 2.849e−149 | 2.846e−149 | 1.2e−30 | not cert. |

(8|4N was not completed: the cost of a ball Cholesky of dimension 63 at ~2200 bits in pure Python; not necessary.)
Key observation: **in every case ε cert > 0**, that is, the form truncated to the 2000 zeros is positive definite
on c^⊥ ∩ block, always. What fails for T ≥ 4.25 is not the positivity of Z_on but that its size falls below
the bound of what is not controlled (Z_off with H = 3·10¹²).

### 4.2 T* (canonical block)

Fine grid T = 0.75, 0.76, …, 4.30 (K = 500 is enough: truncation only lowers ε) — `finegrid.json`: certified at all
points with T ≤ 4.24 and at T = 4.245; fails at every point 4.25…4.30. The jump is structural: N(T) goes from 16 to 17
at T = 17π/(2t₀) = 4.24574…, mode k = 17 is added and μ falls from 3·10⁻³² to 1.4·10⁻³⁶ (≈ 4 decades per new mode),
below τ ≈ 2.5·10⁻³³. **T*_grid = 4.245.** There is non-monotonicity within the same N (e.g. T = 4.21: μ = 1.29·10⁻³²
versus 2.76·10⁻³² at 4.20 and 2.96·10⁻³² at 4.22), produced by the nodes of cos(γT) in Φ_k; with the first version of
τ (N(t) ≤ t log t, without 1/2π) that point failed: the margin is only a factor ≈ 5–10 near T*.

### 4.3 Decay rate: numerical answer to (H_N)

log μ_N(T) (canonical block, K = 2000): −24.8 (T=2), −46.4 (3), −71.0 (4), −96.0 (5), −123.2 (6), −179.2 (8).
Local slopes per unit T: 21.6, 24.6, 25.0, 27.2, 28.0 — **increasing**. Linear fit: c ≈ 25.8; fit
with a T log T term: log μ_N ≈ 5.0 − 10.7T − 5.9 T log T. Interpretation: μ_N falls faster than any fixed
e^{−cT}, approximately like e^{−a·dim·log(dim)} with dim ≈ T (≈ 4–5 decades per mode, growing slowly). It does not resemble
15.449: that exponent bounds λ_A **from above** over all of 𝒟 (cor:margin1) and is a different quantity; there is no conflict (μ_N ≥
μ_∞ and both can be ≪ e^{−15.449T}). Label: **NUMERICAL** (each value is a rigorous lower bound; the functional form
is a fit). For (H_N) this says: the rate of μ_N(T) is superexponential in T on the canonical block, with
μ_N(T) ≈ μ_on(T) to 10⁻³ relative (convergence in K), so the decay is not an artifact of truncation in K.

### 4.4 Blocks 2N, 4N and the "1e−70 floor"

At fixed T, doubling the block multiplies log μ by approximately 2 (½log15: 2.0e−6 → 1.2e−11 → 1.7e−21; T = 4:
1.4e−31 → 1.0e−60 → 2.3e−111). No floor appears: the minimum on c^⊥ keeps falling ≈ 5 decades per added mode,
without stabilizing. At ½log15 the 4N block (dim 9) reaches 1.7·10⁻²¹, far from 1e−70; extrapolating ≈ 2.4 decades per
mode at that T, 1e−70 would correspond to dim ≈ 30 (block ≈ 13N), not to 4N. Reading: the full form on c^⊥ is positive
but not uniformly so (infimum 0 in infinite dimension: the e_k with high k have Φ_k ~ γ^{−2}ω_k and the Gram matrix of nearly
collinear vectors degenerates); the "floor" of CALIB_R4 is then a property of its truncation, not an intrinsic floor.
NUMERICAL.

## 5. What is rigorous and what is not

| Statement | Label |
|---|---|
| Closed form of Φ_k(ρ), c_k = Φ_k(1), Lemma Z.1 | PROVED |
| Lemma Z.2 (tail) | PROVED given Trudgian 2014 (CITED) |
| Zeros on the line up to H = 3·10¹² | CITED (Platt–Trudgian 2021) |
| Position of the K = 2000 zeros used | CITED (arb/FLINT, certified balls) |
| Theorem Z (implication ε > τ ⇒ node) | PROVED |
| Node at every T of the grid 0.75:0.01:4.24 ∪ {4.245} and at the T's marked in the table | PROVED (given the CITED facts) |
| Trivial node for T < 0.75 (c^⊥ ∩ E_N = {0}, N ≤ 2) | PROVED |
| Node for **every** T ∈ (0, 4.2457) (continuum) | **ARGUED**: there is no rigorous Lipschitz bound; ∂_T M_on is O(1) while μ ~ 10⁻³², so a grid alone is not enough; ε with ball arithmetic over an interval of T would require width ~μ. OPEN as a continuum statement |
| Superexponential rate of μ_N, absence of a floor | NUMERICAL |
| Node for T > 4.2457 | OPEN (μ_on > 0 certified, but < τ) |

Contrast with what was requested: the zeros do not come from mpmath but from arb, so the pointwise values remain PROVED (with
citations) and not CONDITIONAL. The only non-rigorous piece of the "∀T ≤ T*" statement is the continuum in T.

## 6. Interpretation

- **What it certifies.** That the verified zero data (all on the line up to 3·10¹²) suffice to fix the inertia of the
  canonical block of 𝔄 up to T ≈ 4.25 (grid), with margin that runs out exactly at the jump N = 16 → 17. It is a
  rigorous-numerical extension of thm:log5W (½log5) up to ≈ 4.24, but **within the block**, not over all of 𝒟^ev.
- **What it does not certify.** Nothing about the full 𝒟^ev (the block is finite and the minimum on c^⊥ keeps falling without a
  floor as the block grows); nothing for T > 4.25; no mechanism: the sign is supplied by the datum "zeros on the line" (CITED), not by a
  structure. It is not a new sign and must not be sold as a closure route for D.
- **Relation to prop:H / RFIN_TRACT.** prop:H (even inertia over all windows) requires Z_T ⪰ 0 on all of c^⊥;
  here it is only verified on a finite subspace, which is the **necessary** condition of the finite reformulation of
  RFIN_TRACT (n₋(𝔄_N) = 1 on the block), not sufficient. The bottleneck is quantified: at fixed verified height
  H, the tail off the line is ~e^{T}T^{−1}·N·ω²·log H/H³ ≈ 10⁻³³, while μ_N(T) is superexponentially small;
  T* grows only like ~ log H / (slope ≈ 25) — tripling log H barely doubles T*. That is why no increase in verified height
  pushes the certificate far: the method is intrinsically local in T.
- **Useful input for (H_N):** evidence that μ_N(T) is not e^{−cT} but faster (increasing slope 22 → 28), which
  makes a lower bound of the form μ_N ≥ e^{−cT} with fixed c unlikely.

## 7. Entry for the index (ROUTES-TRIED-INDEX)

> **ZCERT (phase 206) — certificate of the node from the zero side (REF-D, CITED input).** Φ_k(ρ) in closed
> form T^{−1/2}cos(zT)2ω_k/(ω_k²−z²); 2000 arb zeros + ball Cholesky + off-line tail τ ≈ 10⁻³³
> (Platt–Trudgian H = 3·10¹², Trudgian N(t)). Node PROVED on grid T ≤ 4.245 (canonical block); continuum ARGUED; fails
> at the jump N = 17. μ_N(T) superexponential (slope 22→28), no floor in blocks 2N/4N. No mechanism; do not retry
> "extending T* with more verified height" (T* ~ log H/25).

## 8. Remark proposed for P47 (rem:zcert, after rem:finitesign)

Only with PROVED/CITED content; the continuum in T is deliberately omitted.

```latex
\begin{remark}[zero-side certificate of the even node; computed with cited inputs]\label{rem:zcert}
For odd $k$ the Dirichlet sines of Lemma~\ref{lem:combsine} have the closed transform
$\Phi_k(\rho)=T^{-1/2}\cos(zT)\,2\omega_k/(\omega_k^2-z^2)$, $z=-i(\rho-\tfrac12)$, so $c_k=\Phi_k(1)$
(Remark~\ref{rem:chiev-sine}). On $E_N^{\mathrm{ev}}(T)\cap c^\perp$ the even form equals the zero form
$\sum_\rho\Phi_F(\rho)^2$. Zeros on the critical line contribute nonnegatively; zeros off the line have
$|\gamma|>3\cdot10^{12}$ \cite{PlattTrudgian2021} and, by the closed form and the explicit $N(t)$ of
\cite{Trudgian2014}, contribute at most $\tau(T)\|F\|^2$ with $\tau(T)\le 3\cdot10^{-33}$ for $T\le 4.25$.
Using the first $2000$ zeros in ball arithmetic (Arb) and a ball Cholesky factorisation, the Gram
form is bounded below on $E_N^{\mathrm{ev}}(T)\cap c^\perp$ by $\varepsilon(T)>\tau(T)$ at every
$T\in\{0.75,0.76,\dots,4.24\}$; hence $n_-(\mathfrak A_N(T))=1$ at those $T$. The certified lower bound
decays faster than $e^{-cT}$ for any fixed $c$ in the range tested, and no lower floor appears when
the block is enlarged. This is a verification with cited inputs, not a mechanism.
\end{remark}
```
(Requires adding bibitems PlattTrudgian2021 and Trudgian2014 if not present; the editor must verify the remark against
def:W / eq:Aform and the N(T) convention of lem:archcount before integrating.)

## 9. Reproducibility

`ZCERT_001_data/`: `zcert.py` (table §4.1; `python3 zcert.py` or `python3 zcert.py 1` for the N block only),
`tstar.py` (T = 4.0…5.0), `finegrid.py` (grid 0.75…4.30), `post.py` (recomputes τ with the 1/2π version and the flags),
outputs `run.log`, `zcert_results.json`, `tstar.json`, `finegrid.json`, `edge.log` (T = 4.20…4.245, K = 500/2000; its
τ column is the old version, 2π times larger). Dependencies: python-flint 0.9.0, mpmath.
