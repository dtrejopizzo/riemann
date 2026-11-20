# Cost of taking absolute values between two bands

Prior independent cross-check with BUILD084 (18), 213-022, the discard of the lacunary family in the index and 212 ROUND095_A. Here only the term-by-term domination that would allow adding the budgets of 022 is examined. The example uses the full physical matrix and vectors with both moments zero in each band.

Take the integer bands [12,24), [12R,24R), R a large integer. In the first choose a unit vector u supported on 12,13,14 and orthogonal to 1 and l_j=log(1+1/j). One has |u₁₂|>0 because l₁₃≠l₁₄. In the second split into the three consecutive intervals of length 4R. For the constant values of w on them choose a fixed vector of three coefficients orthogonal to (1,1,1) and to (log(16/12),log(20/16),log(24/20)). The telescoping of l_j gives exactly both moments. Normalize in Euclidean norm over the cells: on the first interval |w_j|=c/√R, c>0 independent of R, because the last two logarithms differ.

For R<n≤(6/5)R the n cells j=12n,...,13n−1 lie entirely in [12R,16R). In each one the arithmetic entry of row 12 includes Λ(n)/n; the off-diagonal archimedean term has the same sign in M. When summing, even when distinct n visit a cell, their weights add. Consequently

    Σ_{i,j}|u_i M_ij w_j| ≥ c|u₁₂| R^(−1/2) Σ_{R<n≤6R/5} Λ(n) ≫ √R,

by the prime number theorem. Each norm is one. The budgets D of 022 for these two bands are O(1) and O(log R); the growth obtained exceeds even their sum. Hence there is no uniform constant to pay the absolute crossing by the sum of the local quadratic budgets D₁||u||²+D₂||w||², even imposing the two moments separately.

The lower inequality refers to the sum of moduli of the summands, before any cancellation. It leaves open an estimate of the signed crossing and a specific estimate for the adaptive arithmetic residues of 022. PROVED after independent mathematical audit.
