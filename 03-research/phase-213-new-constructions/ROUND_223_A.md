# The stability constant of 222 is exact for perturbations on the primes

For each A>0 there exist positive relative weights λ_p→1, on the same primes, such that D(x)=Σ_(p≤x)(λ_p−1)log p satisfies the hypothesis of 222 with that A and

    limsup log(1+|C_k(λ)−C_k(1)|)/k = 4A^(3/2)/(9√3).

The mass in each modified block can be preserved exactly. The conclusion is for the difference of the samples. It does not claim an extreme behaviour of the authentic sample C_k(1).

**The scale that was missing in 221.** Fix z>0, N=k², L₀=z k^(3/2), X=exp(L₀), m(a)=log M_a(3) and choose a by Nm'(a)=L₀. It exists for large k and a=(9/2)z/√k+O(k^(−3/2)) by m(a)=a²/9+O(a⁴). Thus

    Nm(a)−aL₀=−9z² k/4+O(1).

The profile of 221 for fixed a does not suffice here. For L=L₀+d with d in a compact, s=−√k+ik and I_k from 218 one obtains uniformly

    L√N I_k(L)/(3^s exp(Nm(a)−aL))
       = Re[K_a exp(iNθ_a+ix_a d)/(a−ix_a)] + o(1).

The constants x_a,K_a,θ_a are those of 212 at rate 3; x_a→3 and K_a converges to a nonzero constant.

**Integrate first in the rate.** On the contour at rate 3 write u=3t. The Fourier integral of I_k is 3^s/(2π) times the integral in τ of H₃(τ+ia)^N multiplied by

    ∫₁^T t^s exp((iτ−a)Lt)dt.

The endpoint T comes from the original cut and u≤N. Uniformly in compact d, T≥2 eventually because log X_N(6) has order N. Near the two maxima ±x_a, |a−iτ| is bounded away from zero. Integrating twice by parts one obtains the term exp((iτ−a)L)/[(a−iτ)L] with error in modulus ≤C exp(−aL)/L times

    O(k/L + k²/(aL²) + (1+k/L)exp(−aL)) = o(1)

as an additional factor. For the remainder use |s(s−1)t^(s−2)|≤Ck² and ∫₁^∞ exp(−aLt)dt=exp(−aL)/(aL). The choice of two integrations avoids a loss as the contour height approaches zero. Outside fixed neighbourhoods of ±3 use directly |inner integral|≤exp(−aL)/(aL). The integral there of |H₃(τ+ia)|^N is exponentially smaller than exp(Nm(a)) by uniform separation, including the rational tail. The integrated errors at the two peaks use ∫|H₃|^N≤C exp(Nm(a))/√N.

**Uniformity of the Gaussian approximation.** For small 0≤a≤a₁, the maxima remain in two disjoint neighbourhoods, with negative real curvatures bounded away from zero, by continuity from a=0. The local logarithm has bounded third derivatives in those neighbourhoods. At τ=x_a+w/√N the linear term cancels exactly with iL₀(τ−x_a) by the choice of a. After extracting the central phase the integrand is dominated by C exp(−c w²); on compacts it differs by o(1) from the quadratic profile with coefficient h''(x_a+ia) and amplitude 1/(a−ix_a). This also holds uniformly for compact d. The other peak is conjugate in the main term; the complex prefactor 3^s was extracted earlier. The relative profile above is proved, with control at the appropriate exponential scale.

**Weights on the primes.** On a fixed compact of d containing several periods, the main real profile has an interval where it exceeds c and another where it is less than −c, both of the same fixed length, for all large k. This follows from the nonzero modulus of K_a/(a−ix_a) and x_a→3. Apply additional relative weights +b and −b' on the two intervals, with

    b=X^(−1/2)exp(A L₀^(2/3)).

Choose b' making the total change of logarithmic mass exactly zero. PNT gives b'/b between two positive constants, uniformly for these moving intervals inside the compact. The accumulated change inside the block is bounded by C√X exp(A L₀^(2/3)); it vanishes on leaving. The new weights are positive for large k. On projecting the change of C_k onto the direction 3^(ik), the two contributions add with the same sign. The logarithmic mass on each interval is comparable to X and there p^(−1/2) is comparable to X^(−1/2). By the proved profile, the magnitude of the change is at least

    exp([A z^(2/3)−9 z²/4] k − o(k)).

To build a single fixed system of weights, choose the blocks successively above the maximal cut of all previous orders. The previous perturbation is finite at each step and its effect tends to zero with k by the envelope of 211 and the weight of 217. Future blocks do not affect the current sample. The bound on D(x) holds globally by zero mass and by log x=L₀+O(1) within each block. Choosing z=(4A/27)^(3/4) maximises the positive exponent and attains the upper bound of 222. For A=0 stability was already proved there.

**Decision.** The barrier of 222 is exact even imposing positivity, support on the real primes and blockwise mass preservation. Lowering the constant or replacing o((log x)^(2/3)) by O((log x)^(2/3)) in a general subexponential transfer theorem requires additional hypotheses.
