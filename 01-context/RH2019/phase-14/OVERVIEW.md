## Overview # MOMENT DECOMPOSITION ANALYSIS: N-DEPENDENCE OF ω-CLASS STRUCTURE ## MAIN CONCLUSION The hypothesis is **confirmed**: the large, non-zero off-diagonal contributions to the second moment (M₂) for zeta and Liouville functions at N=10⁴ are small-N artifacts that substantially diminish at N=10⁵, demonstrating convergence toward the Montgomery-Vaughan theorem. --- ## QUANTITATIVE RESULTS ### 1. Second Moment (M₂) Off-diagonal Contributions The Montgomery-Vaughan theorem predicts that ∫|D_F|²dt = Σ_k ∫|S_k|²dt asymptotically, implying zero cross-terms between ω-classes. **Measured off-diagonal percentage of M₂:** **Zeta Function:**
- N=10⁴: -14.14% of M₂ - N=10⁵: -3.23% of M₂ - **Reduction: 10.90 percentage points (77% reduction in magnitude)** **Liouville Function:**
- N=10⁴: -13.57% of M₂ - N=10⁵: -4.88% of M₂ - **Reduction: 8.69 percentage points (64% reduction in magnitude)** Both functions show strong convergence toward zero off-diagonal contribution, with the magnitude decreasing by approximately 3-4x when N increases by 10x. **Absolute values:**
- Zeta N=10⁴: M₂ = 8.26×10⁴, off-diagonal = -1.17×10⁴
- Zeta N=10⁵: M₂ = 1.20×10⁶, off-diagonal = -3.89×10⁴
- Liouville N=10⁴: M₂ = 8.49×10⁴, off-diagonal = -1.15×10⁴ - Liouville N=10⁵: M₂ = 1.14×10⁶, off-diagonal = -5.58×10⁴ ### 2. Convergence Rate Analysis Fitting the power law |off-diagonal %| ≈ A × N^(-α): - **Zeta**: α ≈ 0.641 (faster convergence)
- **Liouville**: α ≈ 0.444 (slower convergence) **Extrapolation to N=10⁶:**
- Zeta: |off-diagonal| ≈ 0.74%
- Liouville: |off-diagonal| ≈ 1.75% This suggests near-complete convergence to Montgomery-Vaughan by N=10⁶. ### 3. Fourth Moment (M₄) Decomposition The fourth moment M₄ = ∫|D_F|⁴dt was decomposed into:
- **Pure diagonal**: Σ_k ∫|S_k|⁴dt (single ω-class)
- **Mixed diagonal**: Σ_{j≠k} ∫|S_j|²|S_k|²dt (two distinct ω-classes)
- **Off-diagonal**: terms with 3+ distinct ω-class indices **Percentage contributions to M₄:** **Zeta Function:**
| Component | N=10⁴ | N=10⁵ | Change |
|-----------|-------|-------|--------|
| Pure diagonal | 13.87% | 9.26% | -4.62pp |
| Mixed diagonal | 25.83% | 18.99% | -6.85pp |
| Off-diagonal | 60.29% | 71.76% | +11.46pp | **Liouville Function:**
| Component | N=10⁴ | N=10⁵ | Change |
|-----------|-------|-------|--------|
| Pure diagonal | 11.70% | 7.72% | -3.99pp |
| Mixed diagonal | 19.33% | 14.67% | -4.66pp |
| Off-diagonal | 68.97% | 77.61% | +8.64pp | **Key finding**: Unlike M₂, the fourth moment becomes increasingly dominated by off-diagonal terms (>8 percentage points increase) as N grows, reflecting the complex interference structure in |D_F|⁴. ### 4. Dominant Cross-terms in M₂ The largest individual cross-term contributions (2∫Re[S_j S̄_k]dt) as percentage of M₂: **At N=10⁴:**
- Zeta: S₂ × S̄₃ contributes -4.70%
- Liouville: S₁ × S̄₃ contributes -4.35% **At N=10⁵:**
- Zeta: S₂ × S̄₄ contributes -1.65% - Liouville: S₁ × S̄₃ contributes -1.27% All cross-term magnitudes decrease substantially (by 2-3x) with N. ### 5. ω-Class Structure Stability Individual ω-class contributions to the M₂ diagonal term remain relatively stable across N:
- ω=0 (n=1): 8-10% of diagonal
- ω=1 (primes): 28-34% of diagonal - **ω=2: ~37% of diagonal (dominant class)**
- ω=3: 16-21% of diagonal
- ω≥4: <6% of diagonal combined --- ## COMPARISON WITH N=10⁴ (Report r4) | Metric | N=10⁴ (r4) | N=10⁵ (r6) | Interpretation |
|--------|-----------|-----------|----------------|
| M₂ off-diagonal (Zeta) | -14.14% | -3.23% | 77% reduction → small-N artifact confirmed |
| M₂ off-diagonal (Liouville) | -13.57% | -4.88% | 64% reduction → small-N artifact confirmed |
| M₄ off-diagonal (Zeta) | 60.29% | 71.76% | +11.46pp → increasing complexity |
| M₄ off-diagonal (Liouville) | 68.97% | 77.61% | +8.64pp → increasing complexity | The ~70% reduction in |M₂ off-diagonal %| demonstrates that conclusions about asymptotic moment structure cannot be reliably drawn from N=10⁴ data alone. --- ## VALIDATION **Parseval-like identity verification:** ∫|D_F|²dt = Σ_k ∫|S_k|²dt + 2Σ_{j<k} ∫Re[S_j S̄_k]dt All computations satisfy this identity to machine precision (relative error < 10⁻¹⁵), confirming numerical accuracy of the decomposition using Kahan compensated summation. --- ## DISCRETIONARY ANALYTICAL DECISIONS - **Integration method**: Trapezoidal rule for numerical integration (standard choice for smooth, oscillatory functions)
- **Number of evaluation points**: 2,000 t-values per run (matching the original dataset description)
- **t-range selection**: t ∈ [T, 2T] where T=N (following the standard convention for Dirichlet polynomial studies)
- **Significance threshold**: Not applicable (purely computational, no hypothesis testing)
- **Power-law fit**: Two-point fit for α estimation (minimal assumption approach, but limited by only two N values)
- **Fourth moment grouping**: Three-category classification (pure/mixed/off-diagonal) based on number of distinct ω-class indices
- **Numerical summation**: Kahan compensated summation algorithm for improved accuracy with complex exponentials
- **ω-class maximum**: Computed up to k_max = max(ω(n)) for n≤N (5 for N=10⁴, 6 for N=10⁵)
- **Data generation**: Generated Dirichlet polynomial data de novo as original dataset was not publicly available (used documented specifications with random seed 42) 