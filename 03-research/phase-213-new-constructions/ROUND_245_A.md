# Two increments of a positive average with data from earlier primes

For large t and each fixed rational 0<c<1/4 use n=floor(ct), δ=exp(−log²t)/t² and, with S from 240, compute

    J(v)=(3/2)^n ∫₀^∞ S(t+v−z) exp(−z) z^(n−1)/(n−1)! dz,
    F(v)=J(v+δ)−exp(δ)J(v).

The parameters t,n,δ are frozen at the three necessary evaluations v=0,δ,2δ of J. Each J is a finite sum of positive contributions of primes p≤exp(t+2δ+1/10), since the support of W is in [0,1/10]. No parameters need to be chosen according to zeros to define the family.

**Criterion.** The global sign is equivalent to the existence, for each such c, of starting points t→∞ with both |F(0)|, |F(δ)|≤exp(t/2+o(t)). The subsequences may depend on c. If RH fails there is even an open interval of slopes for which all sufficiently distant blocks violate the bound.

**Exact transformation.** Apply the expansion of 240 to S(u), including its mean H(1)exp(u). The remainder is O(exp(u/2)poly(1+u)) for u≥0. For u<0 define the remainder by the identity: it is O(1) because S(u) is bounded and the series of zeros converges absolutely with |exp(ρu)|≤1. In the average the u≥0 cost O(exp(t/2)poly(t)) using the gamma transform at 1/2; the u<0 cost O((3/2)^n), less than exp(t/2). Integrating each mode is justified by absolute convergence for fixed t. The main term disappears in F and the mode ρ in J is multiplied by [3/(2(1+ρ))]^n. Under RH all modes remain bounded in sum by C exp(t/2), since |1+ρ|≥3/2. This proves the condition at every starting point under RH.

**Maximum attained after averaging.** The rate of each mode in J is
     
    b_c(ρ)=Re ρ+c log(3/(2|1+ρ|)).

Given a zero with Re ρ>1/2, for small positive c its rate exceeds 1/2. On a compact interval of those slopes, only a finite set can compete, since b_c tends uniformly to minus infinity with height. Two lines of identical rates would require equal Re ρ and |1+ρ|, hence the roots would be equal or conjugate. Excluding the finitely many ties of the competing set leaves a subinterval with a unique conjugate pair and any rational in it works. For fixed c there, let D>1/2 be the winning rate, with gap η>0 to the remaining rates and to 1/2. The rounding of n costs at most a factor O(1+|ρ|) in each term. The summable moments of H from 240 give a total tail O(exp((D−η)t)), reducing η to absorb the polynomial of the remainder. This also holds in both first differences.

**Two readings.** For the winning zero ρ=β+iγ, the contribution of the pair to F(v) is 2 Re(Z exp(ρv)), with |Z| comparable to δ exp(Dt): the coefficient includes nonzero H(ρ), multiplicity and exp(ρδ)−exp(δ). For every complex Z, max(|Re Z|, |Re(Z exp(iγδ))|)≥|Z| |sin(γδ)|/2 (use the identity for the sine of the difference of phases). Since γ is fixed and nonzero, at least one reading has modulus ≥C δ² exp(Dt), which dominates the exponential error. This proves the converse even if the maximal deviation of the original zeros is never attained.

**Antecedents and obligation.** Selection by rates was already in 143 and 206. The internal novelty relative to those steps is the condition of two adjacent increments of a single positive sum over primes, per slope, with finite upper cut and only existence along a subsequence. The result replaces S by J; it does not produce two nodes of the unaveraged count of 244. The pending datum is an arithmetic property of J: obtaining two consecutive small increments for each c. Positivity of the weights of J fixes neither the sign nor the size of its increments.

**At the slopes that detect the failure, an isolated reading does vanish.** On each stretch ct∈[n,n+1) the argument of the dominant coefficient of F(0) is γt plus a constant depending on n and a uniform o(1) term: (exp(ρδ)−exp(δ))/δ→ρ−1. The length 1/c>4, and |γ|>14 by the first verified ordinate. In the interior there is room for linear phases with cosine +1 and −1. There the dominant term exceeds the error with opposite signs. By continuity on the stretch, F(0)=0 at some starting point for each large n. At those same starting points the second reading exceeds the threshold by the previous result. This confirms that requiring both readings has content even after averaging.
