# A positive sieve isolates the main scale up to any subpolynomial threshold

For B_t of 309, x≥2 and 2≤D≤x, define

    w_D(n)=τ(n)(Σ_(d|n, d≤D) μ(d))²,    S_D(x,t)=Σ_(n≤x) w_D(n) B_t(x/n).

The weights are nonnegative, w_D(1)=1 and w_D(n)=0 for all 2≤n≤D by Möbius inversion. For 1/2<σ<1 and η>0,

    |S_D(x,t)| ≪_(σ,η) x^σ D^(2(1−σ)+η),    0≤t≤2.

In particular D can be any x^o(1), even exp(√log x), keeping the square-root ceiling with arbitrary loss. The remaining dilations only use arguments x/n<x/D. Unlike the prime sieve of 309, beyond D integers with small primes may reappear. For example, in D<n≤2D all proper divisors are ≤D, and the weight is exactly τ(n)μ(n)².

**Cost of the construction.** Open the square and put l=lcm(d,e). For squarefree d,e, the series of the weights τ(n) with l|n is ζ(s)² times the polynomial ∏_(p|l)p^(−s)(2−p^(−s)); this is checked by summing the local factor of τ over positive exponents. Hence w_D=τ*h_D with h_D a Dirichlet polynomial. In the absolute norm of coefficients with weight n^(−σ),

    ||h_D||_σ ≤ Σ_(d,e≤D; μ(d)μ(e)≠0) l^(−σ) ∏_(p|l)(2+p^(−σ)).

The product is ≪_η D^η (l≤D² and 3^ω(l)≪_ν l^ν for all ν>0). Decomposing d=gu,e=gv with g their gcd, the sum without that product is ≤Σ_(g≤D)g^(−σ)(Σ_(u≤D/g)u^(−σ))² ≪_σ D^(2−2σ), since Σ g^(σ−2) converges. Convolving h_D with the unsieved average of 309 proves the ceiling. The classical idea used is the square of a divisor sum; here one evaluates how much it costs, and how much it must cost, to open a gap in this average of the balance.

**Optimality of the norm exponent.** Suppose w=τ*h is any other system of real weights with w(1)=1, w(n)=0 on 2≤n≤D and w(n)≥0 for all n. One is forced to have h(p)=−2 for p≤D. For two distinct primes p,q∈(D/2,D], one has w(pq)=4−4−4+h(pq)≥0, whence h(pq)≥4. There are ≫D²/log²D pairs for large D, with distinct products up to order. Hence

    ||h||_σ ≥ c_σ D^(2−2σ)/log²D.

The same barrier holds for a norm truncated at x if D²≤x. In particular, for a gap D=x^δ with 0<δ<1/2, every argument that only multiplies the bound x^σ of 309 by that norm pays at least x^(σ+2δ(1−σ)−o(1)). As σ approaches 1/2 the loss is a power x^δ. Thus, optimizing the weights within this class without exploiting cancellation between the coefficients of h does not take this method to a power gap with square-root error. This imposes no lower limit on the arithmetic balance S_D.

**Remaining obligation.** For subpolynomial D the above ceiling already controls B_t(x)+Σ_(D<n≤x)w_D(n)B_t(x/n) in modulus. A floor of order −x^(1/2+ε) for the tail, uniformly or in the relevant integrated version, would close the one-sided ceiling of 292. The positive weights and the gap leave that inequality open.
