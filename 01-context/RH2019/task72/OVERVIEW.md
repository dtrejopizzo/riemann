## Overview ## Analysis Complete: Character-Conjugate Structure Does NOT Produce S₂ Dominance ### Summary of Results The synthetic function F_conj(s) = L(s, χ₅) + i·L(s, χ̄₅) was constructed to test whether character-conjugate interference could be the mechanism underlying L_DH's anomalous S₂-dominance. Analysis of the top 20 highest-magnitude peaks at N=10⁶ in t∈[10⁶, 2×10⁶] reveals: **Key Findings:**
- Mean S₂ perturbation reduction: 26.60% (std: 11.20%)
- Mean S₃ perturbation reduction: 33.03% (std: 11.90%)
- S₂ dominant peaks: 6/20 (30%)
- S₃ dominant peaks: 14/20 (70%)
- Paired t-test: t = -1.430, p = 0.169 (NOT significant) **Conclusion:** The character-conjugate structure does NOT produce consistent S₂ dominance. In fact, S₃ shows greater average causal influence (33.0% vs 26.6%), though the difference is not statistically significant (p=0.169 > 0.05). ### Mechanism Analysis **Power Distribution:** Unlike a consistently S₂-dominant function, F_conj exhibits distributed power across multiple ω-classes:
- Mean S₂ power: 18.9%
- Mean S₃ power: 22.3%
- Mean S₄ power: 24.4% (highest!) **Local vs Global Dominance:** The strong correlation between S₂/S₃ power ratio and reduction difference (Pearson r=0.68, p=0.001; Spearman ρ=0.78, p<0.001) demonstrates that dominance is a LOCAL property determined by peak-specific ω-class power distributions, not a global structural feature of the function. For S₂-dominant peaks (n=6): Mean S₂ power = 27.4%, Mean S₃ power = 10.9%
For S₃-dominant peaks (n=14): Mean S₂ power = 15.2%, Mean S₃ power = 27.1% ### Comparison with Previous Studies **r63 (L(s, χ₃) + L(s, χ₅)):** Real-valued, failed to produce consistent dominance, showed peak-dependent behavior. **Current study (F_conj):** Complex-valued, character-conjugate structure, 80% density. Result: Also shows peak-dependent behavior with NO consistent S₂ dominance. Both synthetic functions fail to replicate L_DH's anomalous causal structure despite being non-multiplicative and having arithmetic coefficient structures. ### Scientific Implications The hypothesis that character-conjugate interference is the mechanism for L_DH's S₂-dominance is **REJECTED**. The simple linear combination of a character and its conjugate does not produce the required causal structure. This suggests that L_DH's anomalous behavior arises from deeper arithmetic properties beyond:
1. Non-multiplicativity alone
2. Character-based coefficient structure
3. Density patterns
4. Character-conjugate interference The mystery of L_DH's S₂-dominance remains unsolved and likely requires investigation of its unique arithmetic construction involving the Möbius function and square-free sieve. --- ## Discretionary Analytical Decisions - **Character choice:** Used the primitive character χ₅ (mod 5) to construct F_conj, chosen for its simple structure and comparability with previous r63 study
- **Peak selection:** Top 20 peaks by magnitude, consistent with dataset protocol and sufficient for statistical power
- **t-range:** Used t∈[N, 2N] = [10⁶, 2×10⁶] following established convention for N-dependence studies
- **Coarse grid spacing:** 100-unit spacing for initial peak search, balancing computational efficiency with resolution
- **Fine grid resolution:** 201 points in ±100 window around coarse peaks for refinement
- **Statistical test:** Paired t-test selected as appropriate for within-peak comparisons of S₂ vs S₃ perturbations
- **Significance threshold:** α = 0.05 for determining statistical significance
- **Correlation methods:** Computed both Pearson (parametric) and Spearman (non-parametric) correlations to assess robustness
- **Summation method:** Kahan compensated summation for all final peak evaluations and ω-class decompositions, ensuring numerical precision
- **Peak prominence threshold:** Minimum prominence of 5.0 for initial peak detection, filtering noise while retaining all significant peaks
- **Minimum distance:** 10-point minimum distance between detected peaks to avoid duplicate identification of the same structure 