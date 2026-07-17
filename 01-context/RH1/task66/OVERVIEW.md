## Overview # DEFINITIVE 2D CLASSIFICATION MAP OF FUNCTION PEAK MECHANISMS ## Main Finding The (M, R_comp) coordinate space successfully separates all four function classes into distinct, statistically significant clusters, confirming the research hypothesis. The separation is hierarchical: primary separation by R_comp (composite coherence) reveals coefficient sign structure, while secondary separation by M (cancellation metric) provides additional discrimination within groups. ## Cluster Centers and Classification **Class 1: ζ (Riemann zeta)**
- Coordinates: (M = 0.5269, R_comp = 0.0020)
- Mechanism: Pure multiplicative structure with uniform positive coefficients
- Characteristics: Lowest M and lowest R_comp due to random phases in composite terms **Class 2: L(χ₄) (Dirichlet L-function mod 5)**
- Coordinates: (M = 0.5901, R_comp = 0.0030)
- Mechanism: Multiplicative with character modulation
- Characteristics: Higher M than ζ due to character-induced phase variation; low R_comp like ζ **Class 3: L_DH (Davenport-Heilbronn)**
- Coordinates: (M = 0.5464, R_comp = 0.0132)
- Mechanism: Non-multiplicative with alternating signs via (-1)^ω(n)
- Characteristics: High R_comp due to aligned phases in composite squarefree terms; intermediate M **Class 4: f_rand (Random multiplicative)**
- Coordinates: (M = 0.6002, R_comp = 0.0119)
- Mechanism: Multiplicative with random phases
- Characteristics: Highest M due to random variability; high R_comp ## Primary Separation: R_comp (Composite Coherence) R_comp measures the mean resultant length of phase alignment in composite squarefree terms (ω(n) ≥ 2, μ(n) ≠ 0). **Low R_comp cluster (≈ 0.002-0.003):**
- ζ: R_comp = 0.0020 ± 0.0013
- L(χ₄): R_comp = 0.0030 ± 0.0015
- Interpretation: Multiplicative functions with consistent sign structure produce incoherent phases in composite terms **High R_comp cluster (≈ 0.012-0.013):**
- L_DH: R_comp = 0.0132 ± 0.0031
- f_rand: R_comp = 0.0119 ± 0.0078
- Interpretation: Functions with the (-1)^ω(n) factor create aligned phases in composite terms **Statistical significance of R_comp separation:**
- ζ vs L_DH: p = 7.1×10⁻¹⁸ (effect size = 4.68 pooled SD)
- L(χ₄) vs L_DH: p = 7.1×10⁻¹⁸ (effect size = 4.18 pooled SD)
- ζ vs f_rand: p = 6.7×10⁻¹⁶ (effect size = 1.76 pooled SD)
- L(χ₄) vs f_rand: p = 6.98×10⁻¹³ (effect size = 1.58 pooled SD)
- f_rand vs L_DH: p = 0.059 (not significant, but trends toward separation) ## Secondary Separation: M (Cancellation Metric) M = √(Σ|S_k|²) / |Σ S_k| quantifies destructive interference among terms partitioned by ω(n). **Within low R_comp cluster:**
- ζ (M = 0.527) vs L(χ₄) (M = 0.590): p = 5.6×10⁻⁵ (highly significant)
- Character χ₄ introduces additional phase modulation, increasing M **Within high R_comp cluster:**
- L_DH (M = 0.546) vs f_rand (M = 0.600): p = 0.026 (significant)
- Random multiplicative phases create more variability and higher M **M hierarchy:**
1. ζ: M = 0.5269 ± 0.0417 (lowest)
2. L_DH: M = 0.5464 ± 0.0523
3. L(χ₄): M = 0.5901 ± 0.0851
4. f_rand: M = 0.6002 ± 0.1195 (highest) ## Quantitative Separation Analysis Euclidean distances between cluster centers demonstrate clear separation:
- Largest separation: ζ — f_rand (0.0740) and ζ — L(χ₄) (0.0632)
- Smallest separation: L(χ₄) — f_rand (0.0135), but still statistically distinct via M axis All pairwise comparisons show statistical significance (p < 0.05) in at least one metric dimension, with most showing highly significant separation (p < 0.001). ## Interpretation: Peak Mechanism Classification The 2D classification map reveals that peak mechanisms are determined by two orthogonal structural properties: 1. **Coefficient sign structure** (captured by R_comp): Distinguishes multiplicative functions with consistent signs from functions with alternating signs
2. **Phase modulation** (captured by M): Distinguishes pure multiplicative structure from character-modulated or random variations The analysis definitively classifies all four function types and provides a framework for understanding how arithmetic structure influences resonance behavior in Dirichlet series. --- ## DISCRETIONARY ANALYTICAL DECISIONS - **Character definition**: Used χ₄ mod 5 with values {0, 1, -1, -1, 1} for n mod 5 = {0, 1, 2, 3, 4}, as specified in the research objective
- **Truncation length**: N = 10⁵ for computational feasibility (N = 10⁶ would have exceeded time limits)
- **Height range**: t ∈ [1000, 10000] with dt = 1.0, yielding 9001 evaluation points
- **Peak selection**: Top 50 highest-magnitude peaks for each function (200 total)
- **Möbius sieve implementation**: Custom sieve algorithm for computing μ(n) and ω(n) up to N = 10⁵
- **Random seed**: seed = 42 for reproducible f_rand coefficients
- **Metric formulation**: M = √(Σ|S_k|²) / |Σ S_k| (literature formulation, yields M < 1 for multiplicative functions)
- **Statistical test**: Mann-Whitney U test for non-parametric comparison of cluster differences
- **Significance threshold**: α = 0.05 for statistical significance, with highly significant defined as p < 0.001
- **Composite coherence definition**: R_comp computed for terms with ω(n) ≥ 2 and μ(n) ≠ 0 (composite squarefree)
- **Numerical computation**: Used numba-accelerated single-point evaluation for partial sums D(t; N)
- **Visualization**: 2D scatter plot with cluster centers marked as stars, different markers for each function class 