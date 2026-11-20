# Local cost of majorizing the prime weight via positive counts of multiples

To use divisibility of factorials in 092, consider h(t)=∫_[1,∞) floor(t/u)dν(u), with ν a locally finite positive measure, and require h(t)≥log t only for 1≤t≤4. Even on this short band there is a fixed loss:

    ∫₁⁴ [h(t)−log t] dt/t² ≥ (5/6)log(6/5)(1/3−5/16)>0.

Indeed G(t)=ν([1,t]) is increasing and h(t)=Σ_{n≤t}G(t/n). For 3≤t<4 the finite inversion gives G(t)=h(t)−h(t/2)−h(t/3). The same combination applied to log is log(6/t), decreasing. Write E=h−log, r=6t/5 and compare G(r)≥G(t) on 3≤t≤16/5. One gets E(r)+E(t/2)+E(t/3)≥log(6/5), removing from the left side of the comparison the terms with negative sign by means of E≥0. Integrate in dt/t²: after the three changes of variable the bands are disjoint inside [1,4] and the factors are respectively 6/5,1/2,1/3. This gives the bound.

For any fixed mixture of that type, by PNT and Riemann sums (h monotone and bounded on the band), the weighted excess Σ_{x/4≤p≤x} log p E(x/p) divided by x tends to the indicated integral. Hence even restricted to the large primes that majorization pays order x, against the square-root margin of 092. The asymptotic statement here is only used for a fixed mixture. The argument does not treat combinations with signed coefficients nor compensations between bands. In 045–047 dilations are already inverted via Möbius; here the quantitative obstacle uses only the indices 1,2,3 without asymptotic behaviour of Möbius.
