# Gaussian window and truncation at the root of log x

In 362 one can use a two-sided weight g(u)=exp(−u²/2)/√(2π) and reduce the required band to T=√(2 log x). With c=1+1/log x and D_z of 362, RH is equivalent to the modulus of

    (1/(2π)) ∫_{−T}^T x^(c+it) exp((c+it)²/2) D_z(c+it) dt

being O_ε(x^(1/2+ε)) for each ε>0 uniformly in large x and (log x)²≤z≤4(log x)². The tail removed in this new integral costs only O((log x)²) in modulus.

**Two-sided observable.** Keep S,P,Q with their coefficients of 360, changing the weight to g(log(x/n)). The two-sided transform of g is G(s)=exp(s²/2), entire without zeros. The sums and their derivatives converge locally absolutely. For 0<x≤1 each observable and the logarithmic derivative of S are O_N(x^N) for each N>1, uniformly in z, since |g(u)|+|g'(u)|≪_N exp(Nu) for u≤0 and the coefficients per integer cost O(log(2n)). Thus arbitrarily small dilations can be used without assuming causal support.

**Replacing the memory term.** In v=log x, the identity μ log=−μ*Λ and g'(u)=−u g(u) give

    dS(e^v)/dv + v S(e^v) = −P(e^v)−Σ_{k≥2,p}(log p) S(e^v/p^k).

Under RH the Mertens bound and partial summation against g and g' give |S|+|dS/dv|≪_ε x^(1/2+ε) for x≥1: after the change n=x exp(−u) the integrals of |g'| and |g''| with fixed exponential weight converge. The identity controls P with a logarithmic loss. The inversion Q_z=K_z(P−L_z S) of 359 and the Euler norm x^o(1) give the required ceiling for Q, starting with a smaller exponent.

**Inverse direction without estimating the derivative a priori.** Fix σ=1/2+ε, 0<ε<1/4. Use two finite envelopes on 0<t≤X,

    A(X)=sup |S(t)|/t^σ,     B(X)=sup |P(t)|/(t^σ log(2+t)).

For every λ>0 there is a constant C_λ such that B(X)≤C_λ+λ(A(X)+B(X)). Indeed in the scalar block x apply P=L_z S+U_z Q_z of 359 with z=log²x. In units of x^σ, the cost of L_z S is O_ε((log x)^(1−2ε) A(x)); the branches d≤√x use the hypothesis with loss ε/2 and cost O(x^(−ε/2+o(1))). For d>√x, the first identity Q_z=K_z(P−L_z S) at each child t=x/d costs, in its own units t^σ, (A(x)+B(x))x^o(1): the Euler norm is computed at the frozen cut and log(2+t)≪log x even at the small children. The return tail costs x^(−ε/4+o(1)) as in 359. These identities remain valid for the two-sided weight by absolute convergence, using the decay at small scales. Divide by log(2+x), take x large and absorb the compact stretch into C_λ.

On the other hand A(X)≤C+3B(X). To see this, take F(v)=e^(−σv)S(e^v). Its equation has left side F'+(v+σ)F and the modulus of the right side is bounded by B(X)log(2+e^v)+C_σ A(X) for v≤log X. Here C_σ=Σ_{k≥2,p}(log p)p^(−kσ)<∞. Above a fixed, sufficiently large v₀ the right side costs at most (v+σ)(2B(X)+A(X)/4). The integrating factor exp(v²/2+σv) gives |F(v)|≤|F(v₀)|+2B(X)+A(X)/4. Incorporating the earlier stretch, taking the supremum and rearranging gives the claimed inequality. Choosing λ small in the first inequality bounds both envelopes. Since ε can be arbitrarily small, the two-sided transform of S extends G(s)/ζ(s) holomorphically to Re s>1/2. G loses no pole of 1/ζ.

**Truncation.** On the line c, |G(c+it)|=exp(c²/2−t²/2) and |D_z(c+it)|≪(log x)² by 362. Invert absolutely and use ∫_T^∞exp(−t²/2)dt≤exp(−T²/2)/T. With T=√(2 log x), the factor x^c exp(−T²/2)=e; the announced polylogarithmic error remains. This is a height reduction in the integral of the new weight. Cancellation in the inner band is not proved and no new support window of paper 46 is obtained.
