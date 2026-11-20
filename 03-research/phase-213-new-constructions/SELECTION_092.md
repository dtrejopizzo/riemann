# Limit of the prime reading of cosh

The exact crossed comb a=1/2 is already in phase 212-57 C1, with weight (1+1/n)log(x/n). Hence computing the elements of the polar matrix again does not open a route.

A consequence for calibrating possible inequalities: let S(x)=Σ_{p≤x}(log p)log(x/p). Then the global sign is equivalent to S(x)≤x for all sufficiently large x. Indeed, for x=exp(2T) the classical integrated explicit formula for ψ gives

    [x−S(x)]/√x = 2 + J(T) + o(1),

with J from 088 a=1/2. Details: integrate ψ(t)/t between 1 and x (from 2 for the individual terms of the explicit formula). The integrated nontrivial residues are −Σ(x^ρ−2^ρ)/ρ²; it is also obtained directly by Perron with multiplier 1/s². The pole at 1 contributes x, the origin O(log x), and the trivial zeros O(1) for x≥2. The omitted square powers weigh 2∫₁^{√x}θ(t)dt/t=(2+o(1))√x by PNT. Those of order ≥3 cost O(x^(1/3)log³x) by trivial counting.

Under RH, |J|≤Σ|ρ|⁻²=Σ1/[ρ(1−ρ)]=2+γ_E−log(4π)<0.047 by the classical Hadamard identity. Hence S(x) stays below x with margin at least (1.953−o(1))√x. Conversely S(x)≤x gives J(T)≥−O(1), which excludes any pole with Re z>0 by the one-sided argument of 088. This criterion exhibits the bias of the square powers. The bound S(x)≤x remains open; Chebyshev integrations and detection by poles are antecedents, and no priority is claimed for this corollary.
