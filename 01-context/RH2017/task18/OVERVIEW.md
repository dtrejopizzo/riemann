## Overview The GEV shape parameter ξ for R_comp block maxima PARTIALLY separates the four function classes, but NOT as hypothesized. Structured multiplicative functions (ζ, L(χ₅)) clearly exhibit bounded tails with ξ = -0.175 [-0.247, -0.101] and ξ = -0.153 [-0.254, -0.030] respectively (95% CIs exclude 0, p < 0.05 vs f_rand). However, both random multiplicative (f_rand) and non-multiplicative (L_DH) functions show weak or bounded tails: f_rand has ξ = 0.079 [-0.022, 0.166] (CI includes 0, Gumbel-like) and L_DH has ξ = -0.081 [-0.183, 0.005] (CI includes 0, bounded). The hypothesized heavy-tail group (ξ > 0) for f_rand and L_DH is NOT observed. Statistical significance is only achieved when comparing structured multiplicative functions against f_rand (p = 0.004 and 0.016), but not against L_DH (p > 0.16). The R_comp metric exhibits fundamentally different extreme value behavior compared to partial sum magnitudes, with L_DH unexpectedly clustering with the bounded-tail structured functions rather than showing heavy tails. DISCRETIONARY ANALYTICAL DECISIONS:
• Used unnormalized magnitude |Σ| = R_comp × count instead of normalized R_comp for GEV analysis due to numerical precision issues with very small normalized values (order 10⁻⁵)
• Set N = 10⁵ truncation length for computational feasibility
• Used t-range [1000, 20000] with step=1, yielding 19,001 sample points
• Extracted 200 block maxima (block size ~95 points) for adequate sample size
• Applied GEV fitting using scipy.stats.genextreme (note: scipy uses c = -ξ convention)
• Generated 1,000 bootstrap resamples for 95% confidence intervals using percentile method
• Performed permutation tests with 1,000 permutations for pairwise comparisons
• Set significance threshold α = 0.05 for hypothesis tests
• Used Kolmogorov-Smirnov test for goodness-of-fit assessment
• Implemented Davenport-Heilbronn function with a_n = 0 for all non-squarefree n (verified correct)
• Implemented L(s, χ₅) using real character mod 5 with Legendre symbol (n/5) (verified correct)
• Generated random multiplicative function f_rand with seed=42
• Computed R_comp from composite squarefree terms (ω(n) ≥ 2 and squarefree) 