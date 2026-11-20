# A fixed weight with only O((log x)²) pending outer samples

In 046 the variation of the derivative of the weight imposed the threshold x^(1/4) on the absolute estimate. We change the weight by means of a compact average of dilations, checking that it preserves the implication to the sign. Antecedents: averages of translations in selection 027, analytic transfer in 038, band in 044 and quadrature in 045–046. The sufficiency step uses Landau and Weil; it does not constitute a new elementary mechanism for signing the remainder.

**A single average for all scales.** Let ν be the law of the sum of independent uniform variables on [0,l_n], with l_n=1/(n(n+1)), n≥1. The sum lies in [0,1]. The transform P(z)=∫exp(zv)dν(v) is the product of (exp(l_n z)−1)/(l_n z). The factors differ from one by O_R(l_n) on |z|≤R. Thus P has no zeros for Re z>0. The density of ν is smooth: in the Fourier transform the first N factors give O_N((1+|ξ|)^(−N)) for each N and the remaining ones have absolute value at most one.

Take the normalised weight W of 044 for even j and use that same weight at every real scale. Define

    V(t)=∫ exp(−v/2) W(t exp(−v)) dν(v),
    D(r)=exp(−r/2)[exp(r)∫V−Σ_n Λ(n)V(n exp(−r))].

V is positive in the interior of its support [a,B]=[1/16,16e]. For h=log16, b=3/2 and c=1/(2cosh(bh)), by the identity of 044 D is the average in v of the value at r+v of (I−c shift_{−h}−c shift_{h})E, writing E in logarithmic coordinate.

**Why an upper bound at j⁴ suffices.** Under the sign, E is bounded on the half-line by 038–039, hence so is D. Conversely D''(r)=O(exp(r/2)) for large r by differentiating the locally supported sum, regularity of V and the Chebyshev bound Σ_{n≤X}Λ(n)=O(X). On the cells between r_j=4log j and r_{j+1} linear interpolation has error O(j²/j²)=O(1). It suffices that D(r_j)≤C for D to be bounded above.

For large r, E(r)=3k(r)+O(1) by 039. The same upper bound transfers to the average of the three translations of k. Its one-sided Laplace transform, up to entire terms from the finite pieces and a constant factor if the 3 is kept, is the transform of k in 038 times

    P(z)[1−cosh(hz)/cosh(bh)].

This is obtained first on Re z>1/2 by shifting the lower limit of each integral, with uniformly bounded translations. The factor does not vanish on 0<Re z≤1/2: for the bracket the only possible real parts of a zero are ±b. The transform is regular on the positive real half-axis by 038. Landau applied to a constant minus the average, eventually nonnegative, excludes poles on Re z>0 as in 038. Every zero of ξ with Re s>1/2 would produce a surviving pole at z=s−1/2; 038 and Weil give the sign.

**Control of derivatives.** In logarithmic variable, the weight exp(y/2)V(exp y) is the convolution of exp(y/2)W(exp y) with ν. Differentiating q of the uniform factors costs in variation norm at most ∏_{n≤q}(2/l_n)=2^q q!(q+1)!. Thus the sup norm of the q-th derivative of V(exp y) on its support is ≤C^(q+1)(q!)², by Leibniz and the factor exp(−y/2). The function χ(y)=ν((−∞,y]) also satisfies that bound: it is the convolution of the bounded step with ν. It equals zero up to 0 and one from 1 on.

Let g(t)=Σ μ(m)V(mt). 045 and its moments apply, since V is smooth with compact support away from zero. In particular ∫g=0, ∫g log=∫V and Σg(k/x)=V(1/x)=0 for large x. With Δ as in 046, the unnormalised deficit is Δ[g(u/x)log(u/K)].

**Upper quadrature.** Define H₊(u)=g(u/x)χ(log(u/K))log(u/K). Its m-th term, without μ, is F_z(mu/x) with z=mK/x and F_z(s)=V(s)χ(log(s/z))log(s/z). Only z≤B intervenes. In the variable log s, by Leibniz the derivatives of order q have sup norm ≤C^(q+1)(q!)²(1+log(B/z)); where the function or its derivatives are nonzero one has s≥z. Passing to ordinary derivatives preserves this order: s^q ∂_s^q is the product of the operators (∂_{log s}−i), 0≤i<q. The coefficient of order l in absolute value is ≤binom(q,q−l) q!/l!, bounding each product of q−l indices by the product of the q−l largest integers between 1 and q. Summing against (l!)² one obtains at most 2^q(q!)². The support s≥a absorbs s^(−q) and the fixed width allows passing to the L¹ norm.

By Poisson and integration by parts q≥2 times, |ΔF|≤2ζ(q)(2π)^(−q)‖F^(q)‖₁ for F smooth and compactly supported on the half-line, extended by zero. In each dilation the factor is (m/x)^(q−1). For M=Bx/K≥1, Σ_{m≤M}m^(q−1)(1+log(M/m))≤C M^q uniformly in q≥2, using m^(q−1)≤M^(q−2)m. Altogether,

    |ΔH₊| ≤ x C₀^(q+1)(q!)² K^(−q).

Choose q=floor(c√K) with c sufficiently small and use q!≤q^q. One gets |ΔH₊|≤C x exp(−c'√K). Therefore a sufficiently large fixed constant A and K=A(log x)² give |ΔH₊|=O(√x).

**Signed obligation.** At x=j⁴, put H₋(u)=g(u/x)[1−χ(log(u/K))]log(u/K). Global positivity is equivalent to ΔH₋≤C√x eventually, because the upper part satisfies the two-sided bound and the normalisation of D is x^(−1/2). The outer sum only contains k<eK. What remains are the integral near zero and the inner Möbius sums in g; their cost and their sign are not controlled by counting samples. All the weights and constants of the cutoff are independent of j.

**Refinement of the cutoff.** For each fixed δ>0 one can choose instead l_n=cδ/[n(log(n+1))^(1+δ)], normalising the sum to one. The same construction gives, up to C^(q+1), the bound q! L(q)^q for the derivatives, with L(q)=max(1,(log(q+2))^(1+δ)). This class of bounds is preserved by Leibniz (use L(l)≤L(q)) and by the conversion to ordinary derivatives above, whose sum now costs at most 2^q q! L(q)^q. In the quadrature bound (q!)² is replaced by q! L(q)^q. With q=ceil(log x), K=Aδ log x (log log x)^(1+δ) and Aδ sufficiently large one again obtains O(√x). The weight is fixed once δ is chosen. One does not take δ=0: the proposed lengths in that case are not summable.

The construction of Gevrey functions by infinite convolution of uniforms already appears in phase 159, G2_B6_R2, lemmas W/E, and G2_P3_R2 in its audit. The joint application to the preservation of the poles of the band and to the cutoff of the quadrature is the specific content here.
