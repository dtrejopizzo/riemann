# A one-sided arithmetic criterion at fourth powers

Let S₂=Σ_{n≥2}Λ(n)/n²=−ζ′(2)/ζ(2). The global sign of P46 is equivalent to the existence of a finite constant C such that, for every integer j sufficiently large and x=j⁴,

    Σ_{2≤n≤x} [1−(n/x)³] Λ(n)/n² ≤ S₂ − 3/(2x) + C/x^(3/2).

Only a finite sum appears for each j. The allowed error and the main term are part of the condition; mere convergence to S₂ does not suffice.

**Physical form of the translated trace.** In 038, the inverse transform of 1/(t²+9/4) is exp(−3|r|/2)/3. Put x=exp r≥1 and define

    Q(x)=x^(−3/2) Σ_{n≤x} nΛ(n) + x^(3/2) Σ_{n>x} Λ(n)/n².

Then exactly

    k(log x)=H(log x)+[(3/2)√x−Q(x)+x^(−3/2)(1/2−S₂)]/3,

where H is the inverse transform of m♯(t)/(t²+9/4) and is bounded by absolute integrability. Indeed, each cos(t log n) produces two exponentials centred at ±log n. The first, with the weight of the contact, gives the two pieces of Q; the second gives x^(−3/2)S₂. The continuous density produces the same expressions with dn on [1,∞) instead of the masses Λ(n); its two values are (3/2)√x−x^(−3/2)/2 and x^(−3/2). The formula follows first with a cut and then by absolute convergence at fixed x and by 038. In particular an upper bound on k(log x) is equivalent, up to a uniform additive constant, to Q(x)≥(3/2)√x−C. Rearranging Q and dividing by x^(3/2) gives the inequality of the statement.

**Why fourth powers suffice.** For r>0 and in the sense of distributions,

    (9/4−∂ᵣ²) k = 2 cosh(r/2) − K(r)/2 − Σ_{n≥2} Λ(n)/√n · δ_{log n},

with K(r)>0 the Lévy kernel of P46. This is obtained by multiplying the transform at the cut by 9/4+t² and passing locally to the limit: the symbol m contributes −K/2 away from the origin, the correction m♯−m contributes exp(−r/2), and the density of the continuous comb contributes exp(r/2). The prime atoms only decrease the right-hand side. Let r_j=4 log j. If k(r_j)≤M eventually, increase M until it is nonnegative. On a cell [l,h]=[r_j,r_{j+1}] the barrier

    V(r)=M+cosh(h/2)(r−l)(h−r)

dominates the endpoints and satisfies (9/4−∂²)V≥2cosh(r/2). By the weak maximum principle on the interval, k≤V (equivalently use the positive Dirichlet Green kernel for the difference measure). The excess over M is at most cosh(h/2)(h−l)²/4, uniformly bounded: cosh(h/2)≤(j+1)² and h−l≤4/j. Thus control of the samples implies a finite upper bound on the whole half-line.

**Closing the equivalence.** If the sign holds, 038 gives k(r)≤k(0) for all r and in particular at the samples. Conversely, the arithmetic inequality at the samples gives an eventual bound k(r)≤M′ by the two previous steps. The Landau argument of 038 applies to M′−k just as to k(0)−k: changing the constant only changes its Laplace transform by a multiple of 1/z. Poles in Re z>0 are excluded and the sign is obtained by the Weil criterion. The equivalence does not prove the arithmetic inequality for all j. Checking a finite list of fourth powers does not suffice either.

