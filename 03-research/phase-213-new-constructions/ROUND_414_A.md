# Eliminating the unknown normalization without losing the sign of each zero

**Status: PROVED, with independent review of the derivative inR², the dyadic identity and the constant3.**

Let X,P,D be from 412, and define with data only at finite real abscissae

    B(R)=2∫₀ᴿ log(X(w)/P(w))dw − 2∫ᴿ^(2R) log(X(w)/P(w))dw.

Then B(R)=2D(R)−D(2R) and B(R)≥0. More precisely

    B(R) ≍ Σ_{γ>0} δ² R³/(R²+γ²)²,      R B(R) → 3 Σ_{γ>0}δ²

(including infinity). The constant c of 412 cancels exactly. The formula does not use argument caps. P still requires the ordinates with multiplicity.

**Positivity per zero.** In the proof of 412, for J_R(d)=∫_(−R)^R log((w−d)²+γ²)dw one has

    J_R''(d)/R = 4a/(a²+4γ²d²),    a=R²+γ²−d².

For |d|≤1/2 and γ≥2 one has a≥γ²−1/4>2γ|d|, with absolute relative margin. The derivative of the expression with respect to R² is negative and its opposite is comparable to 1/(R²+γ²)². Integrating that derivative between R² and 4R² gives 2J_R''(d)−J_(2R)''(d)≍R³/(R²+γ²)² with positive sign. Two integrations with respect to d as in 412 give the claimed upper and lower bounds for B. For each fixed upper zero its contribution multiplied by R tends to 3δ² by the individual equivalent of 412. Cδ² dominates if the sum is finite; in the infinite case positive partial sums suffice. In particular B(R)=o(1/R) along a sequence would imply RH.

**Which part of the real tail is arithmetic.** Since D(U)→0 by 413, D(R)=−2∫_R^∞ [log(X/P)−c]dw as an improper integral. For R>1, X(w)=A(w)ζ(w+1/2), with A(w)=s(s−1)π^(−s/2)Γ(s/2)/(2ξ(1/2)), s=w+1/2. The portion of this tail contributed by log ζ is computed absolutely by

    ∫_R^∞ log ζ(w+1/2)dw = Σ_{n≥2} Λ(n)n^(−R−1/2)/(log n)² = O(2^(−R))  (R≥2).

The tail identity does not confer that saving on the term log(A/P)−c. In the finite version B, c cancels without taking a difference of divergent integrals.

**Robustness when truncating heights in the identity by displacements.** For large H≥R, the part of B coming from γ>H is O(R³/(H³ log H)) by M(T)≪T/log T of 413 and dyadic blocks. This error corresponds to the positive expansion in δ²; it does not authorize replacing P by the truncated product in the two real integrals with the same error. The pending global inequality is still a bound on the contribution of all heights, not on the factor ζ in the right tail.

**Review record.** For q=R², the derivative of4a/(a²+4γ²d²) is4(4γ²d²−a²)/(a²+4γ²d²)². The conditionγ≥2, |d|≤1/2 gives an absolute margin between a and2γ|d|; the opposite of the derivative is comparable to1/(q+γ²)². Moreover2J_R''−J_(2R)''=2R[Q(R²)−Q(4R²)], with Q=J_R''/R, so the factorR³ and its sign are correct. The combination2D(R)−D(2R) cancels exactly the two terms linear in c and coincides with the defined finite integrals. The individual limit is2·(2δ²)−δ²=3δ² after multiplying byR, with one term per upper zero and its multiplicities; domination and positive partial sums also cover the infinite limit.

The use ofD(U)→0 only establishes the improper integral of the complete tail, not absolute convergence of each archimedean part separately. The positive expansion of log ζ allows Tonelli and gives the exact factor(log n)^(−2). Finally, truncating the sum of the deficit and truncatingP are different operations: even underRH, when the deficitB is0, replacingP byP_H leaves log(P/P_H), increasing in w>0, and its dyadic difference is negative and non-zero. It cannot obey a bound based only on the displacementsδ², all zero in that case.
