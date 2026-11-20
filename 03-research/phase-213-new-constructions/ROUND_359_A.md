# Criterion with the whole product free of small primes

Let Q_{z,h} be the part of P_h of 353 with p>z and with all prime factors of m greater than z, including the case m=1. Then RH is equivalent to

    ‖Q_{z,h}‖_Y ≪_η √(hY) Y^η

for each η>0, all large Y, 0<h≤1 and uniformly in (log Y)²≤z≤4(log Y)². Now it is the whole integer n=pm that must lack small primes. The family of cuts has multiplicative width four; the equivalence for a single exact cut of both factors is not claimed here.

**Identity.** Write T_d for the dilation of 357, L_z=Σ_{p≤z}(log p)T_p, K_z=Σ_{d z-smooth}T_d and U_z=Σ_{d z-smooth}μ(d)T_d. At fixed cut one has

    Q_z=K_z(P−L_z S),      P=L_z S+U_z Q_z.

Indeed L_z removes the exterior prime label, and K_z erases the Euler factors of the cofactor by the identity of 357. Under RH the critical norms of S and P are known by 353. In the norm of exponent σ=1/2+ε, the cost of K_z is ≤∏_{p≤z}(1−p^(−σ))^(−1)=Y^o(1) and that of L_z is polylogarithmic. Starting with a loss less than η and using trivial counts at bounded scales proves the direct direction.

**Recovering the sum.** Fix 0<ε<1/4, σ=1/2+ε, and let A(X) be the supremum of ‖S_h‖_Y/(√(hY)Y^ε) for 1/2≤Y≤X and 0<h≤1. It is finite by 353. In what follows all costs in the block X are normalized by √(hX)X^ε. Take z=(log X)². The term L_z S costs at most

    A(X) Σ_{p≤z}(log p)p^(−σ) = O_ε(A(X)(log X)^(1−2ε)),

by Chebyshev and partial summation. This is o(A(X)log X).

For d≤√X in U_z Q_z, the block Y=X/d satisfies (log Y)²≤z≤4(log Y)². Apply the hypothesis with η=ε/2. The total normalized cost of these branches is O(X^(−ε/2)∏_{p≤z}(1+p^(−1/2−ε/2)))=O(1).

For the other d we need a preliminary estimate that may depend on A(X). In each Y≤X with Y≥1/2, the identity of 353 bounds P in the norm of exponent σ by O_ε(A(X)log(2X)): the higher powers sum to Σ_{p,k≥2}(log p)p^(−kσ)<∞ and the integral of widths costs O(1). The same estimate suffices for L_z S. The operator K_z at this exponent costs X^o(1) even if the child block is small, since the cut z remains frozen at that of the parent. Thus Q_z in each child costs A(X)X^o(1) in its own normalized norm. Scales below 1/2 do not contribute. Transporting back to the parent for d>√X has cost

    Σ_{d>√X, z-smooth} μ²(d)d^(−σ)
       ≤ X^(−ε/4)∏_{p≤z}(1+p^(−1/2−ε/2)) = X^(−ε/4+o(1)).

Hence all of P costs O(1)+o(A(X)log X) in the block X. Reinsert into the identity of 353 and divide by log X−1; at exponent σ the other costs are O_ε(A(X)) before the division. One obtains a constant plus o(1)A(X) for the normalized norm of S_h. Apply block by block for Y≤X, choosing a fixed threshold beyond which the coefficient is ≤1/2, and take the supremum: A(X) is bounded uniformly. Since ε can be arbitrarily small, the inverse implication of 353 gives RH.

**What changes.** 358 eliminates primes of the cofactor by inversion. The same Euler cost applied plainly to L_z S may exceed the absorption margin. Here the term of small exterior primes is extracted before inverting; only the long branches use the envelope A, and the extra weight in those branches pays their Euler cost. The unconditional estimate of the sum over fully sieved products remains.
