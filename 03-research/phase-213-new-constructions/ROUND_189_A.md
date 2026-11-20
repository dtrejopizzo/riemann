# Strict positivity of the full form up to T=129/50

For 0<T≤129/50, W_T(f)≥exp(−20000000001)||f||₂² on the whole domain of paper 47. The data Z1–Z3 of 175 are used, including the verified height G=3·10¹². The new stretch with respect to 179 is (2.5,2.58].

**Norm via two applications of the comb.** Let s=14, U=log s, x=exp t, w(t)=(1+x)/√x and C the comb compressed to [−U,U]. With L(y)=Σ_{q≤y}Λ(q)/q and ψ(y)=Σ_{q≤y}Λ(q), the first application gives √x Cw=F(x)=xL(sx)+ψ(sx)+L(s/x)+xψ(s/x). In the second one obtains

    √x C²w = Σ_{q≤sx} Λ(q)F(x/q) + Σ_{q≤s/x} Λ(q)F(xq)/q.

C² has a nonnegative kernel and is self-adjoint. It suffices to bound this numerator by (16.72)²(1+x) to obtain ||C||≤16.72 via Schur and ||C²||=||C||². By reflection 1≤x≤s suffices. The internal breakpoints b=q/s,s/q are collected from ALL of [1/s,s]; one must check the external breakpoints and all the transported bq,b/q falling in [1,s]. Between two endpoints the quotient is linear fractional. The inclusive value at each jump dominates both limits, also for products of indicators. 1758 rational endpoints were verified with Arb balls of 192 bits. Two steps preserve the support constraints between successive shifts.

**Application of the leakage and the filter of 179.** Take R=128000000, k=20, even m=1070000000, H=400000000000 and N=10¹⁰. The filter of 178 has additional support km/H and T+km/H<U; 2U<5.5 is kept. With the new norm, the lower bound of the archimedean symbol minus the comb exceeds 1/10 for |τ|≥R. Globally it exceeds −24 by the floor of 178. Putting a=kR²/(3H²), the same scalar filter satisfies u≤a on |τ|≤R and u≥(7/2)a for |τ|≥2R by the argument of 179. If η is the leakage from Ω=2R, the certificate checks m log(7/2)+log η>10 via the lower bound of 179. With half of the high margin reserved, the remaining floor is ≥a^m[(7/2)^mη/20−24]>3a^m. The polar cost is <a^m and a^m>exp(−20000000000). The same spectral extension and its mask from 178–179 give low cost ≤2π exp(−20000000002)<a^m, and high correcting density <1/1000, absorbed by the reserve 1/(80π). The retained atoms have positive or zero weight. Thus the announced floor is obtained in both parities. Inclusion of supports extends the bound to the smaller windows.

**Reproduction.** Run python3 verify_189.py with python-flint. The second row and the need to also transport the breakpoints below one were checked independently. The extension inherits the analytic lemmas and the verified hypotheses of 175–179. The bound is not uniform over all windows.
