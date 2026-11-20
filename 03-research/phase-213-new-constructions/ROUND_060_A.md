# Averaging fourth-power scales eliminates the squarefree condition in each slope

In 059 the integral term of each slope was annihilated, but an error remained when counting squarefree integers. Here the **complete identity without cutoffs** is averaged over the scales x/k⁴. The unique decomposition as a square times a squarefree number allows estimating jointly the slopes of reduced product up to

    R=L exp(−δ√log L),     L=√x,     δ>0 fixed.

Its cost is o(L), even summing the absolute values of the totals per slope. The change abandons the individual ranges of 056 and uses a new criterion equivalent to the sign, not an improvement of the previous count for the truncated weight itself.

**Exact identity.** Use V from 047, β=ε*ε from 056, b₀ from 059 and y=4x. For each x>0 define Q(x) by the sum of μ(d)μ(m)β(w)V(dmw/y) multiplied by [log(d/L)+log(m/L)]/2−b₀ over all positive indices, without cutoffs. It is finite and vanishes for sufficiently small x. If B(x)=4A(x)−4A(2x)+A(4x) of 054, then

    Q(x)=B(x)−(log L+b₀) Σ_{j=1,2,4} c_j V(j/y),   (c₁,c₂,c₄)=(1,−4,4).

Indeed μ*β=α, μ*α has masses c_j, and (μ log)*1=−Λ by divisor inversion. By symmetry it suffices to expand the logarithm of the first index. The additional term is supported on a compact set of x away from zero.

**Criterion.** Write S(x)=Σ_{k≥1}Q(x/k⁴), a finite sum. The global sign is equivalent to S(j⁴)≤Cj² eventually. If the sign holds, |B(x)|≪√x by 047 and therefore |S(x)|≪√x using Σk⁻²<∞. The sum of the compact corrections costs O(x^(1/4)), since only k comparable to x^(1/4) enter.

For the one-sided converse, the first two logarithmic derivatives of B and B itself are O(x) on the whole positive half-line by Chebyshev, smoothness and support. The compact correction satisfies the same bounds, and Σk⁻⁴ converges. Thus S(exp r)exp(−r/2) is interpolated with error O(1) between the samples at 4log j as in 047. On Re s>1 the Mellin transform with convention ∫S(x)x^(−s)dx/x is

    ζ(4s)[(2−2^s)² V̂(s)(ζ'/ζ)(s)+E(s)],

with E entire from the compact correction. This follows from the series of Λ by absolute convergence and from the change x=k⁴u; V̂(s)=∫V(t)t^(s−1)dt. The expression is regular on the whole real axis s>1/2, including s=1 because of the double zero. If S(x)≤C√x eventually, Landau applied in log x to C√x−S(x) on a tail gives holomorphy for Re s>1/2 as in 038. On 1/2<Re s<1 the factor ζ(4s) does not vanish and neither does (2−2^s). By 044–047 V̂(s) is the product of the averaging factor P(s−1/2) with
     
    2b [1−cosh(h(s−1/2))/cosh(hb)]/[b²−(s−1/2)²],

where b=3/2, h=log16 (integrate the exponentials of 044). Both are nonzero in this strip. Hence no pole of ζ'/ζ there can stay hidden, and one concludes by Weil as in 038. For a two-sided version, instead, the elementary inversion Q(x)=Σ μ(k) S(x/k⁴) and the two-sided bound of 047–054 suffice.

**What happens in a slope.** Let d=at, m=bt, (a,b)=1, r=ab. For nonzero terms r is squarefree. Let f(u)=(log u−b₀)Σ_w β(w)V(u²w/4), the smooth profile of 059, flat at zero, compact from above and of integral zero. At scale x/k⁴ there appears f(k²t/T) with T=L/√r. The contribution of the slope is exactly

    μ(r) Σ_n f(n/T) 1_{v_p(n) even for all p|r}.

Indeed n=k²t with t squarefree is a unique decomposition; the condition on its valuations is precisely (t,r)=1. This replaces the asymptotic density of 057 by a discrete identity.

The indicator is Σ_{h|n, rad(h)|r}(−1)^Ω(h), by alternating sum at each prime power. Extend f by zero to the line. Poisson and ∫f=0 give |Σ_l f(l/Z)|≤C Z^σ with **one and the same C** for all 0<σ≤1/2: if Z≥1 integration by parts twice suffices; for small Z the sum vanishes, and the intermediate interval is compact. The sum over l is over positive integers. Thus the total of absolute values of slopes for r≤R is at most

    C L^σ Σ_{r≤R} 2^ω(r) Σ_{rad(h)|r} h^(−σ)
      ≤ C L^σ R log(2R) ∏_p [1+2/(p(p^σ−1))].

For the inequality, fix h and write r=rad(h)j. Use 2^ω(r)≤2^ω(h)τ(j) and the elementary sum of τ. The logarithm of the product is o(1/σ) as σ tends to zero: each term multiplied by σ tends to zero and is ≤2/(p log p), summable by Chebyshev and partial summation. With σ=δ/(2√log L) one gets a bound L exp(−(δ/2+o(1))√log L), which proves the statement. For r=1 the decay by Poisson is already fast; the new diagonal is included.

**Scope.** The uniform upper bound O(L) on the slopes with r>R is still missing. The average does not erase poles of the global bridge; its proven advantage is that it replaces the count of squarefree t by a smooth sum over all integers, with an explicit condition on the primes dividing r. Inversion by square powers and the Poisson formula are known. The comparison is with the representation of 059 before averaging, which keeps a narrower individual support.
