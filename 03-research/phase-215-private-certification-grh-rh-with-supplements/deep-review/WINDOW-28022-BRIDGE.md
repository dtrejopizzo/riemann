# Analytic bridge of the certificate 2.8022

Independent reconstruction of the main review. Source: ROUND_172_A, ROUND_173_A, ROUND_175_A, ROUND_178_A, ROUND_179_A, ROUND_190_A, ROUND_192_A, first paragraphs of ROUND_193_A and ROUND_195_A, lines 3897–3903 and 5167. Papers 47–48 are not used. The verifier and its reproduction are in WINDOW-28022.md.

## Identity of forms that allows the filter to be used

For a zero ρ=β+iγ put δ=|β−1/2|. The symmetry of the zeros converts the spectral distribution into the sum, with multiplicities, of exp(iγt)cosh(δt). Choose χ equal to one on |t|≤6.5 and supported in |t|≤9.5. One obtains a signed tempered measure

`μ=Σρ δ_γ + C(τ)dτ`,

whose term per zero in C is the transform of χ(t)(cosh(δt)−1)exp(iγt), with factor 1/(2π). The corrections of zeros with |γ|≤G=3·10¹² are zero by Z2. The estimates below justify local convergence and the distributional identity; it is first applied to smooth functions of compact support.

Write F=f̂, and Q(τ) for the even real multiplier constructed below. Let ĝ=QF, with supp(g)⊂[−U,U], U=2.85. Since 2U<6.5, the same μ represents W(f) and W(g). Hence

`W(f)=W(g)+Σρ (1−Q(γ)²)|F(γ)|²+∫(1−Q(τ)²)C(τ)|F(τ)|²dτ`.

This is the identity needed. It is not assumed that C is positive, nor is an integral replaced by a sample. On proving 0≤Q²≤1 on the whole line, the atomic sum can be discarded in a lower bound.

## Continuous control of the prime operator

The program enumerates all the prime powers q<exp(2U), since exp(2U)<300, with weight Λ(q)/√q for each positive translation and its reflection. It divides [−U,U] into 2048 cells. If log q expressed in cell units has integer part j, a translation from cell i ends in i+j or i+j+1; the maximum of the two weights dominates the whole interval. Outside the support the weight is taken to be zero. The weights constructed are positive and symmetric, and the coefficients of the translations are rounded up to integers at scale 10⁸.

The check of all the rows implies the Schur bound ‖C_U‖<19.486 for the complete operator of translations. A sampling of quotients is not interpolated. Thus the archimedean term minus that of the primes is dominated from below by the integral of q(τ)|ĝ(τ)|²/(2π), where

`q(τ)=m_arch(τ)−19.486 ≥−26`, and `q(τ)>1/10` when `|τ|≥R`.

The second statement uses the monotonicity of m_arch and its digamma bound at R, verified in the program and paper 46. The polar term of W(g) is treated separately.

## Filter, support, signs and gain

With v=τ/H and b=13, put

`u(τ)=1−sinc(v)²[cosh(b√(1−v²))/cosh b]²`.

The even series of cosh makes this function entire, independent of a choice of root. Its exponential type is at most 2(b+1)/H. On the line 0≤u≤1. For r=R/H,

`u≤a=r²[1/3+2b/(1+√(1−r²))]` if `|τ|≤R`.

The bound comes from 1−sinc(v)²≤v²/3 and from the fact that log cosh is 1-Lipschitz. On 2r≤|v|≤1, sinc(v) and cosh(b√(1−v²)) are positive and decreasing; the check at the endpoint 2r gives u≥7a/2. For |v|≥1, the second factor becomes a cosine and 1−u≤sech²(b)/v²; the other edge check preserves u≥7a/2.

Let d=m/2 be an integer, h(u)=T_d(2u/a−1)/T_d(2/a−1), B=T_d(2/a−1)⁻². The roots r_i of h are in (0,a), and h(1)=1. The expansion

`1/h(1−v)=Σ c_j v^j`

has c_j≥0 and c_j≤(d/(1−a))^j≤m^j, because a<1/2. Define

`Q(τ)=h(u(τ)) Σ_{j=0}^{24} c_j(1−u(τ))^j`, `J=25(2m)^24`.

On a≤u≤1, the truncation of the reciprocal series implies h≤Q≤1. On 0≤u≤a, |h|≤√B and |Q|≤√B J; the check BJ²<1 gives 0≤Q²≤1 on the whole line. From |τ|≥2R on, the identity T_d(cosh x)=cosh(dx) gives

`Q(τ)²≥h(u(τ))²≥B exp(m arcosh 6)/4`.

The degree of Q in u is d+24; hence Q has type ≤(m+48)(b+1)/H. Paley–Wiener, and the boundedness of Q on the line, give supp(g)⊂[−T−(m+48)(b+1)/H,T+(m+48)(b+1)/H]⊂[−U,U]. For smooth f, the multiplication also preserves the necessary smoothness: Q is the transform of a distribution of compact support and finite order. Its thousands of millions of coefficients are not formed numerically.

## Energy leakage and polar term

The energy leakage of f outside [−Ω,Ω], Ω=2R, is at least

