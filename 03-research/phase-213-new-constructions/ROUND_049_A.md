# Criterion with two factors of size close to the square root

In 048, the positive coefficient of the primes depends on the centre of the logarithm. In the alternating criterion one can use log k at scale y=2x and log(2k) at scale x, because Σg(k/y)=V(1/y)=0 and analogously at x. With coordinated physical cutoffs, the high integrands correspond under dilation. The additional factor log K in the quadrature bound is absorbed by increasing the constant of the cutoff. In the lower sum k=1 then disappears and with it all the primes of the band. For n=2p with p a large prime the coefficient becomes +log 2. Thus the obstruction to summing positive parts is still present at this centre, although the primes no longer contribute.

**Additional step.** One can simultaneously eliminate every k≤√x from the criterion, keeping the second factor m around √x. One uses the fixed weight V with the order-two Gevrey bounds of 047, its inverse g, and the same cutoff function χ. For large x=j⁴ put y=2x, L=floor(√x) and K=A(2L) (log x)² with A a sufficiently large constant. Write a(k)=(−1)^(k+1)log k. For d≤L put b_d=−(μ*a)(d), where * is divisor convolution. For L<d≤2L put b_d=λ with

    λ=−(Σ_{d≤L} b_d/d)/(Σ_{L<d≤2L}1/d),

and put b_d=0 otherwise. Define c(k)=Σ_{d|k} b_d, and U(k)=1−χ(log(k/K)). Then the global sign is equivalent to the existence of C such that, eventually,

    Σ_{L<k<eK} Σ_{a₀ y/k≤m≤B y/k} U(k)[a(k)+c(k)] μ(m)V(km/y) ≤ C√x,

where [a₀,B]=[1/16,16e]. In this sum both factors are at least a constant times √x/(log x)² and at most a constant times √x (log x)². The number of outer indices grows with respect to 048; one gains an upper bound for both factors at once.

**Coefficients.** The identity μ*log=Λ and the even part of a give exactly

    (μ*a)(d)=Λ(d)−2·1_{2|d}(Λ(d/2)+(log 2)1_{d=2}).

From this Σ_{d≤L} b_d/d=log 2−Σ_{L/2<n≤L}Λ(n)/n for L≥2. Chebyshev gives |λ|=O(1), and Σ|b_d|/d=O(log x). In the band k<eK, the sum of the absolute values of the b_d for d≤L dividing k is O(log(2k)) by the divisor identity. For L<d≤2L there are at most k/L divisors because their quotients are distinct. Thus the coefficients a(k)+c(k) are O((log x)²) on the support. For k≤L they vanish exactly by finite inversion.

**Proof of the transfer.** The full sum Σ a(k)g(k/y) is 2A(x)−A(2x) with A(x) the discrepancy of 048: the extra term when unfolding the even part is a multiple of V(1/x)=0. Adding c(k) costs exactly zero, since for d≤2L one has Σ_{d|k}g(k/y)=V(d/y)=0. It remains to verify that the upper part with 1−U has size O(√x).

For a, separate the full mesh and the even one. The corresponding integrals cancel because the second is taken at twice the step with coefficient −2, evaluating the whole function (including log k) in the same physical variable. The estimate of 047 costs O(y(1+log K)exp(−c√(K/2))) when replacing the two upper sums by integrals; the increment log K is obtained by splitting log k=log(k/K)+log K in the proof of 047.

For c, the progression k=dv uses scale y/d and cutoff K/d in the estimate of 047 without the logarithm (its derivative bounds only improve). The error of sum minus integral is at most C(y/d)exp(−c√(K/d)), uniform in d≤2L. Its integral in v is (1/d) times the same integral in k for all progressions. When summed it disappears by Σ b_d/d=0. The total error is O(y log x exp(−c√(K/(2L))))=O(√x) by choosing A sufficiently large. What remains is the lower part of the statement after expanding g, and the equivalence follows from the recovery of 048.

**Scope and antecedents.** Vaughan identities and type II bilinear sums already appear in phase 104, 104_93, and in phase 211, ROUND_013_A §3 and REVIEW_009. No novelty is claimed for decomposing by divisors nor for the bilinear method. The targeted cross-check distinguishes the use of rows exactly vanishing on the samples of 048, with a density compensation that cancels the integral of all progressions, so as to leave only pairs of size close to √x. The signed inequality on those pairs remains open. No type II estimate at square-root precision has been obtained.
