# Uniform contraction of the observed multiplier in an explicit strip

In 320–321 now take L=log X, D=⌊exp(√L)⌋, N=C₀DL², distributed correction and C₀ sufficiently large. The criterion of 320 remains valid: D=x^o(1) in the block, and in the Poisson estimate of order ⌈L⌉ the quotient DL²/N stays constant. This choice sacrifices the polylogarithmic length of the band. The effective multiplier on the mode x^s is

    K_X(s)=H_X(s) ∫ exp(su)dν_>(u).

There exist c,b>0 such that, unconditionally, for large X,

    sup_(1−b/√log D ≤ Re s ≤ 1) |K_X(s)| ≤ exp(−c√log D).

The bound is simultaneous at all heights. Moreover RH is equivalent to sup_(τ real)|K_X(σ+iτ)|→0 for each fixed σ in (1/2,1). The contraction proved without hypotheses only occupies a shrinking strip next to 1. The action on individual modes is controlled; no norm is being iterated over scale-dependent observations.

**High heights.** Let J=⌈L⌉. On |τ|≥L² each of the first J uniform factors of the tail (indices J+1,…,2J) has |τ|l_i bounded below by a positive constant. By the cardinal sine formula, its characteristic transform has modulus ≤r<1. Including the factor exp(σu) modifies each factor by O(l_i) for 1/2≤σ≤1. The rest of the tail costs ≤exp(1). Thus the filter costs O(exp(−c₁L)). The polynomial H costs at most exp(O(log D)) on the whole strip, by the moduli of its coefficients. The product at those heights is exponentially small.

**Remaining heights.** For |τ|≤L² and 1/2≤σ≤1 one has

    1+H_X(s)=ζ(s)A_D(s)+O(exp(−c₂L)),    A_D(s)=Σ_d a(d)d^(−s).

Use the continuation of the Poisson formula of 321 for f(v)=ψ(v/N)v^(−s). With j=⌈L⌉, the L¹ norm of f^(j) is ≤N^(1−σ−j)[C(j²+|τ|+1)]^j. On [N,2N] Leibniz applies, using the order-two bounds of 320 on ψ; outside that interval the derivative of v^(−s) is integrated directly. The contribution of the nonzero modes, after summing over d, is therefore ≤N^(1−σ) O(log(2D)) [C' D(L²+|τ|)/N]^j, sufficient on choosing C₀. The main integral cancels before continuing in s; at 1 the product ζA_D is regular.

**The line 1.** By the classical Mertens bound M(v)≪v exp(−c₃√log v) and partial summation, the tail from D on of Σ μ(n)n^(−1−iτ) and that of its first derivative are O((1+|τ|)(log(2D))^C exp(−c₃'√log D)). These series give the value and derivative of the reciprocal of ζ on the line as a limit from the right. The distributed correction has a coefficient of the same exponential order by the case τ=0 and Σ μ(n)/n=0. With |τ|≤L² the polylogarithmic factors are absorbed into the exponent. Thus A_D−1/ζ and its first derivative cost O(exp(−c₄√log D)) there. At s=1 the difference is exactly zero; for |τ|≤1 this pays for the simple pole when multiplying by ζ. For 1≤|τ|≤L² it suffices that |ζ(1+iτ)|≪log(2+|τ|) by Euler summation. The announced ceiling on the line 1 is obtained. Hadamard three lines for K_X between 1/2 and 1, with the crude ceiling exp(C log D) at 1/2, preserves an exponential gain up to distance b/√log D if b is small enough.

**Reach up to the critical line.** Under RH, M(v)≪_η v^(1/2+η). For fixed σ>1/2, the same partial summation gives A_D−1/ζ=O_(σ,η)((1+|τ|)D^(1/2+η−σ)) choosing 0<η<σ−1/2; the correction on D<d≤2D also satisfies that ceiling. On |τ|≤L² the height factors, including the polynomial growth of ζ on that line, are D^o(1). Elsewhere the high-height filter applies, and hence the supremum tends to zero. Conversely, a fixed exterior zero ρ would give H_X(ρ)=−1+o(1) by the low-height approximation. The probability ν_> has support shrinking to zero, so K_X(ρ)→−1, contradicting the claim at σ=Re ρ. The case of a known critical zero also gives that limit at the edge 1/2. Extending the unconditional ceiling to each interior line remains open.
