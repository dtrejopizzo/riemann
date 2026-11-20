# Trace norm of the tail and exact trace of the full arithmetic form

Let A be the self-adjoint operator on X₀ representing B∞ in the energy product I, and A_L that of the cut of 032–033. Then A is trace class and

    ||A−A_L||₁ ≤ C/√(1+log L),       Tr A = (2/3) ξ′(2)/ξ(2) > 0.

The trace norm controls the sum of singular values. Operator-norm convergence of 033 alone does not allow passing the trace to the limit.

**Tail in trace norm.** Write f(t)=u(exp(−t)), g=f′ for t>0. Integration Jg(t)=∫₀ᵗg(z)dz is Hilbert–Schmidt from L²(dz) to L²(exp(−t)dt): its indicator kernel has squared norm ∫₀^∞t exp(−t)dt=1. To compare two cuts L<K write R=log L, S=log K and use the measure μ in coordinate r with masses Λ(n)/n at log n minus dr. In the contact of 032, the zero ordinary moment allows replacing f(t+r) by f(t+r)−f(r), since ∫conj(f(t))exp(−t)dt=0. Express the increment as the integral of g from r to r+t. By Fubini on the finite strip of cuts the remaining kernel is

    D(t,z)=μ((R,S] ∩ [z−t,z]).

The values at the moving endpoints do not affect integration in z. D vanishes for z<R. For z≥R the discrepancy bound of 032 gives |D(t,z)|≤C/(1+max(R,z−t)), uniformly in S. Separate [R,R+t] from its tail to obtain

    ∫|D(t,z)|² dz ≤ C [t/(1+R)² + 1/(1+R)].

Thus D between the same two spaces has Hilbert–Schmidt norm O((1+R)^(-1/2)). The difference of forms is −2 Re〈Jg,Dg〉 in the weighted space; compressing −J*D−D*J to the zero-mean restriction gives the announced bound for ||A_K−A_L||₁. The identity is obtained first on a smooth kernel and passes by continuity.

**Trace of the cuts.** Let s=1/2+it. The Mellin functional of u in coordinate g has kernel exp(−sz)/s; the zero-mean condition restricts g to the orthogonal complement of exp(−z). By projection, its squared norm there is

    [1/(2 Re s)−2/|s+1|²]/|s|² = 1/(t²+9/4)     (Re s=1/2).

Since |h_L(t)|=O_L(1+log(2+|t|)), multiplying the Mellin map by √|h_L| produces a Hilbert–Schmidt operator with measure dt/(2π). Factoring A_L using between the two factors the sign of h_L proves that it is trace class. By an orthonormal basis and absolute convergence,

    Tr A_L = ∫ h_L(t)/(t²+9/4) dt/(2π).

Completeness in trace norm and the identification of the operator-norm limit with A now justify Tr A=lim Tr A_L.

**Evaluation.** The weight of the integral is one third of the Poisson kernel of height 3/2. Its integral against cos(t log x), x≥1, is x^(−3/2)/3. For m♯(t)=Re ψ(5/4+it/2)−log π, the integral equals [ψ(2)−log π]/3: the harmonic extension to the upper half-plane is Re ψ(5/4−it/2) in the complex variable t, with logarithmic growth, so the Poisson formula applies. It is also obtained by integrating term by term the partial-fraction series of P47 prop:sharp. Using ψ(2)=1−γ_E it follows that

    3 Tr A_L = 1−γ_E−log π −2 Σ_{n≤L} Λ(n)/n² +2(1−1/L).

Removing L leaves 2ξ′(2)/ξ(2) by the definition of ξ and the logarithmic derivative of the Euler product at 2. Its strict sign is seen in the paired Hadamard sum of P47 rem:fe: at s=2 the real terms Re(1/(2−ρ)) are positive, since the nontrivial zeros satisfy 0<Re ρ<1.

**Scope.** The positive trace allows negative eigenvalues compensated by positive ones. The sum of their moduli is exactly (||A||₁−(2/3)ξ′(2)/ξ(2))/2, by the spectral theorem for trace class. The global sign would be equivalent to proving the upper bound ||A||₁≤(2/3)ξ′(2)/ξ(2). The previous tail estimate does not prove that bound. The scalar value of the logarithmic derivative is known; the object computed here is the trace of the normalized operator of 033 with all the von Mangoldt weights.

Exact cross-check: POWER_CONE_001 §§1–2 already obtains the same scalar as the energy of the generator a=2. The factorization as a product of two Hilbert–Schmidt operators and the evaluation of the trace received independent reviews. The identification as a trace does not turn the sign of that generator into global positivity.

## Trace with a dilation: what suffices to control at large distances

For r≥0 put S=S_exp(−r) and k(r)=exp(r/2) Tr(AS). It is real by the reality of A and S. The previous exact trace gives k(0). The global sign is equivalent to k(r)≤k(0) for all r sufficiently large.

**Computation without presupposing a sign.** For the cut L, S multiplies the Mellin transform by exp(−rs). By the trace-class factorization of the previous section and its evaluation diagonal one obtains

    k_L(r)=∫ cos(rt) h_L(t)/(t²+9/4) dt/(2π).

Convergence in trace norm proves uniform convergence on each compact interval to k, and |k_L(r)|≤C exp(r/2) with C uniform in L. Hence k is continuous. The exponential bound does not imply the desired inequality. For real z >1/2, its one-sided transform is

    ∫₀^∞ e^(−zr) k(r) dr
       = [ z k(0) − (ξ′/ξ)(1/2+z) ]/(z²−9/4).

Indeed, at fixed cut the integration of cos(rt) produces z/(z²+t²). Separate the two quadratic fractions. The term of height 3/2 contributes z k_L(0); the other is half the Poisson integral of h_L at height z, with negative sign in the numerator. Removing L, that Poisson integral equals 2(ξ′/ξ)(1/2+z): the cosine of t log n gives n^(−z), the continuous part gives 2/(z−1/2) and the archimedean part gives ψ(5/4+z/2)−log π. Use the recurrence of ψ and the absolutely convergent Euler series. The identity extends holomorphically to Re z>1/2 and meromorphically beyond; z=3/2 is removable by the value of k(0).

**Equivalence.** If A≥0, the compression identity S*AS=exp(−r)A and the Cauchy–Schwarz inequality for the Hilbert–Schmidt operators A^(1/2) and A^(1/2)S give |k(r)|≤k(0) for all r. Conversely, if k(0)−k(r)≥0 eventually, its Laplace transform has no singularity on the positive real axis: it is k(0)/z minus the previous expression and ξ has no real zeros there. Removing an initial piece only subtracts an entire function. The Landau argument used in 028 implies that the abscissa of convergence is ≤0, since a finite positive abscissa would be a real singularity. The transform is holomorphic in Re z>0. The formula then excludes zeros of ξ in Re s>1/2, since each would give a pole of its logarithmic derivative. By the Weil equivalence of P47 the global sign is obtained.

If k(r)>k(0) at a single r, one explicitly has Tr[(Id−exp(r/2)S)* A (Id−exp(r/2)S)]=2[k(0)−k(r)]<0, which forces a negative direction. No violation nor eventual upper bound has been established.

**Cross-check.** P47 thm:oneprofile already reduces the target to a positive definite correlation, and POWER_CONE_001, 028–030 and the screw-function criteria anticipate the translation-and-transform approach. Here the correlation is identified with a trace on X₀ and an eventual one-sided scalar inequality suffices thanks to the explicit meromorphic formula. The equivalence is not to be used as a proof of that inequality.
