# Norm of the crossing after cancelling within triples

The index, selection after the joint control 212-84, already describes the triples and the grouping of edges by divisibility. The jump coordinates (XXXI) also isolate the edge. Here an operation pending in that antecedent is quantified: the norm of the crossing between two bands on the subspace of disjoint packets. The obstruction 023-A applies the modulus before cancellation.

Let K,R be integers, K≥1 and R≥4. On the cells of [K,2K) any vector u; on [RK,2RK) disjoint triples of consecutive cells. In each triple P=[j,j+3) choose a unit vector e_P with zero sum and zero inverse moment. For w=Σ t_P e_P one has ||w||=||t||. With the physical matrix M of BUILD084, there is an absolute constant such that

    |u* M w| ≤ C sqrt(log(2RK)/R) ||u|| ||w||.

For the comb, compress the columns against the e_P before taking moduli. In row i, each contributing n satisfies R/2<n<2R (the endpoints with equality do not matter either). The interval [ni,n(i+1)) partially meets at most two triples; each partial sum has modulus ≤√3. Complete triples pay zero. The absolute row sum is therefore O(Σ_{R/2≤n≤2R}Λ(n)/n)=O(1) by Chebyshev. In the column starting at j, an endpoint of the interval must coincide with j+1 or j+2. For each of these integers m only divisors n of m intervene, with at most two choices of i. The absolute column sum is O((log(j+1)+log(j+2))/R), by Σ_{n|m}Λ(n)=log m. Rectangular Schur gives the indicated bound.

The separated archimedean block has entries O(1/(RK)) by BUILD084 (3), given that the physical distance is at least RK/2. Its Hilbert–Schmidt norm is O(1/√R) even before compressing the columns. Both bounds keep total freedom in the head. Only zero sum on the triples was used; the inverse moment allows choosing them primitive. The estimate does not control the component of the tail that has arbitrary means per triple. Lemma independently reviewed.

## Consequence on all scales of a tail

Additional independent cross-check with P47 lem:ext-hf (window-dependent threshold), 212-83 and the triple selection after BUILD084. Let N_k=3·2^k for k a nonnegative integer. Partition [N_k,2N_k) into disjoint consecutive triples. For k≥k₀ and every finite combination w of the previous primitive packets, we write w_k for the part in that band. There exist absolute constants and k₀ sufficiently large such that

    a(Uw) ≥ (1/2) Σ_{k≥k₀} log(N_k) ||w_k||².

The bands cover the tail and the triples of this partition have disjoint support even when changing band. For the archimedean block, the diagonal of BUILD084 is log j+O(1) uniformly. The off-diagonal remainder has norm O(1) acting from packet coefficients to cells. Indeed, in row i and triple starting at j with |i−j|≥5, subtracting the entry of its first cell from the other two does not change the product. The integral formula for h of BUILD084 gives |h(m+1)−h(m)|≤1/m² for m≥1. Applied to h(i+j) and h(|i−j|−1), it gives a compressed entry O((1+|i−j|)⁻²); for |i−j|<5 the off-diagonal entries are uniformly bounded and zero is put on the diagonal of the remainder. This majorant has uniform row and column sums. Schur and the synthesis isometry pay O(||w||²).

For the comb within a band or between neighbouring bands there are only n≤4. For each n a row of the oriented matrix has at most n contacts and a column at most one. Thus the block and its transpose have norm O(1) before compressing. For l≥k+2 use the previous comb lemma with R=2^(l−k), K=N_k. When normalizing each band by the weight sqrt(log N_k), the norm of that block divided by sqrt(log N_k log N_l) is at most

    C 2^(−(l−k)/2) / sqrt(log N_k),

since log(2N_l)/log N_l is bounded. By symmetry the same majorant uses min(k,l) and |k−l| for the other triangle. In the scalar matrix of normalized block norms, both row and column sums are bounded by C/sqrt(log N_{k₀}) by the geometric series; the three nearby diagonals cost O(1/log N_{k₀}). Applying Schur to the sequence sqrt(log N_k)||w_k|| controls the full comb. The diagonal dominates the two errors for large k₀, and gives the statement.

The cut is existential. The upper limit of the support and the number of bands are free. The argument admits a fixed multiple of the comb by increasing the cut, so localizing the sign for the true weights still requires controlling the complementary modes and their crossings. PROVED after independent mathematical review of the multiscale consequence.
