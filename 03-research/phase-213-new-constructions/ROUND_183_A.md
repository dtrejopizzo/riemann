# Mass law required to saturate the comb in the critical band

Let C be the entrywise positive comb of 081. If ||f_T||₂=1 and exp(−T)⟨f_T,Cf_T⟩→1, then, on each half of the window, the measure |f_T(t)|²dt transported by u=T−|t| converges weakly on [0,∞) to (1/2)exp(−u)du. This restricts any sequence of profiles of 181 with κ=1 and W(M_Γ h)≤o(exp T): the archimedean term is ≥exp T−O(1), the polar one is o(1) by 181 and 081 bounds the comb by (1+o(1))exp T. The modulation does not change the spatial density.

**Concentration.** For fixed D between 0 and T, the shifts log n>2T−D link only the two extreme intervals of length D. The truncated left-to-right block has norm ≤||C|| by pointwise domination on moduli by the complete comb. The rest has norm O(exp(T−D/2)) by Chebyshev and partial summation. If l and r are the norms on those intervals, the normalized quotient is bounded by 2lr(1+o(1))+O(exp(−D/2)). For a saturator, l²+r²≤1 and (l−r)²=l²+r²−2lr. Taking first T large and then D large gives tightness in depth and asymptotic mass 1/2 per half. For fixed κ in (0,1), a value W≤0 in the band of 181 still requires 2lr≥κ−O(exp(−D/2))−o(1).

**Transport of the mass.** Put w=2cosh(t/2), K(t,ds) the kernel of C, P(t,ds)=exp(−T)K(t,ds)w(s)/w(t). By 081, P1=1+o(1) uniformly. In the symmetric measure dJ=exp(−T)w(t)w(s)dt K(t,ds), g=f_T/w satisfies

    (1/2)∫|g(t)−g(s)|² dJ=∫|f_T|² P1−exp(−T)⟨f_T,Cf_T⟩=o(1).

For every test φ bounded by one, ∫|f_T|²Pφ−∫|f_T|²φ=o(1) uniformly. Indeed, by symmetry |g(t)|² is replaced by |g(s)|² under the integral with φ(s) with error o(1) by Cauchy–Schwarz and ∫|g(t)|²dJ=O(1). Then P1=1+o(1) is used.

**Limit row.** From t=T−v with fixed 0≤v≤D, a jump to −T+u for fixed a≤u≤b requires n to lie between Y exp(−b) and Y exp(−a), Y=exp(2T−v). On that interval the weight of P per atom is (1+o(1))Λ(n)/Y, uniformly, replacing w by its dominant exponentials at each end. PNT gives mass exp(−a)−exp(−b)+o(1) uniformly in v. From t=−T+v the same statement holds by reflection. From the end on the same side as the target, the shifts to that interval have bounded length and their normalized mass is o(1). The endpoint conventions do not affect the limit. Integrating these rows against |f_T|² using the preceding tightness and invariance gives the claimed law on each bounded interval. Tightness allows passing to weak convergence of finite measures.

081 and 177 exhibit the weight w that asymptotically attains the norm. Here the conclusion concerns the macroscopic density of *all* saturators, even complex ones and without regularity. Closeness in norm to w is not deduced, nor are fine phase oscillations excluded. The condition on saturators does not decide the sign when κ<1 either.

**Independent check.** Concentration, invariance and limit law were cross-checked. The lemma half of paper 47 already estimates a correlation by the norms at two ends. Here the joint norm of 081 is additionally needed, and then the limit rows to determine the distribution within each end. PNT on macroscopic intervals gives weak convergence of depths.
