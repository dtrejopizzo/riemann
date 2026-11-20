# When the proximity of the pairs pays the budget by itself

Keep η,K,l_m of 325. For fixed a>0 now use h=exp(−am), write E_m(a) for the signed energy, P_m(a) for the sum with |μ(n)μ(d)| and R(a)=limsup E_m(a)^(1/(2m)). Then

    RH ⇔ R(1/j)≤1 for all integers j≥1,
    lim P_m(a)^(1/(2m)) = max(1,2 exp(−a/2)).

For a≥log 4 the subexponential ceiling already holds unconditionally, even in modulus term by term. For a>log 4 the signed energy is asymptotic to the diagonal. For 0<a<log 4 the absolute mass grows exponentially: mere counting of pairs is not enough. The frontier log 4 is that of the estimate by moduli, not a proven threshold for the signed energy.

**Detection with exponential windows.** The representation of 325 as a positive integral of |A_m(t)|² is preserved. On a fixed interval of heights, the density W_m is ≥c exp(−am) for all large m. The local Taylor convergence argument of 325 now gives

    R(a) ≥ exp(−a/2)/(3/2−Θ).

Indeed, passing from the weighted norm to the local integral of |A_m| loses at most exp(am/2) by Cauchy–Schwarz. If Θ>1/2, some sufficiently small a=1/j gives R(a)>1. Under RH, for every r<1 and every η₀>0 one has |A_m(t)|≪_(r,η₀)r^(−m)(2+|t|)^η₀ by Cauchy and the classical bound for 1/ζ in each closed half-plane strictly to the right of 1/2 under RH (the same one used in 292). The weighted quadratic norm of that power costs O(h^(−2η₀)); hence R(a)≤r^(−1) exp(aη₀). Taking first η₀→0 and then r→1 proves the direct direction. At a single fixed width, the floor shown only guarantees detection for Θ>3/2−exp(−a/2).

**Bound by moduli.** For each n the number of distinct d with 0<|log(d/n)|<h is ≤C h n: on each side one counts integers at positive distance ≤(exp(h)−1)n. Use 2l_m(n)l_m(d)≤l_m(n)²+l_m(d)² and symmetry. The absolute cost off the diagonal is ≤C h Σ_n n l_m(n)²≪h 4^m/√m. In the last estimate, the integral corresponding to Σ(log n)^(2m)/n² is (2m)! and the error by unimodality is bounded by a constant times the maximum. The diagonal Δ_m is comparable to 1/√m: more precisely, using Σ_(n≤v)μ(n)²=v/ζ(2)+O(√v) by inversion over squares, one gets

    Δ_m ∼ (2m)! / [ζ(2) 2^(2m+1)(m!)²].

The error after partial summation is bounded by integrating √v times the modulus of the derivative of (log v)^(2m)v^(−3): after dividing by (m!)² one gains exponentially, by the gamma integrals with parameter 5/2 instead of 2. Thus for a>log 4 the absolute tail is o(Δ_m), and at the endpoint a=log 4 one gets O(1/√m) for the whole energy.

**Floor by occupation.** For 0<a<log 4, put Y=exp(2m). In [Y,2Y] there are ≫Y squarefree integers. Split that interval into O(1/h) cells of logarithmic length ≤c₀h, choosing c₀>0 with K≥1/2 on [−c₀,c₀]. Cauchy–Schwarz applied to the occupation of the cells gives ≫hY² ordered pairs in the same cell. Removing the diagonal costs O(Y), negligible since a<log 4<2. In that band l_m(n)≥(2m)^m/[m!(2Y)^(3/2)]. By Stirling the absolute contribution is ≫ h 4^m/m. Together with the previous ceiling and the diagonal this proves the announced limit. The reasoning only requires the density of squarefree integers in [Y,2Y], without assuming they are distributed in every short interval.

In particular, in the block generating the floor, the ordinary distance of the pairs is O(Y^(1−a/2)): for each fixed a a real power has been removed relative to Y. The open step consists in bounding the sum with the Möbius signs before taking moduli, for fixed arbitrarily small a.
