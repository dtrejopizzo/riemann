# Effective crossings beyond the fourth power by a doubly logarithmic factor

For almost every t∈[1,2] there exist C_t>0 and a sequence x→∞ with cutoffs

    √x ≤ y ≤ x/[C_t (log x)^4 (log log x)^2],
    |R_t(x,y)| ≪_t √x.

This is an existence statement **without RH** along a sequence of scales. It is not claimed for the exceptional row t=0. It proves that the oscillation band of 307 reaches beyond the pure fourth power, although it remains below any fixed power 4+ε at the upper end of y prescribed here.

**Comparison cutoff.** Parametrize x by z→∞ via L=log x=z^(1/4)/(d(log z)^a), d>0 fixed, 0<a≤1/2. It is eventually increasing and z∼4^(4a)d⁴ L⁴(log L)^(4a). At the comparison cutoff x/z put F=−LR_t(x,x/z)/(2x). The expansion of 306 to three terms gives

    F=H₀+d z^(−1/4)(log z)^a H₁+d² z^(−1/2)(log z)^(2a) H₂
        + O(z^(−3/4)(1+log z)^C).

H₂(z)=D_t''(1)+O_N((log z)^(−N)) for all N: use the bound of 294 for the tails of the moments up to degree two and for B_t(z)P₂(log z)/z. The moments of degrees zero and one vanish. The Mellin transform of the term H₂ minus its constant, including its weight, is absolutely bounded up to the boundary Re s=−1/2. The constant part contributes d²D_t''(1)Γ(1+2a)(s+1/2)^(−1−2a), up to an entire modification from the lower endpoint.

**The first-order term.** Let M be the Mellin transform of H₁ given in 306. The additional weight (log z)^a has Mellin transform applied to H₁ equal to

    [a/Γ(1−a)] ∫₀^∞ [M(s)−M(s+u)] du/u^(1+a).

The identity is obtained by integrating 1−exp(−u log z), initially under absolute convergence. The integral gives holomorphic continuation near each point whose horizontal ray to the right is free of singularities of M, within its meromorphic domain. For small u the difference is O(u) locally uniformly; for large u, M(s+u) is uniformly bounded by the convergent representation. The shift z^(−1/4) evaluates this expression at s+1/4. On the real ray from −1/4 there is no singularity, including the origin because of the double zero of D_t at 1.

**Oscillation.** Take the critical zero and the generic frequency of 307. If D_t has poles strictly to the right of ρ at the same height, choose the one with largest real part; otherwise use ρ. At the point shifted by −1, the term H₀ keeps the pole and the ray of H₁ is free by the above choice. For the interior point Landau suffices, as in 307. For the boundary point, the term H₂ is bounded when approaching that nonreal height from the right, by the separation of its constant. On the real axis the full Mellin transform at −1/2+h grows at most like d²D_t''(1)Γ(1+2a)h^(−1−2a)+O(1). The complex pole has order 2r≥2 and leading coefficient A≠0 independent of d. Comparing the Mellin transform of a supposed eventual majorant or minorant c z^(−1/2)log z exactly as in 307, one obtains both oscillations of magnitude ≫z^(−1/2)log z. This holds for every fixed d if a<1/2; at a=1/2 choose d small enough that d²D_t''(1)<|A|/2, and then c<|A|/2. In the case of an interior pole any d works. The regularity on the open real line up to the boundary, needed for Landau, follows from the same three terms.

**From the sign to a balanced cutoff.** At a=1/2 one obtains arbitrarily large x where the block at x/z is positive; at √x it is negative by 294. Between the two endpoints, a jump has modulus 2u_p |B_t(x/p)|≪√x by the unconditional bound of 294, since x/p≤√x. The first crossing provides the cutoff of the statement; take, for example, C_t=8d⁴ in the asymptotic equivalence for z. Detection via 306 requires exceeding a fixed power 4+ε; the factor gained here does not reach that scale. The new conclusion uses boundary oscillation and does not estimate the complementary block.
