# Optimal loss of the positive binomial carries in an octave

For a,b>0 set c(y)=⌊(a+b)/y⌋−⌊a/y⌋−⌊b/y⌋. It is the carry received by a prime power y in a binomial coefficient of integer arguments. On any octave I=[x,2x],

    ∫_I c(y)dy ≤ [1/(2 log 2)] ∫₀^∞ c(y)dy.

The constant 0.7213475… is optimal. It holds for each individual kernel, hence also for positive mixtures in which the split, the scale and the coefficients are chosen jointly as functions of x. It admits multinomial carries, by telescoping decomposition of a multinomial into binomials.

**Total mass.** Rescale a+b=1, write λ=min(a,b)/(a+b)≤1/2 and I=[u,2u] in these units. The kernel is zero or one and vanishes for y>1. Its integral is the entropy E(λ)=−λ log λ−(1−λ)log(1−λ): integrate each floor from ε using ∫_ε^∞⌊t/y⌋dy=t Σ_(k≤t/ε)1/k−ε⌊t/ε⌋ and pass to the limit in the difference. Moreover λ/E(λ) is increasing, since E−λE'=−log(1−λ)>0, and E is increasing on (0,1/2].

**Mass inside the octave.** When u≤λ the length u suffices. For u>λ the carry is the sum of the indicators of ((1−λ)/k,1/k], k≥1, up to irrelevant endpoints. If moreover u>1/3 only k=1,2 can intervene. The joint contribution has length at most λ: doubling the captured part of band k=2 moves it to band k=1 outside the interior of [u,2u]. If u≤1/3 the length bound 1/3 is always available. Therefore the mass is ≤max(λ,1/3).

For λ≥1/3 this gives mass/E≤λ/E≤1/(2 log 2). For 1/4≤λ≤1/3 one uses (1/3)/E(1/4)<1/(2 log 2). It remains to treat λ≤1/4. If u>λ, only (1−λ)/(2u)<k≤1/u intervene, and the ratio of the endpoints of the index interval is ≤8/3. If m is the smallest index, all are <3m and their lengths add up to at most λΣ_(k=m)^(3m−1)1/k≤3λ/2. This harmonic sum decreases in m, because on passing from m to m+1 one loses 1/m and gains three terms whose sum is smaller. The bound 3λ/2 also holds if u≤λ. Since (3/2)(1/4)/E(1/4)<1/(2 log 2), the universal ceiling is proved. At λ=u=1/2 exactly the length 1/2 is captured and the total mass is log 2.

**Cost for the budget of 257.** For any positive mixture B of these carries, integrating outside I costs at least κ times what is integrated inside, κ=2 log 2−1. If g_x(y)=g(y/x) is the positive weight of 257, with h=∫g, any pointwise majorant B≥g_x on I costs at least (1+κ)xh in total mass. Even without majorisation, ||B−g_x||₁≥κxh: if A is its interior mass, the cost is ≥|A−xh|+κA. The constant is optimal for the class of positive targets on an octave, by the indicator of the octave in the symmetric case. For a signed representation B_+−B_−=g_x with finite masses, the negative part must pay at least κxh: the leakage of B_+ cancels outside and its interior mass is already ≥xh.

Therefore obtaining the budget xh+O(√x) via pointwise positive majorisation and use of the total factorial cost is impossible even with adaptive splits. A strategy that arithmetically controls and subtracts the exterior contributions remains available; the barrier quantifies what that subtraction must recover. The statement refers to integrals in the continuous prime-power variable. It does not impose that cost on an inequality justified only at the primes with other arithmetic information.

**Antecedent.** Selection 099 ruled out representing log t exactly with positive dilations of a fixed distribution of splits and left adaptive majorisation open. Here the local cost question is resolved for any positive target supported on an octave by a geometric argument without zeros of ζ. The original inequality of 257 remains open.
