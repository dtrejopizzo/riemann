# A single sample per order, without exceptional orders

In 215 one sample D_k per square order detected failure of the sign with a limsup, since several zeros of extreme angle could cancel their phases for some k. The quadratic over a band solved that cancellation by integrating in frequency. Here a single LINEAR integral over rates suffices for EACH k. Changing the real part of the Mellin exponent allows a single complex point to be isolated even if several share the extreme angle.

Let N=k², s_k=−√k+ik and

    C_k=∫₃ᴺ A_N(u) u^(s_k−1)du.

For k→∞ one has lim log(1+|C_k|)/k=Θ. Under RH, C_k→0. If Θ>0, let w₀ be the point of smallest modulus r₀ among the w of 214 with arg w=−Θ, and m₀ its multiplicity (including coincidences of w). Then

    C_k=−(1+o(1)) · m₀ K_N(s_k) w₀^(s_k)/2,
    log |C_k| = Θk − (log r₀)√k − log k + log(m₀√π/2) − 1/4 + o(1).

In particular there is detection along every unbounded subsequence. Even r₀ is determined by the second term of the growth. The parameters of the prime test use neither Θ nor r₀.

**One dominant point.** For each large k, the beta identity of 214 extends to s_k: −2N<Re s_k<−1, which ensures integrability at zero and summability in height by Z3. In Z(s_k) the term w₀^(s_k) has modulus exp(kΘ)r₀^(−√k). There is only a finite number of w with arg w=−Θ, with repeated ones grouped by multiplicity. Each other one of that angle has strictly larger modulus and contributes a fraction O(exp(−c√k)). For the rest, the angular separation η>0 of 215 gives a total O(exp(k(Θ−η))Σ|w|^(−√k)), negligible relative to the dominant one, since Σ|w|^(−√k) is bounded by Z3 for k≥4. This proves a complex equivalence, not just a modulus bound. If Θ=0, instead |Z(s_k)|≤Σ|w|^(−√k)=o(1).

**Beta factor.** With z=s_k/2, the symmetric Stirling expansion in N±z gives log(K_N(s_k)/K_N(0))=z²/N+o(1) since |z|=O(√N). This is obtained by Taylor expansion of (N+z−1/2)log(N+z) in z/N, with the linear term cancelled and remainder O(|z|³/N²+|z|²/N²+1/N). Since z²/N→−1/4 and K_N(0)∼√(π/N), one obtains K_N(s_k)=(1+o(1))√π exp(−1/4)/k.

**Passage to primes.** The Mellin identity uses all u>0. On [3,N] the difference b_N+2A_N has modulus ≤Cu log(2u) by 210. Its integral against u^(−√k−1) is o(1). For u>N, the envelope Cu log(2u) exp(CN/u²) of 214 likewise gives o(1). For 0<u≤3 the estimate must be redone because the weight varies: by |γ|>14 and |δ|≤1/2 one has |h_u|≤5u²/γ² (use |u²+w²|≥Re(u²+w²)≥γ²−1/4). Hence Σ|h_u|^N≤C u²(5u²/196)^(N−1) by Σγ⁻²<∞. Integrating against u^(−√k−1) gives O(3^(2−√k)(45/196)^(N−1)/(2N−√k)). It follows that 2C_k=−K_N(s_k)Z(s_k)+o(1). Off RH the magnitude of the main term diverges, so the additive error gives relative error o(1), included in the logarithm.

**Arithmetic obligation.** A bound |C_k|≤exp(o(k)) along SOME subsequence suffices. Compared with the linear variant of 215, the need to estimate all large k is eliminated. The new weight concentrates smaller rates, at cost exp(−O(√k)) for each fixed rate; that cost leaves visible the signal exp(Θk) of any fixed counterexample. It is not deduced that the term-by-term absolute value over the primes suffices: the loss exp(c k²) of 216 lives in a layer u−3 of width comparable to 1/k² where this weight only pays exp(−O(√k)).
