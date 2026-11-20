# Positive inversion by dilations for the odd discrepancy of the first row

Let C=C₀ of 299 and let A be the same partial sum restricted to odd integers. Then A is an explicit discrepancy between the classes 1 and 2 modulo 3: each odd cube-free integer with all its primes congruent to 2 modulo 3 is given positive weight 4^ω(n), and the weight of the second class is subtracted from that of the first. The integer 1 is included. Indeed, at each prime the sign is (−1)^e.

For all x≥1 one has the absolutely convergent identities

    A(x) = Σ_(j≥2) (j−1)2^(−j) C(2^j x),
    2A(x/2)−A(x) = Σ_(j≥1) 2^(−j) C(2^j x).

In particular, a ceiling C(v)≤K v^σ for v≥1 and 1/2<σ<1 implies simultaneously A(x)≤K x^σ q²/(1−q)² and 2A(x/2)−A(x)≤K x^σ q/(1−q), with q=2^(σ−1). No lower bound for C is needed. In the direct sense, the sought estimate for C is exactly equivalent to an upper bound for the second difference A(x)−4A(x/2)+4A(x/4).

**Boundary condition that allows inversion.** Separating the local factor at 2 gives C(x)=A(x)−4A(x/2)+4A(x/4). It is essential that A(v)≪_R v/log^R(2v) for each fixed R. To see this, repeat the product of 294 at t=0 for the odd series: at p=2 omit the factor (1−2z)² from the start, with z=2^(−s). The correcting factor there becomes (1+z)²/(1−z)², whose local series converges absolutely in Re s>0. At the other primes the same first-degree cancellation as in 294 holds. The hyperbola method with two factors μ and two ordinary factors χ therefore gives the claimed saving; the argument also holds for C. In particular one is not dividing an estimate by a factor that vanishes on Re s=1.

Put a_j=2^(−j)A(2^j x) and d_j=2^(−j)C(2^j x). Then d_j=a_j−2a_(j−1)+a_(j−2). For fixed x, a_j and d_j are O_(x,R)((1+j)^(−R)) for j≥1. Summing the second difference towards infinity once or twice gives both formulas without boundary terms. The positive weights allow transferring a one-sided ceiling. In particular, an odd discrepancy that is too positive at one scale, or too steep a drop of its normalized value between two scales, would force C to violate the ceiling at some dilation.

**Scope.** Removing 2 allows the study of a discrepancy with positive weights on odd integers. In the open half-plane 1/2<Re s<1 the multiplier (1−2^(1−s))² never vanishes: this inversion exactly preserves the multiplicity obstruction of the first row identified in 299. The identities transfer a one-sided control and specify two possible falsifiers; they do not yet prove that control.
