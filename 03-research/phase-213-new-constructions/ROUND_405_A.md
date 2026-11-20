# How much the Euler product loses at the verified and higher heights

**Status: PROVED, with independent review of the cells, the short PNT and the use of the verified height.**

Let G≥2 be fixed such that all zeros with |γ|≤G+1 are verified on the critical line (for example G=10^6 with the data of 175). In 404 one can take any constant

    0<η<1−1/(2G)

in the threshold β−γ²/(2L)>α+δ+η/b. The saving of the eliminated group remains O(T₀ exp(−c L/b)), with c depending on the chosen margin. The effect comes from an oscillatory estimate of the product, not from a new verification of zeros.

**Uniform approximation by a short integral on the logarithmic scale.** For α≤σ≤1+1/L, G≤|t|≤2√L+1, one has

    log|E_z(σ+it)| ≤ [1/(2|t|)+o(1)] L/b

with additive error uniform in both variables. The second and higher powers cost O(b) since α≥1/2. For the first ones, set P=z^(9/10): the range p≤P costs O(z^(0.45)) by summing even over integers. On [P,z] replace the primes by dq/log q. Indeed, divide into cells of logarithmic length Δ comparable to 1/(b(1+|t|)), adjusting all cells to reach both endpoints. The phase and the relative weight vary by O(1/b) in each cell. If the cell starts at q, its ordinary length is ≍qΔ≫q^0.70, since |t|≤O(z^(1/4)) and q≥z^0.9. The short PNT used in 367 (exponent 17/30 plus margin) gives a uniform relative count 1+o(1) there; it is applied to complete cells, without requiring cancellation of their errors. The total error is o(L/b), since the absolute mass of the integral for σ≥α is bounded by (1+o(1))L/b. [Guth and Maynard, corollary 1.3](https://arxiv.org/abs/2405.20552)

With w=1−σ−it and v=log q the integral is ∫_(0.9b)^b exp(wv)dv/v. Integrate by parts with primitive exp(wv)/w. The upper boundary costs at most z^(1−α)/(|t|b)=(1/2+o(1))L/(|t|b). The lower one is O(z^0.45/(|t|b)); the rest is O(L/(|t|b²)), dominating exp((1−σ)v) by exp((1−α)v). This proves the estimate.

**Application to the contour.** In 404 use the common vertical segment up to |t|=G and place the connectors there. The compact set of the connector stays at distance ≳1/b from the verified zeros on the line, even if its endpoint has the ordinate of a zero. On the new wings, including the connector, the logarithmic cost relative to x^α is ≤δL+ηL/b+O(1), after the Gaussian; the cost of the product is ≤(1/(2G)+o(1))L/b. The real product at the saddle point contributes (1+o(1))L/b. The strict margin absorbs the length, √K'' and the reciprocal of ζ on safe edges as in 403–404. The same argument controls the old vertical wings. No poles between 1 and G are lost because σ₀>1/2. For example G=10^6 allows η=0.999999. There is no claim with η=1 nor with a uniform relative error as G varies. The group exceeding the parabola still has no one-sided bound.

**Review record.** The smallest cell length is q/[O(b)z^(1/4)] with q≥z^(9/10), hence it is at least q^(13/18)/O(b)≫q^0.70. The [corollary1.3 of Guth–Maynard](https://arxiv.org/html/2405.20552v1) uses the range q^(17/30+ε)≤length≤q^0.99; for example ε=1/10 leaves threshold2/3<0.70. If a cell exceeds q^0.99 it is subdivided into pieces of lengths between q^0.70 and q^0.90 and their positive counts are combined. The adjusted logarithmic mesh has all its cells comparable toΔ, without a short terminal remainder. The variation of phase and weight contributes O(1/b) relative to the absolute mass and the PNT contributes o(1), uniformly; when summing this error is not multiplied by the number of cells. The subsequent integration by parts gives a uniform additive erroro(L/b), not an error relative to1/|t| as t grows.

The verified hypothesis covers G+1, which protects the connectors and the neighboring zeros. The example G=10^6 is far below3·10^12, the verified height of [Platt–Trudgian](https://arxiv.org/abs/2004.09765) used asZ2 in175. G is fixed before letting x→∞. The available margin is exactly1−η−1/(2G)>0, and allows choosing the exponential saving after fixingη andG; one does not pass to the endpointη=1 nor to variableG.
