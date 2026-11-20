# Residues of prescribed prime support and a cross criterion without diagonal

In 350 one can require every unpaired integer to have one of the two forms qp, 2qp, with p a large prime. Here q is fixed in advance and can be 1 or any odd prime ≤(log X)^B for a fixed B. For q=1 the remaining sign is negative at the primes and positive at their doubles; for odd prime q both signs are inverted. No coefficient of μ is changed: one only chooses which integers to erase from the paired set.

**Reserves.** For each form and in each outer quarter of a cell of length J=⌊X^(2/3)⌋, the number of candidates is ≫ J/(q log X). Indeed, for p one counts an interval of length comparable to J/q with endpoint comparable to X/q. That length exceeds (X/q)^(3/5) for large X, uniformly for the indicated q. The prime theorem already used in 348 gives the lower bound; p exceeds all admissible primes q. [Guth and Maynard, theorem on short intervals](https://arxiv.org/html/2405.20552v1)

Make both corrections of 350 using exclusively those candidates. Eliminating the quantity imbalance uses O_A(J/(log X)^A) of the surplus sign. Then the position imbalance costs O_A(J²/(log X)^A), since each removed sample moves the moment by ≤J. Each correcting pair from opposite quarters compensates at least J/2−O(1) and keeps the quantity balanced. Use A>B+3 to verify that no reserve is exhausted, even after the first erasure. Stop with first moment of modulus ≤J. The Taylor proof of 350 then gives, for the residual pulse R_q,

    |S_h(x)−R_q(x)| ≪_η 1+J²/H =: O_η(E),

uniformly in q and x. The decisions can be fixed by choosing at each step the smallest admissible indices. The selection is made separately for each q: alternative representations of the same observable are obtained.

**Disjointness and cross test.** For q≠r the unpaired samples in the two representations are disjoint. Their only large prime factor p determines by division the cofactor, which belongs to {q,2q} or to {r,2r}; those sets are disjoint. In particular we can choose q=1 and r=3 with no dependence on X. Let L=∫_[X,2X] S_h² dx/x and C=∫_[X,2X] R_1 R_3 dx/x. Then

    |C−L| ≪ E√L + E².

It is obtained by expanding R_i=S_h+(R_i−S_h) and using Cauchy–Schwarz in a measure of mass log 2. Since E=o(√H), the one-sided ceiling C≪_(δ,ε) H X^ε implies L≪_(δ,ε) H X^ε by the quadratic inequality, and L under the same ceiling implies the bound for C. For each δ=1/j, j≥16, the criterion of 337 is thus equivalent to estimating **a cross product with no terms on the same integer**, with supports on primes and their doubles on one side, triples and sextuples of primes on the other.

**What has been localized and what is missing.** The absence of diagonal is exact. The selected subcollections of primes depend on the imbalances of μ in the cell. A theorem counting all primes of the interval provides the reserves and does not automatically estimate the correlation of these subcollections. The root ceiling and the global sign remain open.
