# Sufficient height law for growing windows

Let A_T=Σ_{2≤n≤exp(2T)} 2Λ(n)/√n, the mass of the comb in the window (including an extreme contact only changes the convention there). For all sufficiently large T, if all zeros up to
    G(T)=100 exp(A_T+5T)
lie on the critical line, W_T is strictly positive in L² norm. More precisely, under that hypothesis W_T≥exp(−C T² exp(A_T))I with C absolute. The parameters grow with T and the proof controls their growth. By PNT and partial summation A_T=(4+o(1))exp T. Consequently, for every fixed ε>0 and sufficiently large G, a verification up to G gives positivity for every window
    0<T≤log log G−log 4−ε.
The second statement is obtained at the extreme window and then by inclusion. It is an asymptotic law, not a numerical estimate better than 175 for G=3·10¹².

**Comb without multiplicative overhead.** Let h=exp(−2T). Use an even monotone arithmetic cutoff, one up to 2T+h and zero from 2T+2h. The widening adds at most four integers for large T, since exp(2T)(exp(2h)−1)→2. The additional contribution is O(T exp(−T)). As in 175 the variation of the polar term costs O(exp T) and that of the outer archimedean term O(exp(−T)), independently of the slope of the cutoff, by monotonicity and integration by parts. Its density b satisfies b≥−M with M=O(exp T) by the mass bounds and b≥1/20 from R=100 exp(A_T) on by the lower bound for the digamma: log(R/(2π))−A_T=log(100/(2π)), while the additional errors there are o(1).

**Leakage parameters.** Take k=ceil(log R), m=ceil(4000TR), H=100km/h, G=R exp(5T). The Fourier radius 2km/H=h/50 fits in the guard h. The interpolation argument of 175 with n=ceil(64(1+2RT)) gives η≥exp(−1800(1+TR)) for large TR; its estimates depend only on TR after rescaling. Hence 2^mη/40−M>1. For a=kR²/(3H²) one has 1−sinc(τ/H)^(2k)≤a on |τ|≤R and ≥2a on |τ|≥2R. For the second end evaluate first at v=2R/H: k v²=o(1), so 1−(1−v²/4)^k ≥(3/4)kv²/4>2a. Use monotonicity up to |v|=2 and afterwards |sinc v|≤1/2. Moreover log(1/a)=O(T), since k=O(exp T) and H/R=O(kT exp(2T)). The archimedean part with the reserve of 175 has margin at least a^m≥exp(−C T²R).

**Uniformity of the spectral cost.** Build χ by convolving the indicator of [−(2T+3),2T+3] with two uniforms of radius 1/4 and N=floor(G/200) uniforms of radius 1/N. The plateau covers the enlarged interval. The proof of 175 gives for the continuous cost at every τ
    |C(τ)| ≪ (1+T)exp(T) log(3+|τ|),
because the only prefactor coming from the new interval is its length times exp((2T+O(1))/2). On |τ|≤G/2 the fine factors moreover give 100^(−N). The error there is exp(−cG) for some absolute c>0 and large T, much smaller than the margin because G/(T²R)→∞. On |τ|>G/2 the masked error is at most
    O((1+T)exp(T) log(3+G) m (2H/G)^(2k)).
Here the maximum occurs at the lower end. One has 2H/G≪T exp(−2T), while log m=log R+O(log T), k≥log R. Thus this cost tends to zero and φ<1/2: the reserved half of b absorbs it pointwise. The mixture is exact and the fraction of margin that survives, with Plancherel, proves the statement.

**Distinction from the known horizon.** Paper 47 already gives a doubly exponential horizon of order exp(A_T) for checking the symbol of certain certificates. That estimate alone did not imply that verifying the zeros up to a comparable height would suffice for a positive certificate. Here the additional cost in the logarithm of the sufficient height is at most 5T+log 100. The deduction uses the complete spectral correction and the uncertainty margin, not just the horizon of the symbol. The law is sufficient; it does not prove that this height is necessary. Applying it to arbitrary T would still require an unbounded verification of zeros, so it does not close the global sign.
