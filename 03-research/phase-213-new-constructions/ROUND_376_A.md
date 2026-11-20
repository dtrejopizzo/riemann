# Logarithmic marking of the layer: growth up to (1−ε)log log x

**Status: PROVED, with independent review of the common moment, the marks and the exclusions.**

With the notation of 375, uniformly for 1≤k≤2h,

    k M_(k+1)(x) ≥ (1−o(1)) h M_k(x).

Thus every odd prefix up to (1−ε)h has negative sign for x sufficiently large, for each fixed ε>0. In 375 two possible choices of prime cost k(k+1). Here the total mass of one of those marks is normalized exactly.

**A common prime estimate.** For Y→∞ one has

    Σ_p (log p) g(log(Y/p)) ∼ J Y,   J=∫ g(u)exp(−u)du>0.

On |u|≤B fixed it holds by the PNT, as convergence of the measure θ(Ydt)/Y to dt on a compact set of t>0. The tails are uniformly small relative to Y by taking B large, by θ(t)≪t and unit bands with the Gaussian. The same equivalent holds after truncating to |u|≤2√L if Y→∞ uniformly and L→∞. It is only used for log Y≥L/(3kh), far above √L.

**Input.** Discarding |log(n/x)|>2√L costs o(1) by 375. In each remaining product distribute its mass g among its primes p with weights log p/log n. If only log p≥L/(kh) are retained, the relative loss is O(1/h) by Σ log p=log n. For each distinct cofactor m=n/p so generated, write Y=x/m; then log Y≥L/(2kh). Now summing over all p, including the discarded ones, and using log n∼L in the original central range, one obtains

    (1−o(1)) M_k ≤ (1+o(1)) (J/L) Σ_m Y.

The absorption of the absolute o(1) is uniform by the construction of 375, valid also for k≤2h because kh=o(L).

**Output.** For each m choose q∤m in L²<q≤exp(L/(10kh²)). Set Y'=Y/q. For primes r with |log(Y'/r)|≤2√L one has r>q and log(mqr)∼L. Deleting the r|m costs O(kL) in the sum weighted by log r, since g is bounded and log m≤2L. Since log Y'≥L/(3kh), that cost is o(Y') uniformly. By the prime estimate, the sum for this pair m,q, with weight g(log(Y'/r))log r/log(mqr), is (1+o(1))JY/(qL). Mertens gives Σ_q 1/q=h−O(log h) uniformly, including the exclusion of the divisors of m.

For a final product N=mqr, with r fixed, there are at most k choices of q among the other factors. Summing over r, Σ_{r|N}log r/log N=1. Hence the whole marked output weighs at most k M_(k+1). Comparing input and output gives the announced inequality. The gain comes from keeping the same J in both estimates, in addition to recovering a power of k in the multiplicity.

**Review record.** The prime equivalent is uniform because the smallest allowed log Y' is L/(3kh)≥L/(6h²)→∞ and exceeds sqrt L; that is why the same J appears in input and output, even after the Gaussian truncation. Excluding q|m loses at most k/L² in the sum of reciprocals. Excluding r|m loses O(kL)=o(Y') uniformly, before dividing by L. Each final product fixes m once q,r are designated; for each r there are at most k choices of q, and the sum of all marks log r/log N is exactly 1. Non-generated terms only reduce this positive sum, so the bound kM_(k+1) does not require that all primes can act as r. The lower construction of 375 remains uniform for k≤2h, with log M_k≥L−O(kh+h), and absorbs the o(1) tail.

**Scope.** For k≤(1−ε)h, the ratio exceeds 1 uniformly as x grows. This preserves the favorable sign on a larger strip; the argument loses that guarantee when k/h exceeds 1. The total balance and the control of the intermediate layers of 374 remain open.
