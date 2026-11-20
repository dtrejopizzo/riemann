# Sum over rows with the cutoff pq ≥ L

We use the representative H and the profile J of 063. It is an extension of 064 by summing over the smaller prime. Let h=(log L)^κ with the same 0<κ<a/(1+a), Y=√L, P₀=Y exp(−h/2), Q=L²/p³. For each prime p≥P₀ include all primes q>p with L/p≤q≤QL^(1/4). Write F_p for the sum of their slope contributions (one per pair, the four orderings have equal value). Then Σ_p |F_p|=O(L/log L). Arbitrary subsets of whole rows are allowed. The pairs of a row keep their signs.

**For P₀≤p≤Y.** The sum of Q is O(L exp(h)) even over integers. In the proof of 064 the PNT bounds, the complete Mellin integral and the tail z<L^(−1/8) still hold uniformly, because log Q and log q are comparable to log L. The remainder of the density costs O(QY^(−1/4)). Altogether these terms are o(L/log L). The upper endpoint in z is now Y/p≥1. The tail of the integral from that endpoint costs O_N(Q(p/Y)^N), by rapid decay. For N=4, summing this bound gives O(Σ_{p≤Y} p)=O(L/log L) by Chebyshev. The possible equality q=p at the cutoff p=Y affects at most one bounded evaluation of the main profile.

The exact mask decomposes as in 064. The valuation remainder tied to q costs altogether
    Σ_{p≤Y} (L²/p) Σ_{q≥L/p} q^(−3) ≪ Σ_{p≤Y} p ≪ L/log L.
In the inner sum it suffices to use integers. The one tied to p² costs O(L² P₀^(−4) log L)=O(exp(2h) log L). The term J(T) has T≥p L^(−1/8) and negligible contribution by rapid decay and polynomial number of pairs.

**For p>Y.** The row can only exist if p<L^(9/16). Here Q≤p. The main term can even be summed in absolute value over q. On each interval U≤q<2U with U=2^i p, the bound at zero of 064 gives O(Q exp(−c(log(U/Q))^b)) for the sum, b=a/(1+a), also counting integers. Summing over i gives O(Q), since U/Q≥2^i. Chebyshev in dyadic blocks gives Σ_{p>Y} Q≪L²/(Y² log Y). The remainder tied to q costs O(L² Σ_{p>Y}p^(−3)), of the same order. The one tied to p² and J(T) already satisfy the previous estimates, extending the sum of p^(−5) to infinity. This completes the bound.

The contribution near p=Y is paid for by the number of primes, without requiring the endpoint z=Y/p to grow. The argument covers from P₀ up to the last prime admitting the row and replaces the fixed lower boundary in q by pq≥L. For p much smaller than P₀, the prefactor cost L²/P₀² of the Mellin argument is no longer absorbed by the proven saving. The q beyond the upper cutoff and the masks with more factors also remain outside.
