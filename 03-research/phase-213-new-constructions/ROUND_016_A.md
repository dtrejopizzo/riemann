# Signed translations over a growing number of cell widths

The antecedent 015-A recovers the cumulative function on two strips. When the cell width is exceeded the strips overlap and the physical support of the tail grows. The operation here combines reconstruction from the right endpoint and extraction of the signed mass before estimating the oscillation of the comb. The cross-check distinguished this extraction from the quadrature relative to total variation in 013 and from the bound by the L¹ norm of the whole tail in 015.

**Statement.** There exists γ>0 such that, for all k sufficiently large, the translations of F_k in any interval of length γ/√(k log k) span a space on which the energy is strictly positive for every nonzero vector. Finite complex measures and any number of terms are admitted. The normalization of 015 is used.

**Reconstruction.** Put w=log(1+1/k), M a positive integer and r=Mw≤1. Translate the interval to [0,r]. For the measure ν(ds)=exp(−s/2)μ(ds) extend its cumulative function L(u) by zero to the left and by its mass c to the right. In the physical variable the tail b satisfies b(k exp u)=d(L(u)−L(u−w)) almost everywhere. Write D=Ub. For 0<u<r telescope from u up to u+Mw≥r. For H=L−c on (0,r), Minkowski and dy≥k du on the support imply

    ||H||₂ ≤ M ||D||₂/(d√k).

The logarithmic head is written cF+g, where F is the head of F_k before mixing. The remainder g lies in three tubes of length r with bounded jump coefficients, so ||g||≤CM||D||/√k. The physical L¹ norm of b is ≤C√M||D||, since the support has length k(exp(r+w)−1)≤CM for r≤1. Its signed integral satisfies exactly

    ∫b(y)dy=d∫exp(s)dν(s)=d(c−∫₀ʳ exp(s) H(s)ds).

The first equality integrates cells of length exp(s), the second is Fubini or integration by parts with the endpoints included. In particular the error in replacing the mass by dc is ≤C M^(3/2)||D||/k.

**Self-energies.** We take M≤√(k/log k), so that r→0. On a fixed window a(F)=q(w)>0.15 for large k, the representative of a(F,·) is bounded in L² and a(g)≥−C||g||² as in 015. Thus the head energy is ≥0.15|c|²−o(1)(|c|²+||D||²). On a fixed translated window the tail support has length r+w→0. By 010, a(D)≥||D||².

**Crossings.** Between g and D each tube admits O(M) contacts with n comparable to k and weights O(log k/√k). The absolute value of this whole arithmetic crossing is ≤ C₁ M²(log k)/k ||D||², with C₁ independent of k,M. For cF and D use S_k(y) of 015. By PNT S_k(k)=o(1). For k≤y≤k exp(r+w), each endpoint y/i of the two summation bands changes by O(M). Since each summand is O(log k/k), one has |S_k(y)−S_k(k)|≤CM log k/k. The constant term of the mixed integral pays only the signed mass computed above. The oscillation pays ||b||₁. Altogether the crossing is bounded by

    2|c| [ |S_k(k)| (d|c|+CM^(3/2)||D||/k)
                 + CM^(3/2)(log k)||D||/k ].

It is o(1)(|c|²+||D||²) uniformly in the chosen range. For the archimedean crossing, the kernel between head and tail is O(1/k) by 014. The length of the physical head support is bounded and its L¹ norm is O(|c|+||g||). The preceding estimate of ||b||₁ again gives a relative error o(1). All domains and passages to measures are those of 015, for fixed k.

Choose M=floor(θ√(k/log k)) with 0<θ≤1 a constant so small that C₁θ²≤1/4. For large k we get a(Y)≥0.07|c|²+||D||²/2. If c and D vanish, the reconstruction forces g=0 and hence Y=0. Finally Mw√(k log k)→θ, so γ=θ/2 suffices. The radius tends to zero, but its ratio to the radius of 015 tends to infinity. Paying the crossings for fixed separations and for the global carrier remains pending. PROVED after independent mathematical audit.
