# A prefix inequality without a continuous parameter

Let p_n be the primes in increasing order, w_n=log p_n, H_n=Σ_{k≤n}w_k and Q_n=Σ_{k≤n}w_k². The global sign is equivalent to

    B_n = Q_n − H_n log H_n + H_n ≥ 0 eventually.

Indeed S(x) of selection 092 is the maximum over n≥0 of H_n log x−Q_n (the empty prefix gives zero): the increments are w_n log(x/p_n), which change sign only once. For each n≥1, the maximum over x>0 of H_n log x−Q_n−x is attained at x=H_n and equals −B_n. If S(x)≤x eventually one can evaluate at H_n→∞ and deduce B_n≥0, even if H_n is not between p_n and p_(n+1). Conversely each prefix with B_n≥0 stays below x for all x, and the finitely many initial prefixes also do so for x large enough. Apply 092.

**How much removing the variable x costs.** Exactly, for p=p_n,

    B_n = p−S(p) − p[ (H_n/p)log(H_n/p)−H_n/p+1 ].

The correction being subtracted is non-negative, asymptotic to (H_n−p)²/(2p) when H_n/p→1 with H_n≠p. Thus replacing the maximum of the prefix by its value at the prime loses an explicit second-order term.

**Exact increment.** B_0=0 and B_n−B_(n−1)=∫_{H_(n−1)}^{H_n}log(p_n/t)dt. There are negative increments whenever H_(n−1)≥p_n. Hence an attempt to prove the sign by monotonicity would require information on the position of the prime relative to its accumulated mass. The one-sided task is to control the signed total of these increments. This elementary dualization of the prime criterion does not prove such an estimate.
