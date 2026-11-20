# Cost of the high-multiplicity layers at the exact cut

**Status: PROVED, independently reviewed, including the packing and the roundings.**

Let A_K(x) be the positive Gaussian mass of 368 over squarefree integers without primes ≤L² that have at least K prime factors, L=log x, h=log L. For fixed 0<c<1/2 and K=ceil(cL/h),

    limsup log(1+A_K(x))/L = 1−c.

For any K=(1/2+o(1))L/h one has A_K(x)≤x^(1/2+o(1)). Hence these last layers can be removed from S without affecting the one-sided exponent criterion of 372.

**Uniform ceiling.** For s=1+1/L one has g(u)≤C exp(su), by completing the square with C absolute for L≥1. If H=Σ_p p^(−s)≤log ζ(s)≤log(1+L), the product over k distinct primes has Dirichlet mass ≤H^k/k! by ordering. Hence A_K≤Cx^s Σ_{k≥K} H^k/k!≤2Cx^s(eH/K)^K when K≥2eH. Taking logarithms, the factorial term saves (c+o(1))L for K=(c+o(1))L/h.

**Floor even for either of the two parities.** Choose integers k→∞ of the desired parity, P=k^(1/c), and form products of k distinct primes from [P,2P]. By the PNT there are N≫P/log P candidates. The logarithms of the products lie in an interval of length k log 2; some cell of length ≤1 contains ≥binom(N,k)/O(k) different products. Let L be the midpoint of that cell and x=exp L. We have L=(k/c)log k+O(k), whence log L=log k+log log k+O_c(1). More precisely,

    k−cL/log L = (1+o(1)) k log log k/log k →∞,
    P/L² ≍_c k^(1/c−2)/(log k)² →∞.

Thus k≥ceil(cL/log L) and all chosen primes eventually exceed L². There is no need to round P or x to integers. Each product receives a weight bounded below by a positive constant, since |log(x/n)|≤1/2. Since binom(N,k)≥(N/k)^k, the logarithm of the contribution is ≥(1/c−1)k log k−O_c(k log log k)=(1−c−o(1))L. This proves the limsup. The scales for the two parities may differ; no floor for their difference is deduced.

**Use.** Taking for example K=floor(L/(2h)−L/h^(3/2)), the signed contribution of k≥K costs at most x^(1/2+o(1)) in absolute value. Hence, for each σ>1/2 and each sign, the one-sided ceiling O(x^σ) is equivalent before and after removing it; it is not claimed that a pointwise sign is preserved. Lowering the threshold to cL/h with fixed c less than 1/2 and trying to pay all those layers in absolute value already costs x^(1−c−o(1)) along a subsequence. The estimate leaves the cancellation in k<K uncontrolled.

**Cross-check.** 369 treats large cuts via a signed comparison of layers; here the exact cut is used and the limit of paying in absolute value is quantified. The closest internal antecedents for the floor are 293, "Floor for each sign", and 356, "Optimality of the exponent": both select products of distinct primes and use binom(N,k)≥(N/k)^k. It is the same basic combinatorial mechanism, applied here to primes above the cut and followed by packing into a logarithmic cell to keep the Gaussian weight. The search in the research notes and the index found no exact antecedent of the limsup statement for this tail; no historical novelty is claimed. The independent review confirmed injectivity by unique factorization, the O(k) factor of cells, and that the margin in the rounding of the threshold tends to infinity.
