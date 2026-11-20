# Exponents of the two excursions at the exact moving cut

**Status: PROVED, deduction independently reviewed, including the terminal leaves and the tail of the convolution.**

Let S(x)=S^*(x;(log x)²) of 368 and Θ the supremum of the real parts of the nontrivial zeros. If Θ>1/2, for each sign e=±1,

    limsup log(1+max(e S(x),0))/log x = Θ.

In particular for each 1/2<σ<Θ there are arbitrarily large values with S(x)>x^σ and others with S(x)<−x^σ. The antecedent 365 gives oscillations in a diffusive average, 361 freezes the cut and 368 transports a sign hypothesis. Here a one-sided power bound is transported up to the average, preserving its exponent as a tends to zero.

**Transfer.** If e S(t)≤C t^σ eventually, 1/2<σ<1, the tree of 368 applied to e S^* leaves large leaves bounded by C(x/D)^σ; for the small ones the same bound holds in modulus by the Gaussian decay, even when the final cut is inherited. The constant of the small leaves is uniform in the cut: it suffices to replace their coefficients by 1 and use that the Gaussian sum is O_(σ,t₀)(t^σ) for 0<t≤t₀. The uniqueness of the product D in the tree and its positive weights give uniformly for (log x)²≤z≤4(log x)² the ceiling C' x^σ E_z(σ)=x^(σ+o(1)). The sum over the possibly infinitely many small leaves converges absolutely by E_z(σ)<∞. Indeed log E≪z^(1−σ)log z=o(log x).

Freeze z=2v², v=log x, and apply the convolution of 368 with variance av−1. For |u−v|≤v/5 the ceiling at scale e^u costs, after denormalizing, at most exp(v[σ+η+a(σ+η−1/2)²/2]) by the exponential moment of the normal, for each fixed η>0 and large v. On the complement the absolute tail control of 368 is used for a small enough. Explicitly |S^*(e^u;z)|≪e^u for all u by summing over all integers by dyadic intervals and using the Gaussian. After convolving the normalized observable and denormalizing the result, the tail costs O(exp(v[1+a/8]) P(|N((av−1)/2,av−1)|>v/5)). Its upper exponent is

    1+a/8−(1/5−a/2)²/(2a)+o(1),

which is negative for a small enough, for example 0<a<1/1000.

Choose a zero ρ with β>σ. As a→0, Re Φ_a(ρ)→β, while σ+a(σ−1/2)²/2→σ. Fix a small and then η small to keep a strict separation. The excursions of both signs of the unlabelled diffusive average, proved at the end of 368 by the computation of 365, contradict that ceiling. This proves the lower bound for each sign, even if Θ=1 or the supremum is not attained.

**Upper bound.** For Θ<σ<1, shift the fixed Mellin integral of 368 to Re s=σ. There |E_z(s)|≤exp(o(log x)); 1/ζ has uniform polynomial growth in the band between σ and 2. For this last fact apply Borel–Carathéodory to log ζ on discs centered at 2+it of outer radius 2−(Θ+σ)/2 and inner radius 2−σ, at heights |t|≥4: the real part is bounded by O(log(2+|t|)) by polynomial growth of ζ and the central value is bounded. On the remaining compact set 1/ζ is regular. The Gaussian makes the integral converge and kills the horizontals, whence |S(x)|≤x^(σ+o(1)). For Θ=1 the previous absolute control suffices. This concludes the identity.

The formula quantifies the obstruction if RH fails. It leaves pending a one-sided arithmetic bound of exponent 1/2+o(1) at this cut. The independent review also checked the Borel–Carathéodory radii and the separation of exponents when choosing first a and then η. It is not required that Θ be attained nor that the zeros be simple.
