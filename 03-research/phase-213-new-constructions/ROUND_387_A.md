# The jump at the neutral cut is positive and smaller than the square root

**Status: PROVED, with independent review of the orientation of the jump and of the saving below square root.**

In the notation of 386, when raising the threshold y through a prime p with v=log(x/p²)=κ log z and κ in an interior compact subset of (0,1), the jump of W is

    W(p)−W(p−) ∼ J (x/p)/log(x/p) >0

uniformly. In particular there is a unique crossing in the band of 386 (possibly a plateau of value zero). The error when removing the chosen group is

    |W(y)| ≤ (2J exp(−1/4)+o(1)) √x exp(E/4)/L
            = √x L^(exp(γ)/2−1+o(1)) = o(√x).

In the first inequality it suffices to take one side of the jump, without interpolation.

**Cofactor of the jump.** The terms leaving W have largest prime exactly p. Removing it changes the sign, so the jump is the signed sum at scale X=x/p of m with all their primes in (z,p), including m=1 and the weight g(log(X/m)). Completing to all m without primes ≤z gives S^*(X;z), of absolute value ≪X exp(−c log X/log log X) by the frozen contour of 384, since log X∼L/2. Of what is added, the m with a prime q≥p and some other factor have m≥pz=X z^(1−κ), hence absolute mass ≪X exp(−c(log z)²) by the tail of 375. The rest are the primes q≥p, which contribute a minus sign. Here p=X exp(−v), and the mass of primes smaller than p costs ≪X exp(−c v²); one can complete to all primes to precision o(X/log X). The PNT and the Gaussian give for these (J+o(1))X/log X, by the substitution of 379. Subtracting the added balance gives the announced positive jump. The two Gaussian margins are uniform when κ is separated from 0 and from 1.

**Localization of the crossing prime.** On the interval v=E/2−1/2±1 of 386 all jumps are positive as y increases. The pre and post values of the crossing jump are O(X/log X), by signs and the uniform equivalent. The additive profile of 386 holds for both, including the left limit with the same v by uniformity. This forces v=E/2−1/2+o(1) at the crossing prime. If there is a zero plateau, one endpoint suffices. Substitute X=√x exp(v/2), log X∼L/2. Mertens and log z=2log L give the second expression as an upper bound with the stated exponent, strictly less than square root because exp(γ)<2.

**Review record.** When y increases, terms of sign −μ(m) are removed, so W(p)−W(p−) has sign +μ(m) in the cofactor sum. The complete sum S^*(X;z) is small, and what is added to complete it contains single primes with negative sign: subtracting them gives +JX/log X. The other added terms have m≥pz=Xz^(1−κ); their tail O(X exp(−c(log z)²)) is o(X/log X) uniformly if κ is separated from1. The omission of primes q<p is likewise o(X/log X) when κ is separated from0. All jumps in the band are therefore strictly positive for large x, so there is a unique crossing up to a zero plateau. Each side has absolute value at most the jump, without interpolating masses. The additive localization of386 at the crossing prime gives exp(v/2)=exp(E/4−1/4)(1+o(1)); together with log X∼L/2 it produces the announced constant2J exp(−1/4). The saving √x L^(exp(γ)/2−1+o(1)) is o(√x) because exp(γ)<2.

**Scope.** The two adjacent finite products of cut 386 enclose the true balance, with separation o(√x). The orientation comes from W increasing: before the crossing C=S−W≥S, after it C≤S. Any one-sided estimate at square-root scale is thus transferred with additive error o(√x); what is missing is an estimate of one of those products.
