# The class of primitive quotients already carries the whole absolute rate

At the scale h=exp(−am), 0<a<log 4, let P*_m be the sum of 326 with absolute values restricted to (n,d)=1. Then

    lim (P*_m)^(1/(2m)) = 2 exp(−a/2).

**Count in the band.** For integer X, integer H between 1 and X, count X≤n<2X and d=n+k, 1≤k≤H. As H and X grow, the proportion of pairs for which nd is squarefree tends to

    c = ∏_p (1−1/p)²(1+2/p)>0.

Indeed, for the primes up to a fixed P, take the modulus M product of their squares. The rectangle of (n,k) equidistributes in classes modulo M in both coordinates, and (n,k)↦(n,n+k) is bijective modulo M. At each prime one allows two units or exactly one coordinate divisible by p only once and the other a unit. This gives the written local factor; the product converges to a positive value since its factor is 1−3/p²+2/p³. For p>P the pairs with p²|n or p²|d cost O(H(X/P+√X)), counting first the multiple of the square up to 3X and then up to H neighbours. The pairs with p|n,d only contribute if p|k, hence cost at most Σ_(P<p≤H)(2X/p)(H/p) ≪ XH/P. Divide by XH and let first X,H and then P grow. This elementary count does not require uniformity of the distribution of μ in particular short intervals.

**Transfer.** Take X=⌈exp(2m)⌉, H=⌊c₀hX⌋ with 0<c₀<1 so small that K≥1/2 on [−c₀,c₀]. One has H→∞. In all counted pairs, |μ(n)μ(d)|=1, (n,d)=1, d≤3X and 0<log(d/n)≤c₀h. The restricted sum is therefore ≫ h X² (2m)^(2m)/((m!)²(3X)^3) ≫ h4^m/m by Stirling. The ceiling comes from 326. In particular, even an argument that managed to eliminate exactly all classes with gcd greater than one would still face the full absolute rate in the remaining class. The computation leaves open the aggregate sign within that class and does not prevent cancellation between classes in the total energy.

**Antecedents in the phase.** 326 uses occupation in cells without imposing coprimality; 331 gives a ceiling for the tail of common divisors. Here the floor persists after fixing the gcd exactly equal to one. The elementary density is only used to obtain this conclusion about the energy.
