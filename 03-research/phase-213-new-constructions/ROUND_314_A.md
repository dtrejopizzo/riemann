# Simultaneous sign on the full space of divisor coefficients

Keep t, θ, A, φ, δ and D of 313. For each real vector λ=(λ₁,…,λ_D) form w_λ(n)=τ(n)(Σ_(d|n,d≤D) λ_d)². Convolve with the coefficients of the same positive filter P^m of 313, taking K sufficiently large **once and for all**, independently of λ. Denote by v_λ the resulting weights. The quadratic form

    Q_x(λ)=∫ φ(u) Σ_(n≤X) v_λ(n) B_t(X/n) du,    X=x(1+δu),

satisfies, for all sufficiently large x and simultaneously for all λ,

    Q_x(λ) ≤ −c_t √x L^(−3/2) D^(−10) ||λ||∞².

In particular the matrix of this average is negative definite in dimension D, including the indices that have repeated prime factors. All filter parameters are frozen at the center x of the window. The gap of 310 is a property of the specific vector λ_d=μ(d); the matrix statement allows all vectors.

**Exact multiplier.** The series of w_λ is ζ(s)²h_λ(s), where the pair d,k contributes λ_dλ_k times the product, over the p^e exactly dividing l=lcm(d,k), of the factors p^(−es)[1+e(1−p^(−s))]. This is obtained by summing the factor of τ from exponent e onwards. The support of the multiplier lies in l rad(l)≤D⁴. Normalize ||λ||∞=1. On Re s=1/2 its absolute norm is ≤D⁶: each product of local norms is ≤∏(1+2e)≤l², and there are D² pairs. Moving v to the left costs at most another D^(4v).

**Floor valid for the whole space.** For real s between 1/3 and 1/2 take independent valuations with tail probabilities q_p(e)=p^(−es)[1+e(1−p^(−s))], q_p(0)=1. These are the tails of the mass distribution (j+1)(1−p^(−s))²p^(−js) in j. Let I_e be the indicator that the valuation at p is at least e. Write Z₀=1 and Z_e=I_e−r_e I_(e−1) with r_e=q_p(e)/q_p(e−1) for e>0. For the same p they are orthogonal because the events are nested, with squared norm q_p(e)(1−r_e). By independence, the products Z_d over the primes and exponents of d are also orthogonal. If q(d)=∏q_p(e), the telescoping identity I_e=Σ_(j≤e)q_p(e)Z_j/q_p(j) gives

    Σ_(k≤D) λ_k I_(k divides) = Σ_(d≤D) b_d Z_d,
    b_d = Σ_(d|k,k≤D) λ_k q(k)/q(d).

Here I_(k divides) is the product of the indicators of k. The second moment of this polynomial is h_λ(s), since the joint probability for two indices is q(lcm(d,k)). By upward Möbius inversion, λ_d=Σ_(d|k,k≤D)μ(k/d)b_k q(k)/q(d), hence max|b_k|≥1/D. Moreover r_e decreases with e, so 1−r_e≥1−r₁=(1−p^(−s))²≥(1−2^(−1/3))²>1/32. From q_p(e)≥p^(−e/2) it follows that q_p(e)(1−r_e)≥p^(−8e). Consequently ||Z_d||²≥d^(−8) and the orthogonal sum of squares gives h_λ(s)≥D^(−10). Qualitative positivity for fixed vectors does not suffice, because the dimension increases with x.

**Uniform comparison of the cuts.** Repeat the contour of 313 with the new multiplier. On the real cut the whole jump integrand keeps its orientation and 0<v<1/L gives a modulus ≫_t √x L^(−3/2)D^(−10). On the complex cuts replace D² by D⁶ in 313. With K>20/(1−2θ) the factor (C_t(m+2)log(C_t D)/L)^m costs D^(−K(1−2θ)+o(1)), enough for both cuts to be of smaller order than the real floor. On the left edge exp(−cL/log D) dominates every fixed power of D; on the horizontal edges and in the tail raise the fixed order of integration by parts to gain D^(−10) as well. All errors are uniform in the normalized vector. This proves the inequality by homogeneity.

The result concerns the dilation matrix of the smoothed arithmetic average. The simultaneous negativity allows testing any combination of divisors up to D, but extracting B_t(x) still requires controlling the higher indices that enter each combination.
