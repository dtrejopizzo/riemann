# A second dilation cancels the density of each quotient separately

Write A_h(x)=S_h(x)−2S_h(x/2) as in 338. Now use C_h(x)=A_h(x)−2A_h(x/4), always with the same h=X^(−δ). For δ=1/j, j≥16, its second-moment criterion remains equivalent to RH: the additional Mellin factor 1−2·4^(−s) has all its zeros on Re s=1/2, and stays bounded in the strips of 337. The inverse argument of 337 works with the new bounded coefficients and preserves all poles to the right of 1/2.

In C_h one can remove with pointwise error o(√(Xh)) the whole set of quotients of height up to X^ρ, for each

    0<ρ<1/6−7δ/6.

In particular ρ=1/12 works simultaneously as a choice of exponent for each δ=1/j, j≥16 (the constants may depend on j). Unlike the exponent δ/4 of 341, this exponent stays positive as δ tends to zero.

**Coordinated cuts.** In A_h(x) use the short version of 338 with real D=2√X, P=X^(1−5δ/4) and L=P/D, that is L<d,e≤D, de>P. In A_h(x/4) use D/2, L/2, P/4. For both the truncated identity remains valid since D²≥2X and (D/2)²≥2X/4. The erased combs have length at least a constant times X^(δ/4) in both cases and the Poisson error is O_B(X^(−B)). The cut k≤K=⌈2X/P⌉ serves for both. The real cuts resolve exactly the correspondence of integration intervals without requiring equality of integer endpoints.

**Cancellation prior to the sum.** Fix coprime r,s and d=gr, e=gs. If in the first term the continuous interval of g is J, in the second it is exactly J/2. For each k, the change g'=g/2 gives

    ∫_J W_x(kg²rs) dg = 2 ∫_(J/2) W_(x/4)(k(g')²rs) dg'.

The arithmetic density c_(rs) of 341 is the same at both scales. Hence its contribution disappears for each individual k,r,s, even before using the alternating sign of k. The error of replacing each count by its integral costs O(τ(rs)√(D/max(r,s))) by 341, because the upper endpoint of J is at most D/max(r,s). Empty intervals do not contribute. For R=X^ρ there are at most 2v pairs of height v, so the sum of v^(−1/2) with those multiplicities is O(R^(3/2)). After summing over k and using τ(rs)=X^o(1), the cost is

    O(X^(1/4+5δ/4+3ρ/2+o(1))).

The exponent is strictly less than (1−δ)/2 under the announced condition. This proves the bound even if moduli of the errors over r,s,k are taken.

**Current limit.** The quadratic subtraction exploits that the common variable g enters through g² and preserves the possibly relevant poles. An unconditionally larger strip of quotients is controlled; those where the two reduced factors can be of size close to √X remain pending.
