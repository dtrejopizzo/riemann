# Maximal gain from allowing pairwise coprime composites

For large real x set f(t)=log t log(x/t). Let M(x) be the maximum of Σ f(m) over sets of pairwise coprime integers in [2,x]. With S of 092 one has unconditionally

    M(x)−S(x)=3 S(x^(1/3))+O(x^(1/4) log² x) ∼ 3 x^(1/3).

Assign each m to its smallest prime divisor p. The assignment is injective on each admissible set. The unassigned primes have cost f(p)≥0, so for an upper bound on the gain it suffices to add up the positive gains per prime. If m is composite, m≥p². For p≥x^(1/4), f decreases from p² to x whenever p²≤x. The improvement is then at most the positive part of f(p²)−f(p)=3 log p log(x^(1/3)/p). It is zero from x^(1/3) on. For p<x^(1/4) the total of all improvements is O(x^(1/4)log²x), since f≤log²x/4. This gives the ceiling. For the floor, take all primes up to x, replacing p by p² exactly when p<x^(1/3). The set is still pairwise coprime and the improvement sums exactly to 3 S(x^(1/3)). Finally S(y)=∫₁ʸ θ(t)dt/t ∼ y by the prime number theorem.

**Implication for the sign.** M(x)≤x eventually is equivalent to the global sign: it implies S(x)≤x; conversely the margin under RH of 092 exceeds 1.95√x eventually and the gain of M is o(√x). This removes the need to recognize primes in the formulation of the maximum: only integers, their weights and the condition gcd(m,n)=1 for each pair intervene. The open goal is a combinatorial upper bound for this maximum with the required leading constant and one-sided error. The model of 096 does not respect this restriction. It is not claimed that replacement by squares maximizes exactly for the small primes.

**Exact solution of the maximum (audit).** Decomposing each m into its exact prime powers preserves coprimality and increases the weight if there is more than one factor, since f(ab)=f(a)+f(b)−2 log a log b. Then each prime chooses its exponent independently, including zero. The increment from k to k+1 is log p [log x−(2k+1)log p], decreasing in k. Positive increments always lead to an admissible power p^(k+1)≤x. Therefore

    M(x)=Σ_{k≥0}(2k+1) S(x^(1/(2k+1))).

There are only O(log x) nonzero summands; those with k≥2 add up to O(x^(1/5)log²x) using S(y)=O(y) uniformly for y≥2. The identity determines an extremal set for every x, with equivalent choices when an increment is zero.
