# Which complete rows can be paid for according to their cofactor of large primes

Use exactly the rows U_m of 069. Fix B>1 and 0≤θ<1, and put y=(log x)^B. For squarefree m write t_y(m) for the product of the primes of m larger than y (empty product 1). Let A(x) be the sum of |U_m(x)| over all m with t_y(m)≤x^θ. Then

    limsup_{x=j⁴→∞} log(1+A(x))/log x = 1−(1−θ)/B.

The upper bound also holds for continuous x. If B<2 and θ<1−B/2, the complete sector costs o(√x); after removing it only numerators whose cofactor of large primes exceeds x^θ remain. For θ>1−B/2 control by absolute values at root scale fails. The critical exponent by itself does not decide the equality case.

**Upper bound.** Write m=s t with the primes of s at most y. In the bound of 069 at abscissa σ=1−1/B∈(0,1), the sum over t≤x^θ of its weight is O_σ(x^(θ(1−σ))) by the mean estimate there. The sum over all squarefree s costs ∏_{p≤y}(1+p^(−σ)w_p), with w_p=(1−p^(−σ))^(−2). Its logarithm is O_σ(1+y^(1−σ)/log y) by Chebyshev and partial summation. Since y^(1−σ)=log x, this factor is x^o(1). Multiplying by x^σ yields the stated exponent.

**A family where the true size of the rows is visible.** Let k₀(v)=U_1(v) be the physical kernel of K from 069. It is continuous, not identically zero by its transform, and vanishes on (0,v₀) for some v₀>0 by the lower support of the representative and its averages. Choose 0<A<C with |k₀|≥c₀>0 and of constant sign on [A,C]. If x/m belongs to that interval and all primes of m exceed C/v₀, one has exactly
    
    U_m(x)=μ(m) k₀(x/m).

Indeed, expand the power series of the local factors (1−u+u²)^(−1) of 069 on Re s>1. All terms except the constant one evaluate k₀ at x/(mn)<v₀, because n contains some prime of m. This avoids inferring a lower bound from the Euler majorant.

**Counting at scale comparable to x.** Take X large and Y=(log X)^B. For θ>0 fix 0<τ<θ; for θ=0 take τ=0. Form m by multiplying k distinct primes in [Y/3,Y/2] and, when τ>0, another prime in [X^τ,2X^τ]. Take k=(1−τ)log X/(B log log X)+O(1), an integer. All products are distinct by unique factorisation. Uniformly log m=(1+o(1))log X. There are N≫Y/log Y primes available in the first interval by PNT and N/k→∞. Using binom(N,k)≥(N/k)^k and counting the primes of the second interval, the number of m is at least
    
    X^(τ+(1−τ)(1−1/B)+o(1)).

In an interval for m of fixed ratio ρ>1, with ρ<C/A, there is that same exponent of products: split their range into O(log X) intervals of ratio ρ. For the chosen interval [M,ρM], choose x in an interior subinterval of [AρM,CM] of length comparable to M. It contains a fourth power for large X. Thus x/m∈[A,C], log x∼log X, the small primes chosen are less than (log x)^B and the additional prime, if it exists, is less than x^θ. The identity of the previous row applies. Summing absolute values, and letting τ↑θ for θ>0, proves the equality of exponents. Adjusting k by one unit allows obtaining exclusively rows of either sign in the construction, along eventually different sequences of x.

**Scope.** Counting many choices of primes has antecedents in 043. The bound for their complete rows and the identity that makes the counterexample effective specifically use the representative of 069. The result admits numerators of size comparable to x and all denominators. The lower obstruction concerns absolute values and selected subfamilies of fixed sign; it does not establish the sign of the sum of the rows of the whole region nor of the complement.
