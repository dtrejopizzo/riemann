# Explicit correction with a gain of at least order log log N

With the definition of R_N from 263 one has unconditionally

    liminf_(N→∞) R_N / log log N ≥ 1/15.

The construction uses only rational coefficients before normalizing the correction. It preserves every prime power exactly, even those above the auxiliary cutoff. No optimality of the constant or of the iterated-logarithm order is claimed.

**First family of rows.** For a large integer T, r=1−1/T, M=ceil(T(log T)²) and j≥1, take

    A_j=(1−r)r^j−2(1−r²)r^(2j),       F_j(m)=⌊j/m⌋.

The variation Σ|A_j| is ≤r+2r²≤3. The infinite profile is exactly

    Σ_j A_j F_j(m)=Σ_(l≥1)(r^(lm)−2r^(2lm))=r^m/(1+r^m).

Two geometric series were summed; the above equality also holds at m=1. Truncating at j≤M discards Σ_(j>M)j|A_j|=O((M+T)exp(−M/T))=o(1). In particular B=Σ_(j≤M)jA_j=r/(1+r)+o(1). Balance the vector of floors by subtracting B F_1 and realize it with the cyclic averaging of 261 with ceiling M. This yields a genuine combination of variation ≤2(3+|B|)≤7+o(1). Its entropic value is exactly Σ_(j≤M) A_j j log j: each carry is a defect of the function j log j and the balanced combination of floors has these coefficients, except for the correction at j=1, which is zero for that function. Its factorial value is Σ_(j≤M) A_j log(j!).

**Second family with the same atoms.** On m≥2 the first family equals h_m=Σ_(j≤M)A_j F_j(m) (F_1=0 here). Put L_t=lcm(1,...,t). The row binom(L_t,1) at a prime power m equals 1_(m≤t), since m divides L_t exactly in that case. Thus Σ_(t=2)^M (h_t−h_(t+1)) binom(L_t,1), understood as a combination of carries, coincides on all those atoms with the first family. Its variation is ≤1/2+o(1): the infinite profile r^m/(1+r^m) decreases from below 1/2; the discrete variation of its truncation error over m≥2 costs ≤Σ_(j>M)|A_j|⌊j/2⌋=o(1). Subtracting the two families gives a relation exactly zero on prime powers with total cost ≤7.5+o(1).

**Mass gain.** Agreement on prime powers equates the factorial values by integer factorization. The difference between entropy and factorial logarithm in each row binom(L_t,1) lies between 0 and 1, by (L_t−1)log(1+1/(L_t−1))≤1. The net mass is therefore

    Σ_(j≤M) A_j [j log j−log(j!)]+O(1) = (1/2)log T+O(1).

For the final equality, Stirling gives j log j−log(j!)=j−(1/2)log j+O(1). The linear term sums to B=O(1). The unweighted sum of A_j is r−2r²+o(1/T), including the cutoff, and Σ|A_j| |log(j/T)|=O(1): for j≤T one uses |A_j|≤5/T and Σ_(j≤T)log(T/j)≤T; for j>T it suffices that |A_j|≤5 exp(−j/T)/T and log(j/T)≤j/T. One obtains Σ A_j log j=−log T+O(1).

**Allowed arguments and price.** For large N choose T=floor(log N/(log log N)^4). Then M log M≤log N, so that M and all L_t≤M! are within the limit N. Since log T/log log N→1, the mass divided by the variation gives the announced lower limit. To correct any error Δ in 262 it suffices to scale this relation: the cost is at most (15+o(1))|Δ|/log log N. The bound of 263 requires at least |Δ|/log(N+1). There is still no sufficient unconditional bound for |Δ| in the sign construction.

**Distinction.** 263 proved the existence of relations with growing yield by compactness and continuation of a Dirichlet series. Here two explicit families are matched on the atoms via a geometric profile and least common multiples, and the mass difference is computed by Stirling. Least common multiples are used only for the decreasing profile; the unknown prime sum of 257 is not encoded.
