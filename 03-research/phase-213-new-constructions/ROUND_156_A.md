# Which exact statement a finite number of divisor moments can prove

For integer j≥1, use the positive sum A_j^*(x)=Σ_{m≥1}(log m)^j V(x/m) of 154. Let C_j(x) be the sum of the residues at s=1 and s=1/2 of x^s H(s)(−ζ'/ζ)(s)(−1)^jζ^(j)(s), with H of 155. For fixed M the following are equivalent:

1. For each 1≤j≤M one has A_j^*(x)−C_j(x)≤O_j(√x) eventually.
2. Every nontrivial zero off the critical line has multiplicity strictly greater than M.

In particular the first moment examines exactly the simple zeros. The equivalence identifies the reach of the potential proof; neither of the two conditions is proved for the zeros of ζ in this memo.

**Proof.** By absolute convergence on Re s>1, the integrand defining C_j is that of the Mellin inversion of A_j^*. At a zero ρ of order m the only potentially singular factor to the right of Re s=0 is the logarithmic derivative, apart from the real poles already indicated. For j<m the factor ζ^(j) vanishes and the singularity is removable. For j=m the residue has coefficient (−1)^(j+1)m H(ρ)ζ^(m)(ρ), nonzero if Re ρ>1/2 by the Euler product at 2ρ. Any off-line zero has a partner of the same multiplicity to the right by symmetry. If m≤M, Landau applied to the ceiling of moment j=m, subtracting C_j as in 155, excludes that pole. This proves 1⇒2.

Conversely, under 2 all off-line points are removable for each j≤M. Shifting to Re s=−1/4 avoids the need for separation bounds from multiple zeros inside the strip. On that line the functional equation and Stirling give polynomial growth for the zeta factors and their derivatives of fixed order, and the logarithmic derivative is controlled by reflection to Re s=5/4. The horizontals of 151 avoid all ordinates and allow the shift. At zero the gamma factor introduces at most a simple pole with contribution O_j(1). The critical terms have absolute sum O_j(√x): H decreases exponentially in height up to polynomial factors, ζ^(j) grows polynomially and the count with multiplicity is used. The shifted integral is O_j(x^(−1/4)). One even obtains the two-sided bound for the remainder.

**Decision.** The factorial identity of 155 at d=0 can be differentiated to any finite order, but its first moment introduces the factor (ζ')²/ζ, close to the Selberg identities already recorded in the index. The preceding criterion specifies exactly what an attempt to close via a prescribed number of derivatives would lose. Without independent control of off-line multiplicities, obtaining a few moments does not authorize the global step. The fixed shift of 155 retains detection without that hypothesis. Iterating the table of moments is not proposed.
