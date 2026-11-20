# Divisorial minorization of the weight of 039

Write w(t)=min(t,t⁻²). Then Q(x)=x⁻¹ᐟ²ΣΛ(n)w(n/x). The proposed operation is to minorize w by Df(t)=Σ_{m≥1}f(mt). With absolute convergence the identity Σ_{d|k}Λ(d)=log k turns the pairing with Df into a single sum against log k. Cross-check: N_BUILD022_MATRIX_IDENTITY_FOR_X_M, 212-58/76 and G1_B9_R2 §5 already use the divisorial transformation. Here one checks the possibility that a fixed minorant pays the complete main term of 039.

**A nonnegative profile does not work.** If f≥0 and Df(t)≤w(t) for all t>0, then for y>0 and every integer k one has f(y)≤Df(y/k)≤y/k. Hence f is identically zero. It even suffices to require the minorant at the samples n/x with n=2 and x=j⁴ to exclude every fixed continuous nonnegative f: choose m_j the integer nearest to yj⁴/2. One has f(2m_j/j⁴)≤Df(2/j⁴)≤2/j⁴ and passing to the limit gives f(y)=0. So for this discard it is not necessary to presuppose the comparison between the samples of interest.

**Compact signed profile.** Suppose f continuous real supported on [α,b]⊂(0,∞), with zero integral and Df≤w on the whole half-line. Integrating from ε>0,
    
    ∫_ε^∞ Df(t)dt = ∫ f(u) H_floor(u/ε) du → ∫ log(u) f(u)du,

where H_n is the harmonic sum. The limit follows from the expansion H_n=log n+γ_E+O(1/n), uniform on the support after subtracting the constant using ∫f=0. The positive part of Df is integrable by the minorant, hence so is the negative part by the finite limit. Since Df=0 beyond b, the integral deficit is at least ∫_b^∞w>0. In particular no fixed choice of this type reaches the mass 3/2.

The deficit is also seen directly in the true prime weights, without assuming a quadrature theorem for Df near zero. Fix B>max(b,1). The contacts with Bx<n≤2Bx alone contribute to the cost of the minorization at least

    x^(−1/2) Σ_{Bx<n≤2Bx} Λ(n) w(n/x) ≥ [ψ(2Bx)−ψ(Bx)]/(4B²√x) ∼ √x/(4B).

The total cost may be larger. This loss of order √x prevents obtaining the additive precision O(1) of Q from the minorant alone. Letting the support grow with x or evaluating the remainder separately changes that conclusion.

**Exact inverse.** For t>0, f(t)=Σ_{m≥1}μ(m)w(mt) satisfies Df=w by Möbius inversion. The double sums converge absolutely for fixed t: up to finitely many products the majorant is t⁻²Σ_{m,k}(mk)⁻². For t≥1 the inverse equals t⁻²/ζ(2); for t=1/2 it equals 4/ζ(2)−7/2<0. The exact transfer reintroduces signed Möbius weights. The index already records that family of inversions; no sign route is opened from the change of coefficients.

**Decision.** Discarded: the fixed nonnegative minorant (even if required only at the original samples), and the signed minorant of fixed support that aims to supply the bound without estimating the remainder. No obstruction is deduced for other divisor identities. The uniform inequality of 039 remains open.
