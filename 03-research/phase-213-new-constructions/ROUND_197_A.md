# Exact cancellation at the critical tail rate and a common window for every rate

Take the space of 196: arbitrary datum on [0,L] followed by a tail z exp(−v(y−L)) with v>1/2. There exist L₀>0 common to ALL rates and a common positive margin in L² norm for 0<L≤L₀. At the endpoint v↓1/2 the complete coefficients of this form have a finite limit. The sign statement for v=1/2 refers only to that regularized limit; the original moments diverge separately.

**Crossing at distance x=L−y.** For the unnormalized tail and almost every x in (0,L) the crossing functional is integration against

    k_v(x)=−(1/2)∫₀^∞ K(x+r)exp(−vr)dr
            +exp(x/2)/(v−1/2)+exp(−x/2)/(v+1/2)
            +exp(vx)[ζ'/ζ(v+1/2)+Σ_{n<exp x} Λ(n)n^(−v−1/2)].

The kernel K of 077 gives the archimedean crossing; the two moments are integrated directly. A prime contact crosses the cut exactly for log n≥x and at the other end evaluates exp(−v(log n−x)). Subtracting the prefix from the complete Dirichlet series gives the last line. The conventions at the contacts do not matter in L². The unnormalized diagonal is d_v=(ξ'/ξ)(v+1/2)/v by POWER_CONE_001.

**Critical endpoint.** By ζ'/ζ(1+h)=−1/h+γ+O(h), the singular terms leave −x exp(x/2). In the archimedean term integrate with t=x+r and z=exp(−t); one obtains −exp(x/2) artanh(exp(−x)). Thus

    k_*(x)=exp(x/2)[γ−x+Σ_{n<exp x}Λ(n)/n−artanh(exp(−x))]+exp(−x/2),
    d_*=2+γ−log(4π)>0.04.

The diagonal constant comes from the same expansion, ψ(1/2)=−γ−2log2 and the formula of 001. On each bounded x-interval the already combined singular part converges uniformly, except the prefix with fixed jumps, which also converges in essential sup norm. The archimedean integral is dominated by C_L(1+|log x|) for v≥1/2; by dominated convergence k_v→k_* in L²(0,L). In particular this expression can be used in the Schur complement without subtracting two divergent numerical quantities.

**Explicit example near the endpoint.** For L=10⁻⁴ there is no interior prime; |k_*|≤3+0.51 log(3/x), using (1+exp(−x))/(1−exp(−x))≤3/x. Integrating the square of this majorant gives <0.009 (the first two moments of log(L/x) in uniform measure are 1 and 2). The compact floor exceeds 2: in the Lévy representation of the archimedean term the correlation deficit is nonnegative, and for t≥L the correlation vanishes. Since m(0)>−6, K(t)≥1/t−1/2 for 0<t≤1, giving A≥[−6+log(1/L)−1/2]||g||². The polar term costs ≤2L exp(L/2)||g||², and the comb vanishes. Therefore d_*−||k_*||²/2>0.035; by continuity there is strict sign on this same window for all rates close enough to 1/2 from above. The size of the neighbourhood is not fixed.

**A common length without rate restriction.** Work in coordinates measured from the cut. By 196, on an initial window of fixed certified length there is a uniform margin for v≥V₀ large enough, using a tail of norm one. Reducing L only restricts the data to the left of the cut. For v∈[1/2,V₀], normalize by multiplying k_v by √(2v) and d_v by 2v. The normalized diagonal has a positive minimum on that compact set: 001 gives positivity by the theta kernel for v>1/2 and the critical value is positive. By the cancellation above, the normalized crossing is uniformly dominated near x=0 by C(V₀)(1+|log x|). Its L²(0,L) norm tends uniformly to zero. Choose L₀≤10⁻⁴ so that the square of that norm is less than half the diagonal minimum. The compact bound ≥2 and Young give a common coercivity for the complete combination, by orthogonality of the supports of the two data. This also covers the zone of intermediate rates; L₀ is not computed.

**Scope.** 001 contains the diagonal via logarithmic derivative and 196 the Schur criterion at fixed rate. The additional information is the regularized crossing vector, with its pole-by-pole cancellation, and a common interval for an arbitrary tail across all rates v>1/2. Positivity is not claimed for a superposition of tails of different rates nor for compact length 5.53 at all rates.
