# Cancellation of increments lengthens the windows of small cost

Let Ω(X)=(log X/log log X)^(1/3). For some fixed constant κ>0, set L=X^(2/3)exp(κΩ(X)). Two unconditional ceilings are obtained:

* Along the subsequence of integers n of 237, with X=n, X⁻²∫_X^(X+L) F(x)² dx→0 for the SAME cosine of 236.
* For ALL sufficiently large X, the local quadratic minimum of 231 on [X,X+L] also tends to zero. In this statement even the line of slope one and intercept zero for the count from X suffices.

The factor that lengthens L exceeds every fixed power of log X but is X^o(1). The gain comes from cancelling the main term of the increments of the count; the rule of 237 based only on counting integers does not give these ceilings.

**Imported estimate and uniformity.** Let E(z)=θ(z)−z. For X^(5/8)≤v≤X/2, uniformly in y∈[1,2],

    |E(y(X+v))−E(yX)| ≪ v exp(−c Ω(X))

with some c>0. Thorner–Zaman, section 1.2, is used, a consequence of their Theorem 1.1 for Hoheisel intervals. In their notation take modulus 2, class 1, upper endpoint z=y(X+v), length yv and A=1. For ε=1/48 one has 7/12+ε<5/8, so yv≥z^(7/12+ε)log z eventually. All primes of the interval are odd. The quantities Ω(z) and Ω(X) are comparable and c can be reduced. For 0≤v<X^(5/8) counting integers gives O((v+1)log X). [Thorner and Zaman, section 1.2](https://arxiv.org/pdf/2108.10878).

**Where the main term cancels.** With f(y)=cos(2πy) and the left-open endpoint convention, ∫₁² f(y)dy=0 and f(1)=f(2)=1 give by parts

    F(x)=E(2x)−E(x)−∫₁² f'(y)E(xy)dy.

On subtracting the value at X from the value at X+v one obtains only increments of the same E, including both edges. The integration constant costs at most 2+∫|f'|. For 0≤v≤L one deduces

    |F(X+v)−F(X)| ≪ X^(5/8)log X + L exp(−c Ω(X)).

At X=n with |F(n)|≪log n from 237 the same ceiling can be used for |F(n+v)|. Multiplying its square by L/X² costs
O(X^(−1/12+o(1))+exp((3κ−2c)Ω(X))). Choosing for example κ=c/3 gives convergence to zero. In the second statement the residual of the proposed line is directly E(X+v)−E(X). The same estimate applies to it for every X without choosing a crossing, and minimisation can only improve it.

**Interpretation.** The relative length L/X=X^(−1/3+o(1)) does not satisfy the hypothesis log(1/h)=o(log log X) of 231 and 236. The ceiling for these lengths already holds in both alternatives for RH, so it does not resolve the obligation of the detecting windows. No numerical value for κ nor a fixed improvement of the exponent 2/3 is given.
