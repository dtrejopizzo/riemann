# It suffices to estimate cofactors without small primes, with a single prescribed cut

For X≥e fix y(X)=4^⌊log₂(log X)⌋, so that (log X)²/4<y(X)≤(log X)². Let R_{z,h}(x) be the sum P_h of 353 retaining only pairs pm in which all primes of m are greater than z (m=1 is admitted). The exterior prime p has no restriction. Then

    RH ⇔ for each ε>0, ‖R_{y(X),h}‖_X ≪_ε √(hX) X^ε,
          for all X≥e and 0<h≤1.

Here the norm uses the whole block [X,2X] with the cut frozen at y(X). In contrast with 356, the criterion only asks to estimate cofactors that have **no** small prime. It is a reconstruction by convolution; it does not claim that the removed set has small mass. The factor log(2X) of 353 can be absorbed into X^ε.

**Exact identities.** For f(x) write T_d f(x)=f(x/d). Factorizing the prime factors of the cofactor gives, for z≥w,

    R_z = Σ_{d with primes in (w,z]} T_d R_w,
    P = Σ_{d z-smooth} μ(d) T_d R_z.

In the first equality the coefficients are +1, with all powers allowed. In the second only squarefree d contribute. Both sums admit d=1 and h stays fixed under each dilation. They are verified in the half-plane of absolute convergence by multiplying the factors of 1/ζ and keeping the common factor of the simple primes; they are also coefficient identities by inversion. Only d≤2X matter in a block X.

**Cost of an expansion.** For z≤(log X)², the sum of the moduli of coefficients with weight d^(−1/2) in either of the two expansions is ≤∏_{p≤z}(1−p^(−1/2))^(−1)=X^o(1). Indeed its logarithm costs O(√z/log(2z)+log log(3z)) by Chebyshev and partial summation. The weight d^(−1/2) is exact when transferring the norm normalized by √(hX) to the block X/d. In every block 1/2≤Y≤X^κ there is moreover a uniform trivial ceiling for any cut: each coefficient per integer has modulus ≤log(2+2Y), there are O(1+Y) integers and each pulse has norm ≤√h. The normalized cost is O((1+√Y)log(2+2Y)).

**Direct direction.** Under RH use 353 and the first expansion with w<2 (for example w=1, R_w=P). The bound of 353 on the children X/d≥2, the trivial ceiling on the smaller ones and the cost X^o(1) give the postulated bound, starting with a loss of exponent less than ε.

**Reconstruction with the only available cut.** For the inverse direction start from the second expansion with z=y(X). In a child of scale Y, if Y≤X^κ use the trivial bound. If the inherited cut z coincides with y(Y), apply the hypothesis. If z>y(Y), use the first expansion with w=y(Y) and repeat on the children, without increasing the cut. Between scales X^κ and X there are at most 2+⌈log₂(1/κ)⌉ distinct values of y. At each node requiring expansion the cut decreases strictly, even for the term d=1. Thus the depth is bounded independently of X for fixed κ. At each level the sum of normalized costs is at most that of the previous level multiplied by X^o(1); the stopped branches can be carried along with cost one. With κ small relative to ε, the trivial bound on small leaves and the hypothesis with exponent ε/3 on the other leaves finally give ‖P_h‖_X≪_ε √(hX) X^ε. 353 implies RH.

**Limit.** 309 already uses the cost of small Euler products at scale log². Here the reconstruction resolves the mismatch of the cut when replacing X by X/d: a single cut per scale suffices, without a uniform hypothesis over all lower cuts that would include the original problem. Proving the signed estimate for these sieved cofactors remains.
