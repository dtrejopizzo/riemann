## Overview ## ANSWER The hypothesis is **CONFIRMED**. At peaks with the most negative r values (for the zeta function at N=10⁶ in t ∈ [10⁶, 2×10⁶]), the negative contribution to r does **not** come from the (ω=1, ω=2) interaction, but from interactions involving higher ω-classes. ### Key Quantitative Findings: **Top 3 negative off-diagonal pairs (driving conditional anti-correlation):** 1. **(ω=1, ω=3)**: ⟨Re[S₁ S̄₃] / D⟩ = **-0.103760** (largest negative contribution)
2. **(ω=2, ω=4)**: ⟨Re[S₂ S̄₄] / D⟩ = **-0.079012** (second largest negative)
3. **(ω=1, ω=4)**: ⟨Re[S₁ S̄₄] / D⟩ = **-0.061812** (third largest negative) Sum of top 3 negative contributions: **-0.244585** **In contrast, the (ω=1, ω=2) term:**
- ⟨Re[S₁ S̄₂] / D⟩ = **+0.195596** (POSITIVE)
- This is the **largest positive** off-diagonal contribution ### Analysis Details: - Analyzed 50 zeta peaks with most negative r values at N=10⁶
- 21 of these 50 peaks have r < 0
- Average r across selected peaks: 0.023246
- Average denominator D = ⟨Σ|S_k|²⟩ = 42.890 Total balance of cross-terms:
- All negative contributions: -0.266219
- All positive contributions: +0.289465
- Net (average r): +0.023246 The top 3 negative pairs account for **92%** of all negative contributions (-0.244585 / -0.266219). ### Complete Normalized Matrix ⟨C_jk / D⟩: | | ω=1 | ω=2 | ω=3 | ω=4 | ω=5 | ω=6 | ω=7 |
|-----|---------|---------|----------|----------|----------|----------|----------|
| ω=1 | 0.334 | 0.196 | **-0.104** | **-0.062** | 0.004 | 0.001 | -0.000 |
| ω=2 | 0.196 | 0.386 | 0.073 | **-0.079** | -0.006 | 0.001 | -0.000 |
| ω=3 | -0.104 | 0.073 | 0.218 | 0.015 | -0.014 | -0.001 | 0.000 |
| ω=4 | -0.062 | -0.079 | 0.015 | 0.057 | 0.001 | -0.001 | 0.000 |
| ω=5 | 0.004 | -0.006 | -0.014 | 0.001 | 0.006 | -0.000 | -0.000 |
| ω=6 | 0.001 | 0.001 | -0.001 | -0.001 | -0.000 | 0.000 | 0.000 |
| ω=7 | -0.000 | -0.000 | 0.000 | 0.000 | -0.000 | 0.000 | 0.000 | (Bold values indicate top 3 negative contributions) --- ## DISCRETIONARY DECISIONS - **Peak selection strategy**: Selected 50 peaks with most negative r values from the top 200 highest peaks by |D_F|, rather than selecting peaks that are strictly negative in r (only 21 such peaks existed)
- **Scan resolution**: Used 2000 t-values for initial peak finding in range [10⁶, 2×10⁶] as a balance between computational cost and peak resolution
- **Peak finding parameters**: Used prominence=1.0 and distance=5 for scipy.signal.find_peaks, consistent with the dataset description
- **ω-class range**: Computed S_k for k ∈ [1, 7] to capture all non-negligible ω-classes at N=10⁶
- **Chunking strategy**: Used chunk size of 20 t-values for vectorized Dirichlet sum computation to manage memory usage
- **Numerical summation**: Applied Kahan compensated summation for all Dirichlet polynomial evaluations to minimize floating-point errors
- **Averaging method**: Computed ⟨C_jk / D_i⟩ by averaging the normalized contributions at each peak, rather than normalizing the averaged matrix (the former correctly gives average r as the sum of off-diagonal terms)
- **Random seed**: Set numpy random seed to 42 for consistency with dataset description (though not strictly necessary for deterministic zeta function) 