**Purely arithmetic interpolation.** The reduction of the half-line to fourth powers is also obtained without distributions. With y=x^(−3), the left-hand side of the inequality is P(y)=Σ(1−n³y)₊Λ(n)/n². It is convex, being a locally finite sum of positive parts of affine functions with nonnegative coefficients. Hence P lies below the chord between y_{j+1}=(j+1)^(−12) and y_j=j^(−12). The comparison term F(y)=S₂−(3/2)y^(1/3) has second derivative y^(−5/3)/3. On that cell its chord exceeds F by at most ||F″||∞(y_j−y_{j+1})²/8=O(j²⁰ j^(−26))=O(j^(−6)). The admissible errors at both endpoints are likewise O(j^(−6)), which is O(√y) uniformly on the cell. Thus P(y)≤F(y)+C√y at the samples implies the same inequality with another constant on the whole interval. This is the elementary step in which the sign of Λ is used.

Targeted cross-check: the generator of POWER_CONE_001 and P46 prop:sharp are antecedents of the exponential kernel. The screw-function checkpoints of the index L72 use prime-power events and another function; their equivalence is not used. The formula for Q and the barrier argument received independent review.

## The same sum at powers of any fixed exponent

Let m>0 be fixed. The equivalence of the statement remains true, with the same weights and the same error scale, when replacing x=j⁴ by x=j^m. For arbitrarily large integer m they remain sums over integers. The exponent four was sufficient for the elementary proof by convexity. The improvement that follows uses the representation by zeros and must therefore be read as an analytic reduction, outside an exclusively arithmetic proof of the sign.

Let b=3/2, w=ρ−1/2 for each nontrivial zero with multiplicity and θ=sup Re w∈[0,1/2]. For r≥0 one has

    k(r)=Σ_w exp(wr)/(b²−w²).

Indeed, the Hadamard factorization of the even entire function ξ(1/2+z), of order one and without zero at z=0, gives L(z)=(ξ′/ξ)(1/2+z)=Σ_{pairs ±w} 2z/(z²−w²). The exponential linear factors cancel when pairing and parity eliminates any constant term in L. The trace of 038 gives k(0)=L(b)/b. Inserting by pairs into [z k(0)−L(z)]/(z²−b²) one obtains exactly Σ_w 1/[(b²−w²)(z−w)] in Re z>1/2. The proposed time series converges absolutely and locally uniformly, since Σ_w(1+|w|)^(−3/2)<∞ by order one. Its transform is the expression of 038, whence the equality by uniqueness of Laplace.

For 0≤h≤1, use |exp(wh)−1|≤C min(1,|w|h)≤C√(|w|h), since Re w≤1/2. One obtains the estimate that matters between samples:

    |k(r+h)−k(r)| ≤ C exp(θr) √h.

At r_j=m log j, the separations are O_m(exp(−r_j/m)). If the samples are bounded above, one gets on the whole half-line k(r)≤C_m exp(ηr) with η=max(0,θ−1/(2m)). If θ>0, then η<θ. Apply Landau to C_m exp(ηr)−k(r), increasing the constant on an initial piece. Its transform has no real singularities in (η,∞), since L is regular there and the point b is removable in the formula of 038. The abscissa of convergence is at most η. Consequently the transform of k is holomorphic in Re z>η, a contradiction with some pole w of L in that half-plane. Such a pole exists by the definition of supremum if η<θ, even when the supremum is not attained. Hence θ=0 and the sign holds by P46. The converse implication is inherited from 038. The physical formula of 039 turns the sample bounds into the announced finite inequality.

The same argument quantifies what would be lost on the mesh if the sign failed. Define E(x)=x^(3/2)[Σ_{n≤x}(1−(n/x)³)Λ(n)/n²−S₂+3/(2x)]. Then E(x)=3k(log x)+O(1) uniformly for x≥1 by the physical formula. For each fixed m,

    limsup_{j→∞} log(1+max(0,E(j^m)))/log(j^m) = θ.

The upper bound comes from the absolutely convergent series. If the upper limit were less than θ, take an intermediate exponent η₁<θ bounding the samples. The previous interpolation bounds the continuum by a multiple of exp(max(η₁,θ−1/(2m))r), and the contradiction is repeated. For θ=0 the upper bound and nonnegativity of the quotient suffice. This law identifies an exponent; it does not determine its value unconditionally. No finite table certifies the uniform estimate.

