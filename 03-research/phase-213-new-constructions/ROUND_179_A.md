# Strict positivity up to T=5/2 via a direct Fourier leakage bound

For 0<T≤5/2 one has W_T(f)≥exp(−9000000001)||f||₂² on the full domain of paper 46. The height G=3·10¹² of Z2 is used. The step that changes the scale of the computation with respect to 178 is an explicit bound without high-degree interpolation.

**Leakage lemma.** For f supported in [−T,T] and F=f̂, the fraction of its energy in |τ|>Ω is at least
    η=[1+(1+TΩ)exp(2TΩ+2)]^(−1).
To prove it denote by E_in and E_out the two integrals of |F|², d=1/T, A=Ω+d, F#(z)=conj(F(conj z)). The entire function J(z)=∫_{−d}^d F(z+s)F#(z+s)ds has modulus ≤C_f exp(2T|Im z|) by compact support. On the real rays |x|≥A one has 0≤J(x)≤E_out. Put z=A sin θ in the strip |Re θ|<π/2. The function J(A sin θ)exp(−2TA cos θ) is bounded holomorphic there, since Re(A cos θ)≥|Im(A sin θ)|. On both edges its modulus is ≤E_out. The three-lines principle gives that same bound on the whole strip. On the real interval [−A,A] it follows that J(x)≤exp(2TA) E_out. Integrating, 2d E_in≤∫_{−A}^A J≤2A exp(2TA) E_out, since for each |τ|≤Ω the interval [τ−d,τ+d] is included. This gives the lemma, also for complex f. The strip method and spectral leakage are classical tools; the constant used by the certificate is verified here.

**Parameters and comb.** Take T=5/2, U=log(25/2), R=55000000, k=20, m=500000000, H=400000000000 and N=10¹⁰. Keep u, g, φ and the spectral extension with indicator [−7,7] of 178. One has T+km/H=2.525<U and 2U<5.5. On 1≤x≤s=25/2 the Schur row of 081 is
    [xL(sx)+ψ(sx)+L(s/x)+xψ(s/x)]/(1+x).
The breakpoints are 1,s and q/s,s/q when they belong to the interval, with q a prime power up to floor(s²)=156. The attached Arb computation at each inclusive endpoint gives a common bound 79/5. As in 178 it dominates both one-sided traces and the interior of each cell. The bracket m_arch−79/5 is ≥1/10 on |τ|≥R and ≥−22 on the whole line.

**Margin.** Write a=kR²/(3H²). On |τ|≤R, u≤a by Taylor and Bernoulli. At the endpoint 2R the ball evaluation proves u>(7/2)a. Up to |τ|/H=2 it extends by monotonicity of sinc on the positive interval, and afterwards by |sinc|≤1/2. For the high reserve and the polar cost proceed as in 178. After reserving half of the bracket on |τ|>G/2, the integrated part per unit of ||f||² contributes at least
    a^m[(7/2)^mη/20−22] > 3a^m,
with Ω=2R. The leakage lemma gives −log η≤log(2(1+TΩ))+2TΩ+2. The verifier checks that m log(7/2) minus this majorant exceeds 10 and that a^m>exp(−9000000000). The polar term costs less than a^m||f||² by |u(i/2)|≤k/H²<a/2.

**Remaining spectrum.** The bounds of 178 for C remain unchanged since χ and G are identical. On |τ|≤G/2 the cost is below exp(−9000000002) per unit of |f̂|²dτ. On |τ|>G/2 the ceiling 10⁹log(3+G)m(2H/G)^(2k) is <1/1000 and the mask there is <1/2. The reserved density is at least 1/(80π)>1/1000. The atoms are positive and the low cost, even multiplied by 2π, stays below a^m in L² norm. This closes the announced margin in both parities. The extension to smaller windows is by inclusion.

**Reproduction.** Run python3 verify_179.py with python-flint. The enumeration of primes and endpoints uses integers and exact fractions, and the scalar inequalities use Arb at 192 bits. The previous limit certified here was 2.1, in 178. This proof does not establish positivity for all windows.
