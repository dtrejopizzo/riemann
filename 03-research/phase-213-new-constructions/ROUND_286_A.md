# Proved favorable bands for μ and a multiplicative falsifier of the length jump

For fixed B,A>0 and H=√X(log X)^B, the maximum of |Σ μ(n)| over all prefixes of (x,x+H] is ≤√X/(log X)^A for almost all starting points x∈[X,2X]. Indeed, this is Theorem 1.1(i) of Matomäki, Radziwiłł, Shao, Tao and Teräväinen with the constant function one and logarithmic saving A+B; their maximal norm includes all subintervals and even all progressions. The exceptional set has measure O_(A,B)(X/(log X)^(A+B)). It is an external result applied to the threshold of 285. [Theorem 1.1(i) and definition (1.4)](https://doi.org/10.1007/s00222-026-01408-6).

**The obstacle to assembly.** There is a single multiplicative function f with |f(n)|=μ²(n), which can coincide with μ up to any prescribed initial threshold, with both properties:

* At H=√X(log X)^B, the above maximum, even over progressions, is ≤√X/(log X)^A except on a set of measure O_(A,B)(X/log^A X), for all fixed A,B.
* In EACH large band [X,Xexp(h)] of 285, the maximal excursion from X is ≥X^(3/4−o(1)).

Hence favorable short windows, their frequency and multiplicativity with exactly squarefree support do not suffice as the only inputs to build the long subsequence. Unlike 137, the maximal bounds on almost all intervals are preserved and the failure is imposed in every long band, for the partial sum itself.

**Choice of the primes.** Put β=3/4. From the initial threshold on, run through the primes accumulating p^(β−1); include a prime in S when the integer part of the accumulated sum increases. One has #S(≤z)−Σ_(p≤z)p^(β−1)=O(1), with a constant that allows for the threshold. Flip the sign of μ at the primes of S, extend multiplicatively to the squarefree integers and put zero on the others. Then f=μ*b, where b is nonnegative with Euler factors (1+p^(−s))/(1−p^(−s)) on S and one outside. Σ b(d)/d^η converges for η>β by the count #S(≤z)≪z^β.

**Transfer in short intervals.** Cut the convolution at d≤Z=log^K X. For each d in that range apply the cited theorem at scale X/d, length H/d (between (X/d)^(1/3+ε) and (X/d)^(1−ε) with fixed small ε), with arbitrarily large saving R. The preimage of a progression on imposing d|n is a progression or empty. The union of exceptions has measure O(ZX/log^R X) and the good contribution costs O(H log^(−R)X Σ b(d)/d). For d>Z the integral over starting points of the sum of moduli is O(HX Σ_(d>Z)b(d)/d), by counting multiples up to 3X. The tail is O_η(Z^(η−1)) for β<η<1. First choose K and then R sufficiently large and apply Markov. An additional logarithmic power can be spent to absorb the constants. This gives the first property.

**Pole forcing failure in the long bands.** In Re s>1 the series of f factors as

    ζ(s+1−β)² H₀(s)/ζ(s).

H₀ is holomorphic and nonvanishing in Re s>1/2. To see this take the logarithm of the product for b and subtract 2log ζ(s+1−β). The first-degree terms give 2Σ_p(1_S(p)−p^(β−1))p^(−s), holomorphic for Re s>0 by the bounded accumulated discrepancy. The remaining degrees converge absolutely for Re s>1/2, both in the factors of S and in the shifted zeta. In particular the continued series has a real DOUBLE pole at β, since ζ(β) is finite and nonzero.

The growth allows the use of the contour of 285, also for the narrowing bands. For 1/2<σ₁<σ₂<β, in σ₁≤Re s≤2 the sum of first degrees up to R=(2+|Im s|)^(1/β) costs O(R^(β−σ₁)) by absolute summation and counting; its tail costs O((1+|s|)R^(−σ₁)) by partial summation. Thus |H₀(s)|≤exp(C(2+|Im s|)^κ) with κ=1−σ₁/β<1/2. The shifted zeta grows at most polynomially in the strip at large height. Build the filter of 285 taking the real pole β as target and annihilating with multiplicity the zeros of ζ with real part ≥σ₁. Multiplying its transform by s−β leaves a fixed nonzero residue. The additional bound exp(C|τ|^κ) is absorbed in half of the Gevrey decay exp(−c√(h|τ|)), at cost exp(O(h^(−κ/(1−2κ)))); this is exp(o(log X)) in the range of 285. The same shift gives a weighted sum equal to c₀ X^β+O(X^σ₂ exp(o(log X))), c₀≠0. By partial summation the second property follows. This falsifier preserves the size law and multiplicativity; it changes the exact identity μ*1=δ.
