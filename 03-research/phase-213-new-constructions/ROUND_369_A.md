# Unconditional odd dominance in a growing range of layers

Let S^*(x;z) be the parity pulse of 368, L=log x and u=L/log z. For sufficiently large x there is an **unconditional negative sign**, uniformly in

    2 ≤ u ≤ L^(1/4),   that is,   exp(L^(3/4)) ≤ z ≤ √x.

It is the same fixed Gaussian weight and the same Möbius coefficient. The final cut z=L² corresponds to u=L/(2 log L), outside the range. The sign rule of the continuous model is exactly the derivative of the classical Dickman function; the point here is to control the arithmetic error of the pulse as the number of layers grows.

**Continuous computation.** Write f(t)=1_{t≥1}/t. On replacing each prime by the measure dq/log q and putting t=log q/log z, this becomes z^t f(t)dt. The product of k factors gives the density z^t f^{*k}(t)/k!, with sign (−1)^k, in the product variable. For finite t the series D(t) of signed densities is finite because f has support in [1,∞). If ρ(t)=1+∫₀^t D(v)dv, the symmetry of the k copies gives t f^{*k}=k(tf)*f^{*(k−1)}, with f^{*0} the unit mass at zero. Hence ρ=1 on [0,1] and

    t D(t)=−ρ(t−1)   for t>1.

The identity tρ(t)=∫_{t−1}^t ρ(v)dv for t≥1 follows by differentiation and continuity at 1. It prevents a first zero, hence ρ>0 and decreases. Also ρ(t)≥ρ(t−1/2)/(2t), integrating only the first half. Iterating shows ρ(t)≥exp(−C(t+1)log(t+2)). Thus the continuous sum of layers has negative sign for all t>1, even where an individual layer does not determine the sign.

**Transfer from the primes.** Let g(w)=exp(w/2)φ₁(w). Truncating the real pulse at n≤x² costs O(x exp(−cL²)) by the Gaussian decay, grouping by unit logarithmic intervals. The term n=1 is also of that order. The remaining integers have k≤K=⌊2u⌋ factors >z. Write the sum over ordered primes and divide by k!, removing for now the requirement of distinct primes. The error on n≤x² is O(xL/z): each repeated integer has combinatorial weight ≤1 and some p²|n with p>z, while g(log(x/n))≤C x/n. Sum harmonically first the multiples of p². Completing the sums of each prime up to B≥x² with log B=2L+O(1), even when the product exceeds x², costs at most the previous Gaussian tail, since the weight 1/k! of the orderings of each integer sums to ≤1.

Choose log B as the first endpoint ≥2L of a mesh in log q of step Δ=exp(−L^(1/3)) started at log z. The classical prime theorem with error O(q exp(−c√log q)) gives, in each cell, the number of primes equal to the integral dq/log q with relative error O(exp(−c' L^(1/3))). Indeed log q≥L^(3/4), and dividing by the mass of the cell only loses O((log q)/Δ). In a box of k cells the logarithm of the weight g varies by O((1+KL)KΔ), by its logarithmic derivative. By positivity, replacing the measures in each layer then has relative error O(exp(−c'' L^(1/3))) for their unsigned masses. The error is not multiplied by the number of boxes: relative bounds are summed against the masses. The total unsigned arithmetic mass is O(x), by comparison with all integers and Gaussian summation; hence the total signed error is O(x exp(−c'' L^(1/3))).

In the resulting integral, for t≤2u the individual cuts q≤B and k≤K do not affect the density D(t). For t>2u the cost is O(x exp(−c L²)u), since z^t g(L−t log z) has that ceiling without the factor u and the mass of the truncated convolutions without the factor z^t is ≤exp(∫₁^{log B/log z}dv/v)=O(u). On [1,2u] the signed density is negative. It suffices to integrate over u≤t≤u+1/log z: there z^t≥x, g is bounded below, and the formula for D gives a contribution in modulus at least

    (x/log z) exp(−C(u+1) log(u+2)).

For u≤L^(1/4) this floor dominates all the previous errors. Thus the sign is obtained for the genuine integers without any hypothesis on RH.

**Quantitative limit.** At the target cut u=L/(2 log L), the continuous imbalance can be far smaller than the relative precision of the substitution by dq/log q. The positivity of ρ alone does not justify the discrete sign there. One needs to control the signed difference between layers or to find a discrete recurrence preserving the inequality.
