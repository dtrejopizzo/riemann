# Second difference of scales and elimination of all small rows

048 used 2A(x)−A(2x). In 049 cutting the rows required adding coefficients to balance the densities of their progressions. Here the second difference of the same dilation is used. Its double zero annihilates two densities, which allows cutting directly at the marked power q.

Write P(x)=Σ Λ(n)V(n/x), A(x)=x∫V−P(x), x=j⁴, L=√x, y=4x. Use V,g,χ from the order-two construction of 047, K=C₀ L(log x)² with C₀ fixed and sufficiently large, and U(k)=1−χ(log(k/K)). Let α(v)=1−4·1_{2|v}+4·1_{4|v}, which equals −3 for v≡2 modulo 4 and one in the other classes. Then the global sign is equivalent to having eventually

    Σ_{L<q<eK} Λ(q) Σ_{v≥1} α(v) U(qv) Σ_{m≥1} μ(m)V(qvm/y) ≥ −C√x.

All indices are finite by the supports. In particular v≤eK/q=O((log x)²); the factors k=qv and m remain in the near-root ranges of 049. Here no compensations depending on the primes of a band are chosen.

**Identity and orientation.** Put B(x)=4A(x)−4A(2x)+A(4x). For large x Σ α(k)log k g(k/y)=−B(x) by the divisor identity of 045 and by Σ g(dk/y)=V(d/y)=0 for d=1,2,4. The sum of the linear main terms is also zero. With c₁=1,c₂=−4,c₄=4, we have

    α(k)log k = Σ_{q|k}Λ(q)α(k/q)+E(k),     E(k)=Σ_{d|k, d=1,2,4} c_d log d.

Indeed the sum over q is Σ_{d|k} c_d log(k/d) with the same three indices d. Both Σ c_d/d and Σ c_d log d/d vanish; thus α and E have mean density zero.

**Cutoff.** Replacing the full sum α(k)log k by the sum with U introduces O(√x): apply in each of the three progressions the upper estimate of 047 to the logarithm (including log K), with scales y/d,K/d and the same physical function in k. The integrals sum to zero by the first density identity. For E, the full sum against g is already zero and the same argument in the high part, without logarithm, has density zero by the second identity. Its sum with U is therefore O(√x).

In each row q≤L the full sum over v of α(v)g(qv/y) is Σ_d c_d V(dq/y)=0 for large x. In the high part the integrals cancel by the first density identity and the three quadratures cost O((y/q)exp(−c√(K/(4q)))). Summing with Λ(q) costs at most Cy log x exp(−c√(K/(4L)))=O(√x) by Chebyshev and the choice of C₀. The exhibited criterion is thus −B(x) with two-sided error O(√x).

**Back to the sign.** Under the sign |A(x)|=O(√x) by 047. Conversely, a lower bound for the sum gives B(x)≤C√x at j⁴. The normalised combination B(exp r)exp(−r/2) has second derivative O(exp(r/2)), by 047 applied to the three fixed translations. Interpolation at 4log j extends the upper bound to the whole tail. If 2f(x)−f(2x)≤C√x and f(x)=o(x), the iteration of 048 gives f(x)≤C√x/[2(1−1/√2)]. Apply it first to f(x)=2A(x)−A(2x), then to f=A. Both o(x) hypotheses follow from the PNT with fixed V. Thus 047 returns the global sign.

**Scope.** The second difference of scales and divisor inversion are known tools. The simultaneous cancellation of the two densities eliminates the small rows of this criterion without the correction of 049. The lower inequality on the remaining rows remains open. The choice of C₀ is made once, it does not vary with j.
