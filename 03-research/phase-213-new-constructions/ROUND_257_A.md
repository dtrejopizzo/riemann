# Positive budget using only primes between x and 2x

Let L=log 2, ω=2π/L and g(y)=y^(−1/2)(1−cos(ω log y)) on [1,2], zero outside. Set h=∫₁²g(y)dy and

    D(x)=xh−Σ_(x<p≤2x) g(p/x)log p.

The global sign is equivalent to D(x)≥0 eventually. Under RH one obtains liminf D(x)/√x≥0.029L. Without assuming RH, D(x)>0.009√x on all of 10^12≤x≤10^38. The weight of 256 is changed so as to suppress both tails completely. The correct budget for this sum is xh; the sum of 256 is not being truncated with its same threshold.

**Why the eventual sign decides.** The transform H(s)=∫g(y)y^(s−1)dy equals (exp(Lz)−1)ω²/[z(z²+ω²)], z=s−1/2, by elementary integration, with removable singularities and H(1/2)=L. In particular it does not vanish for Re s>1/2. The Mellin transform of D for x≥1 is h/(s−1)−H(s)P(s), with P from 253: the support of g(p/x) is in [p/2,p], always with x≥1. The main term cancels at 1. Any zero to the right would give a pole, while there is no real singularity there; Landau then excludes an eventual sign. Even controlling D at all sufficiently large integers would suffice: the derivative of the sum is O(1) by θ(y)≤2y and the C¹ weight, and off RH there are negative excursions of order x^d for each 1/2<d<Θ as in 249.

**Separation without paying for the cubes.** For the count with Λ the main term is xH(1), the spectral terms are −ΣH(ρ)x^ρ and the archimedean remainder is −∫ g(u/x)du/[u(u²−1)] for x>1, by the explicit formula of ψ against the compact C¹ weight, with piecewise second derivative. The zero series converge absolutely by the cubic decay. Subtracting the count with Λ of weight g((u/√x)²) eliminates all even exponents. Its main term is √x L/2 and its zeros have multiplier H(ρ/2)/2. The remaining proper odd powers are positive, so their removal only increases D. In a lower bound for D the only archimedean loss comes from the weight at √x and costs at most 2/x for x≥2, by g≤2 and integration of the kernel from √x to infinity.

**Margin of the zeros on the line.** For a critical zero of ordinate γ one has
     
    |H(ρ)|/L=|sin(γL/2)/[(γL/2)(1−γ²/ω²)]|.

Up to G=3·10¹² they are critical by Z2. Use the positive trace of 248, with ceiling 0.047 for the low sum of 1/|ρ|², and remove the first 20 pairs from that budget. From T=γ₂₀ the ratio of |H(ρ)|/L to 1/|ρ|² is ≤(1+1/(4T²))2ω²/[LT(1−ω²/T²)]. The ball verifier sums the first pairs explicitly and adds this remainder, obtaining less than 0.471 in total. Under RH this holds for the whole series. Thus the cost is less than the main term of squares L/2, even using only the interval [x,2x]. For the series of squares the critical zeros have cost ≤2ω² L·0.047 x^(1/4): integrate twice by parts the window 1−cos(ωt) in H(ρ/2), using |(ρ−1)/2|=|ρ|/2. This gives the announced asymptotic margin under RH.

**Finite bound without hypothesis.** The tail |γ|>G of |H(ρ)|/L is term by term ≤300/|γ|³, by the rational-exponential expression, and that of |H(ρ/2)|/(2L) is ≤2ω²/γ² by the same integrations by parts (Re(ρ/2−1/2)≤0). Use Σ_tail 1/γ²<6.4·10^(−12) from 248. In units L√x the high cost is ≤6.4·10^(−12)[300√x/G+2ω²]. Together with the low cost 0.471+2ω²·0.047/x^(1/4), this leaves the indicated margin on the whole interval. Run python3 verify_257.py to reproduce the computation with certified ordinates and outward-rounded bounds.

**Antecedents.** 236 already studies a cosine on [x,2x], with sign changes and an energy criterion. 247 certifies a budget by the trace with a weight that changes sign and reaches the origin. Here the window is dyadic, the weight is positive, the threshold is the exact continuous integral and the residual trace after the 20 pairs proves domination by the squares. The eventual inequality for arbitrarily large primes remains open.
