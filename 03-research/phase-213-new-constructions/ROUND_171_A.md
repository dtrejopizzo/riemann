# Radius of the certificate and displacement of a finite list

Fix T>0, distinct real frequencies γ_j with symmetric multiplicities m_j>0, and displacements 0≤δ_j≤Δ=max δ_j, also symmetric. The local datum is
    g(u)=Σ_j m_j exp(iγ_j u)cosh(δ_j u).
For small Δ and large L, the infimum of the negative mass of the certificates with profile w flat on [−2T,2T] and support [−L,L] satisfies
    c(Z,T)(L^(−2)+Δ²) ≤ inf ν⁻(ℝ) ≤ C(T)(Σ_j m_j)(L^(−2)+Δ²),
with transform of ν equal to wg. For the lower bound the multiplicities and frequencies are fixed; the constants are uniform as all the displacements vary. It also allows multiplicities to be split into several terms of integer mass at the same frequency. The case Δ=0 is 170. In particular the cost of an isolated quartet at distance δ is comparable to L^(−2)+δ².

**Common curvature.** With a and P of 170, let H(t)=|P(exp(it))|² on the real axis, continued as an entire trigonometric polynomial through P(exp(it)) and its reflected conjugate factor. At each θ_j=aγ_j there is a double root with H''(θ_j)>0, because the root of P is simple. For every admissible signed extension, by its moments on the window,
    ∫H(aτ)dν(τ)=Σ_j m_j Re H(θ_j+i aδ_j)
                 =−(a²/2)Σ_j m_j δ_j² H''(θ_j)+O_Z(Σ_j m_j δ_j⁴).
The error is uniform in the box of small displacements; the symmetric datum removes the odd part. Since H≥0 on the real axis, this implies ν⁻(ℝ)≥c_Z Σ m_jδ_j² and in particular ≥c Δ². The common sign of the curvatures prevents several displacements from hiding one another in this finite proof.

**Recovering the radius cost.** Let g₀ be the same datum without displacements and χ an even smooth function of fixed support, equal to one on the window. Correcting the transform by χ(g₀−g) has L¹ norm in the spectral variable O_(Z,T)(Δ²), by Taylor and two integrations by parts on fixed support. One obtains an extension of g₀, still of radius L. The general lower bound of 170 gives ν⁻≥c₁ L^(−2)−C₁Δ². Combining with ν⁻≥c₂Δ² proves the joint lower bound even when the two scales are comparable.

**Upper bound valid for the whole list.** Use the autocorrelation b and the cutoff χ of 170. Let h(u)=b(u/L)/cosh(Δu) and put w=h+χ(1−h). For each |d|≤Δ the quotient cosh(du)/cosh(Δu) is positive definite. For Δ>0 and |d|<Δ, its inverse transform is the real part of a positive constant times sech(π(τ+id)/(2Δ)), applying the transform of sech to the factors exp(±du). That real part is positive by cos(πd/(2Δ))>0. At the boundary the quotient is one; for Δ=0 apply 170 directly. By products and translations hg has nonnegative measure. On fixed support, χ(1−h) and its first two derivatives are O_T(L^(−2)+Δ²). Multiplying by cosh(δ_j u) before translating keeps this bound for bounded Δ. Hence the L¹ norm of the whole correction is ≤C(T)Σ m_j (L^(−2)+Δ²), independently of the height or separation of the frequencies. This gives the upper bound.

**Cross-check.** R7-01 already studied the quadratic negative curvature of an off-line quartet, and the route G7E already contains the Poisson tool on a band. Here they are combined with the finZ rate of 170 for the variational problem of negative mass, with a common profile for distinct displacements and constants uniform in the radius and the displacements. The frequencies are fixed before the limit. The lower bound loses control with the separation and the upper bound grows with the total mass; neither allows simply passing to the infinite spectrum of paper 47.
