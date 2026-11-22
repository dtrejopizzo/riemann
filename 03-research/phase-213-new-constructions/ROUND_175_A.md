# Strict positivity of the full form up to T=6/5

The main result is W_T(f)≥exp(−6000000001)||f||₂² for 0<T≤6/5. The construction is first proved at 26/25; the last section verifies the parameters for 6/5. The two instances gather 22 scalar checks with Arb.

With the unconditional data Z1–Z3 of paper 46, for every admissible test supported in [−26/25,26/25] one has

    W_T(f) ≥ exp(−700000001) ||f||₂².

It is a proof bound, of deliberately conservative size. It is obtained in the original norm and covers any dimension. The application of 174 is detailed because its polynomial majorant alone does not pay the margin at this height.

**Arithmetic density.** In the normalization dν=b(τ)dτ use b=f_w/(2π) of (fw), for an even smooth cutoff, monotone on u≥0, one up to 2.10 and zero from 2.12. The comb has only 2,3,4,5,7,8 with sum of 2Λ(n)/√n less than 6.343. For the archimedean error ∫(1−w)K cos one has the global bound ∫_{2.10}^∞K<1.43 by the geometric series of K, and by parts 2K(2.10)/|τ|<1.43/|τ|. The polar term costs ≤8sinh(1.06)<10.2, or by parts ≤4[2cosh(1.06)−1]/|τ|<9/|τ|. Thus b≥−4 by C₀>−5.373. For |τ|≥R=5000, the lower bound m(τ)≥log(|τ|/(2π))−1/|τ|−1/(2τ²) of the paper gives b≥1/20. The extension is exact up to 2.10.

**Explicit Plancherel leakage.** For functions supported in [−T,T], the fraction of Fourier mass outside [−Ω,Ω], Ω=2R, is at least η=exp(−1800(1+TR)). Here is a computation for these T,R. For g band-limited to [−Ω,Ω] in frequency, ||g||₂=1, use |g^(n)|≤√(Ω/π) Ω^n by Cauchy–Schwarz. In [T,2T] there is a subset of measure ≥T/2 where |g|≤√(2/T)||g||_{L²([T,2T])}. Choose n=ceil(64(1+ΩT)) nodes with separation T/(8n) by successive selection. On [−T,T] the sum of the moduli of the interpolation coefficients is ≤(24n)^(n−1)2^(n−1)/(n−1)! ≤256^n. The remainder is ≤√(Ω/π)(3eΩT/n)^n <1/(4√T), by the integral formula for divided differences (also for complex g). If the interior mass is ≥1/2, the interior supremum is ≥1/(2√T), so the exterior mass fraction of g is ≥256^(−2n)/32. If the interior mass is smaller the bound is immediate. Apply to g the projection of f onto the frequencies [−Ω,Ω]: outside [−T,T], g coincides with g−f, of total norm equal to the square root of the frequency leakage. For ||f||₂=1 a leakage ≥256^(−2n)/64 ≥η follows, also if g=0.

**Mask.** Fix m=20000000, H=20000000000 and φ=1−(1−sinc(τ/H)^16)^m. Its Fourier radius is 16m/H=.016<2.10−2T. Put u=1−sinc(τ/H)^16 and a=8R²/(3H²). On |τ|≤R one has u≤a by Bernoulli and Taylor. On |τ|≥2R one has u≥2a: for |v|=|τ|/H≤1/10, 1−sinc²v≥v²/4 and 1−(1−v²/4)^8≥(7/4)v²; for 1/10≤|v|≤2 use monotonicity of sinc and afterwards |sinc v|≤1/2. Reserve half of b on |τ|>G/2 for the tail, with G=3·10¹². The remaining density b is still ≥1/40 outside R. The remaining part (1−φ)b therefore contributes, per unit of ∫|f̂|², at least
    a^m(2^mη/40−4) ≥ exp(−700000000).
Indeed a>exp(−32) and m log 2−1800(1+TR)>10, so the parenthesis is greater than one.

**Spectral correction at the effective height.** Use the atomic variant of 172 with a special cutoff χ: convolve the indicator of [−5,5] with two uniforms of radius 1/4 and N=10¹⁰ uniforms of radius 1/N, all of mass one. χ=1 at least up to |u|=3.5 and is supported in [−6.5,6.5]. Its finite regularity (more than four derivatives) suffices for the sums and the local distributional identity. For |δ|≤1/2,
    |χ̂(s+iδ)| ≤ 10 exp(6.5/2) min(1,4/|s|)^2 min(1,N/|s|)^N.
