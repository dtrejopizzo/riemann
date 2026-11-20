# Optimal cost of universally compressing to a fixed number of endpoints

Fix r≥1. Among all lists of up to r+1 binomial endpoints ≤N, the minimum of the worst-case cost to reproduce a single arbitrary row on all integer moduli is of order N^(1/r), with constants that may depend on r. The list may be optimized anew for each N, and real coefficients are allowed. For the lower bound a row with two equal sides suffices if the list includes N.

**Precision of the model.** The cost is the sum of the absolute values of the coefficients, infinite if the row has no representation. The formal reproduction of 269 and reproduction on all moduli give the same problem: the matrix (⌊j/m⌋) for j,m=1,…,N is triangular with unit diagonal. The coordinate m=1 of each row is automatically zero. A list omitting N fails at m=N for any nondegenerate row with endpoint N.

**Certificate for any list.** Write the list as N,n₁,…,n_r, repeating N if endpoints are missing. For N sufficiently large put Q=⌊(N/32)^(1/r)⌋. Among the Q^r+1 vectors of fractional parts of j(n₁,…,n_r)/N, for 0≤j≤Q^r, two fall in the same box of the partition into Q^r cubes of side 1/Q. The difference of their indices gives 1≤l≤N/32 with dist(l n_i/N,ℤ)≤1/Q for all i.

Evaluate the formal symbols at F_j=sin(2πlj/N). For an allowed endpoint n reduce θ=2πln/N modulo 2π to the representative of smallest modulus. Then |θ|≤2π/Q and for any phase split u=2πlk/N one has

    |F_n−F_k−F_(n−k)| = |sin θ−sin u−sin(θ−u)| ≤ 2|θ|.

On the other hand, choose k as the integer nearest to N/(4l). It has 1≤2k≤N and |u−π/2|≤π/32. In particular |sin(2u)−2sin u|≥2cos(π/32)−sin(π/16)>1. The row with endpoint 2k and sides k therefore needs variation ≥Q/(4π). The certificate is built from the endpoints, before choosing their coefficients.

**Matching ceiling.** Take in 269 the base b=⌊(N/2)^(1/r)⌋+1. Since b^r>N/2, at most r distinct shifts and N are used. Each k≤N/2 has at most r digits and the cost is ≤4r(b−1). The two bounds fix the exact exponent for every fixed r.

**Decision for the sign problem.** With three optimally chosen endpoints, the worst universal loss is already of order √N. A list of fixed size never offers loss N^o(1) for a procedure that replaces each row and preserves all moduli. This delimits the use of the compression of 269: for a fixed number of endpoints and subpolynomial loss one will have to exploit the concrete target of 262, the freedom on composites or cancellations between rows. The sinusoidal functional used here acts on all symbols and has not been represented by the prime-power and entropy constraints. No floor of this size follows for the weight g.
