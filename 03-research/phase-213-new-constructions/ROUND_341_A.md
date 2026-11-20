# Pointwise bound for all reduced quotients of small height in 338

In 338 use the version with de>X^(1−δ−ε), ε=δ/4, and fix 0<δ≤1/10. Let R=X^(δ/4). For x∈[X,2X], the joint contribution of all pairs whose reduced quotient r/s=d/e satisfies max(r,s)≤R has modulus

    ≪ h√X R + X^(1/4+7δ/4+o(1)) = o(√(Xh)).

In particular, the diagonal and a growing set of rational directions can be removed with mean-square error o(Xh), with no hypothesis on the zeros. The range δ=1/j with j≥10 suffices in the equivalence of 337.

**Proof.** Combine the two pulses as Σ_k (−1)^(k+1)W_x(kde) since the second copy removes the even multiples twice. It suffices that k≤K=⌈2X^(δ+ε)⌉. Write d=gr, e=gs, (r,s)=1. The cuts of 338 and that of the product amount to g in an interval J inside (0,D], independent of k. The coefficient in g is μ(r)μ(s)μ²(g)1_{(g,rs)=1}. For Q=rs the sum of μ²(g)1_{(g,Q)=1} up to z is c_Q z+O(τ(Q)√z) with 0≤c_Q≤1. Indeed one expands μ² with the square divisors: for (l,Q)=1 the coprime count up to z/l² is (φ(Q)/Q)z/l²+O(τ(Q)); the tail when completing the main series costs O(√z).

For each k the total variation in g of the pulse cut by J is O_η(1), by monotonicity of the logarithmic argument. Replacing the sum over g by c_Q times the integral costs O_η(τ(Q)√D). Summing the errors in modulus over the k and the pairs r,s gives O(K R² X^(1/4+o(1))) by the elementary divisor bound.

In the integral change g=√(x/(krs))exp(−hv/2). For each v in the support of η, the condition g∈J delimits an interval in k, even after the cut k≤K. The alternating sum of k^(−1/2) over any interval costs at most one. The Jacobian then gives a ceiling O_η(h√(X/(rs))) for the main term of each quotient. Summing (rs)^(−1/2) up to R in both indices gives O(R). For the first cost the exponent is 1/2−3δ/4; for the second it is 1/4+7δ/4+o(1). Both are strictly below 1/2−δ/2 in the stated range.

**What it contributes to the criterion.** The estimate exploits simultaneously the even and odd multiples of the same product. The true signs in each quotient reduce to a count of squarefree integers and the density term cancels in k. 331 identifies the constancy of sign at fixed quotient for another pair energy; here a bound of the required size is proved for the observable of 338. The quotients of height greater than R remain, including the case of two large coprime factors.
