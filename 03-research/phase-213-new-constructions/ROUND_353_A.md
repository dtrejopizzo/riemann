# The higher prime powers consume at most half of the critical norm

Use the indicator window S_h(x)=Σ_{xe^(−h)<n≤x} μ(n), 0<h≤1. Write ‖·‖_X for L²([X,2X],dx/x). Define the contribution of simple primes

    P_h(x)=Σ_p (log p) S_h(x/p).

RH is equivalent to ‖P_h‖_X ≪_ε √(hX) X^ε log(2X) for each ε>0, all X≥2 and every indicated width. The reduction comes from a contraction of the higher powers at root scale. No absolute value is taken inside P_h.

**Identity for the pulse.** From μ(n)log n=−(μ*Λ)(n), separating k=1 and applying the identity log n=log x−h+∫_0^h 1_{n>xe^(−v)}dv for each n of the pulse (except endpoints of measure zero), one gets

    (log x−h)S_h(x)=−P_h(x)−Σ_{p,k≥2}(log p)S_h(x/p^k)−∫_0^h S_v(x)dv.

Define A(X)=sup_{1/2≤Y≤X, 0<h≤1} ‖S_h‖_Y/√(hY). It is finite for bounded X: when h<1/(4X+4) the intervals of x activated by distinct integers up to 2X are disjoint and each has logarithmic measure at most h. The normalized cost of the higher powers in the block X is at most

    A(X/4) Σ_{p^k≤2X,k≥2} (log p)/p^(k/2) ≤ A(X/4) ((log X)/2+O(1)).

Here the classical Mertens formula Σ_{p≤z}log p/p=log z+O(1) is used; the sum over k≥3 converges absolutely. The coefficient 1/2 is that of this majorant, with no claim that it is attained in the norm. The integral of pulses costs at most (2/3)h A(X) after normalizing.

**Absorption.** If the proposed ceiling for P_h holds, apply the identity in each large block Y and divide by log Y−1. For Y≤X one gets a bound C_ε X^ε+(1/2+O(1/log Y))A(X). Choose a fixed Y₀ so that the coefficient is ≤3/4 when Y≥Y₀; the lower blocks cost A(Y₀). Taking the supremum proves A(X)≪_ε X^ε. Conversely, with this ceiling for A, the identity and the same majorants give the proposed bound for P_h.

**Link with the zeros.** Under RH the method of 337 at abscissa σ=1/2+ε' gives ‖S_h‖_X²≪ X^(2σ)h^(1−2γ), using |1/ζ(σ+it)|≪(2+|t|)^γ for any 0<γ<1/2 and the multiplier (1−e^(−hs))/s of modulus O(min(h,1/|t|)). The Plancherel identity with the discontinuous pulse is obtained first with the multiplier smoothed by convolution in log x with a smooth approximate identity, and then by local L² convergence and dominated convergence on the line σ. For h≥1/(4X+4) choose ε',γ arbitrarily small; for smaller h use disjointness, giving ‖S_h‖_X²≪hX. Thus A(X)≪_ε X^ε. Conversely h=1 suffices: by Cauchy–Schwarz and dyadic summation the Mellin transform of the pulse converges holomorphically in Re s>1/2 under that ceiling. It coincides there by continuation with (1−e^(−s))/(sζ(s)) and the numerator never vanishes in that half-plane.

**Scope.** The countermodel 352 breaks the identity μ log=−μ*Λ. With that exact identity the recursive dependence on all powers p^k, k≥2, can be closed in the critical norm. The open task is controlling the signed sum over p at the indicated scale; the result does not grant that control. The logarithmic differentiation identity is classical. What is recorded here is the absorption coefficient and its uniformity for indicator windows of any width.
