# Three dilations cancel the range of arguments up to a fixed power

Let D=x^o(1), D≥2, q=⌊D⌋+1 and w_D the sieve of 310. Freeze D,q when evaluating at different scales and form the signed weights

    g(n)=w_D(n)−2q w_D(n/q)+q²w_D(n/q²),

interpreting non-integer arguments as weight zero. With κ=77/285, for all sufficiently large x and uniformly in 0≤t≤2,

    B_t(x) + Σ_(D<n≤x^(1−κ)) g(n) B_t(x/n) = O_ε(x^(1/2+ε)).

The main sample enters with coefficient one. The retained sum evaluates B_t only at arguments between x^κ and x/D. Eliminating all arguments smaller than x^κ costs in total O_ε(x^(1/2+ε)), without locating crossings or choosing the endpoint depending on t. The result corresponds to a signed combination of the averages of 310; it does not preserve the positivity of their weights.

**Ceiling of the full average.** The polynomial modifying the sieve is (1−q^(1−s))². The weighted partial sum over all dilations is S_D(x,t)−2q S_D(x/q,t)+q² S_D(x/q²,t). By 310, on any fixed line σ>1/2 the modification multiplies the ceiling by (1+q^(1−σ))²=x^o(1). This gives the square-root ceiling with arbitrary loss. Since q>D, g(1)=1 and g(n)=0 on 2≤n≤D.

**What the difference cancels.** The series of g is ζ(s)²k(s) with k=h_D(s)(1−q^(1−s))². Its finite polynomial is supported up to D⁴q²=x^o(1), has absolute norm x^o(1) at each fixed nonnegative abscissa (by 310 or its expansion by pairs) and satisfies k(1)=k'(1)=0 exactly. Put G(v)=Σ_(n≤v)g(n) and β=131/416. For v≥D⁴q², convolving the divisor asymptotic with k completely cancels v log v and v: the coefficients are k(1) and (2γ−1)k(1)+k'(1). Hence |G(v)|≪_η x^o(1) v^(β+η) for all η>0. The only additional external input is the published bound for the error in the partial sum of τ; logarithmic factors are absorbed into η. [Huxley, Exponential sums and lattice points III](https://doi.org/10.1112/S0024611503014485)

**Transfer to the signed tail.** For V=x^κ, interchanging the sums gives exactly

    Σ_(x/V<n≤x) g(n)B_t(x/n)
        = Σ_(m≤V)b_t(m)[G(x/m)−G(x/V)].

All arguments of G exceed its support threshold for large x. The coefficients satisfy |b_t(m)|≪_η m^η uniformly, by the bounded local factors and the cube-free support. Estimating both terms gives O_η(x^(β+O(η)+o(1)) V^(1−β)). Since β+κ(1−β)=1/2, the tail fits in the budget for every ε>0. The same proof with any exponent β<1/2 for the divisor problem allows κ=(1/2−β)/(1−β). The estimate for g is made after compensating among the three dilations: bounding the three masses in modulus separately would lose the two zeros at 1.

**What is pending.** By 292, controlling the integral over t∈[1,2] of the negative part of the intermediate sum in the statement at scale x^(1/2+ε) is equivalent to the global sign, since its opposite differs from B_t(x) by a uniform error of that order. The trimming of 311 was positive with an adapted endpoint, and the dyadic filter of 300 acted on the first row. Here q>D preserves the initial gap while eliminating the power range for all frequencies. The intermediate interval remains to be paid for.
