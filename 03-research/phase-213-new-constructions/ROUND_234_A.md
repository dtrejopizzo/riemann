# Why small odd inverses do not work either and what a class-wise correction preserves

With V_a from 233, for all 2≤b<q, a=b⁻¹ modulo q, one has the uniform bound

    V_a ≥ M² [b−φ(b)]/(12 q b³).

Therefore V_a≥q^(1−o(1)) if b=q^o(1), b≥2. The case a=1 is exceptional in this reasoning. The same result holds for a=−b⁻¹ by reflection. The obstruction is deterministic and uses the authentic primes with their original weights.

**Exact geometry of the arcs.** For a prime of the interval (q,2q] let l∈{0,…,q−1} be the residue of a(p−q) and j=floor(bl/q). Then

    p=bl+(1−j)q,      (p−q)/q=b(l/q)−j.

The points of j/b≤y<(j+1)/b come only from the class p≡(1−j)q mod b, and each prime of that class belongs to that arc because j↦(1−j)q is bijective modulo b. If (1−j,b)>1, such p would be divisible by a prime factor of b, impossible because p>q>b. b−φ(b) whole arcs remain empty. There R_a−mean is a line of slope −M; independently of its intercept the integral of its square over length 1/b is at least M²/(12b³). Summing proves the bound. M∼q by PNT. No distribution in progressions was used, nor is uniformity of that theorem in b needed.

**Contrast computation for fixed prime b.** There is only one empty arc. On each of the other b−1 arcs the measure normalised by M converges to constant density b/(b−1) by PNT in classes of fixed modulus: in the coordinate u=by−j one counts the primes up to q(1+u) in that class. For each fixed u the mass divided by q tends to u/(b−1). The bridge divided by M converges in L² by domination. Its limit has slope −1 on the empty arc and 1/(b−1) on the rest of the circle. Its variation between maximum and minimum is 1/b and its distribution at a uniform point of the circle is uniform over that range (each of the two linear branches runs through it entirely). Its variance is therefore 1/(12b²). Thus V_(b⁻¹)/q→1/(12b²) when b prime stays fixed. The computation of the constant is not used for variable b.

**What happens when fitting each arc separately.** For c a unit modulo b and u∈[0,1], take the bridge S_c(u)−M_c u, where S_c is the mass of the primes in (q,q(1+u)] of class c and M_c=S_c(1). Denote by E_c this bridge minus its own mean. By the change u=by−j it is exactly the residual on the corresponding arc once the endpoint line has been fitted there and its mean subtracted. The empty arcs give zero after this fit. The corrected normalised energy is

    W_b = (bq)⁻¹ Σ_c ∫₀¹ |E_c(u)|² du.

Let E=Σ_c E_c, the centred bridge of a=1. The variance identity, exact for each q and b, gives

    b φ(b) W_b = V₁ + [φ(b)/q] Σ_c ∫₀¹ |E_c−E/φ(b)|² du.

The second summand measures exclusively the differences between classes. For b=2 it vanishes exactly and the correction returns V₁/2. For other b the correction moreover contains a nonnegative cost. If W_b=q^o(1) were achieved for some b=q^o(1) along a subsequence, the criterion would indeed close by the inequality above. The average bound of 233 corresponds to uncorrected V_a and does not establish such an estimate for a small inverse.

**Decision.** The transfer V₁≤b²V_(b⁻¹) of 233 cannot close the sign through any positive or negative inverse of subpower size other than ±1: its right-hand side is already ≥M²[b−φ(b)]/(12qb)=q^(1−o(1)). This obstruction covers the odd inverses that remained open. The corrected decomposition indicates exactly which term of the original direction persists even after eliminating the empty arcs.
