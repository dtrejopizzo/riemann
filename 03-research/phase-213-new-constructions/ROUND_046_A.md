# The deficit is localised in the first j−1 terms of the quadrature

Antecedents: the signed remainder of 045; N_BUILD_006 §1 already uses a second integration for the periodic remainder. Here the constant log K is eliminated exactly before splitting the logarithm at its zero. That allows bounding the whole part over k≥K by O(x/K²) without a factor log K and without a first-order boundary error. One works with the quadrature discrepancy, not with the size of the original prime sum.

Let x=j⁴>81, W=W_j and g its inverse from 045. For integrable H with convergent sum write ΔH=∫₀^∞H(u)du−Σ_{k≥1}H(k). Define

    H₋(u)=g(u/x) min(log(u/j),0).

Then the global sign is equivalent to ΔH₋≤C j² for all sufficiently large integers j, with a common C. The sum of ΔH₋ only uses the indices 1≤k<j. Its integral reaches down to zero and each evaluation of g still contains Möbius coefficients at large scales.

**Exact centring.** By 045, ∫g=0 and Σ g(k/x)=Dg(1/x)=W(1/x)=0 because 1/x<1/81. Hence the full deficit of 045 is Δ[g(u/x)log(u/K)] for any K>0. The positive and negative parts of the logarithm give two summands continuous at the cut point.

**Uniform bound for the upper part.** For 1≤K≤x let H₊(u)=g(u/x)max(log(u/K),0). In its Möbius expansion only m≤16x/K appear. In the variable s=mu/x the summand without μ is F_z(s)=W(s)max(log(s/z),0) with z=mK/x. The support lies in [1/81,16], and the variation of its derivative, including endpoints and corners, satisfies

    Var(F_z') ≤ C(1+log(16/z)),    0<z≤16.

Indeed, for s>z the derivative is W'(s)log(s/z)+W(s)/s. The variation of W' and the norms of W,W' are uniformly bounded by 045. The derivative of the logarithm is 1/s, bounded on the support. At the cut only the jump W(z)/z is added if z belongs to the support. In u the variation of the derivative is multiplied by m/x.

For a compactly supported continuous function, absolutely continuous with derivative of bounded variation, the error of the trapezoidal rule with step one is at most a constant times the total variation of its derivative: on each cell, the difference with the linear interpolant is at most the oscillation of the derivative; sum over the cells. Apply this extending by zero to the line. With M=16x/K, one deduces

    |ΔH₊| ≤ (C/x) Σ_{m≤M} m(1+log(M/m)) ≤ C' x/K².

The last sum is O(M²), for example grouping m into dyadic intervals. No cancellation of μ is used. Taking K=j gives |ΔH₊|≤C' j². By 044–045 the full deficit must be bounded above by O(j²); the two-sided bound on H₊ proves the stated equivalence. In particular only the lower part could produce an unbounded excess after dividing by j².

**Pending.** It remains to estimate the difference between the integral and the sum in H₋. Counting j−1 outer indices neither limits the number of inner arithmetic terms to j nor controls the behaviour of the integral near zero.

**Limit of the estimate by absolute variation.** At even scales, the derivative of g has a jump of magnitude mW'(1/16+) at t=1/(16m) for each squarefree m: the other two possible terms carry μ(16m)=μ(256m)=0, as in 044. At u=x/(16m)∈[2K,4K], the derivative of H₊ therefore has a jump of magnitude at least (log 2)mW'(1/16+)/x. For x/K→∞ there are ≫x/K squarefree integers in the corresponding interval of ratio two, by the classical positive density of those integers. Summing distinct jumps one obtains Var(H₊')≫x/K². The order paid by using the total variation is exact for this subfamily. The statement leaves open any cancellation in the effective quadrature error.
