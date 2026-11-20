# Effective cancellation among the multiplicity classes near 4z

**Status: PROVED, with independent review of the uniform angular offset, the terminal weight and the modular range.**

At the cut of 395 let C(Y) be the signed sum and A(Y) the absolute mass, optionally including a weight λ∈[0,1] on the last prime in both sums. For fixed κ, Y=(4+κ/b)z, there exist c>0 and x₀ such that

    |C(Y)| ≤ A(Y) exp(−c L/b³)   (x≥x₀).

RH is not used. More generally, for all 2≤m≤√L/b^(5/2) and each residue j modulo m, the mass with ω(n)≡j mod m is (A(Y)/m)(1+O(exp(−c b²))), uniformly. The result estimates the relative imbalance; by itself it does not bound its exponent by 1/2.

**Characters.** Use the positive saddle β of 395 without the terminal weight; omitting or weighting that factor only changes the positive product by a factor 1+O(1/L). In the Gaussian sum A the change is also relatively o(1): the local proof of 395 on the same vertical multiplies the integrand by (1+λp^(−s))/(1+p^(−s))=1+O(1/L) uniformly; the integral of the modulus on that vertical is O(exp(H(β))/√(Lb)) by the same three ranges of 395. Thus the equivalent of A is preserved.

For the character exp(iθω), 0<|θ|≤π, the logarithmic deficit of modulus relative to the positive product dominates

    c Σ_{2z<p≤3z} p^(−β) [1−cos(θ−t log p)].

This is the identity of the square of the modulus of 395, on the vertical s=β+it; outside that block the loss is also non-negative. If |t|≤|θ|/(3b), for large x the angular distance to 2πℤ is ≥c|θ| on the whole block (also for |θ|=π); the loss is ≫(L/b)θ². For |θ|/(3b)≤|t|≤2√L, in the fixed band of log(p/z) an absolute proportion of length has angular distance ≥c min(|t|,1), independently of the initial offset. It is obtained by cutting the phase interval into pieces of angular length comparable to one for large |t|, and removing a neighborhood of the nearest multiple of 2π for small |t|. Subintervals of logarithmic length ≫min(1,1/|t|) can be retained; the short PNT applied as in 395 transfers them to prime mass ≫L/b. The result is loss ≫(L/b)min(t²,1)≫Lθ²/b³. For |t|>2√L the Gaussian gives exp(−2L) without using the primes.

Integrating and dividing by the positive equivalent, the quotient of the character relative to A is ≤O(√(Lb) exp(−c Lθ²/b³)). For parity θ=π, the prefactor is absorbed. For the modular table, invert by discrete Fourier: the sum of the m−1 errors relative to the main term is bounded by O(m√(Lb)exp(−c L/(m²b³))). In the announced range the negative exponent dominates b² with fixed constant, and log(m√(Lb))=O(b). This proves the uniformity.

**Review record.** In the second frequency range, the interval of log(p/z) has fixed length log(3/2); for |t|≤1 an angular neighborhood of size c|t| is removed, not one of fixed size. This leaves a positive proportion of length even with arbitrary offset θ−tb and allows the floor1−cos≥ct² on a subinterval of fixed logarithmic length. For |t|≥1 pieces of length≍1/|t| are used; the shortest have length in p≍z^(3/4), within the short-PNT range of395. The prime count is applied in a region where the angular floor already holds pointwise, so it does not need a PNT error smaller thanθ² whenθ is small. The condition |t|≥|θ|/(3b) then gives min(t²,1)≥cθ²/b² uniformly for|θ|≤π. In the first range, even forθ=π the rotation of size≤(1+o(1))|θ|/3 keeps distance≥c|θ| from2πℤ.

The terminal prime is outside[2z,3z] for large x; weighting it does not alter the factors used for the loss. For the others, including the terminal one withλ∈[0,1], |1+λa exp(iφ)|≤1+λa≤1+a, so the additional loss is not negative. The equivalent of the weighted mass differs from the unweighted one by O(1/L) relatively by the control of the absolute integral of395. Finally, m²≤L/b^5 implies L/(m²b³)≥b², while log(m sqrt(Lb))=O(b). Reducing the constant c therefore absorbs all prefactors and the sum of m−1 harmonics, uniformly in m,j andλ. Neither a sign rate forC nor a power saving in x is claimed.

The loss obtained is of order L/b³ in the logarithm for parity, while the surplus available in 395, at κ strictly above the threshold, is of order L/b². The precise magnitude and orientation of the signed residue remain open.
