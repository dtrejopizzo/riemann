# F0_TEST_001 — Test F₀ of candidate (f) at the Mori extremal μ = 15 (phase 200, round 4; NUMERICAL)

Numerical verifier. Every number in this memo is
**NUMERICAL**. Scripts and data: `F0_TEST_001_data/` (step1_*: window; step2: exterior datum; step3/4: F(ε); step5: gauge).
Units: the quadratic exterior quantities are given in 10⁻⁷⁰.

**One-line result.** F″_{r*}(0) ≈ +18.3 (X = 240; extrapolated ≈ 19.3) > 0, F is convex on the whole grid
[−0.045, 0.245], F″(0)/ℓ* ∈ [2.1, 4.4]. Lemma F **passes** at the extremal with margin ≍ ℓ*. But the memo's
prediction (dominance of ⟨h₁,h₂⟩) is **false**: ⟨h₁,h₂⟩ = −1.32 < 0, and F″ is spread over the diagonal (log n)²‖h_n‖² of many n.

## 0. Conventions and corpus
- Conventions from MORI15_EXTREMAL_001: λ = √15, T = ½log15, Legendre basis of 832 even modes, Möbius inverse f₁ on
  [1/λ, λ] and minimum-leakage gauge M = 28 with φ(0) = 0 and ∫f = 0. Also: 81 prolate functions with c = 30π, 𝓕f(ξ) = ∫f e^{−2πixξ},
  ρ(ω) = r*(λω).
- Paper 47 §22 (def:ext, thm:ext-half, rem:ext-killing, prop:ext-gauge), with 𝒜[Ψ] = b_∞c(0) + 2∫₀^∞(c(0) − c(v))ν(v)dv,
  b_∞ = ψ(¼) − logπ and ν = e^{−v/2}/(1 − e^{−2v}).
- Not a retry: it is the execution of the test requested in A_MU_FACTORIZATION_001 §3/§7, which was not run there.

## 1. Step 1 — reproduction of W* and of the pieces (window)
Independent recomputation in arb (420 bits) from the 120-digit vector (p0_eig.json).
- Fg was obtained via a spherical Bessel series (Miller), with 190 GL panels on [0, 736]. Converges between NQ = 80 and NQ = 110 to
  10⁻⁹⁰.
- Pole and comb were computed with 1700-node GL, exact for the polynomial products.

| piece | value | memo |
|---|---|---|
| arch_Ω | −1.455794761161863487215329988648217560306628148266851965424154… | matches to 60 digits |
| pole 2AB | 1.518998531269458092304876249077067764367997435… | ✓ |
| comb | 0.063203770107594605089546260428850204061369287127720882950176… | ✓ (60 digits) |
| γ(1 − band_Ω) | 1.01817·10⁻⁷⁰ | — |
| **Q = arch_Ω + γ(1−band) + pole − comb** | **4.76314·10⁻⁷⁰** | W* = 4.76347·10⁻⁷⁰ |

- **W* is reproduced.** The O(1) pieces cancel to 74 digits. The residual is 3.2·10⁻⁷⁴ (relative 7·10⁻⁵),
  attributable to Mori's internal discretization of J.
- Window pieces Γ_ℝ −5.3722, Lévy +3.9164, pole +1.5190 and primes −0.0632: reproduced, because arch_Ω = Γ_ℝ + Lévy.
- **Value of the true form** (without Galerkin compression): W_T(g*) = Q − γ(1 − band) + (1/π)∫_{736}^∞ a|Fg|².
  - Tail on [736, 8736]: 1.1143·10⁻⁷⁰.
  - Tail beyond 8736: 0.1187·10⁻⁷⁰, with t²|Fg|²/π stable at 1.2557·10⁻⁶⁸ from t ≈ 2700.
  - Total: **W_T(g*) = 4.978·10⁻⁷⁰**. That is the value the exterior form must reproduce; W* does not.

## 2. Step 2 — exterior datum r* and consistency of Theorem D
- **Gauge.** Recomputed at 70 digits with dense nodes. With 300 nodes per cell, a_k, β and the leakage
  8.4467·10⁻⁷⁰ of the memo are reproduced exactly.
- **Side finding (minor correction to MORI15).** 300 nodes per cell do not resolve the floor modes of g*. The ρ*
  values from MORI15 have errors of 0.1–1% (e.g. ρ(1.5) = −8.054 against −8.126·10⁻³⁶).
- **Leakage via direct Parseval** (‖f‖² − ∫_{|ξ|<λ}|𝓕f|², 400 bits): **ℓ(f*) = 8.6018·10⁻⁷⁰** in the minimum-leakage gauge.
  This is somewhat larger than the memo's prolate bound of 8.44.
- **Computation of ρ.** ρ(ω) was computed at 256 bits from f* at 400 bits, with dense GL nodes (10.7k and 22.6k). It is stable to 30
  digits as the node count is varied. Grids: caustic layer ω ∈ [1, 2] in σ = √(ω−1), [2, 60] with Δ = 0.0025 and
  [60, 240] with Δ = 0.004.
