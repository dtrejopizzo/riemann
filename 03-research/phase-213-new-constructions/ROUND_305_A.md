# Barrier for the balanced cutoff above the square root

Put L=log x and R_t(x,y) as in 303. There exists an absolute K such that, at frequency zero, **all** cutoffs

    √x ≤ y ≤ x exp(−K(log log x)²)

give R₀(x,y)∼−48 U (log 2)² x/L⁵, uniformly. The same interval preserves the transition asymptotic of 302 for any t→0. Thus the lack of a rate in round 304 has arithmetic content: in the region with a single large prime, a cutoff with small balance cannot cross this barrier. If the one-sided ceiling of the first row is proved, the barrier improves to x/y≤(log x)^(8+o(1)) for every cutoff with |R₀(x,y)|=o(x/L⁵).

**Transport between cutoffs.** Denote by B_t(v) the full partial sum. For √x≤y≤x the exact identity is

    R_t(x,y)−R_t(x,√x)=2 Σ_(√x<p≤y) u_p B_t(x/p).

The cofactor is strictly less than p. The classical Mertens bound from the zero-free region, M(v)≪v exp(−c√log v), passes to B_t(v) with another constant c>0, uniform for |t|≤1. Indeed use the factorization of 294: in each convolution via the hyperbola method the long sums are evaluated at arguments ≥√v and the absolute harmonic sum of the short coefficients costs a power of log v. The rectangular intersection satisfies the same estimate. The partial sums of the factors χ(n)n^(±it) are O(log(2v)); the two copies of μ have the above classical ceiling. On adding the correction, absolutely summable at Re s=3/4, one splits into d≤√v and d>√v; in the tail one gains v^(−1/8) relative to the trivial ceiling with logarithms. The logarithmic losses are absorbed by reducing c finitely many times.

Setting z=x/y, the difference of cutoffs costs O(x exp(−c√log z)), since u_p≤2 and Σ_(√x<p≤x)1/p≪1 by the PNT. Choose K with c√K>6 and apply 302 at √x. The error O(x/L⁶) is smaller than the main term over the whole transition, even when t=0.

**One-sided test that could falsify the first row.** If B₀(v)≤C_σ v^σ for 1/2<σ<1, the above identity preserves orientation because u_p≥0. By partial summation and the Chebyshev bound one has Σ_(p≤y)p^(−σ)≪_σ y^(1−σ)/log y. This gives

    R₀(x,y)−R₀(x,√x) ≤ O_σ(C_σ x z^(σ−1)/L).

To raise the balance from its value at √x to o(x/L⁵) in modulus one therefore needs z^(1−σ)≪_σ C_σ L⁴. If the ceiling holds for all σ>1/2, necessarily z≤L^(8+ε) for each ε>0 and sufficiently large x. In particular, constructing infinitely many balanced cutoffs with √x≤y and x/y≥L^(8+δ), for some fixed positive δ, would refute that first row and by 299 also RH. This is a conditional implication; 304 only provides x/y→∞ without that rate. Below √x integers with two large primes intervene and the transport identity used here no longer holds.
