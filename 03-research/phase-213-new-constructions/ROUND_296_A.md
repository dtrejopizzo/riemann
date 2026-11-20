# Two monotone cutoffs and the number of primes separating them

For b_t of 292 write B=Σ_(n≤x)b_t(n), S(p)=Σ_(n≤x; P⁺(n)≤p)b_t(n) and u_p=1−Re(χ(p)p^(it)). For all sufficiently large x and all t∈[1,2], S is nondecreasing on the range I=[√(x/25),√(x/8)]. At the endpoints it starts below min(0,B) and ends above max(0,B). Let p₀ and p_B be the first primes of the range where respectively S≥0 and S≥B. Define

    W(x,t)=Σ_(p₀<p≤p_B) u_p if p_B>p₀, and zero otherwise.

The criterion of 292 is equivalent to ∫₁² W(x,t)dt ≪_ε x^ε for all ε>0. The cutoffs are also defined without writing the total B: p_B is the first prime at which the sum over integers with a prime factor larger than the cutoff becomes nonpositive. Separation in the opposite orientation costs nothing in this criterion.

**Slope certificate.** On 8≤z≤25 put J_t(z)=Σ_(m≤z)b_t(m)(1/m−1/z)=z K_t'(z). The function is continuous (also at the integers) and affine in 1/z between consecutive integers. verify_296.py checks K_t(8)>1/100, K_t(25)<−1/100 and J_t(j)<−1/100 for each integer 8≤j≤25 on 1024 interval cells covering [1,2]. Hence the whole range has slope of that sign. The signs of S at the endpoints and the fact that both targets are crossed follow from 295 and from B≪_R x/log^R x of 294.

**The discrete jump has the same sign.** For p prime in the range and z=x/p², the new terms of exponent one have cofactor ≤x/p and all their primes strictly less than p. In the full partial sum of those cofactors, a factor q≥p is unique and simple (x/p<p² for large x) and the remaining cofactor m≤z≤25. Those with exponent two at p are added separately. Thus

    ΔS = −2u_p [Σ_(k≤x/p)b_t(k) + 2Σ_(m≤z)b_t(m) Σ_(p≤q≤x/(pm); q prime) u_q]
         + u_p² Σ_(m≤z)b_t(m).

By the PNT in the classes modulo 3, the sum over q is (x/(pm)−p)/log p + O(p/log²p), uniformly, even with nearby endpoints: the approximation has absolute error and is applied on [p,25p]. The full sum over k is O(p/log²p) by 294. Hence

    ΔS = −4u_p p z J_t(z)/log p + O(u_p p/log²p).

The factor u_p also multiplies the error; jumps with small u_p remain controlled. There are absolute constants c,C>0 such that c u_p√x/log x ≤ ΔS ≤ C u_p√x/log x on all of I for large x. This proves the monotonicity of the effective values, in addition to that of the continuous main profile.

**Measuring the balance.** With H=√x/log x, on crossing each target its excess lies in [0,CH]. Hence |max(B,0)−max(S(p_B)−S(p₀),0)|≤CH. If p_B>p₀, the last difference is a sum of jumps between cHW and CHW. If p_B≤p₀, W=0 and the corresponding positive part vanishes. Integrating gives the announced equivalence in both directions. The choice is measurable by finitely many inequalities in t.

**Unconditional approximation to the required order.** Even without knowing the sign of B, the sum of weights u_p between the cutoffs, in either order, is ≪1+|B|/H. By 294 it is O_R(√x/log^R x) for every fixed R. Also |p_B−p₀|≪_A √x/log^A x for every fixed A: if an interval of that length fitted between them, the PNT in fixed classes with remainder of any logarithmic power would give ≫√x/log^(A+1)x of u_p mass, a contradiction on choosing R>A+1. Control at the precision of every logarithmic power does not reach the subpolynomial bound for the weighted count in the unfavorable orientation. The two cutoffs are defined via different sums (block and complement), but measuring their separation through the jump identity does not by itself give the pending inequality.
