# The barycentre stays on the positive side up to 10^20

With Z1–Z3 of P46, C(x)>0 for every real 3≤x≤10^20. Moreover C(x)>0.035√x for 10^7≤x≤10^20. The upper endpoint is a limit of this estimate of the barycentre and not a support radius of the Weil form.

**Exact separation.** Let k(v)=(1−v)(3v−1) for 0≤v≤1 and zero for v>1. Set J_d(y)=ΣΛ(n)k((n/y)^d). Then C(x)=J_1(x)−J_2(√x)−R(x), where R contains only powers of odd exponent ≥3, with weight log p. Indeed J_2 eliminates exactly once every even exponent. Since k≤1/3,

    R(x)/√x ≤ (2/3)[x^(−1/6)+x^(−3/10)+(log x)/(2 log 2) x^(−5/14)].

θ(y)≤2y was used: by induction θ(n)≤θ(ceil(n/2))+n log 2 via the central binomial coefficient, sufficient for n≥4, with immediate base cases. After the exponents 3 and 5 there are at most log x/(2 log 2) terms. The ceiling above decreases for x≥10^7.

**Formula with constants.** For d=1,2 and y≥3000 write K_d(s)=−1/s+4/(s+d)−3/(s+2d)=2d(s−d)/(s(s+d)(s+2d)). One has

    |J_d(y)−yK_d(1)+Σ_ρ K_d(ρ)y^ρ| < 50.

Indeed integrate the symmetric explicit formula of ψ against −(d/du)k((u/y)^d) on 1<u<y; the pointwise values of ψ at jumps do not matter. The interchange can be carried out with the primitive of the explicit formula, whose series converges absolutely on compacts, and integration by parts. On integrating the terms u and u^ρ/ρ from zero the two displayed terms come out, by integration by parts and k(1)=0. The cut-off on [0,1] of the main term costs ≤20/y. In the zero term the cut-off adds in modulus at most Σ_(l=d,2d) |a_l| l y^(−l) Σ_ρ 1/(|ρ||ρ+l|), with a_d=4, a_(2d)=−3. The inner sum is <0.048 by the following estimates. The constant −log(2π) of ψ costs ≤7 log(2π), by variation of the polynomial on [0,1]. The term −log(1−u^(−2))/2 costs ≤(10/y)·2 log 2, by the derivative bound 20/y and the integral from 1 to infinity. In particular these budgets fit in 50.

**Zeros.** Up to G=3·10¹² all are verified on the line. Their partial sum Σ|ρ|^(−2) is <0.047 even without assuming RH above G: on the line 2 Re(1/ρ)=|ρ|^(−2) holds, and all other terms 2 Re(1/ρ) are positive in the Hadamard trace 2+γ_E−log(4π). Both ordinates are counted. From G on, Z3 implies for the positive ordinates N(v)≤v log v/(2π) (its error of size ≤log v is absorbed by the linear term). Partial summation ignoring the negative endpoint gives

    Σ_(|γ|>G) |γ|^(−2) ≤4∫_G^∞ N(v)dv/v³ ≤ (2/π)(log G+1)/G < 6.4·10^(−12).

On the line |K_1(ρ)|≤2/|ρ|² and |K_2(ρ)|≤5/|ρ|² using |γ|>14. In the tail, |K_1(ρ)|≤2.01/|γ|² and |K_2(ρ)|≤5/|γ|² by the rational formula and 0<Re ρ<1. Therefore a ceiling for 4/15−C(x)/√x is the sum of

    0.094 + 0.235/x^(1/4) + 6.4·10^(−12)(2.01√x+5) + 100/√x

and the ceiling of R(x)/√x above. Here K_1(1)=0 and K_2(1)=−4/15. On [10^7,10^12] evaluating the increasing term at the right endpoint and the decreasing ones at the left gives less than 0.206. On [10^12,10^20] one obtains less than 0.231. Both leave more than 0.035.

**Initial stretch.** Run python3 verify_247.py --limit 10000019. The procedure of 247 uses only integer bounds of logarithms for each endpoint and concavity for the interval between endpoints. The run completed 664579 strict endpoints between 3 and 10000019. The last prime exceeds 10^7 and gives overlap with the formula. The barrier to continue to infinity is located in the factor √x multiplying the tail of unverified zeros.

**Information that an arithmetic counterexample at larger scale would give.** For x≥10^20, if C(x)≤0, there is a zero with G<|γ|≤Y=100√x log x and Re ρ>1/2+log(10^9)/log x. Indeed, otherwise, on the intermediate band √x can be replaced by 10^9 in the term 2.01·6.4·10^(−12)√x of the budget above. For |γ|>Y the replacement of G by Y in the partial summation costs at most (2.01)(2/π)(log Y+1)/(100 log x)<0.014 in units of √x, because Y≤x/e in this range. The global ceiling above for J_2 is kept. All other decreasing terms can already be evaluated at 10^12. The total cost is less than 4/15, a contradiction. This diagnosis does not presuppose that a violation occurs.
