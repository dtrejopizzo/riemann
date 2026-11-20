# Verification of the phase transfer in 370

We use b,d,α,ξ,L as in 370. Let P=exp(b−1/d), Z=exp b, ε=exp(−c√b), reducing c if necessary. On [P,Z] the classical PNT gives |θ(y)−y|≪εy. Take h(y)=y^(−α)(1−cos(t log y))/log y. Integration by parts gives

    |∫_(P,Z] h(y) d(θ(y)−y)| ≪ ε M(1+|t|),   M=e^ξ/(db).

Indeed, the boundary terms and y|h(y)| are O(e^ξ/b)=O(dM), and y|h'(y)|≪(1+|t|)y^(−α)/log y. The integral of this last weight without the height factor is comparable to M by the change r=d(b−log y). In the continuous integral the density on [0,1] is ≥cM dr. Hence the loss is at least

    cM [1−|sin(t/(2d))/(t/(2d))|] ≫ M min((t/d)²,1).

On 1/b≤|t|≤2√L this is ≫M/ξ². It suffices to take C large so that ε(1+2√L)ξ²=o(1). The formula handles phases centred at exact multiples of 2π and both ends of the band. The resulting mass M is asymptotic to L/b by the saddle equation.

Check of the remaining local range of 370: on |t|≤1/b, F(α+it)=O(d), F'=O(1), |L_z|=O(L) and |H|=O(1), so that |B_z|=O(Ld). These local bounds allow discarding the Gaussian tail from (log L)/√(Lb) without confronting two undetermined constants multiplying log² L. In the local core |L_z(α+it)−L_z(α)|≪|t|Lb=o(L), and |t|/d=o(1), uniformly. With this the two principal coefficients of 370 are recovered. The horizontal ones were also verified by |E_z(σ+it)|≤E_z(α) and x^(1+1/L−α)exp(−2L)=exp(−(2−o(1))L).

Conclusion of the review: the inequalities of 370 follow in the stated range for an absolute C sufficiently large. The proof is asymptotic and does not provide a first effective x.
