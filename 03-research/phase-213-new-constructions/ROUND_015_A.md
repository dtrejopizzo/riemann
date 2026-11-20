# All signed coefficients at the scale of the far cell

Antecedents 213-10 to 014 and BUILD084. The new operation recovers the primitive of the coefficients on two complementary strips of the tail. This makes the error relative to the norm of the tail even with arbitrary cancellations. We use PNT for a fixed piecewise head test, keeping the whole tail. The mechanism was cross-checked before developing it.

**Statement.** There exists k₀ such that for each k≥k₀ the full energy is strictly positive for every nonzero combination of translations of F_k in an interval of length w=log(1+1/k). Finite complex coefficient measures are admitted. All shifts can be translated simultaneously to take the interval [0,w].

**Recovery on two strips.** Denote by μ the measure, by ν(ds)=exp(−s/2)μ(ds), by c its total mass and by L(u)=ν([0,u]) its cumulative function, 0<u<w. In the physical variable the tail b, at y=k exp(u) and y=k exp(w+u), has respectively values dL(u) and d(c−L(u)), up to irrelevant jump points. Let D=Ub. Integrating in dy,

    ||D||² ≥ d² k ∫₀ʷ (|L|²+|c−L|²)du.

Since kw is bounded below for k≥3, |c|≤C||D||. The head in logarithmic coordinates is cF+g where F is the original head of F_k. By 012-A the remainder g lies in the three jump tubes of width w and is built with H=L−c on (0,w). Hence ||g||≤C||D||/√k. If ||D||=0 then c=0 and g=0, so the whole mixture is zero. These bounds are independent of the total variation of μ.

**Self-energies.** On the fixed head window the comb is bounded and m has a lower bound, so a(g)≥−C||g||². The crossing functional with F has an L² representative of uniformly bounded norm: F is a bounded combination of two fixed BV profiles, to which 010-A applies. The diagonal a(F)=q(w)>0 for large k by BUILD084. Hence a(cF+g)≥−C||D||²/√k. Since the logarithmic support of D has length 2w, the fixed-window floor of 010-A, after translating, gives a(D)≥||D||² for large k. The integrals of translations against measures are taken in the domain by continuity in form norm on a fixed window for each k.

**Mixed crossings.** Each of the three tubes of g only contacts D for log n in an interval of length ≤3w located at log k+O(1). It contains O(1) integer indices n after exponentiating. The total arithmetic cost between g and D is O((log k)/√k)||g|| ||D||=o(||D||²).

For the comb between the original head F=Uf and D, write the mixed integral as the physical pairing of b(y) with

    S_k(y)=Σ_n (Λ(n)/n) f(y/n),     k≤y≤k exp(2w).

The factor 2 and the real part of the full crossing are included when bounding by 2|c| ||b||₁ sup|S_k|. For i=1,2 the cells [i,i+1) select y/(i+1)<n≤y/i. Partial summation of ψ(x)=x+o(x) gives in each band ΣΛ(n)/n=log((i+1)/i)+o(1), uniformly in that range of y (endpoints comparable to k). The coefficients of f are bounded and its inverse moment is −dw. Thus sup|S_k|=o(1). The physical support of b has length k(exp(2w)−1)=2+1/k. Hence ||b||₁≤C||D|| and the mixed cost is o(||D||²).

Finally the physical archimedean kernel between head and tail is O(1/k) by separation, as in 014-A. The physical supports have bounded length and the L² norms are O(||D||), so this last crossing is O(||D||²/k). The off-diagonal formula passes to measures by approximation of the integrals of translations in form norm for each k.

We conclude a(Y)≥(1−o(1))||D||², uniformly in the coefficients. The explicit radius w decreases with k. The result leaves open the positivity of every signed combination on a fixed radius independent of k, and that of the full window. Status PROVED after independent review.
