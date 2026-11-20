# Polylogarithmic band with recombinable positive local averages

In each large block X=2^k put L=log X, D=⌊L⌋, j₀=⌈L⌉ and N=C₀ D L² for a sufficiently large absolute constant. Let ν be the law of the independent uniforms of 047, with lengths l_i=1/[i(i+1)], and ν_> the law of the sum of those with indices i>j₀. It is a probability on [0,1/(j₀+1)]. For X≤x≤8X define

    T_X(x,t)=∫ C_t(x exp(u)) dν_>(u).

There are explicit signed weights g(n)(1−ψ(n/N)) for which, uniformly in that band and 0≤t≤2,

    T_X(x,t)+J_X(x,t)=O_ε(X^(1/2+ε)),
    J_X(x,t)=Σ_(D<n<2N)g(n)(1−ψ(n/N)) T_X(x/n,t).

In this formula the same frozen kernel defines T_X also at smaller arguments. RH is equivalent to the ceiling O_ε(X^(1/2+ε)) for ∫₁²(−J_X(x,t))₊dt in all these blocks. Only indices between ⌊log X⌋ and O((log X)³) are needed. The local average of the main sample is positive in its weights and its window has relative width O(1/log X). The sign of the coefficients of the intermediate sum remains free.

**The sieve.** Put a(d)=μ(d) for d≤D, a(2D)=−2D Σ_(d≤D)μ(d)/d and zero elsewhere. Then Σ a(d)/d=0, Σ|a(d)|=O(D log(2D)) and g=1*a has g(1)=1, g(2)=…=g(D)=0. The full mean against T_X has a root ceiling by 309, since the summatory function of 1*c_t is U of 317 and the a(d) cost only powers of L. For ψ take the distribution function of ν evaluated at v−1: it is zero up to 1 and one from 2 on.

**A bound with increasing order of differentiation.** Write S_J(w)=ν_>((w,∞)) with J=j₀. Its derivative of order k has sup norm ≤[2(J+k+1)²]^k. It suffices to differentiate k of the uniforms keeping the survival function of the others: each derivative is a difference of two masses of total norm 2/l_i. Infinitely many uniforms remain and distributional differentiation gives the classical bound. The same proof with J=0 works for ψ. For each m≤8eX/N define F_m(v)=ψ(v/N)S_J(log(mv/x)) on v>0, extended by zero to the left. Its support is in [N,8eX/m]. For j≥1,

    ||F_m^(j)||₁ ≤ O(X) [C(J+j+1)²/N]^j.

Indeed, on v≥N the derivative of order b of S_J(log(mv/x)) is v^(−b) times a combination of the first b derivatives with Stirling coefficients of the first kind. The polynomial of their moduli is z(z+1)…(z+b−1), which at z=2(J+j+1)² is ≤(z+j)^b. Leibniz, the bounds for ψ and the length of the support prove the inequality with C absolute.

In the tail with ψ exchange the coefficients c_t(m). Poisson applied to each Σ_l F_m(dl) eliminates the integral mode on summing over d. The sum of the other modes is bounded by O(||F_m^(j)||₁) Σ_d |a(d)|d^(j−1) for j≥2. Take j=⌈L⌉. Since d≤2D, on summing over m the total error is ≤O(X³)(C' D L²/N)^j, using |c_t(m)|≪_ε m^ε and absorbing the logarithmic powers. Choose C₀ with C'/C₀<exp(−6). What remains is O(X^(−2)), sufficient margin for the identity. This controls the increasing order instead of formally substituting δ by zero in 319.

**Why the short positive average still detects zeros.** Under RH the modulus ceiling of 317 holds. For the converse take x∈[X,2X] and average T_X(x exp(v),t) with respect to the law of the head i≤j₀. All centers fall in [X,8X]. By independence one recovers exactly ∫ C_t(x exp(w))dν(w), with the same fixed law in all blocks. Convexity of the positive part transfers the ceiling to this fixed average without multiplying the constant. Its Mellin transform is that of C_t multiplied by ∫exp(sw)dν(w), up to an entire function from the lower endpoint. That factor does not vanish in Re s>0: it is the convergent product of (exp(s l_i)−1)/(s l_i), and Σ l_i<∞. The localization in t and Landau of 317 therefore detect any exterior pole. This proof only uses nonnegative weights in the local observation and in the recombination.

**Antecedents and limit.** The kernel and its product already appear in 047; 049 also uses cancellation of the integral mode and density correction. The additional step is to separate block-dependent head and tail so as to preserve the pole detector exactly while reducing the observed window, with the ordinary summatory function C_t of 317. The one-sided estimate of J_X is missing. Reducing to a polylogarithmic number of indices does not prove that estimate.
