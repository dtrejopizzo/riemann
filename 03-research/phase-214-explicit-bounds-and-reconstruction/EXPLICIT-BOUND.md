# An explicit bound in each window from the positive representation

**Proposition.** Take as input the spectral conclusion of paper 46: every non-trivial zero of ζ has real part 1/2. In the normalisation of its complete form, for every T>0 and every function of its domain supported in [−T,T] one has

    W_T(f) ≥ exp(−K) ||f||₂².

To compute K one may replace T by max(1,T). We write s=T+1, U=T+1/100, n=ceil(2U/log 2) and define

    L = 2 log(2) ∑_{k=1}^n 2^k / √(2^{k−1}),
    R = exp(L+5),    K = 22sR log(9680000 s²).

In particular exp(−10^529) works at radius 5 and exp(−10^67360) at radius 10. These are deliberately small floors in the original norm. The deduction uses the explicit formula of Row C and the zero-localisation result of Row D with the inputs indicated there. It is different from extending the fixed-height certificate 3·10¹². The role of the localisation is seen in a single comparison inequality.

## Proof

By inclusion it suffices to take T≥1. We normalise ||f||₂=1 and begin with the smooth kernel. Let m=ceil(10sR), H=200m, a=R²/(2H²). In frequency we apply the multiplier

    u(t) = 1 − sinc(t/H)² / sinhc(1/(2H))²,     ĝ(t)=u(t)^m f̂(t),

where sinc(x)=sin(x)/x and sinhc(x)=sinh(x)/x with value one at zero. On the real line 0≤u≤1. At ±i/2 one has exactly u=0. The inverse Fourier transform of sinc(t/H) is a uniform distribution of radius 1/H. By convolution, g is supported in [−U,U] since 2m/H=1/100, and its two Tate moments are zero. The spectral expression of paper 46 gives

    W_T(f) − W_U(g) = ∑_γ (1−u(γ)^{2m}) |f̂(γ)|² ≥ 0.                 (1)

This comparison preserves the complete form and uses all the ordinates, with multiplicity.

**Arithmetic estimate of g.** The prime operator on [−U,U] has norm at most 2∑_{q≤exp(2U)} Λ(q)/√q ≤ L. Indeed, for j=2^{k−1}, every prime power in (j,2j] contributes its prime logarithm to the logarithm of (2j choose j), by the formula for the valuations of the factorial. The other summands in that formula are non-negative and (2j choose j) ≤ 2^{2j}. This explains the terms of L. The archimedean multiplier M of Row D satisfies M(t)≥M(0)>−6, as well as M(t)≥log(|t|/(2π))−1/|t|−1/(2t²) for |t|≥R. By the definition of R, M−L≥1 there. The polar cost of g is zero.

**Filter.** On |t|≤R one has u≤a: use 1−sinc² x≤x²/3 and 1−sinhc(y)^(−2)≤y², a consequence of sinhc(y)≤exp(y²/2) by comparison of series. The result is u≤(R²/3+1/4)/H²≤a. On |t|≥4R one has u≥4a. For 4R/H≤|x|=|t/H|≤1, the alternating series gives sinc(x)≤1−x²/7 and hence 1−sinc² x≥x²/4. On 1≤|x|≤2 use the decrease of sinc and sin(1)²<3/4; from 2 onwards use |sinc x|≤1/2. In both cases 1/4>4a since H≥2000sR.

**Leakage.** If Ω=4R, the fraction of the mass of |f̂|² in |t|>Ω is at least η=[1+(1+TΩ) exp(2TΩ+2)]^(−1). We recall the proof. Let l=1/T and A=Ω+l. The integral J(z) of f̂(z+y) conjugate(f̂(conjugate(z)+y)) for −l≤y≤l is entire of type 2T. On the real rays |x|≥A it is bounded by the exterior mass E. In the strip |Re θ|<π/2, J(A sin θ) exp(−2TA cos θ) is bounded, since Re cos θ≥|Im sin θ|; on the edges it has modulus ≤E. By three lines J(x)≤E exp(2TA) on [−A,A]. Integrating there counts each interior frequency over a length 2l, giving 2l E_in≤2A exp(2TA) E. This proves the inequality. In particular −log η≤8TR+2+log(2(1+4TR))≤12sR (use log(1+x)≤x).

The arithmetic expression, Plancherel and the three regions above imply

    W_U(g) ≥ a^{2m} [4^{2m}η − (L+6)] ≥ a^{2m}.

In the intermediate band R≤|t|≤4R the minorising integrand is non-negative. For the last comparison, 2m log 4−12sR>15sR and exp(15sR)>L+7. Finally m≤11sR and a≥1/(9680000s²), whence a^{2m}≥exp(−K). We apply (1) and pass to the domain by density in the form norm. The floor holds in each window; it depends on T.

## Relation to the finite-height certificate

The global conclusion of paper 46, by itself, gives the floor zero. Here it allows one to remove the correcting density of the earlier phases and to use a contractive filter that annihilates the two poles exactly. The power filter and the leakage have antecedents in phase 213, rounds 176–179; phase 176 already gives an asymptotic law under growing verification heights. This note gives parameters in all windows and specialises them at 5 and 10.

If only the verified height G is used, (1) acquires summands for the exterior zeros evaluated at complex frequencies; the real contraction does not give the sign of those summands. To obtain the same radii with those inputs it would suffice to bound below their total contribution to the difference by −(a^{2m}/2)||f||². None of the numerical evaluations in this folder establishes that inequality.

Sources in the repository: paper 45, explicit formula; paper 46, conclusion and section on the inputs of the proof; annex, theorem labelled i4:thm-final and its four hypotheses. Phase 213, ROUND_195_A, inverse audit of radius 5: the estimate of the norm of the prime operator with the earlier height already meets an obstruction at U=3.156. The present deduction does not require auditing the arithmetic inputs of the annex again.

**Reproduction.** Run python3 verify_bounds.py with python-flint. The program encloses log10 K by means of Arb; the functional inequality is justified above.
