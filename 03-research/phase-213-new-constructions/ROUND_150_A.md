# A fixed positive average that keeps the poles of the Liouville sum

**Result.** With U and R of 144, there is a fixed positive density w, independent of T, for which an eventual constant ceiling of F(T)=∫w(y)U(T+y)dy is equivalent to the global sign. Under RH one even gets F(T)<a/2 eventually, with a=1/ζ(1/2)<0. The unconditional bound on F remains open.

**Construction.** Let p be the even theta density with bilateral transform M(s)=ξ(1/2+s)/ξ(1/2), with convention ∫exp(sy)p(y)dy. For y≥0 it is proportional to the sum over n≥1 of (4π²n⁴exp(9y/2)−6πn²exp(5y/2))exp(−πn²exp(2y)). The identity follows by integrating twice by parts in the theta representation of ξ. Each summand is positive and the first gives the equivalent at infinity. For q(y)=(p(y−1)+p(y+1))/2, the ratio q/(|y|p) tends to infinity both at zero and at both ends. Its infimum h is positive by continuity. Thus w=q+εyp is a strictly positive density of mass one for 0<ε<h. Its transform is M cosh+εM'.

**Computation.** Putting z=1/2+s, B(z)=ζ(2z)(z−1)π^(−z/2)Γ(z/2)/(2ξ(1/2)), the bilateral transform of F is exactly

    R(s)[M(s)cosh(s)+εM'(s)] = B(z)[cosh(s)+εξ'(z)/ξ(z)].

Fubini holds initially for Re s>1/2 by |U(t)|≤exp(t/2) for t≥0 and U=0 to the left. The tail T<0 has entire transform by the doubly exponential decay of w. At each zero ρ with Re ρ>1/2 there remains a simple pole with residue εmρ B(ρ), nonzero by convergence of the Euler product at 2ρ. At s=0 the residue is a by M(0)=1 and M'(0)=0. There are no positive real poles, including z=1.

**Prior choice of ε.** By the classical count of zeros in unit bands there is an absolute constant D with N(n+1)−N(n)≤D log(n+2), counting multiplicities, n≥1. Take S=2D Σ log(n+2) sup_{n≤t≤n+1}|B(1/2+it)|, summing over n≥1 (the first zero has height >1). It is finite by Stirling and the logarithmic bound for ζ(1+it). It suffices to take ε=min(h/2,|a|/(4+4S)). No individual ordinates are used.

**The two implications.** Under RH, moving the inversion to Re s=−1/4 gives F(T)=a+εΣ mρ B(ρ)exp(i Imρ T)+O(exp(−T/4)), summing over distinct zeros. On that line the horizontal distance to the zeros is 1/4 and the local expansion of ζ'/ζ gives polynomial growth. In bands of unit height one can choose horizontals separated from the ordinates by ≫1/log(t+2) by the same count. The gamma factor damps exponentially in the whole strip, justifying the shift and the absolute convergence. The oscillating sum multiplied by ε has modulus ≤|a|/4. Conversely, if F has an eventual ceiling C, apply Landau's theorem to the unilateral transform of C−F from that time on. A positive abscissa would require a real singularity there, impossible by the identity. Holomorphy in Re s>0 then excludes all the preceding poles. The symmetry of ξ gives RH and the bridge of paper 47 gives the sign.

**Antecedents and limit.** The logarithmic derivative and Landau already appear in R162_803 and G2_B7_R3. The difference with respect to 149 is the realization through a fixed density on U without a list of ordinates, recovering each multiplicity without estimating inverses of derivatives at zeros. The term q alone cancels all spectral poles. Therefore an arithmetic argument for the even density alone loses precisely the necessary information. Direct control of the term ∫yp(y)U(T+y)dy remains the obligation. No new window is certified.