- **Decay.** ρ decays only like ≈ 1.2/ω (rms·ω ≈ 1.1–1.3 up to ω = 240). The cause is that g*(T) = −1.42·10⁻³⁴ ≠ 0, so
  f* has jumps μ(m)g*(T)/√λ at u = λ/m and **r* is not admissible** (it is not O(ξ⁻²)). The energy for ω ≤ 240 is 8.38,
  against 8.60 total.
- **Precision.** With ρ×10³⁵ there is no 70-digit cancellation in exterior coordinates: all pieces are O(ℓ). Double
  precision suffices after the high-precision reconstruction.
- **Theorem D on admissible data (step5).** For two pure gauge elements φ ∈ 𝒢_T, smooth and in the radical,
  𝒜 + 2AB − F′(0) = 0 with relative error ≤ 4.6·10⁻¹⁰. This confirms thm:ext-half and Theorem D in the pipeline.
  - Theorem D is a literal restatement of thm:ext-half: F′(0) = 2⟨Zr, Z_log r⟩.
  - At those φ, F″_φ(0) = 5.2·10⁻⁷ and 1.1·10⁻⁵, both > 0.
- **At r*.** Convergence in the cutoff X (n·s ≤ X) is as follows:

| X | F(0) | F′(0) | F″(0) | 𝒜 | 2AB | 𝒲_ext = 𝒜 + 2AB − F′(0) |
|---|---|---|---|---|---|---|
| 15 | 1.641 | 0.067 | 5.01 | 6.518 | 0.0002 | 6.451 |
| 30 | 1.685 | 1.384 | 15.01 | 6.698 | 0.0018 | 5.316 |
| 60 | 1.608 | 1.281 | 15.91 | 6.416 | 0.0002 | 5.135 |
| 120 | 1.611 | 1.397 | 17.37 | 6.483 | 0.0007 | 5.087 |
| 240 | 1.612 | 1.468 | 18.34 | 6.529 | 0.0007 | 5.062 |

- **Extrapolation in 1/X.** F′ → 1.54, 𝒜 → 6.58 and 𝒲_ext → 5.03 (−0.01 from resolution in y). Against W_T(g*) = 4.978, the
  agreement is **≈ 1%**.
- **Theorem D at r*: consistent to 1%, not "to every digit."** The limitation is not arithmetic precision. It comes from
  r* not being admissible (tail 1/ξ, A(Ψ̌) only conditionally convergent) and from the cutoff in ω.
- **Calibration.** The verification to 10⁻¹⁰ on admissible data is what calibrates the method.
- **Values at r*.** A = −0.058, B = −0.006 (2AB negligible) and ‖Ψ̌*‖² = F(0) = 1.61 ≈ 0.19ℓ*.

## 3. Step 3 — F″(0), convexity, Lemma F bound
- **F″(0) = 2‖Z_log r*‖² + 2⟨Zr*, Z_{log²}r*⟩ = 13.81 + 4.53 = +18.34** (X = 240). Both summands are positive.
  Extrapolating in 1/X gives ≈ +19.3. The sign is + at **every** cutoff X ≥ 15.
- **Ratio with ℓ*.**
  - With ℓ* = 8.60 (Parseval, minimum leakage; upper bound of the gauge infimum): F″/ℓ* = 2.13.
  - With 8.44: 2.17.
  - With the structured part 4.4: 4.17.
  - Extrapolated: 2.2–4.4.
- **Convexity.** The second difference of F on the grid ε ∈ [−0.05, 0.25] (step 0.005) is positive at every point: minimum
  14.0 at ε = −0.045 and maximum 82.8 at 0.245. **F is convex on [0, 0.186]** and on the whole grid.
  - Values: F(−0.05) = 1.559, F(0) = 1.612, F(0.1) = 1.872, F(0.186) ≈ 2.36, F(0.25) = 2.995.
- **Lemma F bound.** L(ε) = ‖A_ε r*‖² − ε⁻¹F(ε) = 𝒜 + 2AB + (F(0) − F(ε))/ε.
  - L decreases in ε, from 5.02 (ε = 0.005) to 2.51 (ε = 0.185) and 1.00 (ε = 0.25).
  - **Infimum on (0, 0.186]: ≈ 2.5·10⁻⁷⁰ > 0**, attained at the boundary.
  - The convexity remainder is Δ_ε = 0.046 (ε = 0.005) and 2.55 (ε = 0.185).
  - For large ε the weights n^ε amplify the tail: L(0.25) dropped from 1.84 (X = 60) to 1.00 (X = 240), so the value at that
    endpoint is not converged. For ε ≤ 0.1 the change is < 0.15.

## 4. Comparison with the predictions of A_MU §3

