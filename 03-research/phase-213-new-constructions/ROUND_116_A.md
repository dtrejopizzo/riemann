# Long intervals of excess and sampling on a sequence of bands

Let E be the prime discrepancy of 109 and Θ=sup Reρ. If Θ>1/2, for any ε>0, 0<δ<1 and 1/2<α<Θ, every sufficiently large band [X,X^(1+ε)] contains an interval [y,y+y^(1−δ)] where E(t)>t^α at every point. It also contains another interval of that type with E(t)<−t^α. A zero with real part Θ is not required.

**Existence of peaks.** Write Z(x)=−Σρ x^ρ V(ρ). By 112, E(x)=Z(x)+O(√x): the contribution of squares is O(√x) by Chebyshev on fixed support, the higher powers are O(x^(1/3)log²x) and the trivial ones are o(1). For J(v)=exp(−v/2)Z(exp v) the hypotheses of 115 hold, since V does not vanish in the open strip and is O((1+|γ|)⁻²). For any α'<Θ with α'>1/2 one can choose d between α'−1/2 and Θ−1/2. Apply 115 with mean (1+ε/2)log X and relative half-width small enough to stay strictly inside the band and so that d/(1+half-width)>α'−1/2. Thus there exist points y of each sign with ±Z(y)>y^α', separated from the endpoints of the band by a factor that grows with X.

**Variation between points.** For 0<u≤1/2,
    
    |Z(y(1+u))−Z(y)| ≪ y^Θ u log²(2/u).

Indeed |(1+u)^ρ−1|≪min(1,u(1+|γ|)), by integration in the logarithm and by the trivial bound. For |γ|≤1/u sum (1+|γ|)⁻¹ with the count N(T)≪T log(2T), and above that sum γ⁻². In particular for 0≤u≤y^(−δ) the loss is O(y^(Θ−δ)log²y), by the same splitting at height y^δ. Take α' strictly between max(α,Θ−δ) and Θ. This loss and O(√y) are absorbed by y^α', even comparing with t^α for every t of the interval. This proves both claims.

**Criterion by samples.** It suffices that there be fixed ε,δ>0 (δ<1), a sequence X_j→∞ and in each [X_j,X_j^(1+ε)] a mesh that includes the two endpoints and has consecutive steps of length ≤C t^(1−δ) from its left endpoint t, with E≤C'√t at all its samples. Under RH this holds by 109. If RH fails, apply the theorem with δ/2: the positive interval has length y^(1−δ/2), larger than any gap containing it. It includes a sample whose excess exceeds C'√t. For example any mesh of integer powers n^k works, for each fixed integer k≥1 (cut to the bands or choose endpoints on the mesh). The proof does not identify a mesh where the arithmetic bound is already known.

**Cross-check.** 039/044 use fourth powers, 090 uses a non-meager family of steps for different tests and 115 produces points in power bands. Here the variation controlled by the real abscissa Θ turns the peaks near the supremal exponent into intervals of length y^(1−δ); a variation estimate always using exponent 1 would be insufficient. The interval still has relative length tending to zero.
