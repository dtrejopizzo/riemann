# Reconstruction without depth losses for growing sieves

Let T(X) be a growing family of finite sets of primes, fixed for each real scale X≥1/2. Suppose that for each fixed σ>1/2

    ∏_{p∈T(X)}(1−p^(−σ))^(−1) = X^o(1).

In the criterion 353 it suffices to estimate the sum of simple primes whose cofactor is not divisible by any prime of T(X), with that single set in each block and the same norm and widths as 357. This estimate is equivalent to RH. There is no need to limit the number of changes of T when descending through the scales.

**Reconstruction.** Keep h fixed, and denote by R_T the observable of 357 with forbidden set T. Start with P=Σ μ(d₀)T_{d₀}R_{T(X)}, where d₀ has primes in T(X) and T_d denotes dilation. At a node with scale Y and inherited set U⊇T(Y), if they coincide, stop; if not, expand with coefficient +1 over all integers with primes in U minus T(Y), leaving T(Y) as the new set. This is the local identity of 357, valid for any difference of nested sets. Omit children with scale <1/2 because their block contains no arguments pm≥2. A child with factor 1 keeps its scale and terminates immediately; every other child reduces the scale by at least half. The tree is finite for each X.

**Uniqueness after the first choice.** Given the total product D of a terminal branch and its first factor d₀, the rest of the path, if it exists, is unique. At an expanding node, extract from the still pending quotient **all powers** of the primes belonging to the set difference just opened. That must be the factor of this step: in later steps only primes of the smaller set are admitted. Knowing that factor determines the child scale. This also reconstructs the unit steps and the stopping decision. For fixed D, d₀ is a squarefree divisor, so there are at most 2^ω(D) branches. Every leaf uses the prescribed observable at scale X/D. One could regroup with sign; the bound does not need it.

**Norm.** Let 1/2<σ<1 and η=σ−1/2. The critical-bound hypothesis with loss η at each leaf costs, in units of √(hX), at most C X^η D^(−σ). At compact scales use pulse counting as in 357, increasing C. Summing over D, the remaining multiplier is at most

    Σ_{D with primes in T(X)} 2^ω(D) D^(−σ)
      = ∏_{p∈T(X)} (1+p^(−σ))/(1−p^(−σ))
      ≤ ∏_{p∈T(X)} (1−p^(−σ))^(−2) = X^o(1).

Take η smaller than the requested loss and apply 353. The direction under RH follows from a single positive convolution for R_{T(X)} in terms of P and the same product bound. One works with fixed σ before making η arbitrarily small.

**Examples.** It holds for all primes up to (log X)² without steps and for any growing threshold (log X)^(2+o(1)). Indeed Σ_{p≤y}p^(−σ)≪_σ 1+y^(1−σ)=o(log X) in the indicated range. One can also add at once all primes up to 2X of any fixed set with O(√t) members up to t: by partial summation its series of p^(−σ) converges for σ>1/2. Thus the reconstruction admits certain exclusions of primes much larger than log²X. The antecedent 309 identifies the scale of the Euler norms; here the multiplicity bound resolves the cost of arbitrarily frequent changes of the set in the local criterion.

**Pending.** The theorem allows choosing which primes to exclude under the declared budget. It does not by itself give the critical estimate for the cofactor avoiding those primes.
