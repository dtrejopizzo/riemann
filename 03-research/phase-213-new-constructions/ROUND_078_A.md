# Jensen at the reciprocal frequency: exact floor for the cell complement

Let m be the archimedean symbol of paper 46. For a unit test with primitive G in L²(ℝ),

    ∫ m(ξ)|F̂(ξ)|² dξ/(2π) ≥ m(1/||G||₂).

In particular, for the orthogonal complement of piecewise constants on cells of length h, the floor is m(π/h), with no additive comparison constant. "Floor" denotes a lower bound; it is not claimed to be the attained infimum.

**Proof.** By the exponential expansion of K in P46, with c_j=1/2+2j, m(ξ)=C₀+Σ_{j≥0}(2/c_j)ξ²/(c_j²+ξ²). In the variable Z=1/ξ², each summand is proportional to (1+c_j² Z)^(−1), convex and decreasing. Under the probability |F̂|²dξ/(2π), E Z=||G||² by Plancherel. Apply Jensen term by term and sum by monotonicity. On each mean-zero cell the primitive from the left endpoint vanishes at both endpoints; the concatenated primitives extend by zero and ||G||≤(h/π)||F|| by Wirtinger. This gives the floor. The Jensen in ξ² of P46 gives the other direction and requires a positive moment; it does not contradict this inequality with an inverse moment.

**Archimedean counting.** For the compressed operator of the symbol m on an interval of length L, let λ_k be its increasing eigenvalues with multiplicity, k≥1. Then

    m((k−1)π/L) ≤ λ_k ≤ m(kπ/L).

For the lower side with k≥2, take the complement of the first k−1 Neumann modes (including the constant). The primitive of the mode cos(nπt/L) is L sin(nπt/L)/(nπ) in coordinates [0,L]. Orthogonality gives ||G||≤L/((k−1)π) for ||F||=1, and the min–max principle applies. For k=1 m≥m(0) suffices. For the upper bound use the first k Dirichlet sines and the Jensen of P46 in ξ², with ||F'||≤kπ/L. Thus, if ξ₀ is the positive root of m, the number of strictly negative eigenvalues lies between the number of integers k≥1 with kπ/L<ξ₀ and that of integers k≥1 with (k−1)π/L<ξ₀. The bounds differ by one. The argument is an elementary proof of a Dirichlet–Neumann type bracketing for a subordinate symbol; no general novelty is attributed to that principle.

**Error of the minimum for the full form.** Over a compact set J of windows let λ_h be the minimum of W on constants over cells of length h=2T/N. Uniformly under refinement, for each 0<s<1/2,
    
    0≤λ_h−λ_W(T)≪_{J,s} h^(2s)(1+|log h|).

For a unit minimizer F from 077 and its orthogonal projection by means Π_h, ||F−Π_hF||₂≪h^s||F||_{H^s} by the variance formula on each cell and the difference seminorm. Also ||Π_hF||_{H^s}≪_s||F||_{H^s}. To see this use the mesh on the whole line (aligned with the interval); on distinct cells, by Jensen the square of the difference of means is bounded by the mean of squared differences. The integral of the kernel |v−w|^(−1−2s) between non-adjacent cells is comparable to the area times its minimum value; for adjacent ones the same bound with an s-dependent constant holds by direct integration, finite because 2s<1. Inside a cell the projection is constant. This proves stability also at the boundary of the support.

For e=F−Π_hF, m(ξ)≤C+log(2+|ξ|) and log(2+|ξ|)≤C_s+|log h|+C_s(h|ξ|)^(2s) for h≤1. After integrating and adding the bounded terms of W, W(e)−λ_W||e||²≪h^(2s)(1+|log h|). The weak eigen-equation cancels the linear term exactly: the excess of the quotient of Π_hF is [W(e)−λ_W||e||²]/||Π_hF||², with denominator uniformly close to one. The other sign of the error is variational.

**Use and limits.** The complement of the means has for W the floor m(π/h)−Σ_{n<exp(2T)}v_n−4sinh T. If it is positive, the cross block still enters the Schur complement; positivity of the cell matrix alone does not suffice. P46 lemmas coer-lowpass/coer-B already give logarithmic coercivity using two Tate moments per cell. Here the ordinary mean suffices and the value of the symbol at π/h is obtained directly. The counting up to one unit is for the archimedean operator alone. No numerical error constant for W, no new window, and no uniform sign in T was obtained.
