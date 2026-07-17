## Overview ## Analysis of r-Divergence Mechanism: Sparsity vs Phase The r-divergence mechanism (power redistribution to higher ω-classes with increasing N) is **governed by coefficient sparsity, not phase**. ### Quantitative Results **f_real_rand (dense-real, 100% non-zero coefficients):**
- Mean entropy change N=10⁵→10⁶: +0.0269 (+1.69%)
- Variance fraction shift to k≥4: +0.0232 (+12.99%)
- Statistical significance: p=0.595 (entropy), p=0.466 (variance fraction)
- **Mechanism: ABSENT** (changes not statistically significant) **f_sparse_rand (sparse-complex, 60.8% non-zero coefficients):**
- Mean entropy change N=10⁵→10⁶: +0.1137 (+9.38%)
- Variance fraction shift to k≥4: +0.0490 (+232.74%)
- Statistical significance: p=4.71×10⁻⁵ (entropy), p=5.17×10⁻⁵ (variance fraction)
- **Mechanism: PRESENT** (highly significant increases in both metrics) ### Detailed Power Distribution Evolution For f_sparse_rand, power redistributes from low to high ω-classes:
- k∈{0,1,2}: 85.84% → 73.44% (−12.40%)
- k=3: 12.06% → 19.55% (+7.49%)
- k≥4: 2.11% → 7.01% (+4.90%) For f_real_rand, power distribution remains stable:
- k∈{0,1,2}: 63.89% → 63.79% (−0.10%)
- k=3: 18.25% → 16.03% (−2.22%)
- k≥4: 17.86% → 20.18% (+2.32%, not significant) ### Complete 2×2 Matrix | | **Sparse (~60%)** | **Dense (100%)** |
|--------------|-------------------|------------------|
| **Real** | Möbius: PRESENT (r44) | f_real_rand: ABSENT |
| **Complex** | f_sparse_rand: PRESENT | f_canon_rand: ABSENT (r44) | The mechanism appears in BOTH sparse functions (regardless of phase) and is absent in BOTH dense functions. This definitively establishes **sparsity as the key determinant**. --- ### DISCRETIONARY DECISIONS - Used grid-based peak finding (500 points for N=10⁵, 500 for N=10⁶) without local refinement at N=10⁶ due to computational constraints
- Set significance threshold at α=0.05 for hypothesis testing
- Used Shannon entropy with natural logarithm to quantify power distribution spread
- Defined "high ω-classes" as k≥4 following report r44 methodology
- Used two-sample t-tests to compare distributions between N=10⁵ and N=10⁶
- Applied vectorized numpy summation (replacing Kahan summation in some operations) for computational efficiency at N=10⁶
- Generated f_sparse_rand using f_canon_rand prime coefficients with seed=42 (reproducing established methodology)
- Analyzed top 50 peaks at each N to ensure robust statistical power
- Used t ∈ [N, 2N] convention for evaluation range at each truncation level 