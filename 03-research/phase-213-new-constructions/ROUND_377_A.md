# The intermediate block has positive excess and compensates the prefix

**Status: PROVED, with independent review of the shift and of the obstruction to discarding the prefix.**

At the exact cut of 368 let P_j=Σ_{k≤j}(−1)^k M_k, R_{j,K}=Σ_{j<k<K}(−1)^k M_k and K=floor(L/(2h)−L/h^(3/2)) as in 374. For any odd j in the growth range of 375 (or of 376), uniformly,

    R_{j,K}=−P_j(1+O(exp(−cL/h))),     R_{j,K} ≫ x/log x.

This prevents the strategy of paying for the intermediate zone alone with a one-sided square-root ceiling. Its compensation with the prefix is mandatory.

**Bound for the whole sum.** In the Mellin integral of 368 freeze z=L² at the evaluation scale. Shift from 1+1/L to σ=1−d, d=c₀/h, between heights ±2√L, with c₀ absolute and small. The rectangle lies strictly inside the classical free region used in 370; there |1/ζ|≤exp(O(h²)). For any point of the rectangle,

    log |E_z(s)| ≤ log E_z(1−d) ≪ Σ_{p≤z} p^(−1+d) ≪ exp(2hd) log log z.

The last estimate uses Mertens and the previous one that 1−d≥0.9. The Gaussian is integrable on the vertical and on the horizontals costs exp(−2L+O(1)); on the tails of the initial line the quotient E_z/ζ is an absolutely convergent series with coefficients of modulus ≤1, so it costs O(L) before the Gaussian. One obtains |S(x)|≪x exp(−c₁L/h), with c₁>0 absolute. This bound by itself has power exponent one.

**Comparison.** One has −P_j≥M_1−M_0≫x/L by grouping the pairs of 375 or 376 and by the PNT on [x,2x]. By 374, the modulus of the balance for k≥K is ≤exp((1/2+o(1))L). The identity R_{j,K}+P_j=S−Σ_{k≥K}(−1)^k M_k and the two previous bounds give |R_{j,K}+P_j|≪x exp(−c₁L/h). Dividing by −P_j absorbs L into the exponential with c<c₁. In particular there is an excess of even mass in the intermediate block for each sufficiently large x, even taking j=1. The relative bound obtained remains far above the square-root precision needed for criterion 372.

**Review record and scope of the obstruction.** The contour bounds are uniform and the factor exp(O(h²)) is absorbed because L/h≫h². On the initial tails the complete quotient E_z/ζ and its coefficients of modulus ≤1 are used; it is not split into two series with cut-dependent costs. The floor −P_j≫x/L is uniform in all admissible j; moreover j<K eventually. Hence R_{j,K} is positive at every sufficiently large scale, not only along a subsequence. Although removing P_j formally produces a majorant for S, the remaining block R_{j,K} satisfies no ceiling O(x^(1/2+ε)) with ε<1/2: its floor x/log x prevents it. This refutes that discard as a method to close the criterion, without refuting other groupings that keep the compensation between prefix and block.
