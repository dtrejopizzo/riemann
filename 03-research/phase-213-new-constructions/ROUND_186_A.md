# Separation of the frequencies required by 184

For large N, let μ be the probability on the primes of [N,eN] proportional to log p, U=log(p/N) and φ(t)=Eμ exp(itU). There are absolute constants c,C>0 with the following property: given 0<α<1 and 0<ε<c(1−α)², if |φ(t)| and |φ(t')| are ≥1−ε, then

    |t−t'|≤C√ε   or   |t−t'|>N^α.

The threshold for N may depend on α. The individual heights are arbitrary. In 184, choosing D large enough first, this excludes intermediate differences between two candidates for the same block. The possibility of an isolated peak persists.

**Phase difference.** Each unit variable exp(itU) with mean of modulus ≥1−ε is at L² distance at most √(2ε) from a constant of modulus one. For the product of one and the conjugate of the other the distance to the product constant is ≤2√(2ε). Taking real parts, |φ(t−t')|≥1−4ε.

**Moderate frequency.** For 1≤s≤N^α and any angular arc of fixed half-width η<1, the condition exp(is log(x/N)) in the arc cuts [N,eN] in O(1+s) intervals. Each has length ≤2eηN/s by the chain rule, also if it touches an edge. They can be majorized by intervals of length H=ceil(2eηN/s)+2. The classical Brun–Titchmarsh inequality with modulus one gives O(H/log H) primes per interval; the constant is absolute. For N large depending on η and α one has log H≥(1−α)log(N)/2. Multiplying by log(eN) and dividing by the total mass (e−1+o(1))N, we obtain probability ≤C₀η/(1−α). Here sH=O(ηN) uniformly, for N sufficiently large. Taking η=c₀(1−α) with c₀ absolute and small leaves at least half of the mass outside any such arc. Centring at the argument of φ(s) gives 1−|φ(s)|≥(1−cos η)/2≥c₁(1−α)².

**Low frequency.** For |s|≤1 and U' an independent copy, 1−|φ(s)|²=E[1−cos(s(U−U'))]≥c₂s² Var(U). By PNT, U converges in law to the density e^u/(e−1) on [0,1], of positive variance. These two bounds and the phase difference prove the separation.

**Local shape of the peak.** If φ(t)=|φ(t)|z, |z|=1, then |φ(t+s)−zφ(s)|≤√(2ε) for all s by Cauchy–Schwarz. For s in a compact set, φ(s) converges uniformly to (exp(1+is)−1)/((e−1)(1+is)), by PNT and equicontinuity. This identifies the profile near a candidate, with error O(√ε)+o(1).

181 estimated the total measure of an exceptional set for the global comb. Here separation is deduced for two frequencies of the almost maximal average of the same block and without restriction on their absolute height. Brun–Titchmarsh already appears among the tools of R163_602; here it is applied to the preimage intervals of an arc for the difference frequency. The proof requires mass on all primes and does not apply to the arbitrary weights of 185.
