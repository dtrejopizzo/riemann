# How the cut amplifies the forced oscillation of the triangular window

For a cut z kept fixed as x grows, let Q_w(x;z) be the observable of 360. Fix a zero ρ=1/2+iγ of multiplicity m≥1, γ>0. For both choices of sign it holds unconditionally that

    limsup_{x→∞} (±Q_w(x;z))/(√x (log x)^m)
        ≥ m |W(ρ)| |E_z(ρ)| / |ζ^(m)(ρ)|,
    E_z(s)=∏_{p≤z}(1−p^(−s))^(−1).

The factor of the cut can be exponentially large in √z/log z: the upper and lower limits of log|E_z(ρ)| divided by √z/log z, as z→∞, are respectively 1/|1−ρ| and −1/|1−ρ|. What changes demonstrably is the contribution of that zero to the oscillation floor; the total oscillation is not bounded above.

**Orders of the poles.** For Re s>1 the transform of the observable is

    W(s) E_z(s) / ζ(s) · [−ζ'(s)/ζ(s) − Σ_{k≥2,p}(log p)p^(−ks)
                                      − Σ_{p≤z}(log p)p^(−s)].

In the term of higher powers, adding and subtracting −ζ'(2s)/ζ(2s) leaves a function holomorphic in Re s>1/3 by absolute convergence of the remaining powers. The transform is regular on the real axis in σ>1/2, including 1 by cancellation with the zero of 1/ζ. At 1/2 it has at most a simple pole. At ρ, ζ(2ρ) is finite and nonzero on the line 1 and W(ρ)≠0. The pole has order m+1 with leading coefficient −m·m! W(ρ)E_z(ρ)/ζ^(m)(ρ).

**Landau comparison.** If one of the two limsups were less than the indicated floor, choose a positive constant C strictly between both (or between zero and the floor if the limsup is not positive). The function C√x(log x)^m∓Q_w(x;z) is eventually nonnegative. Its Mellin transform converges absolutely in σ>1/2 by Landau's principle, since its continuation has no real singularities in that interval. Discarding an initial stretch only changes an entire function. For the nonnegative tail, the modulus of its transform at σ+iγ is at most its value at σ. Multiply by (σ−1/2)^(m+1) and let σ↓1/2: the real side tends to C m!, since the real pole of the observable has order ≤1. On the twisted side the modulus of the leading coefficient at ρ survives, contradiction. The argument does not presuppose RH.

**Amplification with the cut.** By expanding the logarithm, log|E_z(ρ)|=Re Σ_{p≤z}p^(−ρ)+O(log log(3z)), summing the terms of order ≥2 in modulus. By the prime number theorem and partial summation, for fixed ρ the sum is z^(1−ρ)/((1−ρ)log z)+o(√z/log z). Indeed integrating t^(−ρ)/log t gives that main term and replacing the prime count by li(t) costs o(√z/log z). The argument of z^(−iγ)/(1−ρ) runs through both extreme phases indefinitely. This proves the limits.

**Decision.** The target with x^ε of 360 is compatible with this floor. A ceiling C√x log x with absolute C for all fixed cuts would be false: if m>1 it already fails at one cut, and if m=1 uniform constants fail by the amplification. The limits are first in x, then in z; they do not give by substitution a sequence with z≈log²x. Antecedents of the oscillation principle in 058 and 126. The explicit dependence on the Euler factor belongs to the doubly sieved observable of 360.
