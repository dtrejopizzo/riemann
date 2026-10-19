# Audit of δV: density or position — and verification of the "pole" Working document (post-LaTeX, en.md). Audits the last GAP of the cascade
Link 2 / ε₀≥0: the discrepancy δV = V_λ − Kφ₀/φ₀. Markers: **[P]** proved · **[N]** robust numerical · **[O]** open. --- ## 0. Context: the cascade so far ```
A_λ ⪰ 0 ⟺ (Schur) (i) K−V ⪰ 0 on φ_pole^⊥ + (ii) scalar b+κ ≥ r*M⁺r
(i) ⟸ (FLS, non-local) K−V₀ ⪰ 0 on φ_pole^⊥ [P] + bound on δV = V_λ−V₀ [O]
```
- Schur: **[P]** (exact algebra).
- Frank–Lieb–Seiringer (ground-state representation): **[P]**, resolves the non-locality for the ground-state potential V₀ = Kφ₀/φ₀.
- Remaining: the bound on δV over φ₀^⊥, and the scalar (ii). --- ## 1. Prior verification: is φ₀ the pole mode? (was a conflation risk) The cascade uses **two** objects both called "φ_pole":
1. **φ₀** = fundamental eigenvector of A_λ in E_λ (where ε₀ lives, the risk direction).
2. **u_pole** = uniform direction in the space of *prime weights* (via #9, global density = pole s=1, unconditional). The cascade **requires** that these coincide (that P, on u_pole, act on φ₀). ### Numerical test (decisive) | precision | ε₀ | overlap φ₀·U₀ | low-freq weight | center/edge mass | reading |
|---|---|---|---|---|---|
| float64 | ~1e-15 (noise) | 0.003 | 0.025 | 0.32 / 1.52 | "edge-localized, ⊥ pole" → **FALSE** |
| **mpmath dps=40** | **9.28e-21** | **0.76** | **0.996** | **0.52 / 0.51** | **φ₀ smooth = pole mode** | **[N, robust] φ₀ IS the smooth pole-type mode:** 99.6% low-frequency, 76% overlap with
the constant mode. The "edge-localized" reading from float64 was **noise** (eigenvalue ~1e-15 below
the machine floor; the same trap as route #9). **Record correction:** the previous characterization "edge-localized eigenvectors with
central vanishing" is very likely a **float64 artifact**. The true ground state
is smooth / pole-aligned. **Consequence:** the conflation is NOT a crack. φ₀ ≈ u_pole. The cascade's mechanism
(the pole acts on the risk direction) **holds**. --- ## 2. The audit of δV: density or position? With φ₀ smooth confirmed, V₀ = Kφ₀/φ₀ is the **smooth mean-field potential**, and
δV = V_λ − V₀ is **the fluctuation of the primes around the mean**. ### Arguments that δV is DENSITY (Scenario A) 1. **V_λ is finite and entire.** V_λ(w) = Σ_{n≤λ²} (Λ(n)/√n)·[mass at log n]. It is a truncated Dirichlet polynomial: **no poles, no zeros**. It does not "contain" the position of any zero. Zeros would only appear if V_λ were related to the *complete* −ζ'/ζ; but the bound we need is on V_λ *directly*.
2. **δV is purely arithmetic:** primes (V_λ) minus smooth mean (V₀ = Kφ₀/φ₀, with K archimedean and φ₀ smooth). No zeros.
3. **Its size is controlled by the PNT error term.** The fluctuation Σ_{p≤λ²}(...) − (mean) is exactly what the **classical zero-free regions (Vinogradov–Korobov)** bound: unconditional input, **does not use Θ=½**. ### The only remainder: quantitative sufficiency [O] Bound (i) closes ⟺
``` ∫ δV |g|² ≤ β_λ ‖g‖² ∀ g ∈ φ₀^⊥,
```
with β_λ the improved Hardy gap (FLS remainder). It is a **quantitative race**:
- **δV side:** classical bound from zero-free regions ~ λ²·exp(−c(log λ)^{3/5}) or similar (unconditional PNT error term).
- **β_λ side:** the FLS remainder gap, ~ order of the ε-gaps of the (k+1)² tower, expected ~ C₀/λ² or (log λ)^{−A}. **It is not an equivalence with RH.** It is: is the unconditional bound on δV (density)
< β_λ? If yes → (i) closes non-circularly. If the classical bound is not enough and
δV ~ RH-optimal is needed → Scenario C re-enters. ### Where Scenario C might hide (what to watch) - If β_λ decays *faster* than the classical bound on δV, the race is lost on density and δV would need to be refined with fine information (position) → C.
- The projection onto φ₀^⊥ might *not* kill the part of δV that correlates with the zero structure. One must verify that δV on φ₀^⊥ is genuinely the "white" (PNT) fluctuation and does not retain an echo of Σ_ρ. --- ## 3. Verdict of the audit - **[N]** φ₀ = smooth pole mode: confirmed in mpmath. The feared conflation does NOT exist; the cascade holds. (Float64 gave a false "edge-localized".)
- **[P/argued]** δV is on the **density side**: finite arithmetic object (primes + smooth mean), with no explicit zeros; its size is governed by classical zero-free regions (not Θ=½). **Leans toward Scenario A.**
- **[O]** The **quantitative sufficiency** (classical bound on δV < β_λ) is the only thing left for (i), plus the scalar (ii). It is a race of sizes, computable. **Frank reading:** the audit did not break the cascade — on the contrary, it ruled out a possible
conflation (via mpmath) and showed that δV lives on the density side. But it **shifts** the
problem to two quantitative bounds (δV and the scalar (ii)) whose sufficiency must be
*computed*, not assumed. Scenario C is not excluded: it could re-enter if β_λ decays
faster than the unconditional bound on δV. ## 4. Concrete next step Numerically measure the **two quantities of the race**:
1. **β_λ** = FLS remainder gap = smallest eigenvalue of (K−V₀) over φ₀^⊥ (computable: K, V₀=Kφ₀/φ₀, project).
2. **‖δV‖ over φ₀^⊥** = norm of the projected primes−mean fluctuation. If β_λ ≳ ‖δV‖_{φ₀^⊥} numerically (and the trend in λ holds), Scenario A gains
quantitative strength. If ‖δV‖ dominates, one must understand why and whether the projection helps.
This is **computable** with the already-built ARCH, ARITH matrices + φ₀ in mpmath. --- ## 5. Measurement of the race (mpmath dps=40, λ=3.7/5/7) ### Left-hand side: β_λ (improved Hardy margin over ℓ^⊥) | λ | ε₀ | β_λ = min A_λ|_{ℓ⊥} | β_λ/ε₀ |
|---|---|---|---|
| 3.7 | 1.67e-20 | 7.59e-20 | 4.53 |
| 5 | 1.00e-20 | 3.78e-20 | 3.79 |
| 7 | 5.81e-21 | 2.30e-20 | 3.95 | **[N] β_λ ≈ 4ε₀, stable.** The pole direction ℓ carries ALL the risk (there the form equals
ε₀, the minimum); projecting it out, the margin jumps to ~4ε₀. **The positive
Brezis–Vázquez remainder is real and robust (4×).** Confirms the improved-Hardy picture. ### Alignment of the risk direction with the pole | λ | overlap(φ₀, ℓ) | tower |
|---|---|---|
| 3.7 | 0.771 | ε₁/ε₀=4.58, ε₂/ε₀=9.14 |
| 5 | 0.782 | 3.86, 9.08 |
| 7 | 0.797 | 4.07, 9.05 | **[N]** φ₀ is ~78% aligned with the pole functional ℓ (=e^{u/2}), **increasing with λ**
→ tends to align further. Tower (k+1)² confirmed. ### Frank reading of the race - **Left-hand side β_λ ≈ 4ε₀ ~ 4C₀/λ²:** measured, positive, stable. The improved Hardy bound has 4× slack over ℓ^⊥.
- **Decisive CAVEAT:** this is RH-true data. The measured β_λ already COMBINES the FLS positivity (β_FLS) and the δV correction — it does not separate them. That the net is +4ε₀>0 says that **δV does NOT dominate β_FLS** (empirically, for this data), but does not isolate δV.
- **What the numerics CANNOT give:** separating β_FLS vs δV is analytic (we only have data with zeros on the line). The unconditional proof needs β_FLS ≥ δV proved from the prime side. ## 6. Synthesis of the state (post-measurement) **Confirmed numerically [N]:**
- Tower (k+1)²; φ₀ pole-dominant (78%, increasing); β_λ≈4ε₀>0 stable.
- The improved-Hardy structure (deficit at the pole-extremal, positive complement) is REAL, not assumed. **What remains, now purely analytic [O]:**
1. β_FLS ≥ δV over ℓ^⊥, unconditional (δV = prime fluctuation, density side).
2. The Schur scalar (ii) over the pole direction. **Verdict:** the cascade passed all the numerical checks that could have broken it.
It is neither circular nor vacuous. What remains are two concrete arithmetic inequalities whose
proof is analytic (not numerical), because the numerics only access the RH-true regime.
The front is alive and localized to the millimeter.
