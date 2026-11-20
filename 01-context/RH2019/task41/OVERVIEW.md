## Overview ## M₄ Decomposition Analysis: Testing Universality of Three-Index Type A Dominance ### Main Conclusion The hypothesis that "Three-Index Type A" (Re[|S_j|² S_k S̄_l]) terms universally dominate the fourth moment off-diagonal contribution in high-magnitude regimes across multiplicative functions is **REJECTED**. The M₄ structure in high-magnitude regimes is function-dependent rather than universal. ### Detailed Results **Top 10% M₄ Regime Category Contributions:** | Category | Zeta | Möbius | f_rand | Mean |
|----------|---------|---------|---------|---------|
| PD | 2.35% | 4.91% | 1.53% | 2.93% |
| MD | 28.80% | 45.46% | 23.35% | 32.54% |
| 3A | 15.12% | 15.65% | 13.73% | 14.83% |
| 3B | 26.84% | 25.63% | 26.89% | 26.45% |
| 4I | 26.90% | 8.34% | 34.49% | 23.24% | **Leading Off-Diagonal Contributors (Top 10%):**
- **Zeta**: Mixed Diagonal (MD) at 28.80%
- **Möbius**: Mixed Diagonal (MD) at 45.46% - **f_rand**: Four-Index (4I) at 34.49% **Three-Index Type A (3A) Rankings:**
- Zeta: Rank 4/4 among off-diagonal terms (15.12%)
- Möbius: Rank 3/4 among off-diagonal terms (15.65%)
- f_rand: Rank 4/4 among off-diagonal terms (13.73%) **Top 1% M₄ Regime Analysis:** Similar patterns persist at the top 1% M₄ magnitude threshold (50 highest points). 3A contributes ~18% across all functions but is never the dominant term:
- **Zeta**: 3B dominates at 32.35%
- **Möbius**: MD dominates at 42.47%
- **f_rand**: 4I dominates at 36.78% **Off-Diagonal Dominance Confirmed:** While the specific breakdown differs from expectations, all functions show strong off-diagonal dominance (95-99%), confirming the general finding from r23. However, there is no single universal off-diagonal term structure. ### Function-Specific Patterns **Zeta**: Balanced competition among MD, 3B, and 4I terms (all ~27-29% in top 10%). 3A consistently ranks last among off-diagonal terms. **Möbius**: Strong and consistent MD dominance (42-45%) across all high-M₄ regimes. Weak 4I contribution (~8%). 3A stable around 16-18%. **f_rand**: Strong 4I dominance (34-37%) with all three-index terms (3A + 3B) combining to ~40-50%. Most variable function with largest M₄ magnitudes (mean M₄ = 31,707 in top 10% vs. 18,016 for zeta and 7,526 for Möbius). --- ## Discretionary Analytical Decisions - **N=10⁶ truncation**: Standard for this dataset series, enabling use of pre-computed omega_values artifact
- **t-range [10⁶, 2×10⁶]**: Followed established N-scaling convention from dataset documentation
- **Grid resolution: 500 t-points**: Balance between statistical power and computational feasibility (~10 min per function at 1.24s per t-point)
- **Top 10% threshold for high-M₄ regime**: Standard percentile cutoff; also examined top 1% for sensitivity analysis
- **M₄ magnitude threshold (absolute value)**: Used |M₄| rather than signed M₄ to capture high-magnitude events regardless of sign
- **Kahan compensated summation**: Critical numerical precision requirement from dataset documentation
- **Möbius function implementation**: Used sieve-based generation rather than direct prime factorization for efficiency
- **Random multiplicative function seed=42**: Standard reproducibility seed from dataset; saved coefficients to file for exact reproducibility
- **Category classification scheme**: Based on index uniqueness and conjugate pair presence: - PD: j₁=k₁=j₂=k₂ - MD: (j₁=k₁, j₂=k₂) but j₁≠j₂ - 3A: 3 unique indices with conjugate pair (j₁=k₁ OR j₂=k₂) - 3B: 3 unique indices without conjugate pair (j₁=j₂ OR k₁=k₂) - 4I: all distinct indices
- **External dataset: omega_values_N1e6.pkl**: Pre-computed Ω(n) values for all n ∈ [1, 10⁶], avoiding repeated prime factorization 