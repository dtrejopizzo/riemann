# Two conjugate saddles and conditional sufficiency of the mass threshold

**Status: PROVED, with independent review of Rouché, the two bands, the phase and the conditional ceiling.** Let κ₀=8(1+log 2)log 4 and p_* the smallest terminal prime of 393. Under RH,

    b(p_*/z−4) → κ₀.

The new part is the conditional ceiling. Without RH one obtains, at each large x, values of both signs of the finite pulse in any terminal strip Y/z∈[4+k₁/b,4+k₂/b], fixed k₁<k₂, with amplitude comparable to that of its complex saddle. The argument allows varying the weight of the last prime continuously from zero to one, as in the definition of p_*.

**Exact saddle.** Write l_p=log p and h_p=1 except for the terminal weight in [0,1]. Let β be the exact positive saddle with those weights, a_p=h_p p^(−β), and G(s)=Ls+(s−1/2)²/2+Σ log(1−h_p p^(−s)), with branches given by the series on Re s>0. Take m equal to the mean of l_p−b with weights l_p a_p/(1+a_p)² and t_c=π/(b+m). By the PNT m→μ of 397 uniformly in the strip. The positive equation is L+β−1/2=Σ l_p a_p/(1+a_p). At s_c=β+it_c, set δ_p=t_c l_p−π=O(1/b). The contribution of each prime to G' is −l_p a_p exp(−iδ_p)/(1+a_p exp(−iδ_p)); its term linear in δ_p sums to zero by definition of m. Hence G'(s_c)=O(L/b²), G''(s_c)=(1+O(1/b))Σ l_p²a_p/(1+a_p)²+1 with sum ≍Lb, and |G'''|≪Lb² on |s−s_c|≤1/b². By Rouché applied to G' against its linear part, there is a unique saddle s_* in |s−s_c|≤C/b³ for C large enough: on the circle the term linear in the displacement dominates both the constant and the quadratic remainder. It is simple and continues as the weight varies. The constants are uniform by compactness of the strip and the PNTs of 395–397, which also apply to every bounded κ (the inner blocks of primes are the same).

**Integrating on the vertical of Re s_*.** The inversion of the finite product allows choosing that vertical directly. In the band |t−Im s_*|≤ε/b² with fixed small ε, Re G''≍Lb and |G'''|≪Lb²; by Taylor in the vertical direction there is a decay ≥cLb(t−Im s_*)². At the scale 1/√(Lb) the cubic error tends to zero. The local contribution with the Mellin normalization is

    Z=(exp(G(s_*))/sqrt(2π G''(s_*))) · (1+o(1)),

with the root of positive real part and uniform complex relative error. The negative band gives the conjugate. For the exterior the proof of 397 is applied with σ=Re s_*: changing β by O(b^(−3)) changes all a_p by a factor 1+O(b^(−2)), so M∼L/b, the limiting mean and the variance are the same. The minimum of the loss at Im s_* equals (π²V/2+o(1))L/b³ because Im s_*=π/(b+m)+O(b^(−3)) and m→μ. Outside both bands there is a margin c_ε L/b³ by 397, independent of the common factor x^σ exp((σ−1/2)²/2)∏(1+h_pp^(−σ)). The Gaussian tail gives the saving of 397. Consequently the pulse is

    [2 exp(Re G(s_*))/sqrt(2π |G''(s_*)|)] · [cos(Im G(s_*)) + o(1)],

since arg G''=o(1). The error here is additive inside the bracket, not relative near a zero. The logarithm of the prefactor differs from log A(Y) by O(L/b³): the loss in the band costs O(L/b³), and moving the positive saddle to σ costs O(Lb·b^(−6)); the logarithms of the prefactors cost O(log L).

**The phase runs through both signs.** When incorporating the prime p with weight λ from 0 to 1, the continuous phase Ψ=Im G(s_*) satisfies exactly

    dΨ/dλ=Im[−p^(−s_*)/(1−λ p^(−s_*))].

The dependence on the saddle disappears by G'=0. At the terminal prime l_p=b+log 4+O(1/b) one has δ=Im(s_*)l_p−π=(π/b)(log 4−μ+o(1)), strictly positive. The derivative is −p^(−σ)sin δ/|1+λ p^(−σ)exp(−iδ)|² and lies between −C/(Lb) and −c/(Lb). When passing to the next prime with weight zero, the product and its saddle are the same. By PNT with classical remainder the strip contains ≍(k₂−k₁)z/b² primes; the error exp(−c√b) is smaller than 1/b. The total variation of Ψ is therefore ≫L/b³→∞. By continuity it reaches even and odd multiples of π, where the previous equivalent determines opposite signs.

**Comparison with S.** Under RH and κ₀<k₁<k₂, 395 gives uniformly log(A/|S|)≥c L/b²: even the monotonicity of the mass and the left endpoint suffice, omitting at most one prime of negligible relative weight. The cost O(L/b³) of the signed saddles does not consume that excess. The constructed phase extremes give values above |S| and below −|S| for the same x. The finite pulse is continuous in the interpolation, hence attains the value S. Thus limsup b(p_*/z−4)≤k₂; letting k₂↓κ₀ and using 394 concludes. With 393 the equivalence between RH and p_*≤(log x)^(2+o(1)) eventually follows. The substantive arithmetic direction remains open: proving that localization without assuming RH.

**Review record.** The definition of m exactly cancels Σl_p a_p δ_p/(1+a_p)². The term i t_c of the Gaussian does not vanish, but it is O(1/b) and is included in G'(s_c)=O(L/b²). On the circle of radius C/b³, |G''(s_c)(s−s_c)|≍CL/b², the constant G'(s_c) costs O(L/b²) and the remainder O(Lb²|s−s_c|²)=O(C²L/b⁴). Choosing C fixed and large and then x large allows Rouché against the linear term, with a single simple root. The series branches are regular on Re s>0 and the unique local root coincides at the junctions when passing from weight1 to weight0 of the next prime.

The real displacement O(b^(−3)) keeps β in the strip of395–397. Its moments and the angular losses keep the same limits; in particular, outside bands of radiusε/b² around the new saddles there is a gap c_εL/b³. Inside, the quotient of the cubic remainder by the quadratic one is O(ε/b), and at the Gaussian scale it is O(sqrt(b/L)). This justifies the complex equivalent with uniform additive error after summing the conjugates; no relative error is claimed near cos Ψ=0. The square root of G'' has argument o(1), so omitting that argument in the cosine costs only o(1).

For the phase, p^(−s_*)=−p^(−σ)exp(−iδ) and log4−μ=2−log4>0. This fixes the negative sign of dΨ/dλ and the size1/(Lb), uniformly in the strip and inλ. The branches and the saddle coincide at each junction, so Ψ is a continuous real phase, not only defined modulo2π. The PNT with classical remainder counts≍z/b² primes in the strip, and its relative error is O(b²exp(−c sqrt b))=o(1); hence the total variation≫L/b³ runs through both signs. UnderRH, the inequality log(A/|S|)≫L/b² uniformly beats the losses O(L/b³), also with a last weight0. Thus the intermediate value theorem attains the exact valueS, and the ceiling for p_* does not depend on rounding the weight nor on knowing the initial asymptotic phase.
