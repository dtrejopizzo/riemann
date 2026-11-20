# One-sided majorant for the Möbius parity and its first failure

For a large endpoint N fix κ>0 and δ=2 asinh(κ/(2√N)). Let Wδ(v)=max(1−|v|/δ,0). For n not squarefree put Q(n)=0. For n squarefree define

    Q(n)=2^(−ω(n)) Σ_(d,e|n) μ(d)μ(e) Wδ(log(de/n)).

For each κ≤√3 one has Q(n)≥μ(n) for all n≤N and

    Σ_(n≤N) |Q(n)−μ(n)| ≪ √N/log log N.

For κ≤1 there is exact equality. On the other hand, for each √3<κ<2 there are infinitely many N for which Q(N)<μ(N). This locates the first loss of the pointwise majorization. The sum defining Q uses pairs of divisors and the condition that n be squarefree; it does not need to multiply by the unknown sign of the whole integer.

**Complement and cancel.** For squarefree n replace e by n/e: μ(n/e)=μ(n)μ(e). In the resulting sum with Wδ(log(d/e)), the diagonal d=e contributes μ(n). For an off-diagonal term write a=d/gcd(d,e), b=e/gcd(d,e), and m=n/(ab). The three factors a,b,m are pairwise coprime. For each reduced ordered pair there are 2^ω(m) choices of the common factor, and μ(n)μ(d)μ(e)=μ(m). Thus the correction is exactly the sum, over ordered pairs a≠b with ab|n and (a,b)=1, of

    μ(m) 2^(−ω(ab)) Wδ(log(a/b)).

If a<b and h=b−a, the term is nonzero only if

    h√m = 2√n sinh(log(b/a)/2) < κ√(n/N) ≤ κ.

For κ≤√3, only h=1 with m=1 or 2 is possible. The case m=2 would require two consecutive integers to be both odd, because (ab,m)=1. What remains is m=1, with positive sign. For κ≤1 not even this possibility survives. This controls the sign before averaging.

**Total price.** The only positive corrections occur at n=a(a+1) and cost at most 2·2^(−ω(a(a+1))) per n. For a≤√N bound the weight using only primes p≤z, z=c log N. At each prime there are two distinct residues with p|a(a+1), so the average of that truncated weight over a primorial period is exactly ∏_(p≤z)(1−1/p). This is ≪1/log z, since its inverse includes the harmonic sum up to z. By Chebyshev the period is ≤N^(1/4) if c is small enough. Counting complete periods and the remainder proves the announced cost, uniformly also for any subinterval.

**First counterexample.** Take a≡1 mod 3 and a,a+1 both squarefree. The set of such a has positive density: truncate the primes at z, use the Chinese remainder theorem, and bound the upper density of the tail by 2Σ_(p>z)p^(−2), counting in addition O(√T) rounding terms up to T. For N=n=3a(a+1) the pair (a,a+1) with m=3 is active for large a and every κ>√3, by the identity above. If κ<2 all active pairs have h=1 and m=1,2,3. Case 2 remains excluded. Case 1 would require 3a(a+1)=s(s+1), which implies s=√3 a+(√3−1)/2+O(1/a). By equidistribution of the multiples of the irrational √3, these a have density zero (bound first by a fixed neighborhood and then shrink it). In the others only negative terms remain, so the majorization fails.

**Use and scope.** For the rises of 287 one can replace μ by Q at the scale N of the right endpoint, and the error on any subinterval fits in the budget. Equivalently, Q is the average of the ordinary square of Σ_(d|n)μ(d)exp(it log(d/√n)), normalized by 2^ω(n), against the positive density whose characteristic function is Wδ. The ordinary square can be negative: one is not averaging a squared modulus. The pairing leaves an explicit majorant and an exact boundary for its sign; a square-root upper bound for the sums of Q is still missing. The bilinear form of 281–283 and the sieve obstruction of 043 do not evaluate this first collision in the pair of complementary divisors.
