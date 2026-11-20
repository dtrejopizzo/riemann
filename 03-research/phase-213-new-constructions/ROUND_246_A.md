# The two readings have a sign and a main term on an interval of slopes

For J,F,δ from 245 and each fixed slope 9/500≤c<1/4 one has, at EVERY starting point t→∞,

    F(0) ∼ F(δ) ∼ H(1/2) δ exp(t/2)/4 > 0.

The verification of zeros up to G=3·10¹² (Z2 of the corpus) is used. Under RH the same law holds for each 0<c<1/4. In particular RH is also equivalent to the FIRST reading being eventually nonnegative at all starting points for each rational 0<c<9/500. Here the quantifier over starting points is stronger than in the two-reading condition of 245.

**Separation of squares.** For u≥0 write S as a smoothed von Mangoldt sum minus squares of primes and powers of order ≥3. The latter cost O((1+u)^C exp(u/3)) by elementary counting (there are O(1+u) exponents). To compute the squares apply the same smoothed explicit formula to half the argument u and to the weight W(2v), with transform H(s/2)/2. On replacing primes by von Mangoldt in that computation the error costs O((1+u)^C exp(u/4)). With the archimedean remainder of the compact formula of 239 one gets

    S(u)=H(1)exp(u)−Σ H(ρ)exp(ρu)−H(1/2)exp(u/2)/2
         + (1/2)Σ H(ρ/2)exp(ρu/2)+O((1+u)^C exp(u/3)).

The sums include multiplicities and admit absolute moments of all orders. For u<0 define the remainder by difference; it is bounded as in 245. RH is not used for this expansion.

**Gap.** After averaging, the rate of exp(su) is Re s−c log(|1+s|/(3/2)). For s=ρ/2 it is ≤1/2−c log(7/(3/2)) by |Imρ|>14. For s=ρ in the verified strip it is ≤1/2−c log(14/(3/2)). For the remaining zeros it is ≤1−c log(2·10¹²)<1/2 if c≥9/500, given that log(2·10¹²)>28. The remainder for u≥0, integrated as in 245, has rate at most 1/3+c log(9/8)<1/2, apart from polynomial factors. The remainder for u<0 costs at most (3/2)^n. Thus there is η>0 leaving all that error in O(exp((1/2−η)t)); the rounding of n only costs a polynomial factor in |s| inside the sums. Under RH all zeros are subject to the bound of the verified strip, at any height.

**Sign.** The main term in exp(u) cancels and the normalisation of the average preserves exactly exp(u/2). For v=0,δ one is left with

    F(v)=H(1/2)exp((t+v)/2)(exp(δ)−exp(δ/2))/2 + O(exp((1/2−η)t)).

The first term is positive and its equivalent dominates the error because log(1/δ)=o(t). If RH fails, 245 selects an arbitrarily small rational slope avoiding ties (start with any interval sufficiently close to zero with positive left endpoint). At it the dominant pair gives readings F(0) of both signs on each stretch of sufficiently large fixed n. This proves the converse of eventual sign.

**Scope.** The pending arithmetic estimate of 245 is proved unconditionally on part of its range, with sign, constant and all starting points. 9/500 is a rounded sufficient bound, not an optimal threshold. The finite verification input only protects slopes bounded away from zero. The argument of bias by squares already appears in 237 for another weight; here it is isolated as the main term after the gamma average and the differences.
