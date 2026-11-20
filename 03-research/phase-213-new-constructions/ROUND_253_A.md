# Simultaneous positivity of all logarithmic moments up to s=9·10^24

Let P(s)=Σ_p(log p)p^(−s), K(s)=2(s−1)/(s(s+1)(s+2)) and F=KP, as in 247. With Z1–Z3 and 248, for every integer n≥0 and every real 1/2<s≤S=(3·10¹²)² one has (−1)^n F^(n)(s)>0. For s>1 this certifies on the genuine primes the sign of the complete integral

    ∫₀^∞ C(exp t)t^n exp(−st)dt.

For 1/2<s≤1 the statement refers to the analytic continuation. It does not require convergence of those integrals there. Unlike 245–246, these are the moments of a single fixed barycentre with independence between s and n.

**The anchor S.** For G=3·10¹² and every zero ρ one has |S−ρ|≥S−1/2. In the verified band Z2 gives it; in the tail |S−ρ|²≥(S−1)²+G²>(S−1/2)². This explains why a whole infinite family can be obtained from a finite verification.

When n≤30S, the integral over t≤46 is nonnegative by 248 (on [1,3] for the variable x it is seen directly from the prime 2). On [34,35] it contributes at least 0.035·34^n exp(−35S). For t>46, |C(exp t)|≤2exp(t) by θ(x)≤2x. Using log(t/46)≤(t−46)/46, that tail costs at most 2·46^n exp(−46(S−1))/(S−1−n/46). The ratio to the positive floor is less than one, since 30 log(46/34)<10 and at least exp(−S+46) remains before the prefactor 2/[0.035(S−1−n/46)].

**High moments.** For n≥30S normalise by (S−1/2)^(n+1)/n! and set u=(n+1)/S. In the formula of 248 the main term of squares gives 4/15. A term x^z goes to the factor [(S−1/2)/(S−z)]^(n+1), also for complex exponents. The sums can be integrated term by term at S by absolute convergence. The error 50 for J_d of 248 holds even for y≥1: the ceilings given there add up to at most 20+20·0.048+7 log(2π)+20 log 2<50. Therefore:
 
* The zero sum of J_1 costs <0.095 by the distance of the anchor and the budget 0.094+2.01·6.4·10^(−12) of 248.
* For J_2, the low zeros with exponent ρ/2 have real part 1/4, with cost ≤0.235 exp(−u/4); the high ones cost ≤5·6.4·10^(−12). The two bounded errors cost ≤100 exp(−u/2).
* For the removed odd prime exponents their one-sided ceiling from 248 suffices. The cost is ≤(2/3)[exp(−u/6)+exp(−3u/10)+(u/log 2) exp(−5u/14)]. Indeed, for z=1/3,1/5,1/7 the real factor is bounded by exp(−(1/2−z)u); for the log x term there additionally appears (n+1)/(S−1/7)≤2u.

For u≥30 all these ceilings decrease and their sum is <0.102. The normalised moment therefore exceeds 0.16 for n≥30S.

**Propagation.** In the open disc |s−S|<S−1/2, the identity P=−ζ'/ζ−Σ_{p,k≥2}(log p)p^(−ks) gives meromorphic continuation; the double sum converges locally absolutely. There are no zeros of ζ inside and K cancels the pole at 1. By Taylor expansion around S, each alternating derivative at a real point between 1/2 and S is a sum with positive coefficients of the alternating derivatives at the anchor. This concludes all orders strictly.

**Precise relation with closure.** It would suffice to prove the same simultaneous positivity at arbitrarily large real anchors. Indeed, for s→∞ and n=floor(st₀) with fixed t₀>0, the integral multiplied by s^(n+1)/n! converges to C(exp t₀): the weight is a gamma density with mean (n+1)/s→t₀ and variance (n+1)/s²→0. Continuity and the growth |C(exp t)|≤2exp t allow passage to the limit (the exponential second moment is uniformly bounded). One would get C(x)≥0 for all x and 247 applies. Conversely under RH the margin of 248 extends to all x≥10^20 using the bound of all zeros on the line from 247 in the same explicit formula of 248: the increasing term 2.01·6.4·10^(−12)√x disappears and the global sum |ρ|^(−2)<0.047 covers the whole series. The finite part is already certified. Thus the obligation of unbounded anchors is indeed equivalent to the global sign.

**Cross-check.** 129–134 already used factorial inversion and 247–248 already obtained the barycentre and the control height. The novelty of this combination is the unconditional proof at ALL orders on an explicit strip of s. The logarithmic normalisation of the moments is kept. The barrier of this proof is the distance inequality for zeros of height greater than G when the anchor is moved to the right.
