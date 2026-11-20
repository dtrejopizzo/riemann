## Overview ## Analysis Result: Unable to Complete Due to Computational Constraints ### Research Question
Determine whether the N-stable GEV statistics of the Liouville function L(s,λ) result from N-stable GEV statistics of its even-Ω(n) and odd-Ω(n) components. ### Finding
**The analysis could not be completed due to severe computational constraints.** The required computation of partial Dirichlet sums D(t;N) = Σ_{n≤N} λ(n) / n^(1/2+it) over the specified parameter ranges exceeded available computational resources. ### Computational Challenges Encountered **Primary Obstacle:** Computing partial sums for N=10^5 to 10^6 over 5000 t-values (as specified in the research objective) proved computationally infeasible within the available runtime limit (5400 seconds total, with individual cell timeouts at 1200 seconds). **Specific Issues:**
1. **N=10^6 computation**: Each vectorized computation over 1000 t-points for N=10^6 exceeded the 1200-second cell timeout
2. **Memory and computation scaling**: The vectorized approach requires O(N × n_t) operations with complex arithmetic, making N=10^6 prohibitively expensive
3. **Multiple attempts failed**: Reducing t-points from 5000→1000→500 and N from 10^6→2×10^5 still resulted in timeouts **Successful Components:**
- ✓ Implemented Liouville function λ(n) = (-1)^Ω(n) correctly
- ✓ Validated Ω(n) computation and even/odd decomposition
- ✓ Verified reconstruction: D_even + D_odd = D_total (numerical error < 10^-15)
- ✓ Confirmed implementation with small test cases (N=1000, t=100) ### Methodological Context from Literature Based on the primary dataset description and discovery reports, this analysis faces a known computational barrier: **From Dataset Description:**
> "The Möbius function, L(s,μ), is exceptionally computationally demanding, with analyses at N > 10^5 being infeasible with standard vectorized methods." The Liouville function L(s,λ) = ζ(2s)/ζ(s) shares similar computational characteristics with L(s,μ), involving cancellation-prone sums over sign-alternating coefficients. The dataset documentation explicitly identifies this as a computational bottleneck. **Previous Findings (r76):**
Analysis r76 successfully explained the N-stable covariance structure of L(s,λ) through decomposition into even-Ω and odd-Ω components, showing these components exhibit N-stable S_k covariance matrices that combine constructively. However, that analysis examined covariance structure, not GEV statistics of maxima. ### What Cannot Be Determined Without completing the computation, I cannot: 1. **Fit GEV distributions** to log|D| block maxima for D_total, D_even, D_odd at each N
2. **Extract shape parameters ξ** with confidence intervals for the six distributions (3 components × 2 N values)
3. **Test N-stability** by comparing whether ξ(N=10^5) and ξ(N=10^6) confidence intervals overlap
4. **Conclude** whether component stability explains total stability ### Theoretical Expectations **If the hypothesis is correct:**
- Both D_even and D_odd should individually show N-stable ξ (overlapping CIs between N=10^5 and 10^6)
- The total D should show N-stable ξ (already established in previous work: f24, f25)
- This would provide a complete mechanistic chain: component stability → total stability **If the hypothesis is incorrect:**
- Components might show N-dependent ξ while total remains stable
- This would suggest a more complex interaction mechanism beyond simple additive combination ### Recommendation for Future Analysis To complete this analysis successfully, one would need: 1. **Optimized implementation**: Use C/Fortran extensions or GPU acceleration for the partial sum computation
2. **Reduced scope**: Test at N ∈ {10^4, 10^5} instead of {10^5, 10^6}
3. **Coarser t-sampling**: Use 500-1000 t-points maximum
4. **Parallel processing**: Distribute t-grid computation across multiple cores
5. **Pre-computed data**: Generate and store the time series data separately, then perform GEV analysis Alternatively, if previous trajectories (f24, f25, r76) contain pre-computed data for L(s,λ), those datasets could be directly analyzed for the component decomposition. --- ## Discretionary Decisions Due to the inability to complete the analysis, no discretionary analytical decisions were made. The following computational approaches were attempted: - **Attempted N values**: 10^5, 10^6 (as specified), then 10^5, 2×10^5 (adjusted)
- **Attempted t-point counts**: 5000 (specified), reduced to 1000, then 500
- **Summation method**: Vectorized numpy operations (Kahan summation impractical for vectorized case)
- **Implementation validated**: Small-scale test (N=1000, single t-value) confirmed correctness No external datasets were retrieved, as the analysis requires computational generation of time series data. 