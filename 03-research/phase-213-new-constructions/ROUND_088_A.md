# Two orientations: exact threshold for switching on the reflected exponential

Fix a≥1/2 and δ≥0. On [−T,T] form the two real tests
     
    g_±(t)=exp(at) ± exp(−2δT)exp(−at).

For EACH sign separately, the eventual non-negativity of W_T(g_±) is equivalent to |Re ρ−1/2|≤δ for every nontrivial zero. In particular, at δ=0, even if a=10000, a single cosh(at) in all large windows already detects the global sign; so does a single sinh(at). The two individually positive directions of 083 cannot be joined for free. For δ>0 in the declared strip there is eventual strict positivity. Equality at the boundary is included even if there are zeros on it.

**Computation.** Let z=ρ−1/2, b=Re z, γ=Im z. Write D_T=e^(−2aT)W_T(exp(at)) and C_T=e^(−2aT)W_T(exp(at),exp(−at)), with the cutoffs implicit. By 083 and dominated convergence (each |b|<1/2), D_T→D=Σ d_z>0, where d_z=Re[1/(a²−z²)]>0. For the crossing one multiplies the integral of exp((a+z)t) by itself. Thus
    
    C_T=J(T)+O_a(exp(−2aT)+exp(−(4a−1)T)),
    J(T)=Σ_z exp(2zT)/(a+z)².

The first error comes from the constant term −2 of the square of 2sinh((a+z)T); the second, from the decreasing exponential. The series converge absolutely for each T and are real by conjugation. By reflection the two diagonals are equal. The energy of g_± multiplied by exp(−2aT) is (1+exp(−4δT))D_T ±2exp(−2δT)C_T.

**If the strip holds.** For δ=0 the result is Weil's direction under RH. For δ>0 only zeros with b=δ can survive in exp(−2δT)J(T), with remainder o(1) by domination. For those zeros
    
    |a+z|^(−2)/d_z = [(a−b)²+γ²]/[a²−b²+γ²] ≤ 1.

Here b≤1/2≤a suffices; if δ≥1/2 the boundary sum is empty. By symmetry d_z=d_{−conj z}, and the first critical pair lies off both boundary lines. Hence 2Σ_{b=δ}|a+z|^(−2)≤D−2/(a²+γ₁²). For both signs the lower limit of the scaled energy is at least 2/(a²+γ₁²)>0. If there are no zeros on the positive boundary, that energy converges exactly to D.

**If the strip fails.** If either of the two energies were eventually non-negative, the above identity would give a one-sided ceiling ≪_a exp(2δT) for one of J or −J. Its Laplace transform, initially for Re s>1, is Σ_z (a+z)^(−2)/(s−2z). It continues meromorphically by normal convergence away from the poles and is regular on the real axis; each pole at 2z carries a nonzero residue, also with multiplicities. Landau applied to the majorant minus the function on a tail excludes poles in Re s>2δ. Contradiction, without requiring the supremal real part to be attained.

**Rate on the explicit family.** Let Δ=sup Re z and take δ=0. For each of the two parities, let M_± be the negative part of the quotient W_T(g_±)/||g_±||², taken in absolute value. One has limsup log(1+M_±)/(2T)=Δ. Indeed the squared norm is comparable to exp(2aT) as T grows; the series gives the upper side. If Δ>0, any exponential bound with exponent η<Δ for that negative part, with 0≤η, would impose a one-sided ceiling O(exp(2ηT)) for ±J (according to parity), a contradiction by the same argument. For Δ=0, RH gives M_±=0. No lower rate for all T is deduced, nor is the minimum over the WHOLE space bounded from above. In particular Q4 of phase 159 is not resolved for that minimum.

**Cross-check.** 083 controls the diagonals separately. Phase 159 G2_B5_R4/R5 already connects negativity rates of windows with zero strips; 038 and 074 already use one-sided pole detection. Here the explicit crossing allows obtaining the rate in both directions on each of two prescribed families and paying the critical case of the damped coupling with the diagonals. There is no new zero-free strip. Any extension of 084 to opposite orientations with free coefficients, even with just two terms in all large windows, would have to resolve the global sign.
