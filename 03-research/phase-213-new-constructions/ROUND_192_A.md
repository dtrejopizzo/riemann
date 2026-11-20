# Strict positivity up to T=68/25

For 0<T≤68/25 and every f in the domain of paper 47, W_T(f)≥exp(−22000000001)||f||₂². The height of verified zeros is still G=3·10¹². The stretch (2.68,2.72] is added.

**Inner filter with transition band.** Fix H=G/2, b=29, v=τ/H and

    u(τ)=1−sinc(v)² [cosh(b√(1−v²))/cosh b]².

The even series of the hyperbolic cosine removes the choice of complex root. For v=x+iy, |Re√(1−v²)|²=(|1−v²|+1−x²+y²)/2≤1+y². Together with the integral representation of sinc this gives growth at most a constant times exp(2(b+1)|Im τ|/H) for u. On the line 0≤u≤1. For the outer polynomial h of 190, of degree m/2, h(u)f̂ is entire of type ≤T+m(b+1)/H and of class L² on the line. The Paley–Wiener theorem preserves the required support. The multiplier is even, so both polar moments are multiplied by the same real value.

**Three regions and pole.** If r=R/H and |v|≤r<1, then

    u≤v²/3+2b v²/(1+√(1−r²)) ≤ a=r²[1/3+2b/(1+√(1−r²))].

Indeed 1−sinc(v)²≤v²/3, and log cosh is 1-Lipschitz, so the deficit of the second squared factor is ≤2b(1−√(1−v²)). For 2r≤|v|≤1 both unsquared factors are positive and decreasing in |v|, and Arb verifies u(2R)>7a/2 (argument in units of τ). From |v|=1 on the hyperbolic factor becomes a cosine and 1−u≤sech²(b)/v². In particular u≥7a/2 still holds. At the pole v=i/(2H), with y=1/(2H), one has sinh(y)/y≤exp(y²), and log cosh(b√(1+y²))−log cosh b≤by²/2. Hence |u(i/2)|≤exp((b+2)y²)−1≤(b+2)/(2H²). The last step uses (b+2)y²<1.

**Certification of the form.** Use T=68/25, U=2749/1000, R=315000000, m=1390000000 and N=10¹⁰. One obtains T+m(b+1)/H=2.7478<U and 2U=5.498<5.5. The step weight of 191, recomputed on this window, verifies in integers the 2048 rows for ||C||≤17.62. The archimedean margin outside R exceeds 1/10; the global floor exceeds −24. Now apply the proof of 190 with the indicated a. In units of B=D_{m/2}(2/a−1)^(−2), the gain after reserving the high density is ≥η exp(m arcosh 6)/80−24; the polar cost is ≤4 exp(T) exp(m arcosh(1+(b+2)/(H²a))). The certificate checks the absorption and B>exp(−22000000000).

For |τ|≥H, the outer mask satisfies 1−P≤2m sech²(b)(H/|τ|)² by the derivative of 190. This quadratic power suffices for the high correction: log(3+t)/t² decreases for t≥H, and at the start 2m sech²(b) times 10⁹log(3+G) is <1/1000. The low cost is ≤2π exp(−22000000002)||f||². The reserve 1/(80π) and the nonnegative sign of the retained atoms complete the proof as in 190; inclusion of supports is applied. The outer filter is still the Chebyshev one of 190; the saving in support comes from the inner function, which suppresses the tail from G/2 on through sech² b.

**Reproduction.** Run python3 verify_192.py with python-flint. The result is internal to the project and keeps the spectral and extension inputs of 175–179.
