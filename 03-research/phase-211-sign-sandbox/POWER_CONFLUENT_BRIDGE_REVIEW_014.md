# POWER_CONFLUENT_BRIDGE_REVIEW_014 — Brief independent review

Status: APPROVED. POWER_CONFLUENT_BRIDGE_014 was reviewed from its formulas; no mathematical correction is required.

1. **Complex convention.** For the usual H¹ product, linear in h and antilinear in the test, the tests y^k e^-ay are real when a>0. Thus J^(k)(a)=0 is exactly their orthogonality, with factor (-1)^k, even though J is continued holomorphically in a bilinear way in z. z must not be conjugated inside J; the text correctly does not do so.

2. **Integration by parts.** h∈H¹ has trace h(0). Its representative is continuous and bounded, and e^-zy h(y) tends to zero for Re z>0. The equality ∫h'e^-zy=−h(0)+zH(z) has the correct signs. Hence J=(1−z²)H+zh(0), and evaluating z=1 forces h(0)=0; no hidden Robin condition remains. Fourier uniqueness on a vertical applies because e^-cy h∈L¹∩L².

3. **Strong norm.** If e^eta y f∈H¹, then f∈H¹ by bounded multiplication. The zero extension to H^s(R),0<s<1/2, admits a jump at0 and is continuous. That norm dominates the logarithmic weight of m. The weight eta>1/2 controls both moments and the infinite comb sum via bilinear estimates. Not only L² density is used.

4. **Passage to the sign.** Positivity of each block implies that of their increasing union. Each translated compact test belongs to the weighted space and is approximated in that strong norm; continuity of the form suffices. No margin uniform in the degree is needed. Translation preserves the complete form, since A and B receive reciprocal factors. Positivity of W is first passed to all tests and window domains; then restricted to the primitive subspace. Primitive approximants are not required in the construction.

5. **Exterior confluence.** The triangular matrix of derivatives of zeta(a)e^(-(a−1/2)y) has diagonal (-1)^k zeta(a), nonzero for a>1. It identifies exactly all confluent degrees without presupposing entrywise positivity.

The sufficiency proved corresponds to ALL complete blocks and cross terms, not to a chain of diagonals nor to families of bounded degree. The current certificates do not complete that obligation.
