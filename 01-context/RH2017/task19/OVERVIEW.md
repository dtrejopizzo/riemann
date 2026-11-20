## Overview # ANSWER TO RESEARCH HYPOTHESIS The hypothesis is **CONFIRMED**: The multiplicative structure of f_rand generates a significantly heavier-tailed distribution of partial sum magnitudes than a function with fully random (non-multiplicative) coefficients. ## Quantitative Evidence ### Percentile Comparison (99th, 99.9th, 99.99th)
- **99th percentile**: f_rand = 13.87, f_fully_rand = 7.27 (ratio: **1.91×**)
- **99.9th percentile**: f_rand = 26.26, f_fully_rand = 8.84 (ratio: **2.97×**)
- **99.99th percentile**: f_rand = 29.43, f_fully_rand = 9.79 (ratio: **3.01×**) The multiplicative function produces extreme values that are **1.9× to 3.0× larger** at the highest percentiles. ### Two-Sample Kolmogorov-Smirnov Test
- **K-S statistic**: 0.3948
- **p-value**: < 0.001
- **Conclusion**: The distributions are **significantly different** (p < 0.001). We strongly reject the null hypothesis that the two distributions are the same. ### Distribution Characteristics
| Metric | f_rand (multiplicative) | f_fully_rand (independent) | Ratio |
|--------|------------------------|---------------------------|-------|
| Maximum | 29.86 | 9.93 | 3.01× |
| Kurtosis | 22.72 | 0.06 | 378.7× |
| Skewness | 3.94 | 0.54 | 7.30× |
| Std | 2.68 | 1.57 | 1.70× | The excess kurtosis of 22.72 for f_rand indicates **extremely heavy tails**, while f_fully_rand has near-zero kurtosis (0.06), consistent with a normal distribution. ### Tail Behavior
The multiplicative structure produces extreme values that are completely absent in the independent random case:
- **|D(t)| > 10**: f_rand = 218 events (2.18%), f_fully_rand = 0 events (0.00%)
- **|D(t)| > 15**: f_rand = 77 events (0.77%), f_fully_rand = 0 events (0.00%)
- **|D(t)| > 20**: f_rand = 38 events (0.38%), f_fully_rand = 0 events (0.00%) Over the 10,001 sampled t-values, f_fully_rand **never** produces a magnitude exceeding 10, while f_rand produces 218 such events. ### Robustness Check
Testing f_rand (seed=42, fixed) against 5 different realizations of f_fully_rand (seeds: 123, 456, 789, 101112, 131415) confirms:
- All f_fully_rand realizations show 99.99th percentile ≈ 9-11 and max ≈ 9-11
- All f_fully_rand realizations show kurtosis ≈ 0-0.5 (near-normal)
- f_rand consistently shows 99.99th percentile ≈ 29 and max ≈ 29
- f_rand consistently shows kurtosis ≈ 26 (heavy-tailed) ## Scientific Interpretation The multiplicative constraint a_{mn} = a_m × a_n imposes long-range correlations among the Dirichlet coefficients. When a prime p has coefficient a_p = +1, all multiples of p inherit this sign pattern (modulo other prime factors). This creates **coherent phase alignment** across families of related integers, leading to constructive interference in the partial sum that produces occasional large peaks. In contrast, fully independent random coefficients lack any correlation structure. Each term in the sum contributes independently, and the central limit theorem drives the distribution toward normality with moderate tails. The result demonstrates that **multiplicative structure itself** is sufficient to generate extreme values, independent of any specific arithmetic properties (e.g., the precise distribution of primes or connection to zeta zeros). This provides a baseline for understanding the behavior of classical L-functions with Euler products. --- # DISCRETIONARY ANALYTICAL DECISIONS - **Random coefficient distribution**: Chose uniform ±1 coefficients rather than other distributions (e.g., complex phases, Gaussian) to match the setup of f_rand in the existing dataset and maintain comparability with prior analyses
- **Seed selection**: Used seed=42 for f_rand (to match existing analyses) and seed=123 for f_fully_rand (arbitrary choice for reproducibility)
- **t-range**: Selected t ∈ [1000, 2000] to avoid small-t regime where convergence may be slower and to provide sufficient sample size (10,001 points)
- **Resolution**: Set dt = 0.1 to balance computational cost with statistical resolution (10 samples per unit interval)
- **Truncation length**: Fixed N = 10^5 based on research objective specification
- **Numerical precision**: Implemented Kahan compensated summation to maintain accuracy, following dataset description protocol
- **Percentile thresholds**: Chose 99th, 99.9th, and 99.99th percentiles as specified in the research objective
- **Statistical test**: Used two-sample Kolmogorov-Smirnov test as specified in research objective; this is a standard non-parametric test for comparing distributions
- **Significance level**: Used α = 0.001 as threshold for "highly significant" given the large sample size (n = 10,001)
- **Tail count thresholds**: Selected thresholds {10, 15, 20, 25} based on observed maximum values to illustrate the divergence in extreme behavior
- **Kurtosis metric**: Computed excess kurtosis (normal distribution = 0) rather than raw kurtosis (normal = 3) for clearer interpretation
- **Robustness testing**: Chose 5 additional seeds for f_fully_rand validation (not required but performed to ensure results are not artifacts of specific seed)
- **Visualization**: Used empirical CDF for final figure as it clearly shows the tail divergence without binning artifacts 