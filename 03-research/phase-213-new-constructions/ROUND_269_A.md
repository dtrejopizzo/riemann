# An explicit set of endpoints suffices for the whole calibrated representation

Fix N≥2 and an integer base b≥2. The endpoints N and N−b^i for 1≤b^i≤N/2 (i starts at zero) suffice. Any binomial row with endpoint n≤N and smaller side k is reproduced by an integer combination of rows with those endpoints of variation ≤4s_b(k), where s_b is the digit sum. The identity holds simultaneously for all moduli and preserves the entropy mass of 262.

**Elementary shift.** Work in the free abelian group on F₁,…,F_N with F₀=0. Put C(u,v)=F_u−F_v−F_(u−v), including the partitions with a zero side, which give the zero vector. For d≤j≤N, subtract the two rows sharing the side N−j. Directly,

    F_j−F_(j−d) = F_N−F_(N−d) + C(N−d,N−j)−C(N,N−j).

Write k as a list d₁,…,d_s of powers of b, repeating each as many times as its digit indicates. With u_i=d₁+…+d_i, telescope first the increments ending at n−k+u_i and then those ending at u_i. On subtracting, the two sums of F_N−F_(N−d_i) cancel term by term. Exactly C(n,k) remains, with at most four rows of sign ±1 per increment. Each partition is valid because both endpoints lie between d_i and N. Sides exceeding half can be replaced by their complements.

**Calibration and cost.** Evaluating the symbols F_j at ⌊j/m⌋ gives the carries for each m. Evaluating them at j log j, with value zero at j=0, preserves the entropy exactly, even for signed families. If W_c is the minimum of 262 and W_c^(b) the minimum with the endpoints prescribed here, one obtains

    W_c ≤ W_c^(b) ≤ 4 (b−1)(1+log_b N) W_c.

Thus, in base two, the whole condition of 262 equivalent to the global sign can be imposed on O(log N) endpoints, paying at most O(log N) in variation. With b=⌈exp(√log N)⌉ there remain O(√log N) endpoints and the additional cost is N^o(1), which also preserves the budget x^(1/2+o(1)). More generally one can take b=⌈N^(1/L)⌉ for any L=L(N)→∞ with L≤log N: L+2 endpoints suffice and the factor is O((L+1)(N^(1/L)+1))=N^o(1).

**Relation to closure.** 261 built a representation from inversion over all integers; 268 ruled out concentrating all endpoints in a narrow band at square-root cost. Here the identity is applied after any fit, including one that only prescribes the prime powers and calibrates the mass. Localization at these sparse scales is no longer a hypothesis that needs justification. The square-root bound on the minimum cost within them remains open.
