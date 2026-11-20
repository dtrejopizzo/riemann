# Neutralizing the union of all large primes: reduction to a finite product

**Status: PROVED, with independent review of the additive precision and the localization of the cut.**

Let W(y) be the balance of all admissible integers with some prime >y and C(y)=S−W(y). At the cut z=L² there exists y such that

    log(x/y²)= E/2−1/2+o(1),     |W(y)| ≪ √x (log x)^O(1),

with E=∏_{p≤z}(1−1/p)^−1. One can choose the side W≤0 or the side W≥0 with that precision. Thus the one-sided criterion of 372 is equivalent to the same ceiling for C(y), which includes only squarefree divisors of the product of primes in (z,y]. The selection uses only W; it does not presuppose the sign of S. The antecedent 385 neutralizes exactly one large prime and leaves two sectors; here the whole union is neutralized.

**Profile to additive precision.** Write v=log(x/y²)=κ log z. For κ in any interior compact subset of (0,1), the first marking T of 385 is JxE/L²+o(x/L²), uniformly: 384 gives the exact moments and its absolute remainder O(x L^(−2.7)); the errors from squares and PNT of 385 are smaller. For the two-prime sector, on |u|≤v/2 the expansion of H(L−u) of 385 has absolute error O(v²/L³), and outside that band the majorant 2(v−u)_+/(L−v)² integrated against the Gaussian has tail o(1/L²). The cost of cofactors different from one is also o(x/L²). Since the weight exp(−u)g(u)/J is normal with mean −1/2, the two-prime sector has balance

    2Jx(v+1/2)/L² + o(x/L²).

In the union, the first marking counts the semiprimes once too often; three or more primes have negligible mass. Hence

    W(y)=Jx/L² · [E−2v−1+o(1)].

The constant E is kept exact. Replacing it by its Mertens equivalent would not justify the additive term −1.

**Choice of the cut.** By Mertens E/(2 log z)→exp(γ)/2<1. Take v=E/2−1/2±1; the uniform profile gives opposite signs. When crossing p only multiples of p vary and the jump costs O(x/p), which in the whole band is O(√x (log x)^O(1)). The union changes on a finite set of primes for fixed x. Choose either of the two values enclosing zero at the first crossing, fixing for example the non-positive side (if zero is attained, choose that value). The jump bounds the absolute value, and the profile itself forces v=E/2−1/2+o(1) for both sides. The choice is between constant values on the cut intervals; it does not require monotonicity.

The transform of the remaining sum at the evaluation scale, with both endpoints frozen, has the finite factor ∏_{z<p≤y}(1−p^(−s)). The Gaussian is the same as in 368. The reduction preserves the requirement O_ε(x^(1/2+ε)) for the positive part; it does not transfer a pointwise sign within margins smaller than the jump. A one-sided bound of that precision for the finite product with the selected cut remains open.

**Review record.** The first marking is preserved to additive error o(x/L²), not only relative to the term containing E; the remainder O(xL^(−2.7)) of384 suffices. In the second sector, ∫u exp(−u)g(u)du=−J/2 gives exactly the term v+1/2. Subtracting a single copy of that sector from the first marking, to form the complete union, produces E−2v−1. Since E/(2log z)→exp(γ)/2∈(0,1), the two values v=E/2−1/2±1 lie in the same compact set of κ and have opposite signs with margin2+o(1). The cost of a jump divided by x/L² tends to0; the additive profile therefore forces the localization o(1), more precise than an o(log z). The finiteness of states and the choice of one of the two sides need neither monotonicity nor knowledge of the sign ofS. The finite product represents C only with its endpoints frozen at the evaluation scale; no single Dirichlet series is claimed for the global moving cut.
