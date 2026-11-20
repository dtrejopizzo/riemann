# The linear error of test 187 is realized with both signs

With the conventions of 187 and fixed κ>0, there are frequencies Γ_+ and Γ_− in [2G,3G] such that |S_X(Γ_±)|/√X=o(T) and

    min_θ W_T(f_θ) − [log Γ_± − |S_X(Γ_±)|/√X] = ±(2+o(1))T.

Thus, looking for the residual sign through a uniform replacement of the error O(T) by o(T) fails even in the prescribed band and for the comb of ζ. The constructed examples have a large positive main margin.

**Signed correction.** The exact overlap of 187 gives for the preceding difference, uniformly in Γ,

    −(4/B) Re Σ_{n≤Z}Λ(n)(1/n−1/Z)n^{iΓ} + O(1),  Z=e^T.

Indeed, the internal part is independent of θ and the two substitutions in the cross part cost O(1) in total. Poles and the difference of the archimedean term from log Γ cost O(1). The terms of non-prime powers of the internal sum are O(1) absolutely by convergence. The term 1/Z costs O(1) by Chebyshev. The mass of the primes with weight log p/p up to Z is (1+o(1))T by PNT, so 2 is likewise the best possible leading coefficient for the uniform error.

**Choice of the frequency.** Take Y=Z/T³ and K=floor(T). For σ∈{−1,1}, use R(t) of 185 over all primes p≤Y with local coefficients σ^r b_r. The sum of squares of the coefficients is one, and the length L of R satisfies log L≤K ψ(Y)=O(Z/T²)=o(log G). The square of the sum of moduli of the coefficients is ≤L. Use the probability on [2G,3G] proportional to |R|². Its normalizing constant, in the measure dt/G, is 1+o(1). As in 185, the expectation of σ Re p^{it} is cos(π/(K+1))+o(1) uniformly for p≤Y. The diagonal errors in these averages are O(YL²/G). By nonnegativity and Markov,

    Σ_{p≤Y}(log p/p)(1−σ Re p^{it})=o(T)

with probability tending to one (choose an o(T) threshold larger than the expectation by a divergent factor). Between Y and Z the mass is O(log T) by Chebyshev and partial summation. The signed correction −(2σ+o(1))T is obtained.

**The cross sum at the same frequency.** In S_X the primes p≤Y cost O(Y log X)=o(√X). The mass in powers of order ≥2 up to x is O(√x) by Chebyshev for squares and O(x^(1/3)log²x) for the others. Integrating against dx/x, their contribution to the Riesz weight is O(√X). For primes p>Y use the second moment of H(t)=Σ_{Y<p≤X}(log p)log(X/p)p^{it} against the same probability. The diagonal of |RH|² consists only of identical coincidences by unique factorization, since the indices of R are Y-smooth. Its mass is Σ_{p≤X,p>Y}(log p)²log²(X/p)=O(X log X), by Chebyshev on strips with j≤log(X/p)<j+1 and the sum of (j+1)² exp(−j). The error of the off-diagonal integral is O((LX)L X²/G)=o(1), by separation of logarithms of integers up to LX and Σ_p(log p)log(X/p)=O(X). In particular |H(t)|≤√X T^(3/4) with probability tending to one. The intersection with the previous event has positive probability for large T, which proves both statements simultaneously.

**Scope.** The resonator already known from 185 and the identity of 187 are used. The additional obstruction is a realization inside the band of the optimal coefficient of the correction and its independence, in this example, from a large value of the cross sum. The proof does not say that the same correction is possible *conditioned on* |S_X|/X being close to κ.

The correction, the length of the resonator, the diagonal of the second moment and the simultaneous selection of frequency were checked independently.
