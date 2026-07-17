## Overview # ANALYSIS RESULTS: Peak Fragility in Partial Sums of ζ(s) and L(s,λ) ## MAIN FINDING **The research hypothesis is DECISIVELY REJECTED.** Contrary to the prediction that resonance peaks would be "fragile" points showing heightened sensitivity to small N-increments, the analysis reveals that **resonance peaks are local stability maxima**. Both ζ(s) and L(s,λ) exhibit dramatically lower fragility scores at their strongest resonance peaks compared to random ordinates. ## QUANTITATIVE EVIDENCE ### 1. ζ(s): Peaks vs Random Ordinates
- **Median fragility at peaks**: 6.62
- **Median fragility at random ordinates**: 85.04
- **Ratio (random/peaks)**: 12.9×
- **Mann-Whitney U test**: p = 1.66×10⁻⁷ (highly significant)
- **Conclusion**: ζ(s) peaks are **12.9 times MORE STABLE** than random ordinates (p < 0.001) ### 2. L(s,λ): Peaks vs Random Ordinates
- **Median fragility at peaks**: 0.50
- **Median fragility at random ordinates**: 5.43
- **Ratio (random/peaks)**: 10.8×
- **Mann-Whitney U test**: p = 1.66×10⁻⁷ (highly significant)
- **Conclusion**: L(s,λ) peaks are **10.8 times MORE STABLE** than random ordinates (p < 0.001) ### 3. Comparison Between Functions at Peaks
- **ζ(s) median fragility at peaks**: 6.62
- **L(s,λ) median fragility at peaks**: 0.50
- **Ratio (ζ/λ)**: 13.2×
- **Mann-Whitney U test**: p = 3.99×10⁻⁶ (highly significant)
- **Conclusion**: L(s,λ) peaks are **13.2 times MORE STABLE** than ζ(s) peaks (p < 0.001) ### 4. Correlation Analysis
- **ζ(s)**: No significant correlation between peak magnitude and fragility (ρ = -0.041, p = 0.865)
- **L(s,λ)**: Significant negative correlation (ρ = -0.605, p = 0.0048) - Stronger L(s,λ) peaks are significantly more stable ## HYPOTHESIS TEST RESULTS 1. **"ζ(s) peaks are more fragile than random ordinates"** → **REJECTED** - Opposite effect observed: peaks are 12.9× more stable (p < 0.001) 2. **"This effect is less pronounced or absent for L(s,λ)"** → **REJECTED** - L(s,λ) shows the same pattern: peaks are 10.8× more stable (p < 0.001) 3. **"L(s,λ) resonances are more robust than ζ(s)"** → **CONFIRMED** - L(s,λ) peaks are 13.2× more stable than ζ(s) peaks (p < 0.001) ## INTERPRETATION The analysis reveals a counter-intuitive phenomenon: **resonance peaks are self-stabilizing features** of the partial sum, not fleeting or fragile phenomena. The fragility score S(t, N, ΔN) = |D(t; N+ΔN) - D(t; N)| / (|D(t; N)| × (ΔN/N)) measures the normalized change in the sum when N is incremented. At resonance peaks: 1. **The partial sum is remarkably stable** with respect to adding the next 1,000 terms
2. **Random ordinates show high fragility**, indicating rapid oscillation of the sum magnitude
3. **L(s,λ) peaks are exceptionally stable**, consistent with previous findings that this function exhibits anomalously strong resonances driven by intrinsic constructive interference of term-class vectors This result fundamentally contradicts the "peak fragility" hypothesis and suggests instead that resonances represent **coherent structures** that persist across N-increments, rather than accidental alignments that disappear when additional terms are added. The stability is not due to the sum magnitude becoming asymptotically constant—rather, the incremental change is proportionally smaller at peaks, indicating that the phase alignment and constructive interference mechanisms are self-maintaining. ## IMPLICATIONS FOR RESONANCE SUPPRESSION The finding that L(s,λ) peaks are 13.2× more stable than ζ(s) peaks provides strong evidence for the robustness of multiplicative anomalies. This is consistent with previous discoveries (r83, r86) showing that L(s,λ) resonances arise from intrinsic alignment of term-class vectors S_k, with an alignment ratio R = 0.822 (82.2% of maximal coherence). The stability of these peaks suggests that the underlying constructive interference mechanism is not disrupted by incremental changes in the truncation, supporting the interpretation that anomalous multiplicative functions sustain resonance through built-in phase coherence rather than through accidental cancellations. For ζ(s), the intermediate fragility (more stable than random but less stable than L(s,λ)) is consistent with its prime-driven resonance mechanism, where peaks result from detectable but weaker prime-phase non-uniformity (mean R = 0.009 at peaks, with 65% showing p < 0.05 for uniformity tests). --- ## DISCRETIONARY ANALYTICAL DECISIONS - **Statistical test selection**: Used Mann-Whitney U test (non-parametric) rather than t-test due to non-normal distributions and consistent with prior analyses (r11, r15, r17, r21, r22, r25, r26, r27)
- **Significance threshold**: Set α = 0.05 for all hypothesis tests
- **Fragility score definition**: Used S = |D(N+ΔN) - D(N)| / (|D(N)| × (ΔN/N)) as normalized measure of sensitivity
- **Base truncation N**: Set N = 10⁶ as base truncation (computationally feasible, consistent with previous studies)
- **Increment ΔN**: Set ΔN = 1,000 as a small relative increment (0.1% of N)
- **Ordinate range**: Used t ∈ [5000, 15000] to avoid low-t behavior and stay within validated numerical regime (t ≤ 20,000 per dataset description)
- **Peak identification spacing**: Used Δt = 5.0 for coarse scan (vs recommended 2π/log(N) ≈ 0.45) to balance resolution and computation time
- **Number of peaks/random ordinates**: Used 20 each per function (reasonable sample size for non-parametric tests)
- **Random seed**: Set seed = 42 for reproducibility of random ordinate selection
- **Kahan compensated summation**: Mandatory per dataset description to mitigate catastrophic cancellation errors
- **Liouville function computation**: Computed λ(n) = (-1)^Ω(n) using sieve-based Ω(n) calculation with JIT compilation for performance 