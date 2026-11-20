# Simultaneous cancellation in the classes of exact greatest common divisor

Let S_q be the signed contribution of the pairs n≠d with (n,d)=q to the energy of 325. In the same range as 329, h=exp(−am)m^b, 0<a≤log 4 and fixed b, for every fixed A>0 one has

    Σ_q |S_q| ≪_(a,b,A,η) h binom(2m,m) m^(−A).

**Proof.** It suffices to bound Σ b_q S_q uniformly for |b_q|≤1, since the sign of each class can be chosen. By inversion, b_(n,d) is the sum of c_g=(μ*b)(g) over the common divisors; |c_g|≤τ(g). For each g, the argument of 331 before summing the divisors gives an absolute off-diagonal ceiling O(h binom(2m,m)/g²) for the pairs of multiples of g. This justifies the exchange of sums and bounds the tail g>G by O(h binom(2m,m)(1+log G)/G), by Σ_{g≤t}τ(g)≤t(1+log t) and partial summation.

For g≤G use 329 with coefficients μ(n)1_{g|n}. The maximum for the partial summation in the short interval is now taken over subintervals intersected with gℤ; each intersection is a progression. Definition (1.3) of the maximal estimate includes all these progressions with the same exceptional set; the scalar input of §1.1, (1.5) and the following paragraph is used, just as in 329. Hence the bound on the central Gram integral preserves any saving m^(−D) with constant uniform in g. The absolute treatment of the edges, the central diagonal and the gamma tail of the distinct pairs also goes through uniformly since terms were removed when estimating in modulus. Separating the diagonal one obtains O_D(h binom(2m,m)m^(−D)) for the signed off-diagonal contribution of all multiples of g. [Article, definition of the maximum and scalar estimate](https://arxiv.org/html/2411.05770v1)

Take G=m^(A+2) and D=3A+6. The sum of |c_g| up to G is ≤G(1+log G); with these parameters both errors satisfy the stated bound.

**Consequence.** The class q=1 of 332 has exponential absolute mass for 0<a<log 4. Its imbalance between positive and negative contributions, as a fraction of that mass, decays faster than each fixed power of 1/m (use the floor h4^m/m and increase D). Hence both masses are asymptotically equal already among coprime pairs. The proof allows choosing independent signs for all classes before summing them. The exponential improvement demanded by 326 remains open.
