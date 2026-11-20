# The cost of reproducing the band with a divisor sum

In 044 the inverse of the hat W had corners arbitrarily close to zero. That discarded a fixed profile with bounded loss on the primes. Here one allows **changing the support and the profile** at each scale. We write Df(t)=Σ_{m≥1}f(mt); W is the normalised hat of the even scales in 044. The following two conclusions clarify whether, with the divisor identity, one can keep the band and perform quadrature of the new profile.

**Exact construction on the whole sampled range.** For each x=j⁴ with even j, there exists a signed continuous f with compact support in (0,∞) with Df≤W on the whole half-line and Df(t)=W(t) for all t≥1/x. Let g(t)=Σ μ(m)W(mt), a locally finite sum with Dg=W. Take δ=1/(8x), multiply g by a continuous cutoff that is zero below δ/2 and one from δ on; call f₀ the product. Take an auxiliary continuous hat 0≤h≤1 supported in [δ/2,4δ], equal to one on [δ,3δ]. For t<δ there are at least δ/t multiples mt in [δ,3δ]; moreover Df₀(t)≤16‖f₀‖∞/t. Thus

    f=f₀−(16‖f₀‖∞/δ)h

gives Df≤0 when t<δ, Df≤W for t≥δ and Df=W for t>4δ. In particular it serves simultaneously for all integers n/x. The resulting equality ΣΛ(n)W(n/x)=Σ f(k/x)log k uses exact inversion at the samples. Its sign requires controlling the signed sum on the right.

**Obstruction to balance.** For any nonzero continuous function f with compact support away from zero, Df≤W globally implies ∫f<0. It holds for any continuous nonnegative band W with compact support away from zero, independently of the scale.

Indeed tDf(t)→∫f by Riemann sums and hence ∫f≤0. If equality held, regularise f by convolution with a positive approximate identity in log t: g(t)=∫f(te^v)φ(v)dv. For a sufficiently narrow kernel g≠0. It is smooth, with compact support away from zero, with ∫g=0, and Dg≤U, where U is the same regularisation of W and has support [a,b]⊂(0,∞) in the sense of inclusion.

Extending g evenly to G on the line, Poisson gives Dg(t)=t⁻¹Σ_{n≥1}Ĝ(n/t); the terms at the origin vanish by G(0)=∫G=0. With the Fourier convention exp(−2πiξs), for each integer k≥1,

    ∫ Dg(t)t^(−2k−1)dt = ζ(2k+1) ∫₀^∞ v^(2k)Ĝ(v)dv = 0,

because G^(2k)(0)=0. The change of order is absolute by the rapid decay of Ĝ and the convergence of Σn^(−2k−1); all integrals in t are over (0,∞).

If Dg were strictly negative at some point of (0,a), it would be ≤−η on an interval [l,h] with h<a. The magnitude of that contribution to the moment would be ≥η(h−l)h^(−2k−1), while the whole positive contribution is ≤a^(−2k−1)∫U. For large k this contradicts the vanishing moment. Thus Dg=0 below a. It also vanishes above the upper endpoint of the support of g and beyond. On the remaining compact set all moments of the measure Dg(t)t⁻³dt in the variable t⁻² vanish, using k=1,2,... . Polynomial approximation implies Dg=0. Finite inversion at each t>0 gives g=0, a contradiction.

**Scope for the sign.** The balance ∫f=0 is the cancellation that eliminates the term x log x·∫f from the integral of f(t/x)log t. It is forbidden precisely for every nontrivial global minorant of this class. The argument does not give a uniform lower bound for |∫f_x|. Nor does it control the quadrature errors when f_x varies. The local inequality of 044 remains open.

Targeted antecedents: selection 040 for the balance condition and the tail loss; 044 for the band, the inverse and the loss of the fixed profile; SPEC_SIGN_OBJECT_003 of phase 200 for the moments at the trivial zeros. Here the additional inference is that the sign alone outside a band, combined with all the moments and the balance, forces vanishing. The construction shifts the correction to scales below the first sample.

## The balance can be approximated with equality at the samples

Fix the hat W of 044. For any threshold τ>0 and any tolerance ε>0 there exists a compact continuous minorant f as above with Df=W on [τ,∞), −ε<∫f<0 and |∫f(t)log t dt−∫W|<ε. More generally one can simultaneously approximate any finite list of logarithmic moments of the exact inverse. There is therefore no fixed loss in the balance, even after imposing all the samples of one scale.

