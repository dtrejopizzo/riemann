# From the strict window to power blocks of growing order and unequal rates

Put T₀=553/200 and δ₀=exp(−85000000001), from 193. Consider a sequence of finite lists of rates v_j>0, repetitions allowed; let u=min v_j, V=max v_j and n its length. If

    u→∞,    log V=o(u),    limsup Σ_j 1/v_j < T₀,

then on the WHOLE causal space of transforms P(s)/∏(s+v_j), deg P<n, one has W(f)≥(δ₀−o(1))||f||₂² uniformly in the numerators, complex ones included. For example, for n equal poles u≥cn with c>1/T₀ and n→∞ the whole block eventually has strict sign. For any n poles in [cn,Kn] with K fixed and c>1/T₀ the same holds. It is an asymptotic statement; no practical first n is extracted from δ₀.

**Weighted control.** Use the rational orthonormal basis of POWER_THREE_002,

    F_j(s)=sqrt(2v_j)/(s+v_j) B_{j−1}(s),
    B_i(s)=∏_{l≤i}(s−v_l)/(s+v_l).

Triangularity of the denominators and Hardy orthogonality through the modulus-one factors give the whole space, also with multiplicities. Fix S between the limsup of the sum and T₀. Eventually n≤SV. On Re s=−λu, 0<λ<1 fixed, every partial product B has modulus ≤M=exp(2λu S/(1−λ²)), since log((1+x)/(1−x))≤2x/(1−λ²) for x=λu/v_j≤λ. Plancherel on the vertical gives ||exp(λuy) f||₂≤poly(n,V) M for unit f. Indeed the norm of (s+v_l)⁻¹ in dτ/(2π) is [2(v_l−λu)]⁻¹/².

The derivative on the half-line has the same bound: sF_j(s)−sqrt(2v_j)=sqrt(2v_j)[−v_j B_{j−1}/(s+v_j)+(B_{j−1}−1)]. Telescope the last term with B_l−B_{l−1}=−2v_l B_{l−1}/(s+v_l). Each summand admits the previous estimate; Cauchy–Schwarz over the unit coefficients introduces at most another factor sqrt(n). For λ=0 the argument gives unweighted H¹ norms that are at most polynomial. All polynomial factors are exp(o(u)) under the hypotheses.

**Truncation in the form norm.** Choose 2S<L<L'<2T₀ and then λ small so that 2S/(1−λ²)<L. With η=1 fixed, on y≥L the L² norms of f and f' with weight exp(ηy) cost at most exp(−(λu−η)L) M exp(o(u))≤exp(−c'u) with c'>0 for sufficiently large rates. Let χ be a smooth cutoff equal to one up to L and zero from L' on. By the above, ||(1−χ)f||_{H_η}≤O(exp(−c'u)), reducing c' if needed. On y≤L' the weight is bounded and the unweighted norm is exp(o(u)), hence ||f||_{H_η}+||χf||_{H_η}≤exp(o(u)). The bilinear continuity of the full form in POWER_CONFLUENT_BRIDGE_014 §3 implies |W(f)−W(χf)|=o(1) uniformly. After translating the support [0,L'] to the centred window, 193 gives W(χf)≥δ₀||χf||₂². The form is translation invariant, as is the product of the polar moments. The zero extension of the truncation with arbitrary initial trace belongs to the form domain by 014. Its L² norm tends to one, giving the statement.

**What it contributes to the bridge.** 014 §§6–8 already established strong density for moving confluent rates when n/u grows without bound, and the obstruction of arithmetic cuts below 2n/u. POWER_THREE_002 already obtains a fixed margin for minimal rates exponential in n. Here 193 is used in the reverse direction, to prove the sign of complete unequal blocks with a budget of reciprocals and rates even linear in n. The margin is the small window margin. At confluent rate, the dense regime n/u→∞ falls outside the hypothesis. Positivity on this collection does not extend through the 014 bridge to all windows.

**Comparison with 213-085 and audit.** 213-085 already proves positivity for any number of poles with Σ1/v≤1/512, margin 1/4, and even for arbitrary truncations. Its Hardy reflection directly provides ||e^(σy)f||₂≤∏(v_j+σ)/(v_j−σ)||f||₂, also for f' because sF−f(0) belongs to the same space. This recovers the weighted estimate above using only the unweighted derivative bound. The improvement of 194 is the asymptotic budget up to any S<2.765 for the whole datum under the stated scaling conditions. The independent review checked the unequal case and this comparison.

**Provenance correction.** The later cross-check of 195 identifies 213-086 and 213-087 as stronger antecedents: the floor of 194 follows from 087 by passing to the limit in the truncation length and applying the window 193. It is an application of the previous result.
