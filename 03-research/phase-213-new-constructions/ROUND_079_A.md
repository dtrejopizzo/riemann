# Uniform bound on the cross block and explicit enclosure of the full minimum

On a fixed window, divide I_T into N equal cells of length h. Let λ_h be the minimum of the matrix of 078 in the basis of normalized indicators. Define
     
    b_T=Σ_{2≤n<exp(2T)} v_n + 4 sinh T,
    d=m(π/h)−b_T,    B=45+b_T.

Then, on the whole full form,
     
    (λ_h+d−√((d−λ_h)²+4B²))/2 ≤ λ_W(T) ≤ λ_h.

The crossing constant does not grow with N. In particular, if d>0 and λ_h>B²/d, a strict sign is certified. For any fixed T with λ_W(T)>0 the condition holds from some sufficiently fine refinement on. It does not require a Sobolev constant estimated on the minimizer.

**Archimedean crossing.** Extend the mesh to the whole line, let P be its projector by means and Q=1−P. By translation take the origin at an endpoint. Cellwise constant functions have transform equal to the transform of the indicator of one cell multiplied by a periodic function of period 2π/h. By Plancherel, grouping ξ=(θ+2πk)/h, −π≤θ≤π, this identifies P on each ℓ² fiber with the projection onto a line whose unit vector has weights of squared modulus
     
    w_k=(2 sin(θ/2)/(θ+2πk))²,     Σ_k w_k=1.

The normalization follows from Parseval for the Fourier coefficients of exp(iθt) on [0,1]. m(D) is diagonal on the fiber. The squared norm of its crossing from that line to its orthogonal complement is the weighted variance of the values m((θ+2πk)/h). It can be majorized by taking the value at k=0 as the center. This estimate also justifies the identity first on inputs of finite support in cells (their logarithmic jumps are in L²); the crossing so bounded extends.

For M₁=sup |t m'(t)|, M₁≤10. From 078, t m'(t)=Σ 4t²c_j/(c_j²+t²)² ≤Σ 4t²/(c_j²+t²)^(3/2), c_j=1/2+2j. The first summand is ≤8 and the rest is bounded by half the integral of the decreasing function over c≥0, equal to 2. For k≠0 and r=|θ|/π≤1, w_k≤r²/k², and the ratio |θ+2πk|/|θ| lies between 1 and 3|k|/r. Thus the modulus of the crossing is bounded by
     
    M₁ [2Σ_{k≥1}(log(3k)+1/e)²/k²]^(1/2) < 45.

Indeed r log(1/r)≤1/e; for a=log3+1/e, the sum of (log k+a)²/k² is ≤a²+∫₁^∞(log t+a)²/t² dt=2a²+2a+2<10. The point θ=0 is irrelevant. Restriction to I_T does not increase the crossing: the support projector commutes with P because the window is a union of cells. The prime and polar part has norm at most b_T by P47. The stated bound B follows.

**Passage to the full form.** Decompose F=u+v into means and the complement of means inside I_T. From 078, W(v)≥d||v||², while W(u)≥λ_h||u||². The crossing bound gives the term −2B||u||||v||. Minimizing the scalar matrix of order two proves the enclosure. If d>λ_h, the width is at most B²/(d−λ_h). For a fixed window, d→∞ and λ_h stays uniformly bounded above by testing the constant on the whole window. Thus the enclosure converges, although the cost of achieving very large d may be prohibitive. The bound of 078 via regularity has a better asymptotic rate, but carried an unevaluated constant.

**Cross-check.** The Schur method and the control of complements already appear in P47 and 026. The new comparison against 078 is the control of the crossing by an explicit variance on the fibers of the mesh, with a bound independent of refinement. It is a sufficient certificate on each window: λ_h>B²/d has not been proved for a family of windows tending to infinity, nor has a new numerical certificate been run.
