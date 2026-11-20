# A maximum over prefixed samples measures the exponent of the zeros

For the canonical profile T of 276 and its cutoffs Y,U, one can fix O(log²(2N) log log(3N)) integer points of the band, without consulting the profile. If M_x is the maximum of |T| at those points, then

    lim_(x→∞) log(1+M_x)/log x = Θ/2.

The points may be required to be prime. Thus, for the global sign it would suffice to have a sequence x_j→∞ in which the WHOLE prefixed set has |T|≤x_j^(1/4+o(1)). The scale 1/4 is for individual values; 3/4 was for the sum of 279. In this proof there is no need to measure the integral or the other prime samples.

**Construction of the points.** Put k=⌈K log(2N)⌉ with a sufficiently large fixed constant. Divide [Y,U] into intervals with endpoints in geometric progression of ratio (U/Y)^(1/J), J=⌈log(U/Y)/log(1+1/(Ck))⌉, with C large and fixed. Their lengths h are comparable to a/(Ck), where a is the left endpoint. In each interval use the k interior Chebyshev nodes of the first kind, translated and rescaled. Round to the nearest integer. In the prime version one can take the smallest prime to the right of each node at distance ≤U^(7/10), by 238. The minimal distances between nodes and to the edges are ≫h/k²≫U^(7/10), so the rounded samples also stay inside and are distinct for large N. There are Jk points, of the announced order.

**Control between samples.** The pointwise bound of 278 gives |T^(k)(y)|≤x log³(2N) C₀^(k+1)(k!)²/y^(k+1). The Taylor polynomial of order k−1 at a approximates T uniformly with error ≤x log³(2N)(C₀ h/a)^k k! C₀/a. By the choice of C and then K the error is O(N^(−3)). For any polynomial P of degree <k one has ||P||∞≤2k max_i |P(z_i)| with the exact nodes z_i: expanding P in cosines of the Chebyshev angle, discrete orthogonality bounds each coefficient by twice the sampled maximum. Markov's inequality gives ||P'||∞≤2k²||P||∞/h. Thus replacing each z_i by the chosen integer or prime adds to the right-hand side at most (4k³U^(7/10)/h)||P||∞, absorbable uniformly since h≫U/log³(2N). Applied to the Taylor polynomial on each cell this gives

    M_x ≤ sup_band |T| ≤ 4k M_x + O(k N^(−3)).

**Passage to the exponent.** By 279 and Chebyshev, sup_band |T|≥A(x)/O(U)=x^(Θ/2+o(1)) as a lower bound on the exponent. The upper argument of 279 already gives sup_band |T|≪_θ(x/U)^θ log⁶(2N) for Θ<θ<1. If Θ=1 one uses the zeroth-order estimate of 278, |T(y)|≪x log³(2N)/Y. The sampling factor O(k) disappears in the exponent. This result concerns the smooth profile fixed in advance. Altering a few rows to annihilate the samples would change the profile whose regularity supports the interpolation.

**Antecedent and limit.** 047 reduced a signed quadrature to a few outer indices, with an integral and inner sums pending. Here the exponent is recovered via a sign-free maximum at explicit points and without an additional integral. Each point still contains an arithmetic sum; counting samples does not by itself provide the quarter-power bound.