**Estimates of the inverse.** One uses the classical quantitative prime number theorem for Möbius, M(y)=Σ_{m≤y}μ(m)=O_A(y/(log y)^A) for each fixed A. It is an unconditional analytic input. Write L=log(1/t) for small t. Partial summation for a function U of bounded variation supported in [1/16,16] gives Σμ(m)U(mt)=O_{A,U}(t⁻¹L^(−A)): in the summation interval m is comparable to 1/t, and the variation of U(mt) is at most that of U. Apply this to W and to uW'(u), both of piecewise bounded variation with finite total variation. The inverse g of the previous construction is locally Lipschitz; one obtains |g(t)|≤C_A t⁻¹L^(−A) and |g'(t)|≤C_A t⁻²L^(−A) almost everywhere. Consequently g is integrable with any weight (1+|log t|)^k.

For s>1 the absolutely convergent inversion gives ∫g(t)t^(s−1)dt=(∫W(t)t^(s−1)dt)/ζ(s). Taking the limit and its first derivative at s=1 by dominated convergence and using the residue one of ζ, one obtains ∫g=0 and ∫g(t)log t dt=∫W(t)dt.

**Correction with small mass.** Repeat the construction of 045 with δ↓0 and a linear cutoff on [δ/2,δ]. For each A, |∫f₀|=O_A(log(1/δ)^(−A)) by ∫g=0 and the tail bound (use a larger exponent in g). Moreover Var(f₀)=O_A(δ⁻¹log(1/δ)^(−A)) by the derivative bound and the variation in the cutoff. For t<δ, comparing each rectangle of width t with its integral gives

    t Df₀(t) ≤ ∫f₀ + t Var(f₀) ≤ ηδ,
    ηδ=max(0,∫f₀)+δ Var(f₀).

It suffices to subtract (ηδ/δ)h, with h the same auxiliary hat of 045. The new f satisfies Df≤W and Df=W for t>4δ. The absolute mass of the correction is O(ηδ). For each fixed k, ∫|f−g|(1+|log t|)^k tends to zero faster than any inverse power of log(1/δ), adding the tail of g and the correction supported at scale δ. Choose 4δ<τ and then reduce δ until the tolerance is reached. The strict sign of ∫f follows from the previous lemma by taking τ below the upper endpoint of the band in the construction to guarantee f≠0.

**What remains to be estimated.** For fixed x, choose τ≤1/x and 4δ<τ. Both f and g agree at each k/x and the sum against log k is identical. However, the integral of g(t/x)log t is exactly x∫W. Thus the only term to be estimated in this comparison is the difference between the discrete sum against log k and that integral. For the band of even scales one needs the sum to exceed the integral minus O(√x). The approximation of the moments alone does not bound that difference.

The same proof covers odd j using the hat W_j(t)=√x w_j(xt) of 044. The lower endpoint lies in [1/81,1/16] and the upper one at 16. In both branches the formulas of 044 give combinations of t and t⁻² with uniformly bounded coefficients (the ratio j/floor(j/2) lies between 2 and 3). Thus W_j and tW_j' have uniformly bounded variations, including the jumps of the derivative. All the approximation bounds above can be taken uniform in j.

To make the remainder precise, write g_j for the inverse of W_j. Integrating by parts over the cells of k/x one obtains exactly

    x∫W_j − Σ_k g_j(k/x) log k
      = x∫₀^{1/x} g_j(t) log(xt)dt
        − ∫_{1/x}^∞ {xt}[g_j'(t)log(xt)+g_j(t)/t]dt.

The value of log(xt) at the lower endpoint is zero. The antecedent of this type of fractional-part formula is in phase 188, N_BUILD_005 §4 and N_BUILD_006 §§1–2. The inequality of 044 asks for a uniform upper bound O(√x) for the right-hand side before normalising. The absolute Möbius estimates used for the moments only give O_A(x/(log x)^A) for each fixed A: in the second integral one separates t≤1/√x, where the inverse power of log x is extracted, from the rest, which costs O(√x log x). Cancellation is missing in this quadrature remainder.
