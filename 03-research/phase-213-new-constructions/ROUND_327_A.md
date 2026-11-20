# Relative cancellation proved in the band of pairs that still demands exponential cancellation

For each fixed 0<a<log 4, with the notation of 325–326 and h=exp(−am), one has unconditionally

    P_m(a) ∼ h binom(2m,m) (∫η)²/[ζ(2)²∫η²],       E_m(a)=o(P_m(a)).

Hence the masses of the pairs with positive and negative Möbius product (the latter in modulus) are each asymptotic to P_m(a)/2. The o(1) is for fixed a. It is an application to the weight of 325 of the theorem of Matomäki and Radziwiłł on real bounded multiplicative functions in almost all short intervals. [Original article, Annals of Mathematics](https://annals.math.princeton.edu/2016/183-3/p06)

**Transferring the theorem to this window.** For f=μ or μ² let c_f be respectively 0 or 1/ζ(2), by the PNT or by the count of squarefree integers. For fixed b,B with a<b<2<B, uniformly over blocks [Y,2Y] with log Y between bm−O(1) and Bm+O(1), the mean square of

    (hx)^(−1) Σ_n f(n) η(log(x/n)/h) − c_f∫η

tends to zero. Indeed hY→∞ uniformly. The cited theorem, the limit of the long mean of f and the bound |f|≤1 give mean-square convergence for the backward additive averages of each fixed length in the block comparable to hY (the same backward conclusion is obtained by translating the variable with boundary error O(h)). To detail the passage to x-dependent length, approximate η uniformly by a step function to precision ε. Each endpoint of its intervals in n is written x−x(1−exp(−hu)) with u fixed. Round each length to a mesh of step ε' hY; there are only O(1/ε') lengths for the whole block and the error of each normalized endpoint is O(ε'+1/(hY)). For a fixed number of steps first take m→∞, then ε'→0 and finally ε→0. Applying the same count to f=1 yields the factor ∫η (the local Jacobian is exp(−hu)). Uniformity over the blocks also follows from the sequential criterion of the theorem, since both Y and each positive length of the mesh grow uniformly.

**Integrating the blocks with the correct weight.** For either of the two energies, the exact expression is

    (h∫η²)^(−1) ∫ |Σ_n f(n) l_m(n) η(log(x/n)/h)|² dx/x.

In the central region bm≤log x≤Bm, l_m(n)/l_m(x)=1+O_b(h) for n in the support, by logarithmic differentiation. The integration weight after normalizing the average is h x l_m(x)² dx/∫η². In each central dyadic block x l_m(x)² varies by a factor bounded independently of m, also by logarithmic differentiation. The uniform mean-square error of the previous paragraph therefore adds up as o(1) of the total integral of that weight. For the extreme blocks one can use the whole block and the same bound. The normalized averages are uniformly bounded, so this also controls the difference of their squares.

Outside that region use |f|≤1, the diagonal of 326 and the inequality between product and mean of squares used there. The cost is bounded by O(Δ_m) (or by the same diagonal without μ²) plus O(h Σ n l_m(n)²) restricted to log n outside [bm+O(h),Bm−O(h)]. The diagonal is negligible because a<log 4. The restricted sum is exponentially smaller than binom(2m,m): by integral comparison and unimodality its integral in u=log n is the tail of u^(2m)exp(−u)/(m!)² outside an interval containing 2m with margin proportional to m. The Chernoff bound for that gamma density suffices; the discretization error by the maximum is also exponentially smaller. The full integral of x l_m(x)² dx is binom(2m,m). This proves both claims.

**A quantitative distinction.** A quotient E_m/P_m tending to zero may still have its 2m-th root tending to one. On the other hand, if for a single fixed a in this range one proved R(a)≤2 exp(−a/2−δ) with δ>0, the floor of 326 would force Θ≤3/2−exp(δ)/2<1. Even that partial improvement would imply a fixed zero-free strip, uniformly at all heights. For RH, R(1/j)≤1 for all j remains pending. The short-interval theorem gives genuine relative cancellation and does not supply, through this argument, a gain in the exponent.
