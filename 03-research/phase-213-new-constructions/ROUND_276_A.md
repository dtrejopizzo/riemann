# At the primes of the band themselves the absolute error exceeds the square-root budget

For the concrete fit of 274–275, let U=⌊√N⌋ and Y=U/(C log²(2N)), taking C sufficiently large in the construction. For all sufficiently large x one has unconditionally

    Σ_(Y<p≤U) log(p) |R(p)| ≫ N^(3/4)/log(2N).

The constant depends on the fixed weight. In particular, an argument that bounds the signed scalar of 275 by summing the modulus of each term cannot reach the sought bound for this construction.

**Forced moment of the continuous response.** Before the pointwise repair write T(y)=Σ_(l≥1) S(ly) for real positive y, with S from 274. At the integers of the band it coincides exactly with R: all repair rows have endpoints ≤Y or ≤6. For y>U one has T(y)=w(y/x) even off the integers, by finite Möbius inversion in the real argument. Write I=∫S. The quadrature of 274 at y=1 gives |I|≪x log²(2N)exp(−c√U); for 0<y≤Y the same periodization gives |T(y)−I/y|≪x log²(2N)y^(−1)exp(−c√(U/y)). Enlarging C, its integral with weight y^(−1/2) up to Y is O(N^(−2)), as one sees by putting z=√(U/y).

For Re s>1 the transform of T is ζ(s)∫S(t)t^(s−1)dt, by a change of variable in each summand. The continuation obtained by subtracting I/y on (0,U) adds the term I U^(s−1)/(s−1) to the transform of the difference. Evaluate at ρ=1/2+iγ₁, the first known critical zero. The terms containing I on [Y,U] and in the continuation are O(N^(−2)). One gets

    ∫_Y^U T(y)y^(ρ−1)dy = −x^ρ H(ρ)+O(N^(−2)).

Here H(ρ)≠0: for the first ordinate, between 14 and 15, λγ₁ log(2)/2 lies strictly between π and 2π, and the uniform factors of total width 10^(−6)log 2 have no zero there either. Their product converges to a nonzero value. Since |y^(ρ−1)|≤1/√Y, we obtain ∫_Y^U |T(y)|dy ≫ √(xY). The Mellin identity is classical; what is needed in addition is to transfer the floor to the effective prime samples.

**Transfer to primes without assuming RH.** For t≥U/4 the formula of 274 gives |S'''(t)|≪x log²(2N)/t⁴. In the inversion part there are only O(x/t) active indices d, all with d/x≤2/t; the derivatives of the cutoff contribute for t comparable to U. The correctors also live at that scale and have amplitude O(x log²(2N)/U). For t<U/4 the function is zero. Summing l³|S'''(ly)| and using l≤2x/y one obtains |T'''(y)|≪x log³(2N)/y⁴ for y∈[Y,U].

Split [Y,U] into cells of lengths between H₀=U^(7/10) and 2H₀. In each cell choose three interior subintervals of length one tenth of the cell, with separation at least another tenth. Each subinterval has prime mass Σlog p ≫H₀ uniformly by 238, since H₀/U^(5/8)→∞ and H₀/Y→0. In each, choose a prime minimizing |T(p)|. Interpolate T quadratically at those three primes. On the whole cell the Lagrange coefficients are O(1) by the separation, and the remainder is O(H₀³ sup|T'''|). After integrating and summing, the contributions of the nodes cost at most a constant times the weighted sum of |T(p)| over the whole band. The total error is

    O(U H₀³ x log³(2N)/Y⁴) = O(U^(11/10) log¹¹(2N)) = o(√(xY)).

This proves the bound at the primes themselves. The result studies the absolute size for this fit; it leaves open the one-sided lower bound for the scalar E(x). Nor does it impose the same obstruction on combinations without the continuous interpolation used here.
