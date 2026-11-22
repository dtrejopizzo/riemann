# Uniform error when replacing only the prime tail by continuous density

**Antecedents.** P46 prop:sharp and its Chebyshev quadrature separate the continuous density; 213-013/020/021 extract constants by means of moments. Here the error in the jump norm of 031 is estimated simultaneously for all sizes. Let f be constant on the physical cells 1,...,N, extended by zero, H=N+1, and J=Σ_{j=1}^H j|b_j|² with b_j=f(j)−f(j−1) (right-continuous representative). For L≥2 replace, only for n>L, the measure with masses Λ(n)/n by dt/t on (L,∞), in the comb expression 2 Re ∫ conj(f(y)) Σ_{n≥2} f(y/n)Λ(n)/n dy. Denote by a_L the resulting pole-free form, keeping the archimedean side. If ∫f=0, there exists an absolute constant C such that

    |a(Uf)−a_L(Uf)| ≤ C (1+log L)^(−1/2) N J.

The classical quantitative estimate of the prime number theorem is used here, for instance ψ(t)=t+O(t/(1+log t)²). By partial summation, E(t)=Σ_{n≤t}Λ(n)/n−log t−c satisfies |E(t)|≤C/(1+log t) for t≥2: the integrated error converges and its tail is O(1/log t). No square-root scale bound is assumed.

**Exact computation.** Since f(x)=Σ_j b_j 1_{x≥j}, the interior error (sum minus integral for t>L) equals

    Σ_{j≤y/L} b_j E(y/j) − E(L)f(y/L).

This fixes the treatment of the endpoint even if L is a prime power. For the sum, Cauchy–Schwarz gives the bound √J (Σ_{j≤y/L}|E(y/j)|²/j)^(1/2). On each strip r≤log(y/j)<r+1 the sum of 1/j is bounded by 2 by comparison with the integral of 1/x (the ratio of endpoints is ≤e). Summing (1+r)⁻² from r=⌊log L⌋ one obtains O(√J/√(1+log L)). The L¹ norm of f is ≤N√J by the estimate of 031.

For the boundary term, subtract f(H/L) from f(y/L) under the integral against conj(f(y)), by the zero ordinary moment. For 1≤y<H,
    
    |f(y/L)−f(H/L)| ≤ √J (1+log(H/y))^(1/2).

Indeed, the jumps involved lie in (y/L,H/L] and the sum of their reciprocals is ≤1+log(H/y), also if y/L<1. By Cauchy–Schwarz in y, ∫|f(y)|√(1+log(H/y))dy≤||f||₂√(2H)≤2N√J. Multiplying by |E(L)|, incorporating the factor 2 of the comb and summing proves the bound. The inverse moment was not used to estimate the error.

**Size bound on the primitive carrier.** One obtains without sign hypothesis β_N=O(N), with β_N of 031. It suffices to fix L=2. The contact n=2 costs O(||f||₂²) by Cauchy–Schwarz and change of variable. For the continuous density, ∫₂^∞ f(y/t)dt/t=∫₀^{y/2} f(u)du/u=−∫_{y/2}^H f(u)du/u by the inverse moment. For 1≤u≤H, telescoping from H gives |f(u)|≤√J√(1+log(H/u)). For y∈[1,H], the integral of the continuous tail is bounded by C√J(1+log(2H/y))^(3/2). Its pairing with f costs O(NJ) by Cauchy–Schwarz, using ∫₀ᴴ(1+log(2H/y))³dy=O(H). Finally m≥m(0) and ||f||₂²≤NJ. The error already proved completes the bound.

By 031, o(N) on a cofinal subsequence would indeed suffice. The current estimate controls the effect of the discrete minus continuous tail, but the sum of the prime block up to L with the continuous density and the archimedean part still requires a signed lower inequality. The tail approximation is preserved when modifying finitely many weights and taking L after the last change. PROVED after independent mathematical audit.

## There are arbitrarily large cuts whose hybrid form is negative

Applying P46 prop:sharp to the hybrid comb, its global symbol on the primitive subspace is

    h_L(t)=m^sharp(t)−2 Σ_{n≤L} Λ(n)cos(t log n)/√n + 2∫₁ᴸ cos(t log x)dx/√x.

Indeed the discrepancy relative to the full density only has support on the prefix. The form is the integral of this symbol against |F̂|²/(2π). If h_L(0)<0, the primitive packets of P46 thm:kappa centred at zero frequency give a negative test as their window grows (L fixed). For L=2 one obtains b−√2 log 2+4(√2−1)<0, b=m^sharp(0)=m(0)+4. The obstacle persists for arbitrarily large cuts, as follows.

Let h(L)=h_L(0)=b+4(√L−1)−2Σ_{n≤L}Λ(n)/√n, also defined for 1≤L<2 by the same formula. The Laplace transform of h(exp x) on x≥0 equals

    [b + 2/(z−1/2) − 2S(z+1/2)]/z,    Re z>1/2.

The pole of the numerator at 1/2 cancels against the residue 1 of S at s=1, and the apparent pole at z=0 cancels by 030, 2S(1/2)=m(0). It thus extends locally along the whole real axis down to z=−1/2 inclusive. To verify this last endpoint, Z(s)=Σ n^(−s) satisfies by partial summation, initially for Re s>1,

    Z(s)=s/(s−1)−1/2−s∫₁^∞ ({u}−1/2)u^(−s−1)du.

The primitive from 1 of the function in parentheses is bounded; an integration by parts extends the last integral to Re s>−1. In particular Z(0)=−1/2, so S=−Z'/Z is regular near zero. For the other positive real points of s the alternating series of 028 is used.

If h had weak constant sign eventually, the tail of h(exp x) or of its opposite would be nonnegative. The Landau argument of 028 excludes a real abscissa of convergence in [−1/2,1/2]. Hence ∫₁^∞ |h(L)|dL/√L would be finite by evaluating the Laplace integral at z=−1/2. But on each interval (n,n+1) the slope is 2/√L. Pair L∈(n,n+1/2) with L+1/2: the sum of the two moduli is at least their difference, ≥1/√(n+1). It follows that the integral of |h(L)|/√L over that cell is ≥1/(2(n+1)). The sum diverges.

There are thus strictly positive and negative values for arbitrarily large real cuts. In particular there are also arbitrarily large integer cuts with h(n)<0, by growth on [n,n+1). Global positivity of the hybrid for all large cuts is discarded; the possibility of a favourable cofinal subsequence, and the sign for the original comb, remain open. The proof is an application of the classical oscillation method; the direct antecedent in the corpus for the transform of crossings is N_BUILD_015_XI_LANDAU, §§1–2. PROVED after independent mathematical audit.
