## Overview # Answer to Research Hypothesis ## Main Finding The synthetic non-multiplicative function **F(s; N) = ζ_N(s) + Λ_N(s)** exhibits **MIXED S₂/S₄ dominance** rather than clear S₂-dominance, with 60% of peaks being S₂-dominant (12/20) and 40% being S₄-dominant (8/20). ## Quantitative Results At N = 10⁶, analyzing the 20 highest-magnitude peaks in t ∈ [10⁶, 2·10⁶]: - **Mean S₂ perturbation reduction**: 60.8% ± 20.6%
- **Mean S₃ perturbation reduction**: 0.0% (structural zero)
- **Mean S₄ perturbation reduction**: 51.9% ± 20.2% Power distribution:
- S₂: 57.8% ± 17.3%
- S₄: 28.5% ± 12.2%
- S₆: 7.2% ± 6.1%
- All odd ω-classes (S₁, S₃, S₅, ...): exactly 0% ## Critical Structural Property The function F(s) = ζ(s) + Λ(s) has coefficient a_n = 1 + λ(n) = 1 + (-1)^Ω(n), which equals:
- **2** when Ω(n) is even
- **0** when Ω(n) is odd This creates:
1. **Sparsification**: 50.0% of coefficients are exactly zero (500,265 out of 1,000,000 terms)
2. **Structural cancellation**: All odd ω-classes vanish identically
3. **Power concentration**: Remaining power redistributes to even ω-classes (S₂, S₄, S₆) ## Conclusion on Hypothesis **The hypothesis is PARTIALLY SUPPORTED with important qualifications.** While the linear combination does create a non-multiplicative function with enhanced S₂ contribution (60% of peaks are S₂-dominant), it does NOT produce the clear, reliable S₂-dominance characteristic of L_DH. The comparable mean reductions (60.8% vs 51.9%) and substantial fraction of S₄-dominant peaks (40%) indicate a fundamentally **mixed causal structure**. **Key insight**: The synthetic function F(s) differs from L_DH in a crucial way—F(s) is **sparse** (~50% zero coefficients) while L_DH is **dense** (all non-zero coefficients). This suggests that: 1. Non-multiplicativity alone is insufficient for S₂-dominance
2. Sparsification through linear combination creates structural zeros that prevent S₃-dominance but don't guarantee S₂-dominance
3. The specific dense, non-multiplicative coefficient structure of L_DH appears essential for its characteristic causal hierarchy The mechanism that produces L_DH's S₂-dominance is more subtle than simple non-multiplicativity—it likely requires both the non-multiplicative structure AND dense coefficient support across all ω-classes. --- ## Discretionary Analytical Decisions - **Peak finding strategy**: Used two-phase approach: (1) coarse grid of 5000 points to identify candidates, (2) refined optimization with search width = 100. Alternative approaches could use different grid densities or optimization methods.
- **Number of peak candidates for refinement**: Refined top 30 candidates from coarse search to ensure capturing true top 20. Could have refined more or fewer candidates.
- **Summation method for grid evaluation**: Used vectorized numpy summation for coarse grid search (phase 1) for computational efficiency, validated in dataset description as having negligible error (<10⁻⁸) for large N exploratory work.
- **Summation method for precise evaluation**: Used Kahan compensated summation for all perturbation analyses and final peak evaluations, following dataset best practices for high-precision work.
- **Significance threshold for dominance**: Classified peak as "S_k-dominant" if perturbation of S_k caused maximum reduction. Equal reductions would be classified as "Mixed" (though none occurred).
- **Peak magnitude threshold**: No explicit magnitude cutoff applied; used optimization-based refinement to find true local maxima within search windows.
- **t-range convention**: Used t ∈ [N, 2N] following established convention in dataset for N-dependence studies.
- **Omega class display limit**: Limited detailed decomposition tables to ω ≤ 12 for readability, though higher classes were computed.
- **Statistical reporting**: Reported mean ± standard deviation for perturbation reductions; could alternatively use median, quartiles, or confidence intervals.
- **Visualization design**: Created single-panel bar chart showing mean reductions with error bars; alternative could show individual peak responses or power distribution heatmap. **External datasets used**: omega_values_N1e6.pkl (pre-computed Ω(n) values for n=1 to 10⁶, from derived artifacts). 