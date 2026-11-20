# The quadratic mean on any interval of fixed ratio detects the complete displacement

For each fixed c>1, B=sup_ρ |Re ρ−1/2|,

    lim_(X→∞) log(1+∫_X^(cX) (ψ(x)−x)² dx/x²)/log X = 2B.

The interval can be [X,2X], or [X,1.01X]. Unlike 229 the length in logarithms is constant. A ceiling X^o(1) along a subsequence for a single fixed c suffices. The implicit constant of the floor depends on the chosen zero and on c; the argument does not allow c to be sent to one with X.

**A filter of arbitrarily short support.** Let ρ₀=β₀+iγ₀ be a zero with β₀>1/2, and fix 1/2<σ<β₀. For H=log c build a smooth complex function f supported in [0,H], with integral one, with

    ∫ f(v) exp((ρ−ρ₀)v)dv = 0

for every distinct value ρ with Re ρ≥σ. Multiplicity will be counted later in the explicit formula. We use Ingham's unconditional estimate N(σ,T)≪ T^[3(1−σ)/(2−σ)] log⁵T. The exponent is strictly less than one, so the sum of 1/|γ−γ₀| over those zeros in the tail converges by dyadic summation. Negative ordinates are included by symmetry.

For each zero of the tail take h=π/|γ−γ₀| and a probability on {0,h} whose ratio between the weight at h and the weight at zero is exp(−(β−β₀)h). Its exponential integral at ρ−ρ₀ is zero. Taking the tail sufficiently high, the sum of the h is less than H/3. The infinite convolution exists as the law of the sum of independent variables on those intervals: the series converges absolutely for each choice of points. It is a probability supported on [0,H/3]. At each exponent to be annihilated, all partial products from its factor onwards give zero and passage to the limit holds by compact support.

Finitely many zeros with Re ρ≥σ distinct from ρ₀ remain. For each w=ρ−ρ₀≠0 choose h>0 so short that the sum of their lengths is less than H/3 and exp(wh)≠1. The measure (δ_h−exp(wh)δ₀)/(1−exp(wh)) has mass one and annihilates w, even if the two zeros have the same ordinate. Its variation may be large but it is a fixed constant. Convolve all factors with a smooth function of mass one supported in (0,H/3). The result is f with the indicated properties. Its transform at w decays like any inverse power of 1+|Im w| uniformly for |Re w|≤1, by integration by parts.

**Extracting a single residue on every band.** Write t=log X, E(x)=ψ(x)−x. Apply the von Mangoldt explicit formula in the variable s=t+v against the test f(v)exp(−ρ₀(t+v)). The distributional identity for s>0 is E(exp s)=−Σ_ρ exp(ρs)/ρ−log(2π)−(1/2)log(1−exp(−2s)); the convention at a jump has no influence. After smoothing, the sum is absolutely convergent by the decay above and Z3. All zeros to the right of σ, including the boundary except the target, disappear. The remaining ones contribute O_f(exp(−(β₀−σ)t)), on summing the transforms in absolute value. The constant term and the trivial zeros cost O_f(exp(−β₀t)). Therefore

    ∫ f(v) exp(−ρ₀(t+v)) E(exp(t+v))dv → −mult(ρ₀)/ρ₀ ≠ 0.

Cauchy–Schwarz bounds the modulus of the integral by C_f exp(−(β₀−1/2)t) times the root of ∫_X^(cX) E(x)²dx/x². A floor ≥c_(ρ₀,H) X^(2β₀−1) on each sufficiently high interval follows. By symmetry 1/2+B can be approximated by such β₀ if B>0, without assuming that the supremum is attained. The ceiling comes from the inclusion inside [(cX)^(1/2),cX] and 229. If B=0 the required floor is trivial by the 1 in the statement.

**Scope and antecedents.** 229 only gave power bands; its concentration argument did not allow an interval of fixed ratio. The filter uses scarcity of zeros in each half-plane strictly to the right of the line, not finiteness of the total of targets. The density estimate already appears in phase 36, document 104. The proof does not compute f from primes nor evaluate the ceiling on dyadic bands. No priority is claimed for this consequence in the theory of oscillations of the prime error. [Density estimate used](https://arxiv.org/abs/2507.15184).