| prediction | result |
|---|---|
| 1. 𝒜 + 2AB − F′(0) = W; pieces O(‖Ψ̌‖²) | ✓ to 1% (5.03 against 4.98); 𝒜/‖Ψ̌‖² ≈ 4.05 |
| 2. ‖A_εr‖², ℰ_ε ≍ ℓ* at ε ≈ 0.19 (does not violate P2) | ✓ ‖A_εr‖² ≈ 15.2, ℰ_ε ≈ 12.7 (×10⁻⁷⁰) |
| 3. Decisive test: sign of F″ on [0, ε] | F″ > 0 on the whole grid, margin ≈ 2–4 ℓ* |
| 4. F′(0) dominated by n ∈ {1,2}; F″ ≈ 2(log2)²‖h₂‖² + 2(log2)²⟨h₁,h₂⟩, sign according to ⟨h₁,h₂⟩ | **false** |

On prediction 4:
- **Coefficient.** The memo's formula has a coefficient error: the exact (1,2) block is 4(log2)²‖h₂‖² + 2(log2)²⟨h₁,h₂⟩.
- **Measured values.** ‖h₁‖² = 4.19, ‖h₂‖² = 1.26 and ⟨h₁,h₂⟩ = −1.32. The latter is negative, consistent with the
  (1,2) resonance of EXTERIOR_DATUM.
  - Exact (1,2) block: +1.16.
  - Memo's formula: would give −0.06, with the wrong sign.
- **Breakdown of F″** (terms (log m + log n)²⟨h_m,h_n⟩):
  - (2,2) = 2.43, (1,2)+(2,1) = −1.27, (3,3) = 3.27, (1,3)×2 = −2.24, (2,3)×2 = 2.79.
  - m, n ≤ 8 sum to 10.0 out of 18.3. The remainder comes from n > 8, because F″ goes from 5.0 (X = 15) to 18.3 (X = 240).
- **Breakdown of F′(0).** The (1,2) block gives −1.83 + 1.75 = −0.08 out of 1.47, so it is not dominated by n ∈ {1,2} either.
- **Reading.** The positivity of F″ is carried by the (log n)² weights on the diagonal ‖h_n‖² of high dilates. At r* that
  diagonal is partly fed by the non-admissible tail 1/ξ.

## 5. Verdict
- **Branch of the objective.** F″(0) ≥ c·ℓ* with c ≈ 2.1 (conservative; up to 4.4). This is the second branch: **Lemma F does not die at
  the extremal** and becomes the logarithmic-moment inequality (OPEN, without Λ):
  M₁-convexity ⇔ 2‖Z_log r‖² + 2⟨Zr, Z_{log²}r⟩ ≥ 0, and in integrated form Δ_ε ≥ 0.
- **(f) survives as a candidate factorization at μ = 15** (NUMERICAL, a single vector).
- **Caveats that must be stated with the lemma:**
  - (i) **Gauge dependence.** F (even F(0)) is not gauge-invariant, unlike 𝒲. An O(1) gauge changes r
    by O(1). Lemma F must be stated on the minimum-leakage representative, or else proved for every representative.
    On the two pure φ tested, F″_φ > 0; no counterexample was found.
  - (ii) At r* the convexity is dominated by high dilates, not by the (1,2) resonance. The inequality that must be
    proved is of diagonal type (log n)² versus cross terms, not a two-mode problem.
  - (iii) r* is not admissible (g*(T) ≠ 0 at the level of the Galerkin floor). Repeat with a kernel vector (g(T) = 0) or with
    a boundary correction before citing the constant c.
  - (iv) The side correction to MORI15: ρ* resolved with 300 nodes per cell has errors of 0.1–1%, and the minimum-gauge
    leakage via Parseval is 8.60·10⁻⁷⁰.
- L′♯ OPEN. Row D OPEN.

## 6. Index entry (ROUTES-TRIED-INDEX, phase 200)
- **F0_TEST_001 (phase 200, round 4, verifier; NUMERICAL):**
  - F₀ test of A_MU (f) at the Mori extremal μ = 15. W* reproduced (74-digit cancellation); W_T(g*) = 4.978·10⁻⁷⁰.
  - Theorem D verified to 10⁻¹⁰ on admissible gauge and to 1% at r*.
  - **F″(0) = +18.3 (≈ 19.3 extrapolated)·10⁻⁷⁰ ≈ 2.1–4.4 ℓ*, F convex on [−0.045, 0.245]**, inf_{ε ≤ 0.186} L(ε) ≈ 2.5·10⁻⁷⁰.
    Lemma F survives and becomes a log-moment inequality (OPEN, without Λ).
  - Falsified: "F″ dominated by ⟨h₁,h₂⟩"; ⟨h₁,h₂⟩ = −1.32 and F″ is diagonal in high n.
  - Do not retry: the two-mode reading of F″. Pending: gauge dependence and kernel vector with g(T) = 0.
