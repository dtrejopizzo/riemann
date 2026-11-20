# The centered factorial remainder descends below the root

In the average of 127 set X=M⁴ and D=floor(M^(2+1/16)). There exists a fixed explicit density b(v), equal to one for v larger than a constant, such that for dE=dψ−b(v)dv and

    K(v)=M⁻¹ Σ_{M<m≤2M} Σ_{d≤D} μ(d) floor(m⁴/(dv)),

one has ∫K dE=o(M²) unconditionally. For v>16X/D one has K(v)=W(v) of 128 by finite inversion. Thus the defect of the mean of ψ relative to its main term remains, with error o(√X), in the integral of (W−K)dE over v≤16X/D=O(X^(31/64)). The restriction is on the argument of the atoms: the kernel of the remainder may be large and signed.

**Calibration of the two terms.** Denote by γ Euler's constant, choose t>0 with cosh t=log(2π)/exp(γ)>1 and take a±=exp(γ±t). Define b(v) as the mean of the two indicators of [a±,∞). For y≥3 large enough, with n=floor(y/a),
    
    ∫_a^∞ floor(y/v)dv=y H_n−an
      =y log y + (γ−log a−1)y + a/2 + O_a(1/y).

This follows from H_n=log n+γ+1/(2n)+O(n⁻²); the terms containing {y/a} cancel at constant order. By divisors, ∫floor(y/v)dψ(v)=log(floor(y)!). By Stirling and by the choice of the means of log a and of a, the exact difference has the uniform expansion

    ∫floor(y/v)dE(v)=(1/2−{y})log y+O(1/y).

In particular the constant term independent of the rounding cancels before summing over d. Using only one cut a=exp γ would leave a constant per term.

**Quartic control.** For d≤M one pays O(M log M) in total by the expansion. For M<d≤D control the weighted average of 1/2−{m⁴/d} over the prefixes M<m≤U≤2M. For each h≤floor(M^(1/8)), the reduced denominator of h/d satisfies M^(7/8)≤q≤M^(33/16). On prefixes of length L≥M^(23/25), the classical Weyl inequality for the quartic polynomial bounds its exponential sum by

    Oε(L^(1+ε)(1/q+1/L+q/L⁴)^(1/8)) ≪ε M^(1−7/64+ε).

For shorter prefixes use the length. Erdős–Turán and the discrepancy inequality for the bounded-variation function 1/2−{u} give a sum over any prefix O(M^(23/25)+M^(7/8)+M^(1−7/64+ε)log M). By Abel, introducing log(m⁴/d) costs O(log M). After dividing by M and summing up to D, the result is o(M²), since 2/25>1/16. The Stirling remainders cost O(D²/M⁴)=O(M^(1/8)). |μ(d)|≤1 was used, without cancellation between denominators.

**Resulting arithmetic obligation.** Since ∫W b(v)dv=M⁻¹Σ m⁴−O(1) and the mean contribution of the proper powers is (7/3+o(1))M² by 127, one has

    M⁻¹Σ (θ(m⁴)−m⁴) = ∫_{v≤16X/D}(W−K)dE − (7/3)M² + o(M²).

An upper bound with constant strictly less than 7/3 for the limsup of this integral divided by M² would suffice for the sign. It is unknown. The estimate of 128 on the gross loss in a band does not bound this centered integral.

**Antecedents.** 128 gives the factorial identity on a band, 045 uses divisor inversion and centering, and 049–053 treat arithmetic quadrature errors. The specific step is to cancel simultaneously the linear and constant terms of the factorial cost and pay the Stirling sawtooth through quartic equidistribution, uniformly beyond d=√X. The proof uses Weyl and Erdős–Turán as classical inputs.
