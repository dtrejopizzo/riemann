# No positive weight on a sufficiently narrow band admits the ceiling of its integral

Let w be continuous, non-negative, nonzero, supported in [a,b]⊂(0,∞), and L=log(b/a). Write V(s)=∫ w(t)t^(s−1)dt and E(x)=Σ_p(log p)w(p/x)−xV(1). If γ is the first positive ordinate and ρ=1/2+iγ the known critical zero, of multiplicity m, then unconditionally

    limsup E(x)/√x ≥ m |V(ρ)| − V(1/2)/2.

In particular for L<2π/(3γ) the right-hand side is strictly positive for ALL such weights, whatever their profile. The critical ratio b/a for this obstruction is approximately 1.160. Sufficiency for bands exceeding that ratio is not ensured.

**Poles and comparison.** In the one-sided Mellin transform over x≥1 with measure x^(−s−1)dx, the transform of E coincides, up to an entire function, with V(s)P(s)−V(1)/(s−1), where P(s)=Σ_p log p/p^s. The part removed from the sum sees only finitely many primes and is away from x=0. In Re s>1/3 one has P(s)=−ζ'(s)/ζ(s)+ζ'(2s)/ζ(2s)+R(s), with R holomorphic there, by separation of powers (the odd orders ≥3 converge absolutely). The pole at 1 cancels and there is regularity on the real axis s>1/2. The residues at 1/2 and ρ are respectively −V(1/2)/2 and −m V(ρ), using ζ(1+2iγ)≠0.

If E≤c√x eventually, apply Landau to c√x−E on the tail: its integral converges for Re s>1/2 by real regularity on that half-axis. For s=1/2+δ, the modulus of its transform at s+iγ does not exceed its value at s, by positivity. Multiplying by δ and passing to the limit gives m|V(ρ)|≤c+V(1/2)/2. Removing the compact head does not change residues. Applying this to any c above the limsup proves the claim, including the infinite case by the usual interpretation.

**Geometry.** In V(ρ) the phases γlog t lie on an arc of length γL. For γL<2π/3, projecting onto the central direction gives |V(ρ)|≥cos(γL/2)V(1/2)>V(1/2)/2. A single critical zero thus forces root excesses at arbitrarily late scales, even if there were other zeros off the line. Detection by residues appears in 074; 105 proves a ceiling equivalent to the sign for a concrete hat of ratio four. Here the impossibility of a ceiling without tolerance holds for a whole class of weights and does not require RH.
