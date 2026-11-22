# How large a sample detecting misalignment over the whole band must be

At the critical scale of 184, N=exp(2T−2D), G=exp(exp T), D fixed. We consider the modulus of the weighted average of p^{it} for N≤p≤eN. Only certificates that replace the average by a single fixed sample with nonnegative weights independent of t are treated.

**Obstruction for small samples.** Let p_1,…,p_m be distinct primes from that interval, with arbitrary weights w_j≥0 summing to one. For fixed K≥2, if

    m[K log(eN)+log K] ≤ (log G)/2,

there is t∈[2G,3G] with Re Σ w_j p_j^{it} ≥ cos(π/(K+1))−o(1), uniformly in the selection and the weights. For a fixed gap ε one can take K of order 1/√ε, with 1−cos(π/(K+1))<ε/2. In particular every sample of size ≤c_ε exp(T)/T admits a frequency with modulus >1−ε. The frequency may change when the sample changes.

**Proof in the prescribed band.** Take b_r proportional to sin((r+1)π/(K+1)) for 0≤r<K, normalizing Σb_r²=1. Form R(t)=∏_j Σ_r b_r p_j^{irt}. By unique factorization, the diagonal mean of |R|² is one. That of p_j^{it}|R|² is Σ_{r<K−1}b_r b_{r+1}=cos(π/(K+1)), by the sine recurrence with zero endpoints. In both expansions the sum of moduli of coefficients is ≤K^m by Cauchy–Schwarz. The quotients of integers representing nonzero frequencies have numerator and denominator ≤(eN)^{mK+1}; hence the modulus of the average of each oscillation over an interval of length G is ≤2(eN)^{mK+1}/G. The joint error is ≤2(eN)G^(−1/2)=o(1). Averaging with the density |R|² and taking a point at least as large as the average proves the obstruction.

**When a sample does reproduce the whole average.** For 0<ε<1/2 there is a sample with repetition of O(ε^(−2)log(2+G/ε)) primes that approximates uniformly, with absolute error ε, the complex average of 184 on the band [G,4G]. This includes the frequency corrections of 184 for large T. Sample independently with probabilities proportional to log p; removing the common phase N^{it} leaves exponents log(p/N)∈[0,1]. Both the true and the empirical averages have derivative of modulus ≤1. On a grid of step ε/8, Hoeffding applied to the real and imaginary parts gives probability ≤4 exp(−c m ε²) of error >ε/2 at each node. The union over O(1+G/ε) nodes has probability <1 with the indicated constant, and the derivative extends the control to the band. It is an existence result for a sample, without a new bound for the value of the original average.

The recurrence of the comb in 081 allows arbitrary heights. The argument here imposes [2G,3G] and allows the number of primes to grow with the window. The coherence of P46 prop:wit-coh and the moments of 181 do not give a pointwise certificate of misalignment for these samples. The result bounds the reach of replacing the block of 184 by few primes. Misalignment of the complete block remains open.
