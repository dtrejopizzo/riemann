# The cosh with rate 1/2 detects an attained extreme on every grid

Assume that Δ=sup Re(ρ−1/2)>0 is attained. Fix any h>0. For g=2cosh(t/2) cut to [−T,T] there are c>0 and an integer L(h) such that in each block of L(h) consecutive sufficiently large integers there appears n with W(g)/‖g‖²≤−c exp(2Δnh) at T=nh. Rational independence of the ordinates is not required. In particular, if that single cosh were eventually non-negative on a single grid, a failure of the sign would require a non-attained supremum.

In the notation of 088 take a=1/2. By domination using Σ|a+z|⁻²<∞,
    
    exp(−2ΔT)J(T)=P(T)+o(1),   P(T)=Σ_{Re z=Δ} exp(2iγT)/(a+z)².

The remainder tends to zero even without separation of the other zeros from Δ. P(0)<0: by conjugation it is real and each term has real part ((a+Δ)²−γ²)/|a+z|⁴<0, since |γ|>14 and a+Δ≤1. Let d=−P(0)>0. Truncate the boundary symmetrically with a tail of moduli <d/8. When all the finitely many phases are close enough to one, the difference of the truncated polynomial from its initial value is <d/4, and P(T)<−d/2. At the multiples of h the phases form the orbit of a rotation on a finite torus. The closure of the whole orbit is a compact group; the translates by integer powers of the chosen neighborhood of the identity cover that group by density. A finite subcover gives returns to the neighborhood with bounded gaps in the index n, also for finite orbits. By 088 the energy multiplied by exp(−(2a+2Δ)T) differs from 2P(T) by o(1), and the squared norm divided by exp(2aT) tends to 1/a. This gives the claim.

**Cross-check.** Phase 159 G2_B5_R5 uses recurrence of the extreme term in continuous time and monotonicity of the minimum as the test varies. Here the test is prescribed, the grid is arbitrary and the negative value sits at the identity of the phase group; thus resonances are avoided without shifting the origin. The odd model of 089 does not contradict this even conclusion. Without an attained extreme the term P disappears, and detection on a single grid remains open.
