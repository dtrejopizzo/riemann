# A single average for the bands of every fixed logarithmic width

In 062 each B>2 required choosing a difference order h>B−2. Here a single transformation independent of B is fixed. In exchange, the upper endpoint of the band is no longer a fixed multiple of Q_p: a tail in q is included. No limit h→∞ is interchanged with the estimate of 062.

**Construction and inversion.** Fix 0<a<1, for example a=1/2. On the unit disc take the positive real branch on (0,1) and write

    C(z)=exp(−(1−z)^(−a))=Σ c_j z^j,
    1/C(z)=Σ d_j z^j,      H(x)=Σ_{j≥0} c_j 4^(−j) S(4^j x).

Here S is the scale sum of 060. The real part of (1−z)^(−a) is ≥cos(aπ/2)|1−z|^(−a). Thus C and its derivatives extend by zero at z=1 with all orders vanishing; on the rest of the circle they are smooth. By integration by parts on the circle c_j=O_N((1+j)^(−N)) for all N. The d_j are nonnegative by expansion of the exponential of a series with positive coefficients. The Cauchy bound at radius 1−j^(−1/(1+a)) gives d_j≤exp(O(j^(a/(1+a)))).

The global sign is equivalent to H(j⁴)≤C'√x eventually for x=j⁴. To justify the inversion one uses the classical unconditional bound ψ(z)−z=O(z exp(−c√log z)). By partial summation with V of compact support and 060 one obtains Q(x)=O(x exp(−c'√log x)). For S split at k≤x^(1/8), where x/k⁴≥√x, and use Q(z)=O(z) on the rest. The same bound holds for S, with another constant. Since a/(1+a)<1/2, for each x>0 the double sum resulting from inserting H into Σ_j d_j 4^(−j)H(4^j x) converges absolutely: the d_j are absorbed into exp(−c_x√(i+j)) of S(4^(i+j)x)/4^(i+j) and the c_i are summable. By convolution of coefficients S(x) is recovered exactly.

Under the sign |S(x)|≪√x, hence |H(x)|≪√x. Conversely, the first two logarithmic derivatives of H are O(x) as in 060, by Σ|c_j|<∞ and locally uniform convergence. By interpolation the upper bound at the fourth powers extends to the whole tail. In the inversion the coefficients d_j are positive and Σd_j 2^(−j)=1/C(1/2)<∞. Hence H(x)≤C'√x implies the same bound for S, and 060 applies. No global Mellin formula for H is needed.

**The profile in the slopes.** In each slope G(Z) of 061 is replaced by J(Z)=Σ_j c_j 4^(−j)G(2^j Z). Even the expansion by slopes at fixed x is justified: the sum of absolute values before grouping at scale z is O(z(1+log z)^C) for large z by support, |β|≤τ, the elementary bounds for divisor sums and Σk⁻⁴ from the average over fourth-power scales. The c_j absorb any power of j. In the mask of each slope the terms with rad(n)|r can also be reordered: for each j there are O(2^j T) integers and G is bounded.

J and its logarithmic derivatives decrease rapidly at infinity. At zero, for each N they satisfy O_N(Z²(1+|log Z|)^(−N)). Indeed G and its derivatives vanish for sufficiently small arguments; if Z<1 one starts at j≥log₂(1/Z)−O(1) and sums the weights 4^(−j)|c_j|. For Re s<2, its Mellin transform in the convention of 061 is C(2^(s−2)) times that of G, justifying the interchange first by absolute convergence. By domination as s approaches 2 from the left and by the flatness of C one obtains

    ∫₀^∞ J(z) z⁻³ (log z)^n dz = 0     for every integer n≥0.

The profile is nonzero by the same identity in the open strip. It need not vanish below a fixed threshold; the absence of that threshold allows a zero of all orders at the boundary of convergence.

**Band and bound.** For each fixed B>2 take L=√x, R=L(log L)^B, P=L/√R, P≤p≤2P, Q_p=L²/p³ and all primes

    √R ≤ q ≤ Q_p exp((log L)^(1/4)).

The signed sum in H over the four slopes of each product pq in that band is o_B(L). In particular the same H serves for every fixed B. The statement is not uniform if B varies with x.

In the expansion of the mask for T=L/√(pq), the first terms are J(T)−J(T/p). Since p<q, the others have total absolute value O((T/q)²+(T/p²)²), by |J(z)|≤Cz² and the sum of two geometric series over powers of p and q. Summing even over integers in the whole range, the first error costs O(L²/R) using Σ_{P≤p≤2P}1/p=O(1) and Σ_{q≥√R}q⁻³=O(1/R). The second costs O(L² P⁻⁴ log L), a fixed power of log L. Both are o(L). One has T≥L^(1/2−o(1)) and the number of pairs is L^(1+o(1)), so that J(T) gives o(L).

For the term with T/p use the change z=√(Q_p/q) of 062. The weight in q has bounded variation independently of p by the bounds for J and its derivative. The error of the quantitative PNT at the upper endpoint is ≪ Q_p exp((log L)^(1/4)−c√log L), negligible after summing. The endpoints in z are exp(−(log L)^(1/4)/2) and a quantity comparable to (log L)^(B/2). Expand 1/(log Q_p−2log z) to any fixed order h, with log q comparable to log L on the whole interval. The moments can be completed down to zero and up to infinity at cost O_{h,N,B}(log^(−N)L) for any N: at the lower endpoint integrate z⁻¹(1+|log z|)^(−M) and at the upper one use the rapid decay of J. All completed moments are zero. The aggregate cost of the main term so treated is O_{h,B}(R/log^(h+2)L), as in 062. Take h>B−2 in the **estimate**; the average H stays fixed.

**Scope.** The one-sided inversion argument of 062 is used with a positive inverse of infinitely many dilations; the classical PNT error, already used in the corpus (phase 188, L2_BUILD_009), justifies the inversion. This result controls a signed band for each fixed power of the logarithm with the same criterion. The balance of the complement remains open.
