# What the residue classes detect in the criterion of 054

Use L=√x, y=4x, K=C₀L(log x)² and the weights of 054. Denote by R(q) the weight of the row before multiplying by Λ(q), including the restriction q>L:

    R(q)=1_{q>L} Σ_{v,m≥1} α(v) U(qv) μ(m) V(qvm/y).

Here q can be any integer. For each fixed 0<η<1/2, with C₀ sufficiently large fixed once and for all,

    sup_{d≤x^(1/2−η)} Σ_{r mod d} | Σ_{q≡r mod d} R(q) | = o(1).

In particular one can replace Λ(q) by Λ(q)−1 in the lower criterion of 054. One can also subtract any periodic profile of modulus in that range and bounded sup norm. The statement concerns the test weights R, not the distribution of primes in progressions.

**Passage to periodic models.** Let f be real, d-periodic, |f|≤1. In the complete sum without U and with all q, α*μ is supported on j=1,2,4 with masses c_j=1,−4,4, respectively. One gets Σ_q f(q)Σ_j c_j V(jq/y). The integral parts of the mean of f vanish by Σc_j/j=0. The remainder has size O_N(y(d/y)^N): in each progression sum the smooth weight by Poisson, with N≥2 integrations by parts. For a smooth function supported on a band of width comparable to Q and derivatives of order n bounded by C_n Q^(−n), the error per progression when d≤Q is O_N((Q/d)(d/Q)^N), uniform in the residue. Summing the d residues leaves O_N(Q(d/Q)^N).

The rows with q≤L and U cost altogether O(y log x exp(−c√(K/(4L))))=o(1). Indeed, their full sums are zero; the quadratures of their high parts have combined density zero by 054. This bound only uses |f(q)|≤1. C₀ is taken sufficiently large so that the exponent absorbs y log x.

**High part of the constant mean.** Write ε(n)=(−1)^(n+1). The divisor convolution satisfies 1*α=ε*ε: both are the convolution of two constant functions with the three atoms c_j, since ε=1*(δ₁−2δ₂). Thus, for the constant model, the part with 1−U is expressed exactly as

    Σ_{a,b,m} ε(a)ε(b)μ(m)[1−U(ab)]V(abm/y).

Use a smooth dyadic partition in a,b, with sizes Q,R, respectively. In a nonempty box QR≳K, m≪y/(QR), and at least one of Q,R is ≳√K. In the larger variable the alternation has mean zero and the progression estimate gives the saving O_N(max(Q,R)^(−N)) with respect to the trivial count. The derivatives of the cutoff cost O_n(Q^(−n)) or O_n(R^(−n)) in the corresponding variable, since it is a fixed cutoff in log(ab/K); the same holds for the weight V on the support of its derivatives. Summing over the other variables and over the O(log²y) boxes yields O_N(y K^(−N/2) log²y).

**High part of the mean-zero profile.** Subtract the mean of f and incorporate the preceding estimate. In the original high sum take boxes q≈Q,v≈R. Both the centred f(q) and α(v) have mean zero, with periods d and 4. The larger scale measured in periods is at least a constant times √(K/d), since QR≳K. Apply the progression estimate in the variable that reaches that scale. Uniformity with respect to the residues avoids the appearance of an additional factor d. The remaining count gives

    O_N(y (d/K)^(N/2) log²y).

For d≤x^(1/2−η), choose N>2/η. All bounds are uniform in f and d. Subtracting the high part and the small rows from the complete sum one obtains Σ f(q)R(q)=o(1). Choosing f in each class as the sign of its sum proves the statement.

**Scope.** The high cutoff of the constant model exploits the factorisation into two alternating variables; centring the prime weight before the cutoff was not enough to justify the result. The bound holds for the complete sum of 054. Imposing afterwards a restriction on qvm can break the factorisation. The uniform lower estimate of Σ(Λ(q)−1)R(q) remains open.

**Almost-root range.** The same conclusion holds uniformly for d≤c₀ L/(log x)² with c₀>0 fixed and sufficiently small. To control the orders of differentiation use the telescopic partition χ(log u−i)−χ(log u−i−1), i integer, in each positive variable. There are O(log²y) active boxes in the full sums. In a variable z of scale Q, the ordinary derivatives of order N of the box weight have L¹ norm ≤Q^(1−N) C^(N+1)(N!)²: in log z the factors are translates of the fixed weights of 047 and their products preserve the bound by Leibniz, and the conversion to ordinary derivatives is the one proved in 047. Therefore, choosing the order in the long variable, the high contribution per box is ≤Cy exp(−c√max(Q/d,R)), by the same optimisation computation as in 047. In total it costs O(y log²y exp(−c(K/d)^(1/4))). For d≤c₀L/(log x)² the exponent exceeds 2log x if c₀ is sufficiently small. The constant mean and the small rows are already controlled; the complete sum of periodic f is also estimated with a large fixed order since d/y is of order at most x^(−1/2). This argument uses a single modulus at a time, with uniformity in its choice. The antecedent CORRECTION_RESIDUE_BALANCE_031 of phase 211 describes the failure of inferring cancellation for arbitrary weights only from balance in a complete class. Here the quantitative control comes from the regularity of the weight and from the second mean-zero variable.
