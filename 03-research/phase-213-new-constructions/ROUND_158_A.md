# Subtracting the elementary weight keeps the critical error per unit of tilt

With E_d,J_d,G,b of 157 and E_0(u)=G(u)+1/2, there are absolute c,C,u₀>0 such that

    c d u ≤ E_d(u)−E_0(u) ≤ C d u   for 0≤u≤u₀, 0<d≤1/4.

Hence, when approximating the inner sums in the difference A_d−A_0 of 155 by their respective integrals and constants, the error of the prefix r≤Y is positive and of order d Y³/x² for large Y and Y≤x√(u₀/π), uniformly even if d depends on x. The tolerance O(d√x) of 155 is reached exactly in order of magnitude at Y=x^(5/6). Making d small does not buy range at that tolerance.

**Uniform proof.** Let h=d/2. By Poisson G is smooth up to zero, with G'(0)=0 and derivatives of positive order vanishing there. For large t, G'(t)=O(t^(−3/2)). The mixture formula of 157 gives

    (J'_d(u)−G'(u))/h =
       [(1/Γ(1+h)−1)/h] G'(u)
       + [1/Γ(1+h)] · {∫₀¹ [G'(u+t)−G'(u)] t^(h−1)dt
                          + ∫₁^∞ G'(u+t)t^(h−1)dt}.

The right-hand side extends continuously to the rectangle 0≤u≤1, 0≤h≤1/8: G'' is bounded on [0,2], so the difference in the first integral is O(t), and in the second there is a uniform integrable majorant. The quotient with gamma has a removable singularity at h=0. For u=0 the result is ∫₀^∞ G'(t)t^(h−1)dt/Γ(1+h), strictly positive for each h by 157. Compactness in h gives a positive minimum. By joint continuity the values stay away from zero for 0≤u≤u₀ and are bounded above. Integrating in u from zero proves the bound, since E_d(0)=E_0(0)=0. The prefix estimate follows from Σ_{r≤Y}r²b(r)≍Y³ in 157.

**Scale of the elementary weight alone.** For Y=k x/√log x with fixed k>0, the error without tilt satisfies

    Σ_{r≤Y} b(r) E_0(π(r/x)²) = x^(1−π/k²+o(1)).

By the dual series, for r≤Y one has E_0(π(r/x)²)=(x/r)Σ_{n≥1}exp(−πn²(x/r)²). Its value at Y is x^(−π/k²+o(1)), and it is increasing in r. This and the mass O(Y) give the upper bound. For the lower bound use [(1−η)Y,Y] of mass ≍_η Y and evaluate the first term at (1−η)Y. Taking first x→∞ and then η→0 proves the exponent. Thus the weight without tilt allows prefixes of order x/√log x (with k<√(2π)) at cost O(√x), but the normalized difference (E_d−E_0)/d keeps a quadratic term in r/x. This difference explains why transferring the precision of the elementary weight directly to the tilt loses range.

**Decision.** 157 treated fixed d and the error without subtraction; its constants did not resolve this joint question in d and x. The result rules out a possible cancellation inside the prefix of the centred difference. The contribution of the remaining indices and its interaction with the global centring remain open. The critical scale here is that of the uniform estimate of 155; its converse for fixed d does not presuppose additional uniformity.
