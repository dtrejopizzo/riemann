# Regularity of minimizers and a power modulus for the full floor

For any compact J⊂(0,∞), any 0<s<1/2 and every normalized full minimizer F on I_T=[−T,T], T∈J, its extension by zero satisfies ||F||_{H^s(ℝ)}≤C(J,s). In particular, for each 0<α<1,
    
    |λ_W(T')−λ_W(T)| ≤ C(J,α)|T'−T|^α,     T,T'∈J.

Lemma contT of paper 46 obtains a logarithmic modulus by controlling the whole form domain. Here it suffices to control the minimizers at the two endpoints, and the equation outside the interval supplies the additional regularity. We work with the full form, without imposing the primitive moments.

**Equation on both sides of the boundary.** Let P be multiplication by 1_{I_T}, m(D) the archimedean multiplier of P46. Inside the interval, the minimum satisfies m(D)F=λ_W F minus the contributions of the prime translations and of the bounded finite-rank polar operator, by the weak equation against compact tests in the interior. These contributions, restricted with P and extended by zero, are uniformly bounded operators on L² and on H^s for T∈J. Indeed the translations are isometries and there is a common finite list; the polar profiles are smooth exponentials on a common compact set restricted with P. We use the classical Sobolev multiplier theorem: the indicator of a half-line acts boundedly on H^s(ℝ) for |s|<1/2 (equivalently the fractional Hardy inequality on the line). For intervals subtract two half-lines, with bounds independent of their endpoints. λ_W is bounded on J by contT and minima exist by compactness.

Outside, the Lévy kernel of P46 gives
     
    m(D)F(x)=−(1/2)∫_{I_T} K(|x−y|)F(y)dy,   K(u)=2e^(−u/2)/(1−e^(−2u)).

The exterior identity is proved against tests separated from the interval using the Lévy formula; only the cross term intervenes. For the right side translate to the endpoint and reflect the interior variable. The two distances to the endpoint are positive and the kernel becomes K(v+w). The same holds at the other endpoint. We show that this crossing operator extended by zero is bounded on H^s and L². Decompose K(u)=e^(−u)/u+R(u). R and its first derivative are bounded down to zero by Taylor and decay exponentially at infinity. The kernel R(v+w) and its first derivative in v are Hilbert–Schmidt on the half-lines, by integrating u|R^{(i)}(u)|². The output lies in H¹ of the half-line; reflect to extend it and apply the indicator to get the bound in H^s.

For the singular term multiply on each side by e^(−v) or e^(−w) (use bounded Lipschitz extensions). The remaining operator is Carleman's. For f supported on the positive half-line its output extended by zero is
    
    ∫₀^∞ f(tv) dt/(1+t),    v∈ℝ.

The L² norm of the dilation is t^(−1/2)||f||₂ and the homogeneous H^s seminorm is t^(s−1/2)||f||_{Ḣ^s}. Both factors are integrable against dt/(1+t) for 0≤s<1/2. Translations, reflections and the initial restrictions do not affect uniformity.

Combining interior and exterior gives m(D)F=B_T F on the line, with B_T bounded on both spaces, uniformly in T∈J. To define B_T on arbitrary inputs, first project by P; build the two outputs above and add. No Sobolev regularity of F has been assumed in advance: the identity is first verified in L² on the three open sets. The distributional difference is supported at the two endpoints and belongs to H^(−ε) for every ε>0, since m has logarithmic growth. No nonzero combination of deltas and their derivatives belongs to H^(−ε) for ε<1/2. This eliminates possible boundary contributions.

**Regularity gain.** Let Q be the Fourier projection onto |ξ|>N and A the multiplier Q/m, defined as zero on |ξ|≤N. Since m(ξ)→+∞, choose N fixed on J such that ||AB_T||<1/2 both in L² and in H^s. The equation is F=(1−Q)F+AB_T F. The first term has H^s norm ≤(1+N²)^(s/2) and the Neumann series converges in both spaces to the same F by uniqueness in L². This proves the regularity statement even across the prime contacts.

**From the minimizer to the floor.** Dilate a unit minimizer from T to T'=rT. In the proof of contT the change of the archimedean part and that of the polar term are O_J(|r−1|) for r close to 1. For the comb, |e^{iu}−1|≤2|u|^(2s) gives an error O_{J,s}(|r−1|^(2s)||F||²_{H^s}) on the common list of translations, including those entering at the boundary. By the variational principle this bounds λ_W(T')−λ_W(T). Exchanging T,T' with the other minimizer gives the two-sided estimate; distant pairs are covered by boundedness of λ_W. Take s=α/2.

**Application and frontier.** If one has λ_W(T₀)≥g>0 and a numerical bound C for this compact set and exponent, it suffices that C|T−T₀|^α<g to transport the strict sign. Neither C nor an additional window has been computed. The certificate of 026 at 1.035 treats the primitive floor. The index already records complete external reproduction at log(11)/2; a qualitative extension by continuity is not new. The contribution here is the modulus for the floor, without extending it to the whole form domain. The constants depend on J and this argument gives no uniform positive margin as T grows.

**Direct antecedent and attribution.** P121_DYADIC_RADICAL_BOOTSTRAP.md already develops the Carleman transmission and the high-frequency inversion to obtain H^s, s<1/2, on finite windows. 106_123_BOUNDED_PRIME_GENERATOR_AND_SECOND_LOG_BOOTSTRAP.md already treats the second logarithmic moment. The regularity part of this note adapts those proofs to the minimum of the full form, with the polar term, and makes the constants uniform as T varies in a compact set. The result to retain is its two-sided application to the modulus of the floor of paper 46; neither mode regularity nor the Carleman method is proposed as a new mechanism.
