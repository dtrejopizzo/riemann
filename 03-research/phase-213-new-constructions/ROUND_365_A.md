# A single moving cut and a single inequality for the diffusive Gaussian

In 364 take exactly z=(log x)² and write Q_a(x) for that sum. Put L=log x and b(x)=√x exp(2L/log L), for large x. For each fixed a>0, the following conditions are equivalent:

* No zero ρ with Re ρ>1/2 satisfies Re Φ_a(ρ)>1/2.
* Eventually Q_a(x)≤b(x).
* Eventually −Q_a(x)≤b(x).

If the exclusion fails, there is a fixed B such that, for each sufficiently large X, **both** thresholds are exceeded in [X,e^B X]. Hence a single one of the two inequalities suffices, with the single prescribed cut, for each a of a positive sequence tending to zero. This is an equivalence, not a proof of that inequality for arbitrarily small parameters.

**Explicit ceiling in the absence of violations.** Use the contour of 364 with fixed, sufficiently large T and without zero ordinates on its horizontals. Move the left edge to 1/2+1/L. On that vertical the meromorphic factors of D_z independent of z cost O_a(L^C) for some fixed constant: in a compact set there are only poles of finite order, the distance to those on the critical line is ≥1/L and the others have positive distance for large L. The possible pole at 1 is handled with the regular form E_z[(1/ζ)'−(H+L_z)/ζ] of 361, where H are the higher powers and L_z the prime polynomial. H also has a simple pole at 1/2, already included in that cost. The cut-dependent factors, on all of Re s≥1/2, cost at most a polynomial in L times

    ∏_{p≤L²}(1−p^(−1/2))^(−1) = exp((1+o(1))L/log L)

by partial summation and the prime number theorem. On the left edge x^ReΦ≤O_a(√x); on horizontals and tails use 364. The interior poles to the right of the line are fixed and have Re Φ≤1/2. On circles of radius 1/L around them, the meromorphic factors cost a power of L and x^ReΦ changes by a bounded factor. The residues thus admit the same ceiling. Summing, |Q_a(x)|≤b(x) eventually.

**The residues with the cut actually moving.** If the exclusion fails, choose the fixed contour of 364 so that its error has exponent strictly less than M, the maximum of Re Φ over the crossed poles, with M>1/2. For x=X exp(u), L₀=log X and u in any fixed interval [0,B], let ρ be one of these poles, β=Re ρ>1/2 and m its multiplicity. On the circle s=ρ+w/L₀, |w|=1, one has uniformly

    E_z(s)=(1+o(1))E_(L₀²)(ρ).

Indeed, the movement of the cut adds O_B(L₀) integers of size comparable to L₀², which costs O_B(L₀^(1−2β)) in the logarithm. The movement of s costs O(L₀^(2−2β)log L₀/L₀)=o(1) using the derivative of the logarithm of the product (summing over integers suffices). The polynomial of removed simple primes costs O(L₀^(2−2β)log L₀)=o(L₀). Thus the term −ζ'/ζ contributes −mL₀/w+O(1) and dominates in the bracket of 361. Integrating over that circle, the residue is

    X^Φ_a(ρ) exp(uΦ_a(ρ)) E_(L₀²)(ρ) L₀^m [c_ρ+o(1)],

where c_ρ=−m Φ_a'(ρ)^m/ζ^(m)(ρ)≠0, by extracting the coefficient in exp(wΦ_a'(ρ)). This computation controls the error **relative to each amplitude**, even if some amplitudes are much larger than others. The maximum norm of the amplitudes is ≥X^(M−o(1)), since |E_(L₀²)(ρ)|≥X^(−o(1)).

**Why both signs are seen.** The complex frequencies λ=Φ_a(ρ) are distinct by 364 and have nonzero imaginary part. For each conjugate pair choose τ=π/|Im λ|. The positive measure δ₀+exp(−τ Re λ)δ_τ annihilates the integral of exp(λu) and its conjugate. Convolve all these measures with the uniform measure on [0,1]. The result is a positive measure on [0,B], with positive density on an interval, annihilating all functions of the system. By independence and analyticity, every nonzero real combination changes sign there. By compactness of the conjugate coefficient vectors with maximum modulus one, both their maximum and the maximum of their negative are ≥c>0, with c independent of the vector. Apply this to the previous expansion after normalizing by the maximum amplitude. The aggregate relative errors are o(1) and so is that of the contour; values of both signs with modulus ≥X^(M−o(1)) appear. They exceed b(x) in that block.

**Scope and antecedent.** 142–144 already employ Gaussians to detect oscillations and 126 records one-sided criteria. The additional step here is allowing the effective movement of the Euler product in each block without freezing the cut and controlling relative amplitudes to obtain both excursions. The range a≥1/((3·10¹²)²−1/4) of 364 is kept. The one-sided inequality as a approaches zero remains pending.