This is obtained factor by factor using, for a uniform of radius h, the two majorants exp(h|δ|) and exp(h|δ|)/(h|s|). Each correction for a zero in 172 is the difference of the half-sum of the two complex translations and the real translation, divided by 2π. In particular its absolute value costs ≤10⁵(1+|s|)^(−2) min(1,N/|s|)^N, s=τ−γ. There are corrections only for |γ|>G by Z2.

By Z1 and Z3 there are ≤100 log(3+|j|) ordinates with multiplicities per interval [j,j+1) with integer endpoints (subtract the two main terms of Z3 by the mean value theorem and add their two errors; for |j|<3 use Z1). Summing the preceding majorant gives |C(τ)|≤10⁹ log(3+|τ|). For example group by l≤|τ−γ|<l+1, l integer ≥0: at most four unit intervals, of counting weight ≤400[log(3+|τ|)+log(3+l)], and sum (1+l)^(−2). On |τ|≤G/2 one moreover gains the factor 100^(−N) since N/|τ−γ|≤1/150. Thus ||C|| in that region is less than exp(−700000002). On |τ|>G/2,
    φ |C| ≤ m(H/|τ|)^16 10⁹ log(3+|τ|) < 1/1000,
by monotonicity of the majorant and substitution of G/2. There φ<1/2 and the reserved half of b multiplied by 1−φ is ≥1/80, which pays the whole cost.

**Closing in this window.** The mixed measure of 173 has the exact data on |u|<2T by the support margin .016. The atoms kept with weight φ are positive. The preceding estimates give, as an inequality of forms after integration (not as a pointwise inequality of densities), the announced margin by Plancherel. The extension of the smooth core to the domain is that of 173. This also covers smaller T by inclusion of supports. There is no passage to arbitrary T.

**Arithmetic reproduction.** Run `python3 verify_175.py` from this folder with python-flint. Eleven scalar checks with Arb balls at 160 bits pass. The script verifies constants and margins; the justification of the functional inequalities is in the preceding proof. The cutoffs w (arithmetic, radius 2.12) and χ (spectral, radius 6.5) are distinct.

**Comparison of windows.** In paper 46 thm:log5A and thm:log5W are relevant. In phase 211, ROUND_026_A, theorem 26A.2, certifies λ_A up to 207/200 on the primitive subspace. Here λ_W>0 is obtained at 26/25 for the full form of (W), which also implies λ_A>0. The contact (log 8)/2 is crossed and the comb considered includes 8=2³.

**Actual frontier of the corpus and extension to T=6/5.** Index line l.10974 records the complete reproduction of rStation45 in both parities up to (log 11)/2≈1.1989476364. Hence the first computation at T=1.04 is an alternative proof with explicit margin. The following change of parameters DOES go beyond that frontier:

    T=6/5, R=50000, m=180000000, H=150000000000, k=16,
    φ=1−(1−sinc(τ/H)^(2k))^m,  G=3·10¹²,  N=10¹⁰.

Use an arithmetic cutoff equal to one up to 2.46 and zero from 2.50. To the previous comb 9 and 11 are added: its total mass is <8.53. The tail bound 4 exp(−2.46/2)/(1−exp(−2·2.46)) is <1.2 and also bounds the variation coefficient of the archimedean correction. The polar mass is <13 and its variation coefficient <12. Thus b≥−5 always and b≥1/20 beyond R by the same lower bound for m(τ). The radius 2km/H=.0384 is smaller than 2.46−2T=.06. The cutoff χ of the spectral part is still one up to 3.5, sufficient for the enlarged window.

For the leakage now take Ω=100000 and n=64(1+ΩT). The same computations give η≥exp(−1800(1+TR)). For u=1−sinc(v)^(2k), a=kR²/(3H²), one has u≤a in the low band; for |v|≤1/10, u≥(k/4)(1−1/400)^(k−1)v²≥(k/5)v². On |τ|≥2R this is larger than 2a and the part |v|≥1/10 is covered as before. Moreover a>exp(−32) and m log 2−1800(1+TR)>10. The integrated margin after the high reserve is ≥a^m(2^mη/40−5)>exp(−6000000000). The correction at low frequencies is <exp(−6000000002); at high ones the ceiling m(2H/G)^(2k)10⁹log(3+G) is <1/1000. The rest of the proof does not depend on these parameters. Consequently,

    W_T(f) ≥ exp(−6000000001) ||f||₂²   for all 0<T≤6/5.

The verifier includes both choices of parameters. This extension is local and does not imply uniformity of the procedure as T goes to infinity.
