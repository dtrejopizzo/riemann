# A model on logarithmic cells with integer data and subexponential error

In 224 the representation by counts between squares still needs exponentially many cells relative to k for a linear order N=jk. Here the same rate is obtained with O_j(k) cells and O_j(k²/log k) integers. Each integer is rounded with absolute error up to 1/2. This is a reduction of the volume of data required to evaluate the sample once precomputed; it is not a polynomial-time algorithm to obtain them from the primes.

Fix b>1/2, n a nonnegative integer and m_n=ceil(b n/log(n+2)). Store, for 0≤r≤m_n,

    T_(n,r) = nearest integer to Σ_(n≤log p<n+1) (log p)/√p · (log p−n)^r.

In particular the cells and the data are independent of the order, of j and of the rate. Take N=jk, U_k=max(4,log log(k+20)), L_N(u)=2N log M₁(u). For sufficiently large k, form

    Y_(k,j) = ∫₃^U_k u^(s_k−1) Σ_(0≤n<floor L_N(u)) Σ_(r=0)^m_n
                 T_(n,r) c_N^(r)(n;u)/r! du.

Then limsup log(1+|Y_(k,j)−C_(k,j)|)/k=0 for each fixed j. In particular the ordinary limit of log(1+|Y|)/k is max(0,Θ−d_j) from 224. It would suffice to bound these combinations of the integer data along a subsequence for each j in an unbounded set.

**Two ends of the cut.** For u≥U_k the absolute bound of 216 with contour of height 1/2 gives C poly(N) exp(N log M_(1/2)(U_k)); the proof works with the weight of 217 since |u^(s_k−1)|≤1. For fixed j its positive logarithm is o(k). For u≤U_k discarding the final incomplete cell costs O(u) before the integral: by the height-one contour, |c_N(log p;u)|≤Cu M₁(u)^N/p and by Chebyshev Σ_(p≥exp(floor L)) (log p)p^(−3/2)≤C exp(−L/2). This includes any atom at a cut endpoint. The product M₁(u)^N exp(−L/2) is one.

**Approximation on complete cells.** For r≤N−1, on the real line

    sup_t |c_N^(r)(t;u)| ≤ C u (4u)^r.

Indeed |τ|H_u(τ)≤4u and ∫H_u^(N−r)≤∫H_u=O(u). Every n used is O(N), so m_n+1≤N−1 for large k. The rounding error per cell costs O(u exp(4u)) by the exponential expansion. The real mass before Taylor is O(exp(n/2)) by Chebyshev. The Taylor error on the cell is thus

    O(exp(n/2) u (4u)^(m_n+1)/(m_n+1)!).

For n≤√k sum with the ceiling O(exp(√k/2)U_k exp(4U_k)), per cell, still subexponential. For √k<n≤O_j(k), the factorial bound m!≥(m/e)^m gives logarithm ≤(1/2−b+o(1))n uniformly: log(m_n+1)=log n−log log n+O_b(1), while log(4U_k)=o(log k). Thus the errors on the remaining cells are summable and the total error after the integral is exp(o(k)). The number of moments is O_j(k²/log k), each datum requires O_j(k) bits by the same mass ceiling, and O_j(k³/log k) bits suffice in total. Storing individual positions of the primes is not required in the evaluation.

**What was gained compared with the counting comparison.** The positions can vary greatly within cells of width one in logarithms, but matching the above moments up to bounded errors suffices to transfer the criterion. It is not required that the two counts differ by O_ε(x^(1/2+ε)) at the interior cuts as in the sufficient condition of 224. The cost is controlled by smoothness of the kernels at growing differentiation orders. The arithmetic problem is the cancellation among the authentic moments. Their roundings and the number of bits do not establish that cancellation.
