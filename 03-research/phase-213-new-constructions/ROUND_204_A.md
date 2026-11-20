# Linear sufficient height and 500 million real poles

Let G=3·10¹². For any listing with n≤500000000 real poles −v_j, v_j>1/2, counting repetitions, and every complex numerator of degree <n, the complete form satisfies W(f)≥exp(−35000000000)||f||₂². For general order n it suffices that the zeros be verified up to G₀=max(G,10000(2n+8)). This last statement is CONDITIONAL for G₀>G. The requirement of positivity on disjoint bands with hard edges is dropped. Instead, multiplicatively weighted bands are summed.

**Two polynomial inequalities.** On [−1,1] put w_j=(1−x²)^j and ||p||_j²=∫w_j|p|². For degree ≤d and integer j≥0,

    ∫w_{j+1}|p'|² ≤ d(d+2j+1)||p||_j².

Indeed the operator −w_j⁻¹(w_{j+1}p')' is symmetric by parts and preserves degrees, with leading coefficient k(k+2j+1) in degree k. In the basis of orthogonal polynomials of successive degrees it is diagonal. For m=2n+8 and d<m, integrating by parts the cross term in the square of the derivative one obtains

    ∫(1−x²)|(w_m^(1/2)p)'|² + m²||p||_{m−1}²
      = m(m+1)||p||_m² + ∫w_{m+1}|p'|².

By the first inequality the right-hand side is ≤(m+d)(m+d+1)||p||_m², so that ||p||_{m−1}²≤5||p||_m². Now apply the first inequality with j=m−1: ||p'||_m≤√15 m||p||_m.

**Weighted sampling.** For I=[A,4A/3], H=A/3, x=2(t−A)/H−1, put w_A(t)=w_m(x), zero outside I. In the L²(w_A dt) norm differentiation has norm ≤8m/H and the same bound iterates on the derivatives of p. The total variation of w_A|p|² costs ≤36(m/H)∫w_A|p|²: the derivative of the weight costs ≤(4m/H)∫w_{m−1}|p|² and the other term ≤(16m/H)∫w_m|p|² (rescaled weights). There are no endpoint contributions. For A≥3G/4 and t∈I the formula Z3 still has remainder ≤log A and main derivative between 0.14 log A and 0.17 log A. Integrating by parts as in 202 gives sampling constants l log A and h log A, with l=0.14−36m/H and h=0.17+36m/H. The discrete sum counts each ordinate with weight w_A(γ) and with multiplicity.

**Control of the shifts.** Use the approximation of 203 on I and its reflection: U=P Q, degree <m, |U−F|≤10⁻⁴|F| both on the ordinate axis and at the shifted points |δ|≤1/2. The radius ratios used in 203 remain valid for A≥3G/4. On each half-axis, the vector X of values U(iγ) is measured in ℓ² with weights w_A(|γ|). Taylor and the upper sampling inequality applied to each derivative give a relative error in U of at most √(h/l)[exp(4m/H)−1]. For n≤500000000 and A≥3G/4 one has m/H<0.001334, l>0.091 and h<0.219. Including the approximation error of both vectors as in 203, each true shifted vector of F is at norm distance from X at most 0.01||X||. Therefore the real weighted sum dominates 0.97||X||², which in turn, including that factor 0.97, dominates ∫_I w_A(t)|F(±it)|²dt since 0.97·l·log A·(1−10⁻⁴)²>1.

**Reconstruction without edge loss.** Integrate in A with measure dA/A for A≥3G/4. For t≥G the recovered weight is exactly the positive constant
     
    J_m=∫_{3/4}^1 w_{bt}(t) db/b,

independent of t by homogeneity. For t<G one obtains something between zero and J_m. The spectral sum of 201 converges absolutely for each F; the integral of the weight at each ordinate is ≤J_m, justifying the interchange even with signs. After dividing by J_m, all zeros above G have their original coefficient. Below G the missing portion of weight is restored because their contributions are squares. The continuous side is ≥∫_{|t|≥G}|F(it)|²dt. This operation essentially uses that the bands overlap and that the transition zone falls below the verified height.

**Norm and scale.** On the first full band I=[G,4G/3], the final extrapolation argument of 203 for the ORIGINAL numerator gives low/high energy ≤6n²(27·9·10¹²)^(2n). Its logarithm is <34000000000 in the declared range. Plancherel proves the announced floor. For any other order take A≥3G₀/4; then m/H≤4m/G₀≤0.0004 if G₀≥10000m. The same reasoning gives strict sign if verification up to G₀ is available. This improves the quadratic law of 203 to linear. Without that verification the portion of zeros with incomplete weight has no proved sign. Positivity on a band with hard endpoints at linear height is not concluded, nor global positivity.

**Antecedents.** The local rational approximation comes from 203 and the sampling via Z3 from 202. The Jacobi estimate with exponent proportional to the degree avoids the quadratic Markov growth at the endpoints; integration in scale exactly restores the high spectral weights that would be lost by introducing it in a disjoint partition.

The independent audit checked the differentiation and variation bounds, the rescaling factors, the constants for 500 million and the recovery of the weight. Equivalently J_m=∫_{−1}¹(1−x²)^m/(7+x)dx; the same factor appears on both sides and does not reduce the margin.
