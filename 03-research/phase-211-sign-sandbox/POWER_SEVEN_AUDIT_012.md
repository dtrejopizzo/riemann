# POWER_SEVEN_AUDIT_012 — Review of the global sign at seven poles

Status: PROVED. POWER_SEVEN_GLOBAL_012.md and tools/power_seven_global_012_verify.py reviewed from the formulas; script run independently with PASS. Papers untouched.

## 1. Confluent matrix

The AP bands and their factors coincide with the kernel and the Laguerre transformations previously audited. The compact formula psi^(r)*u^r/(2r!) used by the program is exactly equivalent to g^(r)*(2u)^r/r!, it does not lose a power of two. The sums16..2000 and integral tails from2001/2000 have correct sign and order. The seven interval eliminations of AP-.069I have positive lower pivots and keep the pivot columns intact. The certificate decides the whole block.

The moment norms AA,BB use seven terms and the check4AA BB<1 suffices for the polar bound employed. That comparison is not extrapolated from a lower degree.

## 2. Product of deficits, not product of independent maxima

The196 panels of length1/4 cover exactly[0,49]. On each, c-ell(x) decreases while the filter polynomial increases. The maximum of the PRODUCT is therefore bounded by the first factor at the left endpoint, truncated to positive, and the second at the right endpoint. This justifies DIRECT on each full interval. The lower bound49>.05>.01 and the monotonicity of m control the whole exterior.

The integral loss is<.057R0N0, without needing a factor x or a separate bound K_n. The filter still has Bernoulli polar factor7/(4u²), with the correct orientation. The bracket .069-.01-.057-7/(4u²) is positive; its slack is small but checked rationally. From this one obtains AP>.01I at all seven poles>=u, keeping the new norm in the identity.

## 3. Weighted trace and factors of the tail

The trace lemma of POWER_COMMON_TRANSFER_010§6 was reviewed in its telescoping, positive decreasing inverse kernel and Laguerre connection. Its hypothesis sigma21<min v_j is satisfied. The exact confluent trace T7=176673441 and2sqrt(T7)<26600 are checked. Only operatornorm<=trace is used; monotonicity of the largest eigenvalue of the Gram is not assumed.

The correlation loses q^-21 and the comb coefficient adds q^-1/2, so the exponent is21.5. The additional factor1/sqrt(q)<=1/sqrt2<5/7 is kept by the rational comparison(7/5)^2<2. Summing logq*q^-21 gives exactly the majorant2^-21[.7+1.4/20+2/20²]=31/(40*2^21). Thus the infinite cost is<1/125, with all contacts and without matrix sign hypotheses.

It concludes W>.01I-.008I=.002I=1/500 I on all declared spaces, even repeated or arbitrarily separated poles. Nothing in this certificate implies the result for eight poles or all degrees.
