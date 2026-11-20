# Windows of size X^(2/3) where the first component already passes the ceiling, unconditionally

Let F be the cosine sum of 236 with weights on plain primes. Without assuming RH one has

    limsup F(x)/√x ≥ 0.24,      liminf F(x)/√x ≤ −0.24.

In particular there are integers n→∞ with |F(n)|≪log n. Moreover, along that same sequence, for 1≤L≤n,

    n^(−2) ∫_n^(n+L) F(x)²dx ≪ L(L+1)² log² n/n².

Taking L=n^(2/3) one obtains O(log² n). This meets the subpower scale even if RH fails: a window of that length cannot replace the windows of 236 with the same normalisation. Optimality of the exponent 2/3 is not claimed. For L=n^c with c<2/3 the obtained ceiling tends to zero.

**Comparison of two residues.** By 236, under failure of RH, excursions of both signs with exponent strictly greater than 1/2 are already known. To cover the other case assume RH during this argument. Let P(s)=Σ_p(log p)p^(−s) and M(s)=H(s)P(s), the one-sided Mellin transform of F. F(x)=O_ε(x^(1/2+ε)) by 235, so the integral converges absolutely to the right of 1/2. To continue up to the two boundary points use

    P(s)=−ζ'(s)/ζ(s)−P(2s)−Σ_(l≥3)P(ls).

The tail converges locally for Re s>1/3. At s=1/2 the pole of P(2s) has residue 1/2 because P(z) has residue one at z=1. At ρ₁=1/2+iγ₁ that term is regular, since ζ has no zeros on Re z=1 and 2ρ₁≠1. Therefore the residues of M are −H(1/2)/2 on the real axis and −mult(ρ₁)H(ρ₁) at ρ₁.

If F(x)≥−c√x eventually, integrate the nonnegative function F(x)+c√x from that threshold. For σ>1/2 the modulus of its Mellin transform at σ+iγ₁ does not exceed its real Mellin transform at σ. Multiplying by σ−1/2 and passing to the limit gives mult(ρ₁)|H(ρ₁)|≤c−H(1/2)/2, since the removed prefix is entire in s. Under the assumption F(x)≤c√x eventually, the same argument with c√x−F(x) gives mult(ρ₁)|H(ρ₁)|≤c+H(1/2)/2. Both conclusions are impossible for c=0.24.

**Certificate.** The verifier verify_237.py uses Arb balls at 1024 midpoints of [1,2]. For y^(−1/2+it)cos(2πy) the supremum of the modulus of the derivative with respect to y is ≤|−1/2+it|+2π; the error of the midpoint rule with that bound is at most the supremum divided by 4096. For the ordinate it is computed at t=14.135 and 1/200 is added for the t-derivative of H, of modulus ≤log 2, covering the certified interval 14.13≤γ₁≤14.14 of Z1. One checks |H(1/2)|<0.01, Re H(ρ₁)<−0.16 and Im H(ρ₁)>0.20, whence |H(ρ₁)|>0.25. The certificate only decides the residue margin.

**Crossings and windows.** The estimate of 236 between x∈[n,n+1] and n is O(log n); the excursions give integers of both signs arbitrarily far out and, between them, integers with |F(n)|≪log n. From each of them, telescope the same estimate up to n+L to dominate the supremum by C(L+1)log n. Integrating the square gives the announced ceiling. This proves existence of good windows with a growing size in both alternatives for RH. Those of 236 that would detect the sign have length X^(1−o(1)), with the more precise condition on h of 231. The good sequence at that size has not been constructed.
