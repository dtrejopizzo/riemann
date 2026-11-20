# Interpolation of the prime comb at the fourth-power nodes

In the reduction 121–122 all prime data can be replaced by two moments of each interval between consecutive fourth powers. The replacement is simultaneous for the vectors of the test space. It does not need an estimate for primes in short intervals.

Let X=exp(2T), F real normalized with support in [−T,T] with extension by zero in H¹ and ||F'||₂≤B. Let c be its autocorrelation and f(v)=v^(−1/2)c(log v). For v≥1 one has |f''(v)|≤C(1+B²)v^(−5/2): the factor in parentheses in the second derivative is c''−2c'+3c/4, and the respective bounds are B², B and 1 by Cauchy–Schwarz. In particular c'' is the negative autocorrelation of F', continuous, also where the support ends. Thus f and its interpolation can be considered on the whole half-line without creating an artificial jump at X.

In each cell [m⁴,(m+1)⁴] let If be the linear interpolant through the endpoints. The length is O(m³), hence |f−If|≤C(1+B²)/v there. Outside the cells touching [1,X] both functions vanish. For the signed measure dD=Σ_p(log p)δ_p−dv one gets

    |∫(f−If)dD| ≤ C(1+B²)(1+log X).

Indeed each dyadic band contributes O(1+B²) by Chebyshev for the prime mass and by integration for the continuous mass. The upper endpoint of the last cell is O(X). The same proof holds for dD restricted to the block (X^a,X], taking the moments only of the portion of the cell included. By affinity, ∫If dD on each cell only uses ∫dD and ∫v dD, with the edges assigned once. Equivalently the mass is distributed to its two nodes with barycentric weights. Being a uniform bound of quadratic forms, it is a norm bound for the difference of the symmetric matrices, with factor 2 for the convention of 121.

By 121 and 122, taking N=ceil(T log log(T+4)), B=πN/T, the largest positive eigenvalue of the block so interpolated keeps the rate of the original block (use log(1+positive part)). It suffices to bound that excess by exp(o(T)) along some unbounded sequence. The concrete benefit is the freedom to redistribute the primes within each cell while preserving the two moments; all the remaining detail of their positions costs at most O((1+B²)(1+T)). The one-sided comparison for the moments actually produced by the primes is missing. The number of cells grows like X^(1/4).

Cross-check: 039 and 044 already use fourth powers and interpolation for a scalar discrepancy; here the test function of each vector is interpolated and the error is controlled in norm. R166_702 already displaces primes to study Beurling systems. No novelty is claimed for linear interpolation nor for the idea of displacing primes.
