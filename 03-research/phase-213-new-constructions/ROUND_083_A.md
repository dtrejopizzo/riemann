# Positivity of the truncated exponential and width of the zero strip

For a>0 and T>0 set F_{a,T}(t)=exp(at)1_{[−T,T]}(t). For the full form W of P47 one has the equivalence

    W_T(F_{a,T})≥0 for all T large enough
    ⇔ |Re ρ−1/2|≤a for each nontrivial zero ρ.

Under the condition on the right there is, for EVERY T>0, the explicit bound

    W_T(F_{±a,T})/||F_{±a,T}||² ≥ [1.9·2a/(a²+γ₁²)] tanh(aT),

where γ₁ is the first positive ordinate. Hence it is unconditional for each a≥1/2, in any window. In particular the two exponential diagonals of the polar plane of 082 are positive, with bound >0.008 tanh(T/2) for a=1/2. Positivity on their span is not claimed.

**Identity.** Write z=ρ−1/2 and γ=Im z. Weil's formula evaluated at F gives
    
    W_T(F_{a,T})=2 Σ_ρ [cosh(2aT)−cosh(2zT)]/(a²−z²).

It is the product of the integrals of exp((a±z)t). The vector is in the form domain: its transform decays as O_T(1/(1+|ξ|)). It can be smoothed by convolution, with supports in a common compact set, convergence in logarithmic norm and uniformly bounded variation. The formula passes to the limit by domination O_{T,a}(1/(1+γ²)) in the sum over zeros. The autocorrelation does not depend on how values at the edges are defined. The squared norm is sinh(2aT)/a.

**Simultaneous control of all negative contributions.** Let b=Re z and assume |b|≤a. For d=Re(1/(a²−z²)), r=|Im(1/(a²−z²))|/d one has
    
    d>0,   d≤1/(a²+γ²−b²),   r=|2bγ|/(a²+γ²−b²)≤1/|γ|,

also using |b|≤1/2. If H=cosh(2aT), the real part of the summand, before the factor 2, is ≥d[H−√(H²+r²(H²−1))]≥−d r²(H−1). For the first inequality one optimizes the phase 2γT and uses |b|≤a; for the second it suffices to square H+r²(H−1). For the first pair of zeros on the line, 14<γ₁<15, the contribution is instead ≥2(H−1)/(a²+γ₁²).

To make the total cost explicit recall Hadamard's classical identity Σ Re(1/[ρ(1−ρ)])=2+γ_E−log(4π)<0.05. It comes from the logarithmic derivative of ξ at 0 and 1 and its functional equation. All |γ|≥γ₁>14 by the verified count cited in P47. For a=1/2, d=[(γ²+β(1−β))(1+r²)]^(−1), β=Re ρ, so d≥0.99/γ² and Σ1/γ²<0.051. For the general a considered, (a²+γ₁²)d≤(a²+γ₁²)/(a²+γ₁²−1/4)<1.002. Hence the total expense, even including the first pair in the loss majorant, is <0.052(H−1)/(a²+γ₁²). The first pair pays for it and the announced bound remains after normalizing. The verified low-height locations and the classical total mass are used, without presupposing that the other zeros lie on the critical line.

**Necessity of the strip.** Take the Laplace transform in T of the unnormalized identity, initially in Re s>max(1,2a). The transform is
    
    2 Σ_ρ [s/(s²−4a²)−s/(s²−4z²)]/(a²−z²).

On compact sets without poles the sum converges normally; the tails of the first term are O(Σγ⁻²) and those of the second O(Σγ⁻⁴). It is regular on the real axis s>2a. Each z with Re z>a gives an effective pole at 2z: the only possible terms are z and −z, with equal denominator and residues of the same algebraic sign, never zero. If W_T(F_{a,T}) were non-negative on a tail, Landau for its Laplace transform would prevent an abscissa of convergence >2a, since it would be a real singularity. The resulting holomorphy excludes that pole. By symmetry the full strip is obtained. The same proof works if only an eventual minorant −C exp(2aT) is required.

**Scope and antecedents.** The scalar criteria of Bombieri–Suzuki and the quartet formulas of P47 already appear in the index; the Landau argument is inherited. Here the constructive estimate pays the negative part of the sum over all zeros using a single verified pair, uniformly in T for the unmodulated exponential. To close the sign through this family it would suffice to establish eventual positivity for a sequence a↓0. The proof given for a≥1/2 does not cross that frontier: if |b|>a, the hyperbolic cosine of the zero can grow faster than H. No new strip nor larger complete window has been certified.
