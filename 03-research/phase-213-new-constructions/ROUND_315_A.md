# Unavoidable cost of the two orientations of the balance for the whole divisor matrix

Let D=x^o(1), λ₁=1 and w_λ the family of weights of 314. For almost every fixed t in [1,2] and each fixed, arbitrarily large V, there exist two fixed intervals of arguments contained in (V,∞), one with B_t strictly positive and another with B_t strictly negative. In each interval the sum of the absolute values w_λ(n)|B_t(x/n)|, over the indices whose argument belongs to the interval, is at least

    c_(V,t) x log x / log²(2D).

The threshold and the constant may depend on the intervals, but the inequality is simultaneous over all normalized real vectors, even chosen depending on x. It also holds for v_λ of 314, which dominates w_λ pointwise. Hence no vector of that matrix can make the negative contributions negligible in modulus while keeping the main sample with coefficient one. The estimate does not rule out their signed cancellation with the positive ones.

**The exact minimum of the density.** Use the orthogonal basis and the inversion of 314, now at s=1. If N_d=||Z_d||², the normalization says 1=Σ μ(d)q(d)b_d and h_λ(1)=Σ N_d b_d². By Cauchy–Schwarz and the invertibility of the triangular change of basis,

    min_(λ₁=1) h_λ(1) = 1/G_D,    G_D=Σ_(d≤D) μ²(d) ∏_(p|d) q_p(1)/(1−q_p(1)).

Here q_p(1)=2/p−1/p² is the probability of exponent at least one; the minimum is attained by taking b_d proportional to μ(d)q(d)/N_d. The non-squarefree indices are included in the optimization. By Mertens' product, G_D≤∏_(p≤D)(1−1/p)^(−2)≪log²(2D). Moreover, without normalizing, h_λ(1)≥D^(−10)||λ||∞² by the same inversion: each tail probability is ≥p^(−e) and 1−r_e≥1/4, enough for N_d≥d^(−8).

**Mass in any proportional interval.** With A=h_λ(1) and E as in 311, for v≥D⁴ the partial sum of w_λ up to v equals v(A log v+E)+O(√v D⁶||λ||∞²), by the norm of 314 and the divisor formula. Freeze λ and D, even if they depend on x. At v=√x nonnegativity forces E≥−(A/2)log x−o(A), since D=x^o(1). Subtract the formulas at v=bx and v=ax with fixed 0<a<b. The terms with log a and log b cost O_(a,b)(Ax), and the error is o(Ax) uniformly in λ. A mass ≥(b−a)Ax log x/3 remains for large x. Thus the bound of the previous paragraph becomes a lower bound for samples in real intervals, not only for a Dirichlet multiplier.

**Both signs exist at arbitrarily large arguments.** For the generic frequencies of 307, D_t has a pole of order ≥2 at a fixed critical zero ρ. The Mellin transform of the partial sum B_t(v) is D_t(s)/s. If B_t eventually had a single sign, Landau and real regularity in s>1/2 would give absolute convergence in that half-plane. At s=1/2+h the Mellin transform stays bounded by 307. After removing a compact set, the transform at that real abscissa would dominate the modulus at ρ+h, contradicting the pole (if there is an interior pole, convergence is already impossible). Hence for each V there exist two intervals between integers greater than V with strictly opposite signs. On each, B_t is a nonzero constant. The corresponding indices n occupy an interval proportional to x and the mass estimate proves the statement.

In particular for 0≤t≤1 and before the trimming of 311 one can directly use the arguments [1,2) and [2,3), where B_t equals 1 and 1−2(1+cos(t log 2)), respectively. The pole argument is what allows placing the two contributions after any fixed trimming, at generic frequency. No uniform constant is claimed for a prescribed trimming V(x) growing with x. The quadratic minimum is the elementary Selberg-type optimization; what is restrictive here is its consequence for the two orientations of the balance B_t in the extraction problem.