## Control within the sandbox: exact limit of interpolation by convexity

For each integer m>4 there exist nonnegative arithmetic weights w_n for which the sum of 039 with Λ replaced by w is *exact* at x=j^m but its intermediate excess, divided by x^(−3/2), is unbounded. Thus the preceding analytic extension is not a consequence of positivity of the weights alone.

Fix J≥2, y_j=j^(−3m), S=(3/2)J^(−m) and F(y)=S−(3/2)y^(1/3). Let P be the linear interpolation of F between the y_j for j≥J, extended by zero to y≥y_J. It is convex decreasing, with P(0+)=S. At each node y_j put n=j^m and w_n equal to the upward jump of P′ divided by n; put zero at the other integers. Then P(y)=Σ(w_n/n²)(1−n³y)₊: both sides have the same slope jumps, are linear between nodes and vanish to the right of the last one. For each y>0 only finitely many terms intervene, and as y decreases to zero monotone convergence gives Σw_n/n²=S.

At the midpoint of each cell, the difference chord minus F lies between the minimum and the maximum of F″ on that cell multiplied by (y_j−y_{j+1})²/8. Since F″ is comparable to j^(5m) and the width is comparable to j^(−3m−1), the excess divided by √y is comparable to j^(m/2−2), which diverges. This countermodel proves the optimality of the exponent four for the class of nonnegative weights without further restrictions. It does not satisfy the divisor identities of Λ and is not a counterexample to the sign.

The README of phase 213 restricts the admissible mechanisms to arguments on the explicit form. Hence the extension to every mesh j^m via the zeros is recorded only as an external analytic comparison. The countermodel and the interpolation at fourth powers are the elementary parts of this cross-check.

**Also with uniformly bounded weights.** On each coarse cell [l,h] of length d, add to F a bump ε d²(min_[l,h] F″) φ((y−l)/d), with φ smooth nonnegative of compact support in (0,1) and φ(1/2)>0. Choose ε||φ″||∞≤1/2. This modified function is convex, coincides with F at the coarse nodes and its second derivative stays between F″/2 and 3F″/2. Now interpolate it linearly at *all* the nodes y=n^(−3), including the coarse ones; extend by zero from y_J. Convexity is kept at the endpoint because the derivative there, before the extension, is negative. At each interior node the slope jump is bounded by the supremum of the second derivative on the two adjacent fine cells times their total length: O(n⁵)O(n^(−4))=O(n). Hence the weights reconstructed by the same procedure satisfy 0≤w_n≤C_{m,J} uniformly. The single junction with the extension has a finite jump. The fine interpolation dominates the modified convex function and therefore keeps at least the excess of the bump at the coarse midpoint. The sum of normalized weights is still S by monotone convergence. Even adding uniform boundedness of the weights does not rescue the interpolation argument on meshes m>4.

## Falsification threshold with explicit constant and bias of the squares

Write E(x)=(3/2)√x−Q(x), k₀=k(0), S₂=−ζ′(2)/ζ(2) and c♯=1/2−γ_E−log(2π). A necessary consequence of the sign, at **each** x>1, is

    E(x) ≤ 3k₀ − (c♯+1/2−S₂)x^(−3/2) − R(x),

    R(x)=x^(−1/2)[z atanh z + (log(1−z²)+z²)/(2z²)],     z=1/x.

In particular, using E(x)=x^(3/2)[Σ_{n≤x}(1−(n/x)³)Λ(n)/n²−S₂+3/(2x)], the comparison requires a finite sum and specified constants. A rigorous violation at a single x would certify a negative direction by 038. Conversely, proving this inequality for all sufficiently large x=j⁴ suffices by 039. Dropping R(x)>0 gives a weaker threshold that would also suffice to falsify the sign if exceeded. No certified violation has been observed here.

