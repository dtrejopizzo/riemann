## Overview ## ANSWER **The hypothesis that Three-Index Type A (3A) term dominance in the fourth moment M₄ strengthens with increasing N is REJECTED.** The comprehensive M₄ decomposition analysis across N ∈ {10⁴, 10⁵, 10⁶} reveals **non-monotonic behavior** rather than the predicted monotonic strengthening: ### Quantitative Evidence **Ratio of 3A to MD contributions (Top 10% |M₄| regime):**
- N = 10⁴: **-0.169** (3A contributes -6.0%, MD contributes 35.6%)
- N = 10⁵: **+1.731** (3A contributes 38.2%, MD contributes 22.1%)
- N = 10⁶: **+0.722** (3A contributes 21.9%, MD contributes 30.3%) The ratio **increases dramatically** from N=10⁴ to N=10⁵ (+1.90), but then **decreases substantially** from N=10⁵ to N=10⁶ (-1.01), directly contradicting the hypothesis of monotonic strengthening. ### Complete M₄ Decomposition **Percentage contributions to M₄ (Top 10% |M₄| regime):** | | Pure Diagonal | Mixed Diagonal | Three-Index A | Four-Index |
|-------|---------------|----------------|---------------|------------|
| N=10⁴ | 19.3% | 35.6% | -6.0% | 51.1% |
| N=10⁵ | 27.3% | 22.1% | 38.2% | 12.5% |
| N=10⁶ | 16.5% | 30.3% | 21.9% | 31.2% | **All term groups exhibit non-monotonic trends:**
- **PD and 3A**: peak at N=10⁵
- **MD and 4I**: valley at N=10⁵ At N=10⁴, the M₄ structure is dominated by Four-Index (51%) and Mixed Diagonal (36%) terms, with 3A actually **negative** (-6%). At N=10⁵, there is a dramatic reorganization with 3A surging to 38% dominance while 4I collapses to 12%. At N=10⁶, the structure partially recovers to a more balanced state with MD (30%), 4I (31%), and moderate 3A (22%). ### Interpretation N=10⁵ appears to represent a **transition regime** rather than a step in asymptotic convergence. The system has not reached asymptotic behavior by N=10⁶, consistent with prior findings (r22) that r-distributions are **diverging** rather than converging across this N-range. The 3A dominance observed at N=10⁶ in report r23 is not an emergent asymptotic feature strengthening with N. Rather, it represents a **partial recovery** from the extreme transient enhancement at N=10⁵. --- ## DISCRETIONARY DECISIONS - **M₄ definition**: Defined as Σ_{i,j,k,l} S_i S_j S̄_k S̄_l (total fourth-moment energy across ω-class interactions), not |D|⁴
- **Term group classification**: Used standard categorization: PD (i=j=k=l), MD (two pairs equal), 3A (three indices in specific pattern), 4I (all distinct)
- **Combinatorial factors**: Applied factor of 4 for 3A terms and factor of 4 for 4I terms to account for index permutations
- **Conditional threshold**: Used top 10% of |M₄| values for high-magnitude regime analysis (90th percentile)
- **Grid resolution**: 500 t-points per N value in interval [N, 2N]
- **t-range convention**: Used [N, 2N] interval as established in dataset methodology
- **ω-class definition**: 8 classes based on prime factorization structure (standard classification from dataset)
- **Numerical precision**: Kahan compensated summation for all Dirichlet sums (required by dataset methodology) 