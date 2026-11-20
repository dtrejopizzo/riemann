# Exact integer binomials and the cost of their signed representation

For x≥2 set N=⌊2x⌋. At the integers 1≤m≤N one wants to reproduce exactly g(m/x), with g from 257, by carries of integer binomials with upper argument ≤N. Let V(x) be the minimal cost (sum of absolute values of the real coefficients) and

    S_j=Σ_(d≤N/j) μ(d)g(dj/x),     b_j=S_j−S_(j+1),     S_(N+1)=0.

Then one has the two-sided arithmetic certificate

    (1/3)Σ_(j≤N)|b_j| ≤ V(x) ≤ 2Σ_(j≤N)|b_j|.

This gives a finite formula controlling the optimum up to a factor six, with an explicit construction of upper cost. The representation coincides at every integer and therefore also at every prime power. Concretely,

    RH is equivalent to V(x)≪_ε x^(1/2+ε) for every ε>0.

**Finite inversion.** Write F_j(m)=⌊j/m⌋ and F₀=0. These N vectors form a triangular basis with unit diagonal. The equality Σ_j b_j F_j(m)=Σ_(l≥1)S_(lm)=g(m/x) is obtained by telescoping and using Σ_(d|k)μ(d)=1_(k=1). At m=1 it gives Σ_j j b_j=0. Each genuine carry is F_n−F_k−F_(n−k), with coefficient norm in this basis ≤3. This proves the floor, including symmetric splits.

**Cyclic construction for the ceiling.** For each j average over r=0,...,N−1. Write r+j=q+eN, with 0≤q<N and e∈{0,1}. The vector F_j+F_r−F_q−eF_N, if e=0, is minus a carry. If e=1 it is the difference between the carry that splits j into q and N−r, and the one that splits N into r and N−r. Partitions with a zero side contribute zero and are omitted. Each term costs ≤2 in variation and only uses arguments ≤N. On averaging, q runs through the same residues as r and there are exactly j cases with e=1. Thus F_j−jF_N/N is represented. Multiplying by b_j and summing cancels F_N by the balance relation. The formula needs neither rounding at the atoms nor choosing factorial arguments larger than 2x. Multiplied by Λ(m) and summed over m, it directly gives a combination of log binom(n,k) for the count with prime powers.

**Size of the coefficients.** Interpolate S(v)=Σ μ(d)g(dv/x) for 1≤v≤N+1. The weight is C¹ and t g'(t) has bounded variation with support [1,2]. Under RH the Mertens bound and partial summation give |S'(v)|≪_ε (x/v)^(1/2+ε)/v on the support. Integrating to bound Σ|S_j−S_(j+1)| proves the square-root ceiling. Unconditionally the same argument up to v=√x uses M(t)≪t exp(−c√log t), and for v≥√x M(t)≪t suffices. It gives V(x)≪x exp(−c'√log x).

Conversely |S₁|≤Σ|b_j|≤3V(x). The Mellin transform with respect to x of S₁(x)=Σ μ(d)g(d/x) in Re s>1, integrating from 0, is H(s)/ζ(s); the lower support is x≥1/2. A square-root bound with arbitrary loss would extend that transform holomorphically to Re s>1/2. There H does not vanish, so no zero of ζ can lie in that half-plane. It would even suffice to bound V at integer x: |dS₁/dx|=O(1) by the absolute sum and the boundedness of g'. The converse argument uses exactness at all integers, including the composite entries that Λ does not see. It does not establish the same necessity for a representation that only fits the atoms of Λ.

**Antecedents and difference.** 259 gave continuous inversion and an approximation budget in L¹. 260 resolved a barrier for positive mixtures at the prime atoms. Here the balance of the floor basis allows an integer inversion to be converted into genuine binomials with uniform cost through the cyclic average. Möbius inversion by itself is classical. The unconditional square-root bound for the explicit arithmetic variation remains open.
