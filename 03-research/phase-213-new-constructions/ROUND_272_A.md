# Unconditional calibrated fit on all moduli above the square-root cutoff

For N=⌊2x⌋, integer 2≤U≤N, there exists a combination of genuine binomial rows, with endpoints ≤N, that reproduces g(m/x) for EVERY integer m>U up to N and has entropic mass exactly xh. Its variation is O((x/U)log²(2N)). In particular, choosing U=⌊√N⌋ simultaneously satisfies all the equations of the large primes of 271 and the initial calibration at cost x^(1/2+o(1)).

**Upper construction.** In the inversion of 261 keep only b_j=S_j−S_(j+1) for j>U, with S_j=Σ_d μ(d)g(dj/x). The discarded coefficients multiply F_j(m)=⌊j/m⌋, identically zero for m>U. For each contributing d (d≤N/U), the variation of the sampling of g(dj/x) is at most Var(g) and its terms with nonzero difference have j≤N/d. By absolute summation one obtains

    Σ_(j>U)|b_j| ≪ x/U,      Σ_(j>U) j|b_j| ≪ x log(2N).

Add F_U with coefficient β=−Σ_(j>U)j b_j/U. The family of symbols becomes balanced, so that the formal cyclic averaging of 261 converts it into genuine rows at cost ≤2(Σ|b_j|+|β|). This conversion preserves the value of any linear evaluation of the symbols.

**Mass adjustment without touching the interpolation.** Evaluating F_j at j log j, the mass H₀ of the balanced combination is Σ_(j>U)j b_j log(j/U). By the second bound its modulus is O(x log²(2N)). Take the row with endpoint U and side ⌊U/2⌋. Its entropy e is ≫U by the binary entropy formula and because ⌊U/2⌋/U∈[1/3,1/2]. All its carries are zero for m>U. Adding the row with coefficient (xh−H₀)/e gives the required calibration within the announced cost.

**Localized residue.** Writing λ=(xh−H₀)/e, for m≤U the exact error (target minus response) is

    r(m)=Σ_(j≤U)b_j⌊j/m⌋ − β⌊U/m⌋ − λ c_(U,⌊U/2⌋)(m).

Here the b_j in the sum are the original ones of 261. Above U the error vanishes even on the proper powers of the small primes. For U=⌊√N⌋, the variation of 271 is concentrated on the chains up to U, with zero at their next level. It remains to prove that this variation is of square-root size, for this choice or for another distribution of the lower coefficients that preserves balance and mass. The magnitude of the initial cost by itself only gives a pointwise bound comparable to the cost at each lower atom; summing such bounds does not close the proof. The calibrated fit on the large moduli is, however, constructed unconditionally.
