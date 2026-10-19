# CA_C_005 — μ_M(η): the infimum of A_M over the s_w family at η = 0.7 and 0.9 (NUMÉRICO)

Phase 193, round 8. This is the one numerical check flagged as strictly necessary in CA_C_003 §3. Script:
03-research/phase-190-near-coincidence-experiment/scripts/mu_family.py, which reuses profile.py and am.py of phase 190 (same
profile F₀ with b = 1, same A_M). Floating point (numpy/scipy eigh), not certified. **No negative value found: μ_M > 0 in every run.**

**Quantity.** μ_M(η) := min of sᵀA_Ms/‖s‖² over the span of Prop. 1 of CA_C_003: vectors equal to c·m^{−½} on m ≤ ηM and free on
(ηM, M]. The span contains every s_w, so μ_M(η) is a lower bound for the infimum over the smooth family 𝒲_η. The lower bound is the
relevant quantity for the margin question: if it is critical, so is the family.

| T₀ | η | M | μ_M(η) | λ_min(A_M) | μ/λ_min |
|---|---|---|---|---|---|
| 0.3 | 0.7 | 100 | 6.53e−5 | 4.46e−6 | 15 |
| 0.3 | 0.7 | 200 | 2.62e−5 | 5.94e−7 | 44 |
| 0.3 | 0.7 | 400 | 4.48e−6 | 7.82e−8 | 57 |
| 0.3 | 0.7 | 800 | 3.57e−7 | 1.01e−8 | 35 |
| 0.3 | 0.9 | 200 | 1.08e−4 | 5.94e−7 | 182 |
| 0.3 | 0.9 | 400 | 1.48e−5 | 7.82e−8 | 189 |
| 0.3 | 0.9 | 800 | 2.03e−6 | 1.01e−8 | 201 |
| 0.3 | 0.9 | 1200 | 6.34e−7 | 3.05e−9 | 208 |
| 0.15 | 0.7 | 200 | 2.42e−5 | 4.71e−6 | 5.1 |
| 0.15 | 0.7 | 400 | 5.38e−6 | 6.15e−7 | 8.7 |
| 0.15 | 0.7 | 800 | 1.21e−6 | 8.09e−8 | 15 |

**Scaling.**
- (T₀ = 0.3, η = 0.9): the local log–log slope is −2.87 on all three steps, so μ_M ≈ M^{−2.9}, with μ/λ_min ≈ 180–210, nearly constant.
- (T₀ = 0.3, η = 0.7): the slope steepens from −1.3 to −3.6 over 100 → 800.
- (T₀ = 0.15, η = 0.7): the slope is ≈ −2.15.
In none of the runs is μ_M of order 1 or of order 1/log M. Restricting to the family costs at most a bounded or slowly growing factor over
λ_min ≍ M^{−3} (EXP_002/003).

**Conclusion (NUMÉRICO).** T*₃(η) for η ∈ {0.7, 0.9} is **critical, not a margin statement**: its infimum decays like a power M^{−2…−3},
tracking λ_min. Lemma shape-est(i) (B′) therefore applies to the family. A hand proof by main term plus remainder must match to relative
precision ≈ M^{−3} in terms of size O(log M), which is the precision obstruction of SPEC_B §1.3 again, now on the prime-free sub-family.
This settles CA_C_003's dichotomy on the critical side. **(Fam_{η>2/3}) is not hand-provable by estimates, and it is not a route.**
Two side observations:
- The family is "near-extremal" even at η = 0.9, where the A_M-minimizer is not in the span. The near-flat part of the minimizer
  (c·m^{−½} on [1, ηM]) already carries almost all of the criticality.
- Hence the criticality of (S) is visible on vectors whose prime content is Λ(2) alone (η > 2/3, 2T₀ < log 2). The near-zero bottom is
  produced by Γ_ℝ, log N (the product formula) and log 2. On this family this is an exact cancellation in an explicit prime-free quantity.

**Self-review.** (1) The span is larger than 𝒲_η (no smoothness bound on the free part), so μ_M is only a lower bound. If the smooth
infimum were of order 1 the margin question would reopen. But the free part lives on (ηM, M], where the A_M-minimizer is itself smooth
(EXP_005), so a smooth restriction should cost a bounded factor. ARGUED, not checked. (2) Floating point at 1e−9 relative to entries of
size O(1): λ_min values agree with EXP_002/003, but the M = 1200 entries are near the reliable limit. (3) One profile only (b = 1).
(4) No sign contact: all values are positive.

**Open sub-question (new, OPEN).** On η > 2/3 the quantity Q_M(w) involves only Γ_ℝ, log N and log 2, and it is still critical. Is there an
exact identity that expresses inf_{w∈𝒲_η} Q_M(w) through the zeros, as for the full A_M (thm:finZ, C_zeros)? If the prime-free family is
critical *because of* the zeros, then by construction the criticality is a zero-side phenomenon and no prime-side mechanism on this
family exists (C_zeros, (R)(4)). Likely yes, via EI_002 Thm 1 (Q = (1/π)∫F̂₀²|ζ_w|²Re R_{X′}); not developed.

## RETRACTION (round 9, CA_C_007)
The scaling conclusion above is **withdrawn**. μ_M(η) was normalized by ‖s‖² (ℓ² of the coefficients), not by ‖F_s‖² = sᵀGs with
G = [c₀(log m/k)] (the norm of the test function). For η ≥ 0.7 the ℓ²-minimizer is supported in the tail (mass on m ≤ ηM is 1e−6 to 1e−10),
and there ‖F‖²/‖s‖² ≈ 1e−5 to 3e−7: this is Gram degeneracy of nearly coincident translates. Its true Rayleigh quotient 𝔞(F)/‖F‖² is ≈ 4.5–6.
With the correct norm, T*₃(η) for η ∈ {0.7, 0.9} is a **margin** statement, not a critical one (table in CA_C_007). The full A_M remains
critical in both norms. The verdict "(Fam_{η>2/3}) is not hand-provable by estimates" is withdrawn with it.
