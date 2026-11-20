# Two-sided suppression of scales in the factorial remainder

With the conventions of 129 set D=floor(M^(33/16)), V=M^(1/32)=X^(1/128). The kernel K can be replaced by another explicit K* such that

    A(M)=∫_{V<v≤16X/D}(W−K*) dE − (7/3)M² + o(M²).

The part v≤V is paid even in absolute value with respect to dψ+b(v)dv. The two scale bounds hold simultaneously for the same formula. The repair requires no cancellation estimate for μ.

**Two correction coefficients.** Keep c_d=μ(d) up to D. Set S=Σ_{d≤D}μ(d), H=Σ_{d≤D}μ(d)/d and add c_{2D}=S−4DH and c_{4D}=4DH−2S. Then Σc_d=Σc_d/d=0 and Σ|c_d|≪D log(2D). Define K* as K with these coefficients. The two new dilations vanish above 16X/D, where K=W. In the full factorial integral 129 is applied to the two new indices: the proof there gives per large index Oε(M^(−2/25+ε) log²M + D/M⁴), also up to 4D because its denominator bounds admit constant factors. Multiplying by O(D log D) still gives o(M²). Hence ∫K* dE=o(M²).

**Lower endpoint.** For all v≥1 one obtains exactly

    K*(v)=Σ_d c_d (1/M) Σ_{M<m≤2M} (1/2−{m⁴/(dv)}).

The indices d≤M cost O(M) in modulus. For M<d≤4D and v∈[1,V] it now suffices to treat the full average of length M: the logarithmic Stirling weight no longer appears. For h≤M^(1/8) approximate h/(dv) by p/q via Dirichlet with Q=floor(M³), in lowest terms, |q h/(dv)−p|≤1/Q and q≤Q. The numerator is positive since h/(dv)≫M^(−33/16−1/32)>1/Q for M large. Thus q≥dv/(2h)≫M^(7/8). In quartic Weyl the parenthesis 1/q+1/M+q/M⁴ is O(M^(−7/8)); Erdős–Turán gives for the mean of the sawtooth Oε(M^(−7/64+ε)log M+M^(−1/8)). This is uniform even for real v and at the atoms where the fractional part vanishes.

By Chebyshev, the mass of dψ+b(v)dv up to V is O(V); both measures vanish below 1 (a_->1). Since |W|≤1, the lower absolute cost is bounded by

    Oε(V (1+M+D log²M M^(−7/64+ε))) = o(M²),

since 1/32+1/16−7/64=−1/64. This proves the formula via 129. It does not imply a bound for the central zone: there the weight has changed, including the two correcting dilations.

**Cross-check.** R162_801 already contains the exact factorial identity and its reading via Stirling. 047 uses regularization of the weight and localizes another quadrature with internal Möbius sums. Here the raw samples of 127 are kept; the exact cancellation of two coefficient sums allows removing the atoms with small argument and the density of that same interval in absolute norm. The pending goal is still to bound from above the central remainder of this representation.
