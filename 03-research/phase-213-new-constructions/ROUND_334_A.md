# Separating by greatest common divisor preserves the rate that detects the zeros

Let B_q be the signed energy of 325 restricted to (n,d)=q, **including the diagonal** when n=d=q. Put V_m=Σ_q |B_q|. Denote by Θ the supremum of the abscissae of the nontrivial zeros. If h→0 and log(1/h)=o(m), then

    limsup V_m^(1/(2m)) = 1/(3/2−Θ).

Moreover, at h=exp(−am), RH implies limsup V_m^(1/(2m))≤1 for each fixed a>0. The condition for all a=1/j implies RH. Thus the ceiling can be demanded even after taking moduli by exact class. In the ceiling-one equivalence the diagonal can also be excluded: exchanging either of the two variations for the other costs at most Δ_m=O(m^(−1/2)).

**Proof.** For weights |b_q|≤1 write b_(n,d)=Σ_{g|n,d}c_g with |c_g|≤τ(g) as in 333. The energy over all multiples of g is a nonnegative Gram integral J_g. Hence V_m≤Σ_g τ(g)J_g. The exchanges at fixed m are justified by absolute convergence: Σ_{g|n,d}τ(g)≤τ(n)^2 and the weights l_m decay like n^(−3/2) times a polynomial in log n.

For each squarefree g, the series of the coefficients μ(n)1_{g|n} is

    F_g(s)=μ(g)g^(−s) ζ(s)^(−1) ∏_{p|g}(1−p^(−s))^(−1).

For the other g it vanishes identically. The identity comes first from the half-plane of absolute convergence. Take 0<r<3/2−Θ and σ=3/2−r. On each disc of radius r centered at 3/2+it, the finite product of inverses costs at most C_(σ,ε) g^ε: for every sufficiently large prime (1−p^(−σ))^(−1)≤p^ε, and the remaining primes give a constant. Apply Cauchy as in 325 to the coefficient of order m of F_g, whose squared modulus integrates to J_g against the density W_m. The polynomial bound of 325 for the reciprocal of ζ on those discs gives

    J_g ≪ g^(−2σ+2ε) r^(−2m) h^(−2C_r).

Choose ε<σ−1/2, possible since Θ≥1/2. The sum with weight τ(g) converges by the series of ζ². The fixed power of 1/h has 2m-th root tending to one. Hence the ceiling is 1/r for each allowed r. The floor comes directly from V_m≥E_m and the equality of 325.

At the exponential scale, under RH one uses the bound of 326 with arbitrarily small exponent η>0 in height instead of C_r. For each r<1 one obtains a ceiling r^(−1)exp(aη). Take η→0 and then r→1. The converse of the implication for the sequence 1/j follows again from E_m≤V_m and 326.

**Scope.** 333 proves an unconditional saving in the exact classes. This identity shows that, at the scale of 325, demanding the absolute value per class preserves even the exact rate that detects Θ. It does not yet provide the unconditional ceiling one.
