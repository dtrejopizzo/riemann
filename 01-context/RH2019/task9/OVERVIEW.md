## Overview # Analysis of F(s) = L(s, χ₃) + L(s, χ₅): Causal Dominance in Non-Multiplicative Arithmetic Functions ## Summary The linear combination F(s) = L(s, χ₃) + L(s, χ₅) produces a non-multiplicative function with 80% density that exhibits **weak S₂ preference** (46.16% vs 40.88% mean perturbation reduction, p=0.165) in causal perturbation analysis, but **strong S₂ dominance** in power distribution (29.74% vs 24.23%). The hypothesis is **partially supported**: while the combination shifts power concentration toward S₂, causal dominance is highly variable and not statistically significant, indicating that simple linear combination of dense arithmetic L-functions is insufficient to reliably replicate the S₂-dominance mechanism of L_DH. ## Detailed Results ### Function Properties (Objectives 1-2)
- **Non-multiplicativity verified**: a₂ × a₃ = (1-1j) ≠ a₆ = (1+0j)
- **Density**: 80.00% non-zero coefficients (800,002/1,000,000) - Zeros occur at three classes: n≡0(mod 15), n≡2(mod 3)∩n≡1(mod 5), n≡1(mod 3)∩n≡3(mod 5) - Not fully dense, but substantially more dense than the failed r61 experiment ### Peak Identification (Objective 3)
- **Method**: Two-phase search with 10,000-point coarse grid (vectorized) followed by Kahan-summation refinement using scipy.optimize.minimize_scalar (Brent's method)
- **Top 20 peaks identified** at N=10⁶, t ∈ [10⁶, 2×10⁶]
- **Highest magnitude**: |F(t)| = 27.17 at t = 1,123,848.59
- Peak magnitudes range from 27.17 to 13.35 ### Causal Perturbation Analysis (Objectives 4-5)
**Perturbation by e^(iπ) = -1:**
- **S₂ perturbations**: Mean reduction = 46.16% ± 10.95%
- **S₃ perturbations**: Mean reduction = 40.88% ± 10.20%
- **Difference**: 5.28 percentage points favoring S₂
- **Statistical significance**: Paired t-test t=1.445, **p=0.165** (NOT significant at α=0.05)
- **Dominance counts**: S₂ dominant in 11/20 peaks (55.0%), S₃ dominant in 9/20 peaks (45.0%) **Key observation**: The dominance pattern is highly variable across peaks, with nearly equal split between S₂ and S₃ dominance. ### Power Distribution
Average power contributions across top 20 peaks:
- S₀: 5.77%
- S₁: 18.81%
- **S₂: 29.74%** (highest)
- S₃: 24.23%
- S₄: 13.30% S₂ is the class with highest power concentration, but only marginally above S₃. ### Correlation Analysis
**Strong predictive relationship discovered:**
- Pearson correlation between |S₂|/|S₃| ratio and dominance difference: **r = 0.9326** (p < 10⁻⁸)
- Power ratio correctly predicts dominance in **18/20 peaks (90%)**
- Mean |S₂|/|S₃| for S₂-dominant peaks: 1.513
- Mean |S₂|/|S₃| for S₃-dominant peaks: 0.879
- Mann-Whitney U test: p = 0.0001 (highly significant) **Interpretation**: Causal dominance is almost entirely determined by the relative magnitudes of S₂ and S₃ at each specific peak, rather than being a global property of the function. ## Conclusion (Objective 6) The combination of L(s, χ₃) + L(s, χ₅) does **NOT** produce consistent S₂-dominance. While there is a weak average preference for S₂ (5.28% higher mean reduction), this difference is not statistically significant (p=0.165). The dominance pattern is highly variable, with the split nearly 50-50 between S₂ and S₃ across peaks. **The hypothesis is REJECTED**: Simple linear combination of two dense, S₃-dominant arithmetic L-functions is insufficient to shift causal dominance to S₂ in a reliable, consistent manner. The mechanism underlying L_DH's S₂-dominance requires more than just combining different arithmetic structures within a dense framework. **Critical finding**: The strong correlation (r=0.93) between |S₂|/|S₃| power ratio and causal dominance indicates that for this particular synthetic function, dominance is determined locally at each peak by the instantaneous power balance, not by global structural properties of the arithmetic function. --- ## Discretionary Decisions - Used Kahan compensated summation for all final evaluations at peak locations to ensure high-precision results
- Set coarse grid size to 10,000 points for Phase 1 search, balancing computational cost with peak detection resolution
- Chose refinement window of ±150 around each candidate peak for local optimization
- Selected top 50 candidates from coarse search for refinement (to ensure robust identification of top 20)
- Used e^(iπ) = -1 as perturbation phase (standard in dataset methodology)
- Applied two-tailed paired t-test at α=0.05 significance level for comparing S₂ vs S₃ perturbation effects
- Used Mann-Whitney U test (one-tailed) for comparing power ratios between dominance groups
- Evaluated first 10 ω-classes (k=0 to 9) for power distribution analysis
- **External dataset**: omega_values_N1e6.pkl (pre-computed Ω(n) values for n=1 to 10⁶) 