# Spectral count at the full cell cut

Let M_X be the pole-free physical matrix of BUILD084 (3) on all cells with indices 1,...,X, with X an integer. One has

    n_{≤0}(M_X) = O(X/(log X)²).

The same majorant holds when restricting to the two primitive moments and for the form with poles on all cells (perturbation of rank at most two). Antecedents cross-checked: matrices of 212-59/75, counts of P47 prop:NC and lem:ext-hf, and the group floor of 025. Bessel's inequality is classical. Here the separation of the contacts in the tail allows applying it to the full arithmetic sum.

Remove the first ⌈√X⌉ coordinates. For remaining i<j, the interval j/(i+1)<n≤j/i has length j/(i(i+1))<1. Hence the arithmetic entry is zero or a single weight Λ(n)/n. For each n there are at most ⌊X/n⌋ possible indices i and at most n indices j per i. Counting both triangles, the sum of squares of the arithmetic entries is at most 2X Σ_{n≥2} (log n/n)²=O(X). By h(m)≤C/(m+1) the off-diagonal archimedean entries are O(1/|j−i|), with sum of squares O(X). The matrix E of all off-diagonal terms of the tail thus satisfies ||E||²_HS=O(X). The diagonal D has minimum δ≥(log X)/2−O(1) by (3).

On a nonpositive subspace of the retained block, each unit vector z satisfies δ≤−⟨z,Ez⟩≤||Ez||. Summing over an orthonormal basis gives dimension ≤||E||²_HS/δ² for large X. Restoring the initial coordinates adds at most ⌈√X⌉ to the nonpositive index by intersection of subspaces. This proves the statement. The argument also admits cΛ for a fixed c. Its conclusion quantifies the fraction of nonpositive eigenvalues; it leaves open the existence of a single one. The parameter X measures cells and the logarithmic half-length of the cut is (log(X+1))/2. PROVED after independent mathematical review.
