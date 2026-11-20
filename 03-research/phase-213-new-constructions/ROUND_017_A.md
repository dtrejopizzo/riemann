# Absorption of the crossing by the two localized energies

Antecedents 010-A, 012-A and 016-A. We keep separately the growing energies of both remainders. The reconstruction from the whole tail of 016-A is replaced here by direct observation of H at the first head jump. The prior cross-check concerns the local scope for F_k, without excluding other mechanisms.

For some fixed θ>0 and all k sufficiently large, any nonzero mixture of translations of F_k in an interval of length r=θ/√k has strictly positive energy. We admit finite complex measures. We use Y=cF+g+D, c, H, and b=U⁻¹D as in 016-A, with the measure supported on [0,r] by translation. The mass identities of 016-A hold for any r (their proof by Fubini does not use r/w integer). On the tube [0,r] of the first jump, separated from the others for large k, g(t)=exp(t/2)(log(3/2)−w)H(t) almost everywhere. Hence ||H||₂≤C||g||₂. Here and below the constants are independent of θ for 0<θ≤1 and k sufficiently large depending on θ.

**Local floor.** On a window of fixed length the norm of the comb is bounded. For any vector Z of the domain supported on a set of total length ≤3r, the proportion of its Fourier mass in |τ|≤r^(−1/2) is ≤3√r/π by Cauchy–Schwarz and Plancherel. Outside that band m(τ)≥(1/2)log(1/r)−O(1) by P47 lem:mbounds. In the band m has a fixed lower bound. It follows that a(Z)≥κ log k ||Z||² for large k, taking for instance κ=1/8 since r≤1/√k. This holds for g on the fixed head window and for D after translating it to a fixed window: their supports have length ≤3r and r+w≤2r respectively. It is important to compress the comb to those separate windows only for the two self-energies.

**Mixed estimate.** In each tube of g, only O(1+kr) integers of size comparable to k contact D. The norm of each translation is one and its weight is O(log k/√k). The arithmetic crossing between both remainders has modulus ≤C(θ+k^(−1/2))log k ||g|| ||D||. We choose θ>0 so that this term is absorbed using at most half of the two previous floors for large k.

The diagonal of F on the head is q(w)>0.15 by BUILD084. The crossing of cF with g costs O(|c| ||g||) by the uniform L² representative of 016. For the arithmetic crossing of cF with D, S_k(k)=o(1) by PNT; on the physical support of b the oscillation of S_k is O((1+kr)log k/k) by the count at the band endpoints of 016. The support has length O(1+kr). By the mass identity,
   
    |∫b| ≤ C(|c|+√r||g||),    ||b||₁ ≤ C√(1+kr)||D||.

The constant part of the crossing is bounded by o(1)|c| (|c|+√r||g||). The oscillating part costs O((1+kr)^(3/2)log k/k)|c| ||D||=o(1)|c| ||D||. The archimedean crossing of the whole head with the tail costs O(√(1+kr)/k)(|c|+||g||)||D|| by the separated kernel of 014 and the bounded length of the physical head support.

Finally Young's inequality absorbs O(|c| ||g||) spending less than 0.05|c|² and a fixed multiple of ||g||², which fits in the growing floor. The remaining errors are o(1)(|c|²+||g||²+||D||²). We obtain, for some constant c₀>0,

    a(Y) ≥ c₀ [ |c|² + log k (||g||²+||D||²) ].

In particular any nonzero Y has strictly positive energy. The radius still decreases. For fixed r the crude count produces a cost of higher order than the available local floor, and the additional arithmetic compensation remains open. Status PROVED after independent mathematical audit.
