# Balance of all sectors of fixed order and obstruction to truncation

**Status: PROVED, with independent review of the convolution, its continuation and the scope of the truncation.**

With the notation of 379–380, for every fixed integer d≥1 and fixed 0<a<1,

    S_d ∼ (−1)^d J x P(0)/L · [log(L/b)]^(d−1)/(d−1)! .

Here S_d includes all parities of the cofactor formed by primes between z and y. The density of d primes without that cofactor already appears in 369. The present statement transports the density through the signed sum of cofactors to the exact cut z=L².

**Prime substitution.** The truncations of 380 are applied, writing n=m p₁⋯p_d and dividing by d!. The repetitions with p_i=p_j cost O_d(Y exp(−b)(1+L)^d) for factors ≤exp(2L), by g(log(Y/n'))≪Y/n', Σ_{p>y}p^(−2)≪1/y and the reciprocal sum of the other factors; Y=x/m. On the untruncated tails, the coefficient per product after ordering and dividing by d! is ≤1. Replacing each prime measure successively by dt/log t costs O_d(Y(1+L)^d exp(−c√b)): fix the other factors, apply the integration by parts of 380 and sum their reciprocals. For fixed d the errors survive the absolute sum over cofactors with a saving larger than any power of L.

**Density and derivatives.** Let H_d(D) be the d-fold convolution of 1_{v≥b}/v on the logarithmic scale, divided by d!. For d≥2 and D>db, multiplying by D=Σv_i and using symmetry gives

    D H_d(D)=(1/(d−1)!)∫_{v_i≥b, Σv_i≤D−b} ∏_{i=1}^{d−1} dv_i/v_i.

For D=L, the simplex contains the cube [b,(L−b)/(d−1)]^(d−1) and is contained in [b,L]^(d−1). Integrating over the two cubes gives H_d(L)∼[log(L/b)]^(d−1)/((d−1)! L). To justify the signed sum, change v_i=b+(D−db)u_i: the domain becomes the fixed simplex u_i≥0, Σu_i≤1. On |D−L|≤L/2, for L large, Re(D−db)≥L/3; each factor of the integrand is bounded in absolute value by C L/(b+Lu_i). This gives holomorphic continuation and the bound O_d(H_d(L)) by integrating over the unit cube. For d=1 one uses H_1(D)=1/D near L.

Then the Taylor argument and the moments of P of 380 apply with this H_d: fixed degree N chosen to absorb L^C(b/L)^N/P(0), and non-constant terms of relative size O_{i,d}((b/L)^i). Outside |u|≤√L the real density is bounded by O_d((1+log(D/b))^(d−1)/D) on D≥db, sufficient by Gaussian decay. The main term has sign (−1)^d and is the stated one.

**Consequence.** For any fixed cut d₀≥1, the sum up to d₀, including the negligible zero sector of 379, is asymptotic to S_(d₀). Its complement is asymptotic to −S_(d₀) by the ceiling of 377. The fixed-order equivalents deliberately leave out the sum when d₀ grows with x; the equivalent ratio between consecutive sectors is only justified here at fixed d. Thus attributing the global sign to the predominance of any fixed last sector is ruled out.

**Review record.** The identity for D H_d uses d symmetric terms, so the resulting factor is d/d!=1/(d−1)!, without an additional multiplicity. In the change to the fixed simplex the complete integrand is the product of (D−db)/(b+(D−db)u_i), with d−1 factors; the bound C_d L/(b+Lu_i) and |D|≥L/2 justify holomorphy and the ceiling O_d(H_d(L)). The inner cube has upper side (L−b)/(d−1), whose logarithm relative to b differs from log(L/b) only by O_d(1). Thus the exact leading coefficient is obtained before applying the signed moments of380. Repetitions, tails and the d PNT replacements are paid in absolute value with a factor polynomial in L for fixed d; the savings exp(−b), exp(−c sqrt b) and exp(−cL/b) dominate those factors for each fixed a in(0,1). Finally the ceiling of377 is smaller in absolute value than any fixed-order S_d, so the complement cancels its main term; it does not determine the sign of the residue nor allow summing the equivalent uniformly in growing d.