`η=[1+(1+TΩ)exp(2TΩ+2)]⁻¹`.

It is checked directly: with d₀=1/T, A=Ω+d₀, J₀(z)=∫_{−d₀}^{d₀}F(z+s)F#(z+s)ds has type 2T. In the strip |Re θ|<π/2, J₀(A sin θ)exp(−2TA cos θ) is bounded because Re cos θ≥|Im sin θ|. On its edges sin θ is real with modulus ≥1, so that |J₀|≤E_out. Three lines gives J₀(x)≤exp(2TA)E_out on [−A,A]. Integrating, 2d₀E_in≤2Aexp(2TA)E_out, which is the bound written. The argument holds for complex f.

Reserving half of q in |τ|>G/2 leaves at least 1/20 in the positive remainder. The unreserved contribution is dominated by

`B[η exp(m arcosh6)/80−26J²] ‖f‖²`.

The logarithmic loss used in the program dominates −log η. At the pole τ=i/2, u is real non-positive and |u(i/2)|≤(b+2)/(2H²). Moreover |1−u(i/2)|≤2. The result is

`|Q(i/2)|² ≤ BJ² exp(m arcosh(1+(b+2)/(H²a)))`.

Both polar moments of f are multiplied by the same Q(i/2). Cauchy–Schwarz gives 2|A(f)B(f)|≤4exp(T)‖f‖². That is why `polar_log` of the program dominates the polar cost in units of B. The check `gain_log > polar_log+10` and `gain_log > 2log J+10` implies that, after paying 26J² and that cost, more than 2B‖f‖² remain: e¹⁰−27>2 and J≥1. The high-frequency reserve is still kept.

## Spectral correction, low and high frequencies

χ is constructed by convolving 1_[−8,8], two uniforms of radius 1/4 and N uniforms of radius 1/N. It is one on [−6.5,6.5], has support [−9.5,9.5] and sufficient finite regularity. For |δ|≤1/2,

`|χ̂(s+iδ)|≤16 exp(9.5/2) min(1,4/|s|)² min(1,N/|s|)^N`.

Each correction is the half-sum of two complex translations minus the real one, divided by 2π. Since (1+|s|)² min(1,4/|s|)²≤25, the prefactor per zero is smaller than 10⁵. Z1 and Z3 give fewer than 100log(3+|j|) zeros per unit interval. For j≥3 one uses N(j+1)−N(j−1), which contains [j,j+1) even if there is a zero exactly at j; it is not presupposed that the ordinates are not integers. The generous bound 100log(3+j) remains valid on taking that interval of length two. The small intervals are covered with Z1 and the negative ones by symmetry. Grouping in l≤|τ−γ|<l+1, at most four intervals are needed. The sums of (1+l)⁻² and log(3+l)/(1+l)² are smaller than 2 and 2log3+3, respectively. One obtains comfortably

`|C(τ)|≤10⁹log(3+|τ|)`.

On |τ|≤H, the zeros that correct have |γ|>G, and |τ−γ|>G−H>2.718N. The same argument adds 2.718⁻ᴺ. The check `low correction` gives |C(τ)|<exp(−D−2), D=120110026806.

For |τ|≥H, write v₀=1−u. Then 0≤v₀≤sech²(b)(H/|τ|)², and z=m sech²(b)<1. The remainder of the reciprocal series gives

`0≤1−Q²≤2z²⁵/(1−z)·(H/|τ|)^50`.

One uses 1−Q²≤2(1−Q), h≤1 and the bound c_j≤m^j. The product with log(3+|τ|) decreases after H. Evaluating it with log(3+G), greater than log(3+H), bounds it by 1/1000. Also 1−Q²<1/2. Since H≥G/2, this whole region has the reserve available: its density is at least (1/2)(1/10)(1/2)/(2π)=1/(80π)>1/1000. Thus it pays the high correction in full. Between G/2 and H the low bound suffices; the reserve is not unduly spent twice.

## Final margin and domain

The check of the denominator ensures B>exp(−D), since cosh(x)≤exp(x). The low correction costs less than 2πexp(−D−2)‖f‖²< B‖f‖². Of the more than 2B kept, more than B remains, and in particular more than exp(−D−1). This is the exponent 120110026807 of the paper.

The inequality was first proved on the smooth core. The density in form norm of paper 46, checked in the analytic audit, extends it to the complete domain. The inclusion of supports extends the result to all 0<T≤14011/5000. Positivity for arbitrary windows is not deduced, nor is the fixed cut-off optimised.

**Verdict of this reconstruction: (a) for the inequality with the inputs Z1–Z3 and the 17 certified predicates.** The text of paper 46 by itself reports the certificate and omits the development; the dossier now provides the argument and the public local program that were missing in the initial reading. The literal comparison of the manuscript must maintain that distinction: there was no developed proof in its lines 1915–1930.

## Cross-review

The theta review read independently the construction notes and this bridge: it confirmed exponential type, reciprocal series, energy leakage through the strip, polar cost, high-frequency reserve and factors 2π. Its observation about endpoints of the counting intervals was incorporated above using N(j+1)−N(j−1). No other failure was detected in this chain. The scope remains the fixed window, with proofs developed in the research annexes, not a global proof of positivity.
