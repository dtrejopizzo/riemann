# A regular zero-free product across the line that changes the barycentre

In 251 the removal of primes made the logarithmic derivative of the modifying factor diverge at 1/2. Now multiplicities 0, 1 or 2 on true primes are allowed. There is a fixed choice, identical to the primes up to any prescribed initial prefix, for which the zeta function of the modified product has exactly the same zeros and poles, WITH MULTIPLICITIES, in Re s>1/3. The ratio relative to ζ is holomorphic and never zero there. Even so the modified barycentre oscillates in sign arbitrarily far out, without assuming RH. For the modified primes counting multiplicities,

    C_mod(x)−C(x)=−√x cos(x^(1/24))+o(√x).

**Realisation on integer primes.** Fix large U=m₀³ and w(u)=u^(−5/12)cos(u^(1/24))/1152 for u≥U, zero before. On each [m³,(m+1)³), with left endpoint b, take I=∫w and choose floor(|I|/log b) distinct primes; duplicate them if I>0, remove them if I<0. There are enough by the interval PNT of 238, since the length is comparable to b^(2/3). The number selected is O(b^(1/4)/log b); they can be chosen at equally spaced indices as in 251. Each logarithm differs from log b by O(b^(−1/3)), hence the rounding error in the signed mass of the whole cell is O(log b). On an incomplete cell the error is O(b^(1/4)) by absolute magnitudes. Write e_p for the change of multiplicity. One gets

    Σ_(p≤x)e_p log p = ∫_U^x w(u)du + O(x^(1/3)log x)    (x≥U),
    Σ_(p≤x)|e_p|log p ≪ x^(7/12).

The second bound follows by summing O(m^(3/4)) per cell. The edited primes have index separation tending to infinity, taking, for example, the midpoints of balanced sublists to avoid contact between cells. Thus the asymptotic proportion of counts is also preserved on every moving interval with number of primes tending to infinity.

**Continuation of the factor.** In Re s>1 its negative logarithmic derivative is Σ e_p(log p)/(p^s−1). The exponents ≥2 converge locally absolutely for Re s>7/24 by the absolute bound above. In the first exponent, the transform of the discrepancy between the atoms and w(u)du is holomorphic for Re s>1/3 by partial summation. The transform of w itself extends to an entire function: with v=u^(1/24) one integrates from U^(1/24)>0 a multiple of v^(13−24s)cos v, initially with absolute convergence. Repeated integrations by parts extend the result to each compact, with entire lower boundary terms. Thus the modifying logarithmic derivative is holomorphic in all of Re s>1/3. Taking its primitive with the appropriate sign and exponentiating from s=2 extends the factor itself without zeros or poles, and proves the equality of divisors in that domain.

**Reading the barycentre.** By bounded variation of k from 247, the discrete discrepancy costs O(x^(1/3)log x). With L=x^(1/24), the continuous contribution is the integral against cos v of the polynomial

    g(v)=(24/1152)v^13 k((v/L)^24),   U^(1/24)≤v≤L.

At the moving endpoint g(L)=0 and g'(L)=−L^12. Two integrations by parts contribute g'(L)cos L; a third bounds the remainder by O_U(1+L^11) using |g''(L)| and ∫|g'''|. This gives the announced oscillation. Under RH, |C(x)|≤(4/15+0.094+o(1))√x by 247, so the phases cos L=±1 give opposite signs. If RH fails, the excursions of 249 of order strictly greater than √x survive the modification.

**What the test discriminates.** Regularity of the logarithmic derivative on the boundary, even simultaneously at all heights, does not now distinguish the two systems by their singularities. The explicit formula of 247 also uses estimates on contours that allow the observable to be represented by the residues and a small remainder. Here the holomorphic factor by itself contributes an oscillation of order √x to that same reading. Neither the functional equation nor the vertical estimates of ζ are attributed to the modified system. R163_102 already treats stability of zeros under edits; 251 already exhibits inversion by deletion. The additional step is to realise the oscillating term through atoms on primes while preserving the divisor across the whole critical line.
