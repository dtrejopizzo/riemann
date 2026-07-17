## Overview ## Analysis Complete: M4 Decomposition for Zeta Function at N=10^6 ### Main Result The hypothesis that four-index terms Re[S_j S_k S̄_l S̄_m] dominate the off-diagonal M4 contribution is **PARTIALLY REJECTED**. The unconditional M4 decomposition over 500 t-values in [10^6, 2×10^6] reveals: **Arithmetic Mean Contributions:**
- (a) Pure Diagonal (PD): 211.10 (11.5%)
- (b) Mixed Diagonal (MD): 412.39 (22.4%)
- (c) Three-Index Type A: -14.48 (-0.8%)
- (d) Three-Index Type B: 311.76 (17.0%)
- (e) Four-Index: 296.81 (16.2%)
- (f) Other 2-Index (3,1 pattern): 142.76 (7.8%)
- (g) Other 2-Index (2,2 pattern): 477.18 (26.0%) **Total off-diagonal (non-PD/MD): 1214.02 (66.1%)** ### Critical Finding The structure varies dramatically depending on the measurement approach: 1. **Arithmetic Mean**: 4IDX (16.2%) > |3IDX_A| (0.8%) ✓
2. **High-M4 Regime (top 10%)**: 3IDX_A (26.4%) > 4IDX (8.6%) ✗
3. **M4-Weighted Mean**: 3IDX_A (34.1%) > 4IDX (9.3%) ✗ At physically meaningful high-M4 points where the Dirichlet polynomial has large magnitude, **Three-Index Type A terms (|S_j|² S_k S̄_l) dominate at 26-34%**, contrary to the hypothesis. The four-index terms contribute only 8-9% in these regimes. ### Unexpected Discovery The largest single contributor to off-diagonal M4 is actually the "Other 2-index" category (33.7% arithmetic mean, 38.8% at high-M4), specifically terms with patterns like |S_j|² S_j S̄_k (3,1 pattern) and non-standard (2,2) patterns. These were not anticipated in the original problem specification but account for approximately one-third of the total M4. ### Comparison to r19 Report r19 stated that "off-diagonal" terms contribute ~85-93% of M4. Our unconditional analysis finds 66% (arithmetic mean), but this increases to 81% in the high-M4 regime (top 10%), which is more consistent with r19's peak-focused methodology. --- ## Discretionary Decisions - **Dataset generation**: Generated new data for N=10^6 using Kahan-compensated summation as specified in dataset documentation, with random seed 42 for reproducibility
- **Evaluation grid**: Used 500 equally-spaced t-values in [10^6, 2×10^6] following the N-dependent convention established in previous analyses
- **Term classification**: Implemented detailed classification scheme based on index structure (a,b,c,d) in S_a S̄_b S_c S̄_d expansion
- **High-M4 threshold**: Defined "high-M4 regime" as top 10% by M4 magnitude (threshold = 717.16)
- **Averaging methods**: Computed three complementary measures: (1) arithmetic mean, (2) high-M4 conditional mean, (3) M4-weighted mean, to capture different physical aspects
- **Category definitions**: Extended the original 5 categories (PD, MD, 3IDX_A, 3IDX_B, 4IDX) to include two additional significant 2-index patterns that emerged from the analysis
- **Omega computation**: Implemented standard ω(n) function (count of distinct prime factors) via trial division for all n ≤ 10^6 