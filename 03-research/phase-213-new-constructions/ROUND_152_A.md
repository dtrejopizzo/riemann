# Drift of the squares in the odd correction

In 150–151 let K(t) be the bilateral inverse of B(1/2+s), with initial contour Re s>1/2. The contribution to E of the powers p² has a linear drift with coefficient −a/2>0. In particular removing all exponents greater than one as a bounded error would change the criterion. For the compact weight of 107 the squares contributed a constant after normalizing. Here the kernel tends to a constant on a half-line.

**Arithmetic identity.** Define
    P(T)=Σ_p (log p)/√p K(T−log p).
The global sign is equivalent to the existence of C such that, eventually,

    P(T) ≥ −aT/2 − C.

To see this write ξ=Jζ, with J(z)=z(z−1)π^(−z/2)Γ(z/2)/2. On Re z>1, split Bξ'/ξ into BJ'/J and Bζ'/ζ. The absolutely convergent Dirichlet series of the second factor and inversion give exactly
    E(T)=A(T)−Σ_{p,k≥1} (log p)p^(−k/2) K(T−k log p),
where A is the inverse of BJ'/J. One can invert term by term by the gamma decay. The pole of J'/J at z=1 is cancelled by B(1)=0. Moving to Re z=1/4 only z=1/2 is crossed, giving A(T)=a(J'/J)(1/2)+O(exp(−T/4)). For K moving to Re z=−1/2 gives K(t)=a+O(exp(−t/2)) for t≥0, including the residue at z=0. To the left it suffices to move to Re s=2 for K(t)=O(exp(2t)). In particular K is bounded and continuous. All of this is unconditional.

**Powers.** The sum over k≥3 converges to the constant value aΣ_{p,k≥3}(log p)p^(−k/2) by dominated convergence. For k=2 introduce r(t)=K(t)−a·1_{t≥0}. With Y=exp(T/2) the sum of squares before its minus sign is
    a Σ_{p≤Y}(log p)/p + Σ_p (log p)/p r(2 log(Y/p)).
The first sum equals a log Y+O(1) by Mertens' theorem. The second is uniformly bounded: by Chebyshev, each band e^j≤p<e^(j+1) contributes mass Σ(log p)/p=O(1), and |r| decays exponentially on both sides. Therefore E(T)=−P(T)−aT/2+O(1). The even average of 150 is bounded for T≥0 by 151 and ε is a fixed positive number, which proves the equivalence. The slope in the lower bound for P is positive because a<0.

**Why the continuous density approximation fails.** Replacing (log p) by the measure du on (0,∞) in P produces exp(T/2)∫exp(−v/2)K(v)dv=exp(T/2)B(1)=0. Using the interval [2,∞) only changes O(1) by boundedness of K. Therefore that substitution loses precisely a term that must grow at least linearly in T. The need to capture this excess in the simple primes is an obstruction to the density argument, not a proof that the lower bound holds.
