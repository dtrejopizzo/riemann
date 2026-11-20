# How far slopes can be removed by summing their absolute values

In 060 the average over fourth-power scales transformed each slope of reduced product r into an integer sum with a mask of valuations. Write u*=2√B, the upper endpoint of the support of f, and

    G(Z)=Σ_{n≥1} f(n/Z),     T=L/√r.

G is zero for Z<1/u*, and is O_N(Z^(−N)) for large Z by Poisson, smoothness of f and integral zero. The slope equals exactly μ(r)Σ_{rad(h)|r}(−1)^Ω(h)G(T/h) for squarefree r.

**Slopes with no primes intervening in the mask.** If all primes of r exceed u*T, only h=1 contributes. Therefore these slopes for r≤x^(1−ε) sum to o(L) in absolute values for any fixed positive ε less than one: T≥x^(ε/2) and there are at most O(x log x) ordered slopes up to x. In particular all slopes of prime reduced product in that range are covered: the primes below the threshold of 060 are already controlled in absolute value, and above it p>u*L/√p for large x.

**Two primes change the behaviour.** For each fixed δ>0 and R=L(log L)^(2+δ), there are two subsets of slopes with product of two primes and r comparable to R. In one, all slope totals are positive and their sum is ≫δ L(log L)^δ. In the other they are negative and the absolute value of their sum satisfies the same bound. Here the absolute values are taken after all the internal cancellations of 060.

Indeed, G takes both signs. On Re s>1 its Mellin transform with convention Z^(−s)dZ/Z equals ζ(s)∫f(u)u^(s−1)du. The integral on the left is entire by the lower support and the rapid decay; the continuation to s=−2 gives ∫Z G(Z)dZ=0 by the trivial zero ζ(−2)=0. G is not identically zero: finite inversion at each Z recovers f(1/Z) from the G(Z/n), and f is nonzero by the value of V in the interior near its upper endpoint, where only w=1 appears in F. Thus there exist fixed intervals 0<z₁<z₂ where G is bounded away from zero with each sign.

Take primes p in a fixed interval of ratio two at scale L/√R, and for each p all primes q such that

    L²/(z₂² p³) ≤ q ≤ L²/(z₁² p³).

Then z₁≤T/p≤z₂ with r=pq, p<q, and r comparable to R. Uniformly q>u*T because q/T grows like (R/L)²; also p²>u*T and T→∞. The only h that can contribute are 1 and p. Each slope has value G(T)−G(T/p), of sign opposite to that of the chosen interval and of absolute value bounded below. By PNT in the intervals of fixed ratio there are ≫R/(log L)² distinct pairs: p and q have scales L/√R and R^(3/2)/L respectively. One could take a single slope per pair. The result proves a limit for removing all those products by the sum of absolute values of their slopes, not a sign statement about the whole band of semiprimes.

**Scope.** The critical exponent for the absolute method of 060 is 1/2 in x: it controls all products up to L exp(−δ√log L), and already fails in a range of order L(log L)^(2+δ). A gap persists between both thresholds. The primes alone do not produce this obstruction. The argument of the negative moment of a sum of dilations has an antecedent in 045. Here it is applied to the centred profile and to the even mask of 060 to construct two families of semiprimes with opposite signs.

**Quantitative extension for the inactive mask.** One can reach r≤c₀x/(log x)^8 with c₀ fixed and sufficiently small. We detail the regularity needed. In F(u)=Σ_{ij}ε(i)ε(j)V(i j u²/4), for small u the boxes of 055 satisfy IJ comparable to u⁻² and their long coordinate M is ≥c/u. Apply first j₀ logarithmic derivatives in u and then n ordinary derivatives in the long coordinate. The cost in sup norm is at most C^(j₀+n+1)(j₀! n!)² M^(−n): in logarithmic coordinates the argument is a sum and one uses (j₀+n)!≤2^(j₀+n)j₀! n!, with Leibniz and the Gevrey partitions of 055. The conversion to ordinary derivatives in the long coordinate is justified with the falling-factorial coefficients of 047. Alternating in that coordinate and optimising n comparable to √M gives, after counting the terms and the boxes,

    |(u∂_u)^j₀ F(u)| ≤ C^(j₀+1)(j₀!)² exp(−c'/√u)     (0<u≤1).

Reducing c' absorbs the polynomial factors in 1/u. Away from zero only a bounded number of summands intervene. Multiplying by log u−b₀ and converting to ordinary derivatives of order j costs in addition u^(−j); its product with exp(−c''/√u) is bounded by C^(j+1)(j!)². Therefore f extended by zero is Gevrey of order four. In Poisson the zero frequency vanishes, and optimising the order of integration by parts gives |G(T)|≤C T exp(−c T^(1/4)) for T≥1. If r≤c₀x/(log x)^8 then T≥(log x)^4/√c₀. Choosing c₀ small makes the saving absorb the O(x log x) slopes, with total o(L), provided each prime of r is larger than u*T.