**Evaluation of the archimedean term.** Let b=3/2 and a_k=k+1/4. In P46 prop:sharp separate partial fractions after dividing the symbol by t²+b². The inverse transform is

    H(r)=(c♯/3) exp(−br) + Σ_{k≥1} exp(−2a_k r)/(4a_k²−b²),       r>0.

The coefficient of the first term comes from the even analytic extension of m♯ at ib: [ψ(2)+ψ(1/2)]/2−log π=c♯. The separation can be done in partial sums; the remaining coefficients are summable and the series of P46 divided by t²+b² converges in L¹ by monotonicity of its nonconstant summands and integrability of the limit. Since 4a_k²−b²=(2k−1)(2k+2), three times the series at r=log x sums to R(x) by the series of atanh and log(1−z²). Substituting into the physical formula of this round and using k(r)≤k₀ gives the threshold.

**Which part of the error comes from proper powers.** Denote by Q_p the same expression as Q restricting n to primes, with weights log p. For the squares, putting y=√x, the two pieces are y^(−3)Σ_{p≤y}p²log p and y³Σ_{p>y}log(p)/p⁴. By the prime number theorem θ(y)∼y and partial summation, each tends to 1/3. For exponents k≥3, the accumulated mass of the weights up to t is O(t^(1/3)): by Chebyshev, the term k=3 is O(t^(1/3)) and the remaining ones sum to O(t^(1/4)log t). By partial summation their two contributions to Q are O(x^(−1/6)). We conclude

    Q(x)−Q_p(x)=2/3+o(1).

Hence, if the sign holds, limsup_{x→∞} [(3/2)√x−Q_p(x)] ≤ 3k₀+2/3. At a finite x the bias 2/3 does not replace an error control for the proper powers. The separation of squares is the classical difference between ψ and θ, here evaluated with the exact weight of 039. The free constant of the uniform criterion absorbs the bias: the pending problem lies in the prime term. Formulas and scope independently reviewed.

NUMERICAL. At x=j⁴ for j=2,...,32 the finite sum was evaluated with a sieve up to 1 048 576, accumulating ΣΛ(n)/n² and ΣnΛ(n) with 50 working decimal digits. The observed minimum of full threshold minus E was 0.09311636354106026, at j=20. It is a check of the formula without interval arithmetic; it is not used in the proof nor extrapolated to other j.

## Continuous certificate of the threshold on 16≤x≤2²⁰

On the whole real interval [16,1048576] the difference between the previous explicit threshold and E(x) is greater than 1/1000. This decides the scalar trace test on the interval; positivity of the full form requires more.

**How the continuum is covered.** Let l,h be cell endpoints and q=max(0,E(l),E(h)). For y=x^(−3), P convex, F=S₂−(3/2)y^(1/3) and E=(P−F)/√y. The chord of P lies below the chord of F plus q times the chord of √y. The latter function is concave. The interpolation remainder bound for F thus gives, for all l≤x≤h,

    E(x) ≤ q + h^(13/2)(l^(−3)−h^(−3))²/24.

Indeed sup F″=h⁵/3 and 1/√y≤h^(3/2). By the positive series of R one has R(x)≤x^(−5/2)(log 2+1/2), summing its coefficients through the limit of the closed formula at x=1. The certificate verifies −16(c♯+1/2−S₂)>log 2+1/2, so the full threshold at x≥16 is at least 3k₀.

**Reproduction.** Run with Python 3 and python-flint 0.9.0 the file `verify_039_interval.py` in this folder. The mesh has rational endpoints (j/32)⁴ for j=64,...,1024. An integer sieve includes each prime power with its weight log p, and the endpoints of the prefixes are determined by integer comparison. Arb at 160 bits encloses S₂ through the quotient of the derivative and value of ζ at 2, the logarithms, both accumulations and the interpolation errors. On each cell it requires with certified strict inequalities that the maximum of both endpoint errors and zero, plus the remainder, lie below 3k₀−1/1000. Reproduced output: PASS, 960 cells, 82267 prime powers. No global sign is presupposed for this computation.
