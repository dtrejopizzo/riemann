# What hypothesis bounding a nonprincipal character would require, and how to eliminate the auxiliary condition

Fix even P=3 and the nonprincipal quadratic character χ, extended with value 1 at the prime P and multiplicatively to the integers; L(s,χ) denotes the usual L-function, which omits the factor at P. For t∈[1,2] let

    a_t(n)=μ²(n)∏_(p|n)(Re(χ(p)p^(it))−1),     b_t=a_t*a_t

with Dirichlet convolution. These are the fixed-frequency coefficients of 290 and their self-convolution. For almost every t, the square-root bound with arbitrary loss for the partial sums of a_t is equivalent to RH TOGETHER WITH the absence of zeros of odd multiplicity of L(s,χ) in Re s>1/2. For b_t, by contrast, RH is sufficient and necessary. Moreover, the choice of a generic t can be dispensed with entirely:

    RH ⇔  ∫₁² max(0,Σ_(n≤x)b_t(n)) dt ≪_ε x^(1/2+ε) for all ε>0.

The formula proposes an auxiliary criterion for the same sign. By itself it does not estimate the original average of 291.

**Product and parity of the order.** For F_t(s)=Σ a_t(n)n^(−s), the local comparison gives in Re s>1

    F_t(s)²= G_t(s)² L(s−it,χ)L(s+it,conj χ)/ζ(s)².

In G_t the large factors are 1+O(p^(−2 Re s)), by equality of the linear term. The square roots of the local Euler factors of the numerator are taken from the right; 1−χ(p)p^(−s+it) does not vanish in Re s>0. The finite factors, including P, are holomorphic in Re s>1/2. Thus G_t is holomorphic and uniformly bounded on each Re s≥σ₀>1/2, for t∈[1,2]; it may have zeros from small factors.

For each fixed zero ρ of ζ to the right of 1/2, the two L factors at ρ are nonzero except for a discrete set of t. For G_t(ρ)=0 one would need 1+(Re(χ(p)p^(it))−1)p^(−ρ)=0 at one of the finitely many p with p^Reρ≤2, which also gives a discrete set. Likewise coincidences of zeros between the two shifted copies of L are avoided except on a countable set of t. Remove the countable union over all zeros. For any remaining t, an exterior zero of ζ produces a pole of F_t², and an exterior zero of odd order of L produces a zero or pole of odd order in the meromorphic quotient: the squared factors do not change parity. A square-root bound for the sums of a_t would continue F_t holomorphically to the half-plane and both situations would be impossible. A square-root bound for b_t continues only F_t²; zeros of the numerator of any order are admissible.

**Converse ceilings.** Under RH the right-hand side representing the series of b_t is holomorphic in Re s>1/2. For a_t, add the condition on multiplicities: then the product of the two L-functions admits a holomorphic square root in the simply connected half-plane, including at its zeros, and the sign compatible with the series in Re s>1 is chosen. In either case the integral of the modulus of the continued series over a vertical block T≤|Im s|≤2T is O_(σ₀,η)(T^(1+η)) for Re s∈[σ₀,2], T≥2. One uses the classical bound under RH for 1/ζ of size O(T^η), and Cauchy–Schwarz with the classical unconditional second moment of an L-function of fixed conductor in σ≥σ₀>1/2. The shifts t∈[1,2] keep the constants uniform. For a_t the square root of the modulus of the product of the L-functions suffices. [Titchmarsh, chapter XIV](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf).

To pass to the ordinary partial sum take x a half-integer and smooth the indicator of n/x≤1 in |n/x−1|<1/(3x), without changing any integer sample. The Mellin transform of the cutoff up to zero is O_j((1+|v|)^(−1) min(1,(x/(1+|v|))^j)) in the strips used, by parts j+1 times. Move the integral to σ₀; horizontal closures at heights tending to infinity can be chosen with integral in σ of polynomial growth, by the block bound and Fubini. Summing blocks on the new line gives O(x^(σ₀+η)) for arbitrarily small η. Half-integers cover all partial sums. This proves the sufficiencies without using GRH for the auxiliary L-function.

**Integrated one-sided criterion.** Under RH the ceiling just obtained for b_t is uniform in t. For the converse, given an exterior zero ρ choose t₀ with numerator G²LL nonzero there. By continuity there is a smooth nonnegative weight η(t) of integral one, supported in a neighborhood of t₀, for which the integral of that numerator still does not vanish at ρ. The η-average of the series of b_t therefore has a pole at ρ, and is holomorphic at all real points >1/2 (also at 1, where the reciprocal of ζ vanishes). If the announced ceiling for positive parts held, the averaged partial sum would have the same upper ceiling. Apply Landau to Kx^σ minus that partial sum, with 1/2<σ<Re ρ: its Mellin transform, which for the partial sum is the averaged series divided by s, would have to have a real singularity to the right of σ. The contradiction proves the necessity of RH. The use of the positive part allows cancellations between coefficients before measuring each partial sum; the unconditional ceiling remains open.
